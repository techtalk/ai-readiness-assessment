# Harness — wordcount

## Context

### Stack

- Languages: Python 3.10+
- Build: pyproject / pip
- Test: pytest + pytest-cov
- Lint/format: ruff

### Conventions

See `CLAUDE.md`.

---

## Constraints

### Consistent formatting

- Rule: All Python files pass `ruff format --check .`
- Enforcement: deterministic
- Tool: ruff
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

- Rule: No bare `except:` clauses
- Enforcement: deterministic
- Tool: ruff (E722)
- Scope: pr

### Spec-first ordering

- Rule: Every PR that touches `src/` must either (a) reference a spec
  file under `specs/` in its PR body, or (b) introduce a new spec
  file in the same PR. Bug-fix PRs labelled `bug` or `fix/` are
  exempt.
- Enforcement: deterministic
- Tool: `scripts/check-spec-first.sh` (runs in CI)
- Scope: pr

### Spec conformance

- Rule: Every code change covered by a spec must reference the spec
  in its PR body and pass the test(s) the spec demands.
- Enforcement: agent
- Tool: human / agent review at PR time
- Scope: pr

### Objections resolved

- Rule: Every non-exempt PR has an objection record under
  `docs/objections/<spec-slug>.md` with all dispositions resolved
  (no `pending` values).
- Enforcement: agent
- Tool: human / agent review at PR time
- Scope: pr

---

## Garbage Collection

### Reflection log review

- What it checks: Whether `REFLECTION_LOG.md` has entries whose
  pattern recurs and should be promoted
- Frequency: monthly
- Enforcement: agent

### CLAUDE.md staleness

- What it checks: Whether CLAUDE.md references files or functions
  that no longer exist
- Frequency: monthly
- Enforcement: agent

### Spec freshness

- What it checks: Whether any spec file has been modified more
  recently than its corresponding objection record (a spec edited
  without re-running adversarial review).
- Frequency: weekly
- Enforcement: deterministic
- Tool: file mtime comparison

---

## Status

Last audit: 2026-04-15
Constraints enforced: 6/7
Garbage collection active: 1/3
Drift detected: spec 0001 mtime newer than its objection record
