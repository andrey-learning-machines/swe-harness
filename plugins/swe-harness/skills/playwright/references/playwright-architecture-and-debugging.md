# Playwright Architecture And Debugging

Use this file when structuring a suite, stabilizing it, or debugging failures.

## Table Of Contents

- [Canonical Sources](#canonical-sources)
- [Isolation](#isolation)
- [Authentication](#authentication)
- [Fixtures, Projects, And Local Servers](#fixtures-projects-and-local-servers)
- [Tracing And Debugging](#tracing-and-debugging)
- [Maintenance Heuristics](#maintenance-heuristics)
- [Do Not](#do-not)

## Canonical Sources

- https://playwright.dev/docs/browser-contexts
- https://playwright.dev/docs/auth
- https://playwright.dev/docs/test-fixtures
- https://playwright.dev/docs/test-projects
- https://playwright.dev/docs/test-webserver
- https://playwright.dev/docs/trace-viewer-intro
- https://playwright.dev/docs/pom

Treat those pages as canonical.

## Isolation

Playwright's default model is test isolation through browser contexts.

Preserve that by default:

- let each test own its own page and context
- keep tests runnable independently
- avoid hidden order dependencies
- only reuse shared state when the suite has an explicit, justified design for it

If a failure depends on previous tests, the suite structure is usually the problem, not the absence of more waits.

## Authentication

Playwright recommends storing authenticated browser state on disk and reusing it when appropriate.

Use that approach intentionally:

- keep auth state under a dedicated ignored directory such as `playwright/.auth`
- treat state files as sensitive
- use setup projects when shared authenticated state is safe for the suite
- avoid a shared account when tests mutate server-side state in parallel

## Fixtures, Projects, And Local Servers

Use fixtures to provide environment and reusable capabilities to tests.

Use projects when the suite truly needs matrices such as:

- multiple browsers
- multiple devices
- multiple environments
- logged-in versus logged-out coverage

Use the Playwright `webServer` option when tests must boot a local app as part of the run and the repo already follows or clearly benefits from that pattern.

Keep configuration proportional to the suite:

- do not create custom fixtures too early
- do not create many projects unless the coverage matrix is real
- do not create page objects before repeated maintenance pain appears

## Tracing And Debugging

Prefer Playwright-native debugging tools before guessing:

- HTML report
- trace viewer
- codegen for locator discovery
- headed runs or UI mode when local exploration is useful

Trace guidance from the official docs:

- traces are especially valuable for failures and retries
- `trace: 'on-first-retry'` is the default style in Playwright starter config for continuous integration workflows
- `trace: 'on'` is heavier and should not become the default casually

When reading a trace:

- inspect the locator used for the failing action
- inspect actionability details
- inspect network and console around the step
- inspect DOM snapshots before and after the action

## Maintenance Heuristics

- Prefer clearer tests over hyper-deduplicated tests when the simpler version is easier to maintain.
- Add fixtures, page objects, or helpers only after repetition is obvious.
- Prefer mocking or routing dependencies you do not control.
- Keep browser workflows aligned with the product's user-visible behavior, not internal implementation details.
- If tests are flaky, fix locator quality, state control, and assertions before increasing timeouts.

## Do Not

- Do not break test isolation casually.
- Do not commit authentication state files.
- Do not share one account across parallel tests that mutate the same server-side state.
- Do not create fixture stacks that hide what a test actually needs.
- Do not create project matrices larger than the real requirement.
- Do not default traces to every run without understanding the performance cost.
- Do not debug failures only from screenshots when traces or reports are available.
- Do not paper over flaky tests with larger timeouts before fixing locator quality, state control, or assertion design.
