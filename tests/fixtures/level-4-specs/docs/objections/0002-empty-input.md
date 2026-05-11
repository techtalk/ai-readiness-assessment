---
spec: specs/0002-empty-input.md
created: 2026-04-22
---

# Objection record — Spec 0002 (empty input is an error)

## Objections raised

### O1. Backwards compatibility break.

**Raised by**: human reviewer.

**Concern**: If anyone is calling `count_words("")` in the wild and
expecting 0, this spec breaks them.

**Disposition**: accepted.

**Reason**: Valid concern, but the library is v0.x and there is no
public release yet. We will mention the change in the next release
notes when we hit 1.0.

---

### O2. Why a string match, not an exception class?

**Raised by**: agent.

**Concern**: The acceptance criteria say "ValueError with the message
'empty input'". This couples callers to the message text.

**Disposition**: deferred.

**Reason**: Custom exception classes are overkill for v0.x. Re-open
when we approach 1.0 and start defining the library's public surface
properly.

---

All dispositions resolved. Proceed to implementation.
