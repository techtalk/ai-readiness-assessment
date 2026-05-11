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

(Inherits the L4 set.)

### Consistent formatting / Lint clean / Coverage floor / No bare except

(Same as L4, deterministic, ruff + pytest.)

### Spec-first ordering

- Rule: PRs touching `src/` reference a spec
- Enforcement: deterministic
- Tool: `scripts/check-spec-first.sh`
- Scope: pr

### Spec conformance

- Rule: Code matches the spec it references
- Enforcement: agent
- Scope: pr

### Objections resolved

- Rule: All objection dispositions resolved before merge
- Enforcement: agent
- Scope: pr

### Choices captured

- Rule: Every load-bearing decision is captured as a story in
  `CHOICES.md` before the PR that implements it merges
- Enforcement: agent
- Scope: pr

### Model-routing compliance

- Rule: All AI tool invocations follow the per-task-type model
  selection in `MODEL_ROUTING.md`. Exceptions require a `CHOICES.md`
  entry.
- Enforcement: agent
- Scope: pr (advisory) + monthly audit

---

## Garbage Collection

### Reflection log review (monthly, agent)

### CLAUDE.md staleness (monthly, agent)

### Spec freshness (weekly, deterministic — file mtime)

### Layer boundary fitness function

- What it checks: No module under `src/wordcount/` imports from
  `src/wordcount/cli/` (CLI depends on library, never the reverse)
- Frequency: weekly
- Enforcement: deterministic
- Tool: `scripts/fitness/layer-boundary.sh`

### Complexity hotspots fitness function

- What it checks: Any module with cyclomatic complexity > 10 across
  the last 4 weekly snapshots
- Frequency: weekly
- Enforcement: agent (interprets the snapshot)
- Tool: `scripts/fitness/complexity.sh`

### Dependency age budget

- What it checks: Total libyear score across all dependencies
  remains ≤ 12 libyears
- Frequency: weekly
- Enforcement: deterministic
- Tool: `scripts/fitness/dependency-age.sh`

### Governance audit cadence

- What it checks: Whether the last governance audit in `audits/` is
  within the quarter
- Frequency: monthly
- Enforcement: deterministic
- Tool: file date check on `audits/*.md`

---

## Status

Last audit: 2026-04-15 (governance audit at audits/2026-Q1.md)
Constraints enforced: 8/9
Garbage collection active: 5/7
Drift detected: complexity in `src/wordcount/main.py` near threshold
