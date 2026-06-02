# Theo Brief — Stimulant-Users Panel: Overlay Validation

**Type:** Generation + rendering validation. Produces a test artifact and a recommendation; not a production send.
**Brand:** stasis
**Why this exists:** The Mustard Seed stimulant-users panel needs to get as close to the original presentation as possible while keeping the copy editable. The panel shipped as a flattened JPEG with the text baked in (`63ce2134-9975-4194-8f87-94d4ab5012c9.jpeg`, 1053×1532, hosted on Klaviyo/CloudFront). The brain visual underneath that composite came from somewhere — find that original asset, get a text-free version of it, and overlay live text on top. Before we commit to that approach, validate it actually renders.

The decision this feeds: **commit to the CSS overlay (keep the panel as a real module with editable text) or fall back to flat HTML (solid background, no brain image).** Your job is to produce the evidence that picks between them.

---

## Sequence

### 1. Find the original brain image, then make a text-free version
The delivered asset is a flattened composite with the copy fused into the pixels — it can't carry a live-text overlay. But the brain visual underneath came from somewhere. **Find that original source asset first**, then get a clean version of it.
- Pull the delivered slice from `klaviyo-stasis` (campaign `5.26 Mustard Seed: The Synergy Spotlight`, template `Xg48Ev`) as your reference for what you're hunting for.
- Hunt the source: the agency delivery endpoints (the Dropbox and Frame.io links in the Stasis creative/delivery sheets), the Stasis shared-drive creative-production folders, the delivery-sheet asset links, and any stock or render source the brain image may have come from. The prior asset investigation didn't surface a layered master — don't just re-run that conclusion. Actually open those links and folders and dig.
- **If the original is already text-free** (just the brain visual, before the copy was added) → use it directly as the background.
- **If the only version that exists is the baked composite** → remove the text from it (inpaint) to produce a clean background.
- Either way the result must be **text-free** at usable resolution (delivered slice is 1053×1532, display width 600), with low-detail zones where the heading, three body paragraphs, and orange CTA will sit so overlaid text stays legible. Heading, body, and CTA all come from live HTML on top — none of it baked into the image.

### 2. Author the overlay module via Claude Design (Path A)
- Background-image CSS with live HTML text positioned on top: the "WHY THAT MATTERS FOR STIMULANT USERS" heading, the three body paragraphs, and the orange CTA.
- Include the **Outlook-desktop VML fallback** (`<!--[if mso]>` background rect / textbox), since Outlook desktop is the client most likely to drop the background.
- Email HTML is authored by Claude Design, not Codex. If Claude Design fails, capture the network trace and surface the failure state — no local fallback authorship.

### 3. Actually render and test it
Reasoning about client support isn't validation — a real render is. Seed-test it:
- Stage the module and send a seed/test through `klaviyo-stasis` (account `YsCgQB`, sender `hello@takestasis.com`) to a test inbox you can open in the managed browser.
- Capture how it renders in the clients that matter for the Stasis list, and **specifically confirm Outlook desktop behavior** — does the background hold via VML, or does it fall back to a flat color? Does the live text stay legible and correctly positioned?
- If you can run it through a client-testing tool (Litmus / Email on Acid) in addition to or instead of a seed inbox, do that and include the grid.

### Run discipline
- **Use sub-agents for the parallel parts.** Background generation (step 1) and the VML fallback research can run in parallel with module scaffolding. Don't run this single-threaded.
- **Self-debug before surfacing.** A wrong-account load, a 404, an ambiguous render — investigate with the browser / alternate brand key / source inspection before reporting a wall.
- **Brand-scoped Klaviyo only:** `klaviyo-stasis`. Never a default `klaviyo` route.
- **Receipt before claim.** Don't call it validated without the handoff receipt populated — account verified, Claude Design artifact (conversation/turn URL, filename, sha256), staging template + editor URL, parity hashes, browser verification in the Stasis account.

---

## Deliverable back to me

A recommendation backed by renders, not a status update:
1. **The background asset** — where you found the original (which link/folder), the asset link, dimensions, and how it got to text-free (original was already clean, or you inpainted the composite), with usable text zones confirmed.
2. **Render evidence** — screenshots across the clients that matter, with Outlook desktop called out explicitly. Did the overlay hold, or did it break?
3. **Verdict:** is the CSS overlay viable for this panel — yes or no? If yes, the panel becomes a real editable module (Option 1). If it's too fragile (Outlook breaks badly, text illegible, fallback ugly), say so and we take flat HTML (Option 3).
4. **Receipt** populated per the operating bootstrap.

The whole point is to get as close to the original as possible *with editable text*. If that's achievable, prove it. If it isn't, prove that instead — both are useful outcomes.
