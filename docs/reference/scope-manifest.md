# Scope manifest schema

`.habitat/scope.yml` declares which subjects a
[portfolio roll-up](portfolio-report.md) covers.

Its absence is meaningful: with no manifest, `/ai-readiness-assess`
behaves exactly as it always has, assessing the current repository as a
single subject. The manifest is opt-in, and only the multi-repo case
needs one.

## Minimal manifest

```yaml
version: 1
team: payments-tribe

subjects:
  - id: orders-api
    path: ../orders-api
  - id: billing
    path: ../billing

report:
  output: assessments/
```

## Fields

| Field | Required | Meaning |
|---|---|---|
| `version` | yes | Schema version. Currently `1`. |
| `team` | yes | Free text. The cognitive read is scoped to this, not to any repository. |
| `subjects` | yes | Non-empty list of the things being assessed. |
| `subjects[].id` | yes | Unique identifier, used as the row label in the matrix. |
| `subjects[].path` | yes | Path to the subject, relative to the manifest. A repo, a submodule, or a directory inside a monorepo. |
| `report.output` | no | Where the roll-up is written, relative to the manifest. Defaults to `assessments/`. |

`team` is deliberately not a repository. A team is people; a repository
is code. Conflating them is the assumption this whole schema exists to
break — see [Subject, habitat, team](../explanation/why-no-portfolio-score.md).

## Where it is looked for

The roll-up searches the working directory, then upward at most three
levels. The usual layout puts it in a parent directory beside the
subjects:

```text
estate/
├── .habitat/scope.yml
├── orders-api/
│   └── assessments/2026-07-02-assessment.md
└── billing/
    └── assessments/2026-06-11-assessment.md
```

## Validation rules

**Hard errors** — the roll-up stops and says why:

- no manifest found
- `subjects` absent or empty
- a duplicate `id`
- a subject with no `path`

**Not errors:**

- **An unreadable path.** Recorded in the coverage ledger as
  `unreachable` and reported as such. A client boundary or a repo you
  lack access to is a normal condition, not a failure.
- **A subject with no assessment yet.** Also `unreachable`, with the
  instruction to run `/ai-readiness-assess` there.
- **Unknown keys.** These warn and are ignored. The schema grows with
  each release, and a manifest written today must keep working against
  a later version.

That last rule is deliberate. Strictness here would mean every schema
extension breaks every existing manifest, and the manifests live in
other people's repositories.

## Declaring a shared habitat

Where the harness governing a subject lives outside it, declare it under
`habitats:` and point subjects at it:

```yaml
habitats:
  - id: platform-harness
    kind: repo                  # repo | submodule | self
    path: ../platform-harness
    provides: [HARNESS.md, AGENTS.md, ci, hooks]

subjects:
  - id: orders-api
    path: ../orders-api
    habitat: platform-harness   # omit ⇒ self-governed
```

| Field | Required | Meaning |
|---|---|---|
| `habitats[].id` | yes | Unique across `habitats` *and* `subjects`. |
| `habitats[].kind` | yes | `repo`, `submodule`, `self`, `package`, `org`, or `upstream` — see [below](#habitat-kinds). |
| `habitats[].path` | yes | Path to the habitat, relative to the manifest. |
| `habitats[].provides` | no | A hint about what it offers. **Never taken as proof** — a declared artefact still has to bind before it raises anything. |
| `subjects[].habitat` | no | Which declared habitat governs this subject. Omit for self-governed. |

### Habitat kinds

| `kind` | Where it lives | Ceiling on what it can claim |
|---|---|---|
| `self` | The repo holding the manifest | Read directly. |
| `repo` | A sibling repository | Read directly. |
| `submodule` | Pinned inside the subject | The **pinned revision** governs, not the shared repo's tip. Pin age reported. |
| `package` | An npm / NuGet / PyPI package, or a marketplace plugin | Pin verified, content not. Dimensions it supplies stay `inferred` unless local evidence corroborates. |
| `org` | Org `.github` repo, org rulesets, org-wide instructions | **Never raises a dimension.** Reported as *declared, unverifiable from here*. |
| `upstream` | An upstream this fork inherits from | Placed as `inherited`; divergence chooses the steer. |

The last three cannot be read from any subject checkout. See
[Assess with an org-level habitat](../how-to/assess-with-an-org-level-habitat.md)
for what each reports and why.

A `habitat` reference naming no declared habitat is a **hard error**, and
the message names the bad reference. Declaring a habitat that nothing
binds to is *not* an error — that is a finding, reported per dimension as
`inherited-unbound`. See
[Provenance and binding](provenance-and-binding.md).

## Posture

`posture` changes how a subject feeds the portfolio, never whether it is
assessed or shown:

| Posture | In the matrix | Feeds the ceiling |
|---|---|---|
| `active` (default) | yes | yes |
| `maintenance` | yes | excluded from common-weak detection |
| `archived` | yes, marked as archived | excluded entirely |

```yaml
subjects:
  - id: legacy-batch
    path: ../legacy-batch
    posture: maintenance
```

Without this a single dead repository pins the estate's ceiling
permanently, and every portfolio report afterwards leads with a finding
nobody intends to act on.

Marking a subject is better than leaving it out of the manifest.
Omitting it would overstate coverage — the report would claim to cover
the estate while quietly skipping part of it.

## Subjects spanning several paths

Where one logical subject lives in more than one place, use `paths:`
instead of `path:`:

```yaml
subjects:
  - id: billing
    paths:
      - ../billing-contract
      - ../billing-impl
```

The evidence from all paths merges into **one** placement. A contract
repository and its implementation are one logical subject; assessing
them separately reports two half-habitats that neither team recognises.

A subject must have exactly one of `path` or `paths`.

## Declared variance

Some divergence is correct and should stay. Declare it and it is
reported as **declared** rather than as drift:

```yaml
subjects:
  - id: legacy-batch
    path: ../legacy-batch
    justified_variance:
      - dimension: testing
        reason: COBOL batch; harness test tooling does not apply
```

Named dimensions are suppressed from drift findings and from extraction
candidates, and listed in the
[portfolio report](portfolio-regimes.md#declared-variance) with their
reason.

Listed, not hidden — a reader must be able to see what was excluded and
disagree with it. Suppressed, because an estate where testing or
observability genuinely cannot be uniform should not be nagged toward a
convergence that would make it worse.

## Fields arriving later

Later releases add the `package`, `org` and `upstream` habitat kinds.
Manifests written to the schema above will keep working when they do.
