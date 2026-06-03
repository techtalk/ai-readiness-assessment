# Spec 0001: Introduce a specifications layer

- **Status**: implemented
- **Date**: 2026-06-03
- **PR**: (this PR)

## Intent

Start the L3→L4 jump by making intent first-class: add a `specs/` layer
and a spec-first convention so substantive changes are captured as "what
and why" before "how". This is the top recommendation of the repo's own
self-assessment ([`assessments/2026-06-03-assessment.md`](../assessments/2026-06-03-assessment.md)),
where **Agent input** and the cognitive read are held at L3 by the
absence of specs.

## Design

- A `specs/` directory with a [`README.md`](README.md) (the convention),
  a [`TEMPLATE.md`](TEMPLATE.md), and sequential `NNNN-slug.md` specs.
- A lightweight format: Intent, Design, Alternatives, Risks / what could
  go wrong, Acceptance.
- **Spec-first** encoded as a HARNESS convention (Context → Conventions),
  not yet an enforced constraint: substantive PRs reference a spec;
  docs / chore / sync / fix are exempt.
- The adversarial "what could go wrong" review is **embedded** as a
  section in every spec, rather than added as a separate gate.

## Alternatives considered

- **A full SDD pipeline** with adversarial-review and plan-approval gates
  (as in `ai-literacy-superpowers`). Rejected for now — disproportionate
  for a small, prose-only plugin; the assessment explicitly recommended a
  lightweight start.
- **A hard deterministic constraint** requiring a spec per PR. Rejected
  initially — "substantive" is a judgment call, and a hard gate would
  fire false positives on docs / chore PRs. Start as a convention;
  promote to an agent-enforced constraint once the habit settles.
- **Keeping intent in PR descriptions only** (status quo). Rejected —
  that is precisely the L3 ceiling the assessment identified.

## Risks / what could go wrong

- **Specs become box-ticking or go stale.** Mitigation: keep them
  lightweight (a one-paragraph Intent is valid) and only for substantive
  work.
- **The convention is ignored because it isn't enforced.** Accepted for
  now; revisit by promoting it to a constraint if adoption lags.
- **Over-spec'ing trivial changes.** The exemptions (docs / chore / fix)
  and the "substantive, behaviour-changing" scope guard against this.

## Acceptance

- `specs/` exists with `README.md`, `TEMPLATE.md`, and this spec.
- HARNESS.md → Context → Conventions documents spec-first.
- A future self-assessment shows **Agent input** moving off L2 and the
  cognitive read on a credible path to L4.
