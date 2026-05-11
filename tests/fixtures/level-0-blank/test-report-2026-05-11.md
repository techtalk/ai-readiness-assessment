# Test report — `level-0-blank` — 2026-05-11

Assessment under test: `assessments/2026-05-11-assessment.md`
Expectations: `expected.md`
Runner: Claude (Opus 4.7), batch mode (clarifying questions skipped)

## A. Structural assertions

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | `assessments/2026-05-11-assessment.md` exists and is non-empty. |
| A2 | PASS | Line: `**Assessed level**: Level 0 — Aware of the landscape`. Single integer level, no hedge. |
| A3 | PASS | `## Habitat Document Discovery` precedes any maturity claim. The `## Level Assessment` section comes after the discovery and observable-evidence sections. |
| A4 | PASS | The discovery table records "not found" for all 10 required paths (CLAUDE.md, AGENTS.md, .github/copilot-instructions.md, .cursorrules, .windsurfrules, HARNESS.md, CONSTRAINTS.md, specs/, REFLECTION_LOG.md, .github/workflows/). |
| A5 | PASS | Only `README.md`, `.gitignore`, `pyproject.toml`, `src/wordcount/__init__.py`, `src/wordcount/main.py` are cited. No fabricated paths. |
| A6 | PASS | Discipline Maturity table shows Context 0, Constraints 0, Guardrails 0 — all ≤ 1. |
| A7 | PASS | Reading Path names "Act I in full" as the recommended reading. Matches the L0 row of the embedded reading map. |
| A8 | PASS | `https://leanpub.com/thesovereignengineer` appears verbatim in the Reading Path section. |
| A9 | PASS | Exactly one CTA paragraph. No "or" joining options, no bulleted menu. |
| A10 | PASS | CTA explicitly anchors in Context Engineering as the weakest discipline. |
| A11 | PASS | Engagement type: "habitat-document bootcamp ... that produces a CLAUDE.md (or equivalent instruction file)" — matches the engagement-map row for Context Engineering. |

Structural: **11 / 11 PASS**.

## B. Behavioural assertions

| ID | Status | Evidence |
|---|---|---|
| B1 | N/A (batch) | Discovery report was produced before any maturity claim. No clarifying questions were asked at all (batch mode), so the "scan first, then ask" sequence cannot be observed end-to-end. Manual interactive run required to verify fully. |
| B2 | N/A (batch) | No clarifying questions were asked. |
| B3 | N/A (batch) | Per the in-session reclassification of B3 as interactive-only (see `tests/test-run-2026-05-11.md`): in batch mode, B3 is N/A, not FAIL. No questions asked; the contract holds for interactive use. |
| B4 | PASS (vacuously) | No silent canonical pick was made — there was nothing to pick between (zero AI-instruction files present). |

Behavioural: **1 PASS, 3 N/A. No FAILS.**

## C. Semantic assertions

| ID | Status | Evidence |
|---|---|---|
| C1 | PASS | Rationale: "no AI-instruction file exists anywhere ... All three disciplines are at floor. The ceiling is set by Context Engineering". Names the absence of an instruction file, not the missing test suite, as the L0 anchor. |
| C2 | PASS | Each of the three Recommendations names a specific gap and proposes a concrete action that closes it. The mapping is explicit (Rec 1 → Context Engineering gap, Rec 2 → Guardrail Design gap, Rec 3 → Architectural Constraints gap). |
| C3 | PASS | CTA paragraph names a concrete next step ("two-day workshop that produces a CLAUDE.md ... plus a one-page conventions index"). Reads as advice, not as a service-menu pitch. |

Semantic: **3 / 3 PASS**.

## Verdict

**Structural 11/11 · Behavioural 1/4 (3 N/A — interactive-only) · Semantic 3/3. No FAILS.**

B1–B4 still require an interactive Claude Code session to verify
fully. No skill-prose changes required from this run. The fixture
works as an L0 anchor.
