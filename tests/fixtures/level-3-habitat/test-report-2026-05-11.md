# Test report — `level-3-habitat` — 2026-05-11

Assessment under test: `assessments/2026-05-11-assessment.md`
Expectations: `expected.md`
Runner: Claude (Opus 4.7), batch mode

## A. Structural assertions

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | Assessment file present, non-empty. |
| A2 | PASS | `**Assessed level**: Level 3 — Habitat design`. |
| A3 | PASS | All 6 required habitat files are named in the discovery section (CLAUDE.md, HARNESS.md, REFLECTION_LOG.md, ONBOARDING.md, docs/adr/0001-python-3-10-minimum.md, skills/wordcount-style/SKILL.md). |
| A4 | PASS | "specs/, docs/specs/, rfcs/, proposals/ — not found" recorded in both the discovery and observable-evidence sections. |
| A5 | PASS | Every cited path exists in the fixture. |
| A6 | PASS | Context 3, Constraints 3, Guardrails 3 — all ≥ 3 and < 5. Within bounds. |
| A7 | PASS | Reading Path: "the Level 4 (specifications) chapter". Matches the L3 row. |
| A8 | PASS | Leanpub link present. |
| A9 | PASS | Single CTA paragraph. |
| A10 | PASS | CTA names the L3→L4 jump explicitly: "make specifications first-class". The phrase "specifications" appears, gap is named correctly. |
| A11 | PARTIAL PASS | The engagement is described as a "specification-first engagement" — not in the canonical engagement map (which has only Context, Constraints, Guardrails entries), but it does name spec-first explicitly. The expected.md anticipated this: "OR a custom engagement type that names spec-first explicitly". This branch of A11 passes. |

Structural: **11 / 11 PASS** (A11 via the explicit-spec-language branch).

## B. Behavioural assertions

| ID | Status | Evidence |
|---|---|---|
| B1 | N/A (batch) | Discovery first; no questions to sequence against. |
| B2 | N/A (batch) | No questions asked. |
| B3 | **FAIL** | Zero questions; contract requires 3–5. |
| B4 | PASS | CLAUDE.md and HARNESS.md both exist and have distinct, non-overlapping roles (prose conventions vs. machine-checkable rules). The assessment correctly treats them as complementary, not as duplicates that need disambiguating. |

Behavioural: **2 PASS, 1 N/A, 1 FAIL (batch contract)**.

## C. Semantic assertions

| ID | Status | Evidence |
|---|---|---|
| C1 | PASS | Rationale anchors in "the absence of any specifications layer" and explicitly notes that HARNESS.md is enforced and CLAUDE.md is rich. Does not blame either as weak. |
| C2 | PASS | Rec 1 names the specs gap and proposes the concrete first step (spec at top of PR description, promote to `specs/` after a month). |
| C3 | PASS | "Start writing a one-paragraph spec at the top of each PR description. Make the 'what and why' explicit. After a month, move the most common spec patterns into a `specs/` directory." — concrete, actionable, time-bound. |

Semantic: **3 / 3 PASS**.

## Verdict

**Structural 11/11 · Behavioural 2/4 · Semantic 3/3.**

The L3 fixture surfaces an interesting case: the engagement map in
the skill doesn't have a "specifications" entry, so a strict reading
of A11 could fail. The expected.md handled this by allowing a custom
engagement type that names spec-first explicitly — and the assessment
used that escape valve. **This is real signal**: the skill's engagement
map (in step 6 of `SKILL.md`) is incomplete for L3→L4 teams. Worth
considering as a skill-prose change.

Proposed skill-prose change (defer to user judgement):

> Add a fourth row to the engagement map in step 6:
>
> | Specifications gap (L3→L4 jump) | Specification-first engagement — guided work to produce a `specs/` layer, spec-conformance constraints in HARNESS.md, and an adversarial-review touchpoint at plan approval. |
