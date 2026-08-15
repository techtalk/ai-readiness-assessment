# Example: the Habitat-Thinking estate (real)

!!! info "Real assessment — run 2026-08-15 across the Habitat-Thinking estate."
    This is not a constructed example. It is an actual
    `/ai-readiness-rollup` over the reports that existed in
    [`techtalk/ai-readiness-assessment`](https://github.com/techtalk/ai-readiness-assessment)
    and
    [`Habitat-Thinking/ai-literacy-superpowers`](https://github.com/Habitat-Thinking/ai-literacy-superpowers)
    on that date, plus one subject that could not be reached. The result
    is not flattering, and it is published as it came out.

The other examples on this site are synthetic — built to show the report
shape. This one shows what the instrument actually says about the estate
that builds it.

## The manifest

```yaml
version: 1
team: habitat-thinking

subjects:
  - id: ai-readiness-assessment
    path: ../ai-readiness-assessment
  - id: ai-literacy-superpowers
    path: ../ai-literacy-superpowers
  - id: leap-companion
    path: ../leap-companion

report:
  output: assessments/
```

## Coverage ledger

| Subject | Status | Report date | Age | Note |
|---|---|---|---|---|
| ai-readiness-assessment | `degraded` | 2026-06-03 | 73d | No `assessment-summary` block; recovered from prose |
| ai-literacy-superpowers | `incompatible`, `stale` | 2026-05-11 | 96d | Produced by `/assess` (a different instrument) — no Habitat Maturity Profile, no gap |
| leap-companion | `unreachable` | — | — | Not found in the organisation |

**Assessed 2 of 3 named subjects; 1 of 3 can enter the dimension matrix.**

Read that second number carefully. Two subjects had readable reports —
but only one of them was measured against this model.

## Dimension matrix

| Subject | AB | AI | WF | OM | TP | OR | OA | HR | WP | AC | AD | Te | Ob | Gv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ai-readiness-assessment | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 2* | 3 | 2* | 2* | 4 |
| *ai-literacy-superpowers* | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| *leap-companion* | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

*AB Agent behaviour · AI Agent input · WF Workflow · OM Operating model ·
TP Teams provide · OR Output role · OA Output artefact · HR Humans review ·
WP Work patterns · AC Agent composition · AD Agents… · Te Testing ·
Ob Observability · Gv Governance*

A one-row matrix is not a matrix. It is a single assessment with extra
formatting, and the report says so rather than dressing it up.

## Gap table

| Subject | Habitat maturity mean | Cognitive level | Gap | Regime |
|---|---|---|---|---|
| ai-readiness-assessment | 2.93 | 4 | +1.07 | Ambition outpaces enablement |
| ai-literacy-superpowers | — | 5 | — | not computable |
| leap-companion | — | — | — | — |

`ai-literacy-superpowers` has a cognitive read — **L5, Sovereign
Engineering**, with all three disciplines at 5 — but no habitat maturity
mean, because its report was produced by an instrument that does not
measure the fourteen dimensions. A cognitive read without a habitat
mean cannot yield a gap. The number is genuinely absent, not withheld.

## Spread

**Not computable.**

A spread is a range across subjects, and a range needs at least two
comparable subjects. This estate currently produces one gap.

Presenting `+1.07` as "the spread" would manufacture precisely the
finding a portfolio view exists to produce. The honest statement is that
the estate cannot yet produce it — and that is a finding of its own, just
not the one anybody wanted.

**What would produce a spread:** run `/ai-readiness-assess` in
`ai-literacy-superpowers`. It is a mature habitat with a long assessment
history; it has simply never been read against *this* model.

## What the one comparable subject says

`ai-readiness-assessment` reads **+1.07 — Ambition outpaces
enablement**: cognitive L4 against a fourteen-dimension habitat mean of
L2.93, held back by Agent composition, Testing and Observability, all at
L2.

That is the instrument reporting incoherence in its own repository. The
report is 73 days old and predates a substantial amount of work on the
testing dimension, so a re-run would likely read differently — which is
itself the point: **a 73-day-old report is evidence about 73 days ago.**

## Portfolio regime

**Not asserted.**

Regime selection needs provenance proportions and a spread. With one
comparable subject and no declared habitats, there is nothing to
classify. A regime is a claim about an estate; one repository is not an
estate.

If forced to characterise it informally: two mature repositories, no
shared habitat, no lineage between their control surfaces, and a wide
difference in cognitive read (L4 against L5). That *shape* is
[Islanded](../reference/portfolio-regimes.md) — but the report does not
assert it, because the evidence required to assert it is not there.

## Split ceiling

**Not reported.** A common-weak dimension is one weak across two-thirds
or more of the assessed subjects. With one subject in the matrix, every
weak dimension is trivially "common" and the split carries no
information.

The weak dimensions of `ai-readiness-assessment` — Agent composition,
Testing, Observability — are that repository's own backlog until there is
a second comparable subject to tell local weakness from shared weakness.

## What this estate should do next

**Assess `ai-literacy-superpowers` against this model.** One command in
that repository turns a one-row matrix into a two-row one and produces
the estate's first real spread. It is the single highest-value action
available, and it costs about ten minutes.

**Re-run `ai-readiness-assessment`.** Its report predates its current
testing posture by 73 days and will be `stale` in another 17.

**Resolve `leap-companion`.** It is named in the manifest and cannot be
found. Either it has moved, it is private, or it should come out of the
scope. Leaving it as `unreachable` is honest but it is not a resting
state.

## Why this example is here

The design argument for a portfolio view is that the *spread* of gaps
across an estate is a finding no single-repository assessment can
produce. This example does not produce a spread.

That is worth publishing. The instrument was pointed at its own estate,
and what came back was: one subject comparable, one measured by a
different instrument, one missing, no spread, no regime, no split
ceiling. Every one of those is the machinery refusing to invent a
number it does not have.

A synthetic example in this slot would have shown a tidy three-row matrix
and a satisfying range. It would also have shown nothing about whether
the instrument tells the truth when the data is thin.

!!! note "This example changed the tool"
    Running it surfaced two real defects. The roll-up had no coverage
    status for a report that parses but was produced by a different
    instrument — everything was either `degraded` or `unparseable`, and
    `ai-literacy-superpowers` is neither. And nothing stopped a
    single-subject estate from having its one gap reported as a spread.
    Both were fixed before this page was written; the `incompatible`
    status and the two-subject spread rule exist because of this run.

## Rendered version

There is no HTML render of this report. The
[HTML portfolio](../reference/portfolio-report.md) is built around the
matrix, and a matrix with one populated row would be a more impressive
artefact than the data behind it deserves. When the estate has two
comparable subjects, it gets a render.
