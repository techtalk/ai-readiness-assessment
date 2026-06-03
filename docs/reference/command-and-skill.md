# Command & skill

The plugin ships two entry points that carry **identical** assessment
content, so either produces the same result.

## The command

`/ai-readiness-assess` — the canonical entry point. Defined in
`commands/ai-readiness-assess.md`.

```text
/ai-readiness-assess
```

## The skill

`ai-readiness-assessment` — the natural-language surface. Defined in
`skills/ai-readiness-assessment/SKILL.md`. It triggers on phrases like:

> assess our AI readiness · run an AI readiness assessment · check our
> AI literacy level · where are we on the framework? · what level are we
> at? · score our AI maturity · how ready is this codebase for AI
> collaboration? · check our habitat maturity · evaluate how we work
> with AI

It does **not** trigger on general framework questions ("what is the
Sovereign Engineer about?") — those are explanation, not assessment.

## Dual-surface sync

The framework content embedded in the command and the skill must stay
**identical** — editing one without the other is forbidden (it's a
harness constraint on this repo). This is why the same assessment is
produced whichever way you invoke it.

## Layout

```text
ai-readiness-assessment/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # techtalkai marketplace manifest
├── commands/
│   └── ai-readiness-assess.md
├── skills/
│   └── ai-readiness-assessment/
│       └── SKILL.md
├── tests/                   # TDAB structural test suite (contributors only)
├── CHANGELOG.md
└── HARNESS.md               # this repo's own harness
```

## Process the instrument follows

1. **Scan** — habitat-document discovery, then a broader signal scan.
2. **Present & question** — a structured summary, then 3–5 clarifying
   questions one at a time.
3. **Assess** — the fourteen-dimension profile, the cognitive read, and
   the Habitat Build Gap.
4. **Document** — write the [report](assessment-output.md).
5. **Reading path** & **Next steps** — gap-anchored book chapter and a
   single TechTalk engagement.
6. Offer the [HTML render](../how-to/render-the-html-report.md) on
   request.
