# Spec 0005: Align report language with the AI Readiness mockup

- **Status**: implemented
- **Date**: 2026-06-03
- **PR**: (this PR)

## Intent

Bring the assessment's reporting language into line with the public
landing-page copy (the "AI Readiness" mockup), so what a visitor reads
and what the report says use the same words — without unwinding the
underlying fourteen-dimension model.

## Design

Three changes, all to the report's *language*, not its scoring:

1. **Headline metric** — show both the public and model terms:
   `AI Readiness — Habitat Maturity: Level N (Verb)`. The verb is the
   level archetype (Dictating · Commanding · Regulating · Orchestrating ·
   Supervising). The `Next Step / Gap` line is unchanged.
2. **AI Readiness Score breakdown** — add a public-facing summary across
   the mockup's **five readiness dimensions**, mapped from the existing
   data (the 14-dim model + 3 disciplines stay underneath, unchanged):
   - **Context** — instruction/context files and their richness
     (Context Engineering; Teams provide).
   - **Conventions** — coding/working conventions encoded and synced
     (HARNESS Conventions; the convention files).
   - **Architectural guidance** — structural rules and intent made
     first-class (Architectural Constraints; specs; constraints).
   - **Guardrails** — feedback loops that catch drift (Guardrail Design;
     Testing; Observability; CI gates).
   - **Agent readiness** — agent topology and workflow (Composition;
     Workflow; Agents…).
   Each placed L1–L5. It is a *view* over the same evidence, not a new
   scoring model; the headline level remains the 14-dimension Habitat
   Maturity mean.
3. **Output 2 → "Prioritised Improvement Plan"** — reframe Recommendations
   as a ranked list of what to build first to reach the next level,
   ordered by **what the team needs to develop** and **what the
   organisation needs to provide** (the latter maps to the model's
   *Teams provide* dimension).

## Alternatives considered

- **Replace the 3-discipline / 14-dim model with the five dimensions.**
  Rejected — unwinds the deliberate model spine; the five dimensions are
  a public summary, not the authoritative scoring.
- **Rename "Habitat Maturity" to "AI Readiness" outright.** Rejected —
  the maintainer chose to show both, keeping the model term visible.

## Risks / what could go wrong

- **The five-dimension view won't exactly equal the 14-dim mean** (it
  aggregates differently), so a reader may wonder why the breakdown looks
  stronger than the headline level. Mitigation: state plainly that it is
  a readiness *view*, and that the headline level is the 14-dimension
  Habitat Maturity.
- **Two metric terms in the headline read as clutter.** Mitigation: keep
  it to one line; the `Next Step / Gap` line stays single-purpose.

## Adversarial review

- **Reviewer**: PR reviewer (human, at merge)
- **Disposition**: accepted
- **Notes**: The five-dimension/14-dim aggregation mismatch was accepted
  as inherent to a summary view and addressed with an explicit note in
  the report and docs.

## Acceptance

- Instrument (command + skill, in sync) leads with
  `AI Readiness — Habitat Maturity: Level N (Verb)`, includes the
  five-readiness-dimension breakdown, and reframes Output 2 as the
  Prioritised Improvement Plan.
- The two committed example reports (md + HTML) are regenerated to match.
- `docs/reference/assessment-output.md` describes the new sections.
