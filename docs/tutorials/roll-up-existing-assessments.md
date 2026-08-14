# Roll up existing assessments

**About ten minutes.** By the end you will have a portfolio report
across three repositories, showing how one team's way of working fares
against three different habitats.

You need three repositories that share a team, and the plugin installed.
You do not need to re-assess anything.

## What you are building

A roll-up reads the summary block from assessments that already exist.
It runs no scan and asks no questions — which is the point. Assessing
twelve repositories interactively is a session nobody sits through, and
the behavioural questions would be the same twelve times over anyway.

## 1. Make sure each repository has an assessment

In each of the three repositories:

```text
/ai-readiness-assess
```

Then check the report ends with a summary block:

```bash
tail -5 orders-api/assessments/*-assessment.md
```

You should see the tail of a fenced `assessment-summary` block. If a
report predates that block, don't re-run anything yet — the roll-up will
recover what it can from the prose and mark the subject `degraded`.

## 2. Write the manifest

In the directory holding all three repositories:

```bash
mkdir -p .habitat
```

`.habitat/scope.yml`:

```yaml
version: 1
team: payments-tribe

subjects:
  - id: orders-api
    path: ./orders-api
  - id: billing
    path: ./billing
  - id: legacy-batch
    path: ./legacy-batch

report:
  output: assessments/
```

## 3. Run the roll-up

```text
/ai-readiness-rollup
```

It finds the manifest, reads the most recent report in each subject, and
writes `assessments/YYYY-MM-DD-portfolio.md`.

## 4. Read the coverage ledger first

The report opens with it, deliberately:

```text
| Subject      | Status   | Report date | Age  |
| orders-api   | assessed | 2026-08-02  | 12d  |
| billing      | assessed | 2026-07-28  | 17d  |
| legacy-batch | stale    | 2026-02-11  | 184d |

3 of 3 subjects assessed; 1 stale.
```

Read this before the matrix. A matrix is persuasive whether or not the
data behind it is complete, and the ledger is what tells you which.

## 5. Read the spread

Skip to **Spread**. This is the finding:

```text
Gap spread: +0.1 (orders-api) to +2.4 (legacy-batch) — range 2.3
```

The same team, the same way of working, measured against three
habitats — and one of them is a long way out of step. That number does
not exist in a single-repository assessment, because a single assessment
only ever has one reading to compare.

## 6. Read the split ceiling

The weakest dimensions, divided by who can fix them:

- **Common weak** across the estate — the enablement backlog. Nobody's
  individual team can fix these; whoever provides the habitat can.
- **Locally weak** — that subject's own backlog.

The split is what stops the matrix becoming a league table. It separates
what the estate owes its teams from what a team owes itself.

## What you will not find

There is no overall score, grade or percentage, and no averaged gap. In
the example above, averaging +0.1 and +2.4 gives +1.25 — a number
describing neither repository and suggesting no action. See
[Why there is no portfolio score](../explanation/why-no-portfolio-score.md).

## Next

- [Write a scope manifest](../how-to/write-a-scope-manifest.md)
- [Portfolio report structure](../reference/portfolio-report.md)
- [Assessment summary block](../reference/assessment-summary-block.md)
