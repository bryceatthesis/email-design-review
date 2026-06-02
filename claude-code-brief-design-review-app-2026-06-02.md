# Build Brief — Stasis Design Review App

**For:** Claude Code (owns this infrastructure end-to-end)
**Date:** 2026-06-02
**Status:** Approved direction. Build to this spec.

---

## What we're building

A small, data-driven web app for reviewing Stasis email designs throughout the project — not a one-off comparison page. It must let us:

- See any design rendered **in context** (real email HTML, at email widths).
- Drop **two variants of a flow side by side** and compare them.
- **Step through a full flow** in send order, with both columns moving in lockstep.
- Flip between flows.

Three layers, built in this order:

1. **Design repo** — git repo holding the design artifacts + a `manifest.json` catalog. The manifest is the spine; the app renders whatever it declares.
2. **Viewer app** — static, manifest-driven. Generalizes the existing scaffold (see "Starting point").
3. **Promotion step** — a script that, when a design is approved, commits its HTML into the repo and updates the manifest in one motion.

## Ownership / division of labor (decided)

- **Theo = producer only.** He authors designs in Claude Design and emits the approved HTML + his existing handoff receipt (Claude Design block, Klaviyo block, provenance hash). He does **not** own the repo, manifest, or app. Keep his loop scoped to production — it's still fighting capture/provenance issues and shouldn't carry infra.
- **Claude Code = infrastructure owner.** Repo, manifest schema, promotion script, viewer app, deploy. Local repo + network + `.env` access and session endurance make this the right home.
- **Cowork/Claude (Bryce's review partner) = spec + design QA** once staged.

The crux is the **contract** between Theo's output and Claude Code's promotion script — defined below. Get that right and the two halves stay decoupled.

## Step 0 — verify current state before building

We do not know whether Theo already commits approved HTML to a repo anywhere, or only stages in Claude Design + Klaviyo. **Confirm this first** (ask Theo / inspect). If a source repo exists, point promotion at it; if not, the artifact source is the Claude Design export + receipt. Today the `Email Design System` Cowork folder is **not** a git repo and holds no design artifacts — only briefs and `design-compare.html`.

---

## Data model

One concept does all the work: a **flow** has one or more **variants**, each variant is an ordered list of **steps** (one email each).

- **A/B variants** → two variants of the same flow (e.g. `a` vs `b`).
- **Cross-flow / against original** → variants labeled e.g. `current` vs `future-state`.
- **Full flow step-through** → the ordered `steps` of a variant.
- A single campaign (like Mustard Seed) is just a flow with one step and multiple variants (`original`, `v8`).

> Note: "version over time" (v7-vs-v8 history) is **not** a required first-class axis — don't build a time slider. The schema can still hold prior builds as extra variants if we ever want them.

### Repo layout

```
designs/
  <flow-id>/
    <variant-id>/
      01-<step-slug>.html
      02-<step-slug>.html
      ...
manifest.json
index.html            # the viewer app
assets/               # app's own css/js if split out
scripts/promote.js    # promotion tool
```

### `manifest.json` schema

```json
{
  "schema": 1,
  "generated_at": "2026-06-02T18:30:00Z",
  "flows": [
    {
      "id": "welcome",
      "name": "Welcome Flow",
      "step_labels": ["Welcome", "Education", "Offer"],
      "variants": [
        {
          "id": "current",
          "label": "Current (live)",
          "status": "live",
          "steps": [
            {
              "step": 1,
              "name": "Welcome",
              "file": "designs/welcome/current/01-welcome.html",
              "approved": true,
              "approved_date": "2026-05-20",
              "claude_design_url": "https://claude.ai/design/p/...",
              "klaviyo_url": "https://www.klaviyo.com/...",
              "sha256": "…"
            }
          ]
        },
        { "id": "future-state", "label": "Future State", "status": "draft", "steps": [ … ] }
      ]
    }
  ]
}
```

`status` ∈ `live | draft | approved | retired`. `approved`/`approved_date` gate what the app marks as review-ready. Provenance fields come straight from Theo's receipt.

---

## Viewer app requirements

**Starting point:** `design-compare.html` already in this folder. It has the working pieces — 600px email canvas, Desktop(600px, default)/Mobile(375px) width toggle, Light(default)/Dark theme toggle with `color-scheme` injection for same-origin content, local-file/srcdoc loading, optional vertical scroll-sync, horizontal-scroll stage. Generalize it; don't start from scratch.

Add:

1. **Manifest loader** — fetch `manifest.json` on load. All designs load same-origin (`designs/**/*.html` via `fetch` → `srcdoc`), so the theme injection and scroll-sync keep working and framing is never blocked.
2. **Flow picker** — dropdown of `flows`.
3. **Two variant pickers** — left/right column selectors populated from the chosen flow's `variants`. Allow same flow / different variants. (Optionally allow cross-flow comparison later, but flow-scoped is the primary case.)
4. **Step navigator** — prev/next + a step list, driving **both** columns in lockstep. If variants have unequal step counts, show an empty-state on the short side.
5. **Keep** the Desktop/Mobile and Light/Dark toggles and sync-scroll exactly as-is (defaults: Desktop, Light).
6. **Per-panel metadata strip** — variant label, step name, approval status, and links out to Claude Design / Klaviyo from the manifest.
7. **Deep-linkable state** — encode flow + both variants + step + toggles in the URL hash so a specific comparison can be shared.

Keep it dependency-light: vanilla JS is fine and matches the existing scaffold.

---

## Promotion step

A script (`scripts/promote.js`) that turns an approved Claude Design export into a committed, catalogued artifact:

```
promote --flow welcome --variant future-state --step 2 --name "Education" \
        --html <export.html> --receipt <receipt.json>
```

Behavior:
1. Copy HTML to `designs/<flow>/<variant>/<NN>-<slug>.html`.
2. Compute `sha256`; pull `claude_design_url` / `klaviyo_url` / provenance from the receipt.
3. Upsert the manifest entry (create flow/variant if new), set `approved`/`approved_date`.
4. `git add` + commit with a structured message. Idempotent on re-run (same step replaces, doesn't duplicate).

**Trigger = the existing approval gate.** Reuse the receipt that already proves a design passed provenance + parity; "approved" → promoted, no separate manual catalog edit. Theo never needs to know the manifest exists — he tags the handoff with flow/variant/step (or Bryce specifies at promotion time), and the script does the mapping. That tag set **is** the contract.

---

## Hosting

Static app + static files — trivial to stage, but it's unreleased creative, so keep it gated:

- **Dev / local:** `npx serve` (or any static server) from the repo root. Same-origin `fetch` of designs works; no deploy needed for day-to-day review.
- **Shareable (e.g. showing Dan):** private, access-controlled static host — Cloudflare Pages or Netlify with Access/password, or a private Vercel project. **Not** public GitHub Pages (repo contents would be exposed).
- Decision rule: stay local until file-sharing friction is real; reach for the gated deploy only when someone outside needs a link.

---

## Non-goals / guardrails

- No public hosting of in-flight designs.
- No time-slider / historical-diff axis (not requested).
- Don't load Theo with repo or manifest ownership.
- Designs are loaded same-origin from the repo — never rely on framing a live `claude.ai/design` or Klaviyo web-view URL (both block embedding); always promote the HTML into the repo first.
