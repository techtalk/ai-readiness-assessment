---
name: wordcount-habitat-init
description: Adopt the wordcount-habitat plugin in a sibling repo. Generates a CLAUDE.md skeleton, a HARNESS.md constraint set, the spec-implement command, the wordcount-style skill, and a CI workflow that matches the wordcount reference repo's setup.
---

# /wordcount-habitat-init

Cross-team adoption command. Installed via the `wordcount-habitat`
plugin (see `.claude-plugin/plugin.json`).

## Process

1. Scan the target repo's stack (language, package manager, CI
   provider).
2. Generate a `CLAUDE.md` skeleton with the sibling team's project
   name and stack details substituted in.
3. Generate a `HARNESS.md` with the core constraint set
   (lint-clean, coverage-floor, spec-first-ordering,
   objections-resolved).
4. Copy `commands/spec-implement.md` and
   `skills/wordcount-style/SKILL.md` into the target repo with
   project-name substitutions.
5. Generate a CI workflow that matches the reference repo's
   pattern, scoped to the target's CI provider.
6. Report what was generated and what the team should review before
   their first commit.
