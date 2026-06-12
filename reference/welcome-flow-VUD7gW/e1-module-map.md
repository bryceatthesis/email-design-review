# E1 "Welcome Email 1" — module map (derived)

> **Derived 2026-06-10 by Claude Code from original template + render (not from slice analysis).**
> (The tasking phrase reproduced verbatim read "derived undefined by Claude Code from original template + render (not from slice analysis)" — the stray token "undefined" is a tasking artifact; treat as the derivation date slot.)
>
> Sources:
> - `_incoming/welcome-flow-VUD7gW/e1-original-render.png` (600×9000; content ends ≈ y1900) — viewed at full resolution in three crops; ground-truth composition/palette.
> - `designs/welcome-quiz/original/01-welcome-email-1.html` (24,192 B, six CloudFront slices + live-text coupon/footer blocks) — its **live text is the verbatim copy source**; slice `alt` text is stale (e.g. alt "Subscribe Now" where the render shows the TRY NOW pill) and is ignored per policy; its CDN `<img>` tags are never copied.
> - Companion asset provenance: `reference/welcome-flow-VUD7gW/e1-source-assets.md` (sha-pinned).
>
> Subject: **Your brain boost is here.** (per build tasking). No module map existed before this file; no slice-analysis provenance shas exist for E1.

## Section order (top → bottom, measured from render)

| # | module | y-range (render) | treatment in build |
|---|---|---|---|
| 1 | Wordmark, white on gradient | 38–75 (≈167×37 px mark) | **Live text** per spec §4 (task directive — NOT the donor wordmark image): Helvetica Neue stack, weight 900, 48px (measures 167×36 at HN-Bold, matching render), `letter-spacing:-0.01em`, uppercase, `#FFFFFF`, links to takestasis.com |
| 2 | Hero display: level-up line + $50 OFF | 148–187 / 227–356 | Live text, white on gradient. "It&rsquo;s time to level up." ≈38px/500. "$50" 900/140px/−0.05em with "OFF" 900/56px run-in; mobile 96px/40px |
| 3 | Subscribe block: when-you-subscribe + "+" + EXTRA pill + 10% line | 400–494 | Live text, black `#000000` on light gradient zone. EXTRA = Lime `#EEEF78` 999px pill (canonical Lime, NOT donor's `#EAEF7A`), black 800/18px uppercase label; "10% OFF + FREE Shipping" 800/24px |
| 4 | Welcome Kit packshot | ≈522–880 | Inline data-URI image from donor, alt "Stasis Welcome Kit", 552px wide, transparent PNG sitting directly on gradient; sha-pinned `b436523f…` per e1-source-assets.md |
| 5 | Brain-boost + coupon code | 875–949 | Live charcoal `#222427` text on white; code line is the **verbatim Klaviyo tag** at 800/26px (mobile 17px, mirroring the original's desktop/mobile pair) |
| 6 | CTA pill "TRY NOW" | 985–1040 | Spec §5.1 bulletproof VML+HTML pill, fill `#FF541E`, **black** label, 800/15px/+0.18em uppercase, 999px |
| 7 | Creme dome arc | 1110–1180 | Pure code per spec §8: fixed-height row (`font-size:0; line-height:0`), white→Creme `#F4EFEB` dome, decoupled from text height. NOT an image |
| 8 | Closing lockup on Creme | 1212–1267 / 1328–1426 / 1479–1527 | Spec §5.2 verbatim: outline STASIS pill + "+" + filled white STIMULANT pill, all royal `#3D72E6`, on Creme `#F4EFEB`; closer "BALANCE FOR BOLD MINDS" 900/48px/−0.05em royal; then §5.1 CTA "SHOP NOW" |
| 9 | Legal footer | 1613–1751 | Live text on **white** (render ground truth — the Creme panel ends flat after SHOP NOW; the approved donor put this on Creme, the render does not). FDA line *italic* 12px; remaining lines 11px; verbatim Liquid tags |

## Verbatim copy (ground truth — use HTML entities in build)

| row | text (verbatim) | where |
|---|---|---|
| T1 | STASIS | wordmark (live text) |
| T2 | It's time to level up. | hero (build as `It&rsquo;s time to level up.`) |
| T3 | $50 OFF | hero amount |
| T4 | when you subscribe | subscribe block |
| T5 | + | subscribe block connector |
| T6 | EXTRA | lime pill label |
| T7 | 10% OFF + FREE Shipping | subscribe block |
| T8 | Your Brain Boost is Here! Use code | code intro |
| T9 | {% coupon_code 'Welcome_Discount' %} | coupon line — Klaviyo tag verbatim |
| T10 | TRY NOW | CTA 1 |
| T11 | STASIS | lockup outline pill |
| T12 | STIMULANT | lockup filled pill |
| T13 | BALANCE FOR BOLD MINDS | closer |
| T14 | SHOP NOW | CTA 2 |
| T15 | These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease. | footer, italic |
| T16 | No longer want to receive these emails? | footer |
| T17 | {% unsubscribe %} or View our Privacy Policy. | footer ("Privacy Policy" is the link) |
| T18 | {{ organization.full_address }} | footer, Liquid verbatim |
| T19 | © {% current_year %} {{ organization.name }}. All rights reserved. | footer, Liquid verbatim (© as `&copy;`) |
| T20 | $50 off your Stasis Welcome Kit — plus an extra 10% OFF + FREE Shipping when you subscribe. | **builder-added** hidden preheader (not in original; donor precedent) |

## Links (from original template)

- Wordmark → `https://takestasis.com/`
- Hero, subscribe block, kit photo, coupon area, TRY NOW, lockup/SHOP NOW → `https://takestasis.com/discount/Welcome_Discount/?redirect=/products/welcomekit`
- Privacy Policy → `https://takestasis.com/policies/privacy-policy` (link color royal `#3D72E6`; legacy `#197BBD` retired per spec §2)

## Palette for this email

- Top zone: CSS `linear-gradient(180deg,#3D70E5 0%,#94B1F5 45%,#B7CBFD 63%,#F2F6FF 100%)` (donor implementation, sanctioned as pure-code rebuild in e1-source-assets.md; render samples y8 `#3E71E6`, y550 `#B9CEFB`, y870 `#F5F8FF` agree). VML gradient fallback `#3D70E5→#F2F6FF` for Outlook.
- Lime pill `#EEEF78` · CTA `#FF541E` (black label) · Royal `#3D72E6` · Creme `#F4EFEB` · charcoal `#222427` · subscribe-block black `#000000` · white text on gradient.

## Image expectation

**Exactly 1 inline data-URI image**: the Welcome Kit packshot (sha256 `b436523f77b76caf163fb53f400386dee4630628359c12aca53f0c28ce8ec6c0`, 873,613 B). The e1-source-assets.md table sanctioned 2 (wordmark image + kit) with live-text wordmark noted as the spec-§4 option; the build tasking pins the live-text wordmark, so the wordmark image row is unused. Dome arc = CSS code (spec §8). Zero CDN references.

Provenance: kit photo = catalog row "SHOT_6_WELCOME_KIT_0298.jpg" → Air `bf6cokwMJ/f180a260-0e93-4451-b3f9-ede3ef47cd90`, Drive `18bwpgXrb-lEZRDHERK40iC2Zmsl1m09r` (Status "Approved candidate"; Bryce Slack approval 2026-06-04 16:40 EDT per e1-handoff-receipt-v3.md). The build tasking separately named candidate "SHOT_8_WELCOME_KIT_0126.jpg" (Notion page `2a9546ad-18d8-4d11-bdb9-22045717309b`) — catalog fetched live 2026-06-10: SHOT_8 is a **different asset** ("Top-down open welcome kit box with blue interior, inserts, and Daytime/Nighttime jars", Air `bf6cokwMJ/9a597fae-b7cf-421d-9826-2891416d7b80`, Drive `1G8pk6jD5wUNdgqm5iWa2QUPPbN2D29P7`, Status "Approved candidate"), not the front-facing packshot the render shows and the donors embed. The sha-pinned SHOT_6 resolution in e1-source-assets.md is honored; the SHOT_8 label in the tasking was a mislabel. Discrepancy flagged to Theo/Bryce.
