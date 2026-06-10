# AI Readiness Assessment — ai-readiness-assessment (re-assessment)

**AI Readiness — Habitat Maturity**: Level 3 (Regulating)
**Next Step / Gap**: +1.1 to Level 4 (Orchestrating)

**Habitat Build Gap**: +1.1 (Ambition outpaces enablement)   <!-- coherence (cognitive − operational); secondary -->
**Assessed level**: Level 4 — Specification-led   <!-- cognitive read; do not remove -->
**Date**: 2026-06-03

> **Note**: a re-assessment of the plugin against **its own repository**,
> after spec-first was made an enforced discipline (specs 0001–0003, the
> Spec-first constraint + gate). It is the progression follow-up to
> [`2026-06-03-assessment.md`](2026-06-03-assessment.md). Clarifying
> answers come from maintainer knowledge.

## What changed since the baseline

The baseline assessment ([`2026-06-03-assessment.md`](2026-06-03-assessment.md))
read a **coherent L3**, with the absence of a specifications layer as the
L3→L4 ceiling. Since then:

- A `specs/` layer with three specs (0001 scaffolding; 0002 a real
  change-driving spec; 0003 a real product-decision record).
- **Spec-first promoted from convention to an enforced constraint**,
  backed by a required **Spec-first gate** (instrument changes must carry
  a spec).
- An **Adversarial review** disposition added to the spec format — a
  lightweight plan-approval review.

## AI Readiness Score — five readiness dimensions

A view over the same evidence (the headline level is the 14-dimension
Habitat Maturity):

| Readiness dimension | Level | Δ vs baseline | Evidence |
|---|---|---|---|
| Context | L4 | — | HARNESS Context, AGENTS, ONBOARDING, synced conventions, docs |
| Conventions | L4 | — | HARNESS conventions, synced convention files |
| Architectural guidance | L4 | **L3 → L4** | `specs/` + spec-first enforced (constraint + gate) |
| Guardrails | L3 | — | TDAB + four required CI gates; Testing / Observability still L2 |
| Agent readiness | L2 | — | Single agent; no read-only critics or orchestration |

## Habitat Document Discovery (delta)

| Document type | Path | Result |
|---|---|---|
| Specifications | `specs/` (README, TEMPLATE, 0001–0003) | **found** (was absent) |
| Spec-first enforcement | `HARNESS.md` constraint + `.github/workflows/spec-first-gate.yml` (required) | **found** (was absent) |
| Adversarial review | `Adversarial review` disposition in each spec | **found** (was absent) |
| Orchestration acting on specs | agent orchestration / `docs/objections/` | **not found** |

## Level Assessment

**Level 4 — Specification-led (freshly crossed).**

Rationale: the L3 ceiling — no specifications layer — has been genuinely
addressed. Specs are now first-class (`specs/`), spec-first ordering is
**enforced** (a required CI gate, not just a convention), and each
substantive spec carries an adjudicated adversarial review at the
plan-approval (PR) gate. All three disciplines now clear L4.

Honest caveats: this is a **narrowly-crossed** L4. The spec practice is
young (three specs, two about the spec system itself), the adversarial
review is lightweight (a disposition + human PR review, not a dedicated
adversarial agent or self-verifying executable specs), and the one L4
signal still absent is **orchestrated multi-step agent workflows acting
on specs** (an L4→L5 edge). The discipline is installed and enforced; the
track record will thicken with use.

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence | Δ |
|---|---|---|---|
| Context Engineering | 4 | HARNESS / AGENTS / ONBOARDING, synced conventions, reflection→promotion loop, docs site | — |
| Architectural Constraints | 4 | 4 constraints (3 enforced) + **4 required CI gates** (tests, changelog, onboarding, spec-first) = policy-as-code; spec-first ordering enforced | 3 → **4** |
| Guardrail Design | 4 | TDAB + four CI gates + **adversarial review at the plan-approval gate** | 3 → **4** |

## Habitat Maturity Profile (Agentic Experience 5-Level Habitat Maturity Model)

| Dimension | Level | Stage (verb) | Δ vs baseline |
|---|---|---|---|
| Agent behaviour | L3 | Regulating | — |
| Agent input | L3 | plans / specs co-authored | **L2 → L3** (specs, spec-first) |
| Workflow | L4 | workflow defined | — |
| Operating model | L3 | drive / verify | — |
| Teams provide | L3 | comprehensive constitution | — |
| Output role | L3 | Standardising | — |
| Output artefact | L3 | process & consistency rules | — |
| Humans review | L3 | implementation detail (+ specs) | — |
| Work patterns | L3 | e2e development | — |
| Agent composition | L2 | single + saved patterns | — |
| Agents… | L3 | Develop (stories) | — |
| Testing | L2 | Asserting | — |
| Observability | L2 | Captured | — |
| Governance | L4 | Policy-as-code | **L3 → L4** (required gates, spec-first) |

**Habitat Maturity Level**: L3 (mean L2.93; weakest: L2 Testing, Observability, Agent composition)

## Operational Axes (Part D)

| Axis | Level | Δ |
|---|---|---|
| Composition | L2 | — |
| Testing | L2 | — |
| Observability | L2 | — |
| Governance | L4 | L3 → **L4** |

**Headline axes mean**: L2.5

## Habitat Build Gap

    Habitat Maturity Level (model):  L3  (14-dim mean L2.93)
    Cognitive read (Parts A–C):      L4
    Habitat Build Gap:               +1.07   (cognitive − 14-dim mean)
    Interpretation:                  Ambition outpaces enablement

This is the headline of the progression. Lifting the **spec discipline**
to L4 moved the cognitive read up — but the broader operational habitat
(Testing, Observability, Agent composition still L2) did not move with
it. So the repo, **coherent at the baseline (+0.2)**, is now
**incoherent (+1.07)**: its thinking has outrun its enablement. That is
not a regression — it is the expected, healthy consequence of a
deliberate discipline jump, and it names the next work precisely.

## Strengths

1. **Spec-first is now lived and enforced**, not aspirational — a
   required gate makes instrument changes carry a spec, and each spec is
   adversarially reviewed at plan approval.
2. **Policy-as-code governance** — four required CI gates block merges on
   a protected `main`.
3. The progression itself was executed **spec-first** (spec 0002 drove
   its own change) — the discipline is already self-applying.

## Gaps

1. **Operational habitat lags the discipline** — Testing (Asserting),
   Observability (Captured), and Agent composition (single) are still L2,
   producing the +1.1 ambition-outpaces-enablement gap.
2. **Thin spec practice** — three specs, two about the spec system; the
   "specification-led" reality needs a track record of specs driving
   real product changes.
3. **No orchestration acting on specs** — the L4→L5 edge.

## Prioritised Improvement Plan

The gap regime flipped to ambition-outpaces-enablement, so the plan is to
**build the habitat your thinking now implies** — lift the lagging
operational dimensions toward Level 4 (Orchestrating). *Team develops* =
practice the team builds; *Org provides* = enablement the organisation
supplies.

1. **Lift Testing off L2** *(team develops → Guardrails)* — behavioural /
   semantic verification (golden-output or an LLM-judge harness for the
   B/C tiers): *Asserting → Verifying*.
2. **Lift Observability off L2** *(org provides → Guardrails)* — capture
   agent-activity / cost signals so the collaboration is measured.
3. **Lift Agent composition off L2** *(org provides → Agent readiness)* —
   a read-only critic on PRs, toward a primary-plus-critic topology.

## Next Steps

> Your spec discipline has reached L4, but the gap is now **+1.1 —
> ambition outpaces enablement**: the habitat needs to catch up to the
> thinking. TechTalk can support a **habitat-build engagement** focused
> on the lagging operational axes — verification depth, observability,
> and agent composition — so the environment delivers what your L4
> specifications already imply. The most common starting points for teams
> at your level:
>
> - a behavioural test harness (golden-output / LLM-judge) for the
>   work agents produce;
> - a read-only critic agent on PRs and basic agent-activity observability.
>
> **[Book a call with TechTalk](https://outlook.office.com/bookwithme/user/129484fb9c5648688428890bc72c1ee7@techtalk.at?anonymous&ismsaljsauthenabled&ep=pcard)** · thomas.stangl@techtalk.at
>
> *Prefer to explore on your own first? The Reading Path below names your
> matched chapter of The Sovereign Engineer.*

## Reading Path

*Prefer to go deeper on your own first? Here is your matched read — the
self-guided alternative to the engagement above.*

Assessed at **L4 — Specification-led**. The next read in *The Sovereign
Engineer* is the **Level 5 (systems and orchestration)** chapter — specs
are in place; the next leverage is platform discipline and agents that
orchestrate around those specs.

Get the book: <https://leanpub.com/thesovereignengineer/c/ai-readiness>
