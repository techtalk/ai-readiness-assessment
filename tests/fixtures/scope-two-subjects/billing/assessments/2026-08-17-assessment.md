# AI Readiness Assessment — billing

**Fixture report — invented numbers, committed as test data.** Produced
for `tests/fixtures/scope-two-subjects/`; not a reading of any real
repository.

**Assessed level**: Level 2 — Verification discipline
**Habitat/Workflow Gap**: +1.21 — Ambition outpaces enablement
**Date**: 2026-08-17

The cognitive placement in this report was gathered against
`payments-tribe`'s general practice, in the same session as `orders-api`,
rather than against this subject specifically. It is recorded as
`cognitive_source: team` and is stated here rather than in a footnote,
because a reader has no other way to tell it from a read taken here.

## Habitat Maturity Profile (Agentic Experience 5-Level Model)

| Dimension | Level | Confidence |
|---|---|---|
| Agent behaviour | 2 | observed |
| Agent input | 2 | observed |
| Workflow | 2 | observed |
| Operating model | 2 | asked |
| Teams provide | 2 | observed |
| Output role | 2 | asked |
| Output artefact | 2 | observed |
| Humans review | 2 | asked |
| Work patterns | 2 | inferred |
| Agent composition | 1 | observed |
| Agents… | 2 | inferred |
| Testing | 1 | observed |
| Observability | 1 | observed |
| Governance | 2 | observed |

**Habitat Maturity Level**: L2 (14-dimension mean 1.79)

## Habitat/Workflow Gap

```text
Habitat Maturity Level (model):  L2  (14-dim mean L1.79)
Cognitive read (Parts A–C):      L3
Habitat/Workflow Gap:            +1.21   (cognitive − 14-dim mean)
Interpretation:                  Ambition outpaces enablement
```

The same team works two levels above what this habitat supports. The
gap is a statement about the environment here, not about the people —
which is the comparison the portfolio view exists to make visible.

## Ceiling

Testing, observability, and agent composition. All three sit at the L1
floor while the team reads L3.

```yaml assessment-summary
schema: 1
subject: billing
subject_path: ./billing
team: payments-tribe
habitat: self
posture: active
assessed_at: 2026-08-17
tool_version: 1.0.0

dimensions:
  agent_behaviour:   { level: 2, confidence: observed, provenance: local }
  agent_input:       { level: 2, confidence: observed, provenance: local }
  workflow:          { level: 2, confidence: observed, provenance: local }
  operating_model:   { level: 2, confidence: asked,    provenance: local }
  teams_provide:     { level: 2, confidence: observed, provenance: local }
  output_role:       { level: 2, confidence: asked,    provenance: local }
  output_artefact:   { level: 2, confidence: observed, provenance: local }
  humans_review:     { level: 2, confidence: asked,    provenance: local }
  work_patterns:     { level: 2, confidence: inferred, provenance: local }
  agent_composition: { level: 1, confidence: observed, provenance: local }
  agents_do:         { level: 2, confidence: inferred, provenance: local }
  testing:           { level: 1, confidence: observed, provenance: local }
  observability:     { level: 1, confidence: observed, provenance: local }
  governance:        { level: 2, confidence: observed, provenance: local }

habitat_maturity_mean: 1.79
habitat_maturity_level: 2
cognitive_level: 3
cognitive_source: team
gap: +1.21
regime: ambition-outpaces-enablement
ceiling_dimensions: [agent_composition, testing, observability]
weakest_discipline: guardrail-design
```
