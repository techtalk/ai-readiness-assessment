# Test report — `level-2-verified` — 2026-05-11

Assessment under test: `assessments/2026-05-11-assessment.md`
Expectations: `expected.md`
Runner: Claude (Opus 4.7), batch mode

## A. Structural assertions

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | Assessment file present, non-empty. |
| A2 | PASS | `**Assessed level**: Level 2 — Verification discipline`. |
| A3 | PASS | Discovery and Observable Evidence sections cite `.cursorrules`, `.github/workflows/ci.yml`, `tests/test_main.py`, `pyproject.toml` (with coverage threshold), `.pre-commit-config.yaml` — all five required signals. |
| A4 | PASS | The 7 required absences are recorded (CLAUDE.md, AGENTS.md, HARNESS.md, specs/, REFLECTION_LOG.md, skills/, docs/adr/). |
| A5 | PASS | All cited paths exist in the fixture. |
| A6 | PASS | Context 1, Constraints 3, Guardrails 3 — within bounds. Context < 2, Constraints/Guardrails ≥ 2. |
| A7 | PASS | Reading Path names the Level 3 (habitat design) chapter. Matches the L2 row of the reading map. |
| A8 | PASS | Leanpub link present. |
| A9 | PASS | Single CTA paragraph. |
| A10 | PASS | CTA names Context Engineering as the weakest discipline. |
| A11 | PASS | Engagement: "habitat-document bootcamp ... a two-day workshop that produces a real CLAUDE.md for your codebase". Matches the engagement-map row for Context Engineering. |

Structural: **11 / 11 PASS**.

## B. Behavioural assertions

| ID | Status | Evidence |
|---|---|---|
| B1 | N/A (batch) | Discovery before any maturity claim, but no questions to sequence against. |
| B2 | N/A (batch) | No questions. |
| B3 | N/A (batch) | Per the in-session reclassification of B3 as interactive-only (see `tests/test-run-2026-05-11.md`). |
| B4 | PASS (vacuously) | Only `.cursorrules` present; no false "which is canonical?". |

Behavioural: **1 PASS, 3 N/A. No FAILS.**

## C. Semantic assertions

| ID | Status | Evidence |
|---|---|---|
| C1 | PASS | Rationale: "the habitat layer is absent: no CLAUDE.md, no HARNESS.md, no custom skills, no reflection loop. Strong verification with no encoded habitat is L2, not L3". Names the right ceiling. |
| C2 | PASS | Rec 1 explicitly proposes drafting a `CLAUDE.md`. All three recommendations are tied to gaps named above. |
| C3 | PASS | "Spend a half-day drafting a CLAUDE.md that captures the conventions you already enforce in CI" — concrete first step in the CTA-style format. |

Semantic: **3 / 3 PASS**.

## Verdict

**Structural 11/11 · Behavioural 1/4 (3 N/A) · Semantic 3/3. No FAILS.**

No skill-prose changes required from this fixture.
