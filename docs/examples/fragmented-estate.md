# Example: fragmented estate

!!! warning "Synthetic example — constructed to illustrate the report shape."
    These numbers are invented to show what the report looks like for an
    estate with no shared harness and several diverged copies of the same
    control surfaces. They are not a reading of any real estate. The
    [self-assessment](../examples.md) is the real one.

Five service repositories, each with its own habitat, plus one legacy
repository nobody is investing in. No shared harness is declared —
because none exists.

## The manifest

```yaml
version: 1
team: commerce-platform

subjects:
  - id: checkout
    path: ./checkout
  - id: search
    path: ./search
  - id: inventory
    path: ./inventory
  - id: pricing
    path: ./pricing
  - id: fulfilment
    path: ./fulfilment
  - id: legacy-batch
    path: ./legacy-batch
    posture: maintenance
    justified_variance:
      - dimension: testing
        reason: COBOL batch; harness test tooling does not apply
```

## Coverage ledger

| Subject | Status | Report date | Age | Note |
|---|---|---|---|---|
| checkout | assessed | 2026-08-05 | 9d | — |
| search | assessed | 2026-08-05 | 9d | — |
| inventory | assessed | 2026-08-06 | 8d | — |
| pricing | assessed | 2026-08-07 | 7d | — |
| fulfilment | assessed | 2026-08-07 | 7d | — |
| legacy-batch | assessed | 2026-08-08 | 6d | maintenance |

6 of 6 subjects assessed; 0 stale; 0 unreachable.

## Dimension matrix

All placements are `local` — no habitat is declared, so nothing is
inherited. `*` marks the weakest cell in the column.

| Subject | AB | AI | WF | OM | TP | OR | OA | HR | WP | AC | AD | Te | Ob | Gv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| checkout | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 |
| search | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 |
| inventory | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 |
| pricing | 2 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| fulfilment | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 |
| *legacy-batch* (maintenance) | 2* | 1* | 1* | 2* | 1* | 2* | 2* | 2* | 2* | 1* | 2* | 1* | 1* | 1* |

*AB Agent behaviour · AI Agent input · WF Workflow · OM Operating model ·
TP Teams provide · OR Output role · OA Output artefact · HR Humans review ·
WP Work patterns · AC Agent composition · AD Agents… · Te Testing ·
Ob Observability · Gv Governance*

## Gap table

| Subject | Habitat maturity mean | Cognitive level | Gap | Regime |
|---|---|---|---|---|
| fulfilment | 3.14 | 3 | −0.14 | Coherent |
| checkout | 2.86 | 3 | +0.14 | Coherent |
| search | 2.79 | 3 | +0.21 | Coherent |
| inventory | 2.79 | 3 | +0.21 | Coherent |
| pricing | 2.21 | 3 | +0.79 | Ambition outpaces enablement |
| *legacy-batch* | 1.50 | 3 | +1.50 | Ambition outpaces enablement |

## Spread

**Across active subjects: −0.14 (fulfilment) to +0.79 (pricing) — range
0.93.** Including `legacy-batch`, the range is 1.64; it is reported but
marked `maintenance`, so it does not set the agenda.

Four of the five active services cluster tightly. `pricing` is the
outlier, and `fulfilment` is the only subject whose habitat is slightly
ahead of the team's cognitive read.

## Portfolio regime

**Fragmented — with lineage.**

The evidence:

- **No habitats declared**, and no `inherited` or `inherited-unbound`
  provenance anywhere. All 84 placements are `local`. That rules out
  Federated and Distributed.
- **Four services carry a `HARNESS.md` descended from a common
  ancestor** — `checkout`, `search`, `inventory` and `pricing`. Same
  section structure, same rule names, same opening paragraph;
  diverged bodies. `fulfilment` wrote its own, which shares nothing.
- **Moderate spread (0.93 across active subjects)**, which separates
  this from Islanded — the estate is not one team pulling ahead of
  three, it is four copies of the same thing drifting.

### Where the copies diverged

| Artefact | Subjects | Divergence |
|---|---|---|
| `HARNESS.md` | checkout, search, inventory, pricing | Constraint list identical in checkout/search; inventory added two agent-composition rules; pricing is missing the CI-gate section entirely and still carries the original's TODO markers |
| `.github/workflows/ci.yml` | checkout, search, inventory | Same job structure; three different Python versions and two different coverage thresholds |
| `CLAUDE.md` | all five services | Same preamble; five different sets of project-specific conventions — genuinely divergent, not drift |

`pricing` is the clearest lineage case: it is an *older* copy that never
received the CI-gate section the other three have, which is most of why
its gap is the widest among active subjects.

### Declared variance

| Subject | Dimension | Reason |
|---|---|---|
| legacy-batch | Testing | COBOL batch; harness test tooling does not apply |

Listed, not hidden. `legacy-batch`'s L1 Testing is **not** reported as
drift and **not** treated as an extraction candidate.

## Split ceiling

**Common weak — Agent composition, Observability.** Weak in four of the
five active subjects. Neither is present in any of the copied harnesses,
so every team has been left to invent them and four have not. This is
the enablement backlog.

**Locally weak — `pricing`:** Agent behaviour, Operating model, Output
role, Humans review, Agents…, Testing, Governance. `pricing` is behind
across the board, and the lineage analysis says why: it is running an
older copy of the shared ancestor.

`legacy-batch` is excluded from common-weak detection by its
`maintenance` posture. Without that exclusion it would set the ceiling on
eleven of fourteen dimensions and every one of those findings would be
noise.

## Confidence

84 placements: 48 `observed`, 36 `inferred`, 0 `asked`. No subject
exceeds five inferred dimensions.

## What this estate should do next

**Extract the common layer — and treat the divergences as the work.**
Four services are maintaining four copies of one harness. The extraction
is not the hard part; reconciling what the copies disagree about is.
Three Python versions and two coverage thresholds encode four local
decisions, and some of those are real requirements while others are
accidents nobody remembers making. Go through them deliberately rather
than picking the newest copy and declaring it canonical.

**Start with `pricing`.** It is the widest active gap and the cheapest
to close, because it is not missing capability — it is missing the CI-gate
section the other three copies already have.

**Put agent composition and observability into the extracted layer, not
into each service.** They are weak in four of five subjects precisely
because no copy of the ancestor ever had them.

**Leave `fulfilment`'s harness alone for now.** It shares no lineage
with the other four, it is the only subject whose habitat is ahead of
the team, and folding it into the extraction would mean reconciling a
fifth unrelated design for no benefit. Read it after the extraction
lands, and take what is good from it then.

---

*This estate is **Fragmented**, not **Islanded** — the distinction
matters. If those five habitats shared nothing, extraction would be the
wrong move and the answer would be to move people instead. See
[Extract or bind](../explanation/extract-or-bind.md).*

**[View this report as a shareable HTML page](fragmented-estate.html)** — a single
self-contained file, no network assets, works opened straight from disk.
