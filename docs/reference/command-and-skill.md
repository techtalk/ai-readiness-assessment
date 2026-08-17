# Command & skill

The plugin ships **two pairs** of entry points — one for assessing a
single subject, one for rolling several up. Each pair is a command and a
skill carrying **identical** content, so either half produces the same
result.

| I want to… | Invoke |
|---|---|
| Assess this repository | `/ai-readiness-assess` |
| Assess **every subject in a scope**, one session | `/ai-readiness-assess --scope` |
| Summarise assessments that **already exist** across repos | `/ai-readiness-rollup` |

The last two need a [scope manifest](scope-manifest.md); with none
present, `/ai-readiness-assess` behaves exactly as it always has.

## The command

`/ai-readiness-assess` — the canonical entry point. Defined in
`commands/ai-readiness-assess.md`.

```text
/ai-readiness-assess
```

### Scope mode

With a `.habitat/scope.yml` present, `--scope` assesses every subject in
one session, asking the behavioural questions **once for the team**
rather than once per repository:

```text
/ai-readiness-assess --scope
```

Each subject gets its own report in its own `assessments/` directory,
and a portfolio report is produced at the end. See
[assess a team across repositories](../tutorials/assess-a-team-across-repositories.md).

## The roll-up command

`/ai-readiness-rollup` — summarises assessments that already exist,
across several subjects. Defined in `commands/ai-readiness-rollup.md`.

```text
/ai-readiness-rollup
```

It runs no scan and asks no questions: it reads the
[summary block](assessment-summary-block.md) from reports that are
already written. That is the recommended path for a large estate, and it
separates *who runs an assessment* from *who reads the summary*. See
[roll up existing assessments](../tutorials/roll-up-existing-assessments.md)
and the [portfolio report structure](portfolio-report.md).

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

## The roll-up skill

`ai-readiness-rollup` — the natural-language surface for the roll-up.
Defined in `skills/ai-readiness-rollup/SKILL.md`. It triggers on phrases
like:

> roll up our assessments · assess across repos · portfolio view · how do
> our repos compare · multi-repo readiness · compare our teams' habitats

## Dual-surface sync

The framework content embedded in each command and its skill must stay
**identical** — editing one without the other is forbidden (it's a
harness constraint on this repo). This is why the same result is
produced whichever way you invoke it.

Both pairs are checked by the test suite rather than by discipline: the
assertions compare the two bodies directly and name the first line that
diverges.

## Layout

```text
ai-readiness-assessment/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # techtalkai marketplace manifest
├── commands/
│   ├── ai-readiness-assess.md
│   └── ai-readiness-rollup.md
├── skills/
│   ├── ai-readiness-assessment/
│   │   └── SKILL.md
│   └── ai-readiness-rollup/
│       └── SKILL.md
├── specs/                   # intent, first-class
├── tests/                   # TDAB structural test suite (contributors only)
├── CHANGELOG.md
└── HARNESS.md               # this repo's own harness
```

## Process the instrument follows

1. **Scan** — habitat-document discovery, then a broader signal scan.
2. **Present & question** — a structured summary, then 3–5 clarifying
   questions one at a time.
3. **Assess** — the fourteen-dimension profile, the cognitive read, and
   the Habitat/Workflow Gap.
4. **Document** — write the [report](assessment-output.md).
5. **Reading path** & **Next steps** — gap-anchored book chapter and a
   single TechTalk engagement.
6. Offer the [HTML render](../how-to/render-the-html-report.md) on
   request.

In scope mode the behavioural questions in step 2 are asked **once for
the team**; each subject is then asked only whether its way of working
differs. A reused cognitive read is always declared in the report body.
