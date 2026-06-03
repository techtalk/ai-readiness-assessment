# Spec 0004: Lead the report with a simple two-line headline

- **Status**: implemented
- **Date**: 2026-06-03
- **PR**: (this PR)

## Intent

Make the assessment far more approachable at a glance: the report should
open with just **two outputs** — the current level and the next step —
before any detail, so a stakeholder gets the answer in one line each.

```
Current Habitat Maturity:  Level 3 (Regulating)
Next Step / Gap:           +1.1 to Level 4 (Orchestrating)
```

## Design

- **Current Habitat Maturity**: `Level N (<Verb>)`, where N is the
  rounded fourteen-dimension Habitat Maturity mean (unchanged definition)
  and `<Verb>` is the model's Agent-behaviour archetype for that level:
  L1 Dictating · L2 Commanding · L3 Regulating · L4 Orchestrating ·
  L5 Supervising.
- **Next Step / Gap**: `+X to Level N+1 (<NextVerb>)`, where X =
  `(N+1) − maturity_mean`, to one decimal — the distance to the next
  level. At L5 (the top), this reads `at the top level (Supervising) —
  sustaining`.
- **Coherence is kept as a secondary line**, not in the headline: the
  **Habitat Build Gap** (cognitive − operational) and its regime stay
  just below, so the "coherence, not level" signal is retained (see
  AGENTS.md ARCH_DECISIONS). The cognitive read (`Assessed level`) and
  date remain as supporting fields.
- The rest of the report (profile, disciplines, gap section, strengths /
  gaps / recommendations, reading path, next steps) is unchanged.

## Alternatives considered

- **Replace the Habitat Build Gap framing entirely** with level-progress.
  Rejected — it reverses the "coherence not level" decision and loses the
  signal that flagged the incoherent L4 jump.
- **Headline the Habitat Build Gap (reframed)** instead of distance-to-
  next-level. Rejected — less intuitive than "you're +X from Level N+1".
- **Floor instead of rounded** for the current level. Rejected — the
  rounded mean is the existing Habitat Maturity Level definition;
  switching would relabel past reports.

## Risks / what could go wrong

- **Two numbers that look alike.** "Next Step / Gap" (distance to next
  level) and the secondary "Habitat Build Gap" (coherence) can coincide
  numerically (they do in the re-assessment). Mitigation: distinct labels
  and a one-line gloss on each.
- **Headlining level may re-tempt level-chasing** — the very thing the
  framework cautions against. Mitigation: the coherence line sits
  immediately below and the recommendations stay coherence-anchored.

## Adversarial review

- **Reviewer**: PR reviewer (human, at merge)
- **Disposition**: accepted
- **Notes**: The level-chasing risk was weighed against approachability;
  keeping the Habitat Build Gap as an adjacent secondary line was the
  agreed mitigation (chosen by the maintainer over fully replacing it).

## Acceptance

- The instrument's output template and the HTML render lead with the two
  lines; the Habitat Build Gap remains as a secondary line.
- The command and skill stay in sync (Dual-surface).
- The two committed example reports (baseline + re-assessment), in
  markdown and HTML, are reformatted to the new header.
- `docs/reference/assessment-output.md` describes the new header.
