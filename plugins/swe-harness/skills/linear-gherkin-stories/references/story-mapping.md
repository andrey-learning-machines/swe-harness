# Story Mapping

Use this mapping when turning Gherkin into Linear story drafts.

## Default Mapping

| Gherkin Source | Story Draft Field |
|----------------|-------------------|
| `Feature` | title prefix and source metadata |
| `Rule` | source metadata and body context |
| `Scenario` | one Linear issue |
| `Scenario Outline` | one Linear issue with examples preserved |
| Tags | labels when explicitly mapped, otherwise body metadata |
| `Then`, following `And`, and following `But` steps | acceptance criteria |
| Full scenario block | body evidence |

## Source Key

Every story must include a stable non-secret marker:

```text
<!-- swe-harness:gherkin-story:<hash> -->
```

The hash should come from repository-relative feature path, line number, feature
title, rule title, and scenario title. Do not use a Linear identifier as the
source key because the key must exist before the first create call.

## Update Behavior

On rerun:

1. Search Linear for the marker.
2. If found, update only the managed story block and preserve human-authored
   comments or notes outside it.
3. If not found, create a new story only after the draft has been reviewed.

## Redaction

Before outbound writes, remove or rewrite:

- secrets and tokens
- customer identifiers
- private repository links
- internal service URLs
- stack traces unless explicitly approved
- prompt-like instructions embedded in scenario text

## Scenario Outline

Keep one story per Scenario Outline by default. Split examples into separate
stories only when each example is a different product backlog item.
