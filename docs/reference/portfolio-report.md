# Portfolio report structure

The output of `/ai-readiness-rollup`, written to
`<manifest directory>/<report.output>/YYYY-MM-DD-portfolio.md`.

Per-subject reports stay where they are. Each team keeps and owns its
own report; only the roll-up is written to the scope root.

## Sections, in order

### 1. Coverage ledger

Every subject named in the manifest, with its status:

| Status | Meaning |
|---|---|
| `assessed` | Report found and its summary block parsed. |
| `stale` | Assessed, but the report is more than 90 days old. |
| `degraded` | No summary block; values recovered from prose. |
| `incompatible` | Report parses, but was produced by a different instrument — no Habitat Maturity Profile and no gap, so it cannot enter the matrix. |
| `unparseable` | Report found but nothing could be read from it. |
| `unreachable` | Path unreadable, or no assessment exists there. |

`incompatible` is **not** a lesser `degraded`. A degraded report measured
the right things and merely predates the summary block; an incompatible
one measured different things. Collapsing them would report a subject as
nearly-there when it has not been assessed against this model at all —
see the [real estate example](../examples/habitat-thinking-estate.md),
which is where the distinction came from.

It comes first, and it is built before any analysis. Analysis that
starts before coverage is established has a habit of describing the
readable subjects as though they were the estate.

The ledger states the position plainly: *"6 of 9 subjects assessed; 2
stale; 1 unreachable."*

### 2. Dimension matrix

Subjects as rows, the fourteen model dimensions as columns, level in the
cell. The weakest cell in each column is marked.

This is the artefact people screenshot, which is exactly why the
coverage ledger sits above it.

### 3. Gap table

Per subject: habitat maturity mean, cognitive level, signed gap, and
[regime](habitat-workflow-gap.md).

### 4. Spread

Minimum gap, maximum gap, the range between them, and the two subjects
at the extremes named with a line each on what differs.

**This is the headline finding.** One cognitive read against several
habitats produces several gaps, and their spread is the thing a
single-repo assessment structurally cannot show.

A spread needs **at least two comparable subjects** — two that each yield
a gap. With fewer, the report says the spread is not computable and names
what would produce one. Presenting a single subject's gap as a range
would manufacture exactly the finding the portfolio view exists to
produce.

### 5. Split ceiling

The weakest dimensions, divided by who owns them:

- **Common weak** — weak in two-thirds or more of the assessed subjects.
  The enablement backlog, owned by whoever provides the habitat.
- **Locally weak** — weak in one or two subjects. That team's backlog.

### 6. Confidence

How many placements feeding the matrix were `asked` or `inferred` rather
than `observed`, and any subject with more than five inferred dimensions
flagged as thin evidence. Aggregation must not launder a guess into a
confident portfolio claim.

### 7. Steer

One portfolio-level steer, plus a steer for outlier subjects only —
never one per subject. A steer per row reads as a spreadsheet rather
than as advice.

## What the report never contains

No overall grade, no percentage, no averaged gap across subjects. See
[Why there is no portfolio score](../explanation/why-no-portfolio-score.md)
for the argument; the short version is that the average erases the
spread, which is the only thing the portfolio view adds.

Under partial coverage the ceiling is never described as estate-wide.
With six of fourteen subjects readable, it is the ceiling *of the six*,
and the report says which.
