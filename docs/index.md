# TechTalk AI Readiness Assessment

A self-contained plugin for [Claude Code](https://claude.com/claude-code)
and [GitHub Copilot CLI](https://github.com/features/copilot) that
assesses how ready a team — and its codebase — is to collaborate with AI.

Invoke it once in any repository and it scans for evidence, asks a few
clarifying questions, and produces a timestamped report that places the
team on two complementary maps:

- the **[Agentic Experience 5-Level Habitat Maturity Model](reference/habitat-maturity-model.md)** —
  fourteen dimensions of what the team's habitat *actually delivers*; and
- the **[Sovereign Engineer cognitive ladder](reference/cognitive-ladder.md)** (L0–L5) —
  what the team can *think and do*.

The distance between them is the **[Habitat Build Gap](reference/habitat-build-gap.md)** —
a coherence diagnostic that points at the single most valuable next move.

[Run your first assessment](tutorials/your-first-assessment.md){ .md-button .md-button--primary }
[Install the plugin](how-to/install-github-copilot.md){ .md-button }
[Product overview (techtalk.at)](https://techtalk.at/ai-readiness-assessment-draft/){ .md-button }

!!! tip "See a real report"
    Curious what the output looks like? We ran the assessment against
    **this plugin's own repo** — read the
    [example self-assessment](examples.md) (markdown + rendered HTML).

---

## Find your way around

This documentation follows the [Diátaxis](https://diataxis.fr/) framework —
four kinds of documentation for four kinds of need.

| | |
| --- | --- |
| **[Tutorials](tutorials/index.md)** — learning-oriented | Start here. A guided, end-to-end run that produces your first assessment. |
| **[How-to guides](how-to/index.md)** — task-oriented | Recipes: install in each tool, run an assessment, read the gap, render the HTML report. |
| **[Reference](reference/index.md)** — information-oriented | The model's fourteen dimensions, the cognitive ladder, the gap formula, the output structure. |
| **[Explanation](explanation/index.md)** — understanding-oriented | Why two maps, why coherence beats level, why the instrument is standalone. |

---

## What you get from one run

1. A discovery report of the habitat documents and signals found (with paths).
2. A **Habitat Maturity Profile** — all fourteen model dimensions placed L1–L5, with the model's own verbs, and a headline **Habitat Maturity Level**.
3. A **cognitive level** (L0–L5) with a one-line rationale anchored in the weakest of three disciplines.
4. The **Habitat Build Gap** and its regime (Coherent / Ambition outpaces enablement / Inherited habitat).
5. Strengths, gaps, and three evidence-anchored recommendations.
6. A gap-anchored reading path into *[The Sovereign Engineer](explanation/the-sovereign-engineer.md)* and a single TechTalk engagement suggestion.

The assessment is **fully self-contained** — it depends on no other
plugin, agent, or service. See
[Why it is self-contained](explanation/self-contained.md).
