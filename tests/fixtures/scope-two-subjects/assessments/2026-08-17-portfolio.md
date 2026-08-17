# AI Readiness Portfolio — payments-tribe

**Fixture report — invented numbers, committed as test data.** The
roll-up output for `tests/fixtures/scope-two-subjects/`, written where
`report.output` resolves from the scope root: `<scope root>/assessments/`,
never `<scope root>/.habitat/assessments/`.

**Subjects assessed**: 2 of 2
**Gap spread**: +0.14 to +1.21 (range 1.07)
**Portfolio ceiling**: agent composition, observability (estate) · testing (billing)
**Date**: 2026-08-17

## Coverage ledger

| Subject | Status | Report date | Age | Note |
|---|---|---|---|---|
| orders-api | assessed | 2026-08-17 | 0d | — |
| billing | assessed | 2026-08-17 | 0d | cognitive read reused from the team |

2 of 2 named subjects assessed; 0 stale; 0 unreachable.

## Dimension matrix

All placements are `local` — no habitat is declared, so nothing is
inherited. `*` marks the weakest cell in the column.

| Subject | AB | AI | WF | OM | TP | OR | OA | HR | WP | AC | AD | Te | Ob | Gv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| orders-api | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 |
| billing | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 1* | 2* | 1* | 1* | 2* |

*AB Agent behaviour · AI Agent input · WF Workflow · OM Operating model ·
TP Teams provide · OR Output role · OA Output artefact · HR Humans review ·
WP Work patterns · AC Agent composition · AD Agents… · Te Testing ·
Ob Observability · Gv Governance*

## Gap table

| Subject | Habitat maturity mean | Cognitive level | Gap | Regime |
|---|---|---|---|---|
| orders-api | 2.86 | 3 | +0.14 | Coherent |
| billing | 1.79 | 3 | +1.21 | Ambition outpaces enablement |

## Spread

+0.14 (`orders-api`) to +1.21 (`billing`), range 1.07 — the headline
finding. One team, two habitats, and the enablement work the two facts
imply is not the same work.

`orders-api` has testing and governance at L3; `billing` has both at or
near the L1 floor. The difference is the environment, not the people —
the same cognitive read produced both gaps.

## Split ceiling

**Common weak** — agent composition and observability, weak in both
`active` subjects. This is the enablement backlog and it belongs to
whoever provides the habitat.

**Locally weak** — testing, weak in `billing` only. That is `billing`'s
own backlog.

## Portfolio regime

**Islanded**

No shared habitat is declared, the two subjects carry little duplication
between their control surfaces, and the gap spread is wide (1.07). One
subject is materially ahead: the steer is to transfer knowledge, moving
people rather than files.

## Confidence

Six placements across the two rows are `inferred` (three per subject) and
six are `asked`. No subject exceeds five inferred dimensions, so neither
row should be read as indicative-only. `billing` carries a reused
cognitive read — declared in its own report and in the ledger above.

## Steer

Transfer what `orders-api` knows about testing and governance into
`billing` before extending either habitat; the estate's shared ceiling
(agent composition, observability) is the enablement backlog behind that.
