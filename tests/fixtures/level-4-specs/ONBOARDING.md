# Onboarding — wordcount

## Day one

1. Clone, set up venv, install dev deps.
2. `pre-commit install`
3. `pytest`

## AI collaboration workflow (spec-first)

1. Read `CLAUDE.md` on every session.
2. Open work by drafting a spec under `specs/NNNN-<slug>.md`. Even
   one paragraph counts — what and why.
3. Run `/spec-implement specs/NNNN-<slug>.md` to produce a plan.
4. At plan approval, walk through the adversarial review. Record
   dispositions under `docs/objections/NNNN-<slug>.md`. All must be
   resolved.
5. Failing test first. Production code second.
6. PR references the spec by path.

## Where things live

- Specs: `specs/`
- Plans: `specs/plans/`
- Objections: `docs/objections/`
- Conventions: `CLAUDE.md`
- Constraints: `HARNESS.md`
- ADRs: `docs/adr/`
- Reflections: `REFLECTION_LOG.md`
- Skills/commands: `skills/`, `commands/`
