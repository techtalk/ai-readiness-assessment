<!-- Generated from HARNESS.md, AGENTS.md, and REFLECTION_LOG.md.
     Do not edit directly — regenerate with /harness-onboarding. -->

# Welcome to ai-readiness-assessment

This project is a **self-contained Claude Code & GitHub Copilot plugin**
that assesses how ready a team — and its codebase — is to collaborate
with AI. Someone installs it in any repository, runs one command, and
gets a report placing the team on the Agentic Experience 5-Level Habitat
Maturity Model and the *Sovereign Engineer* cognitive ladder, with a
Habitat Build Gap that points at the single most valuable next move.

The thing to internalise on day one: **the product is the prose.** There
is no application to compile or run — the plugin's entire behaviour lives
in two Markdown files (`commands/ai-readiness-assess.md` and
`skills/ai-readiness-assessment/SKILL.md`) plus the manifests. Your work
is mostly careful, faithful editing of that prose, kept verifiable by a
test suite and a documentation site.

---

## Tech Stack

- **Markdown (content)** — the assessment instrument. The command and
  the skill carry identical embedded framework content; editing the
  prose *is* changing the product.
- **JSON (manifests)** — `.claude-plugin/plugin.json` (the plugin) and
  `.claude-plugin/marketplace.json` (the `techtalkai` marketplace). They
  must agree on the version.
- **No build system** — this is a plugin distribution layout consumed
  directly by Claude Code, Copilot, Cursor, and Windsurf. Nothing is
  compiled, bundled, or packaged.
- **Testing: TDAB** (Test-Driven Agentic Behaviours). The A-tier
  (structural) assertions live in `tests/run.py` — stdlib-only Python,
  no dependencies — and run in CI on every PR.
- **Docs: MkDocs Material** — the site under `docs/` (build deps in
  `requirements.txt`) is deployed to GitHub Pages by
  `.github/workflows/pages.yml`.
- **No container, no runtime.**

---

## How We Write Code

The conventions below are declared in `HARNESS.md`. They exist because
the product is prose consumed by AI tools, so consistency and honesty in
that prose matter more than anything mechanical.

- **Dual-surface sync.** The framework content in
  `commands/ai-readiness-assess.md` and
  `skills/ai-readiness-assessment/SKILL.md` must be **identical**.
  Editing one without the other is forbidden — the two are the same
  instrument reached two ways, and they must never disagree.
- **Self-contained.** Neither file may reference, invoke, or depend on
  any other plugin, skill, agent, MCP server, or external service, and
  the manifest's `dependencies` must stay empty. The whole model and
  scoring live inside this repo so it runs anywhere.
- **Single CTA.** The assessment's recommendation proposes exactly one
  specific engagement — never a menu. A menu reads like marketing; one
  specific recommendation reads like advice.
- **Frontmatter shape.** Every file in `commands/` and every `SKILL.md`
  carries YAML frontmatter with `name` and `description`; for commands
  `name` equals the filename, for skills `name` equals the directory.
- **Plain-text output.** Any rendered output (HTML, PDF) uses
  print-friendly typography and **no emoji**.

---

## What's Enforced

### At commit time

- **Consistent formatting** — all source files should pass the project's
  configured formatter. *(Declared but currently `unverified` — no
  formatter is wired up yet, so this is an aspiration, not a gate.)*

### At PR time

These block merges into `main` (which is branch-protected):

- **Tests must pass** — `python3 tests/run.py` must be green. This is the
  required CI check **`A-tier structural assertions`**.
- **Dual-surface sync** — a reviewer (or review agent) confirms the
  command and skill carry the same embedded framework content.
- **Changelog gate** (CI) — if a PR bumps the plugin version, it must add
  a matching `## [x.y.z]` section to `CHANGELOG.md`. The required check
  **`Changelog gate`** enforces this; it's a no-op on PRs that don't
  change the version.

### On schedule

- **Template currency** (weekly) — checks that the `HARNESS.md`
  `template-version` marker matches the installed plugin, so new harness
  template content gets reviewed.

---

## Common Pitfalls

From `AGENTS.md` GOTCHAS and the `REFLECTION_LOG.md` workflow entry —
practical traps with what happened and how to avoid them.

- **The tests assert against committed sample assessments, not live
  output.** `tests/run.py` reads the pre-written reports under
  `tests/fixtures/<level>/assessments/`. A green check does *not* prove
  your instrument change is reflected — when you change scoring,
  regenerate those samples (see *How We Test*).
- **Don't desync the command and the skill.** Make the identical edit to
  both surfaces in the same change (the Dual-surface sync constraint).
- **Retroactive releases need real tags.** `gh release create --target
  <short-sha>` returns HTTP 422 for past commits — push an annotated git
  tag first, then `gh release create --verify-tag`.
- **The two manifests must agree on the version.** The release workflow
  and the changelog gate both fail if `plugin.json` and
  `marketplace.json` disagree.
- **`main` is branch-protected.** Branch and open a PR; the
  `A-tier structural assertions` and `Changelog gate` checks must pass.

---

## Architecture Decisions

From `AGENTS.md` ARCH_DECISIONS — the load-bearing choices, each with the
alternative that was rejected. The user-facing rationale lives in
`docs/explanation/`; don't reverse these without good reason.

- **The Agentic Maturity Model is the spine; the cognitive ladder is
  folded in.** All fourteen dimensions are the primary read; the
  Sovereign Engineer L0–L5 ladder is the second, cognitive read.
- **The Habitat Build Gap uses the mean of all fourteen dimensions** —
  not just the four headline axes (the rejected alternative was more
  stable but ignored ten dimensions).
- **Self-contained by design.** The instrument depends on no other
  plugin or service; the alternative — depending on
  `ai-literacy-superpowers` — is richer but won't run standalone.
- **Two entry points, one instrument.** The command and skill carry
  identical content so the assessment never disagrees with itself.

---

## How We Test

From `AGENTS.md` TEST_STRATEGY. Quality is assured through **TDAB** —
Test-Driven Agentic Behaviours:

- **A-tier (structural)** — automated in `tests/run.py` (stdlib-only). It
  reads each fixture's committed sample assessment and checks the report
  has the required structure: the level line, discovery ordering,
  discipline bounds, the four headline Operational Axes, the Habitat
  Build Gap regime, and the full fourteen-dimension Habitat Maturity
  Profile. It exits non-zero on any failure, so it gates PRs.
- **B-tier (behavioural) and C-tier (semantic)** — described in each
  fixture's `expected.md`; they need an interactive session or an LLM
  judge and are run manually. See `tests/README.md`.

The fixtures are **committed sample assessments** — regenerate them (and
`expected.md`, and `run.py`'s expected regimes) whenever scoring changes.
Run the suite locally with `python3 tests/run.py` (or
`python3 tests/run.py --fixture level-3-habitat` for one fixture).

---

## How the Harness Works

Three loops protect the codebase:

- **Advisory loop** — hooks that warn during editing without blocking.
  *(None configured for this minimal repo.)*
- **Strict loop** — CI gates that block merges. Two required checks on
  `main`: `A-tier structural assertions` (the TDAB suite) and
  `Changelog gate`. Two more workflows run automatically: a
  changelog-driven **release** workflow that cuts a GitHub Release on
  every version bump, and the **Pages** workflow that rebuilds the docs.
- **Investigative loop** — scheduled GC rules that catch slow drift.
  Currently: **Template currency** (weekly).

Observability cadences (snapshots, audits, cost capture) are **not
configured** for this repo — it's a small, prose-only plugin, so the
heavier observability machinery isn't wired up.

---

## Your First PR Checklist

`main` is protected — branch, open a PR, and let the required checks run.

- [ ] Branch off `main` (don't commit to it directly).
- [ ] If you touched the instrument, edit **both**
      `commands/ai-readiness-assess.md` and
      `skills/ai-readiness-assessment/SKILL.md` identically.
- [ ] If you changed how the assessment scores, regenerate the six
      `tests/fixtures/*/assessments/` reports **and** their
      `expected.md`, and update `run.py`'s expected regimes.
- [ ] Run `python3 tests/run.py` — it must be green.
- [ ] If you bumped the version, update **both** manifests to match and
      add a `## [x.y.z]` section to `CHANGELOG.md`.
- [ ] If you touched `docs/` or `mkdocs.yml`, run
      `mkdocs build --strict` (broken links fail the deploy).
- [ ] Keep recommendation output to a **single** CTA; no emoji in
      rendered output.
- [ ] Open the PR — `A-tier structural assertions` and `Changelog gate`
      must pass before merge.

---

## Where to Learn More

- [AGENTS.md](AGENTS.md) — gotchas, workflows, test strategy, and
  architecture decisions for working on the plugin
- [HARNESS.md](HARNESS.md) — the full constraint and convention reference
- [REFLECTION_LOG.md](REFLECTION_LOG.md) — session-by-session learnings
- [README.md](README.md) — what the plugin is, install, and usage
- [CHANGELOG.md](CHANGELOG.md) — release history
- [tests/README.md](tests/README.md) — how the TDAB suite is run
- **Documentation site** — <https://techtalk.github.io/ai-readiness-assessment/>
  (tutorials, how-to, reference, explanation)
