# Theo Brief — Mustard Seed: Source-Correct Image Recreation

**Type:** Refinement of the live-text rebuild (`UQdTQi` lineage). Supersedes the open image items in `theo-current-brief.md`.
**Brand:** stasis
**Bar:** the already-sent original, recreated. Not pixel-perfect — "at a glance, roughly equivalent" (Bryce, 2026-05-29).
**Original:** https://www.klaviyo.com/campaign/01KSJYNWB3Y2SQ8G3EZJYBW8AP/web-view

## What's already right — keep it
The live-text rebuild (`UQdTQi`) is correct and stays. Every text-bearing section is selectable live HTML; only the logo and social icons are images. Do not regress any of that. The job below is the two **content images** and getting the whole email to read like the original at a glance.

## The two images — find the source, never the slice
The email is built around two real content visuals:

1. **Hero** — the mustard-**seed** macro with the Stasis Day jar on cream. It is mustard *seed* (macro/product), **not** a mustard plant or flower. Match the subject exactly.
2. **Stimulant-users panel** — the blue brain visual (text-free background, live HTML text overlaid on top).

Disambiguation, because this is where it keeps going wrong:
- "Recreate in HTML" applies to **text and CTAs** — headings, body, buttons, legal. Those are live HTML.
- The **two content images are real photographs/graphics**, placed in image blocks. You do not "recreate" them as HTML, and you do not leave a placeholder. You source the real image.
- The flattened image in the **sent Klaviyo campaign is downstream output with copy baked in**. It is never the source and is never used in the rebuild.

### Where these live — this is the actual source (not the web, not Klaviyo)
The Stasis brand asset library is in our shared Drive, under **`Stasis Adult New Branding`** (https://drive.google.com/drive/folders/1a7tTTexNCEib6FQdojR9Zz6cd9QlfobP). Antidote pulls from here — they are collaborators in this Drive, not a separate vault. Source every image here first. Relevant subfolders:
- **Photography** — https://drive.google.com/drive/folders/14ob4qWi8hHei0zf-qYOTA-gye_bSfujA (product + ingredient + lifestyle shots, incl. the `240624_STASIS_SHOT_…` Day/Night jar set)
- **Creative Assets** — https://drive.google.com/drive/folders/1FuZWkxVha4qyzHzUmLAx_PGwQiI4_k7V
- **Brand Assets** — https://drive.google.com/drive/folders/1Fui8TwJGMGwsiRdmbytoG8B5oKNh-n7U
- **Web Assets**, **Packaging**, plus **Stasis Brand Book.pdf** (https://drive.google.com/file/d/1pa1uQQ-P4NTjWb8xmhaNa_EJE3HoE4El/view) and **Brand Guidelines (Updated)** for imagery direction.

### The two specific assets
- **Hero / mustard seed:** `MustardSeed_Edit.png` is already in the Drive — https://drive.google.com/file/d/1-JFdEXt0PXDlq445wdRbAb5Me7F7gKgY/view. Open it, confirm it matches the original hero subject (mustard *seed* macro, not a plant/flower), and use it. If the hero also needs the Stasis Day jar, the product shots are in the Photography folder.
- **Brain panel:** the brain visual lives in the same library (check Photography / Creative Assets / Brand Assets). Pull the clean version. For the overlay, reuse the text-free brain background you already validated on 5/28 (`stasis-brain-panel-text-free-background-light-top`) — don't re-derive it, don't use the sent slice.
- **If a specific asset genuinely isn't in the library** after you've checked it, surface that as a real gap — a new-shot or new-asset request — and stop. **Do not substitute a web image.** The Annie's Heirloom and Depositphotos guesses were wrong precisely because they skipped the library.

The standing answer to "where does Antidote source imagery" is: **our shared brand Drive (`Stasis Adult New Branding`).** Indexing that library into a usable catalog — each asset mapped to the email module it serves — is the image-system step that ends the hunt for every future email. Flag if you want that scoped as its own task.

## New gate — visual parity to the original
Add this to the receipt and run it before any handoff: composite each section of your render beside the same section of the original web-view, and confirm it's roughly equivalent at a glance. That side-by-side ships with the handoff.

Asset-ID checks (slice absent / image present) are necessary but they are **not** this gate. Passing them while a section still looks wrong is the exact failure we keep hitting ("no change," "doesn't match"). The bar is the look, verified against the original — not the presence of the right hashes.

## Iterate, don't regenerate
Work the **one** template with targeted edits to the flagged section. Stop spawning a fresh Claude Design file and a new Klaviyo template every pass — that's how corrected sections regress and fixes get lost (seven templates in one afternoon on 5/29). Same artifact, edited; capture the authoring trace on the edit.

## Handoff — every time, no exceptions
- **Both links in the same message:** Claude Design and Klaviyo.
- The **visual-parity side-by-side**, the receipt, and a one-line note on where each of the two images was sourced (or what you found if you couldn't pin it).
- Feedback from Bryce arrives as a **section-by-section punch list in the thread**, not as Claude Design comments (those are buggy and don't reliably reach you). Work from the list.
