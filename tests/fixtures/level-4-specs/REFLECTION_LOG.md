# Reflection log

---

## 2026-02-10 — `os.path.join` slipped through review

(Earlier entry — kept for continuity. Lesson promoted to HARNESS.md
as the "No os.path usage" constraint.)

---

## 2026-04-22 — spec-first caught an ambiguous requirement before code

**Surprise**: While drafting `specs/0002-empty-input.md` we realised
we hadn't decided whether empty input should return 0 or raise. The
spec process forced the question; the code hadn't been written yet,
so we got to choose deliberately rather than discover the choice via
a bug report later.

**Why**: Specs separate the "what and why" from the "how". Without
that separation, the question stays implicit and gets resolved by
whoever writes the code first.

**Lesson**: Spec-first is not bureaucracy; it surfaces ambiguity
early. Worth keeping.

**Action**: None — the workflow caught the gap, and we documented the
decision in the spec.

---

## 2026-05-03 — orchestrator command paid for itself on its first run

**Surprise**: `/spec-implement specs/0001-newline-handling.md`
produced an implementation plan that flagged a corner case (Windows
line endings vs. Unix) the spec hadn't called out. We added the
clarification to the spec before writing any code.

**Why**: Drafting the plan forces the agent to enumerate cases. The
human sees the enumeration and notices the gap.

**Lesson**: The plan step is doing real work — not just paperwork.

**Action**: None. The workflow worked.
