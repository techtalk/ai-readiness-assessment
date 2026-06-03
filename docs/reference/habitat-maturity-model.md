# Habitat Maturity Model (14 dimensions)

The **Agentic Experience 5-Level Habitat Maturity Model** is the spine of
the assessment. It describes what a team's habitat *actually delivers*
across **fourteen dimensions**, each placed **L1–L5**. Verbs are in
**bold** — the verb *is* the finding.

| Dimension | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|
| **Agent behaviour** | **Dictating** | **Commanding** (prompting) | **Regulating** | **Orchestrating** | **Supervising** |
| **Agent input** | short ad-hoc prompts | larger prompts, commands | plans co-authored with an agent | iteratively refined specs | refined specs + customer/observable metrics |
| **Workflow** | safe runtime, generic | prompts/commands saved | harness engineered | workflow defined | workflow automated (agentic runtime) |
| **Operating model** | **Chat** with agent | **Prompt**-engineering | humans **drive / verify** | humans **in the loop** | humans **certify** |
| **Teams provide** | — | basic team-specific constitution | comprehensive product-specific constitution | full product-specific constitution | custom product-specific runtime |
| **Output role** (*I am…*) | **Running** | **Inspecting** | **Standardising** | **Specifying** | **Certifying** |
| **Output artefact** | executable / artifact | code | process & consistency rules | clear criteria | evidence |
| **Humans review** | output only | code | implementation in detail | specs | comprehensive evidence |
| **Work patterns** | partial task completion | small task completion | e2e development | semi-autonomous work | mostly-autonomous |
| **Agent composition** | single | single + saved patterns | primary + read-only critics | bounded ensemble (harness-composed) | self-orchestrating constellations |
| **Agents…** | **Assist** individuals | **Complete** basic tasks | **Develop** small changes (stories) | **Implement** larger changes (epics) | **Implement** autonomously |
| **Testing** | **Manual** inspection | **Asserting** (unit tests) | **Verifying** (functional / business) | **Validating** (comprehensive automation) | **Assuring** (multi-perspective + post-deploy) |
| **Observability** | **Eyeballs** | **Captured** | **Instrumented** | **Aggregated** | **Closed loop** |
| **Governance** | trust-based, ambient | conventional | **Constitutional** | **Policy-as-code** | **Continuous certification** |

The dimensions are scored **L1–L5, not L0–L5**: L1 is the "ad-hoc but
present" floor. A repo with essentially no AI-collaboration evidence sits
at the L1 floor on every dimension by definition.

## The headline Habitat Maturity Level

The overall **Habitat Maturity Level** is the rounded mean of the
fourteen placements, with the **weakest dimensions named as the
ceiling** — a habitat is only as mature as the dimensions its work
actually flows through. A high mean dragged down by one L1 dimension is
reported as "L3, held back by L1 Observability", not a flat L3.

## How each dimension is placed

**Eight dimensions are repo-observable** — placed evidence-first from the
scan:

| Dimension | Signals that raise the placement |
|---|---|
| **Workflow** | saved prompts/commands (L2); a harness document — HARNESS.md / CONSTRAINTS.md (L3); defined workflow scripts or CI pipelines (L4); automated agentic runtime (L5) |
| **Teams provide** | richness of CLAUDE.md / AGENTS.md (basic → comprehensive → full constitution); product-specific skills; custom runtime / prod-like agent environments (L5) |
| **Agent input** | ad-hoc prompt traces (L1); saved prompt/command libraries (L2); plan documents (L3); a `specs/` directory (L4); specs + observable metrics (L5) |
| **Output artefact** | raw artifacts (L1); code (L2); process & consistency rule docs (L3); acceptance-criteria documents (L4); evidence artefacts — audits, CI evidence (L5) |
| **Agent composition** | custom agents; read-only critic/reviewer agents; an orchestrator with safety gates; agent-team docs; multi-agent workflow scripts |
| **Testing** | test suites; coverage enforcement; mutation testing; tests-before-merge gates; system/regression suites; agent-authored tests; prod-like environments |
| **Observability** | agent-activity logging; metrics capture; dashboards; per-PR acceptance / mutation-kill tracking; OTel config; closed-loop signals |
| **Governance** | HARNESS.md constraint count + enforcement ratio; policy-as-code CI checks; the unverified → agent → deterministic promotion ladder; governance-audit cadence |

**Six dimensions are behavioural** — they describe how the team works,
not what the filesystem holds. They're inferred from the repo-observable
dimensions and from the clarifying questions, and flagged **(inferred)**
when not directly evidenced: *Agent behaviour, Operating model, Output
role, Humans review, Work patterns, Agents…*.

## Evidence-first vs survey

- **Evidence-first (default)** — repo-observable dimensions placed from
  the scan; behavioural ones inferred.
- **Survey (opt-in)** — marker statements administered on a 1–5 scale,
  two per level, for a rigorous per-dimension score. See
  [Run the precise survey](../how-to/run-the-precise-survey.md).

## The four headline axes

Four dimensions — **Agent composition** (reported as *Composition*),
**Testing**, **Observability**, **Governance** — are the most
repo-observable and map cleanly onto the
[three disciplines](cognitive-ladder.md). They're surfaced as the
*Operational Axes (Part D)* table in the report. The
[Habitat Build Gap](habitat-build-gap.md), however, uses the mean of
**all fourteen** dimensions.

## Provenance

The fourteen dimensions and their verbs are the **Agentic Experience
5-Level Habitat Maturity Model** (TechTalk.AI / Agentic Engineering). The
AI Literacy framework's ALCI drew its four operational axes from this
model; this instrument scores against the model in full. See
[The Sovereign Engineer](../explanation/the-sovereign-engineer.md).
