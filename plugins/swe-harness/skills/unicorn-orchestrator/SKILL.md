---
name: unicorn-orchestrator
description: >-
  Codex-native orchestration workflow for the Unicorn Team custom agents.
  Trigger when the user explicitly asks for delegation, subagents, or parallel
  agent work and the task benefits from specialized architecture, implementation,
  review, DevOps, language-ramp-up, or UI/UX help. Use for multi-step coding
  work, architecture planning, review pipelines, deployment prep, or mixed
  UI/backend efforts where bounded child-agent tasks materially help.
---

# Unicorn Orchestrator

Use this skill only when the user explicitly wants delegation, parallel agent
work, or a subagent-driven workflow. In ordinary turns, keep work local.

This skill targets Codex custom agents installed in `~/.codex/agents`:

| Agent | Name | Use for |
|------|------|---------|
| Architect | `unicorn_architect` | design packages, ADRs, API contracts, tradeoff analysis |
| Developer | `unicorn_developer` | implementation, bug fixes, TDD, refactors |
| QA/Security | `unicorn_qa_security` | review, security findings, regression risk, missing tests |
| DevOps | `unicorn_devops` | CI/CD, IaC, deployment, observability |
| Polyglot | `unicorn_polyglot` | new language or framework ramp-up |
| UI Designer | `ui_ux_designer` | design systems, art direction, UX direction |
| UI Builder | `ui_frontend_builder` | frontend implementation |
| UX Auditor | `ux_auditor` | accessibility, interaction, responsive, perf review |

## Core Rules

1. Form a local plan first.
2. Do not delegate the immediate blocking task if the next local step depends on it.
3. Delegate only bounded tasks with a concrete output.
4. Give each writable agent a clear ownership boundary.
5. Require evidence back: files changed, tests run, findings, or explicit rationale.
6. Wait sparingly; keep doing non-overlapping work while child agents run.
7. For medium or large feature work, establish durable intent first with
   Specification Kit (Spec Kit), Gherkin scenarios, and acceptance evidence
   before delegating implementation.

## Default Routing

| Situation | Pattern |
|----------|---------|
| Simple question or one-shot fix | Handle locally |
| Architecture or multi-service change | `unicorn_architect` first, then `unicorn_developer` |
| Bug fix | `unicorn_developer`; add `unicorn_qa_security` if risk is high |
| Code review | `unicorn_qa_security` |
| Deploy / CI / infra | `unicorn_devops` |
| New language / unfamiliar framework | `unicorn_polyglot`, then implementation agent |
| Visual design / landing page / product UI | `ui_ux_designer`, then `ui_frontend_builder`, then `ux_auditor` |
| Feature files to Linear stories | Use `linear-gherkin-stories` locally for review-first story drafts, then write through Linear MCP only after approval |
| Parallel independent workstreams | Spawn multiple agents with disjoint scopes |

## Delegation Patterns

### Feature

1. For medium or large features, route through `spec-acceptance-harness` first
   so the request has a Spec Kit feature specification, Gherkin scenarios,
   acceptance tests, and story matrix expectations.
2. If design risk is non-trivial, ask `unicorn_architect` for a short design package.
3. Hand implementation to `unicorn_developer` with:
   - exact goal
   - relevant files
   - acceptance criteria
   - explicit request to write or update tests first when practical
   - required validation commands
4. If the change is security-sensitive, externally facing, or broad, run `unicorn_qa_security` on the result.

### Linear Stories

Use `linear-gherkin-stories` locally when the user asks to turn scenarios into
backlog items. Generate story drafts, review them with the user, and then create
or update Linear issues only after explicit approval.

### Bug Fix

Hand `unicorn_developer` a reproduction target and require:

- failing test or clear reproduction
- root cause, not symptom patch
- regression checks
- concise summary of changed files

### Review

Hand `unicorn_qa_security`:

- diff or files to inspect
- areas of concern
- request for findings first, with file references and severity

### Frontend

1. `ui_ux_designer` produces the design system or implementation direction.
2. `ui_frontend_builder` implements with explicit file ownership.
3. `ux_auditor` reviews accessibility, responsiveness, and motion/perf issues.

## Quality Gates

Before accepting delegated work, check:

- requested files or artifacts were actually produced
- tests or validation commands ran when expected
- risky assumptions are called out
- no scope drift into unrelated files
- review findings are addressed or deliberately deferred

## Prompting Rules For Child Agents

- State ownership clearly for writable work.
- Tell the agent it is not alone in the codebase and must not revert unrelated edits.
- Ask for the smallest useful final payload: summary, files changed, test results, findings, open questions.
- For read-only work, require citations to files, symbols, or commands.
