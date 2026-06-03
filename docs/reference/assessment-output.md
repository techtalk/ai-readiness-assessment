# Assessment output structure

Each run writes `assessments/YYYY-MM-DD-assessment.md` with the following
sections, in order. Every section is filled with specific evidence —
paths, counts, dates.

## Header

The report leads with **two lines** — the current level and the next
step — so the headline answer is legible at a glance. Coherence (the
Habitat Build Gap) and the cognitive read follow as secondary fields.

```text
**Current Habitat Maturity**: Level N (Verb)
**Next Step / Gap**: +X to Level N+1 (NextVerb)

**Habitat Build Gap**: <signed gap> (<regime>)   (coherence; secondary)
**Assessed level**: Level N — <Level Name>   (the cognitive read)
**Date**: YYYY-MM-DD
```

The level **verb** is the model's Agent-behaviour archetype: L1
Dictating, L2 Commanding, L3 Regulating, L4 Orchestrating, L5
Supervising. **Next Step / Gap** is `(N+1) − the 14-dimension mean` — the
distance to the next level (at L5: "at the top — sustaining"). It is
distinct from the **Habitat Build Gap**, which is the
[coherence](../explanation/coherence-not-level.md) diagnostic
(cognitive − operational) and can differ in both value and sign.

## Habitat Document Discovery

A table of the habitat documents found — instruction files, constraint
documents, specs, reflection/decision records — each with its **path**
and the **content markers** that confirmed the match. Produced *before*
any maturity claim. If two files plausibly fill the same role, the
assessment stops and asks which is canonical rather than guessing.

## Observable Evidence

Every signal found (with path) and every signal **not** found. The
absences matter as much as the presences.

## Clarifying Responses

The 3–5 questions asked (one at a time) and the answers given — the
behavioural detail the filesystem can't supply.

## Habitat Maturity Profile

All fourteen [model dimensions](habitat-maturity-model.md) placed L1–L5,
each reported with the model's **verb** (e.g. *Testing: L3 — Verifying*).
Behavioural dimensions placed without direct evidence are tagged
**(inferred)**. Ends with the headline **Habitat Maturity Level** (the
rounded mean, weakest dimensions named).

## Level Assessment

The [cognitive level](cognitive-ladder.md) (L0–L5), its name, and a
one-line rationale anchored in the weakest discipline.

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | N | … |
| Architectural Constraints | N | … |
| Guardrail Design | N | … |

## Operational Axes (Part D)

The four discipline-aligned headline dimensions — Composition, Testing,
Observability, Governance — lifted from the profile as a focused view.

## Habitat Build Gap

The signed gap and its regime. See
[The Habitat Build Gap](habitat-build-gap.md).

## Strengths · Gaps · Recommendations

Top three each, anchored in evidence. Recommendations are ordered by
impact and each tied to a specific gap.

## Reading Path

The specific chapter of *[The Sovereign Engineer](../explanation/the-sovereign-engineer.md)*
that closes the weakest discipline gap — gap-anchored, not a generic
plug — with the Leanpub link.

## Next Steps

**One** TechTalk engagement matched to the same gap — deliberately one
recommendation, not a menu. A menu reads like marketing; a specific
recommendation reads like advice.

---

A shareable [HTML version](../how-to/render-the-html-report.md) is
offered on request.
