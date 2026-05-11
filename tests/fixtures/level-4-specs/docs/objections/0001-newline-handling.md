---
spec: specs/0001-newline-handling.md
created: 2026-03-05
---

# Objection record — Spec 0001 (newline handling)

Adversarial review of the spec before implementation. Each objection
has a disposition: `accepted`, `deferred`, or `refuted`, each with a
short reason.

## Objections raised

### O1. The spec doesn't cover CJK languages.

**Raised by**: agent (adversarial-review pass).

**Concern**: `count_words` on a Japanese string like "こんにちは世界"
will return 1, because there are no whitespace separators. The spec
silently endorses this.

**Disposition**: refuted.

**Reason**: The spec explicitly excludes locale-specific word
boundaries in the "Out of scope" section. The user is a writer of
English prose; the tool's job is to be predictable for the user's
input. CJK support is a different tool.

---

### O2. `re.split(r'\s+', ...)` vs. `str.split()`.

**Raised by**: human reviewer.

**Concern**: `text.split()` returns `[]` for `""`. The spec says
empty input should raise. Mixing the two specs is risky.

**Disposition**: accepted.

**Reason**: Real concern. The plan now requires Spec 0002 to land
first, so the empty-input case is handled at the function entry
before `.split()` runs.

---

### O3. Performance on very large inputs.

**Raised by**: agent.

**Concern**: `str.split()` allocates a list of all words. For very
large files, this is wasteful.

**Disposition**: deferred.

**Reason**: The library is intended for prose-sized inputs (essays,
chapters). If a use case for streaming arises, open a new spec.

---

All dispositions resolved. Proceed to implementation.
