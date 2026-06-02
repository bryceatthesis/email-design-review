# Theo — Handoff Tag for Approved Designs

Two things, one quick confirmation and one small standing change to how you hand off approved emails.

## 1. Confirmation I need from you

Does your build loop currently write or commit the approved email HTML anywhere — a git repo, a synced folder, anything on disk — or do you only stage in Claude Design + Klaviyo? I believe it's the latter (Claude Design artifact + Klaviyo template, no repo), but confirm so I'm not missing a source location. If you *do* write HTML somewhere, tell me where.

## 2. The change: tag every approved handoff

Approved designs now get pulled into a review app where we line variants up side by side and step through a flow. To file your output correctly, each approved handoff needs three labels attached. Nothing about how you build changes — this is just metadata on delivery.

With each approved email, give me:

- **Flow** — the lifecycle flow or campaign it belongs to. e.g. `welcome`, `winback`, `mustard-seed`. (A one-off campaign is its own flow.)
- **Variant** — which version of that flow this is, so we know what it's being compared against. e.g. `current` (the live version), `future-state`, `original`, `v8`, or `a` / `b` for an A/B pair. Include a human label and the state: `live`, `draft`, `approved`, or `retired`.
- **Step** — its position in the flow's send order, 1-based. `1` = first email. A single-email campaign is step `1`.

Plus a display **name** for the step (e.g. "Welcome", "Education", "Offer").

### Example tag

```
flow:    welcome           (Welcome Flow)
variant: future-state      label "Future State", status draft
step:    2                 name "Education"
```

## What stays exactly the same

Keep delivering what you already do — they're the source of record and the app links straight out to them:

- The **approved HTML export** (the file itself).
- Your full **handoff receipt** — the `=== HANDOFF RECEIPT ===` block, unchanged. The Claude Design `artifact_url`, the Klaviyo `editor_url`, and `artifact_sha256` are the fields that get carried into the catalog, so keep populating them.
- Both **links** every time (Claude Design + Klaviyo).

One note on the hash: the app verifies the HTML it files against your receipt's `artifact_sha256`, so make sure that hash is taken on the same form of the file you hand over. If they ever diverge for a benign reason, flag it in the receipt rather than leaving it silent.

That's it — same build, same receipt, just the flow/variant/step tag on top.
