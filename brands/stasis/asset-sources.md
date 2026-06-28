# Stasis — Asset Sources & Hosting

> **Brand-pack canonical doc** (created 2026-06-12, multi-brand restructure). This is the
> Stasis answer to everything `reference/send-prep-spec.md` §3/§5 and the
> `email-image-source` skill resolve "through the brand pack": the canonical source chain,
> the wordmark master chain, pinned production font/image hosting, and the measured coupon
> mobile treatments. Compiled from existing repo records — every fact below cites its
> source doc; nothing here is new research. Hashes are sha-256.

**Source docs:** the internal per-flow recreation ledger (hosted font + image
tables, upload verification) · the internal per-flow recreation ledger
(wordmark + per-asset provenance rows) · `.claude/skills/email-image-source/SKILL.md`
(chain + Drive ids) · the internal asset ledger (wordmark
kit) · the internal asset ledger (font Drive ids, license)
· the internal per-flow recreation ledger §2 (coupon treatment measurements) ·
`brands/stasis/design-language.md` §3/§4 (binding spec).

> **"The internal asset ledger"** below denotes internal CreativeOps working files (the wordmark kit, font map, crop/recipe records) kept outside this public pack. The load-bearing facts they hold — sha-256 pins, pixel dimensions, and Air/Drive locators — are cited inline here, so this doc stands alone without them.

---

## 1 · Canonical source chain

Resolution order for every image in a Stasis email (per `email-image-source` SKILL, asset
model decided 2026-06-01): **catalog → Air → Drive exception list.** Gaps stop the build.

| link | what it is | id / locator |
|---|---|---|
| **Stasis Adult Image Catalog** | The email system's curated lens over Air (Notion, CreativeOps-owned): email-ready entries with descriptions, text-baked flags, statuses, gap list. An index, not a second library — every entry points back to its source file. | the internal catalog data source (Notion; id + catalog-lookup logs in the internal source-asset ledgers) |
| **Air** | Source of truth — the creative team's DAM. | the Air DAM (internal); asset-level locators recorded per row in the internal source-asset ledgers |
| **Drive exception list** | Assets that live only in Drive (e.g. the Getty brain master). Folder ids per `email-image-source` SKILL References: | Stasis Adult New Branding (id in the email-image-source skill) · Photography (id in the email-image-source skill) · Creative Assets (id in the email-image-source skill) · Brand Assets (id in the email-image-source skill) |
| **Font masters (Drive)** | Licensed woff2 masters (design-language §3, RESOLVED 2026-06-10). | Antarctica WOFF2 folder (id in the email-image-source skill) · Tiempos Text web files (id in the email-image-source skill) (Klim **web** license — name table says "Not Licensed for Desktop Use"; per-file Drive ids in the welcome-flow font map, the per-flow asset ledger) |

Rules that travel with the chain (`email-image-source` SKILL):

- **Working-CDN URLs (Klaviyo/CloudFront) are never sources** — they are downstream
  output. Self-uploaded, sha-round-trip-verified CDN copies are a *hosting* concern (§4
  below), not a *source*. Never reference the original sends' slice CDN URLs.
- Assets found outside the catalog are catalog-addition candidates — flag to creative ops; don't edit the catalog from a build.
- Derived crops of approved send slices are sanctioned only per design-language §8.5
  (documented crop box + sha of slice and crop) when the canonical master is unresolved.
- Every chosen asset is sha-pinned at selection time; verification is hashes, not eyes.

---

## 2 · Wordmark master chain

Binding rule: **the wordmark is the LOGO ASSET, never typed text** — "The logo has to be
the logo" (design-language §4, RESOLVED 2026-06-10; typed STASIS is acceptable only inside
the §5.2 formula-lockup pills). Full kit, tint method, and per-email measurements:
the internal asset ledger.

**Master** — catalog "Stasis blue wordmark" (Status **Approved**):

- Master locators (Air canonical, Drive backup, staged PNG): in the internal asset ledger
- sha `661cd181b9099c0999713368353b280fdebd52c4395051e99993b0a18db36042` (4336×981 RGBA,
  82,769 B; every opaque pixel flat `#3B6FE4`, all anti-aliasing in the alpha channel)

**Approved renditions** (flat tints of the master — alpha channel resampled alone, LANCZOS
4336×981→1200×271, RGB set constant; geometry/alpha of the master preserved exactly, alpha
byte-identical across the three 1200 variants; per the internal logo-usage + source-asset ledgers):

| rendition | sha256 | px / bytes | used in |
|---|---|---|---|
| `wordmark-white-1200.png` | `92970f10b5399e7f984b2a07bfb2b68cc3db890e88d22c81eea2a3068ed85132` | 1200×271 RGBA, 31,226 B | E1 (royal gradient), E2 (navy hero art) — hosted as `wsc-html-shared-logo-white` (§4) |
| `wordmark-black-1200.png` | `2eebc27153336d56050972edd3525c3558a2cf68391f532353ef1a91f73ed637` | 1200×271 RGBA, 31,023 B | E3/E4 (white), E5 (Creme) — hosted as `wsc-html-shared-logo-ink` (§4) |
| `wordmark-blue-1200.png` | `367f5a5c973d5429f34f9e9da668bb475ff9bc9fabe384731528b26422a77825` | 1200×271 RGBA, 31,222 B | none yet (kit completeness; tint `#3B6FE4`) |
| `stasis-wordmark-white-600.png` (legacy) | `d040df08996e4dd4793d42a53741670aed356dd81c51ceec268d1066bcb3544e` | 600×136 RGBA, 10,379 B | e1 donor bytes only. Own catalog row "Stasis white wordmark" (Approved; locators in the internal asset ledger). Alpha IoU 0.998 vs the 1200 white — **prefer the -1200 exports** (sharper, alpha-identical across variants). |

Display: every welcome-flow original renders the mark at **169×38 CSS px, centered**
(measured per email in logo-usage.md; reference HTML pattern there). Never wide-tracked,
never typed.

---

## 3 · Hosted fonts — Shopify Files CDN (production)

Source: the internal per-flow asset ledger Fonts section (discovery + verification 2026-06-11, plain
HTTPS; each URL fetched and sha-256 compared against the local masters — **byte-identical**).
Canonical host `cdn.shopify.com`, store id `0639/3511/9576`; the same bytes are also
served at `takestasis.com/cdn/shop/files/<name>`. Headers: `content-type: font/woff2`,
`access-control-allow-origin: *`, `cache-control: public, max-age=31557600`.

Faces/weights/roles: the Antarctica **file-weight axis** (400/500/600/700) is enumerated in
`tokens.json` `font.faces`; the role→weight mapping and the Antarctica-vs-Helvetica-fallback
reconciliation (Antarctica 500/700 ≙ Helvetica 900/800) live in design-language **§3** (the
two-weight-axes note); Tiempos Text 400 upright. Match evidence is in the font map.

| file | CSS binding | sha256 | hosted URL |
|---|---|---|---|
| Antarctica-Regular.woff2 | `'Antarctica'` 400 | `d14aa382c44108a3569d00976d04b838a335faa334474c827b06a60936affd22` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Regular.woff2 |
| Antarctica-Medium.woff2 | `'Antarctica'` 500 | `91a92ab72c1dfb5d9f258f3228801db538307aeb299a0251a30ca4ca0dd213f6` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Medium.woff2 |
| Antarctica-SemiBold.woff2 | `'Antarctica'` 600 | `334dd2da7e6ef84bfd7a2985d381ff9346cc7121b3ff5e24a2fd774c8e4b8391` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-SemiBold.woff2 |
| Antarctica-Bold.woff2 | `'Antarctica'` 700 | `ad195eee21c3190f7bb1a2755eb5fa04b9ac388e9b56a2948bbbc80a52a35de3` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Bold.woff2 |
| tiempos-text-regular.woff2 (lowercase name on Files) | `'Tiempos Text'` 400 | `b69bcc874fd7b155826a0424c1e3f56deebb6db3ec6201305a28d601921646e2` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/tiempos-text-regular.woff2 |

Full-sha note: wsc-asset-map records the hosted-verify matches by first-16 prefix for the
four Antarctica files; the full values above were computed 2026-06-12 from the local
masters at the internal asset ledger (the exact files wsc-asset-map
verified byte-identical to the hosted copies). Tiempos full sha is recorded verbatim in
wsc-asset-map. Drop-in hosted `@font-face` block:
the internal asset ledger.

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
(established in the WS-C Phase-0 pass, the internal per-flow asset ledger):

- **Account:** Klaviyo company `YsCgQB` (Stasis).
- **Upload:** Klaviyo Images API `POST /api/image-upload/` (revision `2024-10-15`).
- **Resulting URL pattern:** `https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/<uuid>.<ext>`
- **Verification requirement (non-negotiable):** every CDN URL fetched back and sha-256
  compared against the exact bytes sent — hosted copy must be **byte-identical** before it
  enters a send file. (WS-C batch: all 27 uploads sha-matched; Klaviyo did not re-encode.
  If a future upload re-encodes, that is a stop-and-surface, not a pixel-compare shrug.)

The live hosted inventory (27 images for the welcome-quiz flow, incl. both wordmark
renditions `wsc-html-shared-logo-white` `92970f10…` and `wsc-html-shared-logo-ink`
`2eebc271…`) is the table in the internal per-flow recreation ledger — that file
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
treatment set, carried from the internal per-flow send-spec ledger §2 (measured from the designed originals).

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

---

## 6 · Curated asset pool (2026-06 audit)

A cross-source audit (Air DAM + Drive + the Klaviyo send slices + the Figma email-system
export) was reviewed and approved/denied by Bryce. The pool is a curated lens of **source
masters**, not a hosting layer — individual masters still resolve through the §1 chain at
build time (gaps stop the build).

**Result — 163 approved source masters**, by type: 42 ingredient · 35 portrait ·
34 wordmark · 16 product · 15 icon · 13 lifestyle · 4 graph/chart · 2 illustration · 2 other.

**Three asset states** (the delineation Bryce asked for):

- **READY** — clean master, locked into the pool as-is.
- **RESET** — good visual, needed work before use (baked text to strip, background artifact
  or frame edge to crop out). Resolved, never silently dropped.
- **DROP** — off-brand, pre-rebrand, duplicate, third-party brand, or low-value.

**RESET resolution (16 items — all accounted for, nothing lost):**

- **6** portrait/ingredient masters cropped (vision-determined boxes, verified) → added to pool
  (the 157→163 delta).
- **2** dropped (low-value landscape card · duplicate of a clean master already locked).
- **1** denied (third-party Eli Health brand artwork).
- **4** baked-text-heavy slices routed to the **component track** — they were component
  build-references, not pool assets (see below).
- **3** flagged to **re-source the clean Air original** (no baked text) — tracked gaps below.

**Asset ≠ component.** A further 10 Klaviyo send-slices carried baked headlines/wordmarks; they
were classified as **component build-references** (they informed the coded modules in
`components/`), NOT pool assets. Raw images (photography + concept-graphics) are assets; coded
HTML modules are components — the two are catalogued separately.

The per-asset inventory (source, version/imgix id, vision description, sha) lives in the
CreativeOps curation ledger; this doc pins the chain, the states, and the open gaps.

## 7 · Texture / background treatments

The sends use a recurring texture vocabulary (catalogued 2026-06). The **layout
treatments** are coded as components, not assets: text-over-photo overlay (`hero-art-overlay`),
gradient colour band (`hero-color-band`). The orange/ink painterly band is a **text-over-texture layout** (a tinted panel
with the texture placed as a background image — NOT `hero-color-band`, which is solid-fill/no-image) over a **placed texture asset** — the pool's two 'other'-type
amber-fluid / oil-texture masters (§6). The **background-image masters** below resolve through the §1 chain:

| treatment | master source |
|---|---|
| Blue brain-art masthead (brain-scan / free-radical / marbled ink) | Getty **brain master**, Drive (§1 Drive exception list) |
| Botanical backdrop (artichoke / mushroom / ginkgo) | in the pool (Air) |
| Orange / ink painterly texture | in the pool (the 2 'other'-type amber-fluid / oil masters, §6) |
| Starry night-sky field | tracked gap — source at first use |

The full treatment catalogue (frequency, how-used, asset-vs-component) is the **Texture
treatments** section of `components/catalog.md`.

## 8 · Tracked sourcing gaps (gaps stop the build, §1)

These are known-open and resolve at first use rather than being pre-hosted:

- **Re-source clean Air originals** (no baked text) for the 3 RESET items above.
- **Texture masters to source at first use:** the starry night-sky field. (The brain master is
  already available via the Drive Getty exception, §1; the orange/ink painterly texture is in the
  pool — the 2 'other'-type masters (§6) — placed as the background of a text-over-texture / tinted-panel layout.)
