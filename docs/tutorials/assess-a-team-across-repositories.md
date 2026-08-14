# Assess a team across repositories

**About twenty-five minutes for five repositories.** One session, one
set of behavioural questions, five per-repo reports and a portfolio
report at the end.

This is the walkthrough to use when the repositories have *not* been
assessed yet. If they already have reports, use
[roll up existing assessments](roll-up-existing-assessments.md) instead —
it is faster and asks nothing.

## Why this is one session and not five

The behavioural half of the assessment measures how *the team* works.
Running the full assessment five times would ask the same six questions
five times and get the same answer — at five times the cost, with five
chances to answer differently out of fatigue.

So the scope run asks them **once**, then spends one cheap question per
repository checking whether that answer still holds there.

## 1. Write the manifest

In the directory holding the repositories, `.habitat/scope.yml`:

```yaml
version: 1
team: payments-tribe

subjects:
  - id: orders-api
    path: ./orders-api
  - id: billing
    path: ./billing
  - id: reporting
    path: ./reporting
  - id: notifications
    path: ./notifications
  - id: legacy-batch
    path: ./legacy-batch
    posture: maintenance
```

`legacy-batch` is marked `maintenance` — still assessed and still shown,
but kept out of common-weak detection so a repository nobody is
investing in cannot set the agenda for the four that matter.

## 2. Start the run

```text
/ai-readiness-assess --scope
```

It reads the manifest and **tells you what it is about to do** before it
starts:

```text
Scope: 5 subjects (orders-api, billing, reporting, notifications,
legacy-batch). Behavioural questions asked once for payments-tribe.
```

If your estate is too large for one session, it says so here and
recommends splitting rather than starting something that will degrade
half-way through.

## 3. Answer the behavioural questions once

Three to five questions, one at a time, about how the team *normally*
works — not about any one repository. These place the six behavioural
dimensions and the cognitive level.

Answer them as a team, and answer for the general case. The exceptions
get picked up in the next step.

## 4. One question per repository

For each subject, the habitat is sensed, the eight repo-observable
dimensions are placed from that repository's evidence, and then you get
exactly one question:

> Is your way of working in `legacy-batch` materially different from
> what you described?

**Usually no.** The team read is applied, the report records
`cognitive_source: team`, and it **states in its body** that the
cognitive placement was gathered against the team's general practice.

**Sometimes yes** — and this is worth answering honestly. If you really
do work differently in one repository, say so; the six behavioural
questions are asked again for that subject and its report records
`cognitive_source: subject`.

Each report is written to that repository's own `assessments/`
directory. Each team keeps its own report.

## 5. Read the portfolio report

At the end the roll-up runs over the five reports just written.

Read it in this order:

**Coverage ledger** — first, always. Five of five, no stale rows.

**Spread** — the finding.

```text
Gap spread: −0.29 (orders-api) to +1.50 (legacy-batch) — range 1.79
```

The same engineers, the same habits, five environments. Where the range
is wide, the difference is the *habitat*, not the people. That sentence
is the entire reason to run this across repositories rather than one at
a time.

**Split ceiling** — what enablement owes the estate, versus what a
single team owes itself.

## What you have at the end

- Five per-repo reports, each owned by and living with its repository
- One portfolio report showing the spread and the split ceiling
- The behavioural questions answered once

## If the estate is large

Past roughly a dozen subjects, prefer the artefact route: run
`/ai-readiness-assess` in each repository separately — different people,
different days — and then
[roll up the reports](roll-up-existing-assessments.md). The scope run
holds one subject's evidence at a time and releases it between subjects,
but a session still has a limit, and a run that announces its size is
easier to split deliberately than to abandon half-way.

## Next

- [Subject, habitat, team](../explanation/subject-habitat-team.md) — why the unit changed
- [Assess a monorepo with several habitats](../how-to/assess-a-monorepo-with-several-habitats.md) — the inverse case
- [Portfolio report structure](../reference/portfolio-report.md)
