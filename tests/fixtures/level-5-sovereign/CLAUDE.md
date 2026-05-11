# CLAUDE.md — wordcount

## What this project is

`wordcount` is a small Python library and the reference habitat for
the team's broader portfolio. The codebase is small on purpose; the
habitat around it is the artefact we share with sibling teams.

## Conventions

Python 3.10+, type hints, pathlib, no bare except, no print in
library code, coverage ≥ 80%. See `HARNESS.md`.

## Spec-first workflow

Same as L4 — see `ONBOARDING.md`. The orchestrator command
`/spec-implement` drives spec → plan → objections → code.

## Cross-team artefacts

This habitat is published as the `wordcount-habitat` plugin at
`.claude-plugin/plugin.json`. Sibling teams install it and run
`/wordcount-habitat-init` to adopt the same CLAUDE.md skeleton,
HARNESS.md constraint set, and CI workflow.

Decision archaeology lives in `CHOICES.md` — every load-bearing
choice the project has made is captured as a story (context,
choice, why, alternatives considered).

## Model routing

See `MODEL_ROUTING.md` for how the team picks between models per
task type, the cost ceilings, and the per-quarter spend history.

## Skills available

- `skills/wordcount-style/SKILL.md`

## Commands available

- `commands/spec-implement.md`
- `commands/wordcount-habitat-init.md` (for sibling teams)
