# Spec 0009: Rename the Habitat Build Gap to the Habitat/Workflow Gap

- **Status**: accepted
- **Date**: 2026-07-29
- **Issue**: #57

## Intent

Rename the coherence metric from **Habitat Build Gap** to
**Habitat/Workflow Gap** across the instrument's own language and the
documentation. "Build" described the remedy for one side of the metric —
building habitat when ambition outran enablement — and read oddly when
the gap pointed the other way. "Habitat/Workflow" names the two things
being compared instead of prescribing the fix.

The measure is unchanged: still `cognitive level − 14-dimension habitat
maturity mean`, with the same three regimes (Coherent / Ambition
outpaces enablement / Inherited habitat). Nothing about how a team is
scored moves. This is a naming change only.

## Design

### The term

`Habitat/Workflow Gap` — title-cased, no spaces around the slash,
matching the term it replaces and neighbouring headings such as
`## Habitat Maturity Profile`. The slug form is `habitat-workflow-gap`.

194 occurrences of the term and 19 of the slug, across 37 files.

### What changes

- **Live surfaces** — `skills/ai-readiness-assessment/SKILL.md` and
  `commands/ai-readiness-assess.md` (14 each), so a newly generated
  report uses the new name in both the scannable `**Habitat/Workflow
  Gap**:` header line and the `## Habitat/Workflow Gap` section.
- **Plugin manifests** — the description sentence in
  `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
- **Documentation** — every `docs/` page, `README.md`, `AGENTS.md`,
  `ONBOARDING.md`, `mkdocs.yml`, and a comment in
  `.github/workflows/agentic-behaviours.yml`.
- **Dogfood examples** — both `docs/examples/*.html` and their markdown
  sources under `assessments/`. These are what a reader is shown when
  they ask what a report looks like, so they follow the live surfaces
  rather than being treated as historical records.
- **Tests** — `tests/run.py`, `tests/README.md`, and the six
  `tests/fixtures/*/expected.md`.

### File renames

Two documentation files carried the old term in their names and are
renamed, with the `mkdocs.yml` nav and all sixteen inbound links updated:

- `docs/reference/habitat-build-gap.md` → `habitat-workflow-gap.md`
- `docs/how-to/read-the-habitat-build-gap.md` →
  `read-the-habitat-workflow-gap.md`

### Column alignment

The report's gap block is a fixed-column text block:

```text
Habitat Maturity Level (model):  L2  (14-dim mean L2.3)
Cognitive read (Sovereign Eng):  L3
Habitat/Workflow Gap:            +0.7   (cognitive − 14-dim mean)
Interpretation:                  Ambition outpaces enablement
```

The new label is three characters longer, so every occurrence of the
block had its padding reduced by three to keep the value column at 33.

### What deliberately does not change

Historical records keep the name the instrument used at the time —
rewriting them would falsify what was said when:

- `specs/0003-habitat-build-gap-uses-14-dim-mean.md` (including its
  filename, which is an identifier) and `specs/0004-simplify-report-header.md`
- released `CHANGELOG.md` entries
- `REFLECTION_LOG.md`
- the six `tests/fixtures/*/assessments/*.md` and their test reports —
  generated output from real runs

## Alternatives considered

- **Keeping the two doc filenames and changing only their prose.** Would
  have preserved the published docs-site URLs. Rejected in favour of
  consistent naming; see the risk below.
- **A transitional alias naming both terms in the report.** Rejected —
  the metric is already a two-part idea; naming it twice would make it
  harder to read, not easier.

## Risks / what could go wrong

- **Published docs URLs break.** `/reference/habitat-build-gap/` and
  `/how-to/read-the-habitat-build-gap/` will 404. No redirect plugin is
  installed and none was added. *Accepted deliberately* — the decision
  was to rename and update links.
- **A13 regression.** A13 asserts the gap section and header line by
  literal string. The six fixture assessments predate the rename, so a
  strict rename would fail all six. *Mitigated* — `GAP_NAMES` accepts
  either spelling, with a comment saying to drop the old form once the
  fixtures are regenerated.
- **Fixture drift.** `expected.md` now states the new name while the
  fixture assessments beside it still carry the old one. *Accepted* —
  `expected.md` describes what a re-run should produce, which is the new
  name; the transitional A13 covers the gap until then.
- **`specs/0003` references a path that no longer exists**
  (`docs/reference/habitat-build-gap.md`). *Accepted* — a spec records
  what was true at the time.
- **Stale term reappearing.** Nothing enforces the new name. If it
  matters, a GC rule could grep for the old term outside the historical
  set. Not added here.

## Adversarial review

**Objection**: Renaming a metric that appears in already-published
assessments makes old and new reports look like they measure different
things.
*Disposition*: Accepted as a real but small cost. The formula, the
regimes, and the header-line position are unchanged, so a reader
comparing two reports sees the same number in the same place under a
different label. The two dogfood examples were updated so the current
documented example matches what the instrument now emits.

**Objection**: Breaking two published documentation URLs to fix a
filename is a poor trade.
*Disposition*: Raised as an open question on #57 and decided by the
maintainer in favour of renaming. Recorded here rather than re-litigated.

**Disposition**: Proceed.

## Acceptance

- No occurrence of "Habitat Build Gap" or `habitat-build-gap` remains
  outside the historical set listed above.
- The gap block's value column still lines up in every surface.
- `python3 tests/run.py` passes.
- `mkdocs build --strict` succeeds with no link warnings, and both
  renamed pages resolve at their new paths.
