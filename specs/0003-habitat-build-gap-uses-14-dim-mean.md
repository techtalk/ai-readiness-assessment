# Spec 0003: The Habitat Build Gap uses the 14-dimension mean

- **Status**: implemented (recorded retroactively)
- **Date**: 2026-06-03
- **PR**: retroactive — the decision shipped with the model-as-spine work

## Intent

Record, as a first-class decision, why the **Habitat Build Gap** is
computed against the mean of **all fourteen** Habitat Maturity Model
dimensions rather than the four discipline-aligned headline axes. This is
a genuine product decision already in the instrument; capturing it
retroactively demonstrates the specs layer on real (non-meta) content.

## Design

`Habitat Build Gap = cognitive level − habitat maturity mean`, where the
maturity mean is the arithmetic mean of all fourteen dimension
placements. The four headline axes (Composition, Testing, Observability,
Governance) remain reported as a focused, discipline-aligned view, but
they do not define the gap.

## Alternatives considered

- **Gap on the four headline axes only** (the original implementation).
  More stable and the most repo-observable subset — but it ignores ten
  of the fourteen dimensions and undercuts the claim that the instrument
  evaluates against the *whole* model. Rejected: completeness beats
  stability for a coherence diagnostic.
- **A weighted mean** emphasising the headline axes. Rejected — adds
  opacity for little benefit; an unweighted mean is explainable.

## Risks / what could go wrong

- **Behavioural dimensions are inferred**, so they carry more uncertainty
  into the mean — accepted; they are flagged `(inferred)` in the profile,
  and the gap is a coherence signal, not a precision score.
- **Regime flips** when moving from the 4-axis to the 14-dim mean (two
  fixtures changed regime). Accepted and documented at the time.

## Adversarial review

- **Reviewer**: PR reviewer (human, at the time of the model-spine work)
- **Disposition**: accepted
- **Notes**: The regime flips were reviewed and judged the honest
  consequence of counting the process dimensions, not a defect.

## Acceptance

- The gap formula in `HARNESS.md` is unused here, but the instrument
  (`commands/` + `skills/`) and `docs/reference/habitat-build-gap.md`
  state the gap as the 14-dimension mean — which they do.
