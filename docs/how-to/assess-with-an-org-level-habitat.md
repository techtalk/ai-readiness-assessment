# Assess with an org-level habitat

Some governance lives above every repository you can read: an org
`.github` repository, org-wide Copilot instructions, org rulesets,
shared reusable workflows, a harness shipped as a package.

Declare it — but expect the report to be sceptical about it, and
understand why.

## The three kinds

| `kind` | What it is | What the assessment can sense |
|---|---|---|
| `package` | A harness shipped as an npm / NuGet / PyPI package, or a plugin from a marketplace | The lockfile or plugin manifest: resolved version and pin age |
| `org` | Org `.github` repo, org-wide instructions, org rulesets, shared reusable workflows | Only what a subject actually references |
| `upstream` | An internal fork inheriting a habitat from an upstream nobody here controls | The fork relationship and how far it has diverged |

```yaml
version: 1
team: platform-group

habitats:
  - id: org-standards
    kind: org
    path: ../.github          # may not be readable at all — that is fine
    provides: [copilot-instructions, rulesets, reusable-workflows]
  - id: harness-pkg
    kind: package
    path: "@acme/agent-harness"
    provides: [HARNESS.md, ci]

subjects:
  - id: orders-api
    path: ../orders-api
    habitat: org-standards
  - id: billing
    path: ../billing
    habitat: harness-pkg
```

## What to expect: an org habitat never raises a dimension

This is the part that surprises people, so it is worth being blunt.

An org habitat is reported as **declared, unverifiable from here**. It
does not lift any dimension above what the subject's own evidence
supports, no matter how good the org policy is.

The reason: there is nothing to check it against. With a sibling harness
repository the assessment can at least read the artefact and look for
signals that it binds. With an org habitat there is no artefact in
reach — which makes it the single easiest thing in the instrument to
take silent credit for. A report that quietly credits an org policy
nobody has wired up produces exactly the false comfort the assessment
exists to remove.

### Making it verifiable

The report names the action, and it is the same action that makes the
policy actually work: **reference it from the subject.**

- Have the subject's workflow `uses:` the org's reusable workflow.
- Have the subject's `AGENTS.md` / `CLAUDE.md` include or defer to the
  org file rather than restating it.
- Have the subject's config point at the org ruleset.

Do any of those and the org habitat stops being unverifiable — it
becomes bindable, and therefore observable, and the dimension it
supplies gets placed as `inherited` on the next run.

That is not a reporting trick. An org policy no repository references is
not governing that repository, whatever the org chart says.

## What to expect: a package pin is verified, its content is not

For a `package` habitat the assessment reads the lockfile or plugin
manifest and reports the **resolved version and its age**.

That proves the package is *present*. It does not prove its rules
*run*. So dimensions supplied only by the package are marked `inferred`
unless something local corroborates them — a CI step that invokes it, a
config that loads it.

A stale pin is reported the same way as a stale submodule: the pinned
version is the governing habitat, not whatever the package's latest
release contains.

## What to expect: a fork inherits, and divergence chooses the steer

An `upstream` habitat is placed as `inherited` — you really did inherit
it. The report states how far the fork has diverged, and that decides
the recommendation:

- **Close to upstream** → contribute changes back. Overlaying locally
  duplicates work you would then maintain forever.
- **Heavily diverged** → overlay locally, deliberately, and stop
  describing the fork as tracking upstream. Half-tracking is the
  expensive state: you carry the merge cost without the benefit.

## Next

- [Assess across a client boundary](assess-across-a-client-boundary.md) — when subjects cannot be read at all
- [Provenance and binding](../reference/provenance-and-binding.md)
- [Distribution is not federation](../explanation/distribution-is-not-federation.md) — the same argument one layer down
