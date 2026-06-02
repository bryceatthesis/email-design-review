# Theo Brief — Stasis Asset Source-of-Truth Investigation

**Type:** Investigation (no writes, no staging). Read/inspect only.
**Brand:** stasis
**Why this exists:** Before we define how the email loop picks up imagery, we have to know where Stasis brand assets actually live at source. Klaviyo is downstream — assets land there for delivery, but it is not the entry point. We are unwinding the Antidote agency relationship and bringing creative in-house, so the asset pipeline can no longer assume "whatever Antidote had." This investigation establishes the upstream source of truth so the design loop can connect to it.

This is an open investigation, not a confirm-what-I-already-know task. Treat every location below as a hypothesis to test, not an assumption to validate.

---

## What I need answered

### 1. Where do Stasis brand assets actually live at source?
Find the system(s) of record for finished brand imagery and the working files behind them. Candidates to test, not assume:
- Figma libraries (Stasis brand file / shared library)
- Adobe Creative Cloud (Libraries, or a shared CC account)
- Dropbox / Google Drive / Box shared folders
- A DAM (Bynder, Brandfolder, Frontify, or similar)
- A designer's or agency's local environment with no shared canonical store
- Klaviyo's image library (downstream — note what's here but do not treat it as source)
- Some combination of the above

For each location you confirm exists: what's in it, who has access, and whether it looks like a maintained source of truth or a stale dumping ground.

### 2. Who owns asset creation and approval today, and what's changing?
Working assumption to verify, not invent: **Antidote** (the agency) has owned Stasis email/campaign creative and asset production. That relationship is being wound down. Confirm:
- Which assets Antidote produced vs. which originated elsewhere.
- Whether Antidote's deliverables ever landed in a shared Stasis-owned store, or only in Antidote's environment + Klaviyo.
- What, if anything, exists as an in-house asset store independent of Antidote.

### 3. What is the existing asset-request workflow?
When a campaign needs new imagery today: is there a brief or request process, a typical turnaround, a versioning/naming convention, an approval gate? Document the actual workflow as it runs now, even if it's informal or agency-mediated. If there's no documented process, say so — that's a finding.

### 4. Locate the blue brain image from the May 26 Mustard Seed send.
The Stasis "Mustard Seed" send (2026-05-26) had a stimulant-users panel: blue background, brain image, text overlaid on top, orange CTA. Find that specific asset.
- Is it an existing, reusable asset in a source library, or was it composited once for that send and never stored anywhere permanent?
- If it exists at source: where, at what dimensions, layered or flattened, with or without the text baked in?
- Pull the version actually rendered in the May 26 Klaviyo send (via `klaviyo-stasis`) so we can compare the delivered image against any source asset you find.

This one is the concrete test case — answering it well exercises the whole pipeline question.

---

## How to run it

- **Self-debug before surfacing.** If a URL 404s, an account resolves wrong, or a library is ambiguous, use the managed browser, the `klaviyo-stasis` key, and source inspection to dig before reporting a wall. Surface what you found, not just that you hit one.
- **Use sub-agents for the parallel parts.** Items 1–3 are independent of item 4 and of each other. Spin up separate sub-agents: one to map asset locations (item 1), one to trace ownership + workflow (items 2–3), one to chase the brain image through Klaviyo and into any source store (item 4). Do not run this single-threaded.
- **Klaviyo is brand-scoped.** Use `klaviyo-stasis` (account `YsCgQB`, sender `hello@takestasis.com`). Never a default `klaviyo` route.
- **No writes.** This is inspection only — no template creation, no staging, no flow edits.

---

## Deliverable back to me

A findings doc, not a status update. Structure:
1. **Source of truth** — the system(s) where Stasis assets actually live, with confidence level and access notes. If there is no single source of truth, say that plainly and describe the fragmentation.
2. **Ownership + workflow** — who makes assets today, what the request process is, what changes as Antidote winds down.
3. **Brain image** — exactly where it lives (or that it doesn't), source vs. delivered comparison, dimensions/format/layering.
4. **Gaps** — what you couldn't determine and why, and what a human would need to confirm.
5. **Recommendation** — given what you found, where should the email loop pick up assets, and does asset pickup need a human in the loop or can it be automated?

Anything you assert as fact, show how you confirmed it (endpoint, URL, library, who you'd need to ask). Unknowns stay labeled as unknowns.
