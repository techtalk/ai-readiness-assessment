# Expected behaviour — fixture `level-5-sovereign`

This fixture has the full L4 habitat **plus** the L5 sovereign /
platform layer:

- `.claude-plugin/plugin.json` — the team's habitat **published** as
  the `wordcount-habitat` plugin
- `commands/wordcount-habitat-init.md` — the cross-team adoption
  entry point
- `MODEL_ROUTING.md` — model selection rules + quarterly cost
  snapshots
- `CHOICES.md` — decision archaeology, 5 stories (C-001 through
  C-005)
- `audits/2026-Q1.md` — governance audit cadence with a recorded
  audit that **found drift** (spec-conformance check not running)
  and corrective actions
- `HARNESS.md` GC section — three fitness functions (layer boundary,
  complexity hotspots, dependency age budget)
- `.github/workflows/ci.yml` — a `fitness-functions` job that runs
  the three checks in CI
- `MODEL_ROUTING.md` constraint declared in `HARNESS.md`

This is the textbook L5 signal — the team's practice has crossed the
boundary from "internal habitat" to "shared platform discipline."

When `/ai-readiness-assess` runs against this fixture, the output
**must** satisfy every assertion below.

---

## A. Structural assertions

A1. **Assessment file written** at
`assessments/YYYY-MM-DD-assessment.md`.

A2. **Assessed level is L5.** The assessment contains:

```
**Assessed level**: Level 5 — Sovereign engineering
```

A3. **Discovery report cites the sovereign-layer artefacts.** The
discovery section names each of:

- `.claude-plugin/plugin.json` (published plugin manifest)
- `commands/wordcount-habitat-init.md` (cross-team adoption command)
- `MODEL_ROUTING.md`
- `CHOICES.md`
- `audits/2026-Q1.md`
- The three fitness-function GC rules in `HARNESS.md`

A4. **No fabricated citations.**

A5. **All earlier-layer artefacts are also discovered.** The L3
habitat (CLAUDE.md, HARNESS.md, REFLECTION_LOG, ONBOARDING, ADR,
skill) and the L4 specs layer (specs/, plans/, objections/) are
all named — L5 is additive, not a replacement.

A6. **Discipline maturity bounds.**

- Context Engineering: strength 4 or 5 (rich habitat published as
  plugin, model-routing doc, decision archaeology).
- Architectural Constraints: strength 4 or 5 (HARNESS.md with
  fitness functions, spec-conformance, model-routing constraint,
  governance audit cadence).
- Guardrail Design: strength 4 or 5 (CI gates + fitness functions +
  spec-first + adversarial review + governance audit).

At least one discipline scored 5 must appear. No discipline below 4
is permitted.

A7. **Reading Path matches L5.** The Reading Path section names the
**Enchiridion chapter** and/or the **portfolio-scale chapters** of
*The Sovereign Engineer*. Per the embedded reading map.

A8. **Leanpub link present.**

A9. **Single CTA.**

A10. **CTA frames L5 as a sustained practice, not a one-off step.**
At L5 the team is already at the top of the published framework.
The CTA should anchor in either (a) deepening / sustaining the
practice, (b) helping other teams adopt the habitat, or (c) the
portfolio / sovereignty themes from the book — not in suggesting
a new layer above L5. A "move to L6" recommendation fails this
assertion (no L6 exists).

A11. **CTA engagement type names a sustaining or portfolio-level
engagement** — for example, "portfolio-level assessment", "team
coaching to maintain the practice", "review of the published
habitat plugin", "habitat-as-product workshop for the broader org".
A bare repeat of the L4→L5 engagement (because the team is past
that boundary) fails.

---

### Operational Axes & Habitat Build Gap (Part D)

Part D places four operational axes (L1–L5) and computes the Habitat
Build Gap (cognitive level − operational-axes mean). Expected placement
for this fixture:

- Composition: L4
- Testing: L3
- Observability: L3
- Governance: L5
- Operational axes mean: L3.75
- **Habitat Build Gap: +1.25 (Ambition outpaces enablement)**

Even at sovereign cognition (L5) the operational mean (3.75) lags, driven by Testing and Observability. Governance (L5) is consistent with the Architectural Constraints discipline score.

A12. **Operational Axes section present.** The assessment contains a
`## Operational Axes (Part D)` section naming all four axes
(Composition, Testing, Observability, Governance).

A13. **Habitat Build Gap present.** The assessment contains a
`## Habitat Build Gap` section, a scannable `**Habitat Build Gap**:`
header line, and the interpretation regime **Ambition outpaces enablement**.

---

## B. Behavioural assertions

B1. **Scan first.**

B2. **Questions one at a time** (if asked).

B3. **(Interactive runs only)** 3–5 clarifying questions. **N/A in
batch test runs.**

B4. **No silent canonical picks.** Both `.claude-plugin/plugin.json`
files exist in this fixture in a single canonical location — only
the published-plugin manifest under `.claude-plugin/`. No
disambiguation question should be asked.

---

## C. Semantic assertions

C1. **Rationale fits the evidence.** The L5 rationale names the
sovereign / platform-level practice as the assessed state. It
should **not** position the team as "almost L5" or "approaching L5"
— the published plugin, governance audit cadence, decision
archaeology, fitness functions, and model-routing discipline are
all present.

C2. **Strengths name the platform-level practice.** At least one
of the top-3 Strengths must mention the published plugin, the
governance audit, the decision archaeology, or the fitness
functions.

C3. **CTA reads as advice for an L5 team, not as a sales pitch.**
The recommendation acknowledges the team is at the top of the
framework and proposes a sustaining or portfolio-scale move (e.g.
"open the governance audit cadence to a sibling team and write the
first cross-team audit", or "publish the habitat plugin to the
broader Claude Code marketplace and write the maintenance
playbook").


---

### A14. Habitat Maturity Profile (Agentic Experience 5-Level Habitat Maturity Model)

The assessment must contain a `## Habitat Maturity Profile` section that
places **all fourteen** model dimensions L1–L5 with the model's verb
(Agent behaviour, Agent input, Workflow, Operating model, Teams provide,
Output role, Output artefact, Humans review, Work patterns, Agent
composition, Agents…, Testing, Observability, Governance) and reports a
headline **Habitat Maturity Level**. The four discipline-aligned headline
axes in `## Operational Axes (Part D)` must agree with the same four rows
in the profile. The Habitat Build Gap continues to use the four headline
axes as its operational term.
