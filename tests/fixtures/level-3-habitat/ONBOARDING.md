# Onboarding — wordcount

## Day one

1. Clone the repo.
2. `python -m venv .venv && source .venv/bin/activate`
3. `pip install -e ".[dev]"`
4. `pre-commit install`
5. `pytest` — should pass with ≥ 80% coverage.

## AI collaboration workflow

1. **Read `CLAUDE.md` first.** Always.
2. Open a PR with a one-paragraph description: what's changing and
   why.
3. Write the failing test before writing the production code.
4. Use the `wordcount-style` skill on the diff before requesting human
   review.
5. If something surprises you during the work, add an entry to
   `REFLECTION_LOG.md`. Surprises that recur become entries in
   `CLAUDE.md` or `HARNESS.md`.

## Where to find what

- Conventions (prose): `CLAUDE.md`
- Constraints (machine-checkable rules): `HARNESS.md`
- Reflections / pattern surfacing: `REFLECTION_LOG.md`
- Decisions: `docs/adr/`
- Skills the team uses: `skills/`
