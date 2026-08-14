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
| `habitats[].kind` | yes | `repo` (a sibling repository), `submodule`, or `self` (the harness is in the repo holding the manifest). |
| `habitats[].path` | yes | Path to the habitat, relative to the manifest. |
| `habitats[].provides` | no | A hint about what it offers. **Never taken as proof** — a declared artefact still has to bind before it raises anything. |
| `subjects[].habitat` | no | Which declared habitat governs this subject. Omit for self-governed. |

A `habitat` reference naming no declared habitat is a **hard error**, and
the message names the bad reference. Declaring a habitat that nothing
binds to is *not* an error — that is a finding, reported per dimension as
`inherited-unbound`. See
[Provenance and binding](provenance-and-binding.md).

## Fields arriving later

Later releases add `posture:` (so an archived repo cannot pin the
portfolio ceiling), `paths:` (one logical subject spanning several
directories), `justified_variance:` (divergence that is intentional and
should not be reported as drift), and the `package`, `org` and
`upstream` habitat kinds. Manifests written to the schema above will
keep working when they do.
