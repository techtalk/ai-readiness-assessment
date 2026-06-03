# Why it is self-contained

This plugin does one thing — assess AI readiness — and it does it without
depending on anything else. No other plugin, skill, agent, MCP server, or
external service. The model, the cognitive ladder, the scoring heuristic,
and the evidence checklist are all embedded in the command and skill
files in full.

## Why standalone matters

- **It runs anywhere.** Drop it into any repository, in Claude Code or
  Copilot CLI, and it works — no habitat to install first, nothing to
  configure.
- **The assessment can't drift from its dependencies**, because it has
  none. What it scores against is fixed in its own files and versioned
  with the plugin.
- **It's honest about what it measures.** A self-contained instrument
  has to carry its own model; that forces the model to be explicit and
  inspectable rather than hidden behind a service.

This is also a harness constraint on the repo itself: the command and
skill **may not** reference or depend on any other plugin, and the
`dependencies` field in the manifest must stay empty. A reviewer can
verify it by grepping the two files.

## Relationship to ai-literacy-superpowers

This instrument is **inspired by** the
[ai-literacy-superpowers](https://github.com/Habitat-Thinking/ai-literacy-superpowers)
plugin — the canonical home of the AI Literacy framework, with its full
agent team, harness engineering, governance audit, compound learning
loop, and orchestrator pipeline.

What you get here is **narrower by design**: just the assessment
instrument, extracted into a standalone, dependency-free package. If the
assessment reveals you want the full habitat — the agent pipeline, the
constraint enforcement, the compound learning — that is what
`ai-literacy-superpowers` provides.

The conceptual ground for both — the levels, the disciplines, the
habitat-thinking lens — is set out in
[The Sovereign Engineer](the-sovereign-engineer.md).
