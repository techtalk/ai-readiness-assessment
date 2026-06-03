# Read the Habitat Build Gap

The Habitat Build Gap is the assessment's headline signal. It reconciles
the two reads:

```text
Habitat Build Gap = cognitive level − habitat maturity mean (all 14 dimensions)
```

Both terms sit on the same 0–5 ruler, so the gap is signed. What matters
is **coherence** — whether your thinking and your habitat are in step —
not the size of the level. See
[Coherence, not level](../explanation/coherence-not-level.md) for why.

## Find it in the report

Look for the `## Habitat Build Gap` block:

```text
Habitat Maturity Level (model):  L2  (14-dim mean L1.9)
Cognitive read (Parts A–C):      L2
Habitat Build Gap:               +0.1   (cognitive − 14-dim mean)
Interpretation:                  Coherent
```

## Act on the regime

| Regime | When | What to do |
| --- | --- | --- |
| **Coherent** (`abs(gap) < 0.5`) | Team and habitat are at the same level. | Keep both moving together. Pick the single weakest dimension and lift it; the level rises coherently. |
| **Ambition outpaces enablement** (`gap ≥ +0.5`) | You think at a higher level than your habitat supports. | **Build the habitat your thinking already implies.** The report names the dimension most worth lifting — start there (often Composition or Observability). |
| **Inherited habitat** (`gap ≤ −0.5`) | The habitat is more mature than current practice. | **Literacy uplift before more tooling.** Invest in how the team works, not in more constraints. |

## Two cautions

- **A coherent low level beats an incoherent high one.** A team at L2
  cognitive / L2 operational is healthier than one at L4 cognitive / L1
  operational. Don't chase the number.
- **The floor is not a signal.** A repo with essentially no
  AI-collaboration evidence sits at the L1 floor on every dimension; a
  small negative gap there (a cognitive-L0 repo against the L1 floor) is
  the "nothing yet" baseline, not a genuine inherited habitat.

## Next

- [The Habitat Build Gap reference](../reference/habitat-build-gap.md) — the full formula, regimes, and worked examples.
- [The fourteen dimensions](../reference/habitat-maturity-model.md) — what each axis means and how to lift it.
