# Expected behaviour — fixture `level-4-specs`

This fixture has the full L3 habitat (CLAUDE.md, HARNESS.md, custom
skill, ADR, reflection log, ONBOARDING) **plus** the L4 specifications
layer:

- `specs/0001-newline-handling.md` and `specs/0002-empty-input.md` —
  two specs separating "what and why" from "how"
- `specs/plans/0001-newline-handling-plan.md` — implementation plan
  derived from the spec (separate file)
- `docs/objections/0001-newline-handling.md` and
  `docs/objections/0002-empty-input.md` — adversarial review records
  with **all dispositions resolved** (no `pending` values)
- `commands/spec-implement.md` — local orchestrator command that
  drives the spec → plan → objections → implementation flow
- `.github/PULL_REQUEST_TEMPLATE.md` — references the spec
- `CONTRIBUTING.md` — declares spec-first ordering
- `HARNESS.md` — includes a deterministic spec-first-ordering
  constraint and an agent-enforced objection-resolution constraint
- `.github/workflows/ci.yml` — includes a `spec-first-ordering` job

What it does **not** have:

- `.claude-plugin/plugin.json` or any published-artefact manifest
- `MODEL_ROUTING.md` or cost-capture scripts
- `CHOICES.md` or full story-record archaeology
- `audits/` or governance audit cadence
- Fitness functions in CI

This is the textbook L4 signal.

When `/ai-readiness-assess` runs against this fixture, the output
**must** satisfy every assertion below.

---

## A. Structural assertions

A1. **Assessment file written** at
`assessments/YYYY-MM-DD-assessment.md`.

A2. **Assessed level is L4.** The assessment contains:

```
**Assessed level**: Level 4 — Specification-led
```

Not L3, not L5.

A3. **Discovery report cites the specifications layer.** The
discovery section names each of:

- `specs/0001-newline-handling.md`
- `specs/0002-empty-input.md`
- `specs/plans/0001-newline-handling-plan.md`
- `docs/objections/0001-newline-handling.md`
- `docs/objections/0002-empty-input.md`
- `commands/spec-implement.md`
- `CONTRIBUTING.md` (spec-first declaration)

A4. **Discovery report notes the absence of L5 signals.** The
following are "not found":

- `.claude-plugin/plugin.json`
- `MODEL_ROUTING.md`
- `CHOICES.md` or `docs/choices/`
- `audits/`
- Fitness-function GC rules in HARNESS.md

A5. **No fabricated citations.**

A6. **Discipline maturity bounds.**

- Context Engineering: strength 4 (rich habitat + specs).
- Architectural Constraints: strength 4 (HARNESS.md plus
  spec-conformance and spec-first-ordering constraints).
- Guardrail Design: strength 4 (adversarial review at plan
  approval — the spec-first guardrail that closes the
  drift-before-code gap).

All three disciplines scored < 4 fails. Any discipline scored 5
fails (because L5 cross-team / governance evidence is absent).

A7. **Reading Path matches L4.** The Reading Path section recommends
the **Level 5 (systems and orchestration)** chapter of *The Sovereign
Engineer*. Per the embedded reading map.

A8. **Leanpub link present.**

A9. **Single CTA.**

A10. **CTA names the L4→L5 jump.** The recommendation must mention
cross-team templates, published plugin, governance audit cadence,
decision archaeology, fitness functions, or cost/model-routing as
the missing layer.

A11. **CTA engagement type matches the L4→L5 engagement-map row.**
The engagement map (updated to include the L4→L5 row) describes a
platform-engineering engagement — packaging the habitat as a
published artefact, governance audit cadence, fitness functions,
cost/model-routing. The CTA should align with this row, not with
any of the discipline-keyed rows.

---

### Operational Axes & Habitat Build Gap (Part D)

Part D places all fourteen model dimensions (L1–L5). The four headline
axes below are the discipline-aligned view; the Habitat Build Gap is
cognitive level − the mean of all fourteen dimensions. Expected
placement for this fixture:

- Composition: L4
- Testing: L3
- Observability: L2
- Governance: L4
- Headline axes mean (focused view): L3.25
- Fourteen-dimension mean: L3.64
- **Habitat Build Gap: +0.36 (Coherent)**

Across all fourteen dimensions the operational mean (3.64) sits close to L4 cognition — broadly coherent; Observability (L2) is the one lagging dimension.

A12. **Operational Axes section present.** The assessment contains a
`## Operational Axes (Part D)` section naming all four axes
(Composition, Testing, Observability, Governance).

A13. **Habitat Build Gap present.** The assessment contains a
`## Habitat Build Gap` section, a scannable `**Habitat Build Gap**:`
header line, and the interpretation regime **Coherent**.

---

## B. Behavioural assertions

B1. **Scan first.** Discovery before clarifying questions.

B2. **Questions one at a time** (if asked).

B3. **(Interactive runs only)** 3–5 clarifying questions in total.
**N/A in batch test runs.**

B4. **No silent canonical picks.**

---

## C. Semantic assertions

C1. **Rationale fits the evidence.** The L4 rationale names the
**absence of L5 (sovereign / platform-level) signals** as the
ceiling. It must NOT cite weak specs or weak constraints — those
are at-strength here.

C2. **Recommendations are gap-anchored.** At least one recommendation
mentions cross-team work, published artefacts, governance audit
cadence, fitness functions, or cost/model-routing as the L4→L5
next step.

C3. **CTA reads like advice.** The recommendation paragraph names a
concrete first step (e.g. "package the habitat documents — CLAUDE.md
template, HARNESS.md skeleton, the wordcount-style skill — as a
plugin manifest under `.claude-plugin/` so a sibling team can install
the habitat in one step"), not a generic offering.


---

### A14. Habitat Maturity Profile (Agentic Experience 5-Level Habitat Maturity Model)

The assessment must contain a `## Habitat Maturity Profile` section that
places **all fourteen** model dimensions L1–L5 with the model's verb
(Agent behaviour, Agent input, Workflow, Operating model, Teams provide,
Output role, Output artefact, Humans review, Work patterns, Agent
composition, Agents…, Testing, Observability, Governance) and reports a
headline **Habitat Maturity Level**. The four discipline-aligned headline
axes in `## Operational Axes (Part D)` must agree with the same four rows
in the profile. The Habitat Build Gap is measured against the mean of all fourteen
dimensions, not just these four.
