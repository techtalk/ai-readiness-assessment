# Why there is no portfolio score

Roll a portfolio report in front of anyone senior and the first question
is always the same: *so what's our number?*

There isn't one. Not because it hasn't been built yet — because a single
number would destroy the only thing the portfolio view adds.

## The average erases the finding

The reason to look across repositories at all is that one team's
cognitive read, measured against several different habitats, produces
several different gaps. **The spread of those gaps is the finding.**

Consider two subjects:

| Subject | Habitat maturity | Cognitive read | Gap | Regime |
|---|---|---|---|---|
| `greenfield-api` | 3.9 | 4 | +0.1 | Coherent |
| `legacy-batch` | 1.6 | 4 | +2.4 | Ambition outpaces enablement |

Average those gaps and you get +1.25 — "mildly ambitious". That
describes neither subject. It hides a team working comfortably in one
place and fighting its environment in another, and it points at no
action, because the two situations need opposite responses: hold the
first, invest heavily in habitat for the second.

The average is not a summary of the two facts. It is the destruction of
both.

## A ceiling is not a mean

The single-repo instrument already refuses to average — the
[weakest discipline is the ceiling](coherence-not-level.md#the-weakest-discipline-is-the-ceiling),
because a specification you cannot verify is aspiration, not control.
The portfolio view applies the same rule one level up, and splits the
result:

- **Common weak** — dimensions weak across most of the estate. This is
  the *enablement* backlog. It belongs to whoever provides the habitat.
- **Locally weak** — dimensions weak in one or two subjects. This is
  that team's own backlog.

That split is doing real work. Without it, a matrix across teams becomes
a league table, and the fastest way to make an honest assessment useless
is to give people a reason to game it. Separating what enablement owes
the estate from what a team owes itself keeps the report a diagnostic
rather than a ranking.

## What to say when you are asked anyway

Show the spread and the split ceiling. They answer the question the
number was standing in for — *how are we doing, and what do we do next?*
— and they answer it in a form somebody can act on tomorrow morning.

A grade answers neither. It just ends the conversation.
