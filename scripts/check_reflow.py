#!/usr/bin/env python3
"""
check_reflow.py — verify an email reflows to a target width, using LOCAL headless
Chrome (no Claude in Chrome).

It embeds the email in a `srcdoc` <iframe> sized to each width and reads the
iframe document's scrollWidth — exactly how the review viewer (index.html) frames
it, so the number is 1:1 with the tool's Mobile/Desktop modes. A srcdoc iframe is
same-origin with its host page, so contentDocument is readable even from file://.

    python3 scripts/check_reflow.py designs/mustard-seed/v9/01-mustard-seed.html \
        --width 375 --width 600

Passes only if, at each width W, the email's scrollWidth == W (no overflow).
Exit 0 = pass, 4 = a width overflowed, 1 = error.
"""
import argparse
import os
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _cdp  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PROFILE = REPO_ROOT / ".reflow-profile"


def host_page(email_html, width):
    srcdoc = email_html.replace("&", "&amp;").replace('"', "&quot;")
    return (
        "<!doctype html><html><head><meta charset='utf-8'></head>"
        "<body style='margin:0'>"
        "<iframe id='f' style='width:%dpx;height:2400px;border:0' srcdoc=\"%s\"></iframe>"
        "</body></html>" % (width, srcdoc)
    )


MEASURE = (
    "(() => {"
    "  const f = document.getElementById('f');"
    "  if (!f) return null;"
    "  const d = f.contentDocument;"
    "  if (!d || !d.body) return {ready:false};"
    "  return {ready: d.readyState === 'complete',"
    "          sw: Math.max(d.body.scrollWidth, d.documentElement.scrollWidth),"
    "          iw: f.contentWindow.innerWidth};"
    "})()"
)


def measure(page, width):
    deadline = time.time() + 15
    last = None
    while time.time() < deadline:
        last = page.eval(MEASURE)
        if last and last.get("ready") and last.get("sw"):
            return last
        time.sleep(0.2)
    return last


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", help="path to the (flattened) email HTML")
    ap.add_argument("--width", type=int, action="append", default=[],
                    help="width to test (repeatable; default 375 and 600)")
    ap.add_argument("--chrome", help="path to Chrome/Chromium binary")
    ap.add_argument("--profile", default=str(DEFAULT_PROFILE),
                    help="scratch Chrome profile (default: .reflow-profile)")
    args = ap.parse_args(argv)

    widths = args.width or [375, 600]
    email = Path(args.html).read_text(encoding="utf-8", errors="replace")
    os.makedirs(args.profile, exist_ok=True)

    tmp = Path(tempfile.mkdtemp(prefix="reflow_"))
    rows = []
    with _cdp.Chrome(args.profile, headless=True, chrome_path=args.chrome) as br:
        page = br.new_page("about:blank")
        for w in widths:
            host = tmp / ("host_%d.html" % w)
            host.write_text(host_page(email, w), encoding="utf-8")
            page.navigate("file://%s" % host)
            page.wait_ready(timeout=20)
            m = measure(page, w)
            sw = (m or {}).get("sw")
            ok = sw == w
            rows.append((w, sw, ok))

    print("Reflow check: %s" % args.html)
    all_ok = True
    for w, sw, ok in rows:
        all_ok = all_ok and ok
        print("  @%dpx  scrollWidth=%s  %s"
              % (w, sw, "OK" if ok else "OVERFLOW (expected %d)" % w))
    if not all_ok:
        print("\nFAIL — email does not reflow to one or more target widths "
              "(its HTML is not fully responsive at that width).", file=sys.stderr)
        return 4
    print("\nPASS — email reflows cleanly to all target widths.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print("ERROR: %s" % e, file=sys.stderr)
        sys.exit(1)
