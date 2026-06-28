# Stasis Email Playbook — "what good looks like"

> Distilled from the Men's Health Week build (E1 opener · E2 social-proof · E3 Father's Day), graded against the Antidote agency comps across ~15 review rounds. **These three emails define the *acceptable range / floor* — not the only kind of email we'll ever make, but the bar a Stasis marketing email must clear.** The binding token spec is [`design-language.md`](design-language.md); this file is the design judgment + failure history that sits on top of it.

Companion artifacts:
- Final reference emails: `designs/mens-health-week/build/variants/e1-v2-rd.html` (Framed), `e2-v3-rd.html` (Light), `e3-v1-rd.html` (Overlay).
- Asset pack: `designs/mens-health-week/build/assets/` (every image, sha-pinned, + `manifest.md`).
- Generator: `designs/mens-health-week/build/assemble-variants.py` (one tokenized source → the chrome is identical-by-construction).
- Verification gate: `scripts/check_modes.py` (375/600 reflow + light-only), `scripts/check_public_exposure.py`.

---

## 1. THE BAR (a new Stasis marketing email must hit all of these)

1. **Wordmark locks top, ON the image.** White wordmark over the hero photo as the first element; on light/creme treatments it's **true black (~#0A0A0A)**, never navy. There is **no "blue pill" logo lockup** — that was invented; don't.
2. **Hero is required and cinematic.** Every email opens with a real, in-context lifestyle photo (or a branded color masthead for a stats email). The figure is **never blanketed** by text — copy sits on a baked lower-third scrim or a clean color band so the person stays visible.
3. **Type is bold but not heavy; body is spacious.** Uppercase heroes weight **500**, sentence-case/editorial heroes weight **400** (700 is too heavy). Body **~22px / weight 400**, airy (~4-line wraps like Antidote); 18px reads "too small." Subheads weight 400 (thin, elegant).
4. **One orange CTA per module, welcome-flow treatment.** `#FF541E` pill, `border-radius:999px`, weight **500**, letter-spacing **0.06em**, ~20px desktop / **16px + `white-space:nowrap`** on mobile (one line). Never the component-default 700/0.18em. **No CTA jungle** — exactly one button per section.
5. **Restrained palette.** Creme `#F4EFEB` grounds; royal `#3D72E6` is the accent (closing headline, brand pills); ink `#0E1A38` for body; orange for CTAs only. **Banned:** peach `#FD9A70` / teal `#24DEAD`; any tan-on-tan.
6. **Charts/cards float with separation.** A creme card on white, or a white card on color — never a creme card melting into a creme page.
7. **Antidote-grade footer.** Tall ~88px dome rising from white into creme; STASIS-outline + STIMULANT solid-blue pill lockup; royal `BALANCE FOR BOLD MINDS`; one orange `SHOP NOW`; white-circle social badges with REAL glyphs; FDA + "consult your healthcare provider" disclaimer. No black band, no contact line.
8. **Copy is verbatim and purpose-distinct.** Handed copy used exactly; each email has one clear job; copy identical across treatment variants of one email — only the photo/treatment varies.
9. **Engineering gate.** Reflow-clean at 375 & 600 (zero offenders >376px), explicit light-only declarations, real sha-pinned assets (no emoji/placeholder), <95 KB hosted for send.
10. **Mobile is first-class.** Masthead height held via padding (not shrunk type), stat dividers intact, ingredient rows compact, hero crop "meet in the middle."

---

## 2. THE TYPE SYSTEM (locked — measured off the final emails)

Font: Antarctica (sans) + Tiempos Text (serif, used upright for testimonial quotes & the art caption). All sizes desktop / mobile.

| Role | Weight | Size (d/m) | Tracking | Case | Color |
|---|---|---|---|---|---|
| Hero H1 — uppercase (E1/E2) | **500** | 50–54 / 40 | -0.02em | UPPER | `#0E1A38` (on light) / `#FFFFFF` (on photo) |
| Hero H1 — sentence-case/editorial (E3) | **400** | 40 / 33 | -0.02em | sentence | `#FFFFFF` on navy band |
| Eyebrow | 700 | 15 / 14 | **0.2em** | UPPER | `#FF541E` (light) / `#F6EFE6` (on dark) |
| Hero subhead | 400 | 22 / 18 | -0.01em | none | `#222427` |
| Section H2 (intro/transition) | **500** | 30–32 / 27 | -0.03em | sentence | `#0E1A38` |
| Body copy | **400** | **22** / 18 | -0.01em | none | `#222427` |
| Chart headline | 700 | 34 / 30 | -0.03em | UPPER | `#0E1A38` |
| Stat numeral | 700 | 58 / 46 | -0.03em | — | `#0E1A38` |
| Module heading (Day/Night) | 600 | 32 / 28 | -0.02em | UPPER | `#0E1A38` / `#011D59` |
| Testimonial quote | 400 | 18 | 0 | none (NOT italic) | ink/navy — Tiempos serif |
| Closing headline | 700 | 48 / 39 | -0.02em | UPPER | `#3D72E6` |
| CTA label | **500** | 20 / **16** | **0.06em** | UPPER | `#000000` on `#FF541E` |

Rule of thumb when unsure: **bigger and lighter.**

## 3. COLOR
`#F4EFEB` creme (ground) · `#3D72E6` royal (accent only) · `#0E1A38` ink (body/heads) · `#011D59` navy (night, dark bands) · `#C4D4F3` periwinkle (night alt) · `#FF541E` orange (CTA only) · `#F6EFE6` warm-white (eyebrow on dark). **Day = creme, Night = navy or periwinkle.** Never peach/teal.

## 4. CTA SYSTEM
Anchor + VML twin both: weight 500, `letter-spacing:0.06em`, 20px, `text-transform:uppercase`, `#FF541E` bg, `border-radius:999px`, black label. Desktop padding ~17px 46px. Mobile (`@media max-width:480`): `font-size:16px; white-space:nowrap; padding ~13px 28px` so it stays one line; nbsp-glue the last 1–2 words of long labels for a balanced break. (See [[marketing-cta-welcome-treatment]].)

## 5. FOOTER SYSTEM (identical across all emails)
Dome: `<div style="height:88px;background:#F4EFEB;border-top-left-radius:50% 100%;border-top-right-radius:50% 100%">` rising from a white td. Then: STASIS (creme outline pill, royal text) + "+" + STIMULANT (solid `#3D72E6` pill, white text); `BALANCE FOR BOLD MINDS` (700/48/royal); one `SHOP NOW`; three white-circle social badges (real IG/FB/TikTok glyphs); FDA + consult disclaimer (+ the † survey paragraph on the stats email). No black band, no contact line.

## 6. PHOTO / HERO TREATMENTS — and the variety rule
**Not all emails should use the same hero format.** The three treatments that passed:
- **Overlay** — full-bleed photo, wordmark on it, text on a baked lower-third scrim that fades into a navy band (used on E3). Crop "meet in the middle": full scene, not a tight zoom.
- **Framed** — wordmark on creme, photo in a rounded frame, headline/subhead/CTA on the light field below (used on E1).
- **Color band / masthead** — branded color masthead with the stat card floating on it (used on E2).
Choose the treatment that fits the email's job; **do not template one hero for all three.**

## 7. PER-EMAIL JOBS (the MHW set, as the reference)
- **E1 Opener** — name the problem (the late-day crash) → the science (stimulant-vs-Stasis curve in a floating creme card) → the system (unboxing) → quiz/shop CTAs. Education-first.
- **E2 Social proof** — stat masthead (96/88/65 in a floating card) → Day module (creme, jar + ingredient highlights + testimonial) → Night module (navy/periwinkle, same) → one system CTA. Proof-first.
- **E3 Father's Day** — dad-in-context hero → "the first supplement system…" → focused product shot (the Rx + Day + Night row with the green shelf as the section's bottom border) → 3 benefit rows → gift CTA. Gift-first; exactly 2 CTAs.

## 8. FAILURE LOG (what we tried, why it was wrong, the rule)

| ✗ Mistake | Rule that prevents it |
|---|---|
| Tan-on-tan chart card (creme on creme, disappeared) | Cards float with contrast — creme-on-white or white-on-color. |
| Invented a "blue pill" STASIS logo | Light/creme = true black wordmark; photo = white. Never invent a logo treatment. |
| Logo placed below the hero photo | Wordmark locks top, on the image, always first. |
| Peach/teal Day-Night | Day=creme, Night=navy/periwinkle; royal is accent only. |
| Over-bold hero (700) | Uppercase=500, sentence-case=400. |
| Body too small (17–18px) | Body ~22px/400, airy. Bigger + lighter when unsure. |
| CTA jungle + "Not sure where to start" module | One CTA per module; no helper/junk modules. |
| Component-default CTA (700/0.18em, bulky on mobile) | Welcome-flow pill: 500/0.06em, 16px nowrap mobile. |
| Aggressive hero crop (scene lost) | "Meet in the middle" — full scene, photo fades into the band. |
| Rewriting handed copy | Verbatim only; copy identical across a single email's variants. |
| Wrong footer (black band, contact line, short dome, fake icons) | The footer system in §5, exactly. |
| Stat box broke on mobile; masthead shrunk to 31px | Mobile is first-class — hold height via padding, run the 375/600 gate. |
| Arguing from CSS when Bryce flagged a visual | Measure rendered pixels of ours vs the reference; fix toward his eye; if identical-but-still-off, the reference is upstream. Default to changing, not defending. |
| Auto-picking one blank-page "redesign" | Produce multiple comp-anchored directions; Bryce's eye is the gate. Promotion ≠ approval. |

## 9. PROCESS
Source imagery + anchor to comps before designing; offer **multiple directions**, let Bryce pick. Build from one tokenized generator so the chrome can't drift. Verify with **rendered pixels** (check_modes + crops), never CSS-equality alone. Stage with Antidote on the left, ours on the right; **link Bryce every time.** Publishing/scheduling/sending is always Bryce's click.

See also: [[mhw-9variant-build]], [[wordmark-locks-top]], [[trust-bryce-eye-dont-argue]], [[verify-rendered-pages]], [[always-link-for-review]].
