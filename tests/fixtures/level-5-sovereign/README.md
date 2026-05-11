# word-count

A small Python utility — and the reference habitat the team
publishes as the `wordcount-habitat` plugin so sibling teams can
adopt the same conventions in one step.

## Install

Clone, `pip install -e ".[dev]"`, `pre-commit install`.

## Use

```bash
python -m wordcount path/to/file.txt
```

## How this project is run

- Conventions: `CLAUDE.md`
- Constraints (machine-checkable): `HARNESS.md`
- Specs and plans: `specs/`, `specs/plans/`
- Adversarial reviews: `docs/objections/`
- Decision archaeology: `CHOICES.md`
- Reflections: `REFLECTION_LOG.md`
- Decisions (lightweight): `docs/adr/`
- Governance audits (quarterly): `audits/`
- Model routing and cost discipline: `MODEL_ROUTING.md`
- Published habitat plugin: `.claude-plugin/plugin.json`

Sibling teams install the habitat by installing the plugin and
running `/wordcount-habitat-init` in their own repo.
