# Stasis Design Review

A small, data-driven web app for reviewing Stasis email designs throughout a project.
Render any approved design in context, drop two variants side by side, and step through
a full flow in send order with both columns moving in lockstep.

The app is **manifest-driven**: `manifest.json` is the spine, and the viewer renders
whatever it declares. Designs are committed into `designs/` and served same-origin, so
theme injection and scroll-sync work and framing is never blocked.

## Run it

```bash
python3 -m http.server 8753
# open http://localhost:8753/
```

A static server is required — opening `index.html` over `file://` will fail because the
app fetches `manifest.json` and the design files over HTTP.

## Layout

```
designs/
  <flow-id>/
    <variant-id>/
      01-<step-slug>.html
      02-<step-slug>.html
manifest.json          # the catalog the viewer reads
index.html             # the viewer app (vanilla JS, no build step)
scripts/flatten_claude_export.py  # Claude Design export -> true static HTML
scripts/promote.py     # promotion tool
_incoming/             # staging area for exports + receipts (working dir)
```

## Data model

A **flow** has one or more **variants**; each variant is an ordered list of **steps**
(one email each).

- **A/B compare** → two variants of the same flow (e.g. `a` vs `b`).
- **Against original / cross-state** → variants labelled `current` vs `future-state`.
- **Full-flow step-through** → the ordered `steps` of a variant; both columns move together.
- **A single campaign** (e.g. Mustard Seed) → a flow with one step and multiple variants
  (`original`, `v8`).

`status` ∈ `live | draft | approved | retired`. `approved` / `approved_date` gate what the
app marks review-ready. Provenance fields come straight from the handoff receipt.

## The contract (producer → infrastructure)

The producer (Claude Design loop) authors the design and emits **approved HTML + a handoff
receipt** (the receipt proves provenance and Klaviyo parity). The producer does **not** know
the manifest exists — they tag the handoff with `flow / variant / step`, and the promotion
script does the mapping. That tag set is the whole contract.

`promote.py` accepts the receipt either as the text `=== HANDOFF RECEIPT ===` block or as
JSON, and pulls:

| Manifest field      | Receipt source                                            |
|---------------------|-----------------------------------------------------------|
| `claude_design_url` | `claude_design.artifact_url` (→ conversation/turn URL)    |
| `klaviyo_url`       | `klaviyo_staging.editor_url`                              |
| `sha256`            | computed from the promoted HTML                           |

**Provenance guard:** if the receipt carries `claude_design.artifact_sha256`, the script
verifies it matches the hash of the HTML being promoted. A mismatch means the file is not the
artifact that passed provenance, and promotion is refused (override with
`--allow-sha-mismatch`).

## Flatten a Claude Design export (before promoting)

Claude Design's "Export → Standalone HTML" is **not** static HTML — it's a
JS-runtime preview doc. An "omelette"/Babel runtime boots at load, reads an
embedded asset map, and injects the DOM (images resolve to `blob:` URLs at
runtime). Opened with JS disabled it renders blank, and Klaviyo can't ingest it.
`flatten_claude_export.py` bakes it into true static HTML:

```bash
python3 scripts/flatten_claude_export.py \
  --in _incoming/mustard-seed-v8-standalone-export.html \
  --out _incoming/mustard-seed-v8-flattened.html \
  --expect-sha 18c546…   --parity-png _incoming/mustard-seed-v8-parity-render.png
```

**How it works (and why it isn't a headless DOM scrape):** the export embeds the
complete static email HTML in a `__bundler/template` script (full `<!DOCTYPE>`,
Outlook VML, MSO conditionals, Liquid placeholders) and the image bytes in a
`__bundler/manifest` asset map. The flatten is therefore *deterministic*:
JSON-decode the template, replace every asset-map UUID (and the VML `assets/…png`
path) with a `data:<mime>;base64,…` URI built from the map's own bytes, done. We
deliberately don't extract the DOM from a headless render — Chrome rewrites
`<img src>` to `blob:null/<uuid>` (severing the verifiable asset linkage) and
strips the VML/MSO conditionals Klaviyo and Outlook need. Headless Chrome is used
instead as a **verification oracle**: it renders the original export and the
flattened file and pixel-diffs them.

**Fidelity gates (all must pass, else non-zero exit):**
- every inlined image's sha256 is present in the export's own asset map (no substitution possible);
- zero residue — no `<script>`, `omelette`, `Babel`, `om-src-id`, `__bundler`, `claude.ai`, or bare-UUID / `assets/…` refs;
- visual regression — flattened render vs. the original export, pixel-diff within tolerance (the apples-to-apples gate). A `--parity-png` comparison is also reported but treated as advisory, since an external render may use different fonts → different line-wrap → vertical reflow.

Useful flags: `--asset-map "assets/<file>=<uuid>"` (force a VML-path resolution),
`--no-verify-render`, `--chrome <path>`, `--tolerance`, `--pixel-threshold`.

This flatten is also the step the email loop needs to reach **Klaviyo** — Claude
Design output can't go to Klaviyo as a runtime doc.

## Promote a design

```bash
python3 scripts/promote.py \
  --flow welcome --variant future-state --step 2 --name "Education" \
  --html ./export.html --receipt ./receipt.txt
```

It copies the HTML to `designs/<flow>/<variant>/<NN>-<slug>.html`, upserts the manifest
(creating the flow/variant if new), sets `approved`/`approved_date`, and commits. Re-running
the same step **replaces** it (idempotent), and a renamed step drops its stale file.

Useful flags: `--flow-name`, `--variant-label`, `--status`, `--step-labels "A,B,C"`,
`--draft` (promote without marking approved), `--no-commit`, `--claude-design-url` /
`--klaviyo-url` (supply or override links the receipt lacks).

**Promoting a flattened derivative:** when `--html` is a flattened file (not the
native artifact), pass `--source-artifact-sha256 <native-export-sha>`. The receipt's
provenance is then checked against that **source-of-truth** hash, while the manifest
records the flattened file under its *own* `sha256` plus `source_artifact_sha256`,
`derivation: deterministic-flatten`, and a `provenance_note`. The flatten hash is
never folded into the source field — the native export remains the source of truth.

## Viewer features

Flow picker · two variant pickers · lockstep step navigator · Desktop(600px)/Mobile(375px)
width · Light/Dark theme (injects `color-scheme` into same-origin frames) · optional
scroll-sync · per-panel metadata strip (status, step name, approval, links out to Claude
Design / Klaviyo) · deep-linkable state in the URL hash (flow + both variants + step +
toggles) so a specific comparison can be shared.

## Hosting

Stay local (`python3 -m http.server`) for day-to-day review. These are unreleased creative
assets — if someone outside needs a link, use a private, access-controlled static host
(Cloudflare Pages / Netlify with Access, or a private Vercel project). **Never** public
GitHub Pages, and never frame a live `claude.ai/design` or Klaviyo web-view (both block
embedding) — always promote the HTML into the repo first.
