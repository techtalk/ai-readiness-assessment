# Reflection log

Append-only. Each entry is dated and short: what surprised us, what we
think it means, whether it should change `CLAUDE.md` or `HARNESS.md`.

---

## 2026-02-10 — `os.path.join` slipped through review

**Surprise**: A `os.path.join` call landed in `main.py` and stayed
through two PRs before someone noticed.

**Why**: The convention "use pathlib" was in `.cursorrules` but not in
the linter config. Cursor warned the author at edit time, but the
warning was dismissed and there was no second check.

**Lesson**: Conventions that depend on a human noticing rot. Need a
deterministic check.

**Action**: Added the "No os.path usage" constraint to `HARNESS.md` as
`unverified`. Looking for a way to promote to deterministic (custom
ruff rule? grep in CI?).

---

## 2026-03-05 — coverage threshold caught a real regression

**Surprise**: Test coverage dropped from 92% to 78% on a PR that
"just refactored" the CLI entry point. CI blocked the merge.

**Why**: The refactor moved logic out of `count_words` and into the
CLI block. The CLI block isn't covered by tests, so coverage fell.

**Lesson**: The 80% threshold isn't an arbitrary number — it's a
tripwire. Worth keeping.

**Action**: None. The threshold did its job.

---

## 2026-04-12 — agent wrote `Union[str, None]` instead of `str | None`

**Surprise**: The agent used old-syntax `Union[]` in a new function
even though `CLAUDE.md` and `.cursorrules` both say "no old-syntax
unions."

**Why**: The agent's training data has more `Union[]` than `|`. The
instruction in `CLAUDE.md` was prose; the agent treated it as advice,
not a rule.

**Lesson**: Conventions only stick when they're enforced. The ruff
`UP` rules already catch this — they just weren't being run in CI
yet at the time.

**Action**: Made sure CI runs `ruff check .` with `UP` in the
selected rule set. Closed the loop.
