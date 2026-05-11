# ADR 0001 — Minimum Python version is 3.10

**Date**: 2026-01-15

## Context

The project initially targeted Python 3.8. By late 2025 every active
developer's machine had Python 3.11+ available.

## Decision

Set the minimum supported Python version to 3.10.

## Consequences

- `X | Y` syntax allowed everywhere.
- Match statements allowed.
- Drops compatibility with Ubuntu 20.04's system Python.
