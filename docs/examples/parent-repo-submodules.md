# Example: parent repo with submodules

!!! warning "Synthetic example — constructed to illustrate the report shape."
    These numbers are invented to show what the report looks like when a
    shared harness binds everywhere. They are not a reading of any real
    estate. The [self-assessment](../examples.md) is the real one.

One `HARNESS.md` at the root of a parent repository, three application
submodules underneath, all bound to it.

## The manifest

```yaml
version: 1
team: platform-group

habitats:
  - id: root-harness
    kind: self
    path: .
    provides: [HARNESS.md, AGENTS.md, ci]

subjects:
  - id: web
    path: ./web
    habitat: root-harness
  - id: api
    path: ./api
    habitat: root-harness
  - id: workers
    path: ./workers
    habitat: root-harness
```

## Coverage ledger

| Subject | Status | Report date | Age | Note |
|---|---|---|---|---|
| web | assessed | 2026-08-04 | 10d | — |
| api | assessed | 2026-08-04 | 10d | — |
| workers | assessed | 2026-08-05 | 9d | — |

3 of 3 subjects assessed; 0 stale; 0 unreachable.

## Dimension matrix

`ᶦ` inherited · `ᵘ` inherited-unbound · unmarked is local · `*` weakest in column

| Subject | AB | AI | WF | OM | TP | OR | OA | HR | WP | AC | AD | Te | Ob | Gv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| web | 3 | 3 | 4ᶦ | 3 | 4ᶦ | 3 | 3ᶦ | 3 | 3 | 3 | 3 | 3 | 2* | 4ᶦ |
| api | 3 | 3 | 4ᶦ | 3 | 4ᶦ | 3 | 3ᶦ | 3 | 3 | 3 | 3 | 3 | 3 | 4ᶦ |
| workers | 3 | 2* | 4ᶦ | 3 | 4ᶦ | 3 | 3ᶦ | 3 | 2* | 2* | 3 | 2* | 2* | 4ᶦ |

*AB Agent behaviour · AI Agent input · WF Workflow · OM Operating model ·
TP Teams provide · OR Output role · OA Output artefact · HR Humans review ·
WP Work patterns · AC Agent composition · AD Agents… · Te Testing ·
Ob Observability · Gv Governance*

Five dimensions are `inherited` in every subject, and **none are
`inherited-unbound`**. The root harness reaches all three submodules —
each subject's CI reuses the root workflows and each `AGENTS.md` defers
to the root file rather than restating it.

## Gap table

| Subject | Habitat maturity mean | Cognitive level | Gap | Regime |
|---|---|---|---|---|
| web | 3.14 | 3 | −0.14 | Coherent |
| api | 3.21 | 3 | −0.21 | Coherent |
| workers | 2.86 | 3 | +0.14 | Coherent |

## Spread

**−0.21 (api) to +0.14 (workers) — range 0.35.**

A narrow spread is the signature of a habitat that genuinely reaches
everything it claims to. The same team, working the same way, meets
substantially the same environment in all three submodules. What differs
between the extremes is small: `api` has slightly more observability
wired up; `workers` has thinner test and composition coverage.

## Split ceiling

**Common weak — Observability.** Weak in two of three subjects. This is
the enablement backlog: the root harness does not supply observability
scaffolding, so each submodule is left to invent it. Fixing it once at
the root fixes it three times.

**Locally weak — `workers`:** Agent input, Work patterns, Agent
composition, Testing. These are that team's own backlog and do not
generalise.

## Confidence

42 placements feed the matrix: 24 `observed`, 18 `inferred`, 0 `asked`.
No subject exceeds five inferred dimensions.

## What this estate should do next

Lift observability **at the root**, not in each submodule. It is the one
dimension weak across the estate, and the binding already works — a
change to the root harness propagates without asking three teams to do
anything.

Leave the `workers` gaps to the `workers` team. They are real but local,
and pulling them into an estate-wide programme would slow the fix and
blur who owns it.

Do not chase the levels. All three subjects are Coherent; nothing here
is out of step with itself.

---

*Portfolio regime naming — Federated, Distributed, Fragmented,
Islanded — arrives in a later release. This example shows the shape a
federated estate produces, without asserting the label.*

**[View this report as a shareable HTML page](parent-repo-submodules.html)** — a single
self-contained file, no network assets, works opened straight from disk.
