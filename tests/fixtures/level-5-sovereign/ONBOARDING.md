# Onboarding — wordcount

## Day one (developers)

1. Clone, venv, `pip install -e ".[dev]"`, `pre-commit install`,
   `pytest`.
2. Read `CLAUDE.md`, `HARNESS.md`, `CHOICES.md`, and
   `MODEL_ROUTING.md` in order.
3. Skim `audits/` for the most recent governance audit.

## Day one (sibling-team adopters)

1. `claude plugin install wordcount-habitat`
2. `/wordcount-habitat-init` in your repo.
3. Customise the generated `CLAUDE.md` and `HARNESS.md` to your
   actual stack.
4. Open a PR. CI will check spec-first ordering and the constraint
   set automatically.

## Workflow

Spec-first (see CLAUDE.md). All decisions land in CHOICES.md.
Quarterly governance audit reviews the habitat for drift.
