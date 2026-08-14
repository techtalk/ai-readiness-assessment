# Assess a monorepo with several habitats

The multi-repo case splits one team across several repositories. The
monorepo case is the inverse: one repository containing several
subjects, which may not share a habitat at all.

Assessing a monorepo as a single subject averages those habitats
together and reports a project that does not exist.

## When to split a monorepo into subjects

Split it when the packages differ in the ways the model measures — one
package has a test suite and CI gates and another has neither, or the
convention files apply to some directories and not others.

Do **not** split it when the whole repository shares one harness, one CI
pipeline and one set of conventions. That is a single subject that
happens to contain several packages, and splitting it just produces
identical rows.

## Directory subjects

Point subjects at directories inside the repository:

```yaml
version: 1
team: platform-group

subjects:
  - id: web
    path: ./packages/web
  - id: api
    path: ./packages/api
  - id: data-pipeline
    path: ./packages/data-pipeline
```

Put `.habitat/scope.yml` at the repository root and run from there:

```text
/ai-readiness-assess --scope
```

Each subject gets its own report under `packages/<name>/assessments/`.

## Where the shared habitat is the repository root

Most monorepos have root-level conventions that genuinely govern
everything — a root `CLAUDE.md`, a root CI pipeline. Declare the root as
a habitat so the assessment can tell what is inherited from what is
local to a package:

```yaml
habitats:
  - id: root
    kind: self
    path: .
    provides: [CLAUDE.md, ci]

subjects:
  - id: web
    path: ./packages/web
    habitat: root
  - id: data-pipeline
    path: ./packages/data-pipeline
    habitat: root
```

Now a package whose CI does not actually run the root pipeline shows
`inherited-unbound` rather than quietly borrowing the root's level. In a
monorepo this is common and easy to miss — a package excluded from the
root workflow's path filters looks governed and is not.

See [Provenance and binding](../reference/provenance-and-binding.md)
for what counts as bound.

## Subjects that span several paths

Where one logical subject lives in more than one directory — a contract
package and its implementation — use `paths:`:

```yaml
subjects:
  - id: billing
    paths:
      - ./packages/billing-contract
      - ./packages/billing-impl
```

The evidence from all paths merges into **one** placement. Assessing
them separately would report two half-habitats that neither the team nor
the model recognises.

## Packages nobody is investing in

Mark them, rather than leaving them out:

```yaml
  - id: legacy-importer
    path: ./packages/legacy-importer
    posture: maintenance
```

`maintenance` keeps a package in the matrix but out of common-weak
detection; `archived` keeps it out of the ceiling entirely and marks it
in the matrix. Excluding such a package from the manifest instead would
overstate coverage — the report would claim to cover the repository
while quietly skipping part of it.

## Next

- [Write a scope manifest](write-a-scope-manifest.md)
- [Assess a team across repositories](../tutorials/assess-a-team-across-repositories.md)
- [Subject, habitat, team](../explanation/subject-habitat-team.md)
