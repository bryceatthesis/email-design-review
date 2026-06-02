# Mustard Seed Close-Out Plan

**Brand:** stasis
**Status:** Option 1 (editable CSS/VML overlay) adopted as the module *approach* (2026-05-28) — NOT signed off as shippable. Technical + provenance gates are met; there has been **no creative review or revision pass** on the assembled `UaDFin` module. Bryce has seen the inpainted background and render fragments, not a consolidated shippable version, and has given no design feedback. The module is "close, not final." The real remaining work before close-out is a feedback → revision round on the module — this is the gate, ahead of (and separate from) the non-blocking Outlook confirmation.

Closed: **Claude Design provenance** — Path A module authored in Claude Design and staged as Klaviyo template `UaDFin` (the earlier `RCTYMi` was a local technical draft, now superseded). Receipt has conversation URL, artifact URL, verbatim prompt, filename, SHA; `stored_sha == rendered_sha`; VML markers + heading/body/`SHOP STASIS DAY` preserved. Only empty receipt field is `turn_url` — Claude Design didn't expose a stable per-turn URL; documented limitation, not a redo. **Seed-send + account ambiguity** — browser was silently in Thesis despite `company_id=YsCgQB`; switched to ST Stasis, sent a real preview seed that landed in Gmail from `hello@takestasis.com` with VML/background intact.

Full-email draft staged as `VvjLKt` (2026-05-28) — usable as a **visual review draft** (renders attached; openable in Claude Design via the project_file_url), NOT a shippable artifact yet. Two production gates open:

(1) **Path A not proven (procedural, fixable).** Theo's trace for `VvjLKt` has GetProject/ListFiles/GetFile/UpdateProjectData but NOT `WriteFiles → RecordAsset → ReleaseTurn` — because the script resumed after submit and fetched the already-generated file rather than capturing the authoring turn. `UaDFin` *does* have the trace, so the mechanism works; fix = clean re-run capturing the live generative trace before staging. Bootstrap Rule 2 re-keyed (2026-05-28) so Path A proof = the generative trace, not the conversation/turn URLs Claude Design won't expose.

(2) **Not built to the editable-module standard — rebuild required.** Bryce reviewed in Claude Design: only the stimulant-users brain panel is live text. The header/top and hero sections (and other content panels) were pulled straight from Klaviyo as **flattened image slices with baked-in copy** — they fail the highlight test (text not selectable in preview). The whole point of the system is editable live-text modules, so this is unacceptable. Corrected target (in `theo-current-brief.md`): rebuild every text-bearing section as live HTML text (header/top, hero/defense, job panel, closer, CTA as a bulletproof button, FDA/legal as live text), using the text-free-background + overlay technique where a section needs imagery. Only genuine graphics — logo/wordmark and social icons — stay as images, and those still need a real source or approved reuse per Rule 4. So the earlier "reuse approval" question only ever applied to the logo + icons, not the content slices.

**2026-05-29 redelivery — rebuild NOT done.** Theo re-delivered the same `VvjLKt` (identical `artifact_sha256 96de7204…`), describing the old "assemble with overlay swapped in" task rather than the live-text rebuild. His own `departures_from_source` confirms hero/defense, job, closer, and CTA remain retained image slices — only the brain panel is live text. Fails the highlight test; does not meet `theo-current-brief.md`. **Provenance concern:** receipt now lists `write_files: success` / `record_asset: success` against the same hash Theo previously said lacked `WriteFiles → RecordAsset → ReleaseTurn`, with `release_turn` still unexposed — same-artifact/upgraded-status, which trips the bootstrap's "same hash, one process" rule. Kicked back: work from the current brief, and reconcile the provenance rather than relabeling.

**2026-05-29 11:00 — live-text rebuild done (content), provenance failed, not staged.** Theo rebuilt to the editable-module standard as a new Claude Design artifact (`826c9d16…`, file "2026-05-29 Stasis Mustard Seed Live Text Rebuild.html"). **Content gate PASSED:** 6 `<img>` refs total (logo + 5 social icons), no baked hero/job/brain/closer/CTA/FDA slices, live-text markers across hero/job/overlay/closer/CTA/legal/footer, VML overlay markers present. **Provenance gate FAILED:** only `GetFile` captured, no `WriteFiles → RecordAsset → ReleaseTurn`; Theo correctly refused to stage. Likely root cause = the `run-path-a-live-text.js` capture script erroring (trailing tool-failure trace). Theo also **retracted the `VvjLKt`/`96de7204` provenance as invalid** (only GetFile was ever supported) — confirms the same-hash concern. **Net: content is reviewable in Claude Design and meets the brief; the sole remaining blocker is capturing the Path A authoring trace for the full email — a tooling/capture fix on Theo's side, not a content or design question.** If the script fix doesn't take, escalate full-email trace capture as a dedicated tooling problem rather than retrying one-off.

**2026-05-29 11:22 — BOTH GATES PASS. Staged as `UQdTQi`.** Root cause of the capture failures was a static Claude Design filename: reusing it made Claude short-circuit ("already satisfies") so no fresh authoring write fired. Theo forced a unique filename per run, kept capture live through the turn, and captured the full `WriteFiles → RecordAsset → ReleaseTurn` chain for artifact `826c9d16…` (same hash as the prior unstaged rebuild — expected, since the same prompt regenerates identical HTML; validity comes from the captured chain + new template, not the hash). Content gate still clean (6 imgs = logo + social icons, live text across all sections, VML overlay intact). `VvjLKt`/`96de7204…` remains invalid and unused. **Status: awaiting Bryce's creative review of `UQdTQi` — his entry point. Notes → list to Claude → revision brief → Theo re-run.** Outlook-desktop confirmation still the only separate open item, non-blocking.

Open (reframed from gate to confirmation): **Windows Outlook desktop render.** Theo has no Litmus/EoA access in-session. Decision (Bryce delegated): proceed with Option 1 now — the VML fallback is the correct Outlook mechanism and survived Klaviyo + Gmail; worst-case Outlook degradation ≈ the flat fallback we'd have accepted; nothing rides on a live send (this is the reusable module, reversible). Outlook proof routed to Theo as parallel confirmation: (a) Litmus/EoA — ruled out, no internal account surfaced; (b) manual Windows Outlook desktop screenshot of the seed in `theo@takethesis.com` — Theo has requested one from the team. Right-sizing step suggested: pull the Stasis email-client open breakdown from Klaviyo — if Windows Outlook desktop is a negligible share of opens, the screenshot is moot and this closes on data. `UaDFin` stays staged regardless.
**Role of this doc:** Mustard Seed isn't just a send to finish — it's the first real test of the asset pipeline. Closing it out cleanly proves the loop can pick up source imagery, make the overlay call, and produce a receipt-clean artifact. Closing it out by guessing proves nothing.

---

## The one unresolved design question: the stimulant-users panel

In the source send (2026-05-26), the stimulant-users panel is a **text-on-image overlay**: blue brain image as background, with "WHY THAT MATTERS FOR STIMULANT USERS," three body paragraphs, and the orange CTA layered on top.

The current modular build treats `modules/03_stimulant_user_support.html` as a **flat HTML block** — solid blue background, HTML text, no brain image. That is a real visual departure from the source, and no one explicitly decided to accept it. It happened by default because flat HTML was the easy path. Close-out has to confront this, not inherit it silently.

### The three honest options

1. **Background-image CSS, HTML text on top.** Renders in Gmail, Apple Mail, Outlook web, and mobile. Outlook desktop is the wild card and usually needs a VML fallback. Most aligned with the modular architecture (text stays editable), but adds rendering complexity and a fallback to maintain.
2. **Pre-composited image baked at design time.** The whole panel is one flattened image. Renders identically everywhere. Defeats the modular architecture — text is no longer editable, no longer accessible as text, and every copy change means a new render.
3. **Accept the flat-HTML treatment as an intentional departure.** Cheapest. No brain image. Visually weaker than the source, but fully editable and bulletproof across clients.

### What the investigation settled (2026-05-28)

The brain panel is a **flattened Klaviyo-hosted JPEG with the text baked in** — `63ce2134-9975-4194-8f87-94d4ab5012c9.jpeg`, 1053×1532, displayed at 600px, hosted at `company/YsCgQB/images/...` on CloudFront. **No layered or text-free source master exists** anywhere Theo could find (Drive, sheets, Figma, agency endpoints). There is no clean DAM; Drive + the delivery sheets are the controlled environment, and Klaviyo is downstream-only. So the original "clean background asset exists" branch is off the table — that asset was never stored.

That leaves three real paths:

- **Option 2 — ship the existing flattened JPEG as-is.** It's exactly what went out May 26, renders identically everywhere, zero new work. Cost: the panel's copy is locked inside the image — not editable, not live text, not accessible to screen readers. Right call if this panel's copy is stable and we just need Mustard Seed closed.
- **Option 1 — recreate a clean text-free brain background, then do the CSS overlay.** This is now an *asset-creation* task (the master doesn't exist), plus the Outlook-desktop VML fallback. Keeps the module editable and accessible going forward. Right call only if we expect to reuse/restyle this panel and want it in the modular system properly.
- **Option 3 — flat HTML, drop the brain image.** Cheapest to maintain, fully editable, weakest visual fidelity to the source.

Note: the current modular build (`modules/03_stimulant_user_support.html`) is already Option 3 by default — solid blue, HTML text, no brain image. So "do nothing" silently ships Option 3, which is the path nobody actually chose.

### Who decides

This is a **Stasis brand call** — how much visual departure from the source is acceptable, and whether the Outlook-desktop fallback work is worth it. It is not Theo's call and not mine. The asset findings narrow it to one or two real options; the brand owner picks. Frame it for them with the findings attached, don't pre-decide it.

---

## Close-out sequence

1. ~~**Asset investigation lands** (Theo brief).~~ ✅ Done 2026-05-28. Brain image is a flattened Klaviyo JPEG, text baked in, no source master. Full findings in Theo's investigation doc.
2. **Overlay decision made** by the brand owner, using the three paths above + the findings. Record which option and why. ← *current gate*
3. **Module 03 rebuilt** to match the decision:
   - Option 1 → background-image CSS module + Outlook VML fallback, image sourced from the confirmed location.
   - Option 2 → single pre-composited image module.
   - Option 3 → keep flat HTML, but log it as a deliberate accepted departure, not an accident.
4. **Generation through the correct path.** The email HTML is authored via Claude Design (Path A), not Codex. If Claude Design fails, capture the network trace and surface the failure state — no Codex fallback authorship.
5. **Receipt populated and posted** before anyone calls it done. Required, not optional:
   - `account_verified` against the accounts endpoint (`klaviyo-stasis`, account `YsCgQB`).
   - `claude_design` block: conversation URL, turn URL, verbatim prompt, artifact filename + URL + sha256.
   - `klaviyo_staging` block if staged: template id, editor URL, pasted + rendered body hashes.
   - `parity`: artifact sha == pasted body sha, pasted == rendered (or normalized), with notes.
   - `browser_verification`: the editor URL loaded and resolved in the **Stasis** account.
   - No `n/a` / "verified locally" / "didn't mint a URL" passed off as a value — those are blocks.

---

## Pipeline rule this surfaced (carry-forward)

The investigation exposed a structural gap worth fixing before the next send, not just for Mustard Seed: **there was no requirement that imagery have a real upstream source.** That's how a panel got built from a flattened, copy-locked Klaviyo slice with no editable master, and nobody noticed until we went looking.

Theo's recommended rule, which I'd fold into the operating bootstrap pending your sign-off:

- Add a required field to the email brief/handoff: **`Source asset folder / editable source link`**.
- If that field is empty, the loop **stops before design generation** rather than silently pulling flattened slices out of Klaviyo.
- Treat Klaviyo/CloudFront image URLs as downstream rendered output — usable only as **reference**, or as production source only when explicitly approved for reuse.
- Source of truth for pickup: the Stasis shared Drive + the delivery sheets as the link index; the Brand Bible for messaging/claims, not raw assets.

Folded into `theo-bootstrap.md` (2026-05-28) as operating **Rule 4 — Source-asset discipline**, plus a `source_assets` block in the handoff receipt. Also added: **Rule 2 now requires leading every handoff with the `claude_design` provenance block** so Path A is verifiable at a glance without opening the staged template.

## What "done" means here

Mustard Seed is closed out when: the overlay departure has been resolved by an explicit decision (not inherited), module 03 reflects that decision, the artifact came through Claude Design, and the receipt is complete with matching hashes and a browser verification in the Stasis account. Anything short of that is a partial, and partials get surfaced as failure states — not relabeled as done.
