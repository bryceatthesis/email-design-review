# Stasis — standing email elements

Always-on elements that go on **every marketing send** (campaign + flow email), regardless of topic.
This is a **registry, not a one-off**: `email-build` applies every entry here on every build, and
`email-send-prep` preserves them. Each brand has its own `brands/<brand>/standing-elements.md` — never
carry one brand's elements into another.

## The rule
- Apply **every** element below, at its stated position, to every marketing email.
- **Skip on transactional** messages (order / shipping / backorder / waitlist confirmations) — marketing only.
- **Mind the line.** Each element carries a **Scope** — some are line-specific (Stasis core
  vs the Stasis Kids parent-audience line). Apply an element only on the line(s) its Scope
  names; don't carry a core-audience element onto a Kids send (or vice-versa).
- Prefer the **linked universal / saved block** (edit-once → updates everywhere). For HTML-coded emails
  that can't take a drag-drop block, paste the element's self-contained source HTML (path below) at the
  stated position.
- Standing elements are part of the approved-render contract — they **survive send-prep + staging unchanged**.

## Registry

### 1 · Self-ID nano-bar  *(added 2026-06-22)*
- **What:** the one-line "Quick question: How new are you to ADHD?" strip (three one-click answers).
- **Position:** the **first element**, top of the email, above the logo/header.
- **Klaviyo saved/universal block:** `Stasis · Self-ID nano-bar` (`template-universal-content` id
  `343a3987f2994eeea24a46fbcfef1d6c`) — drag it to the top in the editor.
- **Source-of-truth HTML:** `brands/stasis/components/nano-bar-self-id.html` (paste this for HTML-coded emails).
- **Auto-hide (baked in):** `{% if not person.diagnosis_stage %}…{% endif %}` — disappears for anyone who's
  already answered, so there's nothing to configure per send.
- **Mechanism (don't re-touch):** links → `takestasis.com/?self_id=suspecting|newly|veteran` → click-trigger
  segments → 3 live flows set the `diagnosis_stage` property → audience segments
  `Self-ID · {Suspecting | Newly diagnosed | Veteran}`. Target the **audience** segments for stage content;
  never the `flow trigger` segments. Full design in memory: `stasis-self-id-nano-bar`.
- **Scope:** Stasis **core line only.** The question ("How new are you to ADHD?") speaks to
  the adult/self audience; it does **not** fit **Stasis Kids** (parents of children) — skip
  the nano-bar on Kids sends.

## Adding a new standing element
Append a numbered entry with the same fields (what / position / block name+id / source HTML / any
auto-hide or mechanism / scope). Once it's listed here, `email-build` picks it up automatically — **no
skill edits needed.** That's the design: new always-on elements slot into this registry, not into the skills.
