# AI Readiness Assessment — orders-api

**Fixture report — invented numbers, committed as test data.** Produced
for `tests/fixtures/scope-two-subjects/`; not a reading of any real
repository.

**Assessed level**: Level 3 — Habitat design
**Habitat/Workflow Gap**: +0.14 — Coherent
**Date**: 2026-08-17

## Habitat Maturity Profile (Agentic Experience 5-Level Model)

| Dimension | Level | Confidence |
|---|---|---|
| Agent behaviour | 3 | observed |
| Agent input | 3 | observed |
| Workflow | 3 | observed |
| Operating model | 3 | asked |
| Teams provide | 3 | observed |
| Output role | 3 | asked |
| Output artefact | 3 | observed |
| Humans review | 3 | asked |
| Work patterns | 3 | inferred |
| Agent composition | 2 | observed |
| Agents… | 3 | inferred |
| Testing | 3 | observed |
| Observability | 2 | observed |
| Governance | 3 | observed |

**Habitat Maturity Level**: L3 (14-dimension mean 2.86)

## Habitat/Workflow Gap

```text
Habitat Maturity Level (model):  L3  (14-dim mean L2.86)
Cognitive read (Parts A–C):      L3
Habitat/Workflow Gap:            +0.14   (cognitive − 14-dim mean)
Interpretation:                  Coherent
```

The team's thinking and the habitat it works in are at the same level.
The two weak cells — agent composition and observability — are the
ceiling, and they are local rather than shared.

## Ceiling

Agent composition and observability. Neither blocks the other twelve
dimensions; both cap what a further habitat investment can return.

```yaml assessment-summary
schema: 1
subject: orders-api
subject_path: ./orders-api
team: payments-tribe
habitat: self
posture: active
assessed_at: 2026-08-17
tool_version: 1.0.0

dimensions:
  agent_behaviour:   { level: 3, confidence: observed, provenance: local }
  agent_input:       { level: 3, confidence: observed, provenance: local }
  workflow:          { level: 3, confidence: observed, provenance: local }
  operating_model:   { level: 3, confidence: asked,    provenance: local }
  teams_provide:     { level: 3, confidence: observed, provenance: local }
  output_role:       { level: 3, confidence: asked,    provenance: local }
  output_artefact:   { level: 3, confidence: observed, provenance: local }
  humans_review:     { level: 3, confidence: asked,    provenance: local }
  work_patterns:     { level: 3, confidence: inferred, provenance: local }
  agent_composition: { level: 2, confidence: observed, provenance: local }
  agents_do:         { level: 3, confidence: inferred, provenance: local }
  testing:           { level: 3, confidence: observed, provenance: local }
  observability:     { level: 2, confidence: observed, provenance: local }
  governance:        { level: 3, confidence: observed, provenance: local }

habitat_maturity_mean: 2.86
habitat_maturity_level: 3
cognitive_level: 3
cognitive_source: subject
gap: +0.14
regime: coherent
ceiling_dimensions: [agent_composition, observability]
weakest_discipline: guardrail-design
```
