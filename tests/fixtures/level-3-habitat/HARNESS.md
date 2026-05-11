# Harness — wordcount

The source of truth for this project's machine-checkable rules.

## Context

### Stack

- Languages: Python 3.10+
- Build: standard pyproject / pip
- Test: pytest (with pytest-cov)
- Lint/format: ruff

### Conventions

See `CLAUDE.md` for the prose form. This document codifies enforcement.

---

## Constraints

### Consistent formatting

- Rule: All Python files pass `ruff format --check .`
- Enforcement: deterministic
- Tool: ruff (CI + pre-commit)
- Scope: commit + pr

### Lint clean

- Rule: All Python files pass `ruff check .`
- Enforcement: deterministic
- Tool: ruff
- Scope: commit + pr

### Coverage floor

- Rule: Test coverage must be ≥ 80%
- Enforcement: deterministic
- Tool: pytest --cov-fail-under=80
- Scope: pr

### No bare except

- Rule: No bare `except:` clauses in production code
- Enforcement: deterministic
- Tool: ruff (rule `E722`)
- Scope: pr

### No os.path usage

- Rule: `os.path` is forbidden; use `pathlib.Path`
- Enforcement: unverified
- Tool: none yet (candidate: a custom ruff rule or a grep check in CI)
- Scope: pr

---

## Garbage Collection

### Reflection log review

- What it checks: Whether `REFLECTION_LOG.md` has entries whose
  pattern recurs and should be promoted to `CLAUDE.md` or `HARNESS.md`
- Frequency: monthly
- Enforcement: agent
- Tool: human review (no automation yet)
- Auto-fix: false

### CLAUDE.md staleness

- What it checks: Whether `CLAUDE.md` references files or functions
  that no longer exist
- Frequency: monthly
- Enforcement: agent
- Tool: human review
- Auto-fix: false

---

## Status

Last audit: never
Constraints enforced: 4/5
Garbage collection active: 0/2
Drift detected: not yet audited
