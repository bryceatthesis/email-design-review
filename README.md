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
scripts/promote.py     # promotion tool
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
