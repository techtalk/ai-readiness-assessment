# ai-readiness-assessment

A self-contained AI literacy / AI readiness assessment, packaged as a
plugin for GitHub Copilot (and any other tool that consumes the same
`.claude-plugin/plugin.json` + `commands/` + `skills/` layout — Claude
Code, Cursor via wrapper, Windsurf via wrapper).

Drop into any repository, invoke once, get:

- A timestamped assessment at `assessments/YYYY-MM-DD-assessment.md`.
- A position on the six-level framework from *The Sovereign Engineer*
  (Russ Miles, Habitat-Thinking) — L0 *Aware of the landscape* through
  L5 *Sovereign engineering*.
- A gap-anchored reading path into the book.
- One specific TechTalk engagement recommendation matched to the
  weakest of the three disciplines: Context Engineering, Architectural
  Constraints, or Guardrail Design.

The assessment is fully self-contained. It does **not** depend on the
`ai-literacy-superpowers` plugin, on any external skill, agent, or
service. The framework, scoring heuristic, and evidence checklist all
live inside this repo.

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
6. **Strengths, Gaps, Recommendations** — top three each, anchored in
   evidence.
7. **Reading Path** — the specific chapter of *The Sovereign Engineer*
   that closes your weakest discipline gap.
8. **Next Steps** — one TechTalk engagement matched to that same gap.

A shareable HTML version is offered on request.

## Layout

```
ai-readiness-assessment/
├── .claude-plugin/
│   └── plugin.json
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

## The book

*The Sovereign Engineer* — Russ Miles — Habitat-Thinking.
[leanpub.com/thesovereignengineer](https://leanpub.com/thesovereignengineer)

## TechTalk

If the assessment surfaces a gap your team would like help closing,
TechTalk offers engagements matched to each discipline:

- **Context Engineering** — Habitat-document bootcamp.
- **Architectural Constraints** — Harness-engineering consulting.
- **Guardrail Design** — Orchestrator and verification engagement.

The command produces a single, specific recommendation rather than a
menu — a menu reads like marketing, a specific recommendation reads
like advice.

## Credits

Built on the framework and methodology established in the
[ai-literacy-superpowers](https://github.com/russmiles/ai-literacy-superpowers)
plugin and the
[ai-literacy-for-software-engineers](https://github.com/russmiles/ai-literacy-for-software-engineers)
reference repository. This plugin extracts the assessment instrument
from that work into a standalone, dependency-free package.

## Licence

MIT.
