#!/usr/bin/env python3
"""
flatten_claude_export.py — Claude Design "standalone export" -> TRUE static HTML.

A Claude Design "Export -> Standalone HTML" file is NOT static HTML. It is a
JS-runtime preview document: an "omelette"/Babel bundler boots at
DOMContentLoaded, reads an embedded asset map, and injects the DOM (images are
resolved at runtime to blob: URLs). Opened with JS disabled, it renders nothing.

This tool turns that export into a self-contained .html that renders identically
with JavaScript disabled, with every image inlined as a base64 data: URI sourced
*byte-for-byte* from the export's own embedded asset map.

------------------------------------------------------------------------------
METHOD (and why it differs from a headless-browser scrape)
------------------------------------------------------------------------------
The export embeds three things we need, in <script> tags:

  * type="__bundler/manifest"  -> the ASSET MAP: { uuid: {mime, compressed, data(b64)} }
                                  These are Claude Design's own image bytes.
  * type="__bundler/template"  -> a JSON-encoded string that IS the complete,
                                  static email HTML (plain HTML, not JSX): full
                                  <!DOCTYPE html>, Outlook VML, MSO conditional
                                  comments, Liquid placeholders, the works.
                                  Image refs in it are bare asset-map UUIDs
                                  (src="<uuid>" or background-image:url("<uuid>"))
                                  plus VML/Outlook "assets/<file>" path refs.

So the trustworthy, lossless flatten is DETERMINISTIC and does not need a browser:
  1. Decode the asset map; sha256 each image.
  2. JSON-decode the template -> static HTML.
  3. Replace every asset-map UUID with data:<mime>;base64,<bytes-from-the-map>.
  4. Resolve "assets/<file>" VML paths to the matching asset (proximity in the
     template + PNG-dimension cross-check, with optional --asset-map override).
  5. Enforce fidelity gates (every inlined image's sha is from the map; zero
     runtime residue; zero unresolved refs).

We deliberately DON'T extract the DOM from a headless render: Chrome rewrites
img src to blob:null/<fresh-uuid> (severing the asset-map linkage that makes the
flatten verifiable) and strips the VML/MSO conditional comments that Klaviyo and
Outlook require. Instead the headless browser is used as a VERIFICATION ORACLE
(--verify-render): render the original export and the flattened file, then
pixel-diff them (and optionally against a parity PNG). This honors the brief's
robustness instinct while producing strictly better email HTML.

------------------------------------------------------------------------------
USAGE
------------------------------------------------------------------------------
  python3 scripts/flatten_claude_export.py \
      --in _incoming/mustard-seed-v8-standalone-export.html \
      --out _incoming/mustard-seed-v8-flattened.html \
      --expect-sha 18c546d07e62dc88339a23a21b7e6fb11388ab807ca073a7949e69c5d7c016df \
      --parity-png _incoming/mustard-seed-v8-parity-render.png

Flags:
  --in PATH               (required) the standalone export .html
  --out PATH              (required) where to write the flattened static .html
  --expect-sha HEX        assert the input file's sha256 (provenance guard)
  --asset-map "p=uuid"    force-resolve an "assets/<p>" path to a uuid (repeatable)
  --verify-render / --no-verify-render   pixel-diff oracle (default: on if Chrome found)
  --parity-png PATH       compare the flattened render to this target PNG
  --chrome PATH           path to the Chrome/Chromium binary
  --tolerance FLOAT       max fraction of differing pixels allowed (default 0.02)
  --pixel-threshold INT   per-channel delta that counts a pixel as "different" (default 16)

Exit code is non-zero if any fidelity gate or visual-regression gate fails.
"""

import argparse
import base64
import hashlib
import json
import os
import re
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

UUID_RE = re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')

# Strings whose presence in the output means the flatten leaked runtime residue.
RESIDUE_TOKENS = [
    "<script",
    "omelette",
    "om-src-id",
    "data-om-id",
    "data-omelette",
    "__om_srcmap",
    "__bundler",
    "Babel",
    "babel",
    "claude.ai",
    "text/babel",
]

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
]


class FlattenError(Exception):
    pass


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# Parsing the export
# ---------------------------------------------------------------------------

def extract_script_body(html, script_type):
    """Return the inner text of <script type="...">...</script>, or None."""
    m = re.search(
        r'<script[^>]*type="%s"[^>]*>(.*?)</script>' % re.escape(script_type),
        html, re.S,
    )
    return m.group(1) if m else None


def png_dimensions(raw):
    """Return (width, height) for a PNG byte string, else None."""
    if raw[:8] == b"\x89PNG\r\n\x1a\n" and raw[12:16] == b"IHDR":
        return struct.unpack(">II", raw[16:24])
    return None


def decode_asset(entry):
    """Decode one asset-map entry to its real image bytes."""
    raw = base64.b64decode(entry["data"])
    if entry.get("compressed"):
        try:
            raw = zlib.decompress(raw)
        except zlib.error:
            raw = zlib.decompress(raw, -15)  # raw DEFLATE fallback
    return raw


def load_asset_map(html):
    """Parse __bundler/manifest into {uuid: {mime, bytes, sha256, data_uri, dims}}."""
    body = extract_script_body(html, "__bundler/manifest")
    if body is None:
        raise FlattenError("No __bundler/manifest script found — is this a Claude Design standalone export?")
    raw_map = json.loads(body)
    if not isinstance(raw_map, dict) or not raw_map:
        raise FlattenError("__bundler/manifest is empty or not an object.")
    assets = {}
    for uuid, entry in raw_map.items():
        if not (isinstance(entry, dict) and "mime" in entry and "data" in entry):
            raise FlattenError("Asset map entry %r missing mime/data." % uuid)
        data = decode_asset(entry)
        sha = hashlib.sha256(data).hexdigest()
        b64 = base64.b64encode(data).decode("ascii")
        assets[uuid] = {
            "mime": entry["mime"],
            "bytes": data,
            "sha256": sha,
            "data_uri": "data:%s;base64,%s" % (entry["mime"], b64),
            "dims": png_dimensions(data),
        }
    return assets


def load_template(html):
    """Parse __bundler/template (JSON-encoded string) into static HTML."""
    body = extract_script_body(html, "__bundler/template")
    if body is None:
        raise FlattenError("No __bundler/template script found — nothing to flatten.")
    template = json.loads(body)
    if not isinstance(template, str):
        raise FlattenError("__bundler/template did not decode to a string.")
    return template


# ---------------------------------------------------------------------------
# Resolving "assets/<file>" path references (VML / Outlook backgrounds)
# ---------------------------------------------------------------------------

def resolve_asset_paths(template, assets, overrides):
    """
    Map each unique "assets/<file>" reference to an asset uuid.

    Strategy per path:
      1. explicit --asset-map override wins;
      2. else nearest asset-map uuid by character distance in the template,
         cross-checked against a WxH hint in the filename (if the candidate is
         a PNG whose dimensions match, that's a strong confirmation).
    Returns {path_string: uuid} and raises if any path can't be resolved.
    """
    path_refs = sorted(set(re.findall(r'assets/[^\s"\'\)]+', template)))
    if not path_refs:
        return {}

    uuid_positions = [(m.start(), m.group()) for m in UUID_RE.finditer(template)
                      if m.group() in assets]
    resolved = {}
    for path in path_refs:
        filename = path.split("/", 1)[1]
        if path in overrides:
            uuid = overrides[path]
            if uuid not in assets:
                raise FlattenError("--asset-map override %r points to unknown uuid %r." % (path, uuid))
            resolved[path] = uuid
            log("  assets path %-50s -> %s (override)" % (path, uuid[:8]))
            continue
        # filename can also be given bare in an override (without the assets/ prefix)
        if filename in overrides:
            uuid = overrides[filename]
            if uuid not in assets:
                raise FlattenError("--asset-map override %r points to unknown uuid %r." % (filename, uuid))
            resolved[path] = uuid
            log("  assets path %-50s -> %s (override)" % (path, uuid[:8]))
            continue

        if not uuid_positions:
            raise FlattenError("Cannot resolve %r: no asset-map UUIDs present in template." % path)

        pos = template.find(path)
        nearest = min(uuid_positions, key=lambda p: abs(p[0] - pos))
        uuid = nearest[1]

        # Dimension cross-check against a WxH hint in the filename.
        wh = re.search(r'(\d+)x(\d+)', filename)
        dims = assets[uuid]["dims"]
        confirm = ""
        if wh and dims:
            want = (int(wh.group(1)), int(wh.group(2)))
            if want == dims:
                confirm = " [dims %dx%d match]" % dims
            else:
                raise FlattenError(
                    "Resolution conflict for %r: nearest uuid %s is %sx%s but "
                    "filename implies %sx%s. Pass --asset-map \"%s=<uuid>\" to disambiguate."
                    % (path, uuid[:8], dims[0], dims[1], want[0], want[1], path)
                )
        resolved[path] = uuid
        log("  assets path %-50s -> %s (nearest, dist %d)%s"
            % (path, uuid[:8], abs(nearest[0] - pos), confirm))
    return resolved


# ---------------------------------------------------------------------------
# The flatten itself
# ---------------------------------------------------------------------------

def flatten(template, assets, asset_path_map):
    """Inline all images; return (html, used_uuids)."""
    out = template
    used = set()

    # 1) bare asset-map UUID references (src="<uuid>", url("<uuid>"), url(&quot;<uuid>&quot;))
    for uuid, asset in assets.items():
        if uuid in out:
            out = out.replace(uuid, asset["data_uri"])
            used.add(uuid)

    # 2) "assets/<file>" VML / Outlook background path references
    for path, uuid in asset_path_map.items():
        out = out.replace(path, assets[uuid]["data_uri"])
        used.add(uuid)

    return out, used


# ---------------------------------------------------------------------------
# Fidelity gates
# ---------------------------------------------------------------------------

def gate_sha_provenance(out_html, assets):
    """
    Every inlined image must carry bytes whose sha256 is in the asset map.
    By construction we only inlined asset-map data URIs, but we re-verify from
    the OUTPUT string so the guarantee is about the file we actually wrote.
    """
    known_uris = {a["data_uri"]: a["sha256"] for a in assets.values()}
    # base64 never contains & < > so excluding them keeps url(&quot;...&quot;) intact.
    data_uris = re.findall(r'data:[^"\')\s&<>]+', out_html)
    if not data_uris:
        raise FlattenError("Fidelity gate failed: output contains no inlined images.")
    checked = 0
    inline_svg = 0
    for uri in data_uris:
        # Only image data URIs are subject to the asset-map provenance gate.
        if not uri.startswith("data:image"):
            continue
        # Inline SVG data-URIs are vector markup authored directly in the template
        # (e.g. the CSS/SVG shaped edges the brief mandates). Their bytes are
        # self-contained in the URI — there is nothing to substitute, and flatten
        # never synthesises one (it only swaps asset-map UUIDs / assets-paths for
        # data URIs), so any SVG data-URI here came verbatim from the export's own
        # template. They carry no asset-map provenance and are exempt from this gate.
        if uri.startswith("data:image/svg+xml"):
            inline_svg += 1
            continue
        if uri not in known_uris:
            # Recompute from the URI's own payload to produce a useful error.
            try:
                payload = uri.split(",", 1)[1]
                sha = hashlib.sha256(base64.b64decode(payload)).hexdigest()
            except Exception:
                sha = "<undecodable>"
            raise FlattenError(
                "Fidelity gate failed: an inlined image (sha %s) is not present "
                "in the export's asset map." % sha[:16]
            )
        checked += 1
    log("  sha provenance: %d raster image(s) verified against the asset map"
        "%s" % (checked, ("; %d inline SVG data-URI(s) (self-contained vector, exempt)"
                          % inline_svg) if inline_svg else ""))


def gate_no_residue(out_html):
    lowered = out_html.lower()
    for token in RESIDUE_TOKENS:
        if token.lower() in lowered:
            idx = lowered.find(token.lower())
            snippet = out_html[max(0, idx - 30):idx + 40].replace("\n", " ")
            raise FlattenError("Residue gate failed: found %r  ...%s..." % (token, snippet))
    log("  residue gate: clean (no script/omelette/Babel/__bundler/claude.ai/etc.)")


def gate_no_unresolved_refs(out_html, assets):
    # No bare asset-map UUIDs left behind.
    leftover = [u for u in UUID_RE.findall(out_html) if u in assets]
    if leftover:
        raise FlattenError("Unresolved gate failed: bare asset-map UUID(s) remain: %s"
                           % ", ".join(sorted(set(u[:8] for u in leftover))))
    # No "assets/<file>" paths left behind.
    paths = re.findall(r'assets/[^\s"\'\)]+', out_html)
    if paths:
        raise FlattenError("Unresolved gate failed: 'assets/...' path(s) remain: %s"
                           % ", ".join(sorted(set(paths))))
    # Every <img src> must be a data: URI (no external/relative image srcs).
    for m in re.finditer(r'<img\b[^>]*?\bsrc="([^"]*)"', out_html, re.I):
        src = m.group(1)
        if not src.startswith("data:"):
            raise FlattenError("Unresolved gate failed: non-inlined <img src=%r>." % src[:60])
    log("  unresolved gate: no bare UUIDs, no assets/ paths, every <img> is a data: URI")


# ---------------------------------------------------------------------------
# Visual-regression oracle (headless Chrome + Pillow)
# ---------------------------------------------------------------------------

def find_chrome(explicit):
    if explicit:
        return explicit if os.path.exists(explicit) else None
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    return None


def chrome_screenshot(chrome, html_path, png_path, width=620, height=4000):
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--default-background-color=FFFFFFFF",
        "--virtual-time-budget=8000",
        "--window-size=%d,%d" % (width, height),
        "--screenshot=%s" % png_path,
        "file://%s" % os.path.abspath(html_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if not os.path.exists(png_path):
        raise FlattenError("Chrome failed to produce a screenshot.\nstderr:\n%s" % proc.stderr[-800:])


def image_diff(png_a, png_b, pixel_threshold):
    """Return (fraction_differing, mean_abs_diff, dims) comparing two PNGs."""
    from PIL import Image, ImageChops
    a = Image.open(png_a).convert("RGB")
    b = Image.open(png_b).convert("RGB")
    # Normalize to a common size (crop/pad to the smaller common box).
    w = min(a.width, b.width)
    h = min(a.height, b.height)
    a = a.crop((0, 0, w, h))
    b = b.crop((0, 0, w, h))
    diff = ImageChops.difference(a, b)
    # Per-pixel max channel delta.
    gray = diff.convert("L")
    hist = gray.histogram()
    total = w * h
    differing = sum(hist[pixel_threshold:])
    mean_abs = sum(i * n for i, n in enumerate(hist)) / total if total else 0.0
    return differing / total if total else 0.0, mean_abs, (w, h)


def verify_render(chrome, in_path, out_path, parity_png, tolerance, pixel_threshold):
    log("\nVisual-regression oracle (headless Chrome render + pixel diff):")
    tmp = tempfile.mkdtemp(prefix="flatten_vr_")
    orig_png = os.path.join(tmp, "original.png")
    flat_png = os.path.join(tmp, "flattened.png")
    log("  rendering original export ...")
    chrome_screenshot(chrome, in_path, orig_png)
    log("  rendering flattened output ...")
    chrome_screenshot(chrome, out_path, flat_png)

    frac, mean_abs, dims = image_diff(orig_png, flat_png, pixel_threshold)
    log("  flattened vs original export : %.4f%% differing pixels (mean abs %.2f) over %dx%d"
        % (frac * 100, mean_abs, dims[0], dims[1]))
    ok = frac <= tolerance
    status = "PASS" if ok else "FAIL"
    log("    -> %s (tolerance %.4f%%)" % (status, tolerance * 100))

    parity_ok = True
    if parity_png and os.path.exists(parity_png):
        pfrac, pmean, pdims = image_diff(flat_png, parity_png, pixel_threshold)
        log("  flattened vs parity PNG      : %.4f%% differing pixels (mean abs %.2f) over %dx%d"
            % (pfrac * 100, pmean, pdims[0], pdims[1]))
        # Parity PNG may be captured at a different width/zoom; treat it as advisory
        # unless the flattened-vs-original gate also fails.
        parity_ok = pfrac <= max(tolerance, 0.05)
        log("    -> %s (advisory, tolerance %.4f%%)"
            % ("PASS" if parity_ok else "WARN", max(tolerance, 0.05) * 100))

    log("  screenshots: %s" % tmp)
    return ok


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_overrides(pairs):
    out = {}
    for p in pairs or []:
        if "=" not in p:
            raise FlattenError("--asset-map expects \"path=uuid\", got %r" % p)
        k, v = p.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Flatten a Claude Design standalone export into true static HTML.")
    ap.add_argument("--in", dest="inp", required=True, help="standalone export .html")
    ap.add_argument("--out", dest="out", required=True, help="output static .html")
    ap.add_argument("--expect-sha", help="assert the input file's sha256 (provenance guard)")
    ap.add_argument("--asset-map", action="append", default=[],
                    help='force-resolve "assets/<file>=<uuid>" (repeatable)')
    ap.add_argument("--chrome", help="path to Chrome/Chromium binary")
    ap.add_argument("--parity-png", help="parity render PNG to compare against")
    vr = ap.add_mutually_exclusive_group()
    vr.add_argument("--verify-render", dest="verify", action="store_true", default=None)
    vr.add_argument("--no-verify-render", dest="verify", action="store_false")
    ap.add_argument("--tolerance", type=float, default=0.02,
                    help="max fraction of differing pixels (default 0.02)")
    ap.add_argument("--pixel-threshold", type=int, default=16,
                    help="per-channel delta counting a pixel as different (default 16)")
    args = ap.parse_args(argv)

    in_path = Path(args.inp)
    if not in_path.exists():
        raise FlattenError("Input not found: %s" % in_path)

    raw_bytes = in_path.read_bytes()
    actual_sha = hashlib.sha256(raw_bytes).hexdigest()
    log("Input : %s" % in_path)
    log("  sha256: %s" % actual_sha)
    if args.expect_sha:
        if actual_sha.lower() != args.expect_sha.lower():
            raise FlattenError("Provenance guard failed: expected sha %s but file is %s"
                               % (args.expect_sha, actual_sha))
        log("  provenance guard: OK (matches --expect-sha)")

    html = raw_bytes.decode("utf-8", errors="replace")

    log("\nParsing embedded bundler payload:")
    assets = load_asset_map(html)
    log("  asset map: %d image(s)" % len(assets))
    for uuid, a in sorted(assets.items()):
        dims = "%dx%d" % a["dims"] if a["dims"] else "n/a"
        log("    %s  %-11s %-9s sha=%s  %d bytes"
            % (uuid[:8], a["mime"], dims, a["sha256"][:16], len(a["bytes"])))
    template = load_template(html)
    log("  template: %d chars of static HTML" % len(template))

    log("\nResolving image references:")
    overrides = parse_overrides(args.asset_map)
    asset_path_map = resolve_asset_paths(template, assets, overrides)

    out_html, used = flatten(template, assets, asset_path_map)
    unused = set(assets) - used
    if unused:
        log("  note: %d asset(s) in the map were not referenced by the template: %s"
            % (len(unused), ", ".join(sorted(u[:8] for u in unused))))

    log("\nFidelity gates:")
    gate_sha_provenance(out_html, assets)
    gate_no_residue(out_html)
    gate_no_unresolved_refs(out_html, assets)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out_html, encoding="utf-8")
    out_sha = hashlib.sha256(out_html.encode("utf-8")).hexdigest()
    log("\nWrote : %s" % out_path)
    log("  sha256: %s" % out_sha)
    log("  size  : %d bytes" % len(out_html.encode("utf-8")))

    # Visual-regression oracle.
    do_verify = args.verify
    chrome = find_chrome(args.chrome)
    if do_verify is None:
        do_verify = chrome is not None
    if do_verify:
        if not chrome:
            raise FlattenError("--verify-render requested but no Chrome/Chromium binary found (use --chrome).")
        ok = verify_render(chrome, str(in_path), str(out_path), args.parity_png,
                           args.tolerance, args.pixel_threshold)
        if not ok:
            raise FlattenError("Visual-regression gate failed: flattened render diverges from the original export.")
    else:
        log("\nVisual-regression oracle: skipped.")

    log("\nDONE. Flattened static HTML is self-contained and renders with JS disabled.")
    log("Provenance note for the manifest/receipt:")
    log("  source of truth = the native export (sha %s)" % actual_sha[:16] + "…")
    log("  this flattened file (sha %s" % out_sha[:16] + "…) is a deterministic flatten of it;")
    log("  images verified byte-for-byte against the export's asset map.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FlattenError as e:
        print("\nERROR: %s" % e, file=sys.stderr)
        sys.exit(1)
