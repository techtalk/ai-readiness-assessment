# Assessment summary block

Every assessment report ends with a fenced `assessment-summary` block: a
machine-readable record of the same placements the prose just reported.

It exists so a [portfolio roll-up](portfolio-report.md) can read a report
months later without re-running the assessment and without re-parsing
prose. That single property is what makes multi-repo work tractable —
running an assessment and summarising one become separate acts, done by
different people at different times.

## Shape

````markdown
```yaml assessment-summary
schema: 1
subject: orders-api
subject_path: .
team: payments-tribe
assessed_at: 2026-08-14
tool_version: 0.5.0

dimensions:
  agent_behaviour:   { level: 3, confidence: inferred }
  agent_input:       { level: 2, confidence: observed }
  workflow:          { level: 3, confidence: observed }
  operating_model:   { level: 4, confidence: asked }
  teams_provide:     { level: 3, confidence: observed }
  output_role:       { level: 4, confidence: asked }
  output_artefact:   { level: 3, confidence: observed }
  humans_review:     { level: 4, confidence: asked }
  work_patterns:     { level: 3, confidence: inferred }
  agent_composition: { level: 2, confidence: observed }
  agents_do:         { level: 3, confidence: inferred }
  testing:           { level: 2, confidence: observed }
  observability:     { level: 2, confidence: observed }
  governance:        { level: 3, confidence: observed }

habitat_maturity_mean: 2.93
habitat_maturity_level: 3
cognitive_level: 4
gap: +1.07
regime: ambition-outpaces-enablement
ceiling_dimensions: [testing, observability, agent_composition]
weakest_discipline: guardrail-design
```
````

## Keys

| Key | Meaning |
|---|---|
| `schema` | Block schema version. Currently `1`. |
| `subject` | The subject's identifier — matches `id` in the [scope manifest](scope-manifest.md) where one exists. |
| `subject_path` | Path to the subject, relative to the report. |
| `team` | Whose cognitive read this is. |
| `assessed_at` | Date of the assessment. |
| `tool_version` | Plugin version that produced it. |
| `dimensions` | All fourteen model dimensions, always. |
| `habitat_maturity_mean` | Mean of the fourteen levels, two decimals. |
| `habitat_maturity_level` | The rounded headline level. |
| `cognitive_level` | The Sovereign Engineer cognitive read, L0–L5. |
| `gap` | Signed: `cognitive_level` minus `habitat_maturity_mean`. |
| `regime` | `coherent`, `ambition-outpaces-enablement`, or `inherited-habitat`. |
| `ceiling_dimensions` | The weakest dimensions — the ones naming the ceiling. |
| `weakest_discipline` | `context-engineering`, `architectural-constraints`, or `guardrail-design`. |

The fourteen dimension keys follow the
[Habitat Maturity Profile](habitat-maturity-model.md) table in order.
`agents_do` is the key for the *Agents…* row.

## Confidence

Every placement records how it was arrived at. This is the honesty
mechanism, and it is the one thing a roll-up cannot re-derive — a
downstream reader has no way to tell a measured L3 from a guessed one
unless the report says so.

| Value | Meaning |
|---|---|
| `observed` | Placed evidence-first from the scan. |
| `asked` | A clarifying question was spent on this dimension. |
| `inferred` | Placed from what the other dimensions imply. |

The defaults follow the model's own split: the eight repo-observable
dimensions are `observed`, the six behavioural ones `inferred`.

**Absence is evidence.** A dimension placed at L1 because the scan found
nothing is `observed` — the scan looked, and the artefacts were not
there. `inferred` is for a dimension the evidence could not place either
way.

## Rules

- **The block is the last element of the file.** Nothing follows the
  closing fence; the roll-up reads it as the tail.
- **It is generated from the placements the prose reports, never
  computed separately.** If the two disagree, the report is lying to
  somebody — and the roll-up only ever sees the block. The test suite
  asserts agreement on maturity level, cognitive read and regime.
- **`provenance` is not emitted yet.** It arrives with shared-habitat
  support, where it distinguishes local evidence from an inherited rule
  that does or does not bind. Writing a placeholder `local` on every row
  today would make those cases indistinguishable later.
