#!/usr/bin/env python3
"""
_cdp.py — a tiny, dependency-free Chrome DevTools Protocol client.

The machine has python3 + Google Chrome but no Node, no pip packages
(no websocket-client / selenium / pychrome). So this implements just enough
of the WebSocket protocol (RFC 6455, client side) over a raw socket to drive
headless Chrome via CDP: launch Chrome, open a page target, navigate, and
evaluate JS in the page context (with the profile's cookies, so same-origin
authenticated fetches work).

Used by scripts/capture_canvas.py and scripts/check_reflow.py.
"""
import base64
import json
import os
import re
import signal
import socket
import struct
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]


def find_chrome(explicit=None):
    if explicit:
        if not os.path.exists(explicit):
            raise RuntimeError("Chrome not found at %s" % explicit)
        return explicit
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    raise RuntimeError("No Chrome/Chromium binary found.")


def chrome_user_agent(chrome_path):
    """Build a normal desktop UA matching the installed Chrome major version.

    A consistent, non-"HeadlessChrome" UA across the visible login and the
    headless capture keeps any UA-bound clearance cookies valid."""
    try:
        out = subprocess.run([chrome_path, "--version"], capture_output=True,
                             text=True, timeout=15).stdout
        m = re.search(r"(\d+)\.\d+\.\d+\.\d+", out)
        major = m.group(1) if m else "138"
    except Exception:
        major = "138"
    return ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/%s.0.0.0 Safari/537.36" % major)


def kill_chrome_using_profile(profile_abs):
    """SIGTERM any Chrome already bound to this dedicated profile (releases the
    single-instance lock; lets the profile flush cookies). Safe because the
    profile is dedicated to capture — it is never the user's main Chrome."""
    try:
        out = subprocess.run(["pgrep", "-f", "--user-data-dir=%s" % profile_abs],
                             capture_output=True, text=True).stdout
    except Exception:
        return
    pids = [int(p) for p in out.split() if p.strip().isdigit()]
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    if pids:
        time.sleep(2.0)  # let the profile flush cookies to disk


# ---------------------------------------------------------------- WebSocket
class _WS:
    """Minimal RFC6455 client. Text frames only, with fragment reassembly and
    ping/pong handling. Client frames are masked, as the spec requires."""

    def __init__(self, ws_url, timeout=60):
        assert ws_url.startswith("ws://"), ws_url
        hostport, _, path = ws_url[len("ws://"):].partition("/")
        host, _, port = hostport.partition(":")
        self.sock = socket.create_connection((host, int(port or 80)), timeout=timeout)
        self.sock.settimeout(timeout)
        self.buf = b""
        key = base64.b64encode(os.urandom(16)).decode()
        req = ("GET /%s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\n"
               "Connection: Upgrade\r\nSec-WebSocket-Key: %s\r\n"
               "Sec-WebSocket-Version: 13\r\n\r\n" % (path, hostport, key))
        self.sock.sendall(req.encode())
        resp = b""
        while b"\r\n\r\n" not in resp:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("WS handshake closed early")
            resp += chunk
        if b" 101 " not in resp.split(b"\r\n", 1)[0]:
            raise ConnectionError("WS handshake failed: %s" % resp.split(b"\r\n", 1)[0])
        self.buf = resp.split(b"\r\n\r\n", 1)[1]

    def _read(self, n):
        while len(self.buf) < n:
            chunk = self.sock.recv(1 << 16)
            if not chunk:
                raise ConnectionError("WS closed")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def send(self, text):
        payload = text.encode("utf-8")
        mask = os.urandom(4)
        n = len(payload)
        hdr = bytearray([0x81])  # FIN + opcode text
        if n < 126:
            hdr.append(0x80 | n)
        elif n < (1 << 16):
            hdr.append(0x80 | 126)
            hdr += struct.pack(">H", n)
        else:
            hdr.append(0x80 | 127)
            hdr += struct.pack(">Q", n)
        hdr += mask
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.sock.sendall(bytes(hdr) + masked)

    def recv(self):
        parts = []
        while True:
            b0, b1 = self._read(2)
            fin, opcode = b0 & 0x80, b0 & 0x0F
            masked, ln = b1 & 0x80, b1 & 0x7F
            if ln == 126:
                ln = struct.unpack(">H", self._read(2))[0]
            elif ln == 127:
                ln = struct.unpack(">Q", self._read(8))[0]
            data = self._read(ln) if ln else b""
            if masked:
                mk, data = data[:4], data[4:]
                data = bytes(c ^ mk[i % 4] for i, c in enumerate(data))
            if opcode == 0x8:
                raise ConnectionError("WS closed by peer")
            if opcode == 0x9:  # ping -> pong
                self._pong(data)
                continue
            if opcode == 0xA:  # pong
                continue
            parts.append(data)
            if fin:
                break
        return b"".join(parts).decode("utf-8")

    def _pong(self, data):
        mask = os.urandom(4)
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(data))
        self.sock.sendall(bytes([0x8A, 0x80 | len(data)]) + mask + masked)

    def close(self):
        try:
            self.sock.close()
        except Exception:
            pass


# ---------------------------------------------------------------- Chrome
class Chrome:
    def __init__(self, profile, headless=True, user_agent=None, chrome_path=None,
                 extra_args=()):
        self.chrome_path = find_chrome(chrome_path)
        self.profile = os.path.abspath(profile)
        self.headless = headless
        self.user_agent = user_agent or chrome_user_agent(self.chrome_path)
        self.extra_args = list(extra_args)
        self.proc = None
        self.ws = None
        self._id = 0

    # -- attach to an already-running Chrome (e.g. the visible login window) --
    @classmethod
    def attach(cls, port, chrome_path=None):
        self = cls.__new__(cls)
        self.chrome_path = find_chrome(chrome_path) if chrome_path else None
        self.profile = None
        self.headless = None
        self.user_agent = None
        self.extra_args = []
        self.proc = None
        self.ws = None
        self._id = 0
        ver = json.loads(cls._http("http://127.0.0.1:%d/json/version" % port))
        self.ws = _WS(ver["webSocketDebuggerUrl"])
        return self

    @staticmethod
    def port_alive(port):
        try:
            Chrome._http("http://127.0.0.1:%d/json/version" % port)
            return True
        except Exception:
            return False

    # -- lifecycle --
    def __enter__(self):
        self.launch()
        return self

    def __exit__(self, *a):
        self.close()

    def launch(self):
        kill_chrome_using_profile(self.profile)
        port_file = Path(self.profile) / "DevToolsActivePort"
        if port_file.exists():
            port_file.unlink()
        args = [
            self.chrome_path,
            "--remote-debugging-port=0",
            "--remote-allow-origins=*",
            "--user-data-dir=%s" % self.profile,
            "--user-agent=%s" % self.user_agent,
            "--no-first-run", "--no-default-browser-check",
            "--disable-background-networking", "--disable-extensions",
        ]
        if self.headless:
            args += ["--headless=new", "--disable-gpu", "--hide-scrollbars"]
        args += self.extra_args
        self.proc = subprocess.Popen(args, stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)
        port = self._await_port(port_file)
        ver = json.loads(self._http("http://127.0.0.1:%d/json/version" % port))
        self.ws = _WS(ver["webSocketDebuggerUrl"])
        return self

    def _await_port(self, port_file, timeout=20):
        deadline = time.time() + timeout
        while time.time() < deadline:
            if port_file.exists():
                txt = port_file.read_text().splitlines()
                if txt and txt[0].strip().isdigit():
                    return int(txt[0].strip())
            if self.proc.poll() is not None:
                raise RuntimeError("Chrome exited during startup (code %s)."
                                   % self.proc.returncode)
            time.sleep(0.1)
        raise RuntimeError("Chrome DevTools port not ready within %ss" % timeout)

    @staticmethod
    def _http(url):
        with urllib.request.urlopen(url, timeout=10) as r:
            return r.read().decode()

    # -- CDP --
    def call(self, method, params=None, session_id=None, timeout=60):
        self._id += 1
        msg = {"id": self._id, "method": method, "params": params or {}}
        if session_id:
            msg["sessionId"] = session_id
        self.ws.send(json.dumps(msg))
        while True:
            data = json.loads(self.ws.recv())
            if data.get("id") == self._id:
                if "error" in data:
                    raise RuntimeError("CDP %s error: %s" % (method, data["error"]))
                return data.get("result", {})
            # ignore events / other sessions' traffic

    def new_page(self, url="about:blank"):
        tid = self.call("Target.createTarget", {"url": url})["targetId"]
        sid = self.call("Target.attachToTarget",
                        {"targetId": tid, "flatten": True})["sessionId"]
        page = Page(self, sid, tid)
        page.call("Page.enable")
        page.call("Runtime.enable")
        return page

    def close(self):
        try:
            if self.ws:
                self.call("Browser.close")
        except Exception:
            pass
        try:
            if self.ws:
                self.ws.close()
        except Exception:
            pass
        if self.proc and self.proc.poll() is None:
            try:
                self.proc.terminate()
                self.proc.wait(timeout=5)
            except Exception:
                self.proc.kill()


class Page:
    def __init__(self, chrome, session_id, target_id):
        self.chrome = chrome
        self.session_id = session_id
        self.target_id = target_id

    def call(self, method, params=None, timeout=60):
        return self.chrome.call(method, params, session_id=self.session_id, timeout=timeout)

    def navigate(self, url):
        self.call("Page.navigate", {"url": url})

    def wait_ready(self, timeout=30):
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                if self.eval("document.readyState") in ("interactive", "complete"):
                    return True
            except Exception:
                pass
            time.sleep(0.25)
        return False

    def eval(self, expression, await_promise=False, timeout=60):
        res = self.call("Runtime.evaluate", {
            "expression": expression,
            "awaitPromise": await_promise,
            "returnByValue": True,
        }, timeout=timeout)
        if "exceptionDetails" in res:
            det = res["exceptionDetails"]
            msg = det.get("exception", {}).get("description") or det.get("text")
            raise RuntimeError("JS exception: %s" % msg)
        return res.get("result", {}).get("value")
