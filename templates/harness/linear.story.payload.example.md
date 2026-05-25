# Linear Story Payload Example

## Title

Example feature acceptance: User completes the primary workflow

## Description

As a product user, I want `User completes the primary workflow` to behave as
specified so the expected outcome is captured and verified.

## Source

- Feature file: `tests/features/example.feature`
- Line: 6
- Feature: Example feature acceptance
- Tags: `@example`

## Acceptance Criteria

- the user sees the expected result
- the result is still available when the user returns

## Gherkin

```gherkin
Scenario: User completes the primary workflow
  Given the required setup exists
  When the user completes the primary action
  Then the user sees the expected result
  And the result is still available when the user returns
```

<!-- swe-harness:gherkin-story:examplemarker1234 -->
