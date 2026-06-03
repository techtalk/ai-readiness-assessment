# TechTalk AI Readiness Assessment

[![Tests](https://github.com/techtalk/ai-readiness-assessment/actions/workflows/agentic-behaviours.yml/badge.svg)](https://github.com/techtalk/ai-readiness-assessment/actions/workflows/agentic-behaviours.yml)
[![Release](https://img.shields.io/github/v/release/techtalk/ai-readiness-assessment?label=release&color=2ea44f)](https://github.com/techtalk/ai-readiness-assessment/releases)
[![License](https://img.shields.io/github/license/techtalk/ai-readiness-assessment?color=blue)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-mkdocs--material-526cfe)](https://techtalk.github.io/ai-readiness-assessment/)
[![Marketplace](https://img.shields.io/badge/marketplace-techtalkai-1f6feb)](#install)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#install)
[![Copilot CLI](https://img.shields.io/badge/Copilot%20CLI-plugin-6e40c9)](#install)
![Commands](https://img.shields.io/badge/commands-1-blue)
![Skills](https://img.shields.io/badge/skills-1-blue)
![Harness](https://img.shields.io/badge/harness-3%2F4%20enforced-2ea44f)
[![AI Literacy](https://img.shields.io/badge/AI_Literacy-Level_4-2E8B57)](assessments/2026-06-03-assessment-2.md)
[![Agent Harness Enabled](https://img.shields.io/badge/Agent_Harness-Enabled-000000)](HARNESS.md)

A self-contained AI readiness assessment, packaged as a
plugin for GitHub Copilot (and any other tool that consumes the same
`.claude-plugin/plugin.json` + `commands/` + `skills/` layout — Claude
Code, Cursor via wrapper, Windsurf via wrapper).

Drop into any repository, invoke once, get:

- A timestamped assessment at `assessments/YYYY-MM-DD-assessment.md`.
- A full placement on the **Agentic Experience 5-Level Habitat Maturity
  Model** — all fourteen dimensions, L1–L5, reported with the model's
  own verbs — and a headline **Habitat Maturity Level**.
- A position on the six-level cognitive ladder from *The Sovereign
  Engineer* (Russ Miles, Habitat-Thinking) —
  [leanpub.com/thesovereignengineer](https://leanpub.com/thesovereignengineer) —
  L0 *Aware of the landscape* through L5 *Sovereign engineering* — and
  the **Habitat Build Gap** between the two reads.
- A gap-anchored reading path into the book.
- Recommendations on next steps matched to the
  weakest of the three disciplines: Context Engineering, Architectural
  Constraints, or Guardrail Design.

The assessment is fully self-contained. It does **not** depend on any
external plugin, skill, agent, or service. The model, the framework,
scoring heuristic, and evidence checklist all live inside this repo. The
instrument itself is **inspired by** the
[ai-literacy-superpowers](https://github.com/russmiles/ai-literacy-superpowers)
plugin — see *Inspired by* below.

**Full documentation:**
**[techtalk.github.io/ai-readiness-assessment](https://techtalk.github.io/ai-readiness-assessment/)**
— a Diátaxis-structured site with tutorials, how-to guides, reference,
and explanation.

Contributing or working on the plugin itself? Start with
[ONBOARDING.md](ONBOARDING.md).

## Prerequisites

To run the assessment you need:

- **One supported AI coding tool**, with an active account or
  subscription — either:
  - **GitHub Copilot CLI** — Node.js 18+ (`npm install -g @github/copilot`)
    and a signed-in GitHub account with Copilot access; or
  - **Claude Code** — the `claude` CLI installed
    ([code.claude.com](https://code.claude.com)) and a signed-in
    Anthropic account.
  - Cursor and Windsurf also work via their convention-file wrappers.
- **The plugin installed** from the `techtalkai` marketplace — two
  commands, see [Install](#install) below.
- **A repository to assess.** Open the tool with that repository as the
  working directory / project root, so the scan can see its instruction
  files, CI config, specs, and other habitat signals. A git repo is
  recommended but not required.
- **Write access to the working directory** — the assessment saves its
  report to `assessments/YYYY-MM-DD-assessment.md` in the repo.
- **Network access** the first time, to register the marketplace from
  GitHub.

The assessment itself runs entirely inside the AI tool — there is no
language runtime, build step, or service to set up. Budget around ten
minutes, and expect to answer 3–5 short clarifying questions
interactively. (The Python in `tests/` is only for contributors
verifying the instrument — not needed to run an assessment.)

## Install

This repo is the **`techtalkai`** plugin marketplace. The plugin format
(`.claude-plugin/plugin.json` + `commands/` + `skills/`) is consumed by
both GitHub Copilot CLI and Claude Code, so the install flow is the same
two steps in either tool — register the marketplace, then install the
plugin.

### GitHub Copilot CLI

First install the Copilot CLI (if you haven't already) and sign in:

```
npm install -g @github/copilot
copilot
```

Then register this marketplace and install the plugin. From inside a
`copilot` session:

```
/plugin marketplace add techtalk/ai-readiness-assessment
/plugin install ai-readiness-assessment@techtalkai
```

Or non-interactively, from your shell:

```
copilot plugin marketplace add techtalk/ai-readiness-assessment
copilot plugin install ai-readiness-assessment@techtalkai
```

Confirm it's installed and see its skills:

```
copilot plugin list
/skills list
```

To update or remove later:

```
copilot plugin update ai-readiness-assessment
copilot plugin uninstall ai-readiness-assessment
copilot plugin marketplace remove techtalkai
```

### Claude Code

The same marketplace works from inside a Claude Code session:

```
/plugin marketplace add techtalk/ai-readiness-assessment
/plugin install ai-readiness-assessment@techtalkai
```

Or non-interactively, from your shell:

```
claude plugin marketplace add techtalk/ai-readiness-assessment
claude plugin install ai-readiness-assessment@techtalkai
```

Confirm it's installed:

```
claude plugin list
```

To update later:

```
/plugin marketplace update techtalkai          # in a session
claude plugin marketplace update techtalkai     # from the shell
```

To remove:

```
/plugin uninstall ai-readiness-assessment@techtalkai   # in a session
/plugin marketplace remove techtalkai

claude plugin uninstall ai-readiness-assessment@techtalkai   # from the shell
claude plugin marketplace remove techtalkai
```

## Use

In GitHub Copilot CLI or any Copilot-compatible surface, with this
plugin installed:

```
/ai-readiness-assess
```

Or invoke by natural language — the skill is triggered by phrases like
"assess our AI readiness", "where are we on the framework?", "check our
literacy level", "score our AI maturity".

## What you get

The command produces a structured assessment with the following
sections:

1. **Habitat Document Discovery** — what was found, with paths and the
   content markers that confirmed the match.
2. **Observable Evidence** — every signal found and every signal
   absent, with paths.
3. **Clarifying Responses** — 3–5 follow-up questions filling gaps the
   filesystem cannot answer, asked one at a time.
4. **Habitat Maturity Profile** — your placement on **all fourteen
   dimensions** of the *Agentic Experience 5-Level Habitat Maturity
   Model* (L1–L5 each, reported with the model's own verbs), and a
   headline **Habitat Maturity Level** with the weakest dimensions named
   as the ceiling. This is the spine of the assessment.
5. **Level Assessment** — the cognitive read: your level (L0–L5) on the
   *Sovereign Engineer* ladder with a one-line rationale anchored in the
   weakest discipline.
6. **Discipline Maturity** — Context Engineering, Architectural
   Constraints, Guardrail Design, each scored 0–5.
7. **Operational Axes (Part D)** — the four discipline-aligned headline
   dimensions — Composition, Testing, Observability, Governance — lifted
   from the profile as a focused view.
8. **Habitat Build Gap** — `cognitive level − habitat maturity mean`
   (the mean of all fourteen dimensions), read through three regimes
   (Coherent / Ambition outpaces enablement / Inherited habitat). The
   signal is coherence, not the size of the level.
9. **Strengths, Gaps, Recommendations** — top three each, anchored in
   evidence.
10. **Reading Path** — the specific chapter of *The Sovereign Engineer*
    that closes your weakest discipline gap.
11. **Next Steps** — one TechTalk engagement matched to that same gap.

A shareable HTML version is offered on request.

### Example — and a progression

We ran the assessment against **this plugin's own repo**, then again
after acting on its own top recommendation (enforcing spec-first). The
two reports show real progression — and an honest twist:

| | Baseline | After enforcing spec-first |
|---|---|---|
| **AI Readiness — Habitat Maturity** | Level 3 (Regulating) | Level 3 (Regulating) |
| **Next Step / Gap** | +1.2 to Level 4 (Orchestrating) | +1.1 to Level 4 (Orchestrating) |
| Cognitive read | L3 — Habitat design | **L4 — Specification-led** |
| Habitat Build Gap (coherence) | +0.2 — Coherent | **+1.1 — Ambition outpaces enablement** |
| Report | [md](assessments/2026-06-03-assessment.md) · [HTML](https://techtalk.github.io/ai-readiness-assessment/examples/self-assessment.html) | [md](assessments/2026-06-03-assessment-2.md) · [HTML](https://techtalk.github.io/ai-readiness-assessment/examples/self-assessment-2.html) |

Each report leads with those two lines, then an **AI Readiness Score**
across five readiness dimensions and a **Prioritised Improvement Plan**.
Lifting the spec discipline to L4 left the operational habitat behind, so
the gap flipped from coherent to ambition-outpaces-enablement — the
instrument tracking coherence, not just level. Full write-up in the
[docs](https://techtalk.github.io/ai-readiness-assessment/examples/).

## Layout

```
ai-readiness-assessment/
├── .claude-plugin/
│   ├── plugin.json                  # plugin manifest
│   └── marketplace.json             # techtalkai marketplace manifest
├── commands/
│   └── ai-readiness-assess.md       # /ai-readiness-assess
├── skills/
│   └── ai-readiness-assessment/
│       └── SKILL.md                 # natural-language trigger
└── README.md
```

The command and the skill carry identical framework content, so
either entry point produces the same assessment.

## The model

The spine of the assessment is the **Agentic Experience 5-Level Habitat
Maturity Model** (TechTalk.AI / Agentic Engineering) — **fourteen
dimensions, each placed L1–L5**, measuring what a team's habitat
*actually delivers*. The full model is embedded in the command and skill
files — see `commands/ai-readiness-assess.md` for the canonical version.

Each dimension matures through the model's own **verbs** — the verb
*is* the finding:

| Dimension | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|
| **Agent behaviour** | *Dictating* | *Commanding* | *Regulating* | *Orchestrating* | *Supervising* |
| **Agent input** | short ad-hoc prompts | larger prompts | plans | iteratively refined specs | specs + observable metrics |
| **Workflow** | safe runtime, generic | prompts/commands saved | harness engineered | workflow defined | workflow automated |
| **Operating model** | *Chat* | *Prompt-engineering* | *drive / verify* | *in the loop* | *certify* |
| **Teams provide** | — | basic constitution | comprehensive constitution | full constitution | custom runtime |
| **Output role** (*I am…*) | *Running* | *Inspecting* | *Standardising* | *Specifying* | *Certifying* |
| **Output artefact** | executable / artifact | code | process & consistency rules | clear criteria | evidence |
| **Humans review** | output only | code | implementation in detail | specs | comprehensive evidence |
| **Work patterns** | partial task | small task | e2e development | semi-autonomous | mostly-autonomous |
| **Agent composition** | single | single + saved patterns | primary + read-only critics | bounded ensemble | self-orchestrating constellations |
| **Agents…** | *Assist* | *Complete* | *Develop* (stories) | *Implement* (epics) | *Implement* autonomously |
| **Testing** | *Manual* | *Asserting* | *Verifying* | *Validating* | *Assuring* |
| **Observability** | *Eyeballs* | *Captured* | *Instrumented* | *Aggregated* | *Closed loop* |
| **Governance** | trust-based, ambient | conventional | *Constitutional* | *Policy-as-code* | *Continuous certification* |

The assessment places every one of the fourteen dimensions and reports a
headline **Habitat Maturity Level** (the rounded mean), naming the
weakest dimensions as the ceiling — a habitat is only as mature as the
dimensions its work actually flows through. Eight dimensions are placed
**evidence-first** from a repository scan; the six behavioural ones
(Agent behaviour, Operating model, Output role, Humans review, Work
patterns, Agents…) are placed from a handful of clarifying questions.

## The cognitive read (*The Sovereign Engineer*)

Folded in alongside the model is the six-level AI collaboration literacy
ladder from *The Sovereign Engineer* — the **cognitive** view, what a
team can think and do:

| Level | Name |
|-------|------|
| L0 | Aware of the landscape |
| L1 | Communicating through prompts |
| L2 | Verification discipline |
| L3 | Habitat design |
| L4 | Specification-led |
| L5 | Sovereign engineering |

Three disciplines run through every level. **The weakest is the
ceiling** — strong specs with weak verification is L2, not L4.

1. **Context Engineering** — encoding wisdom into the agent's context.
2. **Architectural Constraints** — making structural rules
   machine-checkable.
3. **Guardrail Design** — feedback loops that catch drift.

(The cognitive ladder runs L0–L5; the model's dimensions run L1–L5. L0
is "aware but nothing encoded" — on the model that is the L1 floor.)

### The Habitat Build Gap

The gap reconciles the two reads. Its operational term is the
**Habitat Maturity Level** — the mean of **all fourteen** model
dimensions — so every dimension the team is weak or strong on moves it:

```text
Habitat Build Gap = cognitive level − habitat maturity mean (all 14 dimensions)
```

Both terms are on the same 0–5 scale, so the gap can be positive or
negative. It is read through three regimes — the signal is *coherence*,
not the size of the level:

| Gap | Regime | Reading |
|-----|--------|---------|
| `abs(gap) < 0.5` | **Coherent** | Team and habitat are at the same level; collaboration is well-supported by the environment. |
| `gap ≥ +0.5` | **Ambition outpaces enablement** | The team thinks at a higher level than the habitat supports. Build the habitat the team's thinking already implies. |
| `gap ≤ −0.5` | **Inherited habitat** | The habitat is more mature than current practice. Literacy uplift before further harness extension. |

A coherent L2/L2 team is healthier than an incoherent L4-cognitive /
L1-operational one. The four discipline-aligned headline axes
(Composition, Testing, Observability, Governance) are still reported as
a focused view of the profile, but the gap is measured against all
fourteen dimensions. The dimensions and their verbs, the cognitive
ladder, the evidence map, the gap formula, and these regimes are
embedded in the command and skill files in full, so the instrument stays
self-contained.

## The book

*The Sovereign Engineer* — Russ Miles — Habitat-Thinking.

The six-level framework, the three disciplines, and the
weakest-discipline-as-ceiling heuristic that this assessment scores
against are all set out in the book. The assessment surfaces the
specific chapter that closes your weakest discipline gap — gap-anchored,
not a generic plug.

Buy or read on Leanpub:
**[leanpub.com/thesovereignengineer](https://leanpub.com/thesovereignengineer/c/ai-readiness)**

## TechTalk

If the assessment surfaces a gap your team would like help closing,
TechTalk supports engagements matched to each discipline:

- **Context Engineering** — Habitat-document bootcamp.
- **Architectural Constraints** — Harness-engineering consulting.
- **Guardrail Design** — Orchestrator and verification engagement.

The command produces a single, specific recommendation rather than a
menu — a menu reads like marketing, a specific recommendation reads
like advice.

## Inspired by

This plugin is **inspired by** the
[ai-literacy-superpowers](https://github.com/russmiles/ai-literacy-superpowers)
plugin — the canonical home of the AI Literacy framework, with its
full agent team, harness engineering, governance audit, compound
learning loop, and orchestrator pipeline. The supporting reference
repository is
[ai-literacy-for-software-engineers](https://github.com/russmiles/ai-literacy-for-software-engineers).

What you get here is narrower by design: just the assessment
instrument, extracted into a standalone, dependency-free package that
runs in any repo and any tool consuming the Copilot/Claude Code plugin
layout. If the assessment reveals you want the full habitat — the
agent pipeline, the constraint enforcement, the compound learning —
that is what `ai-literacy-superpowers` provides.

The conceptual ground for both — the six levels, the three
disciplines, the habitat-thinking lens — is set out in
*The Sovereign Engineer*:
[leanpub.com/thesovereignengineer](https://leanpub.com/thesovereignengineer).
