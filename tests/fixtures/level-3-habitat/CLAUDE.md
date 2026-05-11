# CLAUDE.md — wordcount

This file is the agent's project briefing. Read it on every session start.

## What this project is

`wordcount` is a small Python library plus CLI. The library exposes one
public function (`count_words`); the CLI wraps it. The team keeps the
scope narrow on purpose — the project's job is to be a teaching example
of "small library, lots of habitat", not to grow features.

## Conventions (enforced)

- Python 3.10+ features welcome (`X | Y` unions, match statements,
  pattern matching). Older syntax (`Union[X, Y]`, `Optional[X]`) is a
  CI-blocking lint failure under ruff `UP` rules.
- All public functions have type hints. Internal helpers may omit them
  if the type is obvious from the body.
- `pathlib.Path` always. `os.path` is banned.
- No bare `except:` clauses. Always name the exception.
- No `print` in library code; use `logging`. CLI entry points may
  `print` to stdout for user-facing output.
- Coverage must stay at or above 80% (enforced in CI by
  `--cov-fail-under=80`).

See `HARNESS.md` for the constraint declarations and how each is
enforced (deterministic tool vs agent vs unverified).

## AI workflow

1. New work starts with a one-paragraph description in the PR body —
   what's changing and why.
2. The agent reads `CLAUDE.md` and `HARNESS.md` before touching code.
3. Failing test first. Production code only after the test is red for
   the right reason.
4. After merging, the author skims `REFLECTION_LOG.md` for related
   patterns. If something surprised them during the work, they add a
   reflection.

## Skills available

- `skills/wordcount-style/SKILL.md` — reviews a diff for style drift
  (the `pathlib`, no-`print`, no-bare-`except`, type-hint rules
  above). Invoke during PR review.

## Onboarding

See `ONBOARDING.md` for setting up the dev environment and the AI
collaboration workflow.
