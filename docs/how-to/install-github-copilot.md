# Install in GitHub Copilot CLI

## Prerequisites

- Node.js 18+ and a GitHub account with Copilot access.

## Install the CLI and sign in

```shell
npm install -g @github/copilot
copilot
```

## Add the marketplace and install the plugin

This repo is the **`techtalkai`** marketplace. From inside a `copilot`
session:

```text
/plugin marketplace add techtalk/ai-readiness-assessment
/plugin install ai-readiness-assessment@techtalkai
```

Or non-interactively, from your shell:

```shell
copilot plugin marketplace add techtalk/ai-readiness-assessment
copilot plugin install ai-readiness-assessment@techtalkai
```

## Confirm it's installed

```shell
copilot plugin list
```

```text
/skills list
```

You should see `ai-readiness-assessment`.

## Next

- [Run an assessment](run-an-assessment.md)
- [Update or remove the plugin](update-or-remove.md)
