# Provenance and binding

When a subject is governed by a harness that lives outside it,
dimensions are placed against the **effective habitat** — the shared
layer merged with the local one — and each placement records where its
evidence came from.

Self-governed subjects record `local` throughout and need none of this.

## Provenance values

| Value | Meaning | Effect on the placement |
|---|---|---|
| `local` | Evidence is in the subject itself. | Placed normally. |
| `inherited` | The shared habitat supplies it **and** it demonstrably reaches this subject. | Placed from the shared artefact. |
| `inherited-unbound` | The shared habitat declares it; nothing here executes, references or enforces it. | **Capped at the level local evidence supports.** The report names the shared artefact that was expected to bind. |

See [Distribution is not federation](../explanation/distribution-is-not-federation.md)
for why the third value exists.

## Binding evidence checklist

A shared artefact is *bound* to a subject on any of these signals:

| Signal | Reads as bound when |
|---|---|
| **CI configuration** | Subject workflows call, extend, or reuse the shared workflows. |
| **Hook / plugin configuration** | Subject config points at the shared harness, plugin, or marketplace. |
| **Submodule pin** | The submodule is present *and* pinned within a recent window. The pin age is reported. |
| **Package/lockfile pin** | The shared harness package resolves in the lockfile. The version and its age are reported. |
| **Convention file references** | The subject's `AGENTS.md` / `CLAUDE.md` includes or defers to the shared file rather than restating it. |
| **Shadowing** | A local file overriding a shared rule means **not bound** for that dimension. The override is reported as a divergence. |

### Shadowing is a signal, not an exception

A local file that restates or overrides a shared rule means the subject
is governed by the local copy. The dimension is placed from the local
override, and the divergence is named. Taking the higher of the two
levels would report a governance state that does not exist.

### The pin is the habitat

For submodule and package habitats, the **pinned revision** is the
governing habitat — not the shared repository's current tip. A subject
pinned eighteen months back is governed by an eighteen-month-old
harness, however good the current one is. The report states the pin age.

## Silence is not negation

The checklist can be silent about a binding mechanism it does not
recognise. Where no signal is found **but there is no evidence of
absence either**, the dimension is placed `inferred` — not
`inherited-unbound` — and a clarifying question is spent before anything
is asserted as unbound.

Every binding finding names the artefact expected to bind and where it
was looked for, so a team binding by another route can correct the
record.

## In the summary block

Every dimension row carries its provenance:

```yaml
  governance: { level: 3, confidence: inferred, provenance: inherited-unbound }
```

A subject governed from elsewhere also carries a `binding:` section,
recording what was found rather than only the conclusion:

```yaml
binding:
  habitat: platform-harness
  kind: repo
  pin_age_days: 412
  signals_found: [convention-references]
  unbound_dimensions: [testing, observability]
  expected_to_bind: [.github/workflows/harness-tests.yml]
```

`binding:` is omitted entirely for a self-governed subject. An empty
section would imply a shared habitat was looked for and not found, which
is a different claim.

## In the portfolio report

The [dimension matrix](portfolio-report.md#2-dimension-matrix) marks
provenance in the cell, with a key beneath it. A dimension that is
`inherited-unbound` across several subjects sharing a habitat appears in
the **common weak** column — it is a binding failure owned by whoever
provides the habitat, not a capability failure owned by each team.
