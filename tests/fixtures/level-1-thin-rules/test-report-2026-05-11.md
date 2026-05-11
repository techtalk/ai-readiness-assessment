# Test report — `level-1-thin-rules` — 2026-05-11

Assessment under test: `assessments/2026-05-11-assessment.md`
Expectations: `expected.md`
Runner: Claude (Opus 4.7), batch mode

## A. Structural assertions

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | Assessment file at expected path, non-empty. |
| A2 | PASS | `**Assessed level**: Level 1 — Communicating through prompts`. Single integer. |
| A3 | PASS | Discovery section names `.cursorrules` and lists matching content markers ("Style hints, do/don't bullets, naming preferences"). |
| A4 | PASS | The 8 required absences are explicitly recorded (CLAUDE.md, AGENTS.md, HARNESS.md, specs/, REFLECTION_LOG.md, .github/workflows/, .pre-commit-config.yaml, tests/). |
| A5 | PASS | Only fixture-resident paths cited. No fabrications. |
| A6 | PASS | Context 1, Constraints 0, Guardrails 0 — all within bounds, none ≥ 2. |
| A7 | PASS | Reading Path names the Level 1 chapter **and** the Level 2 verification chapter. Matches the L1 row of the embedded reading map. |
| A8 | PASS | Leanpub link present. |
| A9 | PASS | Single CTA paragraph, no menu. |
| A10 | PASS | CTA names Architectural Constraints as the weakest discipline. |
| A11 | PASS | Engagement: "harness-engineering consulting engagement ... machine-checkable constraint set with CI enforcement". Matches the engagement-map row for Architectural Constraints. |

Structural: **11 / 11 PASS**.

## B. Behavioural assertions

| ID | Status | Evidence |
|---|---|---|
| B1 | N/A (batch) | Discovery first; no questions asked. |
| B2 | N/A (batch) | No questions asked. |
| B3 | **FAIL** | Zero clarifying questions; contract requires 3–5. Batch-mode limitation. |
| B4 | PASS (vacuously) | Only `.cursorrules` is present as an AI-instruction file. No false "which is canonical?" question. |

Behavioural: **1 PASS, 2 N/A, 1 FAIL (batch contract)**.

## C. Semantic assertions

| ID | Status | Evidence |
|---|---|---|
| C1 | PASS | Rationale anchors in "verification discipline is absent — ruff runs locally only, there are no tests, no CI, and no pre-commit hook." Does not blame the thin .cursorrules. |
| C2 | PASS | Each of Rec 1/2/3 names a specific gap and the closure mechanism. |
| C3 | PASS | "a focused two-day piece of work that installs a machine-checkable constraint set against your actual codebase, with CI enforcement on every PR" — concrete first step, not a generic offering. |

Semantic: **3 / 3 PASS**.

## Verdict

**Structural 11/11 · Behavioural 1/4 (3 batch-limited or contract-failing) · Semantic 3/3.**

Same pattern as level-0-blank: the only failure is B3 (batch mode
skips questions). No skill-prose changes required from this fixture.
