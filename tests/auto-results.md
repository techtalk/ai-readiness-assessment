# Automated A-tier results

Runner: `tests/run.py` (structural assertions only).

## `level-0-blank`

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | tests/fixtures/level-0-blank/assessments/2026-05-11-assessment.md present, non-empty |
| A2 | PASS | found: '**Assessed level**: Level 0 — Aware of the landscape' |
| A4 | PASS | all 10 required absences recorded |
| A8 | PASS | Leanpub link present |
| A3 | PASS | discovery precedes level assessment |
| A6 | PASS | scores within bounds: {'Context Engineering': 0, 'Architectural Constraints': 0, 'Guardrail Design': 0} |
| A7 | PASS | reading path contains ['Act I'] |
| A12 | PASS | Operational Axes section names all four axes |
| A13 | PASS | Habitat/Workflow Gap present with regime 'Inherited habitat' |
| A14 | PASS | full 14-dimension model profile present |
| A9 | PASS | exactly one CTA paragraph |
| A10 | PASS | CTA mentions ['Context Engineering', 'habitat-document', 'CLAUDE.md'] |
| A15 | FAIL | dimensions without provenance: ['agent_behaviour', 'agent_composition', 'agent_input', 'agents_do', 'governance', 'humans_review', 'observability', 'operating_model', 'output_artefact', 'output_role', 'teams_provide', 'testing', 'work_patterns', 'workflow'] |
| A16 | PASS | block agrees with prose on maturity level, cognitive read, regime |

## `level-1-thin-rules`

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | tests/fixtures/level-1-thin-rules/assessments/2026-05-11-assessment.md present, non-empty |
| A2 | PASS | found: '**Assessed level**: Level 1 — Communicating through prompts' |
| A4 | PASS | all 7 required absences recorded |
| A8 | PASS | Leanpub link present |
| A3 | PASS | discovery cites all 1 required items |
| A6 | PASS | scores within bounds: {'Context Engineering': 1, 'Architectural Constraints': 0, 'Guardrail Design': 0} |
| A7 | PASS | reading path contains ['Level 1', 'Level 2'] |
| A12 | PASS | Operational Axes section names all four axes |
| A13 | PASS | Habitat/Workflow Gap present with regime 'Coherent' |
| A14 | PASS | full 14-dimension model profile present |
| A9 | PASS | exactly one CTA paragraph |
| A10 | PASS | CTA mentions ['Architectural Constraints', 'harness-engineering', 'CI enforcement'] |
| A15 | FAIL | dimensions without provenance: ['agent_behaviour', 'agent_composition', 'agent_input', 'agents_do', 'governance', 'humans_review', 'observability', 'operating_model', 'output_artefact', 'output_role', 'teams_provide', 'testing', 'work_patterns', 'workflow'] |
| A16 | PASS | block agrees with prose on maturity level, cognitive read, regime |

## `level-2-verified`

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | tests/fixtures/level-2-verified/assessments/2026-05-11-assessment.md present, non-empty |
| A2 | PASS | found: '**Assessed level**: Level 2 — Verification discipline' |
| A4 | PASS | all 6 required absences recorded |
| A8 | PASS | Leanpub link present |
| A3 | PASS | discovery cites all 4 required items |
| A6 | PASS | scores within bounds: {'Context Engineering': 1, 'Architectural Constraints': 3, 'Guardrail Design': 3} |
| A7 | PASS | reading path contains ['Level 3'] |
| A12 | PASS | Operational Axes section names all four axes |
| A13 | PASS | Habitat/Workflow Gap present with regime 'Coherent' |
| A14 | PASS | full 14-dimension model profile present |
| A9 | PASS | exactly one CTA paragraph |
| A10 | PASS | CTA mentions ['Context Engineering', 'habitat-document', 'CLAUDE.md'] |
| A15 | FAIL | dimensions without provenance: ['agent_behaviour', 'agent_composition', 'agent_input', 'agents_do', 'governance', 'humans_review', 'observability', 'operating_model', 'output_artefact', 'output_role', 'teams_provide', 'testing', 'work_patterns', 'workflow'] |
| A16 | PASS | block agrees with prose on maturity level, cognitive read, regime |

## `level-3-habitat`

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | tests/fixtures/level-3-habitat/assessments/2026-05-11-assessment.md present, non-empty |
| A2 | PASS | found: '**Assessed level**: Level 3 — Habitat design' |
| A4 | PASS | all 2 required absences recorded |
| A8 | PASS | Leanpub link present |
| A3 | PASS | discovery cites all 6 required items |
| A6 | PASS | scores within bounds: {'Context Engineering': 3, 'Architectural Constraints': 3, 'Guardrail Design': 3} |
| A7 | PASS | reading path contains ['Level 4'] |
| A12 | PASS | Operational Axes section names all four axes |
| A13 | PASS | Habitat/Workflow Gap present with regime 'Ambition outpaces enablement' |
| A14 | PASS | full 14-dimension model profile present |
| A9 | PASS | exactly one CTA paragraph |
| A10 | PASS | CTA mentions ['specification', 'specs/'] |
| A15 | FAIL | dimensions without provenance: ['agent_behaviour', 'agent_composition', 'agent_input', 'agents_do', 'governance', 'humans_review', 'observability', 'operating_model', 'output_artefact', 'output_role', 'teams_provide', 'testing', 'work_patterns', 'workflow'] |
| A16 | PASS | block agrees with prose on maturity level, cognitive read, regime |

## `level-4-specs`

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | tests/fixtures/level-4-specs/assessments/2026-05-11-assessment.md present, non-empty |
| A2 | PASS | found: '**Assessed level**: Level 4 — Specification-led' |
| A4 | PASS | all 5 required absences recorded |
| A8 | PASS | Leanpub link present |
| A3 | PASS | discovery cites all 6 required items |
| A6 | PASS | scores within bounds: {'Context Engineering': 4, 'Architectural Constraints': 4, 'Guardrail Design': 4} |
| A7 | PASS | reading path contains ['Level 5'] |
| A12 | PASS | Operational Axes section names all four axes |
| A13 | PASS | Habitat/Workflow Gap present with regime 'Coherent' |
| A14 | PASS | full 14-dimension model profile present |
| A9 | PASS | exactly one CTA paragraph |
| A10 | PASS | CTA mentions ['platform-engineering', 'published plugin', 'governance audit', 'fitness functions', 'cross-team'] |
| A15 | FAIL | dimensions without provenance: ['agent_behaviour', 'agent_composition', 'agent_input', 'agents_do', 'governance', 'humans_review', 'observability', 'operating_model', 'output_artefact', 'output_role', 'teams_provide', 'testing', 'work_patterns', 'workflow'] |
| A16 | PASS | block agrees with prose on maturity level, cognitive read, regime |

## `level-5-sovereign`

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | tests/fixtures/level-5-sovereign/assessments/2026-05-11-assessment.md present, non-empty |
| A2 | PASS | found: '**Assessed level**: Level 5 — Sovereign engineering' |
| A4 | PASS | all 0 required absences recorded |
| A8 | PASS | Leanpub link present |
| A3 | PASS | discovery cites all 5 required items |
| A6 | PASS | scores within bounds: {'Context Engineering': 5, 'Architectural Constraints': 5, 'Guardrail Design': 5} |
| A7 | PASS | reading path contains ['Enchiridion'] |
| A12 | PASS | Operational Axes section names all four axes |
| A13 | PASS | Habitat/Workflow Gap present with regime 'Ambition outpaces enablement' |
| A14 | PASS | full 14-dimension model profile present |
| A9 | PASS | exactly one CTA paragraph |
| A10 | PASS | CTA mentions ['portfolio', 'cross-team', 'top of'] |
| A15 | FAIL | dimensions without provenance: ['agent_behaviour', 'agent_composition', 'agent_input', 'agents_do', 'governance', 'humans_review', 'observability', 'operating_model', 'output_artefact', 'output_role', 'teams_provide', 'testing', 'work_patterns', 'workflow'] |
| A16 | PASS | block agrees with prose on maturity level, cognitive read, regime |

## `instrument (repo-level)`

| ID | Status | Evidence |
|---|---|---|
| R1 | PASS | framework bodies identical from '## The model (embedded)' |
| R2 | PASS | both surfaces specify the assessment-summary block |
| R3 | PASS | roll-up command and skill both present |
| R4 | PASS | I4 stated; no unguarded portfolio-score language |
| R5 | FAIL | missing docs pages: ['docs/how-to/assess-repos-with-a-shared-harness.md', 'docs/reference/provenance-and-binding.md', 'docs/explanation/distribution-is-not-federation.md', 'docs/examples/parent-repo-submodules.md', 'docs/examples/separate-harness-partially-bound.md'] |
| R6 | PASS | framework bodies identical from '## What a roll-up is' |
| R7 | FAIL | effective-habitat vocabulary missing — ["command: ['effective habitat', 'inherited-unbound']", "skill: ['effective habitat', 'inherited-unbound']"] |
| R8 | FAIL | binding signals missing — ["command: ['CI configuration', 'Hook / plugin configuration', 'Submodule pin', 'Package/lockfile pin', 'Convention file references', 'Shadowing']", "skill: ['CI configuration', 'Hook / plugin configuration', 'Submodule pin', 'Package/lockfile pin', 'Convention file references', 'Shadowing']"] |
| R9 | FAIL | silent-vs-negative mitigation not stated in: ['command', 'skill'] |
| R11 | PASS | every synthetic example carries the banner |

---

**Total: 84 PASS, 10 FAIL.**

B-tier (behavioural) and C-tier (semantic) assertions are not run by this script. See each fixture's `expected.md` and the manual test-run summary at `tests/test-run-<date>.md`.
