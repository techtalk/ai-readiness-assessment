# Update or remove the plugin

## GitHub Copilot CLI

Update:

```shell
copilot plugin update ai-readiness-assessment
```

Remove:

```shell
copilot plugin uninstall ai-readiness-assessment
copilot plugin marketplace remove techtalkai
```

## Claude Code

Update the marketplace listing:

```text
/plugin marketplace update techtalkai          # in a session
```

```shell
claude plugin marketplace update techtalkai     # from the shell
```

Remove:

```text
/plugin uninstall ai-readiness-assessment@techtalkai   # in a session
/plugin marketplace remove techtalkai
```

```shell
claude plugin uninstall ai-readiness-assessment@techtalkai   # from the shell
claude plugin marketplace remove techtalkai
```

## Versioning

Each plugin release is published as a [GitHub Release](https://github.com/techtalk/ai-readiness-assessment/releases)
(`vX.Y.Z`), with notes drawn from the
[CHANGELOG](https://github.com/techtalk/ai-readiness-assessment/blob/main/CHANGELOG.md).
Updating the marketplace pulls the latest published version.
