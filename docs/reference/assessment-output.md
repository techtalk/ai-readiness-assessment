# Assessment output structure

Each run writes `assessments/YYYY-MM-DD-assessment.md` with the following
sections, in order. Every section is filled with specific evidence —
paths, counts, dates.

## Header

```text
**Date**: YYYY-MM-DD
**Habitat Maturity Level**: Level N (model) — <held back by: weakest dimensions>
**Assessed level**: Level N — <Level Name>   (the cognitive read)
**Habitat Build Gap**: <signed gap> (<regime>)
```

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
