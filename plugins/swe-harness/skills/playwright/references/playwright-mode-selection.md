# Playwright Mode Selection

Use this file when deciding what kind of Playwright output the task should produce.

## Table Of Contents

- [Canonical Sources](#canonical-sources)
- [Mode Selection](#mode-selection)
- [Repo Inspection Checklist](#repo-inspection-checklist)
- [Language And Binding Choice](#language-and-binding-choice)
- [Playbooks For Codex](#playbooks-for-codex)
- [Do Not](#do-not)

## Canonical Sources

- https://playwright.dev/
- https://playwright.dev/docs/writing-tests
- https://playwright.dev/docs/getting-started-cli
- https://playwright.dev/docs/getting-started-mcp
- https://playwright.dev/docs/test-projects

Treat those pages as the source of truth.

## Mode Selection

Choose the lightest Playwright mode that matches the actual task.

### Playwright Test

Prefer this when the result should become durable regression coverage in the repository.

Use when:

- the repo already uses Playwright Test
- the workflow should run in continuous integration
- the task needs retries, projects, reporters, traces, fixtures, or rich test structure
- the user is asking for end-to-end coverage rather than a disposable script

### Playwright Library Script

Prefer this when the result is a checked-in automation script rather than a test suite entry.

Use when:

- the task is a scripted browser utility
- assertions are secondary or minimal
- the repo uses Playwright as a browser automation library instead of the test runner
- the task is operational rather than coverage-oriented

### Playwright CLI For Coding Agents

Prefer this for agent-driven browser playbooks when the environment already exposes the CLI workflow.

The official docs describe `playwright-cli` as best for coding agents that favor token-efficient, skill-based workflows, while the Model Context Protocol server is better for specialized loops that benefit from persistent state and iterative reasoning.

Use when:

- the task is transient and agent-operated
- the workflow is command-oriented rather than checked-in code
- token efficiency matters
- the environment already has or can explicitly install the Playwright CLI

### Model Context Protocol Server

Model Context Protocol is a standard tool interface for model-driven agents.

Prefer this when:

- persistent browser state and structured page snapshots matter
- the environment already uses Model Context Protocol tools
- the agent needs iterative page reasoning rather than a short command sequence

## Repo Inspection Checklist

- Check for `playwright.config.*`.
- Check for `@playwright/test` in `package.json`.
- Check for Python, Java, or .NET Playwright setup before defaulting to Node.js examples.
- Check existing test directories, fixtures, auth setup, reporters, trace config, and projects.
- Check package-manager lockfiles and test scripts before suggesting commands.
- Check whether the app already expects a local web server, base URL, or authenticated state bootstrap.

## Language And Binding Choice

- Stay in the repo's existing binding whenever possible.
- Prefer the repo's current language over introducing a new one.
- If the repo is greenfield and the user did not specify a language, TypeScript or JavaScript is the most directly documented default path on the main Playwright docs.
- If the repo already uses Python, Java, or .NET, continue in that stack unless the user asks to migrate.

## Playbooks For Codex

Within this skill, a playbook means a repeatable browser workflow for Codex.

Encode it as:

- a checked-in Playwright test when the workflow should guard against regressions
- a checked-in Playwright script when the workflow is a utility
- a Playwright CLI or Model Context Protocol server workflow when the task is agent-executed and transient

## Do Not

- Do not create Playwright Test files when a short library script is the real requirement.
- Do not create a disposable CLI playbook when the user actually needs checked-in regression tests.
- Do not assume Playwright CLI or Model Context Protocol tooling is available without checking.
- Do not change the repo's Playwright binding or language casually.
- Do not skip repo inspection and then impose a generic Playwright structure.
