# Theo Brief — Mustard Seed: Full Editable-Module Rebuild

**Type:** Full email rebuild to the editable-module standard. Supersedes the prior "full draft" ask.
**Brand:** stasis

## The problem with `VvjLKt`
The full-email draft converted only the stimulant-users brain panel to live text. Every other text-bearing section — the header/top and hero sections especially — was pulled straight from Klaviyo as a **flattened image slice with the copy baked in**. In preview the text can't be highlighted, which is the tell: it's an image, not live text. That does not meet the standard. We are building an editable, modular email system, not re-staging the old flattened send with one panel swapped.

## The standard — the highlight test
**Every text-bearing section must be live HTML text.** In preview, all headings, body copy, and CTAs must be selectable. If you can't highlight it, it's a flattened image and it's wrong. The only exceptions are genuine graphics with no live copy — logo/wordmark and social icons — which are legitimately images.

## Per-section treatment (from your 12-row ledger)
- **Header / top slice(s)** — currently flattened from Klaviyo. Rebuild as a live-text module. If it sits on background imagery, use the text-free-background + overlay technique (source or recreate a clean background the same way we did the brain panel); do not bake text into the image.
- **Hero / defense panel** — live-text module, same approach.
- **Mustard Seed "job" panel** — live-text module.
- **"Balance for Bold Minds" closer** — live-text module.
- **Stimulant-users brain panel** — already correct (editable overlay, live text). Keep it.
- **Shop CTA** — live HTML bulletproof button, not an image slice.
- **FDA / legal disclaimer** — live text (matters for legibility and accessibility), not an image.
- **Wordmark / logo, social icons (IG / FB / TikTok)** — legitimately images. Keep as images, but each needs a real editable source or explicit approved-reuse, not just a Klaviyo URL (Rule 4 + the `source_assets` ledger).

## Backgrounds / imagery
Where a section needs an image behind live text, source the real asset (Drive / editable master) or recreate it text-free like the brain background. No baked-text composites for text-bearing sections.

## Authoring + proof (Path A)
- Author the full email in **Claude Design**. Capture the **live generative-turn network trace** — `write_files → record_asset → release_turn` — at authoring time. Do **not** resume-after-submit and fetch the file via `GetFile`; that's what left `VvjLKt` unprovable.
- Lead the handoff with the `claude_design` provenance block (Rule 2). Stage in `klaviyo-stasis` (`YsCgQB`, `hello@takestasis.com`). Post the full receipt including the `source_assets` ledger.

## Render-back
- Full desktop + mobile renders, and confirm the **highlight test passes** — text selectable in every content section.

## Run discipline
- Use sub-agents for the parallel section builds (don't run single-threaded).
- Self-debug the Klaviyo account state before staging — the browser has silently sat in Thesis with a Stasis `company_id`; confirm `ST Stasis`.
- `klaviyo-stasis` only.

The goal isn't a picture of the Mustard Seed email — it's the Mustard Seed email rebuilt as editable modules. The highlight test is how we both know it's real.
