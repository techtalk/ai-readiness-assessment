# AI Readiness Assessment — ai-readiness-assessment (re-assessment)

**AI Readiness — Habitat Maturity**: Level 4 (Orchestrating)
**Next Step / Gap**: +1.4 to Level 5 (Supervising)

**Habitat/Workflow Gap**: +0.36 (Coherent)   <!-- coherence (cognitive − operational); secondary -->
**Assessed level**: Level 4 — Specification-led   <!-- cognitive read; do not remove -->
**Date**: 2026-08-16

> **Note**: a re-assessment of the plugin against **its own repository**,
> 74 days after [`2026-06-03-assessment-2.md`](2026-06-03-assessment-2.md)
> and immediately after the v1.0.0 release. Clarifying answers come from
> the maintainer. The previous report read **+1.07 — Ambition outpaces
> enablement**; its own prescription was to lift the operational habitat
> alongside the discipline. This report tests whether that happened.

## Habitat Document Discovery

| Document | Status | Path | Markers matched |
| --- | --- | --- | --- |
| `HARNESS.md` | Found, conventional | `HARNESS.md` (202 lines) | `## Context`, `## Constraints`, `## Garbage Collection`, `## Observability`, `## Status`; five four-field constraint blocks (Rule / Enforcement / Tool / Scope) |
| `AGENTS.md` | Found, conventional | `AGENTS.md` (153 lines) | Six sections; STYLE / conventions / architecture decisions |
| Copilot instructions | Found, conventional | `.github/copilot-instructions.md` (91 lines) | Synced convention surface |
| Cursor rules | Found | `.cursor/rules/` (constraints.mdc, conventions.mdc) | Synced convention surface |
| Windsurf rules | Found | `.windsurf/rules/` (constraints.md, conventions.md) | Synced convention surface |
| Specifications | Found | `specs/` (11 numbered specs + `TEMPLATE.md`, `README.md`) | Numbered `NNNN-slug.md`; Intent / Design / Alternatives / Risks / **Adversarial review** / Acceptance |
| Reflection log | Found | `REFLECTION_LOG.md` (73 lines) | Dated entries with Task / Surprise / Proposal |
| Onboarding | Found | `ONBOARDING.md` (254 lines) | Generated human-readable guide |
| `CLAUDE.md` | **Not found** | — | Absent at root; `.claude/` is gitignored |
| `CONSTRAINTS.md` | **Not found** | — | Superseded by `HARNESS.md` |
| `CHOICES.md` / decision records | **Not found** | — | No `docs/adr/`, `docs/decisions/`, or story records |
| `MODEL_ROUTING.md` | **Not found** | — | No cost or model-routing discipline recorded |
| `observability/` | **Not tracked** | — | Untracked and gitignored as of PR #62 (local agent telemetry) |

No ambiguities. Both alternative-path candidates (`.cursor/`, `.windsurf/`)
were checked and found.

## Observable Evidence

| Signal | Found | Evidence |
| --- | --- | --- |
| Saved commands | yes | `commands/ai-readiness-assess.md`, `commands/ai-readiness-rollup.md` |
| Product-specific skills | yes | `skills/ai-readiness-assessment/`, `skills/ai-readiness-rollup/` |
| CI encoding the process | yes | 6 workflows; 4 required gates (A-tier assertions, spec-first, changelog, onboarding) plus release and pages |
| Test suite | yes | `tests/run.py` — **111 assertions**, 6 fixtures (L0–L5), 29 repo-level checks, zero dependencies |
| Coverage / mutation enforcement | **no** | No coverage threshold, no mutation testing |
| Specs layer | yes | 11 specs; spec-first gate is deterministic (ordering) + agent (review adjudication) |
| Adversarial review | yes | Every spec carries a disposition; spec 0011 records four objections and their resolutions |
| Custom agents | **no** | No `agents/` directory; no critic or orchestrator agents |
| Agent-activity logging | **no** | `observability/` untracked; `HARNESS.md` `## Observability` is four "Not yet configured" placeholders |
| Metrics / cost capture | **no** | No token, latency or cost capture; no `MODEL_ROUTING.md` |
| Governance audit cadence | **stale** | `HARNESS.md` Status: last audit **2026-06-03** — 74 days ago; "Drift detected: no" |
| Published artefact | yes | `techtalkai` marketplace entry; **v1.0.0** released 2026-08-15 |
| Portfolio-level artefacts | yes | `/ai-readiness-rollup`, portfolio report structure, four published portfolio examples incl. one real |

### Two documentation drifts found

Both understate the repo rather than flatter it, and both are recorded
here because the instrument scores what is *true*, not what is written:

- **`HARNESS.md` Status is 74 days stale.** It reports "Constraints
  enforced: 4/5" and "Drift detected: no" as of 2026-06-03. The
  dual-surface parity constraint is described as verifiable by "a
  reviewer … diffing the agreed framework sections" — i.e. **agent**
  enforcement. It is now **deterministic**: assertions `R1` and `R6`
  compare both surface pairs on every CI run. The real enforcement ratio
  is higher than the document claims.
- **`specs/README.md` says spec-first is "currently a convention … not
  yet an enforced constraint."** A required `spec-first-gate.yml` has
  been enforcing it on every PR since spec 0002.

## Clarifying Responses

Four questions were spent on the six behavioural dimensions; the
remaining two were inferred from the answers and from the repo-observable
placements.

| Question | Answer | Places |
| --- | --- | --- |
| Working relationship with the agent? | **Supervising — I certify outcomes** | Agent behaviour → L5 |
| What do you inspect before accepting? | **Specs — I review intent, tests carry the rest** | Humans review → L4 |
| How much of a unit of work does the agent carry? | **Semi-autonomous — a whole slice, with checkpoints** | Work patterns → L4 |
| Primary act on the output? | **Specifying — I define what it must satisfy** | Output role → L4 |

*Inferred, not asked*: **Operating model** → L4 (humans in the loop —
"with checkpoints" places this below *certify*), and **Agents…** → L4
(implementing larger changes/epics — the agent carried six vertical
slices from failing tests to merged PR, but at set decision points
rather than autonomously).

## AI Readiness Score — five readiness dimensions

| Readiness dimension | Level | Drawn from | Evidence |
|---|---|---|---|
| Context | L4 | Context Engineering; Teams provide; instruction files | Four synced convention surfaces (AGENTS, Copilot, Cursor, Windsurf), ONBOARDING.md, HARNESS Context; no root CLAUDE.md |
| Conventions | L4 | HARNESS Conventions; synced convention files | Convention sync across four tools; onboarding gate enforces currency |
| Architectural guidance | L4 | Architectural Constraints; specs; constraints | 11 specs, adversarial review in every one, spec-first gate required on main |
| Guardrails | L3 | Guardrail Design; Testing; Observability; CI gates | 111 assertions + 4 required gates, but no coverage/mutation enforcement and no observability at all |
| Agent readiness | L3 | Agent composition; Workflow; Agents… | Workflow L4 and Agents… L4, dragged by single-agent composition (L2) |

## Habitat Maturity Profile (Agentic Experience 5-Level Habitat Maturity Model)

All fourteen dimensions, each placed L1–L5 with the model's verb.
Behavioural dimensions placed without direct evidence are tagged
*(inferred)*.

| Dimension | Level | Stage (verb) | Evidence / basis |
|---|---|---|---|
| Agent behaviour | L5 | Supervising | Maintainer certifies outcomes rather than driving execution *(asked)* |
| Agent input | L4 | iteratively refined specs | Spec 0011 refined across six slices, acceptance ticked per slice |
| Workflow | L4 | workflow defined | 6 CI workflows encode the process; 4 required gates. Not L5 — no scheduled or self-triggering runtime |
| Operating model | L4 | humans in the loop | *(inferred)* — checkpoints per slice, not certification-only |
| Teams provide | L3 | comprehensive product-specific constitution | Four synced surfaces + ONBOARDING; no custom runtime, no root CLAUDE.md |
| Output role | L4 | Specifying | Maintainer's primary act is defining what the output must satisfy *(asked)* |
| Output artefact | L4 | clear criteria | Every spec carries explicit Acceptance; slice PRs tick them. Not L5 — no evidence/audit bundles |
| Humans review | L4 | specs | Intent reviewed; suite and gates carry implementation detail *(asked)* |
| Work patterns | L4 | semi-autonomous work | Whole slices carried end to end with checkpoints *(asked)* |
| Agent composition | **L2** | single + saved patterns | Two commands + two skills; **no custom agents, no critics, no orchestrator** |
| Agents… | L4 | Implement larger changes (epics) | *(inferred)* — six vertical slices, each spec→red→green→docs→PR |
| Testing | L3 | Verifying (functional / business) | 111 assertions over 6 behavioural fixtures asserting report structure; required CI gate. Not L4 — no coverage or mutation enforcement, B/C tiers manual |
| Observability | **L2** | Captured | `tests/auto-results.md` regenerated and committed each run. **Nothing captures agent activity, tokens or cost**; HARNESS Observability unconfigured |
| Governance | L4 | Policy-as-code | 5 falsifiable constraints, 4 required CI gates, branch protection. Not L5 — audit cadence stale at 74 days |

**Habitat Maturity Level**: Level 4 (model) — mean L3.64; held back by
L2 Agent composition and L2 Observability. This fourteen-dimension mean
(L3.64) is the Habitat/Workflow Gap's operational term.

## Level Assessment

**Level 4 — Specification-led.**

Specs are first-class and enforced: a `specs/` directory with eleven
numbered specs, spec-first ordering gated in CI, adversarial review
recorded as a disposition in every one, and — in spec 0011 — a spec that
was genuinely refined across six increments rather than written once and
abandoned.

The cognitive read does **not** reach L5. Three of the six L5 markers
are present: a **published plugin** (v1.0.0 on the `techtalkai`
marketplace), **fitness functions in CI**, and **portfolio-level
assessment artefacts**. Three are absent: **governance audit cadence**
(last audit 74 days ago), **decision archaeology** (no `CHOICES.md` or
story records — the specs' *Alternatives considered* sections are the
closest thing), and **cost / model-routing discipline** (nothing at all).

By the scoring heuristic the weakest discipline is the ceiling, and two
tie at 4.

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 4 | Four synced convention surfaces, ONBOARDING.md, HARNESS Context, reflection log. Held below 5 by a moderate constitution (AGENTS.md at 153 lines) and no curation cadence |
| Architectural Constraints | **5** | Specs first-class and CI-enforced; adversarial review in every spec; constraints falsifiable and machine-checked; spec 0011 demonstrably drove six slices |
| Guardrail Design | 4 | 111 assertions and four required gates — but **no feedback loop from running agents**: observability unconfigured, no cost or model-routing signal, audit cadence stale |

Context Engineering and Guardrail Design tie as the ceiling at 4.

## Operational Axes (Part D)

The four discipline-aligned headline dimensions, lifted from the profile
above — a discipline-aligned view (the Habitat/Workflow Gap uses all
fourteen dimensions, not just these four).

| Axis | Level (L1–L5) | Evidence |
|---|---|---|
| Composition | L2 | Two commands + two skills; no agents |
| Testing | L3 | 111 assertions, 6 fixtures, required gate |
| Observability | L2 | Test results captured; no agent-activity signal |
| Governance | L4 | Policy-as-code, 4 required gates, stale audit |

**Headline axes mean**: L2.75 — a focused, discipline-aligned view; the
Habitat/Workflow Gap uses all fourteen dimensions

## Habitat/Workflow Gap

    Habitat Maturity Level (model):  L4  (14-dim mean L3.64)
    Cognitive read (Parts A–C):      L4
    Habitat/Workflow Gap:            +0.36   (cognitive − 14-dim mean)
    Interpretation:                  Coherent

The gap has closed from **+1.07 to +0.36** — from *Ambition outpaces
enablement* back to **Coherent**, and at a higher level on both reads.
The habitat caught up with the thinking, which is exactly what the June
report prescribed.

But read *how* it closed. Of the three dimensions June named as the
ceiling — Agent composition, Testing, Observability — **only Testing
moved** (L2 → L3). The other two are still at L2 and are still the
ceiling. Coherence was restored by everything *else* rising: the
behavioural read climbed six levels across five dimensions as the
working practice shifted to supervising whole slices, and Agent input
and Output artefact each gained a level from the specs work.

That is a real and healthy result, but it is not the same as fixing what
was named. The two dimensions flagged in June are the two dimensions
flagged now.

## Strengths

1. **Specs genuinely drive the work.** Spec 0011 was written before
   implementation, refined across six slices, and its Acceptance section
   ticked as each landed. Eleven specs, adversarial review in every one,
   spec-first gated in CI. This is the strongest discipline at 5.
2. **The suite grew 54% and caught real defects.** 72 → 111 assertions,
   every one written red-first. The parity assertion caught surface
   drift within minutes of being written; the no-portfolio-score guard
   fired on its own author's prose; a link check caught a broken
   internal link before it deployed.
3. **The instrument now has multi-repo scope and a real published
   example.** v1.0.0 ships subject × habitat, provenance and binding,
   portfolio regimes, and a real estate roll-up published exactly as it
   came out — including the fact that it produces no spread.

## Gaps

1. **Agent composition is L2 and has not moved since the baseline.**
   Two commands and two skills, no critic, no orchestrator, no
   read-only reviewer. Every check in this repo is a script or a human;
   nothing in the habitat reviews the work as an agent.
2. **Observability is L2 and is the least-evidenced placement in this
   report.** Nothing captures agent activity, tokens, latency or cost.
   `HARNESS.md`'s own Observability section is four "Not yet configured"
   placeholders, and the one agent-telemetry artefact that existed was
   deliberately untracked in PR #62. The L2 placement rests entirely on
   `tests/auto-results.md`; for *agent* activity specifically the honest
   reading is L1.
3. **The governance loop has stopped closing.** The audit is 74 days
   stale, and in that window the harness drifted twice in its own
   favour — the parity constraint became deterministic and spec-first
   became enforced, and neither document was updated. Understating
   enforcement is benign; a Status block nobody refreshes is not.

## Prioritised Improvement Plan

Ordered by what closes the L4→L5 platform gap, which is now the binding
constraint.

1. **Install a governance audit cadence** *(org-provides)* — the single
   cheapest L5 marker. The machinery exists; the Status block is 74 days
   old. Schedule it and let it correct the two drifts already found.
   Lifts Governance toward L5.
2. **Add a read-only critic agent** *(team-develops)* — the one move
   that lifts Agent composition off L2, where it has sat across two
   assessments. A reviewer agent with no write access, run on PRs,
   converts the harness from scripts-and-humans to primary-plus-critic.
3. **Capture agent activity** *(team-develops)* — token, latency and
   cost per session, and an `observability/` snapshot at a cadence.
   This is the dimension with the weakest evidence in the whole profile
   and the one blocking Guardrail Design from 5.
4. **Add `MODEL_ROUTING.md` and cost discipline** *(org-provides)* —
   named explicitly as an L5 marker and entirely absent.
5. **Start decision archaeology** *(team-develops)* — a `CHOICES.md` or
   story records. The specs' *Alternatives considered* sections are
   most of the way there; they are just not addressable as a record.
6. **Refresh `specs/README.md` and the HARNESS Status block**
   *(team-develops)* — both understate the repo. Cheap, and they are
   what a reader meets first.

## Next Steps

The gap is now **+0.36 — Coherent**: the habitat has caught up with the
thinking, and both reads sit at L4, so nothing here is out of step with
itself. The constraint is no longer coherence but **altitude** — the
L4→L5 platform layer, where three of six markers are present (a
published plugin, fitness functions, portfolio artefacts) and three are
missing (governance audit cadence, decision archaeology, cost and
model-routing discipline). TechTalk can support a **platform-engineering
engagement** on those three, together with the two dimensions that have
now been the ceiling across two consecutive assessments — Agent
composition and Observability — so that the next level is reached by
lifting what was named rather than by everything else rising around it.

Your assessment shows where your repository is today. A review helps you
understand why these findings matter, which improvements will have the
biggest impact, and what should come next.

## Assessment Review

> ### Not sure what these results mean?
>
> Your assessment tells you **where** you are. A review helps you
> understand **why** you received these scores and **what to do next**.
>
> **Review your results with Russ Miles**
> *Creator of the AI Readiness Assessment | Author of
> [The Sovereign Engineer](https://leanpub.com/thesovereignengineer/c/ai-readiness)*
>
> For one hour, you'll review your report together, discuss the reasoning
> behind the findings, and identify the highest-leverage improvements for
> your organisation.
>
> **After 60 minutes you'll leave knowing**
>
> - which findings actually matter
> - where to invest first
> - what can wait
> - how to explain the results internally
>
> **[Book your AI Readiness Review](https://outlook.office.com/bookwithme/user/f16fa59374724894aebc49506ac9bc20@techtalk.at?anonymous&ismsaljsauthenabled)**
>
> *Prefer exploring on your own first? The Reading Path below names your
> matched chapter of
> [The Sovereign Engineer](https://leanpub.com/thesovereignengineer/c/ai-readiness).*

## Reading Path

Prefer to go deeper on your own first?

Your weakest disciplines are **Guardrail Design** and **Context
Engineering**, tied at 4 — but the binding constraint is altitude, not a
single discipline. In
*[The Sovereign Engineer](https://leanpub.com/thesovereignengineer/c/ai-readiness)*,
**Level 5 — systems and orchestration** is the matched chapter: specs
are already in place here, and the next move is platform discipline
across teams. Read it alongside the Level 3 chapter on harness
engineering for the observability and critic-agent work that Guardrail
Design needs.

```yaml assessment-summary
schema: 1
subject: ai-readiness-assessment
subject_path: .
team: ai-readiness-assessment
habitat: self
posture: active
assessed_at: 2026-08-16
tool_version: 1.0.0

dimensions:
  agent_behaviour:   { level: 5, confidence: asked, provenance: local }
  agent_input:       { level: 4, confidence: observed, provenance: local }
  workflow:          { level: 4, confidence: observed, provenance: local }
  operating_model:   { level: 4, confidence: inferred, provenance: local }
  teams_provide:     { level: 3, confidence: observed, provenance: local }
  output_role:       { level: 4, confidence: asked, provenance: local }
  output_artefact:   { level: 4, confidence: observed, provenance: local }
  humans_review:     { level: 4, confidence: asked, provenance: local }
  work_patterns:     { level: 4, confidence: asked, provenance: local }
  agent_composition: { level: 2, confidence: observed, provenance: local }
  agents_do:         { level: 4, confidence: inferred, provenance: local }
  testing:           { level: 3, confidence: observed, provenance: local }
  observability:     { level: 2, confidence: observed, provenance: local }
  governance:        { level: 4, confidence: observed, provenance: local }

habitat_maturity_mean: 3.64
habitat_maturity_level: 4
cognitive_level: 4
cognitive_source: subject
gap: +0.36
regime: coherent
ceiling_dimensions: [agent_composition, observability]
weakest_discipline: guardrail-design
```
