---
name: playwright
description: Build, review, refactor, and debug Playwright tests, browser automation scripts, and coding-agent browser playbooks. Use when Codex needs to work with Playwright Test, Playwright library scripts, Playwright CLI workflows for coding agents, or Model Context Protocol server browser automation; write resilient locators and assertions; structure fixtures, projects, authentication, traces, code generation output, local web-server config, page objects, or cross-browser setups in TypeScript, JavaScript, Python, Java, or .NET.
---

# Playwright

## Overview

Use this skill for Playwright work across three common outcomes:

- checked-in automated browser tests
- checked-in browser automation scripts
- repeatable Codex browser playbooks

In this skill, a "playbook" means a reusable browser workflow for Codex. Implement playbooks in the form that best matches the task:

- Playwright Test when the workflow should become regression coverage in the repo
- Playwright library scripts when the workflow is a utility or one-off browser automation program
- Playwright CLI or Playwright Model Context Protocol server workflows when the task is agent-driven browser control and the integration is already available

Treat the official Playwright documentation as the canonical and most up-to-date source. Use this skill as a working guide, not as a substitute for the official docs. If command syntax, configuration, API behavior, language support, or tool availability is uncertain, re-open the official docs before finalizing.

- [Playwright homepage](https://playwright.dev/)
- [Writing tests](https://playwright.dev/docs/writing-tests)
- [Best Practices](https://playwright.dev/docs/best-practices)
- [Locators](https://playwright.dev/docs/locators)
- [Assertions](https://playwright.dev/docs/test-assertions)
- [Isolation](https://playwright.dev/docs/browser-contexts)
- [Authentication](https://playwright.dev/docs/auth)
- [Projects](https://playwright.dev/docs/test-projects)
- [Page object models](https://playwright.dev/docs/pom)
- [Test generator](https://playwright.dev/docs/codegen)
- [Trace viewer](https://playwright.dev/docs/trace-viewer-intro)
- [Auto-waiting and actionability](https://playwright.dev/docs/actionability)
- [Coding agents CLI](https://playwright.dev/docs/getting-started-cli)
- [Model Context Protocol server](https://playwright.dev/docs/getting-started-mcp)

## Workflow

1. Identify which Playwright mode actually fits the task:
   - checked-in tests
   - checked-in scripts
   - agent playbook
2. Inspect the repo before drafting:
   - detect language and package manager
   - detect existing Playwright usage, config, fixtures, auth setup, projects, reporters, and local dev-server wiring
   - preserve repo conventions unless they are clearly brittle or incorrect
3. Choose the existing repo binding first:
   - stay in TypeScript or JavaScript repos that already use `@playwright/test`
   - stay in Python, Java, or .NET repos that already use those Playwright bindings
   - do not introduce a different binding unless the user explicitly wants that
4. Open the reference file that matches the task:
   - [references/playwright-mode-selection.md](references/playwright-mode-selection.md) for deciding between Playwright Test, library scripts, Playwright CLI, or Model Context Protocol server workflows
   - [references/playwright-authoring.md](references/playwright-authoring.md) for locators, assertions, actionability, code generation, and page object guidance
   - [references/playwright-architecture-and-debugging.md](references/playwright-architecture-and-debugging.md) for fixtures, projects, authentication, local servers, traces, and suite structure
5. Draft the smallest change that solves the task without fighting the repo.
6. Re-open the official Playwright docs if any behavior is uncertain. Do not guess.
7. Validate against the review checklist before presenting the result as finished.

## Codex Execution Notes

- Prefer the repo's existing Playwright language binding and file layout over personal preference.
- Prefer the repo's existing package manager and command style over generic `npm` examples.
- Prefer checked-in tests for durable coverage and checked-in scripts for utilities. Use agent-only workflows when the task is inherently transient.
- If Playwright CLI or the Model Context Protocol server is not configured in the environment, do not pretend it is. Fall back to repo-local Playwright usage.
- Cite the official Playwright docs in user-facing answers when the user wants rule sources, latest guidance, or explanation of a Playwright behavior.
- Treat generated code from codegen as a starting point that usually needs refactoring.

## Core Rules

- Use resilient locators first. Prioritize user-facing attributes and explicit contracts.
- Prefer `getByRole`, `getByLabel`, `getByPlaceholder`, `getByText`, `getByAltText`, `getByTitle`, and `getByTestId` over brittle selectors.
- Use Playwright's web-first assertions such as `await expect(locator).toBeVisible()`.
- Rely on auto-waiting and actionability checks instead of manual sleeps.
- Keep tests isolated. Assume each test should stand alone unless the suite deliberately uses a different pattern.
- Use authentication state intentionally and keep it out of version control.
- Use projects for browser, device, environment, or authenticated-state matrices when that matrix is part of the requirement.
- Use page objects only when repetition and maintenance pressure justify them.
- Use trace viewer to debug failures rather than guessing from screenshots alone.
- Use local web-server config when tests depend on a local app startup sequence.

## Do Not

- Do not assume this skill is more current than the official Playwright docs.
- Do not guess on Playwright API behavior, CLI flags, configuration names, or language-binding differences when the official docs can answer it.
- Do not introduce Playwright into a repo without first checking whether the repo already has a browser-testing strategy and conventions.
- Do not switch a repo from one Playwright binding to another unless the user explicitly wants that migration.
- Do not default to long CSS or XPath chains when role, label, text, or test id locators exist.
- Do not use `first()`, `last()`, or `nth()` as the first answer to locator ambiguity.
- Do not rely on `page.waitForTimeout()` or `frame.waitForTimeout()` in production test code. Those are for debugging only.
- Do not rely on `networkidle` readiness checks for test correctness when web assertions can express readiness directly.
- Do not write manual assertions such as `expect(await locator.isVisible()).toBe(true)` when a web-first assertion exists.
- Do not bypass actionability with `force` unless there is a concrete, justified reason.
- Do not commit authentication state files.
- Do not test third-party services you do not control when mocking or routing the dependency is the better design.
- Do not accept raw codegen output without review and cleanup.
- Do not over-abstract early with fixtures or page objects before the suite actually needs them.
- Do not use stale `ElementHandle`-style flows for ordinary user actions and assertions when locators are the correct abstraction.

## Review Checklist

- Confirm the chosen Playwright mode matches the task.
- Confirm the change follows the repo's existing language binding, test runner, and package-manager conventions.
- Confirm locators are resilient and user-facing where possible.
- Confirm assertions are web-first and retry-aware.
- Confirm there are no unnecessary manual waits, brittle selectors, or unjustified forced actions.
- Confirm authentication state, if used, is stored safely and ignored by version control.
- Confirm fixtures, projects, and page objects are justified by repetition, matrix coverage, or suite scale.
- Confirm debugging guidance uses traces, reports, or Playwright-native tools instead of guesswork.
- Confirm any uncertain API or configuration rule against the official Playwright docs before presenting the result as final.

## References

- Read [references/playwright-mode-selection.md](references/playwright-mode-selection.md) for deciding whether the task should become a test, script, or agent playbook.
- Read [references/playwright-authoring.md](references/playwright-authoring.md) for locators, assertions, actionability, codegen cleanup, and authoring rules.
- Read [references/playwright-architecture-and-debugging.md](references/playwright-architecture-and-debugging.md) for fixtures, projects, authentication, local web servers, traces, and suite maintenance.
- Use the official Playwright docs as the canonical source:
  - [Playwright](https://playwright.dev/)
  - [Writing tests](https://playwright.dev/docs/writing-tests)
  - [Best Practices](https://playwright.dev/docs/best-practices)
  - [Locators](https://playwright.dev/docs/locators)
  - [Assertions](https://playwright.dev/docs/test-assertions)
  - [Isolation](https://playwright.dev/docs/browser-contexts)
  - [Authentication](https://playwright.dev/docs/auth)
  - [Projects](https://playwright.dev/docs/test-projects)
  - [Page object models](https://playwright.dev/docs/pom)
  - [Test generator](https://playwright.dev/docs/codegen)
  - [Trace viewer](https://playwright.dev/docs/trace-viewer-intro)
  - [Auto-waiting](https://playwright.dev/docs/actionability)
  - [Coding agents CLI](https://playwright.dev/docs/getting-started-cli)
  - [Model Context Protocol server](https://playwright.dev/docs/getting-started-mcp)
