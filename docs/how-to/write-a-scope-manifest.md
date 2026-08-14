# Write a scope manifest

A scope manifest tells `/ai-readiness-rollup` which subjects to include.
You need one before your first roll-up; you do not need one to run a
single-repo assessment.

## 1. Pick where it lives

Put `.habitat/scope.yml` in a directory *above* the repositories it
names — usually the directory you clone into:

```text
estate/
├── .habitat/
│   └── scope.yml
├── orders-api/
├── billing/
└── legacy-batch/
```

The roll-up searches upward from the working directory, at most three
levels, so running it from inside `orders-api/` finds a manifest in
`estate/`.

## 2. Name the team and the subjects

```yaml
version: 1
team: payments-tribe

subjects:
  - id: orders-api
    path: ../orders-api
  - id: billing
    path: ../billing
  - id: legacy-batch
    path: ../legacy-batch

report:
  output: assessments/
```

Paths are relative to the manifest. `team` is free text and should name
*people* — a tribe, a squad, a department. It is not a repository name.

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

The report lands in `estate/assessments/YYYY-MM-DD-portfolio.md`.

## Common cases

**A repository you cannot read.** Leave it in the manifest. It will be
reported as `unreachable` and counted in the coverage ledger — which is
better than quietly dropping it, because the report will then say "5 of
6" rather than implying it covered everything.

**A monorepo.** Point several subjects at directories inside it:

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
