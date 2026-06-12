# E5 — Your First 30 Days on Stasis — Step 0 source-asset table, undefined

Step 0 (blocking) sourcing pass per `email-build` / `email-image-source` Mode A, 2026-06-10.
Scope: every image-bearing role from `e5-module-map.md` (1 content + 2 hybrid rows). **§4 update
2026-06-10: the wordmark header (01) is NOT a pure-CSS rebuild (spec §4 RESOLVED — the wordmark is
the LOGO ASSET, never typed text); image row added below.** Pure-CSS rebuild
elements get no row — they are code, not assets: outlined headline box (02),
30-dot grid (03), headline/body blocks (04, 10), CTA pills (05, 13, 14), promo band (06), stat
numerals/labels (07/09 text), pricing cards (11, 12), disclaimer (15), closing formula lockup +
domed shaped edge (16).

*(Header note: "undefined" in the title is the literal string requested by the build order — it
appears to be an unrendered template variable, likely the build/run id. Kept verbatim.)*

| role | source_link | text_baked | sha256 | notes |
|---|---|---|---|---|
| e5-01 header wordmark — STASIS logo, black on Creme `#F4EFEB` · kit rendition `wordmark-black-1200.png` | Derived 2026-06-10 from catalog "Stasis blue wordmark" (Status **Approved**) → Air canonical https://app.air.inc/a/bFVACbwGW/98e78704-52bb-4c1b-ab2d-1fd76df15180 ; Drive backup https://drive.google.com/file/d/1ZOo4f6yTl3IfDWL1_1JxyoYodAtaxitk/view ; master staged `_incoming/welcome-flow-VUD7gW/assets/brand/stasis-wordmark-blue.png` | yes (logo glyphs are the asset itself — brand mark) | master `661cd181b9099c0999713368353b280fdebd52c4395051e99993b0a18db36042` → rendition `2eebc27153336d56050972edd3525c3558a2cf68391f532353ef1a91f73ed637` (1200×271 RGBA, 31,023 B) | Tint op: alpha channel resampled alone (LANCZOS 4336×981→1200×271), RGB set constant `#000000` — master geometry/alpha preserved exactly, no crop. Display in E5: **169×38 CSS px, centered** on Creme — measured from `reference/welcome-flow-VUD7gW/e5-composite.png` (2×): baked-mark bbox x 431–768, y 74–149 = 338×76 @2×; geometry vs rendition alpha IoU 0.978. The build's typed STASIS span (26px) must be swapped for this image. Full kit + measurements: `_incoming/welcome-flow-VUD7gW/assets/brand/logo-usage.md`. |
| e5-08 product still-life (blue water glass + frosted DAYTIME jar + copper capsules, glossy reflective surface) | Catalog: `240624_STASIS_SHOT_006_SHELF_SHOT_STACK_086.jpg` https://app.notion.com/p/28dec93cb6e4458a9d14510e1efbc119 — Air canonical https://app.air.inc/a/bf6cokwMJ/f831389d-f0e5-4356-acf8-dc2bdafcc113 — Drive backup https://drive.google.com/file/d/1Uc_yWCliLrEpqt69cPc139xY85T8lFch/view?usp=drivesdk | yes (product-label text only — SUN/MON/TUE, DAYTIME, STASIS packaging copy; no campaign/layout text) | `c15e130e047b13bcf1e924bd1412ad343d947f63679fa9d1306a4f4281017440` (reused approved donor bytes: 58844-byte 1200×603 JPEG extracted from `designs/welcome-quiz/html-v1/05-your-first-30-days-on-stasis.html` alt "Stasis Daytime jar with water glass and capsules"; sha cross-checks EXACTLY against module-map provenance sha for `e5-08.jpeg`) | Canonical RESOLVED by visual match of the Drive preview (identical set: glass left, jar right, capsule placement matches; send slice is a tighter crop of the master). Catalog status is "Approved candidate" (not plain Approved) — flag to Bryce at review; bytes reused are already-approved donor bytes, so not blocking. Air board: Photography / Product Imagery / Product Lifestyle Imagery. |
| e5-07 stat icon A — orange two-tone capsule (flat brand icon) | GAP — catalog lookup done, no entry for this glyph. Probable home: Air board "Brand Elements / Iconography" (where the cataloged icon family lives). Closest cataloged icon, NOT a match: "Third Party Tested capsule icon" (black/white split capsule) https://app.notion.com/p/42d70ca2ed204ef0837d151ddc2a5577 | no | n/a — no approved bytes exist in any donor build (html-v1/05 shipped flat colored-circle placeholders, not icons) | Needed for stats panel 1 ("96% / 88%"). Options for Bryce: (a) Theo/creative pull the icon set from Air Iconography board + add to catalog (candidate catalog addition); (b) approve clean SVG recreation of the flat glyph; (c) sanctioned fallback — bake the icon row as a single image once art is sourced. Never crop from the Klaviyo slice. |
| e5-07 stat icon B — teal brain (flat brand icon) | GAP — catalog lookup done, no entry. Probable home: Air "Brand Elements / Iconography". NOT a match: "Green brain visual" (Getty photographic brain, Drive-canonical exception, status Needs review + Getty rights check) https://app.notion.com/p/00a05f9ff431465fa6a33cfd3ac12561 | no | n/a — no approved bytes in any donor build | Same options as icon A. Do not substitute the Getty brain photo — wrong asset class (photo vs flat icon) and unresolved stock rights. |
| e5-09 stat icon C — teal hourglass (flat brand icon) | GAP — catalog lookup done, no entry. Probable home: Air "Brand Elements / Iconography". | no | n/a — no approved bytes in any donor build | Needed for stats panel 2 ("63% / 85%"). Same options as icon A. |
| e5-09 stat icon D — blue "Zz" sleep mark (flat brand icon) | GAP — catalog lookup done, no entry. Probable home: Air "Brand Elements / Iconography". | no | n/a — no approved bytes in any donor build | Same options as icon A. Glyph is two offset weight-900 "Z" letterforms in royal-adjacent blue — if Bryce picks recreation, this one is the most trivially CSS/SVG-safe of the four. |

## Derived-crop kit rows (2026-06-10, spec §8.5 sanctioned mode — Bryce live review)

> Resolves the four icon GAP rows above. The old "Never crop from the Klaviyo slice" instruction in
> those rows is **superseded by §8.5.2**: derived crops from the sha-verified original send slices are a
> sanctioned sourcing mode (exact sourcing, not approximation). A future Air "Brand Elements /
> Iconography" pull can still upgrade these to canonical masters; until then these crops are the build
> bytes. Crops live in `_incoming/welcome-flow-VUD7gW/assets/crops/` (full manifest: `crops-manifest.md`
> there). Crop boxes are PIL `(left,top,right,bottom)`, slice-native px (1200-wide = 2×).

| role | source_link | text_baked | sha256 | notes |
|---|---|---|---|---|
| e5-07 stat icon A — orange two-tone capsule (`crops/e5-stat-icon-capsule.png`, 89×53) | derived crop of approved send slice e5-07 — sha matches module-map provenance row 7 exactly (1200×649 JPEG, 60,254 B; CloudFront origin `e6f76bfd-…361.jpeg`; CDN URL must NOT appear in build) | no | slice `79119daf11a6894cbdb4a707a726c2ee3b9e83e2cde572eeb46a21b050675719` → crop `29882776226195050cc12e1b5ea12382e7121edd518e90adda2f98baab4c977f` | Crop box (115,98,204,151); off-white `#F7F7F7` panel bg preserved; dominant `#F8986F`. Stats panel 1 (96%). |
| e5-07 stat icon B — teal brain (`crops/e5-stat-icon-brain.png`, 77×76) | derived crop of approved send slice e5-07 (same slice as above) | no | slice `79119daf…` (above) → crop `49e3ce4cceaf62e6aacfe5edb9750d2dbeab35d23ca6eada1179ea5a154e1f42` | Crop box (637,77,714,153); off-white bg; dominant `#20D8A8` — note the E5 brain is TEAL (the E2 panel's brain is royal blue). Stats panel 1 (88%). |
| e5-09 stat icon C — teal hourglass (`crops/e5-stat-icon-hourglass.png`, 59×75) | derived crop of approved send slice e5-09 — sha matches module-map provenance row 9 exactly (1200×750 JPEG, 62,647 B; CloudFront origin `97d2d319-…269.jpeg`; CDN URL must NOT appear in build) | no | slice `6b8c26bfa48bfbd0d6c5efede97bc3cea6432c4718b93c7c10bc444f3a0ff2f6` → crop `947bc82cfc07203b4f55ffc3873bc7ac680475e85a8cd4d46a09b7e8caa52fa6` | Crop box (131,118,190,193); light-grey `#F4F4F4` bg preserved; dominant `#20D8A8` — teal in E5 (lime in E2). Stats panel 2 (63%). |
| e5-09 stat icon D — blue "Zz" sleep mark (`crops/e5-stat-icon-zz.png`, 75×75) | derived crop of approved send slice e5-09 (same slice as above) | no | slice `6b8c26bf…` (above) → crop `614dc6be714246b3e4752c4afad8812c2d34c915e6f2a0212868d424b9989392` | Crop box (637,118,712,193); light-grey bg; dominant `#3868E0` (royal-adjacent). Stats panel 2 (85%). |

These slot into the reserved space above each stat rule in
`designs/welcome-quiz/cc-from-spec/05-your-first-30-days-on-stasis.html` (see Build outcome below —
the icons were omitted at build time pending sourcing; that gap is now closed at the asset level).

## Review-fix pass (2026-06-10, Bryce live review — assets embedded)

All five image assets below are now EMBEDDED as base64 data URIs in
`designs/welcome-quiz/cc-from-spec/05-your-first-30-days-on-stasis.html`; every embed verified by
round-trip extraction (embedded bytes sha == source bytes sha, byte-identical — PNGs shipped
unmodified, no re-encode).

| role | embedded asset | sha chain (source → crop → embed) | display |
|---|---|---|---|
| header wordmark §4 | `brand/wordmark-black-1200.png` (1200×271 RGBA, 31,023 B) | master `661cd181…6042` → rendition `2eebc271…4637` → embed `2eebc271…4637` (byte-identical) | 169×38 CSS px, centered on Creme; replaces the typed 26px STASIS span (§4 violation closed) |
| e5-07 stat icon A — orange capsule | `crops/e5-stat-icon-capsule.png` (89×53) | slice `79119daf…0719` → crop (115,98,204,151) `29882776…c977c` → embed identical | 44×26 CSS, panel-1 left cell, above the 1px black rule |
| e5-07 stat icon B — teal brain | `crops/e5-stat-icon-brain.png` (77×76) | slice `79119daf…0719` → crop (637,77,714,153) `49e3ce4c…4f42` → embed identical | 38×38 CSS, panel-1 right cell |
| e5-09 stat icon C — teal hourglass | `crops/e5-stat-icon-hourglass.png` (59×75) | slice `6b8c26bf…3ff6` → crop (131,118,190,193) `947bc82c…2fa6` → embed identical | 30×38 CSS, panel-2 left cell |
| e5-09 stat icon D — blue Zz | `crops/e5-stat-icon-zz.png` (75×75) | slice `6b8c26bf…3ff6` → crop (637,118,712,193) `614dc6be…9392` → embed identical | 37×37 CSS, panel-2 right cell |

Stat-panel treatment corrected to the measured designed original (slices e5-07/e5-09 @2×): cells
202px CSS at x58/x317 (gutters 58/57/81), 1px BLACK rules, BLACK 75px/500 numerals (glyph 58px =
baked; the royal `#3D72E6` numerals were e5-flattened recreation drift, NOT the designed send),
black 21px/26px/500 labels with designed line breaks. Panel-2 bg set `#F4F4F4` (= baked icon-crop
bg, seamless; was `#F3F3F3`). No other image assets changed; e5-08 product still-life embed
untouched (`c15e130e…7440` re-verified at this pass).

## Donor inventory (verified by extraction, 2026-06-10)

`designs/welcome-quiz/html-v1/05-your-first-30-days-on-stasis.html` contains exactly 2 `<img>` tags:

1. alt "Stasis Daytime jar with water glass and capsules" — base64 JPEG, 58844 bytes, 1200×603,
   sha256 `c15e130e…7440` == module-map e5-08 provenance sha. This is the reuse source above.
2. alt "" — URL-encoded inline `data:image/svg+xml` dome arc (600×54, `Q300,-10` curve), i.e. the
   shaped-edge transition. **Code, not an asset** — no table row. Build note: it hard-codes fill
   `%23F3EFE9`; canonical Creme is `#F4EFEB` (spec §2/§10.5) — rebuild the arc per spec §8
   (fixed-height row, CSS dome), don't copy this SVG verbatim.

The four stat icons have no donor bytes anywhere in `designs/` (html-v1/05 used 46px colored-circle
`<div>` placeholders; the cc-from-spec/03 "Stasis capsule" PNG is a photographic render, not the
flat icon). Zero CloudFront/Klaviyo references involved in any reuse.

## Build outcome (2026-06-10, `designs/welcome-quiz/cc-from-spec/05-your-first-30-days-on-stasis.html`)

E5 was built with the four e5-07/e5-09 stat icons **omitted** (the build-order-sanctioned fallback:
live-text stats + divider rules shipped without icon art; the old slice was NOT baked). The four
icon rows above remain open gaps — if Bryce approves an Air pull or SVG recreation, the icons slot
into the reserved space above each stat rule. e5-08 was embedded from the sha-pinned approved donor
bytes (`c15e130e…7440`, verified at build and re-verified by round-trip extraction).

**SUPERSEDED 2026-06-10 (review-fix pass, see section above):** the icon gap is closed — all four
derived-crop icons are embedded in the build, the typed wordmark is swapped for the logo image, the
brand font kit is embedded, and the stat treatment now matches the measured designed original.

## Catalog lookups performed (Stasis Adult Image Catalog, collection://d7c05078-a1e2-4f25-955f-4de690d9959f)

- Still-life queries (×3) → resolved to `240624_STASIS_SHOT_006_SHELF_SHOT_STACK_086.jpg` (visual match via Drive preview).
- Icon queries (×3) → catalog icon family found ("Third Party Tested capsule", "Daytime sunburst",
  "Nighttime crescent", "Clinically Studied plus", "Transparently Formulated eye", "Maximum
  Efficacious Dosages arrow") but none of the four E5 stat glyphs is cataloged → recorded as gaps,
  candidate catalog additions for Theo.
