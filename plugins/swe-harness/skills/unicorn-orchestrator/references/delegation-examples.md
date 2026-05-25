# Delegation Examples

Codex-native prompt examples for the Unicorn custom agents. These are meant to
show what to hand each agent, not a rigid literal tool payload.

## Example 1: Architect Then Developer

Use this when a change spans multiple services or needs an explicit design
before implementation.

### Spawn `unicorn_architect`

```text
Design the cloud migration plan for the invoice export pipeline.

Context:
- Existing batch job lives in services/billing/export/
- New target is an event-driven worker pipeline
- Must preserve current CSV schema and retry semantics

Deliver:
- short ADR
- module/file plan
- failure modes and rollback notes
- implementation handoff for `unicorn_developer`
```

### Spawn `unicorn_developer`

```text
Implement the invoice export migration from the approved design package.

Ownership:
- services/billing/export/
- tests around export dispatch and retries

Constraints:
- write the narrowest failing test or reproduction first
- preserve external CSV contract
- do not revert unrelated edits

Return:
- summary
- files changed
- tests run
- remaining risks
```

## Example 2: Direct Bug Fix

Use this when the design is already obvious and the main need is a tight
root-cause fix.

### Spawn `unicorn_developer`

```text
Fix the bug where password-reset tokens remain valid after use.

Context:
- token issue path in auth/reset_tokens.py
- validation path in auth/routes/reset.py
- existing regression tests under tests/auth/

Requirements:
- start from a failing test or exact reproduction
- fix root cause, not just surface behavior
- run targeted regression tests
```

## Example 3: Review Pass

Use this after implementation when correctness or security risk is material.

### Spawn `unicorn_qa_security`

```text
Review the webhook verification changes in payments/webhooks.py and related tests.

Focus:
- signature validation
- replay protection
- tenant isolation
- missing regression coverage

Return findings first with severity and file references.
```

## Example 4: Frontend Pipeline

Use this when the user explicitly wants design help plus implementation.

### Spawn `ui_ux_designer`

```text
Define a design system and implementation direction for the new analytics dashboard.

Context:
- audience is finance operators
- desktop-first, responsive down to tablet
- stack is React + Tailwind

Return:
- visual thesis
- color/type system
- component plan
- notes for `ui_frontend_builder`
```

### Spawn `ui_frontend_builder`

```text
Implement the dashboard using the approved design direction.

Ownership:
- frontend/src/pages/analytics/
- shared chart and filter components touched by this feature

Requirements:
- preserve existing app shell patterns
- cover loading, empty, and error states
- report accessibility and responsive states covered
```

### Spawn `ux_auditor`

```text
Review the analytics dashboard changes for accessibility, responsive behavior,
interaction quality, and obvious performance risks. Lead with findings.
```

## Example 5: DevOps Delivery Work

### Spawn `unicorn_devops`

```text
Add safe deployment checks for the ingestion worker.

Ownership:
- .github/workflows/
- deploy scripts and runbooks

Return:
- files changed
- deployment steps
- rollback procedure
- monitoring implications
```
