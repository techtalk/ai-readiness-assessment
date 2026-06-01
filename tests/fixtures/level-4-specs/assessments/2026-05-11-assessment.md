# AI Literacy Assessment — wordcount (level-4-specs fixture)

**Date**: 2026-05-11
**Assessed level**: Level 4 — Specification-led
**Habitat Build Gap**: +0.75 (Ambition outpaces enablement)

> **Test-run note**: batch mode, clarifying questions skipped.

## Habitat Document Discovery

| Document type | Path | Result | Markers |
|---|---|---|---|
| AI-instruction file (rich) | `CLAUDE.md` | found | Project context, conventions, full spec-first workflow, skills + commands index. |
| Constraint document | `HARNESS.md` | found | Context / Constraints / Garbage Collection / Status. 7 constraints (5 deterministic, 2 agent); includes spec-first-ordering and spec-conformance. 3 GC rules including spec freshness. |
| Reflection log | `REFLECTION_LOG.md` | found | Three dated entries, including spec-first surfacing ambiguity (2026-04-22) and orchestrator catching a corner case (2026-05-03). |
| Onboarding | `ONBOARDING.md` | found | Spec-first workflow steps explicit. |
| Decision record | `docs/adr/0001-python-3-10-minimum.md` | found | One ADR. |
| Custom skill | `skills/wordcount-style/SKILL.md` | found | Project-local; frontmatter present. |
| **Specifications** | `specs/0001-newline-handling.md`, `specs/0002-empty-input.md` | **found** | Both carry frontmatter (id, title, status, created); "What / Why / Acceptance / Out of scope / Plan / Objections" structure. |
| **Plan separated from spec** | `specs/plans/0001-newline-handling-plan.md` | **found** | Separate file under `specs/plans/`; references parent spec by path. Approach / Steps / Risk / Verification structure. |
| **Adversarial reviews** | `docs/objections/0001-newline-handling.md`, `docs/objections/0002-empty-input.md` | **found** | All dispositions resolved (no `pending` values). Mix of `accepted`, `deferred`, `refuted` with reasons. |
| **Orchestrator command** | `commands/spec-implement.md` | **found** | Drives spec → plan → adversarial review → code with an explicit human-approval pause. |
| **Spec-first declaration** | `CONTRIBUTING.md` | **found** | Declares the spec-first rule; refers to `scripts/check-spec-first.sh`. |
| **PR template** | `.github/PULL_REQUEST_TEMPLATE.md` | **found** | Spec / Plan / Objections fields. |

The specifications layer is present and integrated.

## Observable Evidence

**Found:**

Full L3 habitat + L4 specifications layer (all listed above) + the L2
verification stack (`.github/workflows/ci.yml` with a
`spec-first-ordering` job alongside `lint-and-test`, `pytest`,
`pre-commit`, coverage threshold). Implementation files
(`src/wordcount/__init__.py`, `src/wordcount/main.py`) match the
specs (the `raise ValueError("count_words received empty input")`
matches Spec 0002 verbatim).

**Not found:**

- `.claude-plugin/plugin.json` — no published-plugin manifest. The
  team has not packaged its habitat for cross-team consumption.
- `MODEL_ROUTING.md` or cost-capture scripts — no model/cost
  discipline.
- `CHOICES.md` or full story-record archaeology directory — only one
  ADR.
- `audits/` directory — no governance audit cadence.
- Fitness-function rules in HARNESS.md (layer boundary, complexity
  hotspots, dependency age budget) — no fitness functions wired into
  CI either.
- Portfolio-level artefacts (cross-team templates, marketplace
  entries) — absent.

## Clarifying Responses

Skipped (batch test run). Plausible questions:

1. "Is the spec-first rule actually followed for small fixes, or
   only for new features?"
2. "Has the orchestrator command ever been overridden — code written
   without going through `/spec-implement`?"
3. "Are there decisions the team has made that should have landed in
   ADRs but are still implicit in PR descriptions?"

Not asked in this run.

## Level Assessment

**Level 4 — Specification-led.**

Rationale: the specifications layer is real and integrated — specs
under `specs/`, implementation plans separated into `specs/plans/`,
adversarial review records under `docs/objections/` with all
dispositions resolved, an orchestrator command (`/spec-implement`)
that drives the workflow with a human-approval pause, and a CI job
that enforces spec-first ordering. The reflection log shows the
spec-first practice has caught real ambiguity before code (entry
2026-04-22) and the orchestrator has caught a corner case the spec
missed (entry 2026-05-03) — the L4 pattern has been exercised, not
just declared.

The ceiling is the absence of L5 sovereign / platform-level
practice: no published habitat plugin for sibling teams, no
governance audit cadence, no decision archaeology (CHOICES.md or
story records), no fitness functions in CI, no model/cost-routing
discipline.

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 4 | Rich CLAUDE.md, ONBOARDING.md, custom skill, custom orchestrator command, two specs with frontmatter and structured "what/why/acceptance". Specs make intent first-class. No cross-team adoption mechanism yet. |
| Architectural Constraints | 4 | HARNESS.md with 7 constraints (5 deterministic, 2 agent), including spec-first ordering enforced in CI and a spec-conformance agent check. No fitness functions. |
| Guardrail Design | 4 | CI gate, pre-commit, test suite, coverage tripwire, **plus** adversarial review at plan approval — the L4 guardrail that catches drift before code. No fitness-function gates. |

## Operational Axes (Part D)

| Axis | Level (L1–L5) | Evidence |
|---|---|---|
| Composition | L4 | `/spec-implement` orchestrator drives a harness-composed workflow with a human-approval pause and adversarial review at plan approval — multi-agent workflow is first-class. |
| Testing | L3 | CI tests + coverage with tests-before-merge and functional coverage of critical paths. No system-level regression or agent-authored test suites. |
| Observability | L2 | REFLECTION_LOG records workflow catches and CI logs are searchable; no instrumented dashboards, acceptance metrics, or calibration data. |
| Governance | L4 | Spec-first ordering enforced deterministically in CI plus a spec-conformance agent check — policy-as-code with blocking rules; consistent with the L4 Architectural Constraints score. |

**Operational axes mean**: L3.25

## Habitat Build Gap

```text
Cognitive level (Parts A–C):     L4
Operational axes mean (Part D):  L3.25
  Composition:   L4
  Testing:       L3
  Observability: L2
  Governance:    L4
Habitat Build Gap:               +0.75
Interpretation:                  Ambition outpaces enablement
```

Spec-led cognition (L4) runs ahead of the operational mean (3.25). The axis most worth lifting is Observability — instrument agent activity and per-PR acceptance so the spec workflow's effects are measured, not just reflected on.

## Strengths

1. **Plan-and-objections separation.** Plans live next to specs but
   are separate files. Objection records carry dispositions with
   reasons. The team has built the most expensive-to-build L4
   pattern.
2. **The orchestrator command has paid for itself.**
   `REFLECTION_LOG.md` entry 2026-05-03 records the orchestrator
   catching a Windows-line-ending corner case the spec didn't
   mention. The L4 workflow has been verified by lived experience.
3. **CI enforces spec-first ordering deterministically.** The check
   isn't a convention people remember; it's a script that fails the
   build.

## Gaps

1. **No published habitat artefact.** The team's CLAUDE.md /
   HARNESS.md / spec-implement command set is excellent — but it
   lives only in this repo. Sibling teams have to read documentation
   and reproduce the pattern by hand.
2. **No governance audit cadence.** Constraints are declared but
   nobody periodically verifies they're still enforced as declared.
   Drift is invisible.
3. **No fitness functions, no model/cost discipline.** Architectural
   drift (layer boundaries, complexity) goes unchecked between major
   refactors. AI tool costs are not measured.

## Recommendations

1. **Package the habitat as a plugin.** Create
   `.claude-plugin/plugin.json`, scaffold a
   `/wordcount-habitat-init` adoption command, and have one sibling
   team install it. This is the highest-leverage L4→L5 move.
2. **Adopt a quarterly governance audit cadence.** Set up `audits/`
   and write the first audit checking each HARNESS.md constraint's
   declared vs. actual enforcement state. The audit will catch
   constraint drift before it ossifies.
3. **Start `CHOICES.md` with the decisions you've already made.**
   The spec-first rule, the orchestrator command, the
   plan-separation pattern — capture them as stories so a sibling
   team adopting the habitat sees the reasoning, not just the
   artefacts.

## Reading Path

Your assessed level is **L4 — Specification-led**. The natural next
read in *The Sovereign Engineer* is the **Level 5 (systems and
orchestration) chapter** — your specs are in place; the next move is
platform-level discipline across teams.

Get the book: <https://leanpub.com/thesovereignengineer>

## Next Steps

> Your habitat is healthy at L4 and the L4→L5 jump is about platform-
> level discipline. If you'd like help making that jump, TechTalk
> runs a **platform-engineering engagement**: a three-week piece of
> work that packages your habitat (`CLAUDE.md` skeleton, `HARNESS.md`
> constraint set, `/spec-implement` orchestrator, the
> `wordcount-style` skill, the CI workflow) as a published plugin
> with a `/wordcount-habitat-init` adoption command; installs a
> quarterly governance audit cadence with the first audit conducted
> alongside the team; and adds three CI-resident fitness functions
> (layer boundary, complexity hotspots, dependency age budget). One
> sibling team adopts the published plugin during the engagement so
> the cross-team transfer is verified, not theoretical.
>
> Get in touch: <https://techtalk.ai>
