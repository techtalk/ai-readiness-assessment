# Expected behaviour — fixture `level-2-verified`

This fixture has the L1 signals (`.cursorrules`, ruff config) **plus**
the L2 verification stack:

- `pytest` test suite under `tests/`
- CI workflow at `.github/workflows/ci.yml` that runs ruff and pytest
- Coverage threshold (`--cov-fail-under=80`) enforced by CI
- `.pre-commit-config.yaml` wiring ruff into local commits

What it does **not** have:

- `CLAUDE.md`, `AGENTS.md`, `HARNESS.md` — no rich habitat document
- Custom skills/commands/agents
- A reflection log
- Decision records (ADRs)
- Specs

The team can detect AI drift in code (CI gates, coverage threshold)
but has not yet built a persistent collaboration environment. This
is the textbook L2 signal.

When `/ai-readiness-assess` runs against this fixture, the output
**must** satisfy every assertion below.

---

## A. Structural assertions

A1. **Assessment file is written** at
`assessments/YYYY-MM-DD-assessment.md`.

A2. **Assessed level is L2.** The assessment contains:

```
**Assessed level**: Level 2 — Verification discipline
```

Not L1, not L3.

A3. **Discovery report cites the verification stack.** The Observable
Evidence section lists, at minimum:

- `.cursorrules` (AI-instruction file)
- `.github/workflows/ci.yml` (CI configuration)
- `tests/test_main.py` (test suite)
- `pyproject.toml` (with coverage threshold)
- `.pre-commit-config.yaml` (pre-commit hook)

A4. **Discovery report enumerates the missing habitat layer.** The
following are "not found":

- `CLAUDE.md`
- `AGENTS.md`
- `HARNESS.md`
- `specs/` or `docs/specs/`
- `REFLECTION_LOG.md`
- `skills/`, `commands/`, `agents/` directories
- `docs/adr/` or `docs/decisions/`

A5. **No fabricated citations.** Only paths that actually exist in the
fixture appear in the assessment.

A6. **Discipline maturity bounds.**

- Context Engineering: strength 1 (.cursorrules present but thin; no
  CLAUDE.md / AGENTS.md).
- Architectural Constraints: strength 2 or 3 (CI enforces ruff +
  coverage threshold).
- Guardrail Design: strength 2 or 3 (CI gate, pre-commit hook, test
  suite).

Context Engineering scored ≥ 2 fails. Constraints or Guardrails
scored < 2 fails.

A7. **Reading Path matches L2.** The Reading Path section recommends
the **Level 3 (habitat design)** chapter of *The Sovereign Engineer*.
Per the embedded reading map, this is the next step for a team with
verification discipline.

A8. **Leanpub link present.**

A9. **Single CTA.**

A10. **CTA names Context Engineering as the weakest discipline.**
Since this fixture has CI + tests + hooks but no habitat document,
Context Engineering is the lowest-scored discipline and the natural
gap-anchor for the CTA.

A11. **CTA engagement type matches the engagement map.** For weakest
= Context Engineering, the recommended engagement is a
habitat-document bootcamp focused on building `CLAUDE.md` /
`AGENTS.md` / `HARNESS.md` for the team's own codebase.

---

### Operational Axes & Habitat Build Gap (Part D)

Part D places four operational axes (L1–L5) and computes the Habitat
Build Gap (cognitive level − operational-axes mean). Expected placement
for this fixture:

- Composition: L1
- Testing: L2
- Observability: L1
- Governance: L2
- Operational axes mean: L1.5
- **Habitat Build Gap: +0.50 (Ambition outpaces enablement)**

Verification thinking (L2) runs ahead of the operational mean (1.5); Composition and Observability are the floor axes.

A12. **Operational Axes section present.** The assessment contains a
`## Operational Axes (Part D)` section naming all four axes
(Composition, Testing, Observability, Governance).

A13. **Habitat Build Gap present.** The assessment contains a
`## Habitat Build Gap` section, a scannable `**Habitat Build Gap**:`
header line, and the interpretation regime **Ambition outpaces enablement**.

---

## B. Behavioural assertions

B1. **Scan first.** Discovery before clarifying questions.

B2. **Questions one at a time** (if asked).

B3. **(Interactive runs only)** 3–5 clarifying questions in total.
**N/A in batch test runs.** Plausible questions for this fixture
include: "Is `.cursorrules` actually read by the team, or is it
stale?", "Does the PR review process explicitly check for
AI-generated drift?".

B4. **No silent canonical picks.** Only `.cursorrules` is present.

---

## C. Semantic assertions

C1. **Rationale fits the evidence.** The L2 rationale names the
**absence of any habitat document** (no CLAUDE.md / AGENTS.md /
HARNESS.md / skills / reflection log) as the ceiling. Strong
verification with no encoded habitat is L2, not L3 — the rationale
must make this explicit.

C2. **Recommendations are gap-anchored.** Top-3 close specific gaps.
At least one recommendation must mention building a `CLAUDE.md` (or
equivalent rich habitat document).

C3. **CTA reads like advice.** The recommendation paragraph names a
concrete first step (e.g. "spend a half-day drafting a CLAUDE.md
that captures the conventions you already enforce in CI"), not a
generic offering.


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
