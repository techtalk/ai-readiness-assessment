# ADR 0001 — Minimum Python version is 3.10

**Date**: 2026-01-15

## Context

The project initially targeted Python 3.8 because that was the system
Python on the laptops the team had. By late 2025 every active
developer's machine had Python 3.11+ available, and the codebase had
started accumulating `Union[]` and `Optional[]` annotations that we'd
rather write as `X | None`.

## Decision

Set the minimum supported Python version to 3.10. Update
`pyproject.toml` and the CI matrix.

## Consequences

- `X | Y` syntax allowed everywhere; old-syntax unions become a lint
  failure under ruff `UP` rules.
- Match statements allowed.
- Anyone still on 3.8 needs to upgrade their local environment. None
  of the active developers are affected.
- Drops compatibility with Ubuntu 20.04's system Python; not a real
  loss since the project isn't intended for that environment.
