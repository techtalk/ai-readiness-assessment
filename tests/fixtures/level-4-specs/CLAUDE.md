# CLAUDE.md — wordcount

This file is the agent's project briefing. Read it on every session start.

## What this project is

`wordcount` is a small Python library plus CLI. The team uses it as
a teaching example of "small library, fully harnessed, spec-first
discipline."

## Conventions (enforced)

Same as L3: Python 3.10+, type hints, pathlib, no bare except, no
print in library code, coverage ≥ 80%. See `HARNESS.md` for the
enforcement table.

## Spec-first workflow

This project is **spec-first**. The order is:

1. Write a spec under `specs/NNNN-<slug>.md` describing what and why.
2. Run `/spec-implement <spec>` — the orchestrator drafts an
   implementation plan under `specs/plans/NNNN-<slug>-plan.md` and
   pauses for human approval.
3. At plan approval, run the adversarial review — record dispositions
   under `docs/objections/NNNN-<slug>.md`. All objections must be
   resolved (accepted, deferred with reason, or refuted with reason)
   before implementation begins.
4. Write a failing test that reflects the spec.
5. Write the production code to make it pass.
6. The PR description must reference the spec by path.

The CI workflow enforces the PR-references-a-spec check.

## Skills available

- `skills/wordcount-style/SKILL.md` — diff-time style review.

## Commands available

- `commands/spec-implement.md` — orchestrator that takes a spec and
  produces a plan, then pauses for adversarial review before
  proceeding.

## Onboarding

See `ONBOARDING.md`.
