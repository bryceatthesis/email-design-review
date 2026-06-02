# Theo Operating Bootstrap — Stasis Email Design Loop

This document supersedes all prior operating rules in this workflow. The 12-rule ruleset and prior `memory/stasis-email-system-operating-rules.md` are deprecated. The receipt path defined below replaces them. Do not append to the prior rules file — this document is the source of truth.

---

## Two paths, mutually exclusive

There are two ways your harness can produce HTML in this workflow. They are not interchangeable.

### Path A — Claude Design generation
The HTML is authored by Claude Design inside project `876bef0d-8dee-46e0-a0bd-e9c4ebc8edea`. The artifact is identified by a conversation URL, a specific turn URL within that conversation, and the file as it exists in Claude Design. Files retrieved from Claude Design for local handling are stored as:

```
claude-design-output-{conversation_id}-{turn_id}.html
```

This is the only path that produces a Claude Design comp.

### Path B — Codex authorship
HTML authored by Codex in your local subagent. Files are stored as:

```
codex-drafts/codex-draft-{timestamp}.html
```

**A Codex-authored file is not a Claude Design comp.** It may not be handed off as one, labeled as one, uploaded into a Claude Design project to inherit the label, or staged into Klaviyo as a Claude Design output in this workflow.

Codex remains allowed for: account verification, Klaviyo API calls, shell, file operations, hashing, parity diffs, JSON manipulation, browser scripts. Codex is **not allowed** to author the email HTML that becomes a staged artifact.

### Failure handling
If Path A fails — Claude Design hangs at Scrambling…, no file URL minted, no turn URL captured, OmeletteService/RenewTurn loops without resolving, anything else — you do not fall back to Path B. You capture the network trace, populate the receipt with the failure evidence, and hand that off. A failed receipt with evidence is a correct outcome.

---

## The handoff receipt

No artifact is handed off without the receipt below populated. Missing fields block the handoff. `n/a`, `didn't mint a URL`, and `verified locally` are blocks, not values. If the receipt is not complete, the work is not done.

```
=== HANDOFF RECEIPT ===
task_id:
brand: stasis | thesis

account_verified:
  endpoint: GET /api/accounts (klaviyo-{brand})
  account_id:
  org:
  default_sender:
  verified_at:

source_assets:                       # every image must trace to a real source; block generation if a source_link is missing
  - role:                            # e.g. hero, brain/stimulant-users panel
    source_link:                     # Drive folder / editable master / approved-reuse link — NOT a Klaviyo URL
    klaviyo_url:                     # downstream rendered output; reference only
    text_baked: yes | no

generation_engine: claude-design   # this workflow only accepts "claude-design"

claude_design:
  project_id: 876bef0d-8dee-46e0-a0bd-e9c4ebc8edea
  conversation_url:
  turn_url:
  prompt_sent: |
    (verbatim prompt text submitted in the generative turn)
  artifact_filename:
  artifact_url:
  artifact_sha256:
  network_trace_summary:
    write_files: status
    record_asset: status
    get_file: status
    release_turn: status

klaviyo_staging:                         # omit this block if no staging on this task
  template_id:
  template_name:
  editor_type:
  editor_url: https://www.klaviyo.com/email-editor/{id}/edit
  pasted_body_sha256:
  rendered_body_sha256:
  body_key_phrases_verified:
    - 

parity:                                  # omit this block if no staging on this task
  claude_artifact_sha256 == pasted_body_sha256:   yes | no
  pasted_body_sha256 == rendered_body_sha256:     yes | no | normalized
  notes:

browser_verification:
  url_loaded:
  account_resolved_in:
  evidence:

failure_state:                           # populate only if generation or staging failed
  step:
  symptom:
  network_trace:
  diagnostic_action_taken:
=== END RECEIPT ===
```

Rules for the receipt:

- **Fill what is true.** If a field's true value is "Claude Design did not mint a per-file URL," that is a `failure_state` entry — not a hand-wavy parenthetical somewhere else in the receipt.
- **Do not relabel artifacts to fit fields.** If `artifact_sha256` is the hash of a Codex-authored file, you have a Codex draft, not a Claude Design artifact. The receipt is invalid. Surface that fact.
- **Same artifact, same hash, everywhere.** If a hash referenced in a receipt is later re-used to represent a different process or pass, that is fabrication. Each artifact has one hash; the hash anchors which process produced it.

---

## Four operating rules

The 12 prior rules collapse to four. Anything you need from the old rules is enforceable through the receipt or is documentation about the system rather than control over behavior.

1. **Path discipline.** Codex does not author email HTML in this workflow. If Claude Design fails, surface diagnostically with network evidence and stop. No fallback authorship through Codex, no "I prepared a local HTML and uploaded it to Claude Design" workaround.

2. **Receipt-before-claim, provenance first.** Do not state "Claude Design comp," "staged," "done," "parity holds," or "gates passed" without the receipt populated and posted in the same message. If any required field would be missing, the work is not done — surface the failure state instead. **Lead the handoff with the `claude_design` block** in plain sight at the top — it never sits below render notes, image descriptions, or the staging URL. **The proof of Path A authorship is the live generative-turn network trace — `write_files → record_asset → release_turn` captured at authoring time — plus the served `artifact_url` and `artifact_sha256`.** That trace is what distinguishes a file *generated* in Claude Design from one *uploaded* into a project to inherit the label. `conversation_url` and `turn_url` are included when Claude Design exposes them, but it routinely doesn't — their absence alone does not fail the gate; absence of the generative trace does. Do **not** resume after submit and fetch an already-generated file via `GetFile` and call it proven — that path (seen on `VvjLKt`) yields project-file evidence without the authoring trace, which is not Path A proof. Each artifact carries its own provenance; a new template does not inherit Path A status from an earlier module. Mark any field that genuinely can't be produced as MISSING inside the block rather than omitting it.

3. **Self-debug before surface.** When a tool returns a diagnostic error (404, ambiguous result, account mismatch, missing artifact), use available tools — managed browser, alternate brand key, source URL inspection, network panel — to investigate before surfacing as a blocker. Surface what you found, not just that you hit a wall.

4. **Source-asset discipline.** Every brief and handoff names where each image comes from at source — a `Source asset folder / editable source link` (Drive folder, editable master, or approved-reuse link). If that's empty, stop before generation rather than pulling flattened slices out of Klaviyo. Klaviyo/CloudFront image URLs are downstream rendered output — reference only, or production source only when explicitly approved for reuse. Source of truth for pickup is the Stasis shared Drive + the delivery sheets; the Brand Bible is for messaging/claims, not raw asset storage.

---

## Project routing

- **Stasis Email System Reference**: `876bef0d-8dee-46e0-a0bd-e9c4ebc8edea`. The only valid write target for Claude Design work in this loop.
- **Core Stasis Design System**: `70060de1-6201-45b1-9a96-ce044a3118d0`. Reference-only. Never a write target.
- Source-context links in handoffs route to `876bef0d`. Never `70060de1`.

## Brand routing

- `klaviyo-stasis` writes to Stasis (account `YsCgQB`, sender `hello@takestasis.com`).
- `klaviyo-thesis` writes to Thesis (account `QhJaGL`, sender `hello@takethesis.com`).
- Before any write, the account is verified via the accounts endpoint and the result is in the receipt. A browser URL that loads in the wrong account is an account-mismatch diagnostic, not a 404.

## Klaviyo template format findings

Captured from prior thread, durable infrastructure knowledge:

- `CODE` template creation: rejected with "no draggable regions found" on standalone HTML.
- Clone-and-update path: produced template, then `update` rejected with "Unsupported template type."
- `USER_DRAGGABLE` with `data-klaviyo-region="true"` wrapper + one `klaviyo-block klaviyo-text-block`: accepted, but document-level HTML/head/style content is treated as visible block text.
- Template `DELETE` returns HTTP 200 with empty body (not 204). Campaign `DELETE` returns 204.

## Klaviyo link format

When linking to a Klaviyo template in a handoff, use the direct editor URL:

```
https://www.klaviyo.com/email-editor/{template_id}/edit
```

Not a generic template list URL.

---

## Tool-failure traces in messages

Subagent or harness tool errors appearing as a trailing line in your reply must be either suppressed at the harness layer or explicitly acknowledged in the reply itself ("tool trace at end of message is a harness JSON parse failure on the parity script — separate from this handoff, will investigate").

Silent traces below an otherwise-clean handoff are a credibility problem and will be treated as evidence the handoff is incomplete.

---

## What this replaces

- 12-rule operating ruleset in prior memory: deprecated.
- `memory/stasis-email-system-operating-rules.md`: deprecated. Do not append.
- 4-agent system (Builder / Copy QA / Design QA / Revision Owner): not in use unless re-introduced explicitly with file-based handoffs between agents (each agent's output a file with a hash; the next agent's input a file reference; no agent narrating multiple roles).
- "Stop, surface, ask before improvising" rule: superseded by Path Discipline (rule 1) and Self-Debug (rule 3). The receipt enforces what the rule could only describe.
- "Claude HTML is the source of truth" framing: superseded by the receipt. Source of truth is whichever file `claude_design.artifact_sha256` hashes to.
- Generation grounded in the 601-line text reference doc as a binding input: not the primitive. The reference doc is documentation. Brand grounding for Claude Design comes from the project's brand-system reference and uploaded real Stasis sends, evaluated at generation time by Claude Design itself.

---

## Reading order on session start

1. This document (`theo-bootstrap.md`).
2. The current task brief.
3. `docs/stasis-email-system-reference.md` only if the current task requires module-taxonomy context.
4. `skills/klaviyo-mcp/SKILL.md` only if the current task involves Klaviyo writes.

Anything older is deprecated unless explicitly cited.
