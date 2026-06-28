# Stasis Design Tokens — the single source of truth

**Status:** DRAFT for Bryce approval (2026-06-16). Nothing references this yet; on approval, components and every build derive from it.

**The rule that makes this a system:**
1. **Source of truth = the original Klaviyo *sends*** (measured) and the brand book — **never the recreations** (the welcome recreation drifted; that's how the CTA shipped 15px instead of 20px).
2. **Builds and components reference these tokens** — no inline one-off values. Change a token once → it propagates everywhere.
3. **A new value is a token you approve**, added here with its source. Not something improvised in a build.
4. Each token carries a **verification status**: `verified` (measured from an original send / brand book) or `pending-verify` (carried from `design-language.md`, not yet re-checked against an original — treat as provisional).

---

## CTA pill — `verified`
**Standing geometry: 20px · padding 18px 40px · weight 700 · radius 999 · VML 264×56** (component default box; the original send-02 slice measured 236×56; re-measure VML width per label). Big text, tight padding.

| Property | Value | Note |
|---|---|---|
| font-size | **20px** | |
| padding | **18px 40px** | tight; VML box 264×56 (orig slice 236×56) |
| weight | 700 | Antarctica Bold |
| letter-spacing | 0.18em | |
| text-transform | uppercase | |
| text color | `#000000` | black, not white |
| fill | `#FF541E` (Spice) | |
| radius | 999px | |
| mobile | standard CTA keeps 20px + wraps (`.cta-link{white-space:normal}`); hero variant `.m-cta` 15px 46px | no font-size shrink ships |
| label length | **keep short** ("Try Stasis", "Shop Now", "Gift the Set") — long phrases make stretched bars, off-brand |

## Color — `verified` (canonical, pixel-sampled from sends; from design-language §2)
`spice` `#FF541E` · `lime` `#EEEF78` · `royal` `#3D72E6` · `navy` `#011D59` · `ink` `#0E1A38` · `creme` `#F4EFEB` · `charcoal` `#222427` · `panel` `#F7F7F7` · `black` `#000000` · `white` `#FFFFFF`

## Fonts — `verified` (same sources the welcome flow uses)
- **Sans:** `Antarctica` → fallback `'Helvetica Neue', Arial, sans-serif`, `mso-font-alt:'Helvetica Neue'`. Faces (Shopify CDN `…/0639/3511/9576/files/`): `Antarctica-Regular`(400) · `-Medium`(500) · `-SemiBold`(600) · `-Bold`(700).
- **Serif:** `Tiempos Text` → `Georgia,'Times New Roman',serif`, `mso-font-alt:'Georgia'`. `tiempos-text-regular`(400). **UPRIGHT, never italic.**

## Wordmark — `verified`
Hosted transparent PNGs (the approved send assets): **white** `…/02b774d0-…png` (on dark) · **ink** `…/602ec7a2-…png` (on light). Display **169×38**, top-center. The logo is an **image asset, never typed**.

## Type scale — `verified` 2026-06-18

_Validated via the Bryce-approved live-text rebuild (cc-from-spec, 2026-06-11, faithful to originals); primary elements corroborated by original-slice pixel measurement (CTA 236×56/20px hard-confirmed; stat-numeral glyph ~58px → 75px font; H1 dominant band). Weights are the Antarctica face weight; the Helvetica fallback uses 900 display / 800 CTA (see design-language §3)._
Reconciled 2026-06-18 against the shipped components + original-slice measurement (see each row's status); originally carried from `design-language.md §3`.

| Role | size / lh / tracking | weight | status |
|---|---|---|---|
| Hero / H1 | 40px / 1.02 / −0.04em → 32 mobile | 500 | verified 2026-06-18 |
| H2 / subhead | 30px / 1.08 / −0.03em | 500 | verified 2026-06-18 |
| Lead paragraph | 20px / 1.34 / −0.02em | 600 | verified 2026-06-18 |
| Body | 15px / 1.55 / −0.01em | 500 | verified 2026-06-18 |
| Stat numeral | **75px** -> 56px mobile / 0.9 / −0.01em | 500 | verified 2026-06-18 (shipped stats-panel-dark/light) |
| Eyebrow / label | 13px / +0.2em uppercase | 700 | verified 2026-06-18 |
| Caption / stat label | 14–15px / 1.3 (stat-panel label 21px) | 500 | verified 2026-06-18 |
| Disclaimer | 11px / 1.55 | 400 | verified 2026-06-18 |


