# Write a scope manifest

A scope manifest tells `/ai-readiness-rollup` which subjects to include.
You need one before your first roll-up; you do not need one to run a
single-repo assessment.

## 1. Pick where it lives

Put `.habitat/scope.yml` in a directory *above* the repositories it
names — usually the directory you clone into. That directory is the
**scope root**, and every path in the manifest resolves from it:

```text
estate/                  ← the scope root
├── .habitat/
│   └── scope.yml
├── orders-api/
├── billing/
└── legacy-batch/
```

The roll-up checks the working directory and then its first three parent
directories — four in total — and stops at the first
`.habitat/scope.yml` it finds. The scope root is the directory that
produced the hit, so running the roll-up from inside `orders-api/` still
resolves every path from `estate/`.

## 2. Name the team and the subjects

```yaml
version: 1
team: payments-tribe

subjects:
  - id: orders-api
    path: ./orders-api
  - id: billing
    path: ./billing
  - id: legacy-batch
    path: ./legacy-batch

report:
  output: assessments/
```

Paths resolve from the scope root — the directory containing
`.habitat/`, so `./orders-api` here means `estate/orders-api`. See
[path resolution](../reference/scope-manifest.md#path-resolution).

`team` is free text and should name *people* — a tribe, a squad, a
department. It is not a repository name.

## 3. Check each subject has an assessment

The roll-up reads reports; it does not produce them. For each subject:

```bash
ls orders-api/assessments/
```

If a subject has none, run `/ai-readiness-assess` in that repository
first. A subject with no assessment is not an error — it will appear in
the coverage ledger as `unreachable` — but it contributes nothing to the
matrix.

## 4. Run the roll-up

```text
/ai-readiness-rollup
```

The report lands in `estate/assessments/YYYY-MM-DD-portfolio.md` —
`report.output` resolves from the scope root, so `assessments/` means
`estate/assessments/`.

## Common cases

**A repository you cannot read.** Leave it in the manifest. It will be
reported as `unreachable` and counted in the coverage ledger — which is
better than quietly dropping it, because the report will then say "5 of
6" rather than implying it covered everything.

**A monorepo.** Put `.habitat/scope.yml` at the repository root — that
root is then the scope root — and point several subjects at directories
inside it:

```yaml
subjects:
  - id: web
    path: ./packages/web
  - id: api
    path: ./packages/api
```

**Something changed and you're unsure the manifest is current.** Run the
roll-up and read the coverage ledger. It names every subject it expected
and what it found — which is the fastest way to spot a manifest that has
drifted from the estate.

## Next

- [Scope manifest schema](../reference/scope-manifest.md) — every field
- [Roll up existing assessments](../tutorials/roll-up-existing-assessments.md)
  — the full walkthrough
