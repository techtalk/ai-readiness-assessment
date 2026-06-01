# TechTalk AI Readiness Assessment

A self-contained AI readiness assessment, packaged as a
plugin for GitHub Copilot (and any other tool that consumes the same
`.claude-plugin/plugin.json` + `commands/` + `skills/` layout — Claude
Code, Cursor via wrapper, Windsurf via wrapper).

Drop into any repository, invoke once, get:

- A timestamped assessment at `assessments/YYYY-MM-DD-assessment.md`.
- A position on the six-level framework from *The Sovereign Engineer*
  (Russ Miles, Habitat-Thinking) —
  [leanpub.com/thesovereignengineer](https://leanpub.com/thesovereignengineer) —
  L0 *Aware of the landscape* through L5 *Sovereign engineering*.
- A gap-anchored reading path into the book.
- Recommendations on next steps matched to the
  weakest of the three disciplines: Context Engineering, Architectural
  Constraints, or Guardrail Design.

The assessment is fully self-contained. It does **not** depend on any
external plugin, skill, agent, or service. The framework, scoring
heuristic, and evidence checklist all live inside this repo. The
instrument itself is **inspired by** the
[ai-literacy-superpowers](https://github.com/russmiles/ai-literacy-superpowers)
plugin — see *Inspired by* below.

## Install

This repo also acts as the **`techtalkai`** Claude Code marketplace.
From inside a Claude Code session:

```
/plugin marketplace add techtalk/ai-readiness-assessment
/plugin install ai-readiness-assessment@techtalkai
```

To update later:

```
/plugin marketplace update techtalkai
```

To remove:

```
/plugin uninstall ai-readiness-assessment@techtalkai
/plugin marketplace remove techtalkai
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
4. **Level Assessment** — your level (L0–L5) with a one-line rationale
   anchored in the weakest discipline.
5. **Discipline Maturity** — Context Engineering, Architectural
   Constraints, Guardrail Design, each scored 0–5.
6. **Operational Axes (Part D)** — four axes of what the habitat
   *actually delivers* — Composition, Testing, Observability,
   Governance — each placed L1–L5 from repository evidence.
7. **Habitat Build Gap** — `cognitive level − operational-axes mean`,
   read through three regimes (Coherent / Ambition outpaces enablement
   / Inherited habitat). The signal is coherence, not the size of the
   level.
8. **Strengths, Gaps, Recommendations** — top three each, anchored in
   evidence.
9. **Reading Path** — the specific chapter of *The Sovereign Engineer*
   that closes your weakest discipline gap.
10. **Next Steps** — one TechTalk engagement matched to that same gap.

A shareable HTML version is offered on request.

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

## The framework

The assessment is built on the six-level AI collaboration literacy
framework from *The Sovereign Engineer*. The full level table, the
three disciplines, and the scoring heuristic are embedded in the
command and skill files — see `commands/ai-readiness-assess.md` for
the canonical version.

A quick orientation:

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

### Operational axes and the Habitat Build Gap (Part D)

Alongside the cognitive level, the assessment places four **operational
axes** — Composition, Testing, Observability, Governance — each L1–L5,
measuring what the team's habitat actually delivers. The **Habitat
Build Gap** (`cognitive level − operational-axes mean`) reconciles the
two views: a positive gap points at habitat investment ("build the
habitat your thinking implies"), a negative gap at literacy uplift. The
axes, markers, the gap formula, and the three interpretation regimes
are embedded in the command and skill files in full, so the instrument
stays self-contained.

## The book

*The Sovereign Engineer* — Russ Miles — Habitat-Thinking.

The six-level framework, the three disciplines, and the
weakest-discipline-as-ceiling heuristic that this assessment scores
against are all set out in the book. The assessment surfaces the
specific chapter that closes your weakest discipline gap — gap-anchored,
not a generic plug.

Buy or read on Leanpub:
**[leanpub.com/thesovereignengineer](https://leanpub.com/thesovereignengineer)**

## TechTalk

If the assessment surfaces a gap your team would like help closing,
TechTalk offers engagements matched to each discipline:

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
