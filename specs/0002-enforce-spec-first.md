# Spec 0002: Enforce spec-first and adversarial review

- **Status**: implemented
- **Date**: 2026-06-03
- **PR**: (this PR)

## Intent

Complete the L3→L4 jump the self-assessment identified. The specs layer
(spec 0001) is scaffolding; this makes spec-first a **lived, enforced
discipline** so intent is genuinely first-class: substantive,
behaviour-changing changes carry a spec, and each spec's risks get an
adversarial review at the plan-approval (PR) gate.

## Design

- Promote **Spec-first** from a HARNESS *convention* to an **enforced
  constraint** (scope: pr).
- Add a deterministic **spec-first gate**
  (`.github/workflows/spec-first-gate.yml`, required check): a PR that
  changes the instrument (`commands/**` or `skills/**`) must also change
  a file under `specs/`, unless it carries an exempt label
  (`chore` / `fix` / `docs`). This enforces spec-first ordering for
  behaviour-changing work.
- Add an **Adversarial review** disposition to the spec format (template
  + existing specs): a reviewer other than the author adjudicates the
  Risks section at PR — the plan-approval gate L4 calls for.

## Alternatives considered

- **Leave spec-first as a convention.** Rejected — that is the
  scaffolding state the self-assessment already capped at L3; intent
  isn't first-class until the discipline is enforced.
- **A heavy SDD pipeline / dedicated adversarial-reviewer agent** (as in
  ai-literacy-superpowers). Rejected — disproportionate for a prose
  plugin; the PR reviewer is a real human plan-approval gate, and the
  spec's Risks + disposition capture the adversarial review lightly.
- **Require a spec on *every* PR.** Rejected — docs/chore/fix don't need
  one; the gate scopes enforcement to instrument changes.

## Risks / what could go wrong

- **Spec-first becomes bureaucratic theatre** — mitigate by scoping the
  gate to instrument changes only, and keeping specs lightweight.
- **The gate is gameable** (touch any `specs/` file to pass) — accepted;
  the adversarial-review disposition and human PR review are the quality
  backstop, not the file-touch check.
- **Over-claiming L4 on thin practice** — mitigate by assessing honestly
  afterward and only publishing an L4 example if the instrument reads L4.

## Adversarial review

- **Reviewer**: PR reviewer (human, at merge)
- **Disposition**: accepted
- **Notes**: The "gameable gate" risk is acknowledged and accepted — the
  gate enforces *ordering* (a spec accompanies instrument changes), while
  quality rests on the adversarial-review disposition and human review,
  not on the deterministic check.

## Acceptance

- HARNESS.md carries an enforced **Spec-first** constraint.
- `spec-first-gate.yml` exists and is a required check on `main`.
- The spec template and existing specs carry an Adversarial review
  disposition.
- A subsequent self-assessment honestly reads **L4** (specs first-class,
  enforced, reviewed). If it does not, the discipline is recorded as
  "L4 machinery in place" and the example is held.
