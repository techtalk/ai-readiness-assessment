# The Habitat Build Gap

The Habitat Build Gap is the coherence diagnostic that reconciles the two
reads — the [cognitive level](cognitive-ladder.md) (what the team can
think and do) against the [habitat maturity](habitat-maturity-model.md)
its environment actually delivers.

## The formula

```text
Habitat Build Gap = cognitive level − habitat maturity mean
```

`habitat maturity mean` is the arithmetic mean of **all fourteen**
dimension placements — the same mean behind the Habitat Maturity Level.
The cognitive level is 0–5 and the maturity mean is 1–5; both sit on the
same 0–5 ruler, so the gap is signed (positive or negative).

## Interpretation regimes

Working defaults — recalibrate after a quarter of use:

| Gap | Regime | Meaning |
|---|---|---|
| `abs(gap) < 0.5` | **Coherent** | Team and habitat are at the same level; collaboration is well-supported by the environment. |
| `gap ≥ +0.5` | **Ambition outpaces enablement** | The team thinks at a higher level than the habitat supports. Build the habitat the team's thinking already implies. |
| `gap ≤ −0.5` | **Inherited habitat** | The habitat is more mature than current practice. Literacy uplift before further harness extension. |

The headline signal is **coherence, not the size of the level**. A
coherent L2/L2 team is healthier than an incoherent L4-cognitive /
L1-operational one. A positive gap points at habitat investment; a
negative gap points at literacy uplift.

## The floor caveat

At the very bottom of the scale, the dimensions sit at their L1 floor
when a repo has essentially no AI-collaboration evidence. Read a small
negative gap there (a cognitive-L0 repo against the L1 floor) as the
"nothing yet" baseline, **not** a genuine inherited habitat.

## Worked examples

A verification-disciplined team with no habitat documents:

```text
Habitat Maturity Level (model):  L2  (14-dim mean L1.86)
Cognitive read (Parts A–C):      L2
Habitat Build Gap:               +0.14   (cognitive − 14-dim mean)
Interpretation:                  Coherent
```

A spec-led team whose observability lags:

```text
Habitat Maturity Level (model):  L4  (14-dim mean L3.64)
Cognitive read (Parts A–C):      L4
Habitat Build Gap:               +0.36   (cognitive − 14-dim mean)
Interpretation:                  Coherent
```

A team whose thinking has outrun a thin habitat:

```text
Habitat Maturity Level (model):  L3  (14-dim mean L2.50)
Cognitive read (Parts A–C):      L3
Habitat Build Gap:               +0.50   (cognitive − 14-dim mean)
Interpretation:                  Ambition outpaces enablement
```

## Acting on it

See [Read the Habitat Build Gap](../how-to/read-the-habitat-build-gap.md)
for what to do in each regime, and
[Coherence, not level](../explanation/coherence-not-level.md) for why the
gap — not the level — is the signal that matters.
