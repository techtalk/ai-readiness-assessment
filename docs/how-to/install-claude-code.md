# Install in Claude Code

The same `techtalkai` marketplace works from Claude Code — register the
marketplace, then install the plugin.

## Prerequisites

- The `claude` CLI installed ([code.claude.com](https://code.claude.com))
  and a signed-in Anthropic account.

## Add the marketplace and install the plugin

From inside a Claude Code session:

```text
/plugin marketplace add techtalk/ai-readiness-assessment
/plugin install ai-readiness-assessment@techtalkai
```

Or non-interactively, from your shell:

```shell
claude plugin marketplace add techtalk/ai-readiness-assessment
claude plugin install ai-readiness-assessment@techtalkai
```

## Confirm it's installed

```shell
claude plugin list
```

## Next

- [Run an assessment](run-an-assessment.md)
- [Update or remove the plugin](update-or-remove.md)
