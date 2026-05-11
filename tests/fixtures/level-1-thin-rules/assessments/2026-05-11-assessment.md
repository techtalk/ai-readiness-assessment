# AI Literacy Assessment — wordcount (level-1-thin-rules fixture)

**Date**: 2026-05-11
**Assessed level**: Level 1 — Communicating through prompts

> **Test-run note**: batch mode, clarifying questions skipped.

## Habitat Document Discovery

| Document type | Path | Result | Markers matched |
|---|---|---|---|
| AI-instruction file | `.cursorrules` | **found** | Style hints ("Use Python 3.10+ features"), a few do/don't bullets, naming preferences. Thin — ~20 lines, prose only, no enforcement claim. |
| AI-instruction file | `CLAUDE.md` | not found | — |
| AI-instruction file | `AGENTS.md` | not found | — |
| AI-instruction file | `.github/copilot-instructions.md` | not found | — |
| AI-instruction file | `.windsurfrules` | not found | — |
| AI-instruction file | `GEMINI.md` / `AI.md` / `LLM.md` | not found | — |
| Constraint document | `HARNESS.md` / `CONSTRAINTS.md` | not found | — |
| Specifications | `specs/`, `docs/specs/`, `rfcs/`, `proposals/` | not found | — |
| Reflection / decisions | `REFLECTION_LOG.md`, `docs/adr/`, `CHOICES.md` | not found | — |

One AI-instruction file is present and clearly intended for the
agent. No constraint document, no specs, no reflection layer. This is
the L1 fingerprint.

## Observable Evidence

**Found:**

- `.cursorrules` — thin agent instructions (style hints + do/don't).
- `pyproject.toml` — declares `[tool.ruff]` with `line-length`,
  `target-version`, and an explicit lint rule set (`E`, `F`, `I`,
  `UP`). Ruff configuration exists.
- `README.md` — references `.cursorrules` and mentions running ruff
  before pushing; no CI claim.
- `src/wordcount/__init__.py`, `src/wordcount/main.py` — implementation
  uses type hints (`text: str`) and `pathlib.Path`, consistent with
  the `.cursorrules` content.

**Not found:**

- `.github/workflows/` — no CI workflow exists. The ruff config is
  local-only.
- `tests/` or `test_*.py` — no test suite.
- `.pre-commit-config.yaml` — no pre-commit hook.
- Coverage threshold — no `[tool.pytest.ini_options]`, no
  `--cov-fail-under`.
- `skills/`, `commands/`, `agents/` — no custom AI tooling.

## Clarifying Responses

Skipped (batch test run). The questions the skill would have asked:

1. "Is `.cursorrules` actually read by the team during sessions, or
   has it gone stale?"
2. "Does ruff get run reliably before push, or is it intermittent?"
3. "Is the lack of a test suite a temporary choice, or load-bearing?"

These are recorded for honesty; they were **not** asked during this
run.

## Level Assessment

**Level 1 — Communicating through prompts.**

Rationale: a thin `.cursorrules` file exists and the codebase reflects
it (`pathlib.Path`, type hints), so the team is communicating with
the agent through structured prompts. But verification discipline is
absent — ruff runs locally only, there are no tests, no CI, and no
pre-commit hook. The team cannot detect when AI-generated output
drifts from intent, which is the L2 threshold.

Weakest disciplines: **Architectural Constraints** and **Guardrail
Design**, both at 0. The cursorrules content gets Context Engineering
above the floor.

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 1 | `.cursorrules` is present and load-bearing; ~20 lines, prose only; no `CLAUDE.md` / `AGENTS.md` / skills. |
| Architectural Constraints | 0 | `[tool.ruff]` config exists but is local-only — no CI enforcement, no constraint document. |
| Guardrail Design | 0 | No tests, no CI, no pre-commit, no PR review checklist. |

## Strengths

1. **The instruction file is honest about its scope.** It encodes
   style preferences and naming rules without pretending to be a full
   constraint document — easy to extend, low cognitive load.
2. **The codebase already obeys the instruction file.** `pathlib.Path`
   and type hints are present in `main.py`; the agent (or the human)
   is following the rules they wrote down.
3. **A linter is configured.** Ruff config exists in `pyproject.toml`
   with a deliberate rule set. The mechanism for verification
   discipline is one CI workflow away.

## Gaps

1. **No CI.** Ruff is configured but not enforced. A PR could land
   with `Union[X, Y]` style and nothing would catch it before merge.
2. **No tests.** Nothing detects functional regressions, AI-generated
   or otherwise.
3. **No pre-commit hook.** Local-only enforcement depends on
   developer memory.

## Recommendations

1. **Add a one-job GitHub Actions workflow that runs `ruff check .`
   on every PR.** Promotes the existing local-only ruff config to
   architectural-constraint status. Closes the L1→L2 gap most
   directly.
2. **Add `pytest` with one test for `count_words`.** Establishes
   verification discipline. Closes the Guardrail Design gap.
3. **Wire ruff into pre-commit (`.pre-commit-config.yaml`).** Removes
   the "developer forgot to run ruff" failure mode. Cheap.

## Reading Path

Your assessed level is **L1 — Communicating through prompts**. The
direct next read in *The Sovereign Engineer* is the **Level 1
chapter** on prompts and structured context, **plus** the **Level 2
verification chapter** so the next step is already in view. Read them
back to back — the Level 1 chapter validates what you have; the Level
2 chapter is the bridge.

Get the book: <https://leanpub.com/thesovereignengineer>

## Next Steps

> Your weakest discipline is **Architectural Constraints** — you have
> the lint configuration but no machine-checkable enforcement of it.
> If you'd like help moving from Level 1 to Level 2, TechTalk runs a
> **harness-engineering consulting engagement**: a focused two-day
> piece of work that installs a machine-checkable constraint set
> against your actual codebase, with CI enforcement on every PR, so
> the ruff rules you already wrote down are the rules the merge gate
> actually enforces.
>
> Get in touch: <https://techtalk.ai>
