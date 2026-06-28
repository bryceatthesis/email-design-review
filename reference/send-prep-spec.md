# Send-prep spec — approved build → sendable copy (brand-agnostic)

> Established 2026-06-12, generalized from the WS-C welcome-flow send pass
> (the internal per-flow send-spec, now partially superseded — see its banners).
> The approved review-tool build is the visual contract. Send-prep adds ONLY what sending
> legally and functionally requires, and proves nothing else changed.

## 0 · What send-prep is

The email Bryce approves in the review tool is not yet sendable: it has no legal footer,
no coupon/discount codes, and its assets may not be on production hosting. Send-prep is the
controlled transform from `designs/<flow>/<approved-variant>/` to
`designs/<flow>/<send-variant>/`. **The ONLY permitted changes:**

1. Legal footer appended (brand pack's footer component, verbatim Liquid).
2. Coupon/discount code zones per §2.
3. Font + image sources swapped to production hosting (brand pack's `asset-sources.md`).
4. Hidden plain-text preheader if the campaign calls for one.

Anything else that moves is a defect. Each send copy is a separate file, promoted as its
own variant (`--variant-label` names it plainly, e.g. "Klaviyo variant B — send-ready
(hosted assets)"), status `in-review` until Bryce clears it.

## 1 · Legal footer

Use the brand pack's footer component verbatim (Stasis: `brands/stasis/components/`,
derived from wsc-send-spec §1.3 — FDA line, unsubscribe line with `{% unsubscribe %}` /
`{% manage_preferences %}` / privacy link, address + © Liquid). Inserted as the new last
`<tr>` of the layout table. Flow-position nuances (e.g. E1's original has no
manage_preferences) follow the original being replaced; net-new emails take the full block.

## 2 · Coupon zones — BINDING (Bryce, 2026-06-12)

> Supersedes the WS-C "match each original exactly" call for coupon lines. Cause: the
> originals were incoherent on mobile (bare codes, context without codes, doubled codes),
> the send copies reproduced it faithfully, and Bryce rejected it on a real Gmail iOS read.

1. A coupon code (`{% coupon_code '…' %}` or literal) appears **only inside a coupon
   zone** — a block whose copy explains it ("…with code:", "Use code…").
2. The code sits **directly under its context line**.
3. Every zone shows context AND code in **both desktop (600) and mobile (375)** renders.
   No mode may show a context line ending "with code:" with nothing beneath.
4. The code renders **exactly once per zone per mode** (a `.wsc-desk`/`.wsc-mob`
   display-split pair counts as once).
5. **No standalone bare code lines anywhere.**
6. Multiple zones per email are fine (top banner + bottom band is the house pattern).
7. Styling: keep the zone's desktop treatment; mobile sizing per the brand pack's
   measured treatments (Stasis: black-band codes 17px regular Helvetica stack;
   yellow-strip codes 18px bold Antartica→Lucida stack — the misspelled `Antartica`
   first family in code spans is intentional fallthrough; do not "fix" it).

## 3 · Hosting + size budget

- Fonts and images come from the brand pack's pinned production hosts, every URL
  sha-verified against the canonical master (Stasis: Klaviyo image CDN for images,
  Shopify Files CDN for woff2 — tables in `brands/stasis/asset-sources.md`).
- **No data: URIs** (Gmail strips them). **Gmail clip budget: total HTML < 95 KB**
  (clipping starts ~102 KB; 95 leaves headroom for Klaviyo's save-time normalization,
  which grows the stored copy 10–25%).
- Never reference the *original send's* slice CDN URLs. Self-uploaded assets on the same
  CDN (sha round-trip verified) are the sanctioned path — the ban is on derivative
  slices, not the host.

## 4 · Verification protocol (what "done" means)

1. `scripts/check_modes.py <file> --width 375 --width 600` PASS (reflow + light-only pin
   + overflow offenders + 375/600/dark-sim screenshots). Unique `--profile` per parallel run.
2. Render at 600 and 375 and pixel-compare against the approved build: the diff must be
   confined to the inserted footer/coupon/preheader regions and asset-source swaps
   (hosted assets must render pixel-identical — that is the point of sha-pinning).
3. Coupon-zone audit per §2: map every code occurrence to a zone, check both modes.
4. Liquid inventory: every tag the platform needs (unsubscribe, preferences, address,
   year, org name, coupon) present byte-exact; nothing else added.
5. Diff confinement: `git diff` vs the approved file touches only the permitted changes.
6. **Lesson written in blood (E5 dot grid):** verification of any *injected/stored* copy
   must cover the FULL document — head/tail or length checks miss mid-document
   corruption. See `klaviyo-stage` skill for the stored-copy protocol.

## 5 · Multi-brand

Everything brand-specific above resolves through the brand pack (`brands/<brand>/`):
design-language spec, components (incl. footer), asset-sources (hosting tables, font
URLs+shas, CDN account), coupon mobile treatments. This file never hardcodes a brand.
