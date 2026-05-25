# Orchestrator Workflow Examples

These traces show how a Codex-native Unicorn workflow should flow from task
classification through delegation and quality gates.

## Trace 1: Simple Fix

```text
User asks for a narrow bug fix in one area.

1. Keep planning local.
2. Spawn `unicorn_developer` with the failing behavior, likely files, and
   required validation.
3. Accept only if the result includes the root cause, changed files, and tests.
4. Return the fix summary to the user.
```

## Trace 2: Multi-Service Feature

```text
User asks for a feature that crosses service boundaries.

1. Spawn `unicorn_architect` first for the design package.
2. Check the handoff:
   - decision summary exists
   - modules/files to touch are named
   - constraints and validation criteria are explicit
3. Spawn `unicorn_developer` with that handoff and a bounded write scope.
4. If the feature is externally facing or security-sensitive, run
   `unicorn_qa_security` on the result before closing.
```

## Trace 3: Parallel Workstreams

```text
User asks for backend, frontend, and deployment changes that can proceed in
parallel after a shared design step.

1. Do the shared design locally or via `unicorn_architect`.
2. Spawn independent agents with disjoint ownership:
   - `unicorn_developer` for backend files
   - `ui_frontend_builder` for frontend files
   - `unicorn_devops` for CI/deployment files
3. While they run, continue non-overlapping local work.
4. Gate each return on scope discipline, validation, and missing risks.
5. Run `ux_auditor` or `unicorn_qa_security` if the integrated result is risky.
```

## Trace 4: New Language Or Framework

```text
User asks for a change in an unfamiliar ecosystem.

1. Spawn `unicorn_polyglot` for a compact ramp-up:
   - idioms
   - tooling
   - testing conventions
   - gotchas
2. Use that handoff to brief `unicorn_developer`.
3. Keep the implementation scope narrow until the first working slice lands.
```

## Trace 5: Review-First Workflow

```text
User asks for review or wants a second pass on a risky diff.

1. Spawn `unicorn_qa_security`.
2. Require findings first, with severity and file references.
3. If findings are actionable, hand only those fixes to `unicorn_developer`.
4. Re-review only the touched areas instead of re-running the whole pipeline.
```

## Standard Gates

- The agent touched only the intended files or clearly justified any expansion.
- Validation actually ran when it was requested.
- Risky assumptions are called out explicitly.
- Findings include concrete file references.
- Rework is driven by specific failed gates, not vague dissatisfaction.
