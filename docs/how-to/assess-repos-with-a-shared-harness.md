# Assess repos with a shared harness

When the harness governing a repository lives somewhere else, declare it
so the assessment can tell an inherited rule that *binds* from one that
merely exists.

Two shapes are common. Both use the same mechanism.

## Shape 1 — a separate harness repository

A platform team owns `platform-harness`; several services are meant to
be governed by it.

`.habitat/scope.yml`:

```yaml
version: 1
team: payments-tribe

habitats:
  - id: platform-harness
    kind: repo
    path: ./platform-harness
    provides: [HARNESS.md, AGENTS.md, ci]

subjects:
  - id: orders-api
    path: ./orders-api
    habitat: platform-harness
  - id: billing
    path: ./billing
    habitat: platform-harness
  - id: internal-tools
    path: ./internal-tools     # no habitat: — self-governed
```

Then assess each subject as usual. Where a dimension is satisfied only by
the shared harness, the report records it as `inherited` — but **only if
something in the subject actually reaches it**.

## Shape 2 — a parent repo with submodules

One `HARNESS.md` at the root, application repos underneath as submodules.

```yaml
version: 1
team: platform-group

habitats:
  - id: root-harness
    kind: self          # the harness is in the repo holding the manifest
    path: .

subjects:
  - id: web
    path: ./web
    habitat: root-harness
  - id: api
    path: ./api
    habitat: root-harness
```

If the repository has a `.gitmodules` file and no manifest, the
assessment will notice, say a multi-subject scope appears to be present,
and offer to write one. Declining leaves the run exactly as it was.

## What makes a rule count as bound

Declaring a habitat is not enough. The assessment looks for evidence
that the shared artefact reaches the subject — CI reuse, hook or plugin
config, a submodule or lockfile pin, or a convention file that defers to
the shared one rather than restating it. The full list is in
[Provenance and binding](../reference/provenance-and-binding.md#binding-evidence-checklist).

Where nothing binds, the dimension is capped at what local evidence
supports and marked `inherited-unbound`, with the artefact that was
expected to bind named in the report.

## Reading the result

**Mostly `inherited`.** The harness is doing its job. Watch the pin ages.

**Mostly `inherited-unbound`.** The habitat already exists and is not
wired up — usually the cheapest available uplift in the whole estate.
Nobody needs to build anything; somebody needs to bind it.

**A stale pin.** The report states the pin age and assesses the *pinned*
revision. A subject pinned a year back is governed by a year-old
harness.

**A shadowed rule.** A local file overriding a shared one means the
subject is governed by the local copy. The report names the divergence
rather than taking the higher level.

## If a finding looks wrong

Binding detection can miss a mechanism it does not recognise, which is
why the assessment places a dimension `inferred` — and asks — rather
than asserting `inherited-unbound` when it finds no signal but no
evidence of absence either.

Every binding finding names what it looked for. If your harness binds by
another route, say so when asked; the placement is corrected and the
route is worth adding to the checklist.

## Next

- [Provenance and binding](../reference/provenance-and-binding.md)
- [Distribution is not federation](../explanation/distribution-is-not-federation.md)
- [Scope manifest schema](../reference/scope-manifest.md)
