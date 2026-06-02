# Theo Brief — Stasis Image System (Asset Catalog & Management)

**Type:** New build. This thread is the **image system**, not the Mustard Seed email. Park Mustard Seed — it resumes once the catalog exists, at which point the two images become simple catalog lookups. Don't get pulled back into the email.
**Brand:** Stasis (start with Stasis Adult), expandable to Kids + Thesis later.

## Goal
A real, maintained **catalog of our brand image library** that (a) Bryce can browse and see, and (b) carries your understanding of what each asset is — so the email loop can pull the right image for any module without hunting. This is asset management, not a one-off list: it stays current as new assets land.

## The asset source of truth (Drive — not Klaviyo, not the web)
Catalog over the shared-Drive brand library:

- **`Stasis Adult New Branding`** — https://drive.google.com/drive/folders/1a7tTTexNCEib6FQdojR9Zz6cd9QlfobP
  - **Photography** (`14ob4qWi8hHei0zf-qYOTA-gye_bSfujA`) — product / ingredient / lifestyle shots (incl. the `240624_STASIS_SHOT_…` Day/Night set)
  - **Creative Assets** (`1FuZWkxVha4qyzHzUmLAx_PGwQiI4_k7V`)
  - **Brand Assets** (`1Fui8TwJGMGwsiRdmbytoG8B5oKNh-n7U`)
  - **Web Assets**, **Packaging**, **Stasis Brand Book.pdf** (`1pa1uQQ-P4NTjWb8xmhaNa_EJE3HoE4El`), **Brand Guidelines (Updated)**
- Shared-drive **`Kids + Adult Assets`** (`19gFGf0K-4HJ3xg0dNiY3chMbzR1b2Xsr`) + its photoshoot output folders.

Drive stays the binary store. The catalog is the index over it — every entry points back to its Drive file.

## Where the catalog lives — recommendation
Build it as a **Notion database Bryce can browse** (Gallery view = the visual catalog), not only a file in your repo. Bryce needs to *see* it, with the image and your notes on the same card. Keep a machine-readable mirror (JSON) in your repo only if your pipeline needs to query it programmatically — synced from the Notion DB, secondary to it. Where in Notion it lives is Bryce's call; put it somewhere he and the creative team can find it.

**Nail this first:** Notion does not reliably preview Google Drive links as thumbnails. Before cataloging the whole library, get **one** entry showing a real rendered preview (an uploaded preview image, or a working Drive thumbnail URL) and confirm with Bryce that he can see it. If previews can't be made to render in Notion, don't ship a thumbnail-less table — propose a rendered gallery page instead and confirm the approach with Bryce before scaling.

## Catalog schema (per asset)
- **Name / file name**
- **Preview** — a viewable thumbnail (the part to validate first)
- **Type** — Product / Ingredient / Lifestyle / Brand graphic / Packaging / Icon / Logo
- **Brand** — Stasis Adult / Stasis Kids / Thesis
- **What it is** — your plain-language description of what's actually depicted. **Open and look at each image to write this — do not infer from the filename** (`240624_STASIS_SHOT_002…` tells you nothing). This description is the "understanding" Bryce wants from the system.
- **Has baked-in text** — yes/no (text-baked composites are reference-only, not reusable in new builds)
- **Orientation / crop** + any usable text-free background zones
- **Drive file ID + link** — the canonical pointer
- **Source** — the shoot/folder it came from
- **Suggested use / email module** — where the asset fits (hero, ingredient, lifestyle, CTA, etc.)
- **Status** — Approved / Needs review / Gap

## Real asset management (what makes it a system, not a dump)
- **Repeatable scan:** enumerate the Drive library, create/update one entry per asset, and on re-runs flag new / changed / removed assets so the catalog stays current.
- **Intake:** when a new photoshoot lands in Drive, a re-scan catalogs it. Say how you'd trigger and run that.
- **De-dupe + flag:** mark duplicates; flag text-baked composites as reference-only.
- The catalog becomes the **lookup the email loop uses**: a module needs an image → query the catalog → pull the Drive asset. No more hunting.

## Scope / phasing (don't boil the ocean)
1. **Pilot:** catalog **Stasis Adult → Photography + Creative Assets + Brand Assets** (the folders that feed emails). Prove the whole thing end to end, including a rendered preview Bryce can see.
2. **Bryce reviews the pilot** catalog; adjust the schema from his feedback.
3. **Expand** to Kids + Thesis once the pilot is right.

## Handoff
- The catalog link, with a few entries fully populated and **previews rendering**, before you scale to the full library.
- The schema, the asset count per folder, and any gaps (assets that look missing, or text-baked-only with no clean source).
- Surface honestly per your usual receipt discipline; include any Drive/Notion links involved.

Mustard Seed stays parked. When we return to it, the hero (`MustardSeed_Edit.png`) and the brain visual should already be catalog entries — that's the proof the system works.
