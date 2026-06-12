# Stasis — Asset Sources & Hosting

> **Brand-pack canonical doc** (created 2026-06-12, multi-brand restructure). This is the
> Stasis answer to everything `reference/send-prep-spec.md` §3/§5 and the
> `email-image-source` skill resolve "through the brand pack": the canonical source chain,
> the wordmark master chain, pinned production font/image hosting, and the measured coupon
> mobile treatments. Compiled from existing repo records — every fact below cites its
> source doc; nothing here is new research. Hashes are sha-256.

**Source docs:** `reference/welcome-flow-VUD7gW/wsc-asset-map.md` (hosted font + image
tables, upload verification) · `reference/welcome-flow-VUD7gW/e1..e5-source-assets.md`
(wordmark + per-asset provenance rows) · `.claude/skills/email-image-source/SKILL.md`
(chain + Drive ids) · `_incoming/welcome-flow-VUD7gW/assets/brand/logo-usage.md` (wordmark
kit) · `_incoming/welcome-flow-VUD7gW/assets/fonts/font-map.md` (font Drive ids, license)
· `reference/welcome-flow-VUD7gW/wsc-send-spec.md` §2 (coupon treatment measurements) ·
`brands/stasis/design-language.md` §3/§4 (binding spec).

---

## 1 · Canonical source chain

Resolution order for every image in a Stasis email (per `email-image-source` SKILL, asset
model decided 2026-06-01): **catalog → Air → Drive exception list.** Gaps stop the build.

| link | what it is | id / locator |
|---|---|---|
| **Stasis Adult Image Catalog** | The email system's curated lens over Air (Notion, CreativeOps-owned): email-ready entries with descriptions, text-baked flags, statuses, gap list. An index, not a second library — every entry points back to its source file. | Notion data source `collection://d7c05078-a1e2-4f25-955f-4de690d9959f` (id recorded in `e4-source-assets.md` / `e5-source-assets.md` catalog-lookup logs) |
| **Air** | Source of truth — the creative team's DAM. | app.air.inc (asset-level URLs recorded per row in the source-asset tables) |
| **Drive exception list** | Assets that live only in Drive (e.g. the Getty brain master). Folder ids per `email-image-source` SKILL References: | Stasis Adult New Branding `1a7tTTexNCEib6FQdojR9Zz6cd9QlfobP` · Photography `14ob4qWi8hHei0zf-qYOTA-gye_bSfujA` · Creative Assets `1FuZWkxVha4qyzHzUmLAx_PGwQiI4_k7V` · Brand Assets `1Fui8TwJGMGwsiRdmbytoG8B5oKNh-n7U` |
| **Font masters (Drive)** | Licensed woff2 masters (design-language §3, RESOLVED 2026-06-10). | Antarctica WOFF2 folder `1ZUqAg9c89xHptVWl8p_UeTN0Rv_K_QeB` · Tiempos Text web files `1CMiAgacGWxrgWGL3XEMTvEpgUqO6s6MC` (Klim **web** license — name table says "Not Licensed for Desktop Use"; per-file Drive ids in `_incoming/welcome-flow-VUD7gW/assets/fonts/font-map.md`) |

Rules that travel with the chain (`email-image-source` SKILL):

- **Working-CDN URLs (Klaviyo/CloudFront) are never sources** — they are downstream
  output. Self-uploaded, sha-round-trip-verified CDN copies are a *hosting* concern (§4
  below), not a *source*. Never reference the original sends' slice CDN URLs.
- Assets found outside the catalog are catalog-addition candidates — flag to creative ops
  (Theo); don't edit the catalog from a build.
- Derived crops of approved send slices are sanctioned only per design-language §8.5
  (documented crop box + sha of slice and crop) when the canonical master is unresolved.
- Every chosen asset is sha-pinned at selection time; verification is hashes, not eyes.

---

## 2 · Wordmark master chain

Binding rule: **the wordmark is the LOGO ASSET, never typed text** — "The logo has to be
the logo" (design-language §4, RESOLVED 2026-06-10; typed STASIS is acceptable only inside
the §5.2 formula-lockup pills). Full kit, tint method, and per-email measurements:
`_incoming/welcome-flow-VUD7gW/assets/brand/logo-usage.md`.

**Master** — catalog "Stasis blue wordmark" (Status **Approved**):

- Air canonical: https://app.air.inc/a/bFVACbwGW/98e78704-52bb-4c1b-ab2d-1fd76df15180
- Drive backup: https://drive.google.com/file/d/1ZOo4f6yTl3IfDWL1_1JxyoYodAtaxitk/view
- Staged: `_incoming/welcome-flow-VUD7gW/assets/brand/stasis-wordmark-blue.png`
- sha `661cd181b9099c0999713368353b280fdebd52c4395051e99993b0a18db36042` (4336×981 RGBA,
  82,769 B; every opaque pixel flat `#3B6FE4`, all anti-aliasing in the alpha channel)

**Approved renditions** (flat tints of the master — alpha channel resampled alone, LANCZOS
4336×981→1200×271, RGB set constant; geometry/alpha of the master preserved exactly, alpha
byte-identical across the three 1200 variants; per logo-usage.md + e1/e2/e3/e4/e5
source-asset rows):

| rendition | sha256 | px / bytes | used in |
|---|---|---|---|
| `wordmark-white-1200.png` | `92970f10b5399e7f984b2a07bfb2b68cc3db890e88d22c81eea2a3068ed85132` | 1200×271 RGBA, 31,226 B | E1 (royal gradient), E2 (navy hero art) — hosted as `wsc-html-shared-logo-white` (§4) |
| `wordmark-black-1200.png` | `2eebc27153336d56050972edd3525c3558a2cf68391f532353ef1a91f73ed637` | 1200×271 RGBA, 31,023 B | E3/E4 (white), E5 (Creme) — hosted as `wsc-html-shared-logo-ink` (§4) |
| `wordmark-blue-1200.png` | `367f5a5c973d5429f34f9e9da668bb475ff9bc9fabe384731528b26422a77825` | 1200×271 RGBA, 31,222 B | none yet (kit completeness; tint `#3B6FE4`) |
| `stasis-wordmark-white-600.png` (legacy) | `d040df08996e4dd4793d42a53741670aed356dd81c51ceec268d1066bcb3544e` | 600×136 RGBA, 10,379 B | e1 donor bytes only. Own catalog row "Stasis white wordmark" (Approved): Air https://app.air.inc/a/bFVACbwGW/8a947528-c91f-4742-8bc5-2f6061d45721 · Drive `1WwqSKXr9hLpdkYw0GHUE1MtN6zo9TiiY` · Notion https://app.notion.com/p/67206412ea20430e95e852b6dfa65b3c. Alpha IoU 0.998 vs the 1200 white — **prefer the -1200 exports** (sharper, alpha-identical across variants). |

Display: every welcome-flow original renders the mark at **169×38 CSS px, centered**
(measured per email in logo-usage.md; reference HTML pattern there). Never wide-tracked,
never typed.

---

## 3 · Hosted fonts — Shopify Files CDN (production)

Source: `wsc-asset-map.md` Fonts section (discovery + verification 2026-06-11, plain
HTTPS; each URL fetched and sha-256 compared against the local masters — **byte-identical**).
Canonical host `cdn.shopify.com`, store id `0639/3511/9576`; the same bytes are also
served at `takestasis.com/cdn/shop/files/<name>`. Headers: `content-type: font/woff2`,
`access-control-allow-origin: *`, `cache-control: public, max-age=31557600`.

Faces/weights/roles are pinned in design-language **§3** (Antarctica 400/500/600/700 +
Tiempos Text 400 upright; role map + match evidence in `font-map.md`).

| file | CSS binding | sha256 | hosted URL |
|---|---|---|---|
| Antarctica-Regular.woff2 | `'Antarctica'` 400 | `d14aa382c44108a3569d00976d04b838a335faa334474c827b06a60936affd22` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Regular.woff2 |
| Antarctica-Medium.woff2 | `'Antarctica'` 500 | `91a92ab72c1dfb5d9f258f3228801db538307aeb299a0251a30ca4ca0dd213f6` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Medium.woff2 |
| Antarctica-SemiBold.woff2 | `'Antarctica'` 600 | `334dd2da7e6ef84bfd7a2985d381ff9346cc7121b3ff5e24a2fd774c8e4b8391` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-SemiBold.woff2 |
| Antarctica-Bold.woff2 | `'Antarctica'` 700 | `ad195eee21c3190f7bb1a2755eb5fa04b9ac388e9b56a2948bbbc80a52a35de3` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Bold.woff2 |
| tiempos-text-regular.woff2 (lowercase name on Files) | `'Tiempos Text'` 400 | `b69bcc874fd7b155826a0424c1e3f56deebb6db3ec6201305a28d601921646e2` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/tiempos-text-regular.woff2 |

Full-sha note: wsc-asset-map records the hosted-verify matches by first-16 prefix for the
four Antarctica files; the full values above were computed 2026-06-12 from the local
masters at `_incoming/welcome-flow-VUD7gW/assets/fonts/` (the exact files wsc-asset-map
verified byte-identical to the hosted copies). Tiempos full sha is recorded verbatim in
wsc-asset-map. Drop-in hosted `@font-face` block:
`_incoming/welcome-flow-VUD7gW/assets/fonts/fontface-hosted.html`.

Known limits (wsc-asset-map):

- **TiemposText-Medium (500) is NOT hosted as woff2** (local master
  `a568c34aca2fe636960c1b2c8153e6bef2ffb889bc547543e8552eeb1f648c17`). Caution: a
  `TiemposText-Medium.woff` (**.woff**, not woff2) answers 200 on Files — different
  format/bytes, not verifiable against the woff2 master; **do not use**. In every E1–E5
  send file the Tiempos 500 declaration proved dead weight and was dropped; new builds
  must run their own usage check before treating it as a blocker.
- Upload provenance: the Files uploads landed out-of-band 2026-06-11 (19:44 / 19:54 GMT),
  not by an agent — [UNVERIFIED — confirm] presumed manual upload by Bryce, per the
  open flag in wsc-asset-map.

---

## 4 · Image hosting for sends — Klaviyo image CDN

Send copies must reference production-hosted images, never data URIs and never the
original sends' slice CDN URLs (`reference/send-prep-spec.md` §3). The sanctioned path
(established in the WS-C Phase-0 pass, `wsc-asset-map.md`):

- **Account:** Klaviyo company `YsCgQB` (Stasis).
- **Upload:** Klaviyo Images API `POST /api/image-upload/` (revision `2024-10-15`).
- **Resulting URL pattern:** `https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/<uuid>.<ext>`
- **Verification requirement (non-negotiable):** every CDN URL fetched back and sha-256
  compared against the exact bytes sent — hosted copy must be **byte-identical** before it
  enters a send file. (WS-C batch: all 27 uploads sha-matched; Klaviyo did not re-encode.
  If a future upload re-encodes, that is a stop-and-surface, not a pixel-compare shrug.)

The live hosted inventory (27 images for the welcome-quiz flow, incl. both wordmark
renditions `wsc-html-shared-logo-white` `92970f10…` and `wsc-html-shared-logo-ink`
`2eebc271…`) is the table in `reference/welcome-flow-VUD7gW/wsc-asset-map.md` — that file
stays the per-flow ledger; this doc pins the account, API, URL pattern, and verification
rule. New uploads for any flow follow the same procedure and get logged in that flow's
asset map.

Quirk worth keeping (wsc-asset-map notes): images used as `td background=` /
`background-image:url()` (e.g. e1 gradient zone, e2 marble hero) need BOTH the attribute
and the CSS url swapped — they are not `<img src>` swaps.

---

## 5 · Coupon mobile treatments (measured)

Referenced by `reference/send-prep-spec.md` §2 item 7: zone *placement/coherence* rules
live in send-prep-spec §2 (the 2026-06-12 normalization rule — it supersedes
wsc-send-spec's match-the-original call); the *styling* below is the brand pack's measured
treatment set, carried from `wsc-send-spec.md` §2 (measured from the designed originals).

| zone type | mobile (≤480px) | desktop (600) | source |
|---|---|---|---|
| **Black-band code** (black promo band, white text — E4/E5 pattern) | **17px, NOT bold (400)**, white `#FFFFFF`, span stack `Helvetica, Arial, sans-serif` inside outer `'Helvetica Neue',Arial`, centered, ~10px above-margin to the band sub-line | 26px **bold**, same Helvetica stack | wsc-send-spec §2.4(b)/(c), §2.5(b) |
| **Yellow-strip / light-bg code** (yellow `#EEEF7A` strip or white mid-body row — E2/E3 pattern) | **18px bold**, ink `#222427`, span stack `Antartica, Lucida, 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Geneva, Verdana, sans-serif`, td padding `9px 18px`, centered | 26px regular (no bold), same Antartica→Lucida stack, on `#EEEF7A` | wsc-send-spec §2.2(a)/(b), §2.3 |

Non-negotiables that travel with these treatments:

- **The misspelled `Antartica` first family is intentional** — no client resolves it, so
  it falls through to Lucida/fallback exactly as the originals do. Do NOT "fix" it to the
  `'Antarctica'` webfont name (that WOULD change rendering). (wsc-send-spec §2 locked
  call; restated in send-prep-spec §2.7.)
- E2's black band keeps its Antartica→Lucida desktop code (per-email exception); E4/E5
  band codes are Helvetica — keep per-email (wsc-send-spec §2.4(b)).
- Desktop/mobile split plumbing: `.wsc-desk` / `.wsc-mob` pair at the **480px**
  breakpoint, mobile blocks inline `display:none` + `mso-hide:all` wrapped in
  `<!--[if !mso]><!--> … <!--<![endif]-->`; background/padding on the inner div/cell,
  never the `<tr>`/`<td>` (wsc-send-spec §2.0).
- A `.wsc-desk`/`.wsc-mob` pair counts as ONE code occurrence per zone per mode
  (send-prep-spec §2.4).
