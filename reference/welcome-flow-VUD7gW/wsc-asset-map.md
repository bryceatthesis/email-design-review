# WSC send-version asset map — Klaviyo image library

**Date:** 2026-06-11 · **Phase 0 (host assets)** · Source: the five APPROVED live-text emails in `designs/welcome-quiz/cc-from-spec/01..05` (data-URI extraction, sha-256 dedupe: 31 embedded URIs → 27 unique images; no SVGs found).

Uploads via Klaviyo Images API `POST /api/image-upload/` (revision 2024-10-15), account company `YsCgQB` (Stasis). **Verification:** every CDN URL fetched back and sha-256 compared against the exact bytes sent — all 27 byte-identical (Klaviyo did not re-encode; no pixel-compare needed).

| sha256 (first 16) | filename | emails | klaviyo image id | CDN URL | verify |
|---|---|---|---|---|---|
| `41b2199dec5ac4e9` | wsc-html-e1-bg-hero-gradient.png | e1 | 334369241 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/63f385a0-c3e5-4789-aedd-279e42b5201f.png | sha-match |
| `b436523f77b76caf` | wsc-html-e1-hero-welcome-kit.png | e1 | 334369255 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/85ff86f4-7b43-4898-9f65-04267ff40155.png | sha-match |
| `2c5ae4dc21559a95` | wsc-html-e2-bg-hero-marble.jpg | e2 | 334369261 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/cdfd8c58-3384-4d87-afba-aee8c508665f.jpeg | sha-match |
| `7bcbc26af82ed5cf` | wsc-html-e2-capsules-dashed-ring.png | e2 | 334369274 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/8d2f7725-a67f-42c4-bda6-cc246a157a7f.png | sha-match |
| `18af739c354f866a` | wsc-html-e2-divider-wave.jpg | e2 | 334369280 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/f0b9c697-5029-46b8-9faa-3ad84d12cb21.jpeg | sha-match |
| `97741e7bd351356e` | wsc-html-e2-icon-brain.png | e2 | 334369304 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/69ca7aa1-5c82-4186-a471-095d57c08ae6.png | sha-match |
| `7a2540b3e9f9cc7c` | wsc-html-e2-icon-capsule.png | e2 | 334369384 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/4a6fb3db-6d70-48f0-9406-f04e0df4538f.png | sha-match |
| `a26c988e0ed17a7e` | wsc-html-e2-icon-hourglass.png | e2 | 334369414 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/8ee20ed7-f42b-4cd0-b7b0-d16e21e73653.png | sha-match |
| `4148f1ae64c1bd4c` | wsc-html-e2-icon-leaf.png | e2 | 334369421 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/c0229ffd-236b-4f5e-95bf-6d0860961225.png | sha-match |
| `902b6445834d516e` | wsc-html-e2-icon-zzz.png | e2 | 334369007 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/e56b918d-e2f3-4c2c-8c9f-9ec936b18a06.png | sha-match |
| `1d71eb1f54aca696` | wsc-html-e2-photo-customer-laptop.jpg | e2 | 334369428 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/154a2c24-785c-49df-89af-349d2d41d066.jpeg | sha-match |
| `813e93173d94af01` | wsc-html-e2-photo-fingers-capsule.png | e2 | 334369438 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/3bc51a79-b924-452d-80ff-27d78d4b6b81.png | sha-match |
| `728ade09e6eadbee` | wsc-html-e2-product-set-kraft-box.jpg | e2 | 334369449 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/461a9594-b39d-448e-8c51-2d8509670b4f.jpeg | sha-match |
| `1a23f0335a442166` | wsc-html-e3-capsule-split-bottom.png | e3 | 334369536 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/d7f18650-c949-4d43-a87b-4ef515fa2fb1.png | sha-match |
| `f6557958c48edda5` | wsc-html-e3-capsule-split-top.png | e3 | 334369632 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/0c67c6dd-18f3-4152-b603-367e4d97f624.png | sha-match |
| `cd2f79bb77081a5e` | wsc-html-e3-photo-customers-laughing.jpg | e3 | 334369641 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/3139a530-8876-4d10-b833-90925fbb207f.jpeg | sha-match |
| `d39f04560e06cd32` | wsc-html-e3-product-jars-day-night.jpg | e3 | 334369649 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/26f177cd-cb0f-44a9-88d8-9adf3c7d4d45.jpeg | sha-match |
| `addd435d16656308` | wsc-html-e3-stat-crossed-capsules.jpg | e3 | 334369653 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/4268d069-6090-4ed7-850b-93cbef804035.jpeg | sha-match |
| `d47eb5e71fb9e8aa` | wsc-html-e4-photo-customer-henley.jpg | e4 | 334369675 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/c4c1787e-55df-4861-a4d7-b5446bc6416d.jpeg | sha-match |
| `038e89bb8736a5db` | wsc-html-e4-photo-real-people.jpg | e4 | 334369694 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/d096dd26-be08-4aa2-90a3-bad27d7f8991.jpeg | sha-match |
| `49e3ce4cceaf62e6` | wsc-html-e5-icon-brain.png | e5 | 334369701 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/8b2106f3-e46b-47c0-a1d3-f5efbd6e7fa7.png | sha-match |
| `2988277622619505` | wsc-html-e5-icon-capsule.png | e5 | 334369713 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/adcf824d-a26a-4725-a8a0-de3a1d8f9bc0.png | sha-match |
| `947bc82cfc07203b` | wsc-html-e5-icon-hourglass.png | e5 | 334369720 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/770fdbbb-1009-4f90-aaa4-33a7c89f7023.png | sha-match |
| `614dc6be714246b3` | wsc-html-e5-icon-zzz.png | e5 | 334369726 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/00d1ac1c-203d-4e7a-925f-29946109defa.png | sha-match |
| `c15e130e047b13bc` | wsc-html-e5-product-jar-water-glass.jpg | e5 | 334369733 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/79bcb3a0-b908-4011-bc8c-04710117a525.jpeg | sha-match |
| `2eebc27153336d56` | wsc-html-shared-logo-ink.png | e3,e4,e5 | 334369741 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/602ec7a2-6456-4fb1-bd52-f1c0eb365cd6.png | sha-match |
| `92970f10b5399e7f` | wsc-html-shared-logo-white.png | e1,e2 | 334369752 | https://d3k81ch9hvuctc.cloudfront.net/company/YsCgQB/images/02b774d0-8762-42c7-9dfd-1cea2705eb0b.png | sha-match |

Full sha256 values:

- wsc-html-e1-bg-hero-gradient.png: `41b2199dec5ac4e9d6d35bad88a60d49e442c6047798f0ece1bff0d52ad09673`
- wsc-html-e1-hero-welcome-kit.png: `b436523f77b76caf163fb53f400386dee4630628359c12aca53f0c28ce8ec6c0`
- wsc-html-e2-bg-hero-marble.jpg: `2c5ae4dc21559a95352845fe3c2eab9708de008f30fa38e7ed79188591ad170c`
- wsc-html-e2-capsules-dashed-ring.png: `7bcbc26af82ed5cf6a8d00edb1b86309a43c8318ada3ef73094ac71ad0df628d`
- wsc-html-e2-divider-wave.jpg: `18af739c354f866af83cfd822fe278f2c67c58dbd473c353a366282dcb2638ab`
- wsc-html-e2-icon-brain.png: `97741e7bd351356e5a074419e8a3dd427110fc670005066557e1852860a90c96`
- wsc-html-e2-icon-capsule.png: `7a2540b3e9f9cc7ce2cac1fd03a8af94d20618a3ce10892ad66a4c5fde91997c`
- wsc-html-e2-icon-hourglass.png: `a26c988e0ed17a7e4e3e719abe1c45c172901970d957150617b0deba52f96718`
- wsc-html-e2-icon-leaf.png: `4148f1ae64c1bd4cc28305703ddeafa2a047ec7450b4b35692ea7cb6419ed6f6`
- wsc-html-e2-icon-zzz.png: `902b6445834d516efe5e2f12736b86da8705c0926adf98ea0734bad954d3e198`
- wsc-html-e2-photo-customer-laptop.jpg: `1d71eb1f54aca696bee78f54937f6a410864491c8253ea9fd38730634c235eb5`
- wsc-html-e2-photo-fingers-capsule.png: `813e93173d94af01585b4b246b72e00832b9e56bebc56a60420630044f5bc5c9`
- wsc-html-e2-product-set-kraft-box.jpg: `728ade09e6eadbee1f2de9cb63c208636b8f0f0a78fb5c9b9cfb594db228d9a5`
- wsc-html-e3-capsule-split-bottom.png: `1a23f0335a44216615cf03fa276b945c360590da54eabbfcd28d0aeef5004d17`
- wsc-html-e3-capsule-split-top.png: `f6557958c48edda5b4b3f26f5e2b3eac1fdabb4fa79f9b78e176169781748945`
- wsc-html-e3-photo-customers-laughing.jpg: `cd2f79bb77081a5ea188bb87f8fd7a7e27ffd5072cd0086d660c8c381e81f14e`
- wsc-html-e3-product-jars-day-night.jpg: `d39f04560e06cd32a7f88522b271b856887b4cc9648fd29f150fca36bd07be7b`
- wsc-html-e3-stat-crossed-capsules.jpg: `addd435d166563086b841784ecdc2a20435a50fb511c9138cdf12ab208196375`
- wsc-html-e4-photo-customer-henley.jpg: `d47eb5e71fb9e8aa81371970a9773ba351420b3bfe26e23dfb5490ea4dfe6055`
- wsc-html-e4-photo-real-people.jpg: `038e89bb8736a5dbb32c6d10e7fb0a072a30b579f01985a104300ed762ae18c7`
- wsc-html-e5-icon-brain.png: `49e3ce4cceaf62e6aacfe5edb9750d2dbeab35d23ca6eada1179ea5a154e1f42`
- wsc-html-e5-icon-capsule.png: `29882776226195050cc12e1b5ea12382e7121edd518e90adda2f98baab4c977f`
- wsc-html-e5-icon-hourglass.png: `947bc82cfc07203b4f55ffc3873bc7ac680475e85a8cd4d46a09b7e8caa52fa6`
- wsc-html-e5-icon-zzz.png: `614dc6be714246b3e4752c4afad8812c2d34c915e6f2a0212868d424b9989392`
- wsc-html-e5-product-jar-water-glass.jpg: `c15e130e047b13bcf1e924bd1412ad343d947f63679fa9d1306a4f4281017440`
- wsc-html-shared-logo-ink.png: `2eebc27153336d56050972edd3525c3558a2cf68391f532353ef1a91f73ed637`
- wsc-html-shared-logo-white.png: `92970f10b5399e7f984b2a07bfb2b68cc3db890e88d22c81eea2a3068ed85132`

Notes:
- `shared-logo-white` (white wordmark) appears in e1+e2; `shared-logo-ink` (black wordmark) in e3/e4/e5.
- `e1-bg-hero-gradient` and `e2-bg-hero-marble` are used as `background=` / `background-image:url()` (td backgrounds), not `<img>`; swap both the attr and the CSS url in the send versions. `e2-bg-hero-marble` appears as both `td background=` and CSS `background-image` of the same cell.
- All other entries are `<img src>` swaps.

## Fonts — Antarctica + Tiempos Regular RESOLVED (hosted on Stasis Shopify Files); Tiempos Medium still unhosted

**Update 2026-06-11 (E1 send repair):** the Shopify MCP connector is still unauthenticated (`get-shop-info` re-failed), but the four Antarctica woff2 are now LIVE on the Stasis store's own Shopify Files CDN — Files `last-modified: 2026-06-11 19:44 GMT`, i.e. uploaded out-of-band after the blocker above was logged (provenance: not uploaded by an agent; presumed manual upload — confirm with Bryce). Discovery + verification done with plain HTTPS, no Admin API: each URL fetched and sha-256 compared against the local masters — **all four byte-identical**. Headers: `content-type: font/woff2`, `access-control-allow-origin: *`, `cache-control: public, max-age=31557600`. Canonical host `cdn.shopify.com` (store id 0639/3511/9576); same bytes also served at `takestasis.com/cdn/shop/files/<name>`.

| file | sha256 (first 16) | hosted URL (canonical) | verify |
|---|---|---|---|
| Antarctica-Regular.woff2 | `d14aa382c44108a3` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Regular.woff2 | sha-match |
| Antarctica-Medium.woff2 | `91a92ab72c1dfb5d` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Medium.woff2 | sha-match |
| Antarctica-SemiBold.woff2 | `334dd2da7e6ef84b` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-SemiBold.woff2 | sha-match |
| Antarctica-Bold.woff2 | `ad195eee21c3190f` | https://cdn.shopify.com/s/files/1/0639/3511/9576/files/Antarctica-Bold.woff2 | sha-match |

`fontface-hosted.html` now exists at `_incoming/welcome-flow-VUD7gW/assets/fonts/fontface-hosted.html` (the drop-in hosted @font-face block + full provenance notes).

**Tiempos Text — Regular RESOLVED on Files; Medium still unhosted (update 2026-06-11, E4 send repair):**
- TiemposText-Regular (`b69bcc874fd7b155`): now LIVE on Shopify Files under the lowercase name `tiempos-text-regular.woff2` — https://cdn.shopify.com/s/files/1/0639/3511/9576/files/tiempos-text-regular.woff2 — fetched and sha-256 compared against the local master: **byte-identical** (full `b69bcc874fd7b155826a0424c1e3f56deebb6db3ec6201305a28d601921646e2`). Headers: `content-type: font/woff2`, `access-control-allow-origin: *`, `cache-control: public, max-age=31557600`; Files `last-modified: 2026-06-11 19:54:35 GMT` — ten minutes after the Antarctica four, i.e. the same out-of-band upload session (provenance: not uploaded by an agent; presumed manual — confirm with Bryce). The fragile theme-asset copy (`/cdn/shop/t/281/…`) is now moot; use the Files URL.
- TiemposText-Medium (`a568c34aca2fe636`): still hosted nowhere as woff2. (Caution: `TiemposText-Medium.woff` — note **.woff**, not woff2 — answers 200 on Files; different format/bytes, NOT verifiable against the woff2 master — do not use.)
- Impact check: the approved E1 never references 'Tiempos Text' in markup (declarations were dead weight; dropped in `cc-send/01`). E2–E5 send builders must check their own files' actual serif usage before treating Tiempos as a blocker.

**Update 2026-06-11 (E5 send repair):** E5 verified Tiempos-free in markup (all 'Tiempos' mentions outside `@font-face` are inside the font-kit CSS comment; zero body usage — same dead-weight situation as E1, declarations dropped). The hosted 4-face Antarctica block (this file's table above; sha re-verified against local masters this session) was swapped into BOTH `cc-send/05` (now 40,014 B, zero data URIs) and `cc-from-spec/05` (180,470 B — images remain embedded by design, font block only). Proof: check_modes PASS at 375/600/darksim for both files, pre-swap vs post-swap full-page renders byte-identical (all 6 screenshots), `document.fonts` reports all four Antarctica faces `loaded` from cdn.shopify.com, glyph-parity crop max channel delta 0. Tiempos remains unhosted but blocks nothing in E1 or E5; E2/E3/E4 builders still must run their own usage check.

**Update 2026-06-11 (E4 send repair):** E4 usage check: markup uses 'Tiempos Text' ONLY at weight 400 (the three `.qq` testimonial quotes; the 480px media block touches `.qq` font-size only, never weight) — so the Tiempos 500/Medium declaration was dead weight and was DROPPED (same sanctioned path as E1/E5); Tiempos 400 swapped to the newly-discovered Files URL above. All six embedded payloads sha-verified against the local masters before swapping (file-to-file, base64 never read). Applied to BOTH `cc-send/04` (443,513 → 22,799 B, zero data URIs of any kind, 3 Klaviyo-CDN images intact) and `cc-from-spec/04` (796,211 → 375,458 B — images remain embedded by design, font block only). Also trimmed the §2.0 spec-pasted CSS comment in `cc-send/04` that contained a literal `@media …{` string (naive grep now counts exactly 1 @media; rule content untouched). Proof for both files: check_modes PASS at 375/600 + light-only, zero offenders @375, pre-swap vs post-swap full-page pixel compare max channel delta 0 / no diff bbox at 375-light, 600-light, 600-darksim; `document.fonts` reports all five faces (Antarctica 400/500/600/700 + Tiempos Text 400) `loaded` from cdn.shopify.com. Tag counts re-proved on `cc-send/04`: 3× coupon_code + full footer set incl. manage_preferences.

**Update 2026-06-11 (E2 send repair):** E2 usage check: markup uses 'Tiempos Text' ONLY at weight 400 (three testimonial paragraphs, all `font-weight:400`) — Tiempos 400 swapped to the lowercase Files URL above; the Tiempos 500/Medium declaration was dead weight and DROPPED (same sanctioned path as E1/E4/E5). All six embedded payloads sha-verified against the local masters before swapping (file-to-file, base64 never read): embed sha == master sha == hosted sha for every face, including Antarctica-Bold 700 (the original blocker — resolved by the out-of-band Files upload; all 14 weight-700 CTA usages now load the true Bold). Applied to BOTH `cc-send/02` (NEW — built from the verified staged copy at /tmp/wsc-e2-send: footer + 3 coupon insertions + 12 Klaviyo-CDN image swaps were diff-proven sanctioned-only against the approved file; now **42,232 B, zero data URIs of any kind**) and `cc-from-spec/02` (1,410,403 → 989,652 B — images remain embedded by design, font block only). Proof: check_modes PASS at 375/600 + light-only + zero offenders @375 for both files; `cc-from-spec/02` pre-swap vs post-swap screenshots byte-identical (375-light, 600-light, 600-darksim); `cc-send/02` full-page renders byte-identical to the embedded-font staged renders at 600 AND 375; `document.fonts` reports all five faces (Antarctica 400/500/600/700 + Tiempos Text 400) `loaded` from cdn.shopify.com. Row-parity vs approved: every original row identical height, offsets shifted exactly by the four inserted blocks (C-a 51.8px @600 only, C-b 64.8px @375 only, C-c +42.8px in-band @600 only, footer 193.4/229.0); E2's mobile band still ends at "WITH CODE:" with NO code (locked original quirk preserved, render-verified). Tag counts re-proved on `cc-send/02`: 3× coupon_code + full footer set incl. manage_preferences. Crops of all four inserted zones visually matched against `wsc-send-crops/e2-*`.

**Update 2026-06-11 (E3 send repair):** E3 usage check: markup uses 'Tiempos Text' ONLY at weight 400 (one testimonial `<p>`, inline stack `'Tiempos Text',Georgia,'Times New Roman',serif`) — Tiempos 500/Medium declaration was dead weight (`document.fonts` left it `unloaded` even when embedded) and was DROPPED (E1/E4/E5 precedent); Antarctica 400/500/600/700 + Tiempos 400 swapped to the hosted Files URLs above. All five hosted URLs independently re-fetched and sha-256 re-verified byte-identical to the local masters this session (and the six embedded payloads sha-matched the masters before swapping; file-to-file, base64 never read). Shopify MCP re-checked: still unauthenticated — discovery again via plain HTTPS. Applied to BOTH `cc-send/03` (444,947 → 24,267 B, zero data URIs of any kind, 6 Klaviyo-CDN images intact) and `cc-from-spec/03` (777,381 → 356,556 B — images remain embedded by design, font block only). Proof for both files: stripped-diff confined to the font-kit `<style>` block; check_modes PASS at 375/600 + light-only, zero offenders @375; full-page pixel compare max channel delta 0 at 375-light/600-light/600-darksim — `cc-from-spec/03` post-swap vs the approved embedded baseline, AND `cc-send/03` post-swap vs its pre-swap build (render heights exact: 375×3427 / 600×3473 send, 375×3098 / 600×3228 spec); `document.fonts` reports all five faces `loaded` from cdn.shopify.com in both. Tag counts re-proved on `cc-send/03`: 2× coupon_code + full footer set incl. manage_preferences (wsc-send-spec §3).
