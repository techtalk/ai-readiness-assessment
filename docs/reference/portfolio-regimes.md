# Portfolio regimes

A second axis, parallel to the per-subject
[gap regimes](habitat-workflow-gap.md) and read the same way: **a
regime, not a score**. It names what *kind* of multi-repo situation an
estate is in, and the one structural move that fits it.

| Regime | Shape | Steer |
|---|---|---|
| **Federated** | Shared habitat, bound across subjects, narrow gap spread | Hold. Maintain the binding; watch the pin ages. |
| **Distributed** | Shared habitat present, unbound or stale in several subjects | **Bind what already exists** — usually the cheapest uplift in the estate. |
| **Fragmented** | Per-subject habitats, high near-duplication, diverged | **Extract the common layer.** |
| **Islanded** | Per-subject habitats, little duplication, wide spread | **Transfer knowledge.** One team is materially ahead; move people, not files. |

See [Extract or bind](../explanation/extract-or-bind.md) for why the
steers differ so sharply, and how to tell Fragmented from Islanded.

## The four inputs

Selection is deliberately coarse. A regime a reader cannot check for
themselves is worse than no regime at all.

| Input | What it contributes |
|---|---|
| **Declared habitats** | Picks the axis. Declared → Federated / Distributed. None → Fragmented / Islanded. |
| **Provenance proportions** | `inherited` against `inherited-unbound` across assessed subjects. Separates a harness that binds from one that only exists. |
| **Near-duplication** | Whether per-subject control surfaces share an ancestor. Separates Fragmented from Islanded. |
| **Gap spread** | The range already computed for the spread section. |

### The decision

- Shared habitat, mostly `inherited`, narrow spread → **Federated**
- Shared habitat, `inherited-unbound` or stale pins in several subjects → **Distributed**
- No shared habitat, several near-identical but diverged control surfaces → **Fragmented**
- No shared habitat, little duplication, wide spread → **Islanded**

Where the inputs disagree — a declared habitat that binds nowhere *and*
heavy duplication — the report names **both**, rather than forcing one
label onto an estate that is genuinely in two states at once.

## Regime claims carry their evidence

A regime is a claim about somebody's estate, so the report always states
what produced it: the provenance counts, the spread, how many habitats
were declared, and which duplicated artefacts were found.

An unevidenced classification is indistinguishable from a guess, and it
gets argued with rather than acted on.

## Near-duplicate detection

A duplicated control surface reads as **all three** of:

1. the **same artefact name** across subjects — `HARNESS.md`,
   `.github/workflows/ci.yml`, `CLAUDE.md`;
2. **substantially overlapping content** — the same sections, rules and
   structure;
3. **divergent specifics** — the copies have drifted apart.

All three together is reported as **fragmented with lineage**: the
artefacts share an ancestor and have been maintained separately since.
The report names where they diverged, because that is what an extraction
has to reconcile — and it is the part nobody remembers.

Two subjects with the same filename and unrelated content are not
duplication, and are not reported as such.

## Declared variance

Divergence is not always drift. A manifest can declare it:

```yaml
subjects:
  - id: legacy-batch
    path: ../legacy-batch
    justified_variance:
      - dimension: testing
        reason: COBOL batch; harness test tooling does not apply
```

Named dimensions are **suppressed** from drift findings and extraction
candidates, and **listed** in the report as declared variance with their
reason.

Listed, not hidden — a reader must be able to see what was excluded and
disagree with it. Suppressed, because an estate where testing or
observability genuinely cannot be uniform should not be nagged toward a
convergence that would make it worse.

## What a regime is not

It is not a score, a grade, or a ranking of estates. Like the gap
regimes it tells you *which way to invest*, not how well you are doing.
An Islanded estate is not worse than a Federated one — it needs
different work.
