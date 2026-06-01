# AI Literacy Assessment — wordcount (level-5-sovereign fixture)

**Date**: 2026-05-11
**Assessed level**: Level 5 — Sovereign engineering
**Habitat Build Gap**: +1.25 (Ambition outpaces enablement)

> **Test-run note**: batch mode, clarifying questions skipped.

## Habitat Document Discovery

The full L0–L4 stack is present (see L4 fixture for the inherited
discovery table — every L0–L4 artefact present there is also present
here). The L5 sovereign-layer additions:

| Document type | Path | Markers |
|---|---|---|
| **Published plugin manifest** | `.claude-plugin/plugin.json` | Plugin name `wordcount-habitat`, version 1.0.0, description names the published artefacts (CLAUDE.md skeleton, HARNESS.md constraint set, /spec-implement, wordcount-style, CI workflow). Adopt with `/wordcount-habitat-init`. |
| **Cross-team adoption command** | `commands/wordcount-habitat-init.md` | Documented six-step adoption process for sibling teams. |
| **Model routing discipline** | `MODEL_ROUTING.md` | Per-task-type routing rules with cost ceilings; quarterly spend history; capture cadence noted. |
| **Decision archaeology** | `CHOICES.md` | Five stories (C-001 through C-005), each with Context / Choice / Why / Alternatives / Verified-by. C-001 is verified by a real reflection-log entry. |
| **Governance audit cadence** | `audits/2026-Q1.md` | A real audit record: constraints-reviewed table with declared-vs-actual columns; **detected drift** (spec-conformance not running); corrective actions taken; next audit date set. |
| **Fitness functions** | `HARNESS.md` GC section + `.github/workflows/ci.yml` `fitness-functions` job | Three fitness functions wired into CI: layer boundary, complexity hotspots, dependency age budget. |
| **Sovereign-layer constraints** | `HARNESS.md` Constraints section | Added: "Choices captured" (agent), "Model-routing compliance" (agent + monthly audit). |

## Observable Evidence

**Found** (in addition to the full L4 stack):

- Published plugin (`wordcount-habitat`, v1.0.0).
- `/wordcount-habitat-init` adoption command.
- `MODEL_ROUTING.md` with routing rules and 2025-Q4 / 2026-Q1 spend
  history.
- `CHOICES.md` with five stories covering: habitat-as-plugin (C-001),
  quarterly governance audit cadence (C-002), CHOICES.md adoption
  (C-003), fitness functions in CI (C-004), model-routing exception
  for adversarial review (C-005).
- `audits/2026-Q1.md` — quarterly audit; caught real drift; actions
  recorded.
- Three fitness functions in CI (layer boundary, complexity hotspots,
  dependency age budget).
- HARNESS.md constraint set extended to include "Choices captured"
  and "Model-routing compliance".
- `REFLECTION_LOG.md` entries showing the L5 mechanisms in action:
  sibling adoption (2026-04-10), governance audit catching drift
  (2026-04-28), model-routing budget exception (2026-05-02).

**Not found:**

- No artefact above L5 (which is the top of the framework, so this
  is expected).
- One minor gap: `scripts/` directory referenced by HARNESS.md and
  CI (for `check-spec-first.sh`, `cost-capture.sh`, fitness-function
  scripts) is not present as files in the fixture — the references
  are declarations rather than implementations. Noted for honesty,
  not held against the level assessment.

## Clarifying Responses

Skipped (batch test run). Plausible questions for this fixture:

1. "How many sibling teams have installed `wordcount-habitat` so
   far, and how many are still using it?"
2. "Are the fitness-function thresholds (e.g. complexity > 10,
   libyear budget 12) reviewed periodically, or were they set once?"
3. "Has the governance audit ever found drift that the team chose
   *not* to fix? What was the reasoning?"

Not asked in this run.

## Level Assessment

**Level 5 — Sovereign engineering.**

Rationale: every platform-level signal is present and exercised. The
team's habitat is **published** as a Claude Code plugin with a real
adoption command, and a sibling team has installed it
(REFLECTION_LOG.md 2026-04-10 — verified, not aspirational). The
governance audit cadence is **running** with a real audit on file
that found and corrected drift (audits/2026-Q1.md and
REFLECTION_LOG.md 2026-04-28). Decision archaeology is **maintained**
— five stories in CHOICES.md, cross-referenced with the reflection
log and HARNESS.md. Fitness functions are **wired into CI**, not
declared on a roadmap. Model routing is **governed by an explicit
document and audited** for compliance.

The team is at the top of the published framework. The L5 question
is no longer "what's the next level?" — there isn't one — but
"how is this practice sustained over time, and how is it carried
across the wider organisation?".

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 5 | Rich CLAUDE.md + ONBOARDING.md + custom skill + custom commands + specs + MODEL_ROUTING + CHOICES (decision archaeology) + habitat **published as a plugin** for cross-team consumption. |
| Architectural Constraints | 5 | HARNESS.md with 9 constraints (5 deterministic, 4 agent), 7 GC rules (including 3 fitness functions and the governance-audit-cadence check), Status section recording a real audit on 2026-04-15. |
| Guardrail Design | 5 | CI with three jobs (spec-first-ordering, lint-and-test, fitness-functions), pre-commit hook, adversarial review at plan approval, governance audit at quarterly cadence — catches drift the PR-time gates miss. |

## Operational Axes (Part D)

| Axis | Level (L1–L5) | Evidence |
|---|---|---|
| Composition | L4 | Published habitat plugin + `/spec-implement` orchestrator with approval gates and adversarial review; humans still drive orchestration, so short of self-orchestrating constellations. |
| Testing | L3 | CI lint-and-test with coverage and tests-before-merge; no multi-perspective risk, prod-like, or agent-authored test plans. |
| Observability | L3 | Fitness functions in CI, a quarterly governance audit on file, and GC rules run at cadence — instrumented at known cadences, but not closed-loop or cross-team aggregated. |
| Governance | L5 | A running governance-audit cadence that found and corrected drift, policy-as-code constraints, and decision archaeology (CHOICES.md) carrying per-change compliance evidence — consistent with the L5 Architectural Constraints score. |

**Operational axes mean**: L3.75

## Habitat Build Gap

```text
Cognitive level (Parts A–C):     L5
Operational axes mean (Part D):  L3.75
  Composition:   L4
  Testing:       L3
  Observability: L3
  Governance:    L5
Habitat Build Gap:               +1.25
Interpretation:                  Ambition outpaces enablement
```

Even at sovereign cognition (L5) the operational mean (3.75) lags, driven by Testing and Observability. The axis most worth lifting is Testing — add multi-perspective risk and agent-authored test plans so verification matches the team's process sovereignty.

## Strengths

1. **The habitat-as-plugin pattern has crossed a real boundary.**
   C-001 in `CHOICES.md` records the decision; REFLECTION_LOG.md
   2026-04-10 records the verification (a sibling team adopted in
   two steps). This is the L5 cross-team transfer working in
   practice, not in theory.
2. **The governance audit is doing real work.** audits/2026-Q1.md
   found a drifted constraint (spec-conformance check not running)
   and recorded the corrective action. CHOICES.md C-002 captures the
   decision that put the audit cadence in place. This is the
   mechanism that keeps a long-lived harness honest.
3. **CHOICES.md, REFLECTION_LOG.md, and HARNESS.md are
   cross-referenced as a triple.** C-005 (model-routing exception)
   is verified by REFLECTION_LOG.md 2026-05-02; C-001 by
   REFLECTION_LOG.md 2026-04-10. The pattern-surfacing →
   decision-capture → constraint-promotion loop is fully closed.

## Gaps

1. **Scripts referenced but not implemented.** HARNESS.md and CI
   reference `scripts/check-spec-first.sh`, fitness-function
   scripts, and `scripts/cost-capture.sh`, but the files are not
   present in the fixture. This is a fixture-fidelity gap, not a
   habitat gap.
2. **Single-team adoption record.** REFLECTION_LOG.md 2026-04-10
   records one sibling-team adoption. Sustaining L5 means more than
   one adoption, and a maintenance playbook for the published
   plugin.
3. **No external dependency on the plugin.** The published plugin is
   inside this repo. To verify the cross-team artefact really works
   as a portable habitat, it would need to be consumed from
   somewhere else.

## Recommendations

1. **Open the governance audit cadence to a sibling team.** Conduct
   the next quarterly audit jointly with the team that adopted
   `wordcount-habitat`. The audit becomes a cross-team artefact, not
   only an internal one. The Q3 audit (next scheduled 2026-07-15) is
   the natural moment.
2. **Write a habitat maintenance playbook.** What happens when the
   plugin needs a breaking change? When a sibling team's CI provider
   doesn't match the workflow template? When a constraint set
   diverges across teams? The L5 question is "how does this
   practice sustain itself" and the maintenance playbook is the
   answer.
3. **Publish or share the habitat plugin beyond the immediate org.**
   The pattern is reproducible; a Claude Code marketplace entry, an
   internal package, or a public Git repo is the next sovereignty
   move.

## Reading Path

Your assessed level is **L5 — Sovereign engineering**. The natural
next read in *The Sovereign Engineer* is the **Enchiridion chapter**
— distilling the practice into a personal handbook — and the
**portfolio-scale chapters** that follow, on carrying the practice
across teams and over years.

Get the book: <https://leanpub.com/thesovereignengineer>

## Next Steps

> Your team is at L5 — the top of the published framework. The
> question is no longer "what's next" but "how is this sustained?".
> TechTalk runs a **portfolio-sovereignty engagement** for L5 teams:
> a two-week piece of work that (a) facilitates a cross-team
> governance audit with one sibling team, (b) drafts the maintenance
> playbook for your published habitat plugin (versioning, breaking-
> change protocol, support window), and (c) sets up the
> portfolio-level assessment artefact your team will use to track
> the next year's habitat health. The aim isn't a sixth level; it's
> compounding the practice you already have.
>
> Get in touch: <https://techtalk.ai>
