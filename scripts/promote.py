#!/usr/bin/env python3
"""Promote an approved Stasis email design into the review repo.

Turns an approved Claude Design export + Theo's handoff receipt into a committed,
catalogued artifact: copies the HTML under designs/, verifies its sha256 against
the receipt, upserts manifest.json, and commits.

Usage:
    promote.py --flow welcome --variant future-state --step 2 --name "Education" \\
               --html ./export.html --receipt ./receipt.txt

The receipt may be Theo's text "=== HANDOFF RECEIPT ===" block or a JSON file.
Run --help for the full flag list.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "manifest.json"
VALID_STATUS = {"live", "draft", "approved", "retired"}


# ---------------------------------------------------------------- helpers
def fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "step"


def titleize(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return dt.date.today().isoformat()


def _clean(value: Optional[str]) -> Optional[str]:
    """Normalise receipt values: treat blanks / placeholder blocks as missing."""
    if value is None:
        return None
    v = value.strip().strip("|").strip()
    if not v:
        return None
    if v.lower() in {"n/a", "na", "none", "missing", "tbd", "didn't mint a url",
                     "didnt mint a url", "verified locally"}:
        return None
    return v


# ---------------------------------------------------------------- receipt parsing
def parse_receipt(path: Path) -> dict:
    """Extract provenance fields from a receipt file.

    Returns a dict with any of: claude_design_url, klaviyo_url, artifact_sha256,
    brand, task_id. Accepts either a JSON receipt or Theo's text handoff block.
    """
    raw = path.read_text(encoding="utf-8", errors="replace")

    # Try JSON first.
    try:
        data = json.loads(raw)
        return _from_json_receipt(data)
    except json.JSONDecodeError:
        pass

    return _from_text_receipt(raw)


def _from_json_receipt(data: dict) -> dict:
    cd = data.get("claude_design", {}) if isinstance(data.get("claude_design"), dict) else {}
    kv = data.get("klaviyo_staging", {}) if isinstance(data.get("klaviyo_staging"), dict) else {}
    out = {
        "claude_design_url": _clean(
            data.get("claude_design_url")
            or cd.get("artifact_url") or cd.get("conversation_url") or cd.get("turn_url")
        ),
        "klaviyo_url": _clean(data.get("klaviyo_url") or kv.get("editor_url")),
        "artifact_sha256": _clean(data.get("sha256") or data.get("artifact_sha256")
                                  or cd.get("artifact_sha256")),
        "brand": _clean(data.get("brand")),
        "task_id": _clean(data.get("task_id")),
    }
    return out


def _from_text_receipt(raw: str) -> dict:
    """Tolerant line-based parse of the YAML-ish handoff receipt.

    Tracks the current top-level (zero-indent) section so we can disambiguate
    keys that repeat across blocks (e.g. artifact_sha256). Inline '# comments'
    and the === RECEIPT === fences are ignored.
    """
    # Scope to the receipt block if the fences are present.
    m = re.search(r"=== *HANDOFF RECEIPT *===(.*?)=== *END RECEIPT *===", raw, re.S | re.I)
    body = m.group(1) if m else raw

    fields: dict = {}
    section = ""  # current zero-indent section name
    for line in body.splitlines():
        # strip trailing inline comments (but not '#' inside a URL fragment value)
        stripped = line.rstrip()
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip())
        content = stripped.strip()
        # remove a trailing " # comment" only when there's a space before #
        content = re.sub(r"\s+#.*$", "", content)
        if ":" not in content:
            continue
        key, _, value = content.partition(":")
        key = key.strip()
        value = value.strip()
        if indent == 0:
            section = key
            # a top-level key may also carry a value (e.g. "brand: stasis")
            if value:
                fields[key] = value
            continue
        fields[f"{section}.{key}"] = value

    out = {
        "claude_design_url": _clean(
            fields.get("claude_design.artifact_url")
            or fields.get("claude_design.conversation_url")
            or fields.get("claude_design.turn_url")
        ),
        "klaviyo_url": _clean(fields.get("klaviyo_staging.editor_url")),
        "artifact_sha256": _clean(fields.get("claude_design.artifact_sha256")),
        "brand": _clean(fields.get("brand")),
        "task_id": _clean(fields.get("task_id")),
    }
    return out


# ---------------------------------------------------------------- manifest
def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"schema": 1, "generated_at": now_iso(), "flows": []}


def find_or_create(items: list, key: str, value: str, factory) -> dict:
    for it in items:
        if it.get(key) == value:
            return it
    created = factory()
    items.append(created)
    return created


def upsert_step(variant: dict, step_obj: dict) -> None:
    steps = variant.setdefault("steps", [])
    for i, s in enumerate(steps):
        if s.get("step") == step_obj["step"]:
            steps[i] = step_obj
            break
    else:
        steps.append(step_obj)
    steps.sort(key=lambda s: s.get("step", 0))


def write_manifest(manifest: dict) -> None:
    manifest["generated_at"] = now_iso()
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- git
def git_commit(paths: list, message: str) -> None:
    subprocess.run(["git", "-C", str(REPO_ROOT), "add", *paths], check=True)
    subprocess.run(["git", "-C", str(REPO_ROOT), "commit", "-q", "-m", message], check=True)


# ---------------------------------------------------------------- main
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Promote an approved design into the review repo.")
    p.add_argument("--flow", required=True, help="flow id, e.g. welcome")
    p.add_argument("--variant", required=True, help="variant id, e.g. future-state")
    p.add_argument("--step", required=True, type=int, help="1-based step number within the variant")
    p.add_argument("--html", required=True, help="path to the approved HTML export")
    p.add_argument("--receipt", help="path to Theo's handoff receipt (text or JSON)")
    p.add_argument("--name", help="step display name (default: derived from slug)")
    p.add_argument("--flow-name", help="flow display name (set/updated on the flow)")
    p.add_argument("--variant-label", help="variant display label")
    p.add_argument("--status", choices=sorted(VALID_STATUS),
                   help="variant status (default: draft for new variants)")
    p.add_argument("--step-labels", help="comma-separated flow-level step labels")
    p.add_argument("--draft", action="store_true",
                   help="mark the step not-yet-approved (default: approved on promote)")
    p.add_argument("--claude-design-url", help="override/supply Claude Design URL")
    p.add_argument("--klaviyo-url", help="override/supply Klaviyo editor URL")
    p.add_argument("--allow-sha-mismatch", action="store_true",
                   help="proceed even if the HTML hash differs from the receipt")
    p.add_argument("--no-commit", action="store_true", help="write files but skip git commit")
    return p


def main(argv: Optional[list] = None) -> None:
    args = build_parser().parse_args(argv)

    html_src = Path(args.html).expanduser()
    if not html_src.is_file():
        fail(f"--html not found: {html_src}")
    if args.step < 1:
        fail("--step must be >= 1")

    receipt = parse_receipt(Path(args.receipt).expanduser()) if args.receipt else {}

    sha = sha256_of(html_src)

    # Provenance guard: the file we promote must be the one the receipt vouches for.
    receipt_sha = receipt.get("artifact_sha256")
    if receipt_sha and receipt_sha != sha:
        msg = (f"sha256 mismatch — HTML is {sha} but receipt vouches for {receipt_sha}. "
               "The file being promoted is not the artifact that passed provenance.")
        if args.allow_sha_mismatch:
            print(f"warning: {msg}", file=sys.stderr)
        else:
            fail(msg + " Re-export the approved file, or pass --allow-sha-mismatch.")

    name = args.name or titleize(slugify(html_src.stem))
    slug = slugify(name)
    filename = f"{args.step:02d}-{slug}.html"
    dest_dir = REPO_ROOT / "designs" / args.flow / args.variant
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / filename
    rel = dest.relative_to(REPO_ROOT).as_posix()

    # Remove any prior file for this step that had a different slug (avoid orphans).
    for old in dest_dir.glob(f"{args.step:02d}-*.html"):
        if old != dest:
            old.unlink()

    shutil.copyfile(html_src, dest)

    manifest = load_manifest()
    flow = find_or_create(
        manifest.setdefault("flows", []), "id", args.flow,
        lambda: {"id": args.flow, "name": args.flow_name or titleize(args.flow), "variants": []},
    )
    if args.flow_name:
        flow["name"] = args.flow_name
    if args.step_labels:
        flow["step_labels"] = [s.strip() for s in args.step_labels.split(",") if s.strip()]

    variant = find_or_create(
        flow.setdefault("variants", []), "id", args.variant,
        lambda: {"id": args.variant, "label": args.variant_label or titleize(args.variant),
                 "status": args.status or "draft", "steps": []},
    )
    if args.variant_label:
        variant["label"] = args.variant_label
    if args.status:
        variant["status"] = args.status

    approved = not args.draft
    step_obj = {
        "step": args.step,
        "name": name,
        "file": rel,
        "approved": approved,
        "approved_date": today() if approved else None,
        "claude_design_url": args.claude_design_url or receipt.get("claude_design_url"),
        "klaviyo_url": args.klaviyo_url or receipt.get("klaviyo_url"),
        "sha256": sha,
    }
    upsert_step(variant, step_obj)
    write_manifest(manifest)

    print(f"promoted {args.flow}/{args.variant} step {args.step} -> {rel}")
    print(f"  sha256: {sha}")
    if step_obj["claude_design_url"]:
        print(f"  claude design: {step_obj['claude_design_url']}")
    if step_obj["klaviyo_url"]:
        print(f"  klaviyo: {step_obj['klaviyo_url']}")

    if args.no_commit:
        print("  (--no-commit: files written, not committed)")
        return

    commit_msg = (
        f'promote({args.flow}/{args.variant}): step {args.step} "{name}"\n\n'
        f"file: {rel}\n"
        f"sha256: {sha}\n"
        f"approved: {step_obj['approved_date'] or 'no (draft)'}\n"
        f"claude_design: {step_obj['claude_design_url'] or '-'}\n"
        f"klaviyo: {step_obj['klaviyo_url'] or '-'}\n"
    )
    git_commit([rel, "manifest.json"], commit_msg)
    print("  committed.")


if __name__ == "__main__":
    main()
