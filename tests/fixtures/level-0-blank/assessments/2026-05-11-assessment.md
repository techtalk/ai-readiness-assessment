# AI Literacy Assessment — wordcount (level-0-blank fixture)

**Date**: 2026-05-11
**Assessed level**: Level 0 — Aware of the landscape

> **Test-run note**: This assessment was produced by the
> `ai-readiness-assessment` skill running in **batch mode** against a
> TDAB fixture. Step 2 of the skill's process (3–5 clarifying
> questions, one at a time) was skipped because the run was
> non-interactive. The skipped step is recorded honestly in the
> Clarifying Responses section below and counts as a behavioural
> assertion failure in the matching test report.

## Habitat Document Discovery

| Document type | Path checked | Result |
|---|---|---|
| AI-instruction file | `CLAUDE.md` | not found |
| AI-instruction file | `AGENTS.md` | not found |
| AI-instruction file | `.github/copilot-instructions.md` | not found |
| AI-instruction file | `.cursorrules` / `.cursor/rules/` | not found |
| AI-instruction file | `.windsurfrules` / `.windsurf/rules/` | not found |
| AI-instruction file | `.aider.conf.yml` | not found |
| AI-instruction file | `GEMINI.md` / `AI.md` / `LLM.md` | not found |
| Constraint document | `HARNESS.md` | not found |
| Constraint document | `CONSTRAINTS.md` | not found |
| Constraint document | `ARCHITECTURE.md` (as enforcement) | not found |
| Specifications | `specs/`, `docs/specs/`, `rfcs/`, `proposals/` | not found |
| Reflection / decisions | `REFLECTION_LOG.md`, `JOURNAL.md`, `docs/adr/`, `docs/decisions/`, `CHOICES.md` | not found |

No habitat documents exist. This is the L0 fingerprint.

## Observable Evidence

**Found (paths verified to exist in the fixture):**

- `README.md` — a thin, project-status README. Mentions Python 3.10+
  and points the reader at an issue tracker; says nothing about AI
  collaboration or conventions.
- `.gitignore` — standard Python ignores.
- `pyproject.toml` — minimal project metadata (name, version,
  `requires-python`). **No** `[tool.ruff]`, `[tool.pytest.ini_options]`,
  coverage config, or any linter configuration.
- `src/wordcount/__init__.py` — re-exports `count_words`.
- `src/wordcount/main.py` — five lines: a function and a `__main__`
  block.

**Not found:**

- `.github/workflows/` — no CI workflow.
- `.gitlab-ci.yml`, `.circleci/`, `azure-pipelines.yml` — no CI of any
  kind.
- `tests/` or `test_*.py` — no test suite.
- `.pre-commit-config.yaml`, `lefthook.yml`, `husky/` — no pre-commit
  or pre-tool hooks.
- `skills/`, `commands/`, `agents/` — no custom AI tooling.
- `MODEL_ROUTING.md`, cost-capture scripts, AI-spend observability —
  no cost or model-routing discipline.

## Clarifying Responses

Skipped (batch test run). The questions the skill would normally have
asked here:

1. "Are AI tools used by the team at all, even informally?"
2. "Has anyone drafted (but not committed) an instruction file?"
3. "Is the lack of tests a deliberate choice for this stage, or a
   gap?"

These are recorded for honesty; they were **not** asked during this
run.

## Level Assessment

**Level 0 — Aware of the landscape.**

Rationale: no AI-instruction file exists anywhere in the conventional
or alternative locations. No constraint document, no specs, no
reflection log, no custom AI tooling. The repo has not yet encoded
the existence of AI collaboration in any way. All three disciplines
are at floor.

The ceiling is set by Context Engineering: until at least one
instruction file exists, the team is communicating with the agent
fresh every session.

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 0 | No AI-instruction file, no skills, no onboarding for AI workflow. |
| Architectural Constraints | 0 | No constraint document, no lint config, no enforced rules. |
| Guardrail Design | 0 | No CI, no tests, no hooks, no review checklist. |

## Strengths

1. **README exists and is honest about project status.** "Early. The
   team has only just started this project." That candour is rare and
   makes the next step (encoding intent) easier to start.
2. **The codebase is tiny.** Five-line implementation, one public
   function. Adding a CLAUDE.md and a small test suite is a
   low-friction first step.
3. **The dependency surface is empty.** Nothing to migrate, no
   compatibility constraints. Greenfield habitat work is possible.

## Gaps

1. **No AI-instruction file.** Every Claude/Cursor/Copilot session
   starts blank. The agent has no project context, no conventions, no
   anchors — it has to be told everything afresh, every time.
2. **No verification discipline.** No tests, no CI, no linter — the
   team has no automated way to detect when AI-generated output drifts
   from intent.
3. **No persistent collaboration environment.** No skills, commands,
   or hooks. Anything the agent learns this session is lost next
   session.

## Recommendations

1. **Write a thin `CLAUDE.md` (or `.cursorrules`) — today.** Even a
   one-page file with five conventions and one "always do this, never
   do that" pair lifts the team out of L0. Closes the Context
   Engineering gap.
2. **Add `pytest` and one test for `count_words`.** A single failing-
   then-passing test establishes verification discipline. Closes the
   Guardrail Design gap.
3. **Wire ruff and pytest into a one-job GitHub Actions workflow.**
   Once the test exists, the CI gate exists. Closes the Architectural
   Constraints gap.

## Reading Path

Your assessed level is **L0 — Aware of the landscape**. The natural
next read in *The Sovereign Engineer* is **Act I in full** — the
amplifier thesis, the two kinds of intelligence, and why the
collaboration space (not the agent) is the unit of leverage. That
framing makes the next concrete steps (an instruction file, a test
suite, a CI gate) feel like investments in a shared environment
rather than chores.

Get the book: <https://leanpub.com/thesovereignengineer>

## Next Steps

> Your weakest discipline is **Context Engineering** — the project
> has no encoded intent at all. If you'd like help moving from Level
> 0 to Level 1, TechTalk runs a **habitat-document bootcamp**: a
> two-day workshop that produces a `CLAUDE.md` (or equivalent
> instruction file) for your actual codebase, plus a one-page
> conventions index the team agrees to maintain. The two days take
> you out at L1 with a credible path to L2.
>
> Get in touch: <https://techtalk.ai>
