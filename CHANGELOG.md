# Changelog

All notable changes to the `ai-readiness-assessment` plugin are documented in
this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the plugin adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The version lives in `.claude-plugin/plugin.json`. **Every version bump must add
a matching `## [x.y.z]` section below** — the release workflow
(`.github/workflows/release.yml`) reads this file for the GitHub Release notes
and fails the release if the entry is missing. Record day-to-day changes under
`Unreleased` and rename it to the new version when you bump.

## [Unreleased]

### Changed

- **Aligned HTML report design with the TechTalk marketing site** (spec
  0006): all-sans-serif typography (drop Georgia serif body); dark navy
  header band with TechTalk wordmark, headline lines, and a five-level
  progress strip; TechTalk navy `h2` headings and borders; TechTalk GmbH
  footer branding. Updated the two example reports and fixed their
  `techtalk.ai` CTA links to `techtalk.at`.
- **Aligned repo language and links with the TechTalk marketing site**:
  fixed the TechTalk CTA domain (`techtalk.ai`, a parked GoDaddy page →
  `techtalk.at` with `thomas.stangl@techtalk.at`) in the command and
  skill; corrected the command description from "AI literacy" to "AI
  readiness"; added a **Product page** link to the README and a matching
  button to `docs/index.md`; echoed the "scan, score, and a plan"
  framing in the README intro line. (#42)

### Added

- An **AI Literacy: Level 4** badge (and an **Agent Harness Enabled**
  badge) in the README, after `/assess` independently confirmed the repo
  reads **Level 4 — Specification-led**. Also corrected the stale harness
  badge (2/3 → 3/4 enforced) after the Spec-first constraint.

### Changed

- The assessment now **leads with two headline lines** — *AI Readiness —
  Habitat Maturity: Level N (Verb)* and *Next Step / Gap: +X to Level N+1
  (NextVerb)* — with the Habitat Build Gap (coherence) kept as a
  secondary line. (Specs 0004–0005.)
- **Report language aligned with the public "AI Readiness" mockup**
  (spec 0005): the headline shows *AI Readiness — Habitat Maturity*; an
  **AI Readiness Score** breakdown across five readiness dimensions
  (Context · Conventions · Architectural guidance · Guardrails · Agent
  readiness) is added; and Recommendations are reframed as a
  **Prioritised Improvement Plan** ordered by what the team must develop
  and the organisation must provide. The two example reports — and the
  narrative example surfaces (the docs `examples` page and the README
  example table) — were aligned to match.

### Added

- An example self-assessment — the plugin run against its own repo —
  committed under `assessments/` (markdown + HTML) and linked from the
  README and the docs site (`/examples/`).
- A `specs/` layer (README + template + the first spec) and a
  **spec-first** convention in HARNESS.md — starting the L3→L4 jump the
  self-assessment recommended.
- An **Onboarding gate** (`.github/workflows/onboarding-gate.yml`) and a
  matching GC rule: a PR that changes the HARNESS body or AGENTS.md must
  refresh ONBOARDING.md, so the onboarding guide can't silently trail its
  sources.
- **Spec-first is now enforced**: promoted from convention to a HARNESS
  constraint, backed by a **Spec-first gate**
  (`.github/workflows/spec-first-gate.yml`) — instrument changes must
  carry a spec. The spec format gained an adjudicated **Adversarial
  review** disposition, and specs 0002–0003 were added (completing the
  L3→L4 specifications discipline).
- A **re-assessment** showing the L3→L4 progression
  (`assessments/2026-06-03-assessment-2.md` + HTML), linked from the
  README and docs as a progression example: cognitive read L3→L4, with
  the Habitat Build Gap flipping +0.2 (Coherent) → +1.1 (Ambition
  outpaces enablement).

## [0.4.1] - 2026-06-03

### Changed

- Reworded the TechTalk call to action in the assessment ("TechTalk
  offers …" → "TechTalk can support …"), kept in sync across the command
  and skill, and the matching engagements line in the README.

## [0.4.0] - 2026-06-02

### Added

- Apache License 2.0 (`LICENSE`), declared as `Apache-2.0` in
  `plugin.json` and `marketplace.json`, with a License badge in the
  README.
- A documentation site (MkDocs Material, Diátaxis-structured) under
  `docs/`, deployed to GitHub Pages via `.github/workflows/pages.yml`,
  covering tutorials, how-to guides, reference, and explanation for the
  whole plugin — especially the assessment.
- `CHANGELOG.md` and a changelog-driven release workflow: every version
  bump publishes a GitHub Release whose notes are the matching CHANGELOG
  section.
- CI for the TDAB structural suite, a PR-time changelog gate, and
  required status checks (`A-tier structural assertions`, `Changelog
  gate`) on a protected `main`.
- `AGENTS.md`, `ONBOARDING.md`, and `REFLECTION_LOG.md` for contributors,
  plus a "Dual-surface sync" harness constraint (command ≡ skill) and
  synced Cursor / Copilot / Windsurf convention files.
- README prerequisites and status / scope badges; repo description,
  topics, and homepage.

### Changed

- The Sovereign Engineer call-to-action now points to the AI-readiness
  campaign URL (`https://leanpub.com/thesovereignengineer/c/ai-readiness`)
  — in the assessment's reading-path CTA (command + skill) and the
  "buy the book" CTAs in the README and the docs.

## [0.3.0] - 2026-06-02

### Changed

- Made the **Agentic Experience 5-Level Habitat Maturity Model** the assessment
  spine — all fourteen dimensions placed L1–L5 with the model's own verbs, with
  the *Sovereign Engineer* six-level cognitive ladder folded in as the cognitive
  read (#5).
- The **Habitat Build Gap** is now measured against the mean of all fourteen
  dimensions, not just the four headline axes (#5).
- README leads with the model; install docs cover GitHub Copilot CLI first, then
  Claude Code, with both interactive and command-line forms (#5).

### Added

- TDAB A-tier structural test suite (`tests/run.py`) wired into CI on every PR,
  including the fourteen-dimension Habitat Maturity Profile assertion (#5).
- Required `A-tier structural assertions` status check on `main`.
- Convention files for Cursor, Copilot, and Windsurf synced from HARNESS.md (#7).
- Release workflow that cuts a GitHub Release on every version bump (#8).

### Maintenance

- Upgraded the harness to template 0.40.0; adopted the *Consistent formatting*
  and *Tests must pass* constraints and the *Template currency* GC rule (#6).

## [0.2.0] - 2026-06-01

### Added

- ALCI Part D operational axes (Composition, Testing, Observability, Governance)
  and the Habitat Build Gap (#4).

## [0.1.0] - 2026-05-11

### Added

- Initial `ai-readiness-assessment` plugin: the self-contained assessment
  instrument (command + skill).
- `techtalkai` marketplace manifest.
- Harness and TDAB scaffolding.

[Unreleased]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/techtalk/ai-readiness-assessment/releases/tag/v0.1.0
