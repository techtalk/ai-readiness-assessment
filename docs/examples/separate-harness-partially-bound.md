# Example: separate harness repo, partially bound

!!! warning "Synthetic example — constructed to illustrate the report shape."
    These numbers are invented to show what the report looks like when a
    shared harness binds in some subjects and not others. They are not a
    reading of any real estate. The [self-assessment](../examples.md) is
    the real one.

A platform team owns `platform-harness`. Four services are meant to be
governed by it. Two are, one is pinned a year back, and one is not
bound at all.

This is the shape that matters most in practice, because on an
architecture slide all four services look identical.

## The manifest

```yaml
version: 1
team: payments-tribe

habitats:
  - id: platform-harness
    kind: repo
    path: ./platform-harness
    provides: [HARNESS.md, AGENTS.md, ci, hooks]

subjects:
  - id: orders-api
    path: ./orders-api
    habitat: platform-harness
  - id: billing
    path: ./billing
    habitat: platform-harness
  - id: reporting
    path: ./reporting
    habitat: platform-harness
  - id: legacy-batch
    path: ./legacy-batch
    habitat: platform-harness
```

## Coverage ledger

| Subject | Status | Report date | Age | Note |
|---|---|---|---|---|
| orders-api | assessed | 2026-08-01 | 13d | — |
| billing | assessed | 2026-07-29 | 16d | — |
| reporting | assessed | 2026-08-06 | 8d | harness pinned 412d |
| legacy-batch | assessed | 2026-08-02 | 12d | harness declared, not bound |

4 of 4 subjects assessed; 0 stale; 0 unreachable.

## Dimension matrix

`ᶦ` inherited · `ᵘ` inherited-unbound · unmarked is local · `*` weakest in column

| Subject | AB | AI | WF | OM | TP | OR | OA | HR | WP | AC | AD | Te | Ob | Gv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| orders-api | 3 | 3 | 4ᶦ | 3 | 4ᶦ | 3 | 3 | 3 | 3 | 3 | 3 | 4ᶦ | 3 | 4ᶦ |
| billing | 3 | 3 | 4ᶦ | 3 | 4ᶦ | 3 | 3 | 3 | 3 | 2 | 3 | 4ᶦ | 2 | 4ᶦ |
| reporting | 3 | 2 | 3ᶦ | 3 | 3ᶦ | 3 | 3 | 3 | 2 | 2 | 3 | 3ᶦ | 2 | 3ᶦ |
| legacy-batch | 2* | 1* | 1ᵘ* | 2* | 1ᵘ* | 2* | 2* | 2* | 2* | 1* | 2* | 1ᵘ* | 1* | 1ᵘ* |

*AB Agent behaviour · AI Agent input · WF Workflow · OM Operating model ·
TP Teams provide · OR Output role · OA Output artefact · HR Humans review ·
WP Work patterns · AC Agent composition · AD Agents… · Te Testing ·
Ob Observability · Gv Governance*

The `ᵘ` marks are the finding. `legacy-batch` declares
`platform-harness` in the manifest, but nothing in the repository reaches
it: its CI defines its own workflows rather than reusing the shared ones,
its `AGENTS.md` restates rules rather than deferring, and there is no
pin. Four dimensions the harness would have supplied are capped at what
local evidence supports.

`reporting` **is** bound — via a submodule pin — but the pin is 412 days
old. It is assessed against the *pinned* revision, which is why its
inherited dimensions sit a level below the two current subjects.

## Gap table

| Subject | Habitat maturity mean | Cognitive level | Gap | Regime |
|---|---|---|---|---|
| orders-api | 3.29 | 3 | −0.29 | Coherent |
| billing | 3.14 | 3 | −0.14 | Coherent |
| reporting | 2.71 | 3 | +0.29 | Coherent |
| legacy-batch | 1.50 | 3 | +1.50 | Ambition outpaces enablement |

## Spread

**−0.29 (orders-api) to +1.50 (legacy-batch) — range 1.79.**

One team, one way of working, four habitats — and the range is wide. The
same engineers who sit comfortably Coherent in `orders-api` are working
a full level and a half ahead of their environment in `legacy-batch`.
That is not a capability difference. It is an environment difference,
and it is the reason a single-repository assessment of `orders-api`
would have reported a healthy team and missed this entirely.

## Split ceiling

**Common weak — Observability, Agent composition.** Weak in three of
four subjects, including subjects where the harness *does* bind. The
shared harness does not supply these, so binding it harder will not fix
them. Enablement backlog.

**Locally weak — `legacy-batch`:** Workflow, Teams provide, Testing,
Governance. These read as local weaknesses but they are not: all four
are `inherited-unbound`. The capability exists in `platform-harness`
already. This is a **binding** failure, not a team failure, and it
belongs to whoever owns the harness.

## Confidence

56 placements: 32 `observed`, 20 `inferred`, 4 `asked`. The four `asked`
placements were spent on `legacy-batch`, confirming that the harness is
genuinely not wired up rather than bound by a mechanism the checklist
does not recognise — the report does not assert `inherited-unbound`
without that confirmation.

## What this estate should do next

**Bind the harness in `legacy-batch`.** This is the cheapest uplift
available anywhere in the estate, and it is not a build. Nobody needs to
write a testing policy or a governance model — `platform-harness` has
both. Somebody needs to make `legacy-batch` reuse the shared workflows
and defer to the shared conventions. Four dimensions move on the day it
lands.

**Refresh the `reporting` pin.** It is bound, which is the hard part.
It is 412 days behind, which is the easy part.

**Then lift observability and agent composition in the harness itself.**
Only after the binding work — doing it first would improve a harness
that half the estate cannot see.

Note the ordering. The instinct with a matrix like this is to start with
the lowest row and treat `legacy-batch` as a struggling team. The
provenance marks say otherwise: the estate's biggest number is a wiring
problem, and treating it as a capability problem would have that team
rebuild what already exists twenty metres away.

---

*Portfolio regime naming — Federated, Distributed, Fragmented,
Islanded — arrives in a later release. This example shows the shape a
distributed estate produces, without asserting the label.*

**[View this report as a shareable HTML page](separate-harness-partially-bound.html)** — a single
self-contained file, no network assets, works opened straight from disk.
