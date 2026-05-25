# Playwright Authoring

Use this file when writing or refactoring Playwright interactions and assertions.

## Table Of Contents

- [Canonical Sources](#canonical-sources)
- [Authoring Rules](#authoring-rules)
- [Locator Strategy](#locator-strategy)
- [Assertions And Waiting](#assertions-and-waiting)
- [Code Generation And Cleanup](#code-generation-and-cleanup)
- [Page Objects](#page-objects)
- [Do Not](#do-not)

## Canonical Sources

- https://playwright.dev/docs/writing-tests
- https://playwright.dev/docs/best-practices
- https://playwright.dev/docs/locators
- https://playwright.dev/docs/test-assertions
- https://playwright.dev/docs/actionability
- https://playwright.dev/docs/codegen
- https://playwright.dev/docs/pom
- https://playwright.dev/docs/handles
- https://playwright.dev/docs/api/class-page

Treat those pages as canonical.

## Authoring Rules

- Perform actions and assert outcomes with Playwright-native patterns.
- Lean on Playwright auto-waiting and actionability.
- Express readiness through web-first assertions instead of sleeps.
- Keep interactions readable and close to how a user perceives the interface.

## Locator Strategy

Prefer locators in this order unless the repo has a deliberate testing contract:

1. `getByRole`
2. `getByLabel`
3. `getByPlaceholder`
4. `getByText` for non-interactive content
5. `getByAltText`
6. `getByTitle`
7. `getByTestId`

Use chaining and filtering to narrow scope before falling back to positional selection.

Use CSS or XPath only when user-facing locators and stable contracts are unavailable.

Remember:

- locators re-resolve against the current page state for each action
- locators are strict for single-element operations
- `first()`, `last()`, and `nth()` are escape hatches, not primary design tools

When list contents change dynamically, avoid patterns that freeze a stale set of elements.

## Assertions And Waiting

- Prefer `await expect(locator).toBeVisible()` and similar web-first assertions.
- Prefer Playwright's async assertions over manual boolean checks.
- Use locator actions and assertions that retry automatically.
- Reach for `locator.waitFor()` or equivalent locator-based readiness only when an assertion is not the right expression.

Important official guidance to internalize:

- `page.waitForTimeout()` is discouraged and should only be used for debugging
- `frame.waitForTimeout()` is discouraged and should only be used for debugging
- `networkidle` is discouraged for test readiness; rely on web assertions instead
- `page.waitForSelector()` is discouraged when a web assertion or locator-based wait expresses the intent better
- `force` disables non-essential actionability checks and should be treated as an exception path

## Code Generation And Cleanup

Use codegen to accelerate drafting, locator discovery, and quick prototyping.

After codegen:

- remove redundant steps
- replace brittle selectors with clearer locators
- add meaningful assertions
- rename tests for the business behavior, not the click sequence
- align the output with the repo's fixtures, base URL, and page-object conventions

Treat generated code as scaffolding, not final design.

## Page Objects

Page object models are useful when the suite is large enough that repeated selectors and flows create maintenance pressure.

Use page objects when:

- repeated UI areas appear across multiple tests
- selectors and small workflows are duplicated
- the suite benefits from a higher-level domain API

Keep page objects narrow:

- model domain actions and stable regions
- keep assertions in tests unless a helper assertion genuinely improves clarity
- do not hide the entire test narrative behind abstractions

## Do Not

- Do not use long CSS or XPath chains by default.
- Do not reach for `first()`, `last()`, or `nth()` before trying better locators.
- Do not write `expect(await locator.isVisible()).toBe(true)` when `await expect(locator).toBeVisible()` is the intended assertion.
- Do not add sleeps or timeouts to "stabilize" tests that should be expressed with locator actions or assertions.
- Do not use `networkidle` as a general readiness rule for testing.
- Do not spray `force: true` through the codebase to mask actionability problems.
- Do not keep raw codegen output without review.
- Do not prefer `ElementHandle` for normal user actions and assertions when locators are the intended Playwright abstraction.
