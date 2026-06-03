# AI Literacy Assessment — wordcount (level-3-habitat fixture)

**Date**: 2026-05-11
**Assessed level**: Level 3 — Habitat design
**Habitat Maturity Level**: Level 3 (model)
**Habitat Build Gap**: +0.50 (Ambition outpaces enablement)

> **Test-run note**: batch mode, clarifying questions skipped.

## Habitat Document Discovery

| Document type | Path | Result | Markers |
|---|---|---|---|
| AI-instruction file (rich) | `CLAUDE.md` | **found** | Project context, conventions (enforced), AI workflow, skills index, pointer to ONBOARDING.md. ~50 lines of prose, load-bearing. |
| Constraint document | `HARNESS.md` | **found** | Context / Constraints / Garbage Collection / Status structure. 5 constraints declared, 4 deterministic, 1 unverified. 2 GC rules. Matches the harness-engineering pattern. |
| Reflection log | `REFLECTION_LOG.md` | **found** | Three dated entries showing the surprise → lesson → action loop. Promotion to HARNESS.md visible in entry 1 ("Added the No os.path usage constraint to HARNESS.md as unverified"). |
| Onboarding | `ONBOARDING.md` | **found** | Day-one setup plus an explicit AI-collaboration workflow section. |
| Decision record | `docs/adr/0001-python-3-10-minimum.md` | **found** | One ADR with Context / Decision / Consequences structure. |
| Custom skill | `skills/wordcount-style/SKILL.md` | **found** | Project-local skill that reviews diffs against CLAUDE.md / HARNESS.md rules. Frontmatter present (name, description). |
| Specifications | `specs/`, `docs/specs/`, `rfcs/`, `proposals/` | **not found** | — |

The habitat layer is present and integrated. The specifications layer
is absent. This is the L3 fingerprint.

## Observable Evidence

**Found:**

- `CLAUDE.md` (rich), `HARNESS.md` (constraint document with 5
  declared rules), `REFLECTION_LOG.md` (3 entries, ongoing loop),
  `ONBOARDING.md` (AI workflow included), `docs/adr/0001-python-3-10-minimum.md` (one ADR),
  `skills/wordcount-style/SKILL.md` (custom skill with frontmatter).
- Full L2 verification stack: `.cursorrules`-equivalent role filled
  by `CLAUDE.md`, `.github/workflows/ci.yml`, `tests/test_main.py`,
  `pyproject.toml` with coverage-floor config, `.pre-commit-config.yaml`.
- Implementation files: `src/wordcount/__init__.py`,
  `src/wordcount/main.py`.

**Not found:**

- `specs/`, `docs/specs/`, `rfcs/`, `proposals/` — no specifications
  directory.
- Spec-first commit ordering — no CI check or contribution-guide
  statement enforcing spec-before-code.
- Adversarial spec review — no `docs/objections/` or equivalent
  pattern.
- Multi-step agent orchestration — no orchestrator agent, no
  workflow pipeline beyond the one custom skill.
- Cross-team templates / governance audit cadence / decision
  archaeology beyond a single ADR / fitness functions / `MODEL_ROUTING.md` —
  all absent (the L4–L5 surface).

## Clarifying Responses

Skipped (batch test run). The questions the skill would have asked:

1. "Are specs written before code in practice anywhere — even
   informally in PR descriptions — or only post-hoc?"
2. "Has the reflection log produced patterns the team chose **not**
   to encode? If so, why?"
3. "How often does the team actually invoke the `wordcount-style`
   skill during review, vs. doing the check by eye?"

Not asked in this run.

## Habitat Maturity Profile (Agentic Experience 5-Level Habitat Maturity Model)

All fourteen dimensions, each placed L1–L5 with the model's verb. (Batch
test run — behavioural dimensions are inferred from the repo-observable
ones and marked accordingly.)

| Dimension | Level | Stage (verb) | Evidence / basis |
|---|---|---|---|
| Agent behaviour | L3 | Regulating | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Agent input | L2 | larger prompts, commands | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Workflow | L3 | harness engineered | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Operating model | L3 | drive / verify | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Teams provide | L3 | comprehensive product constitution | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Output role | L3 | Standardising | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Output artefact | L3 | process & consistency rules | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Humans review | L2 | code | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Work patterns | L2 | small task completion | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Agent composition | L2 | single + saved patterns | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Agents… | L2 | Complete basic tasks | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Testing | L2 | Asserting (unit tests) | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Observability | L2 | Captured | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |
| Governance | L3 | Constitutional | HARNESS.md harness + rich CLAUDE.md drive a regulating/standardising habitat; no specs, single agent + one skill. |

**Habitat Maturity Level**: Level 3 (model) — mean L2.5 (on the L2/L3 boundary); held back by L2 Composition, Testing, and Observability. This fourteen-dimension mean (L2.50) is the Habitat Build Gap's operational term.

## Level Assessment

**Level 3 — Habitat design.**

Rationale: the team has a persistent collaboration environment — a
rich `CLAUDE.md`, an enforced `HARNESS.md`, a live reflection loop
that has visibly promoted at least one pattern from surprise to
constraint, AI-aware onboarding, decision records, and a custom
project skill. All three disciplines are at strength 3 or above. The
ceiling is the absence of any specifications layer: no `specs/`,
no spec-first ordering, no adversarial spec review, no orchestrated
multi-step agent workflows operating on specs. Intent is implicit in
PR bodies and CLAUDE.md, not first-class.

Weakest discipline: a tie between Context Engineering and
Architectural Constraints at 3 — both at the level where promoting
intent to first-class would be the next compounding move. The L3→L4
jump is primarily about making specifications first-class, which
sits at the intersection of context (encoded intent) and constraint
(spec-conformance gates).

## Discipline Maturity

| Discipline | Strength (0–5) | Evidence |
|---|---|---|
| Context Engineering | 3 | CLAUDE.md (rich), ONBOARDING.md (AI workflow), custom skill, ADRs. No specs/ — intent is implicit. |
| Architectural Constraints | 3 | HARNESS.md with 4 deterministic constraints (ruff format, ruff lint, coverage floor, ruff E722) and 1 unverified (no os.path). One reflection-driven promotion path visible. No spec-conformance gate. |
| Guardrail Design | 3 | CI (ruff + pytest + coverage), pre-commit (ruff + ruff-format), test suite, coverage tripwire. No adversarial-review gate, no plan-approval gate. |

## Operational Axes (Part D)

| Axis | Level (L1–L5) | Evidence |
|---|---|---|
| Composition | L2 | One custom skill (reusable command) and documented conventions; still a single primary agent with no read-only critic or orchestrator. |
| Testing | L2 | CI runs pytest with a coverage floor; unit tests + disciplined review. No functional/business-outcome or agent-authored tests yet. |
| Observability | L2 | REFLECTION_LOG captures patterns and CI logs are searchable, but there are no instrumented dashboards or per-PR acceptance tracking. |
| Governance | L3 | HARNESS.md is an enforced written constitution (4 deterministic + 1 unverified constraint) with a visible promotion path — consistent with the L3 Architectural Constraints score. |

**Headline axes mean**: L2.25 — a focused, discipline-aligned view; the Habitat Build Gap uses all fourteen dimensions

## Habitat Build Gap

```text
Habitat Maturity Level (model):  L3  (14-dim mean L2.50)
Cognitive read (Parts A–C):      L3
Habitat Build Gap:               +0.50   (cognitive − 14-dim mean)
Interpretation:                  Ambition outpaces enablement
```

Across all fourteen dimensions the operational mean (2.50) trails L3 cognition. The dimensions most worth lifting are Composition, Testing, and Observability — add a read-only critic agent or a small orchestrator so the habitat delivers the multi-agent review its constraints already imply.

## Strengths

1. **The reflection loop has actually run end-to-end.** Entry 1 in
   `REFLECTION_LOG.md` surfaced a pattern (`os.path.join` slipping
   through), entry 3 closed the loop by tightening CI. The team has
   demonstrated, not just declared, the L3 pattern.
2. **`CLAUDE.md` and `HARNESS.md` divide responsibility cleanly.**
   Prose conventions in CLAUDE.md, machine-checkable rules in
   HARNESS.md, cross-references between them. The agent reads both
   and they don't contradict each other.
3. **The custom skill (`wordcount-style`) extends agent capability
   in a project-specific way.** Frontmatter is correct, scope is
   tight (5 specific checks), and it cites the documents it enforces.
   This is the L3 "make the agent learn your codebase" pattern done
   well.

## Gaps

1. **No specifications layer.** Intent lives in PR descriptions and
   in `CLAUDE.md` prose — there is no `specs/` directory where the
   "what and why" of a change is captured separately from the
   "how". Refactors can drift from intent silently.
2. **No spec-first ordering.** Nothing in CI or contribution
   conventions requires a spec before code. The team could regress
   to code-first habits without noticing.
3. **No adversarial-review gate.** Reflections happen *after*
   incidents. There is no plan-approval step that surfaces
   objections *before* the code lands.

## Recommendations

1. **Start writing a one-paragraph spec at the top of each PR
   description.** Make the "what and why" explicit. After a month,
   move the most common spec patterns into a `specs/` directory.
   Closes the largest L3→L4 gap at near-zero cost.
2. **Add a spec-conformance constraint to `HARNESS.md`** once
   `specs/` exists: "Every code change covered by a spec must
   reference the spec in its PR body and pass the spec's associated
   test or check." Promote to deterministic once you have a habit.
3. **Introduce one adversarial-review touchpoint** — for example,
   require the agent to write a short "what could go wrong with
   this spec" record before implementation begins. The reflection
   loop catches failures after the fact; this catches them before.

## Reading Path

Your assessed level is **L3 — Habitat design**. The natural next read
in *The Sovereign Engineer* is the **Level 4 (specifications)
chapter** — your habitat is in place; the next leverage is making
intent first-class, separating "what we're trying to do" from "how
we're doing it".

Get the book: <https://leanpub.com/thesovereignengineer>

## Next Steps

> Your habitat is healthy at L3 and the L3→L4 jump is about making
> specifications first-class. If you'd like help making that jump,
> TechTalk runs a **specification-first engagement** — two to three
> weeks of guided work that produces a `specs/` directory wired into
> your existing `HARNESS.md` and CI, an adversarial-review touchpoint
> at plan approval, and a small set of orchestration patterns for the
> agent to act on specs rather than ad-hoc instructions. The
> engagement reuses your existing reflection loop as the discovery
> mechanism — no parallel process, no second source of truth.
>
> Get in touch: <https://techtalk.ai>
