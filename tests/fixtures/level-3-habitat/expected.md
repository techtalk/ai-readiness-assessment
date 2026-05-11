# Expected behaviour — fixture `level-3-habitat`

This fixture has the L2 verification stack **plus** a full habitat
layer:

- Rich `CLAUDE.md` with project context, conventions, and AI workflow
- `HARNESS.md` constraint document with 5 declared constraints (4
  deterministic, 1 unverified) and 2 GC rules
- `REFLECTION_LOG.md` with 3 entries showing the pattern-surfacing
  loop in action
- `ONBOARDING.md` covering the AI workflow
- `docs/adr/0001-python-3-10-minimum.md` (one decision record)
- `skills/wordcount-style/SKILL.md` (one custom skill)

What it does **not** have:

- `specs/` or `docs/specs/`
- Spec-first commit ordering
- Multi-step agent orchestration
- Cross-team templates, governance audit cadence, decision archaeology
  records, fitness functions, or cost/model-routing discipline

The team has a persistent collaboration environment. They have not
yet made specifications first-class. This is the textbook L3 signal.

When `/ai-readiness-assess` runs against this fixture, the output
**must** satisfy every assertion below.

---

## A. Structural assertions

A1. **Assessment file written** at
`assessments/YYYY-MM-DD-assessment.md`.

A2. **Assessed level is L3.** The assessment contains:

```
**Assessed level**: Level 3 — Habitat design
```

Not L2, not L4.

A3. **Discovery report cites the habitat layer.** The discovery
section names each of:

- `CLAUDE.md`
- `HARNESS.md`
- `REFLECTION_LOG.md`
- `ONBOARDING.md`
- `docs/adr/0001-python-3-10-minimum.md`
- `skills/wordcount-style/SKILL.md`

A4. **Discovery report notes the absence of specs.** The following
are "not found":

- `specs/` or `docs/specs/`
- `rfcs/` or `docs/rfcs/`
- `proposals/`

A5. **No fabricated citations.** Every file path mentioned exists in
the fixture.

A6. **Discipline maturity bounds.**

- Context Engineering: strength 3 or 4 (CLAUDE.md + ONBOARDING.md +
  custom skill).
- Architectural Constraints: strength 3 or 4 (HARNESS.md with
  enforced constraints + CI).
- Guardrail Design: strength 3 (CI, pre-commit, tests, coverage
  threshold).

All three disciplines scored < 3 fails. Any discipline scored ≥ 5
fails (because L4 evidence — specs, orchestration — is absent).

A7. **Reading Path matches L3.** The Reading Path section recommends
the **Level 4 (specifications)** chapter of *The Sovereign Engineer*.

A8. **Leanpub link present.**

A9. **Single CTA.**

A10. **CTA gap is the L3→L4 jump.** The recommendation must mention
specifications, spec-first ordering, intent-first, or equivalent
phrasing as the missing layer. A recommendation that targets only
"more constraints" or "more guardrails" misses the L3→L4 jump and
fails this assertion.

A11. **CTA engagement type matches the closest engagement-map entry.**
The engagement map does not have an explicit "specs" engagement;
since the L3→L4 jump is primarily about encoding intent first
(Context Engineering's most senior form), the closest match is the
habitat-document bootcamp **scoped to specifications**, OR a
custom engagement type that names spec-first explicitly. Generic
harness-engineering consulting or generic orchestrator engagement
without spec language fails.

---

## B. Behavioural assertions

B1. **Scan first.** Discovery before clarifying questions.

B2. **Questions one at a time** (if asked).

B3. **3–5 clarifying questions** total (if asked). Plausible questions
include: "Are specs written before code in practice, or just
sometimes?", "Has the reflection log produced any patterns that you
chose *not* to encode?".

B4. **No silent canonical picks.** Both `CLAUDE.md` and `HARNESS.md`
exist with non-overlapping roles; no false "which is canonical?"
question.

---

## C. Semantic assertions

C1. **Rationale fits the evidence.** The L3 rationale names the
**absence of specs / spec-first practice** as the ceiling. The
rationale must NOT cite "weak HARNESS.md" or "no coverage threshold"
— both are present and at-strength here.

C2. **Recommendations are gap-anchored.** Top-3 close specific gaps.
At least one recommendation mentions specs, spec-first ordering, or
making intent first-class.

C3. **CTA reads like advice.** The recommendation paragraph names a
concrete first step (e.g. "start writing a one-paragraph spec at the
top of each PR description and move the most common ones into a
`specs/` directory after a month"), not a generic offering.
