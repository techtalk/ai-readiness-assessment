# Cognitive ladder & disciplines

Alongside the [habitat maturity model](habitat-maturity-model.md), the
assessment places the team on the **cognitive read** — the six-level AI
collaboration literacy ladder from *The Sovereign Engineer*. This
measures what the team can *think and do*.

## The six levels

| Level | Name | What's visible in the repo when a team is here |
|-------|------|------------------------------------------------|
| **L0** | Aware of the landscape | AI tools may be used, but nothing in the repo encodes that fact. No instruction files, no AI-aware conventions, no captured prompts. |
| **L1** | Communicating through prompts | Some AI-instruction file exists (`.github/copilot-instructions.md`, `CLAUDE.md`, `.cursorrules`, `.windsurfrules`, `AGENTS.md`). Usually thin — style hints, a few do/don't bullets. |
| **L2** | Verification discipline | The above, plus deterministic guardrails: linting in CI, coverage thresholds, pre-commit hooks, PR review that catches AI drift. The team can *detect* when output has drifted. |
| **L3** | Habitat design | A persistent collaboration environment: rich CLAUDE.md/AGENTS.md, an explicit constraint document (HARNESS.md), custom skills/commands/hooks, a reflection log, decision records, AI-aware onboarding. |
| **L4** | Specification-led | Specs are first-class: a `specs/` directory, plans separated from specs, spec-first ordering, adversarial spec review at a plan-approval gate, orchestrated multi-step agent workflows. |
| **L5** | Sovereign engineering | Platform-level practice: cross-team templates or a published plugin, governance audit cadence, decision archaeology, fitness functions in CI, cost/model-routing discipline, portfolio-level artefacts. |

The cognitive ladder runs **L0–L5** (six rungs); the model's dimensions
run **L1–L5** (five). L0 is "aware but nothing encoded" — on the model's
dimensions, that is the L1 floor.

## The three disciplines

Every cognitive level rests on three disciplines:

1. **Context Engineering** — how the team encodes accumulated wisdom into
   the agent's context window (instruction files, skills, onboarding, the
   reflection-to-curation loop).
2. **Architectural Constraints** — how the team makes structural rules
   machine-checkable (HARNESS.md, CI gates, fitness functions;
   deterministic vs agent-enforced vs by-convention).
3. **Guardrail Design** — how the team designs the feedback loops that
   catch drift (test suites, pre-tool hooks, adversarial review, output
   validation, plan- and integration-approval gates).

## The scoring heuristic

> The assessed cognitive level is the **highest level where the team has
> substantial evidence across all three disciplines.** The weakest
> discipline is the ceiling.

So strong specs with weak verification is **L2, not L4**. Strong
guardrails with no encoded context is **L2, not L3**. See
[Coherence, not level](../explanation/coherence-not-level.md) for the
reasoning behind "the weakest discipline is the ceiling".

The **Governance** dimension of the model is the operational face of the
**Architectural Constraints** discipline; the report keeps the two
consistent — the dimension is the one-line placement, the discipline
score is the deeper read.
