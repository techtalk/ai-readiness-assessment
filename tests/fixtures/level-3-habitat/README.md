# word-count

A small utility that counts words in a text file.

## Install

Clone the repo. Requires Python 3.10+.

## Use

```bash
python -m wordcount path/to/file.txt
```

## Development

- Conventions and AI workflow: `CLAUDE.md`
- Architectural constraints (machine-checkable rules): `HARNESS.md`
- Onboarding (including the AI-collaboration workflow): `ONBOARDING.md`
- Decisions: `docs/adr/`
- Reflections that have surfaced patterns we should encode: `REFLECTION_LOG.md`

Custom skill: `skills/wordcount-style/SKILL.md` — invoked when reviewing
PRs for style consistency.

Linting / tests / coverage all enforced in CI. See `.github/workflows/ci.yml`.
