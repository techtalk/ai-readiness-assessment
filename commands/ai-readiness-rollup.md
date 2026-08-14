---
name: ai-readiness-rollup
description: Roll up existing AI readiness assessments across several repositories into one portfolio report. Reads the assessment-summary block from reports that already exist — no re-assessment, no behavioural questions — and produces a coverage ledger, a dimension matrix, the gap spread, and a split ceiling.
---

# /ai-readiness-rollup

Summarise AI readiness across several subjects, using assessments that
already exist.

This command is fully self-contained — it does **not** depend on any
plugin skills, agents, sub-commands, or external services. Everything it
needs is below.

Run `/ai-readiness-assess` first in any subject that has no assessment
yet: a roll-up reads reports, it does not produce them.

---

## What a roll-up is

A roll-up reads the machine-readable `assessment-summary` block from
reports that already exist and assembles them into one portfolio view.
It runs no scan, asks no behavioural questions, and writes no per-subject
report.

That restraint is the design. Twelve repositories at ten minutes each,
with the behavioural questions asked twelve times, is not a session
anyone sits through, and a single pass over twelve repositories exhausts
context long before it finishes. Reading artefacts instead of
re-assessing also separates *who runs the assessment* from *who reads
the summary*, which is what a consultancy engagement actually needs: each
team keeps and owns its own report, and the portfolio view is assembled
from what they produced.

### The unit

The assessment unit is **subject × governing habitat**, with the
cognitive read scoped to the **team**:

- **Subject** — the code artefacts under examination: a repository, a
  submodule, or a directory inside a monorepo.
- **Habitat** — the harness and control surfaces governing that subject.
- **Team** — the people whose behaviour produces the cognitive read.
  Never a repository.

### What the roll-up is for

One cognitive read measured against *N* different habitats produces *N*
different gaps, and **the spread of those gaps is the headline finding**.
A team can sit Coherent in the greenfield service and deep in
Ambition-outpaces-enablement in the legacy one. The enablement work those
two facts imply is completely different, and a single-repository
assessment cannot surface the difference because it only ever has one
reading to compare.

### There is no portfolio score

The roll-up never reduces the estate to one number. It produces no
overall grade, no percentage, and never an averaged gap across subjects.

This is a design position, not a missing feature. Averaging destroys the
spread — the exact signal the portfolio view exists to expose. An estate
with one Coherent subject and one badly incoherent subject averages to
"slightly incoherent", which describes neither subject and points at no
action. The portfolio headline is **a distribution and a ceiling**.

If asked for the single number anyway, decline and show the spread and
the split ceiling instead. They answer the question the number was
standing in for.

## The scope manifest

The roll-up is driven by `.habitat/scope.yml`.

```yaml
version: 1
team: payments-tribe          # the cognitive read is scoped to this

habitats:                     # optional — omit when every subject governs itself
  - id: platform-harness
    kind: repo                # repo | submodule | self
    path: ../platform-harness
    provides: [HARNESS.md, AGENTS.md, hooks, skills, agents, ci]

subjects:
  - id: orders-api
    path: ../orders-api       # repo, submodule, or directory
    habitat: platform-harness # omit ⇒ self-governed
    posture: active           # active | maintenance | archived
  - id: billing
    paths:                    # one logical subject, several paths
      - ../billing-contract
      - ../billing-impl
    habitat: platform-harness
  - id: legacy-batch
    path: ../legacy-batch
    posture: maintenance

report:
  output: assessments/        # roll-up destination, relative to the manifest
```

`provides` is a hint about what the shared habitat offers. It is never
taken as proof — a declared artefact still has to bind to a subject
before it raises anything there.

**Posture.** `posture` changes how a subject feeds the portfolio, never
whether it is reported:

| Posture | In the matrix | Feeds the ceiling |
|---|---|---|
| `active` (default) | yes | yes |
| `maintenance` | yes | excluded from common-weak detection |
| `archived` | yes, marked as archived | excluded entirely |

Without this a single dead repository pins the estate's ceiling
permanently, and every report afterwards leads with a finding nobody
intends to act on. An archived subject is still shown — hiding it would
misstate the coverage — but it does not set the agenda.

**Validation.** `subjects` must be non-empty, and each subject needs an
`id` and exactly one of `path` or `paths`. Every `id` must be unique
across both `subjects` and `habitats`. A path that cannot be read is **not** an error — record it in
the coverage ledger as `unreachable` and carry on. Keys not described
here produce a warning and are then ignored: the schema grows over later
releases, and a manifest written today must keep working.

Stop with a clear message naming the problem when the manifest is
absent, has no `subjects`, has a duplicate `id`, or when a subject's
`habitat` names no declared habitat — name the bad reference.

## Procedure

### 1. Locate the manifest

Look for `.habitat/scope.yml` in the working directory, then upward at
most three levels. If none is found, say so, show the minimal manifest
above, name the directory where it should be written, and stop.

Do not guess a scope. Inferring the estate from sibling directories
produces a portfolio report whose coverage nobody can check.

### 2. Collect each subject's most recent report

For each subject, read `<path>/assessments/` and take the report with
the most recent date in its filename. Then parse it, in this order:

1. **`assessment-summary` block present** — use it. Status `assessed`.
2. **No block, prose parseable** — recover what the headings give: the
   Habitat Maturity Level, the cognitive read, the gap and its regime,
   and any dimension levels stated in the Habitat Maturity Profile
   table. Status `degraded`.
3. **Neither** — status `unparseable`.

A report whose most recent assessment is older than 90 days is `stale`
as well as `assessed`; report the age and keep its data.

### 3. Build the coverage ledger before any analysis

Build it first, deliberately. Analysis that starts before coverage is
established tends to describe the readable subjects as if they were the
estate.

### 4. Write the report

Write to `<manifest directory>/<report.output>/YYYY-MM-DD-portfolio.md`
using the structure below. Per-subject reports are never rewritten or
moved — they belong to their subjects.

## Report structure

```markdown
# AI Readiness Portfolio — <team>

**Subjects assessed**: N of M
**Gap spread**: <min> to <max> (range <max − min>)
**Portfolio ceiling**: <common-weak dimensions> (estate) · <locally-weak> (per subject)
**Date**: YYYY-MM-DD

## Coverage ledger

| Subject | Status | Report date | Age | Note |
|---|---|---|---|---|
| orders-api | assessed | 2026-07-02 | 43d | — |
| billing | stale | 2026-01-11 | 216d | re-run recommended |
| legacy-batch | unreachable | — | — | path not readable |

<one plain sentence: "6 of 9 subjects assessed; 2 stale; 1 unreachable.">

## Dimension matrix

Subjects by the model's fourteen dimensions. The weakest cell in each
column is marked — that is the dimension's estate-wide ceiling.

Where a report records `provenance`, mark it in the cell: a level
reached through an *inherited* rule is a different fact from one reached
locally, and an `inherited-unbound` dimension is a different fact again —
the shared habitat declares it and nothing in that subject enforces it.
Use a consistent notation and give it a key beneath the matrix.

| Subject | Agent behaviour | Agent input | Workflow | Operating model | Teams provide | Output role | Output artefact | Humans review | Work patterns | Agent composition | Agents… | Testing | Observability | Governance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| orders-api | 3 | 2 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 2* | 3 | 2* | 2* | 3 |

## Gap table

| Subject | Habitat maturity mean | Cognitive level | Gap | Regime |
|---|---|---|---|---|
| orders-api | 2.93 | 4 | +1.07 | Ambition outpaces enablement |

## Spread

<min gap, max gap, range. Name the two subjects at the extremes, one
line each on what differs between them. This is the headline finding —
lead the reader to it, do not bury it under the matrix.>

## Split ceiling

**Common weak** — dimensions weak in two-thirds or more of the assessed
subjects, counting `active` subjects only. This is the enablement
backlog; it belongs to whoever provides the habitat, not to any one team.
`maintenance` subjects are reported but excluded from this count, and
`archived` subjects are excluded from the ceiling entirely.

**Locally weak** — dimensions weak in one or two subjects only. This is
that team's own backlog.

## Portfolio regime

**<Federated | Distributed | Fragmented | Islanded>**

<the evidence that produced it: provenance counts, spread, declared
habitats, duplicated artefacts found. Then the structural move that fits
— bind, extract, transfer, or hold.>

<declared variance, where any: the dimension, the subject, and the
stated reason. Listed as declared, never as drift.>

## Confidence

<count of asked and inferred placements feeding the matrix. Name any
subject where more than five dimensions are inferred — its row is thin
evidence and should be read as indicative, not measured.>

## Steer

<one portfolio-level steer. Then a steer for outlier subjects only —
never one per subject. A steer per row reads as a spreadsheet, not as
advice.>
```

## Portfolio regimes

A second axis, parallel to the per-subject gap regimes and read the same
way — a **regime, not a score**. It names what *kind* of multi-repo
situation this is, and the one structural move that fits it.

| Regime | Shape | Steer |
|---|---|---|
| **Federated** | Shared habitat, bound across subjects, narrow gap spread | Hold. Maintain the binding; watch the pin ages. |
| **Distributed** | Shared habitat present, unbound or stale in several subjects | **Bind what already exists** — usually the cheapest uplift in the estate. |
| **Fragmented** | Per-subject habitats, high near-duplication, diverged | **Extract the common layer.** |
| **Islanded** | Per-subject habitats, little duplication, wide spread | **Transfer knowledge.** One team is materially ahead; move people, not files. |

### Choosing one

Four coarse inputs. Keep them legible — a regime a reader cannot check
is worse than no regime at all.

1. **Are shared habitats declared?** This picks the axis: declared →
   Federated / Distributed; none → Fragmented / Islanded.
2. **Provenance proportions** — `inherited` against `inherited-unbound`
   across all assessed subjects.
3. **Near-duplication across control surfaces** (below).
4. **Gap spread** — the range already computed for the spread section.

Then:

- Shared habitat, mostly `inherited`, narrow spread → **Federated**.
- Shared habitat, `inherited-unbound` or stale pins in several subjects
  → **Distributed**. The steer is to bind the harness that exists, not
  to extend it.
- No shared habitat, several subjects carrying near-identical but
  diverged control surfaces → **Fragmented**, reported as *fragmented
  with lineage*.
- No shared habitat, little duplication, wide spread → **Islanded**.

### Never assert a regime without showing why

State the evidence in the report: the provenance counts, the spread, how
many habitats were declared, and which duplicated artefacts were found.

A regime is a claim about somebody's estate. An unevidenced one is
indistinguishable from a guess, and it will be argued with rather than
acted on.

Where the inputs disagree — a declared habitat that binds nowhere *and*
heavy duplication — say so and name both, rather than forcing a single
label onto an estate that is genuinely in two states at once.

### Near-duplicate detection

Coarse and legible. A duplicated control surface reads as all three of:

- the **same artefact name** across subjects (`HARNESS.md`,
  `.github/workflows/ci.yml`, `CLAUDE.md`);
- **substantially overlapping content** — the same sections, rules and
  structure; and
- **divergent specifics** — the copies have drifted apart.

All three together is *fragmented with lineage*: the artefacts share an
ancestor and have been maintained separately since. Report **where** they
diverged, because that is what an extraction would have to reconcile,
and it is the part nobody remembers.

Two subjects with the same filename and unrelated content are not
duplication. Do not report it.

### Declared variance is not drift

A subject may declare `justified_variance` in the manifest:

```yaml
subjects:
  - id: legacy-batch
    path: ../legacy-batch
    justified_variance:
      - dimension: testing
        reason: COBOL batch; harness test tooling does not apply
```

Named dimensions are **suppressed from drift findings and from
extraction candidates**, and are **listed in the report as declared
variance**, with their reason.

Listed, not hidden — a reader must be able to see what was excluded and
disagree with it. But an estate where testing or observability genuinely
cannot be uniform must not be nagged toward a convergence that would
make it worse.

## Rules that hold throughout

- **Honesty flags survive aggregation.** Every placement carries the
  `confidence` its report recorded. An `inferred` placement stays
  visibly inferred in the matrix and in the confidence section; it is
  never presented as a measured fact because it was aggregated.
- **Reused cognitive reads are declared.** Where a subject's report
  records `cognitive_source: team`, its cognitive placement was gathered
  against the team's general practice rather than that subject. Say so in
  the body of the portfolio report. Silent reuse is a lie about evidence.
- **A subject that was asked separately is shown separately.** Where a
  subject records `cognitive_source: subject` inside a scope run, the
  team said their way of working there is materially different. Its gap
  is not evidence about the team's general pattern, and the spread
  section should say which subjects carry their own read.
- **Never claim an estate-wide ceiling under partial coverage.** With
  six of fourteen subjects readable, the ceiling is the ceiling *of the
  six*. Say which.
- **Degraded rows are marked wherever they appear**, not only in the
  ledger. A row recovered from prose has no confidence data, and a
  reader scanning the matrix must be able to see that.
- **The weakest dimensions name the ceiling** — per subject and per
  portfolio. Do not average dimensions into a subject score.
- **An unbound rule is not a weak team.** Where several subjects share a
  habitat and a dimension is `inherited-unbound` across them, that is a
  *binding* failure, not a capability failure. It belongs in the common-weak
  column — the enablement backlog — and the steer is to bind what already
  exists rather than to build anything new. Name the subjects and the
  artefact expected to bind.

## Report to the user

Present in chat, briefly:

- Coverage: "N of M subjects assessed", and what is missing
- The spread, with the two extreme subjects named
- The split ceiling: what enablement owes the estate, what individual
  teams owe themselves
- The one portfolio steer
- The path to the written report

Lead with coverage. A portfolio report that reads as complete when it
covers half the estate is worse than no portfolio report.
