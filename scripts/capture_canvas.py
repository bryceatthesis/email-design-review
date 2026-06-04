#!/usr/bin/env python3
"""
capture_canvas.py — headless capture of a Claude Design file + assets from the
live canvas, with NO visible Chrome and NO "Claude in Chrome" tab groups.

This is the standing source step for the email loop. It drives a headless Chrome
that reuses a dedicated, pre-authenticated profile (.capture-profile/) and replays
the OmeletteService/GetFile API same-origin from a claude.ai/design page, so the
request carries your session cookies. It saves the exact bytes and prints sha256s.

One-time setup (interactive login):
    python3 scripts/capture_canvas.py login
  -> opens a VISIBLE Chrome on the dedicated profile; log into claude.ai, then
     close that window. The session persists in the profile for headless reuse.

Capture (headless, repeatable — what future briefs call):
    python3 scripts/capture_canvas.py capture \
        --project 876bef0d-8dee-46e0-a0bd-e9c4ebc8edea \
        --file "2026-06-02 Stasis Mustard Seed UQdTQi Hardened Loop v9.html" \
        --asset "assets/brain-panel-baked-600x873.png" \
        --out _incoming/live-canvas-capture-v9b \
        --expect-file f5b256d0f23286da3f6155505e8f4186587ac88f8ea66f32f46f2d1caa9c4b1c \
        --expect "assets/brain-panel-baked-600x873.png=fa6d84534857babb10d4e173bbb60d083c35f44d386bce3f566f738d4c3b0cf0"

Exit codes: 0 ok; 2 session expired (re-run `login`); 3 hash/expectation mismatch;
1 other error.
"""
import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _cdp  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PROFILE = REPO_ROOT / ".capture-profile"
GETFILE = "/design/anthropic.omelette.api.v1alpha.OmeletteService/GetFile"
# The visible login window exposes this CDP port so `capture` can attach to the
# live, authenticated session — sidestepping disk-cookie-flush timing and any
# headless bot-challenge. After a live capture we close it gracefully, which
# flushes the session cookie so subsequent captures can run fully headless.
LOGIN_PORT = 9444


def log(m):
    print(m, flush=True)


def die(code, msg):
    print("\n" + msg, file=sys.stderr)
    sys.exit(code)


# ---------------------------------------------------------------- login mode
def cmd_login(args):
    profile = os.path.abspath(args.profile)
    os.makedirs(profile, exist_ok=True)
    chrome = _cdp.find_chrome(args.chrome)
    ua = _cdp.chrome_user_agent(chrome)
    _cdp.kill_chrome_using_profile(profile)
    argv = [
        chrome,
        "--user-data-dir=%s" % profile,
        "--user-agent=%s" % ua,
        "--no-first-run", "--no-default-browser-check",
        "https://claude.ai/login",
    ]
    argv[1:1] = ["--remote-debugging-port=%d" % LOGIN_PORT, "--remote-allow-origins=*"]
    proc = subprocess.Popen(argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log("Opened a visible Chrome (pid %d) on the dedicated capture profile:" % proc.pid)
    log("  %s" % profile)
    log("\n  1) Log into claude.ai in that window until you see your workspace.")
    log("  2) Leave the window OPEN.")
    log("\nThen run `capture`: it attaches to this live session (CDP port %d), captures,"
        % LOGIN_PORT)
    log("and closes the window for you — which flushes the session cookie so future")
    log("captures run fully headless with no visible Chrome.")
    return 0


# ---------------------------------------------------------------- capture mode
def _fetch_expr(project, path):
    body = json.dumps({"projectId": project, "path": path})
    # Returns {ok, status, b64?, loc} — base64 of the file bytes on success.
    return (
        "(async () => {"
        "  try {"
        "    const r = await fetch(%s, {method:'POST',"
        "      headers:{'content-type':'application/json','connect-protocol-version':'1'},"
        "      body: %s});"
        "    if (r.status !== 200) return {ok:false, status:r.status, loc: location.href};"
        "    const j = await r.json();"
        "    if (!j || j.content == null) return {ok:false, status:200, nocontent:true, loc: location.href};"
        "    return {ok:true, status:200, b64: j.content};"
        "  } catch(e) { return {ok:false, status:-1, err: String(e), loc: location.href}; }"
        "})()"
        % (json.dumps(GETFILE), json.dumps(body))
    )


def _session_expired(page):
    """True if the design page bounced us to auth (no valid session)."""
    href = (page.eval("location.href") or "")
    return ("/login" in href) or ("/auth" in href) or ("claude.ai" not in href)


def cmd_capture(args):
    profile = os.path.abspath(args.profile)
    if not (Path(profile) / "Default").exists() and not Path(profile).exists():
        die(2, "No capture profile at %s — run:\n  python3 scripts/capture_canvas.py login"
             % profile)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    expects = {}
    if args.expect_file:
        expects["__file__"] = args.expect_file.lower()
    for e in args.expect or []:
        if "=" not in e:
            die(1, "--expect expects 'path=sha', got %r" % e)
        k, v = e.split("=", 1)
        expects[k.strip()] = v.strip().lower()

    targets = [("__file__", args.file, "canvas-source.html")]
    for a in args.asset or []:
        targets.append((a, a, os.path.basename(a)))

    live = _cdp.Chrome.port_alive(LOGIN_PORT)
    if live:
        log("Attaching to the live login window (CDP port %d) ..." % LOGIN_PORT)
        br = _cdp.Chrome.attach(LOGIN_PORT, chrome_path=args.chrome)
    else:
        log("No login window open — launching headless Chrome on profile:\n  %s" % profile)
        br = _cdp.Chrome(profile, headless=True, chrome_path=args.chrome)
        br.launch()

    results = []
    try:
        page = br.new_page("https://claude.ai/design/p/%s" % args.project)
        page.wait_ready(timeout=30)
        time.sleep(1.0)
        if _session_expired(page):
            die(2, "SESSION EXPIRED — not logged into claude.ai.\n"
                   + ("Log in inside the open login window, then re-run capture."
                      if live else
                      "Run:  python3 scripts/capture_canvas.py login   (then log in, then capture)"))

        for key, path, fname in targets:
            res = page.eval(_fetch_expr(args.project, path), await_promise=True, timeout=90)
            if not res or not res.get("ok"):
                status = (res or {}).get("status")
                loc = (res or {}).get("loc", "")
                if status in (401, 403) or "/login" in loc or "/auth" in loc:
                    die(2, "SESSION EXPIRED while fetching %r (status %s).\n"
                           "Re-run login and capture." % (path, status))
                die(1, "GetFile failed for %r: %s" % (path, json.dumps(res)))
            data = base64.b64decode(res["b64"])
            dest = out / fname
            dest.write_bytes(data)
            sha = hashlib.sha256(data).hexdigest()
            results.append((key, path, fname, len(data), sha))
    finally:
        # Graceful Browser.close flushes cookies to the profile (so the NEXT
        # capture can run headless) and closes the visible login window.
        br.close()
        if live:
            log("(closed the login window; session cookie flushed for headless reuse)")

    # report
    log("\nCaptured from live canvas (project %s) -> %s" % (args.project, out))
    log("  %-46s %10s  %s" % ("file", "bytes", "sha256"))
    bad = []
    for key, path, fname, n, sha in results:
        exp = expects.get(key) or expects.get(path)
        mark = ""
        if exp:
            ok = (sha == exp)
            mark = "  OK" if ok else "  MISMATCH (expected %s)" % exp
            if not ok:
                bad.append((path, sha, exp))
        log("  %-46s %10d  %s%s" % (fname, n, sha, mark))

    if bad:
        die(3, "HASH MISMATCH — live file does not match the pinned hash; it changed "
               "since acceptance, or the wrong file/asset was captured. STOP and report.")
    log("\nOK — all captured bytes match their pinned hashes." if expects
        else "\nOK — capture complete (no --expect provided; verify the sha256s above).")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chrome", help="path to Chrome/Chromium binary")
    ap.add_argument("--profile", default=str(DEFAULT_PROFILE),
                    help="dedicated capture profile dir (default: .capture-profile)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("login", help="open a VISIBLE Chrome to log into claude.ai once")

    c = sub.add_parser("capture", help="headless capture of a file + assets")
    c.add_argument("--project", required=True, help="Claude Design project id")
    c.add_argument("--file", required=True, help="file path within the project (the HTML)")
    c.add_argument("--asset", action="append", default=[],
                   help="asset path within the project (repeatable)")
    c.add_argument("--out", required=True, help="output directory")
    c.add_argument("--expect-file", help="assert the captured file's sha256")
    c.add_argument("--expect", action="append", default=[],
                   help="assert an asset: 'assetpath=sha256' (repeatable)")

    args = ap.parse_args(argv)
    if args.cmd == "login":
        return cmd_login(args)
    if args.cmd == "capture":
        return cmd_capture(args)
    ap.error("unknown command")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        die(1, "ERROR: %s" % e)
