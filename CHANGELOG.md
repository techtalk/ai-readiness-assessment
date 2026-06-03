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

[Unreleased]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/techtalk/ai-readiness-assessment/releases/tag/v0.1.0
