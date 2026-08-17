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
    path: ./orders-api
  - id: billing
    path: ./billing

report:
  output: assessments/
```

## Path resolution

**The scope root is the directory containing `.habitat/`** — not
`.habitat/` itself. Every path in the manifest resolves from the scope
root, and there is no second anchor:

| Field | Resolves from | Example | Means |
|---|---|---|---|
| `subjects[].path` | scope root | `./orders-api` | `<scope root>/orders-api` |
| `subjects[].paths[]` | scope root | `./billing-impl` | `<scope root>/billing-impl` |
| `habitats[].path` | scope root | `./platform-harness` | `<scope root>/platform-harness` |
| `report.output` | scope root | `assessments/` | `<scope root>/assessments/` |
| `subject_path` in the [summary block](assessment-summary-block.md) | scope root | `./orders-api` | `<scope root>/orders-api` |

Worked through the usual layout:

```text
estate/                      ← the scope root
├── .habitat/scope.yml
├── orders-api/              ← path: ./orders-api
├── billing/                 ← path: ./billing
└── assessments/             ← report.output: assessments/
    └── 2026-08-17-portfolio.md
```

The scope root is a property of *where the manifest was found*, not of
where you ran the command. Run the roll-up from inside
`estate/orders-api/` and the manifest is still found at
`estate/.habitat/scope.yml`, so paths still resolve from `estate/` and
the portfolio report is still written to `estate/assessments/`.

`.habitat/` is a container for scope configuration, not a base for path
arithmetic. Anchoring on the directory above it is what makes the
`report.output: assessments/` default correct as written — anchored on
`.habitat/` it would bury portfolio reports inside a dot-directory — and
it keeps the manifest movable. The trade-off is that the manifest departs
from the self-relative convention of `.gitmodules` or `docker-compose.yml`;
that choice is recorded in
[spec 0012](https://github.com/techtalk/ai-readiness-assessment/blob/main/specs/0012-scope-manifest-path-resolution.md).

## Fields

| Field | Required | Meaning |
|---|---|---|
| `version` | yes | Schema version. Currently `1`. |
| `team` | yes | Free text. The cognitive read is scoped to this, not to any repository. |
| `subjects` | yes | Non-empty list of the things being assessed. |
| `subjects[].id` | yes | Unique identifier, used as the row label in the matrix. |
| `subjects[].path` | yes | Path to the subject, resolved from the [scope root](#path-resolution). A repo, a submodule, or a directory inside a monorepo. |
| `report.output` | no | Where the roll-up is written, resolved from the [scope root](#path-resolution). Defaults to `assessments/`. |

`team` is deliberately not a repository. A team is people; a repository
is code. Conflating them is the assumption this whole schema exists to
break — see [Subject, habitat, team](../explanation/why-no-portfolio-score.md).

## Where it is looked for

The roll-up checks `<dir>/.habitat/scope.yml` for `dir` = the working
directory, then each of its first three parent directories, stopping at
the first hit. **Four directories are tested in total**, and the scope
root is the `dir` that produced the hit.

The usual layout puts the manifest in a parent directory beside the
subjects:

```text
estate/
├── .habitat/scope.yml
├── orders-api/
│   └── assessments/2026-07-02-assessment.md
└── billing/
    └── assessments/2026-06-11-assessment.md
```

Started in `estate/orders-api/`, the search tests `orders-api/`, then
`estate/`, and stops there — so the scope root is `estate/`, never
`orders-api/`.

## Validation rules

**Hard errors** — the roll-up stops and says why:

- no manifest found
- `subjects` absent or empty
- a duplicate `id`
- a subject with no `path`
- **no subject path resolves at all** — the roll-up stops rather than
  writing a zero-coverage portfolio report, and names a path-anchor
  mismatch as the likely cause. Paths resolve from the
  [scope root](#path-resolution); a manifest written against `.habitat/`
  itself misses every subject by one level.

**Not errors:**

- **An unreadable path.** Recorded in the coverage ledger as
  `unreachable` and reported as such. A client boundary or a repo you
  lack access to is a normal condition, not a failure. *Some* subjects
  unreachable is a finding; *every* subject unreachable is the hard error
  above.
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
    path: ./platform-harness
    provides: [HARNESS.md, AGENTS.md, ci, hooks]

subjects:
  - id: orders-api
    path: ./orders-api
    habitat: platform-harness   # omit ⇒ self-governed
```

| Field | Required | Meaning |
|---|---|---|
| `habitats[].id` | yes | Unique across `habitats` *and* `subjects`. |
| `habitats[].kind` | yes | `repo`, `submodule`, `self`, `package`, `org`, or `upstream` — see [below](#habitat-kinds). |
| `habitats[].path` | yes | Path to the habitat, resolved from the [scope root](#path-resolution). |
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
    path: ./legacy-batch
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
      - ./billing-contract
      - ./billing-impl
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
    path: ./legacy-batch
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
