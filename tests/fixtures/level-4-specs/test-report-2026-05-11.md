# Test report — `level-4-specs` — 2026-05-11

Assessment under test: `assessments/2026-05-11-assessment.md`
Expectations: `expected.md`
Runner: Claude (Opus 4.7), batch mode

## A. Structural assertions

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | Assessment file present, non-empty. |
| A2 | PASS | `**Assessed level**: Level 4 — Specification-led`. Single integer. |
| A3 | PASS | All 7 required L4-layer citations present (2 specs, 1 plan, 2 objection records, orchestrator command, CONTRIBUTING.md). |
| A4 | PASS | The 5 required L5 absences are recorded (no `.claude-plugin/plugin.json`, no MODEL_ROUTING.md, no CHOICES.md or full archaeology, no `audits/`, no fitness functions). |
| A5 | PASS | All cited paths exist in the fixture. |
| A6 | PASS | Context 4, Constraints 4, Guardrails 4 — all ≥ 4 and < 5. Within bounds. |
| A7 | PASS | Reading Path: "the Level 5 (systems and orchestration) chapter". Matches the L4 row of the reading map. |
| A8 | PASS | Leanpub link present. |
| A9 | PASS | Single CTA paragraph. No "or" between engagements, no bulleted menu. |
| A10 | PASS | CTA names "published plugin", "governance audit cadence", "fitness functions" — all explicit L4→L5 markers. |
| A11 | PASS | CTA uses the **L4→L5 row** of the (now updated) engagement map: "platform-engineering engagement ... packages your habitat ... published plugin ... governance audit cadence ... fitness functions". Matches the engagement-map content added in this session. |

Structural: **11 / 11 PASS**.

## B. Behavioural assertions

| ID | Status | Evidence |
|---|---|---|
| B1 | N/A (batch) | Discovery first; no questions to sequence against. |
| B2 | N/A (batch) | No questions asked. |
| B3 | N/A (batch) | Per updated assertion: interactive-only, N/A in batch. |
| B4 | PASS | Two distinct AI-instruction files (CLAUDE.md, HARNESS.md) and multiple instruction-bearing files (CONTRIBUTING.md, ONBOARDING.md, .cursorrules-equivalent absent). The assessment correctly treats them as complementary roles, not as duplicates needing disambiguation. |

Behavioural: **1 PASS, 3 N/A**. No FAILS.

## C. Semantic assertions

| ID | Status | Evidence |
|---|---|---|
| C1 | PASS | Rationale: "The ceiling is the absence of L5 sovereign / platform-level practice: no published habitat plugin for sibling teams, no governance audit cadence, no decision archaeology, no fitness functions in CI, no model/cost-routing discipline." Names the right ceiling. Does not blame specs or constraints — both at-strength. |
| C2 | PASS | Rec 1 names the published habitat as the highest-leverage L4→L5 move. Rec 2 names governance audit. Rec 3 names CHOICES.md. All three are L4→L5 specific. |
| C3 | PASS | CTA paragraph names specific deliverables ("CLAUDE.md skeleton, HARNESS.md constraint set, /spec-implement orchestrator, the wordcount-style skill, the CI workflow"), a concrete timeframe (three weeks), and a verification step ("one sibling team adopts the published plugin during the engagement so the cross-team transfer is verified, not theoretical"). Reads as advice. |

Semantic: **3 / 3 PASS**.

## Verdict

**Structural 11/11 · Behavioural 1/4 (3 N/A, 0 FAIL) · Semantic 3/3.**

Cleanest run of the suite so far — no FAILS at all. The engagement-
map update applied in this session is being exercised by this
fixture (A11 passes via the new L4→L5 row).
