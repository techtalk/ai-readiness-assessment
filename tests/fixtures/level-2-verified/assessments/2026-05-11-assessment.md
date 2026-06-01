# AI Literacy Assessment — wordcount (level-2-verified fixture)

**Date**: 2026-05-11
**Assessed level**: Level 2 — Verification discipline
**Habitat Build Gap**: +0.50 (Ambition outpaces enablement)

> **Test-run note**: batch mode, clarifying questions skipped.

## Habitat Document Discovery

| Document type | Path | Result | Markers |
|---|---|---|---|
| AI-instruction file | `.cursorrules` | **found** | Style + do/don't, ~15 lines, includes "Drop coverage below 80% — CI will fail" — couples the instruction file to enforced verification. |
| AI-instruction file | `CLAUDE.md` / `AGENTS.md` / `.github/copilot-instructions.md` | not found | — |
| Constraint document | `HARNESS.md` / `CONSTRAINTS.md` | not found | — |
| Specifications | `specs/`, `docs/specs/`, `rfcs/`, `proposals/` | not found | — |
| Reflection / decisions | `REFLECTION_LOG.md`, `docs/adr/`, `CHOICES.md` | not found | — |

One AI-instruction file. No constraint document, no specs, no
reflection layer. The habitat layer is absent even though the
verification layer is mature — this is the L2 fingerprint.

## Observable Evidence

**Found:**

- `.cursorrules` — agent instructions; explicitly references CI
  enforcement.
- `pyproject.toml` — `[tool.ruff]` with `E F I UP B` rules,
  `[tool.pytest.ini_options]` with `--cov=wordcount
  --cov-fail-under=80`, `dev` extras pinning pytest, pytest-cov, ruff.
- `tests/test_main.py` — four tests covering `count_words` (empty,
  single word, whitespace, newlines).
- `.github/workflows/ci.yml` — runs `ruff check .` and `pytest` on
  every PR and push to main. Sets up Python 3.10.
- `.pre-commit-config.yaml` — wires `ruff` and `ruff-format` hooks
  into commit time.
- `src/wordcount/__init__.py`, `src/wordcount/main.py` — implementation
  with type hints and pathlib, consistent with the rules.

**Not found:**

- `CLAUDE.md`, `AGENTS.md`, `HARNESS.md` — no rich habitat document.
- `skills/`, `commands/`, `agents/` — no custom AI tooling.
- `REFLECTION_LOG.md`, `docs/adr/`, `CHOICES.md` — no pattern-surfacing
  loop, no decision archaeology.
- `specs/`, `docs/specs/`, `rfcs/` — no specifications layer.
- `MODEL_ROUTING.md`, cost-capture scripts — no model/cost discipline.

## Clarifying Responses

Skipped (batch test run). The questions the skill would have asked:

1. "How consistently is `.cursorrules` actually consulted by agents,
   given how thin it is compared to the CI config?"
2. "Does PR review explicitly check for AI-generated drift, or only
   for the CI-checked properties?"
3. "Is `CLAUDE.md` actively on the roadmap (per the README), or is
   that aspirational?"

Not asked in this run.

## Level Assessment

**Level 2 — Verification discipline.**

Rationale: the verification stack is real and load-bearing — CI runs
ruff and pytest on every PR, a coverage threshold blocks regressions,
and pre-commit catches style drift before commit. The team can detect
when AI-generated output drifts from intent. But the habitat layer is
absent: no `CLAUDE.md`, no `HARNESS.md`, no custom skills, no
reflection loop. Strong verification with no encoded habitat is L2,
not L3 — the rules and the rationale exist only in CI configuration
and in one thin `.cursorrules` file.

Weakest discipline: **Context Engineering** (1, against Constraints
and Guardrails at 3 each).

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 1 | `.cursorrules` only; no CLAUDE.md / AGENTS.md / skills / onboarding for AI workflow. |
| Architectural Constraints | 3 | Ruff + coverage threshold enforced in CI; pre-commit hook; deliberate rule selection. No formal constraint document yet. |
| Guardrail Design | 3 | CI gate, pre-commit, test suite, coverage tripwire — feedback loops are in place. No adversarial review or plan-approval gate. |

## Operational Axes (Part D)

| Axis | Level (L1–L5) | Evidence |
|---|---|---|
| Composition | L1 | Single-agent via `.cursorrules`; no reusable command/skill library or critic agent. |
| Testing | L2 | Unit tests with CI and an 80% coverage tripwire; disciplined review. No mutation testing. |
| Observability | L1 | CI build logs only; no agent-activity metrics, dashboards, or acceptance tracking. |
| Governance | L2 | Style + coverage enforced in CI, but no written constitution (CLAUDE.md/HARNESS.md) — conventional, partly-enforced norms. |

**Operational axes mean**: L1.5

## Habitat Build Gap

```text
Cognitive level (Parts A–C):     L2
Operational axes mean (Part D):  L1.5
  Composition:   L1
  Testing:       L2
  Observability: L1
  Governance:    L2
Habitat Build Gap:               +0.50
Interpretation:                  Ambition outpaces enablement
```

Verification thinking (L2) runs ahead of the operational habitat (mean 1.5). The axis most worth lifting is Composition — encode a CLAUDE.md and a reusable review command so the verification habit persists beyond CI config.

## Strengths

1. **CI is the source of truth for code quality.** Ruff + pytest +
   coverage-floor gate every PR. The rules in `.cursorrules` align
   with what CI actually enforces — no convention drift.
2. **Pre-commit shortens the feedback loop.** Issues are caught before
   commit, not after PR-open. Local-environment cost is minimal.
3. **Coverage threshold is a real tripwire.** 80% is high enough to
   matter and low enough to be sustainable. This is the L1→L2 move
   done well.

## Gaps

1. **No `CLAUDE.md` / `AGENTS.md` / `HARNESS.md`.** Agents start each
   session with only `.cursorrules` (and only if they happen to look
   for it). The rationale behind the conventions, the architectural
   decisions, the "why we don't do X" — none of it is encoded.
2. **No reflection loop.** When a CI failure reveals a recurring
   AI-generated pattern, there's nowhere for the team to capture and
   promote it.
3. **No custom skills/commands.** Every AI session re-derives how to
   review a diff for project-specific style. No team-shared agent
   tooling.

## Recommendations

1. **Spend a half-day drafting a `CLAUDE.md` that captures the
   conventions you already enforce in CI** — type hints, pathlib,
   no bare except, coverage discipline, plus the *rationale* for
   each. Closes the largest Context-Engineering gap immediately.
2. **Add `REFLECTION_LOG.md` and write one entry from a recent
   incident.** The mechanism for promoting patterns from lived
   experience into `CLAUDE.md` becomes available.
3. **Pick one team-specific review task and make it a small skill or
   command.** E.g. a "style-check" skill that reviews a diff for the
   conventions in `CLAUDE.md`. Demonstrates the L3 pattern at low
   cost.

## Reading Path

Your assessed level is **L2 — Verification discipline**. The natural
next read in *The Sovereign Engineer* is the **Level 3 (habitat
design) chapter** — your team already has the verification habit; the
next compounding move is to persist it in the environment so it isn't
re-derived every session.

Get the book: <https://leanpub.com/thesovereignengineer>

## Next Steps

> Your weakest discipline is **Context Engineering** — the
> verification machinery is solid but the team's accumulated wisdom
> isn't encoded anywhere the agent can read. If you'd like help
> moving from Level 2 to Level 3, TechTalk runs a **habitat-document
> bootcamp**: a two-day workshop that produces a real `CLAUDE.md` for
> your codebase — not a template, your conventions, your rationale,
> your "why" — plus a one-page constraints index that aligns your
> existing CI rules with their stated intent.
>
> Get in touch: <https://techtalk.ai>
