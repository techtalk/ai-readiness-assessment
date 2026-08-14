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

## Fields arriving later

Later releases add `habitats:` (for a harness that governs a subject
from outside it), `posture:` (so an archived repo cannot pin the
portfolio ceiling), `paths:` (one logical subject spanning several
directories), and `justified_variance:` (divergence that is intentional
and should not be reported as drift). Manifests written to the schema
above will keep working when they do.
