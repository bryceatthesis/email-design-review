# Stasis Email Design Language

**Status:** APPROVED 2026-06-08 (conflicts resolved §10). Binding visual spec.
**Date:** 2026-06-08
**Purpose:** A written, binding visual spec for Stasis email. Builders (Claude Design or human) follow this when there is *no* composite to imitate, and graders check against it. It exists because Claude Design follows text instructions, not image inspiration — wherever a treatment was only *referenced*, output drifted (E4: wrong wordmark tracking, doubled badge, testimonial alignment off). Every rule below is pinned to a concrete value and a source.

## How to read this doc

Each value is tagged:

- **`[EXTRACTED]`** — measured from a primary source: a live-send HTML file, or a pixel sample of a send composite/slice. The source is named inline.
- **`[INFERRED — confirm]`** — not present in any source I could read; reasoned from context. Do not treat as binding until confirmed.
- **canonical** — the value Bryce fixed as the standard on 2026-06-08 where sources disagreed (the decision record is in [§10](#10-conflicts--resolved-2026-06-08)).

**Source-of-truth order** (per the build brief): for *email-specific* treatment, the live sends win over the brand-wide books. So hex/px below are taken from the actual welcome-flow sends (E2–E5) first, with brand-book palette *names* cross-referenced where known.

**Two design vocabularies exist in the source material** — read this first, it explains every "two values" below:

| | Original sends (`step*.html`, send composites/slices) | Recreations that passed visual judgment (`e{2-5}-flattened.html`) |
|---|---|---|
| Sans font | `Antartica` (brand custom face) | `'Helvetica Neue', Arial` (email-safe substitute) |
| Display tracking | n/a (mostly baked into images) | tight / negative (−0.02 to −0.05em) |
| Color encoding | mostly **baked into image slices** | **live HTML/CSS** |

For an *email* design language, the recreations are the more useful reference for live-text geometry (they're what actually renders as text in an inbox), and the original composites are the reference for color and overall composition. This doc fuses both.

---

## 1. Layout fundamentals

| Rule | Value | Source |
|---|---|---|
| Content width | **600px** max (`max-width:600px; width:600`) | `[EXTRACTED]` e4-flattened.html body table |
| Outer background | `#FFFFFF` | `[EXTRACTED]` e4-flattened.html `<body>` |
| Horizontal gutters | **40px** (header) / **32px** (card sections) / **48px** (CTA + closing) per side | `[EXTRACTED]` e4-flattened.html `<td>` padding |
| Grid | multiples of **4px** for all spacing and type | `[EXTRACTED]` Stasis Digital Web Style Guide → "Grid system… multiples of 4px" |
| Vertical section rhythm | header `30/40/22/40` · card section `30/32/8/32` + card inner `26/28/28/28` · CTA section `22/48/30–40/48` · promo band `26–30/40–48` · closing lockup `8/48/48/48` (px, T/R/B/L) | `[EXTRACTED]` e4/e5-flattened.html |
| Default alignment | hero / headlines / CTAs **center**; testimonial card contents **left** | `[EXTRACTED]` e4-flattened.html (`text-align` per section) |

---

## 2. Color tokens

Hex below are **`[EXTRACTED]`** (live-HTML values, or pixel-samples of the named send slice) or **canonical** (Bryce's 2026-06-08 call where sources disagreed). Brand-palette **names** are from the Stasis Digital Web Style Guide; its swatches are images, so the *name↔hex binding* is `[INFERRED — confirm]` against the style-guide swatch page or the `.fig` masters (see [§9](#9-inferred-items-consolidated--confirm-before-binding)).

### Core palette

| Token | Email hex | Role | Brand name (inferred) | Source |
|---|---|---|---|---|
| **Spice / CTA orange** | **`#FF541E`** (canonical) | Primary CTA pill fill | "Spice" | `[EXTRACTED]` e5-flattened + step-1 brief; e4-flattened shipped `#FF5128`; baked original `#FD531D` |
| **Lime / chartreuse-yellow** | **`#EEEF78`** (canonical, saturated) | Yellow header bands, promo pill, yellow quote card | "Lime" | `[EXTRACTED]` e2-01, e4-03 (baked); recreation shipped `#F0F36A` (not used) |
| **Royal / Electric Blue** | **`#3D72E6`** (canonical) | Formula-lockup pills, closing headline, stat numerals | "Electric Blue" / "Blue" | canonical (step-1 brief line 62); extracted range `#3F73E6` e4-flattened / `#3B6FE4` e5-flattened |
| **Navy (hero / ink)** | `#011D59` hero · `#0E1A38` text-navy | Navy hero background; near-black headline/body ink | "Blue" (dark) | `[EXTRACTED]` e2-02→05 (hero); e3/e4/e5-flattened (ink) |
| **Creme** | **`#F4EFEB`** (canonical) | Closing-lockup panel, E5 full background | "Creme" | canonical (step-1 brief line 62); e4/e5-flattened shipped `#F3EFE9` |
| **Promo black** | `#000000` | Promo / discount band background | "Black" | `[EXTRACTED]` e4-05, e5-06, e2-14 (bg); e4/e5-flattened promo `<td>` |
| **Charcoal (body text)** | `#222427` | Body copy on light | "Dark Grey" | `[EXTRACTED]` step*.html (43×); e2-flattened body |
| **White** | `#FFFFFF` | Page bg, text on dark, filled-pill bg | "White" | `[EXTRACTED]` throughout |

### E4 testimonial quote-card trio

**RESOLVED 2026-06-08:** the **saturated baked originals are canonical**; the softer recreation fills are **not used**. The harmonized dark text colors hold on the saturated fills.

| Card | Canonical fill (baked) | Re-sample confirm | Recreation fill (not used) | Harmonized text color | Source |
|---|---|---|---|---|---|
| Yellow | **`#EEEF78`** | `#EFF079` | `#F0F36A` | navy `#0E1A38` | `[EXTRACTED]` e4-03 |
| Peach | **`#FD9A70`** | `#FE9B71` | `#FF9B70` | dark brown `#3A1A0E` (quote `#2A1206`) | `[EXTRACTED]` e4-06 |
| Teal | **`#24DEAD`** | `#25DFAE` | `#BDEBDF` | dark green `#0B3D32` | `[EXTRACTED]` e4-10 |

> The module maps had previously estimated the trio as `#F4A87C` (peach) / `#2FE0A6` (teal). Pixel sampling the actual send slices gives the canonical values above. Use the sampled values, not the estimates.

### Secondary / accents

| Token | Email hex | Role | Source |
|---|---|---|---|
| Teal section rule | `#25DFAE` | 4px accent rule at section seams | `[EXTRACTED]` e4-flattened `border-bottom:4px solid` |
| Light Blue | `#A4CEFD` (+ `#689EF0`) | Chart/illustration fills (E5) | `[EXTRACTED]` e5-08 sample |
| Legacy link blue | `#197BBD` | **RETIRED from display 2026-06-08** — was the original-send live-text/table fallback blue; use Royal `#3D72E6` instead | `[EXTRACTED]` step*.html (92×) |

---

## 3. Type system

### Families

| Use | Email face (embedded) | Fallback stack | Source |
|---|---|---|---|
| Display / headers / labels / CTA | **`Antarctica`** (brand geometric sans — weight matched per role against the baked originals) | `'Helvetica Neue', Arial, sans-serif` weight 900 | RESOLVED 2026-06-10; Drive `Antarctica WOFF2` folder (`1ZUqAg9c89xHptVWl8p_UeTN0Rv_K_QeB`) |
| Testimonial quotes / body serif | **`Tiempos Text`** — **UPRIGHT, never italic** | `Georgia, 'Times New Roman', serif` upright | RESOLVED 2026-06-10; Drive WOFF2 (`1CMiAgacGWxrgWGL3XEMTvEpgUqO6s6MC`) |

> **RESOLVED 2026-06-10 (Bryce live review — supersedes §10.6 and the earlier no-@font-face rule):** the brand faces ARE available as licensed woff2 in Drive and **must be embedded via `@font-face`** (progressive enhancement: Apple Mail et al. render the brand face; Gmail falls back to the tuned Helvetica/Georgia stacks). The prior rule was based on a misspelling — the face is **Antarctica**, not "Antartica"; sourcing failed on the typo and Helvetica substitution shipped, which Bryce rejected ("text weighting is really not correct across the board"). Per-role faces/weights are pinned by **rendering candidates against the baked original text and matching** — parity with the designed send beats the abstract size table below. Production hosting (vs data-URI embed) is a separate Bryce decision before any Klaviyo send.
>
> **Italics: the designed sends use UPRIGHT serif for testimonials.** The italic in e3/e4-flattened was recreation drift, not brand. Never italicize quotes ("to change from normal to italics is crazy" — Bryce, 2026-06-10).

### Weights

`900` (display / headlines / wordmark / pills / stat numerals) · `800` (CTA label, sub-emphasis) · `600` (lead paragraphs) · `500` (body) · `400` (serif quotes, disclaimers). `[EXTRACTED]` across e2-e5-flattened.

### Scale (live-text, 600px desktop → mobile override)

| Role | Size / line-height / tracking | Weight | Source |
|---|---|---|---|
| Closing headline ("BALANCE FOR BOLD MINDS") | **48px** / 0.98 / −0.05em → 40px mobile | 900 | `[EXTRACTED]` e4-flattened `.h-closer` |
| Hero / section H1 | **40–42px** / 0.98–1.04 / −0.04em → 34px mobile | 900 | `[EXTRACTED]` e3-flattened hero; e5-flattened `.h-box` |
| Stat numeral | **58px** / 0.9 / −0.04em → 54px mobile | 900 | `[EXTRACTED]` e5-flattened `.stat-num` |
| H2 / section subhead | **30–32px** / 1.08 / −0.03em | 900 | `[EXTRACTED]` e3/e5-flattened `.h-lg` |
| Promo discount line | **22–24px** / 1.0 / −0.01em, uppercase | 900 | `[EXTRACTED]` e4/e5-flattened promo |
| Lead paragraph | **19–20px** / 1.34 / −0.02em | 600 | `[EXTRACTED]` e2/e3-flattened |
| Serif quote | **16–17px** / 1.5 / (none), *italic* | 400 | `[EXTRACTED]` e3/e4-flattened |
| Body | **15px** / 1.5 / −0.01em | 500 | `[EXTRACTED]` e2-flattened |
| CTA label | **15px** / 1.0 / **+0.18em** (≈3px), uppercase | 800 | `[EXTRACTED]` e4/e5-flattened CTA |
| Card heading | **15px** / 1.1 / **+0.06em**, uppercase | 900 | `[EXTRACTED]` e4-flattened card headings |
| Caption / stat label | **14px** / 1.3 | 600 | `[EXTRACTED]` e5-flattened |
| Disclaimer / footnote | **11px** / 1.55 (dagger marks `10–11px`, `vertical-align:top`) | 400 | `[EXTRACTED]` e3/e5-flattened footnotes |

### Tracking rule (this is what drifts — pin it)

- **Display type is TIGHT: negative tracking** (−0.02em headlines, up to −0.05em on the big closer). `[EXTRACTED]`
- **Only small uppercase labels get positive tracking** (CTA +0.18em, card heading +0.06em, hero badge +0.12em) — for legibility at small caps. `[EXTRACTED]`
- Any positive tracking on a large headline or on the wordmark is **wrong** (see [§4](#4-wordmark)).

---

## 4. Wordmark

> **RESOLVED 2026-06-10 (Bryce live review — supersedes the typed-text pattern below): the wordmark is the LOGO ASSET, never typed text.** "The logo has to be the logo." Use the approved image: catalog entry "Stasis blue wordmark" (Status Approved; Air canonical `app.air.inc/a/bFVACbwGW/98e78704-52bb-4c1b-ab2d-1fd76df15180`; Drive backup `1ZOo4f6yTl3IfDWL1_1JxyoYodAtaxitk`; staged at `_incoming/welcome-flow-VUD7gW/assets/brand/stasis-wordmark-blue.png`, sha `661cd181…`, 4336×981 transparent RGBA). White/black variants are flat-tint derivations of the same asset (geometry untouched, derivation documented); a verified white 600px copy is staged alongside (sha `d040df08…`). Size/placement per the original being recreated (measure the baked wordmark). Typed STASIS remains acceptable only inside the §5.2 formula-lockup pills (those are typographic pills, not the logo).

Historical reference — the typed approximation this section used to specify (kept for the tracking rule, which still applies to any incidental typed brand text). Pinned from `e4-01.jpeg`:

| Property | Value | Source |
|---|---|---|
| Glyph | `STASIS`, **all caps** | `[EXTRACTED]` e4-01.jpeg |
| Weight | **heaviest available — `900` / Black** | `[EXTRACTED]` e4-01.jpeg (heavy strokes); e4-flattened `font-weight:900` |
| **Tracking** | **TIGHT — `letter-spacing:0` to `−0.01em`. Letters nearly touch.** | `[EXTRACTED]` e4-01.jpeg (glyphs nearly kerned together) |
| Case | uppercase (`text-transform:uppercase`) | `[EXTRACTED]` |
| Color | `#000000` on light (true ink) · white on dark | `[EXTRACTED]` e4-01.jpeg |
| Email size | **22–26px** in the 600px header | `[EXTRACTED]` e4-flattened (26px), e5-flattened (22px) |
| Clear space (email) | ≥ **22px** above/below, **40px** left/right (the header `<td>` padding) | `[EXTRACTED]` e4-flattened header padding |
| Clear space (brand formal rule) | likely 1× cap-height on all sides | `[INFERRED — confirm]` — brand-book swatch is image-only; not extractable here |

```html
<!-- Wordmark — bold + TIGHT (correct) -->
<a href="https://takestasis.com/" style="text-decoration:none;" target="_blank"><span
  style="font-family:'Helvetica Neue',Arial,sans-serif; font-weight:900; font-size:26px;
         line-height:1; letter-spacing:-0.01em; color:#000000; text-transform:uppercase;">STASIS</span></a>
```

> ⚠️ **Both judged-good recreations ship the wordmark WIDE-tracked — `e4-flattened.html` at `letter-spacing:0.30em`, `e5-flattened.html` at `0.26em`** — bold weight (correct) but wrong tracking. The footer lockups passed judgment; the wordmark tracking was not caught. **Do not copy those values.** Correct tracking is tight (≤ 0), and the fix applies to **both** files. This is the exact failure the spec exists to stop. `[EXTRACTED]` e4/e5-flattened
>
> **NEVER:** thin/regular weight · positive (wide) tracking · letterspaced-out "S T A S I S".

---

## 5. Buttons & pills

### 5.1 Primary CTA pill (copy-pasteable, bulletproof)

Fill `#FF541E` (Spice) · **black** label `#000000` · weight 800 · 15px · `+0.18em` · uppercase · `border-radius:999px` · padding `17–18px / 50–54px`. VML block for Outlook + HTML fallback. `[EXTRACTED]` e4/e5-flattened.

```html
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"
  href="{{ CTA_URL }}" style="height:54px;v-text-anchor:middle;width:230px;" arcsize="50%"
  stroke="false" fillcolor="#FF541E"><w:anchorlock/>
  <center style="color:#000000;font-family:'Helvetica Neue',Arial,sans-serif;font-size:15px;
    font-weight:800;letter-spacing:3px;text-transform:uppercase;">TAKE STASIS</center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-->
<table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0"
  style="border-collapse:collapse; margin:0 auto;"><tbody><tr>
  <td align="center" bgcolor="#FF541E" style="background-color:#FF541E; border-radius:999px;">
    <a href="{{ CTA_URL }}" target="_blank" style="display:inline-block; padding:18px 54px;
       font-family:'Helvetica Neue',Arial,sans-serif; font-weight:800; font-size:15px; line-height:1;
       letter-spacing:0.18em; text-transform:uppercase; color:#000000; text-decoration:none;
       border-radius:999px; white-space:nowrap;">TAKE STASIS</a>
  </td>
</tr></tbody></table>
<!--<![endif]-->
```

### 5.2 STASIS + STIMULANT formula lockup (the recurring failure — copy-pasteable)

The closing "balance" lockup, rebuilt live (text-classified brand/formula lockups are rebuilt as live HTML, never reused as the original slice image). **Outline** STASIS pill + `+` + **filled** STIMULANT pill, all royal blue `#3D72E6`, on a Creme panel, followed by the closing headline. Pills: weight 900 · 17px · `−0.02em` · uppercase · `border-radius:999px` · padding `10px 24–26px`. Geometry `[EXTRACTED]` e4-flattened closing lockup; color canonical `#3D72E6` (step-1 brief line 62; e4/e5 shipped `#3F73E6` / `#3B6FE4`).

```html
<td align="center" bgcolor="#F4EFEB" style="padding:8px 48px 48px 48px; background-color:#F4EFEB; text-align:center;">
  <!-- formula pills -->
  <table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0"
    style="border-collapse:collapse; margin:0 auto 26px auto;"><tbody><tr>
    <td style="padding:0 8px 0 0;"><span style="display:inline-block; padding:10px 26px;
      border:2px solid #3D72E6; border-radius:999px; background-color:#F4EFEB;
      font-family:'Helvetica Neue',Arial,sans-serif; font-weight:900; font-size:17px; line-height:1;
      letter-spacing:-0.02em; color:#3D72E6; text-transform:uppercase;">STASIS</span></td>
    <td style="padding:0 8px; font-family:'Helvetica Neue',Arial,sans-serif; font-weight:900;
      font-size:19px; line-height:1; color:#3D72E6;">+</td>
    <td style="padding:0 0 0 8px;"><span style="display:inline-block; padding:10px 24px;
      border-radius:999px; background-color:#FFFFFF;
      font-family:'Helvetica Neue',Arial,sans-serif; font-weight:900; font-size:17px; line-height:1;
      letter-spacing:-0.02em; color:#3D72E6; text-transform:uppercase;">STIMULANT</span></td>
  </tr></tbody></table>
  <!-- closing headline -->
  <h2 style="margin:0 auto 28px auto; max-width:480px; font-family:'Helvetica Neue',Arial,sans-serif;
    font-weight:900; font-size:48px; line-height:0.98; letter-spacing:-0.05em; text-transform:uppercase;
    color:#3D72E6; text-align:center;">BALANCE FOR BOLD MINDS</h2>
  <!-- CTA pill (§5.1) goes here -->
</td>
```

> **Lockup invariants** (these are what regenerate wrong): STASIS = **outline** pill (2px border, panel-colored fill), STIMULANT = **filled** white pill, both the *same* royal blue text, `+` is blue weight-900, all pills `999px`. Never render this as the original baked image, and never let either pill become a solid color block. `[EXTRACTED]`

### 5.3 Radius system

`999px` pills (CTA, formula pills, promo pill, badge) · `18px` cards · `14px` smaller media/cards · `50%` for VML `arcsize` and circular elements. `[EXTRACTED]` e2-e5-flattened (`border-radius` frequency: 999px ×53, 50% ×30, 18px ×7, 14px ×3).

---

## 6. Cards & panels

### 6.1 Testimonial quote card (E4 pattern — alignment goes here)

> **RESOLVED 2026-06-10 (Bryce live review — REVERSES the 2026-06-08 left-alignment call):** alignment follows the **designed original, per email**. The E4 designed version is **CENTERED**, with the quote block the **same width as the hero image above it, abutting directly beneath** (no extra inset). Quotes are **UPRIGHT serif (Tiempos Text), never italic**. The "centering = drift" claim below came from grading the old recreations, not the designed sends — it was wrong. Measure the original; match it.

- Container: `width:100%; background-color:{CARD}; border-radius:18px; border-collapse:separate;` `[EXTRACTED]`
- Inner padding: `26px 28px 28px 28px` `[EXTRACTED]`
- ~~All contents LEFT-aligned~~ **alignment per the designed original of the email being built** (E4: centered). Superseded 2026-06-10, see banner above.
- Heading: weight 900 · 15px · 1.1 · `+0.06em` · uppercase · in a **dark tone harmonized to the card hue** (yellow→navy `#0E1A38`, peach→brown `#3A1A0E`, teal→green `#0B3D32`). `[EXTRACTED]`
- Quote: `Georgia` *italic* · 400 · 17px · 1.5 · same harmonized dark tone. `[EXTRACTED]`
- Attribution line: sans, smaller, same column (left). `[INFERRED — confirm]` exact size (treat as caption 14px / weight 600).

```html
<table role="presentation" width="100%" border="0" cellpadding="0" cellspacing="0"
  style="width:100%; background-color:#EEEF78; border-radius:18px; border-collapse:separate;">
  <tbody><tr><td style="padding:26px 28px 28px 28px;">
    <p style="margin:0 0 12px 0; font-family:'Helvetica Neue',Arial,sans-serif; font-weight:900;
      font-size:15px; line-height:1.1; letter-spacing:0.06em; color:#0E1A38; text-transform:uppercase;
      text-align:left;">SAVING ME</p>
    <p style="margin:0 0 14px 0; font-family:Georgia,'Times New Roman',serif; font-style:italic;
      font-weight:400; font-size:17px; line-height:1.5; color:#1C2233; text-align:left;">“…quote…”</p>
    <!-- attribution -->
  </td></tr></tbody>
</table>
```

### 6.2 Stat panel (E5 pattern)

> **RESOLVED 2026-06-10 (Bryce live review):** stat treatments follow the **designed original per email** — numeral color, layout, and **every artistic element** (brand icons, photos) included. E2's designed panel is a black 2-column icon-grid: flat brand icon above a divider rule, **WHITE numeral**, label beneath, with the capsule-in-hand photo bleeding into the right edge. Stripping icons/photos to bare numeral|label rows is a redesign, not a recreation ("we need to be like good designers, not just designers").

Geometry reference (from e5-flattened): numeral weight 900 · **58px** (mobile 54px) · line-height 0.9 · `−0.04em`; label weight 600 · 14px · 1.3. Color and arrangement per the original being recreated.

### 6.3 Promo / discount band

- Band: full-width `bgcolor="#000000"`, padding `26–30px / 40–48px`. `[EXTRACTED]`
- Discount headline — two approved treatments: **(a)** yellow text `#EEEF78`, weight 900, 24px, `−0.01em`, uppercase (E4); **(b)** yellow **pill** `#EEEF78` fill / navy `#0E1A38` text, weight 900, 22px, padding `12px 26px`, `999px` (E5). `[EXTRACTED]` (yellow = canonical Lime `#EEEF78`; recreations shipped `#F0F36A`).
- Sub-line ("EXTRA 10% OFF + FREE shipping with code:"): white `#FFFFFF`, weight 700–800, 14–15px, 1.3, `+0.02–0.03em`. `[EXTRACTED]`

---

## 7. Hero & badge

- **Hero image** is a sourced photograph (portrait or product), full 600px width, with rounded corners. `[EXTRACTED]` e4-02 / e4-09 (module map). Crop and source come from the brief's source-asset table — never a flattened slice.
- **Badge over hero** (e.g. "REAL PEOPLE, REAL STORIES"): a single **black pill**, white text, weight 800, 14px, `+0.12em`, uppercase, padding ~`11px 22px`, `position:absolute; left:50%; bottom:28px; transform:translateX(-50%)` (bottom-center). `[EXTRACTED]` e4-flattened.
- **Invariants** (E4 drift was a doubled/clipped badge): exactly **one** badge, bottom-center, fully inside the image, not duplicated by both a baked-in and a live copy. `[EXTRACTED]`

---

## 8. Shaped edges (scalloped / domed transitions)

The brand uses curved panel transitions (the cream arc rising into the closing lockup). **No decorative edge or panel boundary may depend on rendered text height** — the preview runtime injects typography that is stripped on export, so any edge tied to text height shifts or vanishes across export/Gmail/Outlook. `[EXTRACTED]`

**Implementation:** put the curve in its own fixed-height row with `font-size:0; line-height:0`, decoupled from any text.

```html
<!-- Domed arc rising into a Creme panel — fixed height, text-independent -->
<td align="center" bgcolor="#FFFFFF" style="padding:0; font-size:0; line-height:0;
    mso-line-height-rule:exactly; background-color:#FFFFFF;">
  <div style="height:54px; background-color:#F4EFEB;
       border-top-left-radius:50% 100%; border-top-right-radius:50% 100%;
       font-size:0; line-height:0;">&nbsp;</div>
</td>
```

- `border-top-left/right-radius:50% 100%` = a wide, shallow dome across the full 600px. `[EXTRACTED]` e4-flattened.
- Thin seam accents (e.g. teal `border-bottom:4px solid #25DFAE`) sit on their own zero-height row, same principle. `[EXTRACTED]`
- For deeper scallops or multi-bump edges, render as a **full-width image row** (baked whole), not as text-dependent CSS. `[INFERRED — confirm]` — extends the text-height rule above; no live multi-scallop example exists in these sends.

---

## 8.5 Artistic completeness & derived-crop sourcing (RESOLVED 2026-06-10, Bryce live review)

1. **Never simplify away artistic elements** present in the designed original — icons, photos, decorative rings, organic shapes, tonal transitions. Omitting them because sourcing is hard is a build failure, not a fallback.
2. **Derived crops are a sanctioned sourcing mode:** when no canonical master exists, crop the element from the **sha-verified original slice** and record provenance (source slice sha + crop box) in the email's source-asset table. This is exact sourcing, not approximation.
3. **CSS recreations of distinctive organic/hand-drawn decorations are NOT acceptable substitutes** (e.g. the e2-06 hand-drawn dashed ring became a "blue dashed square" in CSS). If the original's look is specific, use the original's pixels.
4. **Continuous tonal transitions ship as image assets, not CSS gradients,** when the original is an asset (e.g. E1's blue→white zone = `gradient_top_zone.png`, seamless into the white section; the CSS approximation produced a visible hard cut).

## 8.6 Modes — mobile reflow & dark mode (RESOLVED 2026-06-10, Bryce live review: "perfect from all modes")

**Mobile (375px) — blocking gate.** Every email must pass `scripts/check_reflow.py <file> --width 375 --width 600` (scrollWidth == width, no horizontal overflow). The designed original rendered at 375 is the reflow reference. Checklist:
- No fixed-width element without a `@media (max-width:480px)` override (inner tables with `width=` attrs, fixed-px divs, padded sums > 375).
- `white-space:nowrap` only where the content provably fits 375 at its mobile size.
- Fixed `background-size:<px>` is forbidden — use `cover` (or `100% auto` with a safe anchor).
- Type scales per the established mobile map (`.h-hero`, `.h-lg`, `.h-closer`, `.stat-num`, …); new components must ship their mobile rule with them.

**Mobile-first principles (RESOLVED 2026-06-11, Bryce review round 2 — most opens are mobile; presentation must fit both without ripping up desktop):**
- **Supplementary elements must not inflate when columns stack.** A side-render or accent image keeps a capped mobile size (supporting-cast scale, e.g. ≤ ~45% of frame width) — stacking must never promote it to a hero ("turning what's meant to be a supplementary element into a main one").
- **CTA scroll-depth parity:** at 375, the first CTA lands within ~15% of the original's scroll depth. Tall stacked sections get compacted on mobile (smaller decorative grids, tightened verticals) rather than pushing CTAs down.
- **Pinned desktop line-breaks** use the hide-on-mobile pattern: `word <br class="dbr"/>nextword` (space *before* the br) + `@media{.dbr{display:none}}` — never a bare `<br/>` that forces ragged mobile lines, never a hidden br that would merge words.
- **Continuity effects survive breakpoints:** elements that straddle a section boundary in the design (e.g. a capsule cut by the color border) are built as split assets — bottom-of-element on the upper section's last row, top-of-element on the lower section's first row — so the effect holds at every width, no negative margins.
- **Wordmark optical size is measured per email from the original** — the kit default proved oversized in review; size the mark to the baked original's optical box and rebalance the elements beneath it (padding + any anchored background compositions) to the original's ink positions.

**Dark mode — lock light, harden colors.** Every email pins light: `<meta name="color-scheme" content="light only">`, `<meta name="supported-color-schemes" content="light only">`, and `:root,body{color-scheme:light only}` in `<style>`. Plus hardening for partially-recoloring clients: every content `td` carries `bgcolor` attr + `background-color` style; every text element carries an explicit `color`. Client reality (documented, not hidden): Apple Mail/iOS honor the pin → renders as designed; Gmail app dark ignores it and partially recolors live-text emails — an inherent HTML-vs-image difference, to be confirmed in Litmus before any live send. The review tool renders light-pinned emails unchanged in its Dark toggle (Apple-Mail-faithful); non-pinned content gets an aggressive inversion model.

## 9. Inferred items (consolidated — confirm before binding)

1. **Brand-name↔hex bindings** (§2) — the Digital Web Style Guide names the palette (Spice, Lime, Electric Blue, Turquoise, Creme…) but its swatches are images; the brand's *canonical* hex per name could not be read here. The email hex are extracted/canonical and solid; only the name mapping is inferred. Confirm from the style-guide swatch page or the `.fig` masters.
2. **Wordmark formal clear-space ratio** (§4) — email padding is extracted; the brand-book "1× cap-height" rule is inferred.
3. **Never-load-Antartica-in-email** (§3) — extracted that the sends don't load it; that we never *want* to is a reasonable inference, confirm.
4. **Testimonial attribution line size** (§6.1) — treated as 14px/600; not separately measured.
5. **Deep/multi-scallop shaped edges** (§8) — only the shallow dome exists in-source; the "bake as image" extension is inferred from the text-height rule.

## 10. Conflicts — resolved 2026-06-08

All six resolved by Bryce on 2026-06-08; kept here as the decision record. Where a value is `not used`, it appeared in a source but was rejected as canonical.

1. **Wordmark tracking — RESOLVED.** Both judged-good recreations ship the wordmark WIDE-tracked — `e4-flattened.html` at `letter-spacing:0.30em`, `e5-flattened.html` at `0.26em` — bold weight (correct) but wrong tracking; only the footers were graded. **Canonical = tight (≤0)**, and the correction applies to **both** files. (The reference HTML files themselves were left unedited under this task's commit scope — flagged for a follow-up correction pass.)
2. **Quote-card trio — RESOLVED: the saturated baked originals are canonical** — yellow `#EEEF78`, peach `#FD9A70`, teal `#24DEAD` (re-sample confirms `#EFF079` / `#FE9B71` / `#25DFAE`). The pale recreation fills (`#F0F36A` / `#FF9B70` / `#BDEBDF`) are not used. Harmonized dark text colors hold on the saturated fills.
3. **Royal blue — RESOLVED: canonical `#3D72E6`** (step-1 brief line 62); extracted range `#3F73E6` (e4-flattened) / `#3B6FE4` (e5-flattened). `#197BBD` retired from display.
4. **CTA orange — RESOLVED: canonical `#FF541E`** (step-1 brief + e5-flattened); e4-flattened shipped `#FF5128`; baked original `#FD531D`.
5. **Creme — RESOLVED: canonical `#F4EFEB`** (step-1 brief line 62); e4/e5-flattened shipped `#F3EFE9`.
6. **Sans family — RESOLVED: keep the stated email substitution** — brand face is Antartica; email falls back to the Helvetica Neue stack at weight 900. Stated explicitly so a builder doesn't "fix" it by chasing the brand font into email.

---

### Sources referenced

- **Stasis Brand Book** (Drive) and **Stasis Digital Web Style Guide** / **Brand Guidelines (Updated)** — palette names, type-system structure (Bold Caps headers, Serif body, 4px grid), component inventory. Hex/px are visual swatches in these PDFs and were not text-extractable in this environment.
- **Welcome-flow sends E2–E5** — composites and per-slice images (pixel-sampled for baked color) and the live recreations `e{2-5}-flattened.html` (extracted for live-text geometry). E4/E5 closing lockups are the approved live-lockup reference.
- **Internal Claude Design constraints notes (text-height rule)** — governs shaped edges (§8).
