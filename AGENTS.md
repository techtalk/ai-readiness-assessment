# AGENTS.md

Human-curated knowledge for anyone — person or agent — working **on**
this plugin. It is the operational layer that complements two other
surfaces and deliberately does **not** duplicate them:

- **`HARNESS.md`** holds the *rules* (conventions and enforced
  constraints). Don't restate them here.
- **`docs/explanation/`** holds the *user-facing why* (why the model,
  why coherence beats level, why self-contained). Link to it, don't
  copy it.

This file is the rest: the gotchas, the workflows, the test strategy,
and the decisions-with-rationale that neither of those captures. Humans
edit this file; agents propose changes via `/reflect` and a human
promotes them.

> **Status: DRAFT for review.** Seeded from the first `REFLECTION_LOG.md`
> entry and the decisions made building the plugin. Edit freely — you
> own it.

---

## GOTCHAS

Practical traps, with what happened and how to avoid them.

- **The tests assert against committed sample assessments, not live
  output.** `tests/run.py` reads the pre-written reports under
  `tests/fixtures/<level>/assessments/`. A green check does **not** prove
  your instrument change is reflected — it only proves the *committed
  samples* still satisfy the structural assertions. When you change
  scoring, you must regenerate those samples (see TEST_STRATEGY).
- **Retroactive releases need real tags.** `gh release create --target
  <short-sha>` returns HTTP 422 for past commits. Push an annotated git
  tag first, then `gh release create --verify-tag`. (Tags aren't subject
  to branch protection.)
- **The two manifests must agree on the version.** `plugin.json` and
  `marketplace.json` must carry the same `version`; the release workflow
  and the changelog gate both fail on a mismatch.
- **`main` is branch-protected.** You can't push to it directly — branch
  and open a PR. Two required checks must pass: `A-tier structural
  assertions` and `Changelog gate`.

---

## WORKFLOWS

### Changing the instrument

The instrument is the prose in `commands/ai-readiness-assess.md` and
`skills/ai-readiness-assessment/SKILL.md`. When you change it:

1. Edit **both** files identically — the *Dual-surface sync* constraint
   forbids changing one without the other.
2. If you changed **how the assessment scores**, regenerate the six
   `tests/fixtures/<level>/assessments/*.md` reports **and** their
   `expected.md`, and update `run.py`'s expected gap regimes to match.
3. Run `python3 tests/run.py` — it must be green.
4. If you touched `docs/` or `mkdocs.yml`, run `mkdocs build --strict`.

### Cutting a release

1. Bump `version` in **both** `plugin.json` and `marketplace.json`.
2. Add a `## [x.y.z]` section to `CHANGELOG.md` (rename `Unreleased`).
3. Open the PR. On merge, `release.yml` tags `vX.Y.Z` and publishes a
   GitHub Release whose notes are that CHANGELOG section. The `Changelog
   gate` check blocks a version bump that lacks its CHANGELOG entry.

### Keeping the surfaces in sync

After a material `HARNESS.md` change, run `/harness-sync` to regenerate
the convention files (`.cursor/`, `.github/copilot-instructions.md`,
`.windsurf/`), and `/harness-onboarding` to refresh `ONBOARDING.md`.

---

## TEST_STRATEGY

Quality is assured through **TDAB** (Test-Driven Agentic Behaviours):

- **A-tier (structural)** — automated in `tests/run.py`, stdlib-only.
  Checks each fixture's report for the required structure (level line,
  discovery ordering, discipline bounds, the four headline Operational
  Axes, the Habitat Build Gap regime, the fourteen-dimension Habitat
  Maturity Profile). Runs in CI on every PR and gates merges.
- **B-tier (behavioural) and C-tier (semantic)** — described in each
  fixture's `expected.md`; need an interactive session or an LLM judge,
  run manually. See `tests/README.md`.

The fixtures are **committed sample assessments** — regenerate them (and
`expected.md`, and `run.py` regimes) whenever scoring changes; see the
GOTCHAS note above. Run locally with `python3 tests/run.py` or
`python3 tests/run.py --fixture <name>`.

---

## ARCH_DECISIONS

Load-bearing choices, with the alternative we rejected. The *user-facing*
rationale lives in `docs/explanation/` — linked, not duplicated.

- **The Agentic Maturity Model is the spine; the cognitive ladder is
  folded in.** All fourteen dimensions are the primary read; the
  Sovereign Engineer L0–L5 ladder is the second, cognitive read.
  *Why:* the mismatch between the two is the signal a single score hides.
  → `docs/explanation/two-reads.md`.
- **The Habitat Build Gap uses the mean of all fourteen dimensions** —
  not just the four headline axes. *Alternative rejected:* the four-axis
  mean (more stable, but ignores ten dimensions and undercuts "evaluate
  against the whole model"). → `docs/reference/habitat-build-gap.md`,
  `docs/explanation/coherence-not-level.md`.
- **Self-contained by design.** The instrument depends on no other
  plugin, agent, or service; the model and scoring are embedded in the
  command and skill. *Alternative rejected:* depending on
  `ai-literacy-superpowers` (richer, but won't run standalone).
  → `docs/explanation/self-contained.md`.
- **Two entry points, one instrument.** The command and the skill carry
  identical framework content (enforced by the Dual-surface sync
  constraint). *Why:* the same assessment, reachable by slash command or
  natural language, must never disagree with itself.

---

## Where this connects

- Enforced rules and constraints: [HARNESS.md](HARNESS.md)
- User-facing explanation: [docs/explanation/](docs/explanation/index.md)
- Session learnings (promotion source): [REFLECTION_LOG.md](REFLECTION_LOG.md)
- New-contributor guide (regenerated from this file + HARNESS):
  [ONBOARDING.md](ONBOARDING.md)
