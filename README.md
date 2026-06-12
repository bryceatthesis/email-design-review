# Email Design System

A multi-brand system for building marketing emails as live-text HTML, reviewing them
in a small data-driven web app, and staging them in Klaviyo as drafts. Brand truth
lives in brand packs under `brands/<brand>/` (Stasis today; Thesis later); the process
and tooling are brand-agnostic.

The review app is **manifest-driven**: `manifest.json` is the spine, and the viewer
renders whatever it declares. Designs are committed into `designs/` and served
same-origin, so theme injection and scroll-sync work and framing is never blocked.

## Run the review tool

```bash
python3 -m http.server 8753
# open http://localhost:8753/
```

A static server is required — opening `index.html` over `file://` will fail because the
app fetches `manifest.json` and the design files over HTTP.

## Layout

```
brands/
  <brand>/                      # brand pack — all brand truth lives here, never mixed
    design-language.md          # the binding visual spec (values pinned + sourced)
    components/                 # extracted, approved section patterns (+ catalog.md index)
    asset-sources.md            # canonical asset chain, hosted font/image tables (sha-pinned)
designs/
  <flow-id>/
    <variant-id>/
      01-<step-slug>.html       # promoted, reviewable HTML
manifest.json                   # the catalog the viewer reads
index.html                      # the viewer app (vanilla JS, no build step)
overview.html                   # static share-out page
reference/
  send-prep-spec.md             # brand-agnostic send-prep rules (footer, coupon zones, hosting, budget)
  <flow>/                       # per-flow artifacts: module maps, source-asset tables, composites
scripts/                        # local pipeline tooling (see note below)
  promote.py                    # promotion tool — lands HTML in designs/ + upserts the manifest
  check_modes.py                # THE verification gate (reflow + light-only + offenders + screenshots)
  check_reflow.py               # legacy subset of check_modes (reflow only)
  _cdp.py                       # tiny stdlib Chrome DevTools Protocol client (shared)
```

`reference/stasis-email-design-language.md` is a stub: the Stasis spec moved to
`brands/stasis/design-language.md` when the repo went multi-brand (section numbers
unchanged).

> **Note:** `scripts/` is gitignored and does not appear on the public mirror, along
> with the skills and internal process docs. The public repo is the review app only —
> `index.html`, `overview.html`, `designs/`, `reference/`, `manifest.json`.

## Lifecycle

Each step is a skill (local, in `.claude/skills/`); Claude Code is the single builder
and the only writer to this repo.

1. **email-design** (net-new only) — copy → section mapping against the brand pack's
   component catalog → blocking imagery sourcing → 2–3 sourced direction options
   promoted into the review tool → Bryce picks. Origination is human.
2. **email-build** — assembles live-text HTML from the brand pack (spec + components),
   after a blocking image-sourcing step (`email-image-source`: canonical masters only,
   sha-pinned; an unresolvable role stops the build). Must pass the modes gate, then
   promotes `in-review`.
3. **Review / approval** — Bryce reviews in this app (locally or on the hosted mirror).
   Promotion is never approval; his eye is the gate. A fix is a direct edit +
   re-promote, not a regeneration.
4. **email-send-prep** — approved build → sendable copy: legal footer, coupon zones per
   `reference/send-prep-spec.md` §2, production-hosted assets, total HTML < 95 KB —
   and proof that nothing else changed. Promoted as its own variant, `in-review`.
5. **klaviyo-stage** — verified send copy → Klaviyo draft (flow A/B variant or full
   campaign), with byte-exact editor injection and invariant-based stored-copy
   verification.

**Publishing, scheduling, and sending are always Bryce's click.** Nothing in this
system reaches a customer on its own.

## Data model

A **flow** has one or more **variants**; each variant is an ordered list of **steps**
(one email each).

- **A/B compare** → two variants of the same flow (e.g. `original` vs `cc-from-spec`).
- **Build → send-prep lineage** → variants of the same flow (e.g. `cc-from-spec`
  approved builds vs `cc-send` send copies).
- **Full-flow step-through** → the ordered `steps` of a variant; both columns move together.
- **A single campaign** → a flow with one step and multiple variants.

Variant `status` ∈ `live | draft | approved | retired | in-review`. Each step carries
`approved` / `approved_date` (promotion writes them false/null), its `file`, its
`sha256`, and optional `claude_design_url` / `klaviyo_url` links plus provenance fields
(`source_artifact_sha256`, `derivation`, `provenance_note`) where they apply.

## Verify before promoting

`scripts/check_modes.py` is the gate every build must pass:

```bash
python3 scripts/check_modes.py designs/<flow>/<variant>/01-<slug>.html \
  --out /tmp/modes-e1 --profile /tmp/modes-profile-e1
```

With local headless Chrome it checks reflow at 375 and 600 (`scrollWidth` must equal
the frame width, same srcdoc-iframe technique as the viewer), scans for overflow
offenders at 375 (full dump to `offenders-375.json`), verifies the light-only
declarations are present, and emits 375-light / 600-light / 600-darksim screenshots to
eyeball against the parity target. Exit 0 = pass; 4 = reflow overflow; 5 = light-only
declarations missing. Always pass a unique `--profile` so parallel runs never collide.
`check_reflow.py` is the legacy reflow-only subset; `check_modes.py` is the gate.

## Promote a design

```bash
python3 scripts/promote.py \
  --flow welcome-quiz --variant cc-from-spec --step 2 --name "Smarter Balance" \
  --status in-review --html ./build.html
```

It copies the HTML to `designs/<flow>/<variant>/<NN>-<slug>.html`, upserts the manifest
(creating the flow/variant if new), and commits + pushes. Re-running the same step
**replaces** it (idempotent), and a renamed step drops its stale file. If `--html`
already sits at its canonical `designs/` path (an in-place edit), promotion re-hashes
and updates the manifest without copying.

**The promotion contract:** promotion is never approval. Every promote writes the step
with `approved: false` / `approved_date: null`, and new variants default to status
`in-review`. `--status` accepts `draft | in-review | live | retired` — `approved` is
deliberately not a choice; approval is a separate, explicit manual step after Bryce
reviews.

Useful flags: `--flow-name`, `--variant-label`, `--step-labels "A,B,C"` (the step
navigator's labels — plain English, named by email topic), `--claude-design-url` /
`--klaviyo-url` (links shown in the viewer), `--no-commit`, `--no-push`. Provenance
flags for derivative files (`--receipt`, `--source-artifact-sha256`,
`--allow-sha-mismatch`) remain from the legacy pipeline and still enforce hash checks
when used.

## Viewer features

Design (flow) picker · two variant pickers · lockstep step navigator (labelled from the
flow's `step_labels`) · Desktop (600px) / Mobile (375px) width · Light/Dark theme ·
optional scroll-sync · per-panel step name with links out to Claude Design / Klaviyo
when the manifest has them · deep-linkable state in the URL hash (flow + both variants
+ step + toggles) so a specific comparison can be shared.

Dark mode is a **simulation** (full-inversion filter), with one exception: emails that
pin `color-scheme: light only` render unchanged, matching Apple Mail / iOS Mail.
Neither is a faithful per-client preview — confirm real dark rendering in a live client
before shipping.

## Hosting

Day-to-day review stays **local** (`python3 -m http.server`) — zero latency, no failure
modes, and that's where `promote.py` lands designs. The hosted site is only a **mirror**
for share-out moments (a link to send the team).

The mirror is **public GitHub Pages**, served from this repo's root on `main`
(`bryceatthesis.github.io/email-design-review`). `promote.py` pushes on every promotion
(default on; `--no-push` to skip, and it warns-and-skips if no `origin` remote exists,
so local-only promotion keeps working). Pages serves the review app only; pipeline
machinery (`scripts/`, skills) and internal working docs are gitignored so they're
never published.

Never frame a live `claude.ai` or Klaviyo web-view (both block embedding) — always
promote the HTML into the repo first.
