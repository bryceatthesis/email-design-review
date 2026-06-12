# WS-C send-spec — footer + coupon insertion for the cc-send copies (A/B variant B)

> **SUPERSEDED IN PART 2026-06-12 (Bryce, Gmail iOS review of the staged sends):** the **"variant B's coupon line must match each original exactly" governing call is replaced by `reference/send-prep-spec.md` §2** — every coupon zone shows context AND code in BOTH modes, the code sits directly under its context line, exactly once per zone, and **no standalone bare code lines anywhere**. This retires: governing call 2 in the header below, the §2 intro "locked call", §2.2's E2 mobile-band quirk ("ends at WITH CODE: with no code" — now forbidden), the bare mobile code insertions §2.2b / §2.3b / §2.4a / §2.5a, §3's coupon crop and tag-count expectations, and §4's open item on §2.5b. The cc-send copies were coupon-normalized to send-prep-spec §2 on 2026-06-12. **Still valid** — and generalized into send-prep-spec: the footer spec (§1), the visibility plumbing (§2.0), and the verification approach (§3's structure). Original text below is unedited; where they conflict, send-prep-spec §2 wins.

> **Derived 2026-06-11 by Claude Code** from the ORIGINAL Klaviyo templates
> (`designs/welcome-quiz/original/0N-*.html`, live text — data-URI-stripped working copies, never read raw)
> + headless-CDP renders of those originals at 600px and 375px (scripts/_cdp.py, unique /tmp profiles).
> Footer and coupon zones were **viewed as rendered crops**; all visual claims below are render-verified.
> Crops persisted at `reference/welcome-flow-VUD7gW/wsc-send-crops/` (naming: `eN-<width>-*-coupon|footer|tail|band.png`).
>
> Governing calls (Bryce, locked 2026-06-11):
> 1. Send versions get the legally-required unsubscribe footer.
> 2. **Variant B's coupon line must match each original exactly.**
> 3. The approved cc-from-spec render is the contract — the ONLY permitted changes are: footer added,
>    coupon line added (matched to original), font/image sources swapped. Anything else is a defect.
>
> Audience: the cc-send build agent. This file is self-sufficient — you do not need to open the originals.

---

## 0 · Tag inventory — originals vs approved rebuilds

Every Klaviyo template tag in the five originals (exhaustive — `{%…%}` and `{{…}}` grep over data-URI-stripped copies):

| tag | E1 orig | E2 orig | E3 orig | E4 orig | E5 orig | in rebuilds today |
|---|---|---|---|---|---|---|
| `{% coupon_code 'Welcome_Discount' %}` | 2× | 3× | 2× | 3× | 3× | E1: 1× (approved, covers both modes) · E5: 1× (in promo band) · E2/E3/E4: **0** |
| `{% unsubscribe %}` | 1× | 1× | 1× | 1× | 1× | E1 only |
| `{% manage_preferences %}` | **0** | 1× | 1× | 1× | 1× | none (E1 original doesn't have it either — correct) |
| `{{ organization.full_address }}` | 1× | 1× | 1× | 1× | 1× | E1 only |
| `{% current_year %}` | 1× | 1× | 1× | 1× | 1× | E1 only |
| `{{ organization.name }}` | 1× | 1× | 1× | 1× | 1× | E1 only |

**No other Klaviyo tags exist in any original.** Checked for and found absent: preheader tags, view-in-browser /
web-view tags, hidden-preheader divs, personalization tags (`first_name` etc.). The originals rely on
Klaviyo flow-level preview text. (Side note, NOT in this contract's scope: the E1/E2 rebuilds carry a
builder-added hidden plain-text preheader; E3/E4/E5 rebuilds have none. Parity is a separate call for Bryce.)

The footer link `https://takestasis.com/policies/privacy-policy` appears once per original (inside the footer).

---

## 1 · FOOTER

### 1.1 Original ground truth (render-verified: `wsc-send-crops/e*-600-tail.png`)

Identical visual treatment in all five originals; **E2–E5 footer markup is byte-identical across the four files**
(sha-checked on the unsubscribe block: `55aa91c6a6c46d21…` for all four). E1 differs in exactly one way: its
unsubscribe line has **no `{% manage_preferences %}`**.

Position: the footer is the last content in the email, sitting **directly below the cream closing lockup**
(STASIS+STIMULANT pills / BALANCE FOR BOLD MINDS / SHOP NOW on Creme). The cream panel ends flat; the footer
sits on a **full-width white (#ffffff) background**. Two stacked text blocks:

| block | td padding | text style (all inherited from a wrapper div `font-family:'Helvetica Neue',Arial; line-height:1.3; color:#222427`) |
|---|---|---|
| FDA disclaimer | `9px 0` | 12px, *italic*, centered |
| unsubscribe/address | `9px 18px` | 10px, centered; links `#197bbd` underlined |

Verbatim copy + structure (E2–E5 flavor; Liquid verbatim):

```
These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease.

No longer want to receive these emails?
{% unsubscribe %}, {% manage_preferences %}, or View our <a href="https://takestasis.com/policies/privacy-policy">Privacy Policy</a>.
                                     ← double <br/> gap here →
{{ organization.full_address }}
© {% current_year %} {{ organization.name }}. All rights reserved.
```

E1 flavor (original AND approved rebuild): same, except the second line reads
`{% unsubscribe %} or View our Privacy Policy.` (no manage_preferences, no commas).

Verbatim original inner markup of the unsubscribe block (E2–E5, byte-identical in all four):

```html
<div style="font-family:'Helvetica Neue',Arial;font-size:14px;font-style:normal;font-weight:400;letter-spacing:0px;line-height:1.3;text-align:left;color:#222427;"><div style="text-align: center;"><span style="font-size: 10px;">No longer want to receive these emails?</span><br/><span style="font-size: 10px;">{% unsubscribe %}, {% manage_preferences %}, or View our <a href="https://takestasis.com/policies/privacy-policy" style="color:#197bbd; text-decoration:underline">Privacy Policy</a>.</span><br/><br/></div>
<div style="text-align: center;"><span style="font-size: 10px;">{{ organization.full_address }}</span><br/><span style="font-size: 10px;">© {% current_year %} {{ organization.name }}. All rights reserved.</span></div></div>
```

### 1.2 E1 — diff of approved rebuild footer vs E1 original footer

The approved `cc-from-spec/01` already has the footer (last `<tr>` of the layout table, comment
`<!-- 5 · Legal footer …-->`). **Gaps: NONE.** Every tag and every copy line of the E1 original footer is present
(`unsubscribe`, `full_address`, `current_year`, `organization.name`, FDA line, Privacy Policy link;
manage_preferences correctly absent). The deviations that do exist were all sanctioned in
`e1-module-map.md` row 9 and are part of the approved render — do not "fix" them:

| aspect | E1 original | approved E1 rebuild (sanctioned) |
|---|---|---|
| font stack | `'Helvetica Neue',Arial` | `'Antarctica','Helvetica Neue',Arial,sans-serif` |
| non-FDA size | 10px | 11px |
| Privacy link color | `#197bbd` | royal `#3D72E6` (spec §2 — legacy #197BBD retired) |
| block padding | 9px/18px tds | one td, `20px 40px 40px 40px` |
| line gaps | `<br/><br/>` | `<p>` margins 14px |

**E1 send-copy footer work: none.** Carry it through unchanged.

### 1.3 Insertion spec — E2, E3, E4, E5

Insert ONE row as the **new last `<tr>`** of the single layout table — i.e. immediately after the closing-lockup
SHOP NOW row, immediately before the final `</tbody></table>` (each rebuild ends
`…SHOP NOW…</td></tr>` + blank line + `</tbody></table>`). Use the **approved E1 rebuild footer verbatim** with
exactly one content change — the unsubscribe line gains manage_preferences to match the E2–E5 originals:

```html
<!-- F · Legal footer — white per original render ground truth, verbatim Liquid (wsc-send-spec §1.3) -->
<tr><td align="center" bgcolor="#FFFFFF" class="px" style="padding:20px 40px 40px 40px;background-color:#FFFFFF;text-align:center;">
  <p style="margin:0 0 14px 0;font-family:'Antarctica','Helvetica Neue',Arial,sans-serif;font-style:italic;font-weight:400;font-size:12px;line-height:1.55;color:#222427;text-align:center;">These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure or prevent any disease.</p>
  <p style="margin:0 0 14px 0;font-family:'Antarctica','Helvetica Neue',Arial,sans-serif;font-weight:400;font-size:11px;line-height:1.55;color:#222427;text-align:center;">No longer want to receive these emails?<br/>{% unsubscribe %}, {% manage_preferences %}, or View our <a href="https://takestasis.com/policies/privacy-policy" target="_blank" style="color:#3D72E6;text-decoration:underline;">Privacy Policy</a>.</p>
  <p style="margin:0;font-family:'Antarctica','Helvetica Neue',Arial,sans-serif;font-weight:400;font-size:11px;line-height:1.55;color:#222427;text-align:center;">{{ organization.full_address }}<br/>&copy; {% current_year %} {{ organization.name }}. All rights reserved.</p>
</td></tr>
```

Notes:
- White background is original-correct (renders confirm the cream panel ends before the footer in all five).
- E3/E4/E5 already render their disclaimers ("These statements…" appears in E2–E5 originals ONLY inside this
  footer — the separate †survey disclaimer module in the rebuilds is different copy and stays untouched).
- E2 caveat: the E2 rebuild's closing SHOP NOW row is the last row; same insertion point.
- Styling choice made here: the **approved-E1 treatment** (Antarctica/11px/royal link), not the originals'
  Helvetica/10px/#197bbd — it is the one footer treatment Bryce has already approved in this family, and the
  deviation set is identical to the E1 set he signed off. If byte-faithful original styling is preferred instead,
  that is a one-line call for Bryce; both are fully specified above.

---

## 2 · COUPON LINES — per-email insertion spec

> ⚠ **SUPERSEDED 2026-06-12** — the "match each original exactly" locked call below is replaced by `reference/send-prep-spec.md` §2 (context+code both modes, code under context, once per zone, no bare codes). See the top-of-file banner. Text kept for the record; the font-stack guidance (verbatim `Antartica` fallthrough) survives in send-prep-spec §2 item 7.

**Locked call: variant B coupon lines match each original exactly** — font stacks verbatim (including the
originals' misspelled `Antartica` first family: no client resolves it, so it intentionally falls through to
Lucida/fallback exactly as the original does in real clients — do NOT "correct" it to the rebuilds'
`'Antarctica'` webfont name, which WOULD change rendering), sizes, weights, colors, backgrounds, paddings,
desktop/mobile split. None of the original coupon blocks is wrapped in a link.

### 2.0 Visibility plumbing (add once per file that gets desktop/mobile-split coupons: E2, E3, E4, E5)

The originals split desktop/mobile at **480px** — same breakpoint the rebuilds' existing
`@media only screen and (max-width:480px){…}` uses. Add inside that existing block:

```css
  /* append inside the file's existing @media only screen and (max-width:480px){ … } block */
  .wsc-desk{display:none !important;}
  div.wsc-mob{display:block !important;}
```

(No base-CSS rule needed: desktop blocks are plain markup; mobile blocks carry inline `display:none`.)

Mechanism mirrors the original MJML output: mobile blocks carry inline `display:none` + `mso-hide:all` and are
wrapped in `<!--[if !mso]><!--> … <!--<![endif]-->` (Outlook never sees them); desktop blocks are plain
(Outlook, a desktop client, shows them). Never put background/padding for a hidden block on the `<tr>`/`<td>` —
keep it on the inner div/table cell so the row collapses to 0 height when hidden.

### 2.1 E1 — no coupon work

Original has a desktop/mobile pair ("Your Brain Boost is Here! Use code" zone, between kit packshot and TRY NOW):
desktop 26px bold `Antartica…` stack on the pale gradient; mobile-only twin 17px bold `Helvetica, Arial`.
The approved rebuild covers both with one element (`p.code`, 26px → 17px via media query) — sanctioned in
`e1-module-map.md` row 5, part of the approved render. **Carry through unchanged.**
Crops: `e1-600-00-coupon.png`, `e1-375-00-coupon.png`.

### 2.2 E2 — three insertions (crops: `e2-600-00`, `e2-375-00`, `e2-600-01`, `e2-375-band`)

> ⚠ **SUPERSEDED 2026-06-12** — do NOT reproduce the asymmetry described below; send-prep-spec §2 forbids a mode ending at "WITH CODE:" with nothing beneath, and forbids bare codes. See the top-of-file banner.

The E2 original's coupon layout is asymmetric — reproduce it as-is:
desktop shows the code twice (top yellow strip + black promo band); mobile shows it once, mid-body;
**on mobile the black band ends at "WITH CODE:" with no code** (render-verified, `e2-375-band.png`). Quirk of
the original; locked call says match it.

**(a) Desktop-only yellow code row** — insert between module 1 (yellow promo strip
`Save an extra 10% with code`, td `bgcolor="#EEEF78"`) and module 2 (marbled hero). Original: full-width row,
bg `#EEEF7A`, td padding `9px 18px`, centered, 26px, no bold, ink `#222427`, Antartica→Lucida stack. Visually it
extends the yellow strip so strip+code read as one banner. (Original row bg is `#EEEF7A`; the approved strip
above is `#EEEF78` — 2/255 apart, imperceptible; keep the original's value for the inserted row.)

```html
<!-- C-a · desktop code row under yellow strip (wsc-send-spec §2.2a — matches original exactly) -->
<tr><td style="padding:0;">
  <div class="wsc-desk">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="width:100%;border-collapse:collapse;"><tbody><tr>
      <td bgcolor="#EEEF7A" style="background-color:#EEEF7A;padding:9px 18px;font-family:'Helvetica Neue',Arial;font-size:26px;font-weight:400;line-height:1.3;color:#222427;text-align:center;">
        <span style="font-family: Antartica, Lucida, 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Geneva, Verdana, sans-serif;">{% coupon_code 'Welcome_Discount' %}</span>
      </td>
    </tr></tbody></table>
  </div>
</td></tr>
```

**(b) Mobile-only mid-body code** — insert between module 3 (intro copy "Millions rely on stimulants…") and
module 4 (explainer, whose first row is the 1px divider rule). Original: white bg (none set), td padding
`9px 18px`, centered, **18px bold**, ink, Antartica→Lucida stack.

```html
<!-- C-b · mobile-only code between intro copy and explainer (wsc-send-spec §2.2b) -->
<tr><td style="padding:0;">
  <!--[if !mso]><!-->
  <div class="wsc-mob" style="display:none;mso-hide:all;padding:9px 18px;font-family:'Helvetica Neue',Arial;font-size:18px;line-height:1.3;color:#222427;text-align:center;">
    <strong><span style="font-family: Antartica, Lucida, 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Geneva, Verdana, sans-serif;">{% coupon_code 'Welcome_Discount' %}</span></strong>
  </div>
  <!--<![endif]-->
</td></tr>
```

**(c) Desktop-only code in the black promo band** — module 8 (`$50 OFF SUBSCRIPTIONS` pill +
"EXTRA 10% OFF+FREE SHIPPING WITH CODE:"). Append inside the band's black td, after the WITH CODE: `<p>`.
Original: black bg, white 26px, **no bold**, Antartica→Lucida stack, 9px above the code.

```html
  <!-- C-c · desktop code inside black band (wsc-send-spec §2.2c) -->
  <p class="wsc-desk" style="margin:9px 0 0 0;font-family:'Helvetica Neue',Arial;font-size:26px;font-weight:400;line-height:1.3;color:#FFFFFF;text-align:center;"><span style="font-family: Antartica, Lucida, 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Geneva, Verdana, sans-serif;">{% coupon_code 'Welcome_Discount' %}</span></p>
```

No mobile twin for (c) — the original has none.

### 2.3 E3 — two insertions (crops: `e3-600-00`, `e3-375-00`)

**(a) Desktop-only yellow code row** — insert between module 1 (BLACK promo band: yellow `$50 OFF SUBSCRIPTIONS`
pill + white "Plus, Get EXTRA 10% OFF + FREE shipping with code:") and module 2 (wordmark). Render-verified:
the code row is a **yellow `#EEEF7A` strip directly under the black band** (black band → yellow code strip →
white wordmark zone). Markup: identical to E2 block (a), byte for byte.

**(b) Mobile-only code** — insert between module 5 (jars render img) and module 6 ("While stimulants are highly
effective… they come with:"). White bg, td padding 9px 18px, 18px bold, Antartica→Lucida stack — markup identical
to E2 block (b), byte for byte.

(That's the complete set: E3's original has only 2 coupon tags; its black band gets its code from the yellow
strip beneath it on desktop, and on mobile only the mid-body code shows.)

### 2.4 E4 — three insertions (crops: `e4-600-00`, `e4-375-00`)

**(a) Mobile-only code before the band** — insert between module 4 (TAKE STASIS CTA) and module 5 (black promo
band). White bg, td padding 9px 18px, 18px bold Antartica→Lucida — markup identical to E2 block (b).

**(b) Desktop code inside the black band** — module 5 band td (`$50 OFF SUBSCRIPTIONS` pill + white
"EXTRA 10% OFF + FREE shipping with code:"). Append after the sub-line div. Original: white **26px BOLD**,
**`Helvetica, Arial`** stack (E4/E5 band code is Helvetica, unlike E2's Antartica stack — keep per-email), black
bg, original td padding `0 18px 15px 18px` (code tight under the band art, 15px below).

**(c) Mobile code inside the black band** — directly after (b), same band td. Original: white **17px, NOT bold**,
`Helvetica, Arial`, same paddings. (In the original these two live either side of a Klaviyo section seam —
visually one continuous black band; render-verified that adjacency reproduces it.)

```html
  <!-- C-b/C-c · band code pair (wsc-send-spec §2.4b/c — desktop 26 bold / mobile 17 regular, Helvetica) -->
  <p class="wsc-desk" style="margin:10px 0 0 0;font-family:'Helvetica Neue',Arial;font-size:26px;line-height:1.3;color:#FFFFFF;text-align:center;"><strong><span style="font-family: Helvetica, Arial, sans-serif;">{% coupon_code 'Welcome_Discount' %}</span></strong></p>
  <!--[if !mso]><!-->
  <div class="wsc-mob" style="display:none;mso-hide:all;margin:10px 0 0 0;font-family:'Helvetica Neue',Arial;font-size:17px;font-weight:400;line-height:1.3;color:#FFFFFF;text-align:center;"><span style="font-family: Helvetica, Arial, sans-serif;">{% coupon_code 'Welcome_Discount' %}</span></div>
  <!--<![endif]-->
```

(The 10px top margin approximates the original's sub-line→code gap inside the rebuild's band geometry — verify
against `e4-600-00-coupon.png` / `e4-375-00-coupon.png` per §3.)

### 2.5 E5 — one insertion + one reconciliation (crops: `e5-600-00`, `e5-375-00`)

**(a) Mobile-only code before the band** — insert between module 5 (SUBSCRIBE TO STASIS CTA, cream td) and
module 6 (black promo band). Original: **white** strip (the cream behind the CTA is baked art; the coupon row
itself sits on white — render-verified), td padding 9px 18px, 18px bold Antartica→Lucida — markup identical to
E2 block (b), but give the td/div an explicit white background (`background-color:#FFFFFF`) because the
rebuild's module 5 td is cream `#F4EFEB`.

**(b) ⚠ DELTA — the rebuild's existing in-band code does not match the original.** The approved E5 rebuild
already renders the code inside the module 6 band as one always-visible div: Antarctica webfont, 24px,
weight 600, white. The original band code is a desktop/mobile pair exactly like E4's: desktop **26px bold
`Helvetica, Arial`**, mobile **17px regular `Helvetica, Arial`**, white on black. Under the locked call
("variant B coupon line matches the original exactly") the send copy should **replace that one div** with the
E4 §2.4 b/c pair verbatim. This is a visual change to an approved-render element — it is confined strictly to
the coupon line and is mandated by the locked call, but because it intersects the approved-render contract,
**surface it to Bryce in the build report** rather than silently shipping. Variant A (the approved rebuild used
in the flow as-is) is untouched either way.

---

## 3 · Verification protocol (what "done" looks like)

1. Re-render each cc-send file at 600 and 375 via `scripts/check_modes.py` (unique `--profile` under /tmp).
2. Crop the same zones and compare against `wsc-send-crops/`:
   - every `eN-600-tail.png`: cream lockup → white footer, FDA italic line, unsubscribe line
     (E1 without, E2–E5 with manage_preferences), address, © line;
   - every coupon crop: placement, background, size/weight/color of the literal
     `{% coupon_code 'Welcome_Discount' %}` text per the tables above (the literal wraps to 2 lines at 375 —
     expected; it renders as a short code after Klaviyo substitution);
   - `e2-375-band.png`: E2's mobile band still ends at "WITH CODE:" with NO code (intentional).
3. Tag count check per send file: E1 unchanged; E2 = 3 coupon + full footer tag set; E3 = 2 coupon + footer set;
   E4 = 3 coupon + footer set; E5 = 3 coupon + footer set (1 pre-band + band pair) — all with manage_preferences
   except E1.
4. Nothing else moved: diff send copy vs approved rebuild must touch ONLY the inserted blocks, the visibility
   CSS, and (separately scoped) font/image source swaps.

## 4 · Open items surfaced (not blockers; decisions logged here)

- §1.3 footer styling: spec'd as approved-E1 treatment (recommended); byte-faithful original styling is the
  alternative if Bryce prefers — flag at review.
- §2.5b E5 in-band coupon restyle: mandated by the locked call, intersects the approved render — include in
  build report for Bryce's eyes.
- Preheader parity (E3/E4/E5 rebuilds have none; not an original tag, out of this contract) — separate call.
