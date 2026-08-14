# Extract or bind

Two estates arrive at the same complaint: *"our repos are all
different, and nothing we write centrally seems to stick."*

One of them should extract a shared layer. The other should not touch a
single file — it should move a person. Getting this backwards is
expensive, and the surface symptoms are identical.

## The two situations

**Case 1 — a shared habitat exists.** A platform team wrote a harness.
It is declared, referenced in the architecture deck, and genuinely good.
The question is whether anything in each subject actually *reaches* it.

**Case 2 — no shared habitat.** Each team built its own control
surfaces. The question is whether those surfaces share an ancestor.

The [portfolio regimes](../reference/portfolio-regimes.md) split each
case in two, and the steers do not transfer between them.

## Case 1: bind before you extend

An estate with a declared harness that binds in one subject and not in
three is **Distributed**, and the instinct it provokes is almost always
wrong.

The instinct is to improve the harness. More rules, more coverage,
another round of adoption comms. But the harness is not the problem —
three-quarters of the estate cannot see the one that exists. Improving
it makes a better artefact that still reaches one subject.

**Binding is the cheapest uplift available in the whole estate**, and it
is not a build. Nobody writes a testing policy or a governance model;
they already exist. Somebody makes the subject reuse the shared
workflows and defer to the shared conventions. Several dimensions move
the day it lands.

The tell that you are here: `inherited-unbound` marks in the matrix, and
a spread driven by the subjects carrying them.

## Case 2: extract only what has lineage

An estate with no shared habitat splits on one question: **do the
per-subject control surfaces share an ancestor?**

**Fragmented** — several subjects carry near-identical but diverged
copies of the same artefact. Somebody copied a `HARNESS.md` four times
and four teams maintained it separately. That is a genuine extraction
candidate, and the divergences are the work: they encode four local
decisions, some of which are real requirements and some of which are
accidents nobody remembers making.

**Islanded** — each subject's habitat is genuinely its own, with little
overlap, and the spread is wide because one team is materially further
along.

Extraction is the wrong move here, and it is the move people reach for.
There is no common layer to extract; there is one team that has figured
something out and three that have not. Consolidating four unrelated
habitats into one produces an artefact that fits nobody and erases the
local knowledge that made the leading team effective.

**Move people, not files.** Rotate someone from the leading team.
Have them run the assessment with another team and explain their own
report. What transfers is the reasoning, and the reasoning is not in the
files.

## Why the distinction is easy to miss

Fragmented and Islanded look the same from a distance: four repos, four
different habitats, wide spread, no central harness. The matrix rows
look similarly ragged.

The difference is only visible if you actually read the control
surfaces and ask whether they are *versions of each other*. That is why
near-duplicate detection requires all three of a shared name,
overlapping content, **and** divergence — any two of those without the
third is a coincidence, and acting on a coincidence starts a
consolidation programme against files that were never related.

## Declared variance is not drift

Some divergence is correct and should stay. A COBOL batch job cannot
adopt the harness's test tooling; a data pipeline's observability will
not look like a web service's.

An estate can declare those exceptions, and the report lists them as
**declared** rather than reporting them as drift. This is not a
loophole — it is listed in the open precisely so a reader can disagree
with it. Without it the report generates a permanent backlog of
"convergence" work that nobody should do, and the honest response is to
stop reading the report.

## The short version

| You see | You are | Do |
|---|---|---|
| Harness declared, `inherited-unbound` in several subjects | Distributed | Bind it. Do not extend it. |
| Harness declared, `inherited` throughout, narrow spread | Federated | Hold. Watch the pins. |
| No harness, near-duplicate diverged artefacts | Fragmented | Extract, and reconcile the divergences deliberately. |
| No harness, unrelated artefacts, wide spread | Islanded | Move people. Leave the files alone. |
