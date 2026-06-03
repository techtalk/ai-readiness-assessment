# AI Readiness Assessment — ai-readiness-assessment

**AI Readiness — Habitat Maturity**: Level 3 (Regulating)
**Next Step / Gap**: +1.2 to Level 4 (Orchestrating)

**Habitat Build Gap**: +0.2 (Coherent)   <!-- coherence (cognitive − operational); secondary -->
**Assessed level**: Level 3 — Habitat design   <!-- cognitive read; do not remove -->
**Date**: 2026-06-03

> **Note**: this is the plugin assessed against **its own repository** — a
> dogfooding example of the output `/ai-readiness-assess` produces.
> Clarifying questions were answered from the maintainers' knowledge of
> the repo rather than asked interactively.

## Habitat Document Discovery

| Document type | Path | Result | Markers |
|---|---|---|---|
| AI-instruction (cross-tool) | `AGENTS.md` | **found** | GOTCHAS, WORKFLOWS, TEST_STRATEGY, ARCH_DECISIONS — human-curated operational layer |
| Convention files | `.cursor/rules/`, `.github/copilot-instructions.md`, `.windsurf/rules/` | **found** | Synced from HARNESS.md via `/convention-sync` — conventions + constraints |
| Constraint document | `HARNESS.md` | **found** | Context / Constraints / GC / Observability / Status; 3 constraints + 1 GC rule; template-version 0.40.0 |
| Reflection log | `REFLECTION_LOG.md` | **found** | 2 dated entries, both with verified `Promoted` lines into AGENTS.md / HARNESS.md |
| Onboarding | `ONBOARDING.md` | **found** | Generated from HARNESS + AGENTS; 10-section contributor guide |
| Docs site | `docs/` + `mkdocs.yml` | **found** | 22 pages, Diátaxis (tutorials / how-to / reference / explanation), deployed to GitHub Pages |
| Plugin + marketplace | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | **found** | Published `techtalkai` marketplace plugin, v0.4.1, Apache-2.0 |
| Specifications | `specs/`, `docs/specs/`, `rfcs/`, `proposals/` | **not found** | — |
| Decision archaeology | `CHOICES.md`, `docs/adr/`, choice-story records | **not found** | (ARCH_DECISIONS in AGENTS.md is a lightweight substitute) |
| Cost / model routing | `MODEL_ROUTING.md` | **not found** | — |
| Observability snapshots | `observability/` | **not found** | — |

The habitat layer is rich and integrated. The specifications layer is
absent. That combination is the L3 fingerprint.

## Observable Evidence

**Found:**

- Rich, synced context surfaces: `HARNESS.md`, `AGENTS.md`,
  `ONBOARDING.md`, and three convention files kept in lockstep via
  `/convention-sync` / `/harness-sync`.
- A live reflection→promotion loop: `REFLECTION_LOG.md` (2 entries) with
  `Promoted` lines landing in `AGENTS.md` and `HARNESS.md`.
- Verification + governance in CI: four GitHub Actions workflows
  (`agentic-behaviours.yml`, `changelog-gate.yml`, `release.yml`,
  `pages.yml`), two **required status checks** on a branch-protected
  `main`, and a changelog-driven release pipeline (5 releases,
  v0.1.0–v0.4.1).
- A TDAB test suite (`tests/run.py`) with six fixtures, gating PRs.
- A published Diátaxis docs site (22 pages) on GitHub Pages.

**Not found:**

- No `specs/` layer, no spec-first commit ordering, no adversarial spec
  review (`docs/objections/` or equivalent).
- No agent composition for development — single agent, no read-only
  critics or orchestrator on PRs.
- No observability of agent activity or cost; no `observability/`
  snapshots, no `MODEL_ROUTING.md`.
- No decision-archaeology records beyond `AGENTS.md` ARCH_DECISIONS.

## AI Readiness Score — five readiness dimensions

A view over the same evidence (the headline level is the 14-dimension
Habitat Maturity):

| Readiness dimension | Level | Evidence |
|---|---|---|
| Context | L4 | HARNESS Context, AGENTS, ONBOARDING, synced convention files, docs |
| Conventions | L4 | Six HARNESS conventions, synced to Cursor / Copilot / Windsurf |
| Architectural guidance | L3 | HARNESS constraints + CI gates; no specs layer yet |
| Guardrails | L3 | TDAB + CI gates, but Testing and Observability still L2 |
| Agent readiness | L2 | Single agent; no read-only critics or orchestration |

## Clarifying Responses

Answered from maintainer knowledge (not asked interactively):

1. *Are specs written before code?* No — work is driven by
   natural-language requests plus the HARNESS/AGENTS context. There is no
   `specs/` layer.
2. *Do read-only critics or an orchestrator run on changes?* No — a
   single agent does the work; CI provides deterministic gates, not agent
   review.
3. *Is agent activity or cost observed?* No — only CI run logs exist; no
   AI-collaboration metrics or dashboards.

## Habitat Maturity Profile (Agentic Experience 5-Level Habitat Maturity Model)

All fourteen dimensions, each L1–L5, reported with the model's verb.

| Dimension | Level | Stage (verb) | Evidence / basis |
|---|---|---|---|
| Agent behaviour | L3 | Regulating | Humans direct and verify each change; harness-engineered guardrails |
| Agent input | L2 | larger prompts, commands | NL requests + HARNESS/AGENTS context; no specs layer |
| Workflow | L4 | workflow defined | CI pipeline, automated releases, changelog gate, docs deploy |
| Operating model | L3 | drive / verify | Human reviews and merges every PR |
| Teams provide | L3 | comprehensive product constitution | HARNESS + AGENTS + ONBOARDING + convention files |
| Output role | L3 | Standardising | Process & consistency rules are the primary output |
| Output artefact | L3 | process & consistency rules | HARNESS constraints + conventions; releases carry CHANGELOG evidence |
| Humans review | L3 | implementation in detail | PR diffs and prose reviewed in detail; no spec review |
| Work patterns | L3 | e2e development | Each change is branch → implement → test → PR → merge |
| Agent composition | L2 | single + saved patterns | Single agent + saved conventions; no critics/orchestrator for dev |
| Agents… | L3 | Develop small changes (stories) | Agent implements story- to epic-sized changes under approval |
| Testing | L2 | Asserting | A-tier structural assertions in CI; B/C (behavioural/semantic) manual |
| Observability | L2 | Captured | CI run logs captured/searchable; no AI-activity or cost metrics |
| Governance | L3 | Constitutional | HARNESS constitution enforced; required checks + changelog gate are emerging policy-as-code |

**Habitat Maturity Level**: L3 (mean L2.8; weakest: L2 Agent input, Agent composition, Testing, Observability)

## Level Assessment

**Level 3 — Habitat design.**

Rationale: the team has an exemplary, persistent collaboration
environment — a rich and *synced* context layer (HARNESS / AGENTS /
ONBOARDING / convention files), a reflection loop that has demonstrably
promoted learnings into the harness, policy-as-code governance (required
CI checks + changelog gate on a protected `main`), a TDAB test suite, and
a published plugin with an automated release pipeline and a docs site.
The ceiling is the **absence of a specifications layer**: no `specs/`, no
spec-first ordering, no adversarial spec review. Intent lives in PR
descriptions and AGENTS/HARNESS prose, not as first-class specs — so
despite some L5-flavoured platform artefacts (a published, versioned
plugin), the L4 rung (specs) has not been climbed.

Weakest discipline: **Architectural Constraints** and **Guardrail
Design** are tied at 3 — strong machine-checkable enforcement and
feedback loops, but missing the spec-conformance and adversarial-review
layer that L4 implies.

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 4 | HARNESS Context, AGENTS.md, ONBOARDING.md, synced convention files, a running reflection→promotion loop, and a 22-page docs site. Exemplary for the project's size. |
| Architectural Constraints | 3 | HARNESS.md with 3 constraints (1 deterministic, 1 agent, 1 unverified) + 1 GC rule; required CI checks + changelog gate (policy-as-code). Small set; one unverified; no spec-conformance or fitness functions. |
| Guardrail Design | 3 | TDAB suite gating PRs, two required checks, branch protection, changelog gate, release verification. No adversarial-review or plan-approval gate. |

## Operational Axes (Part D)

The four discipline-aligned headline dimensions, lifted from the profile
above — a focused, discipline-aligned view. The Habitat Build Gap uses
all fourteen dimensions, not just these four.

| Axis | Level (L1–L5) | Evidence |
|---|---|---|
| Composition | L2 | Single dev agent + saved conventions; no read-only critics or orchestrator |
| Testing | L2 | A-tier structural assertions automated in CI; B/C tiers manual |
| Observability | L2 | CI run logs only; no AI-activity/cost metrics or dashboards |
| Governance | L3 | Enforced HARNESS constitution + required-check / changelog-gate policy-as-code |

**Headline axes mean**: L2.25

## Habitat Build Gap

    Habitat Maturity Level (model):  L3  (14-dim mean L2.79)
    Cognitive read (Parts A–C):      L3
    Habitat Build Gap:               +0.21   (cognitive − 14-dim mean)
    Interpretation:                  Coherent

The team and its habitat are in step — a coherent L3. Thinking is not
running ahead of the environment, nor vice versa; the lift is to raise
both together. The single dimension most worth lifting is **Agent input**
(toward specs), because it is also the L3→L4 ceiling for the cognitive
read.

## Strengths

1. **The reflection→promotion loop actually runs end to end.**
   `REFLECTION_LOG.md` has two entries, both with verified `Promoted`
   lines into `AGENTS.md` and `HARNESS.md` — the compound-learning cycle
   is demonstrated, not just declared.
2. **Policy-as-code governance.** Two required status checks (the TDAB
   suite and a changelog gate) block merges on a protected `main`, and a
   changelog-driven release workflow publishes versioned releases
   automatically.
3. **Rich, synchronised context.** HARNESS / AGENTS / ONBOARDING and the
   Cursor / Copilot / Windsurf convention files are kept in lockstep, and
   a 22-page Diátaxis docs site is published to Pages.

## Gaps

1. **No specifications layer.** No `specs/`, no spec-first ordering, no
   adversarial spec review — the L3→L4 ceiling. Intent is implicit in PR
   prose.
2. **Verification depth is shallow.** The automated tests assert
   *structure* against committed sample assessments; behavioural and
   semantic checks (does the assessment actually behave correctly) are
   manual. Testing sits at L2 (Asserting).
3. **No agent composition or observability for development.** A single
   agent, no read-only critics/orchestrator on PRs, and no observability
   of agent activity or cost.

## Prioritised Improvement Plan

Ranked by what most moves you toward Level 4 (Orchestrating). *Team
develops* = practice the team builds; *Org provides* = enablement the
organisation supplies.

1. **Introduce a lightweight specifications layer** *(team develops →
   Architectural guidance)*. A one-paragraph spec atop substantive PRs,
   graduating into a `specs/` directory, with an adversarial "what could
   go wrong" review. Closes the L3→L4 ceiling at near-zero cost.
2. **Deepen verification beyond structural assertions** *(team develops →
   Guardrails)*. Behavioural checks (golden-output / LLM-judge for the
   B/C tiers) move Testing from *Asserting* to *Verifying*.
3. **Add a read-only critic and basic observability** *(org provides →
   Agent readiness)*. A review-agent touchpoint on PRs plus simple
   agent-activity / cost capture lift two L2 dimensions.

## Reading Path

Your assessed level is **L3 — Habitat design**. The natural next read in
*The Sovereign Engineer* is the **Level 4 (specifications) chapter** —
your habitat is in place; the next leverage is making intent first-class,
separating "what we're trying to do" from "how we're doing it".

Get the book: <https://leanpub.com/thesovereignengineer/c/ai-readiness>

## Next Steps

> Your habitat is healthy at L3, and the L3→L4 jump is about making
> specifications first-class. If you'd like help making that jump,
> TechTalk can support a **specification-first engagement** — guided work
> that introduces a `specs/` layer wired into your existing `HARNESS.md`
> and CI, an adversarial-review touchpoint at plan approval, and a small
> set of orchestration patterns so agents act on specs rather than ad-hoc
> instructions. The most common starting points for teams at your level:
>
> - a one-paragraph spec at the top of each substantive PR, graduating
>   into a `specs/` directory;
> - an adversarial "what could go wrong with this spec" review before
>   implementation begins.
>
> Get in touch: <https://techtalk.ai>
