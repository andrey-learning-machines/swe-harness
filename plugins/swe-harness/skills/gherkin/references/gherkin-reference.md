# Gherkin Reference

Use this file for exact authoring rules and quick syntax recall.

## Table Of Contents

- [File Shape And Keywords](#file-shape-and-keywords)
- [Step Semantics](#step-semantics)
- [Shared Context](#shared-context)
- [Parameterization And Step Arguments](#parameterization-and-step-arguments)
- [Tags And Language](#tags-and-language)
- [Compact Templates](#compact-templates)
- [Do Not](#do-not)

Treat the official Cucumber documentation as canonical:

- https://cucumber.io/docs/gherkin/
- https://cucumber.io/docs/gherkin/reference/
- https://cucumber.io/docs/gherkin/languages/
- https://cucumber.io/docs/cucumber/api/

This file deliberately paraphrases the docs to stay concise. Re-open the official pages when any rule is uncertain.

## File Shape And Keywords

- Start a feature file with `Feature:` as the first primary keyword.
- Keep exactly one `Feature` per `.feature` file.
- Use these structural keywords and aliases:
  - `Rule:`
  - `Scenario:` or `Example:`
  - `Background:`
  - `Scenario Outline:` or `Scenario Template:`
  - `Examples:` or `Scenarios:`
- Use these step keywords without a trailing colon:
  - `Given`
  - `When`
  - `Then`
  - `And`
  - `But`
  - `*`
- Use line comments only. Start them with `#`. Do not use block comments.
- Use spaces or tabs for indentation. Prefer two spaces for readability.
- Use free-form descriptions under `Feature`, `Rule`, `Background`, `Scenario`, and `Scenario Outline` when they clarify intent.
- Keep description lines from accidentally starting with a Gherkin keyword, or they will terminate the description block.

## Step Semantics

- Use `Given` for context and preconditions.
- Use `When` for the event or action.
- Use `Then` for an observable outcome.
- Use `And` and `But` to improve readability for repeated step types.
- Use `*` when a list-like cadence reads better than repeated conjunctions.
- Keep scenarios short enough to remain readable. The official guidance recommends roughly 3 to 5 steps.
- Remember that Cucumber ignores the step keyword when matching step definitions. Duplicate text such as `Given there is money in my account` and `Then there is money in my account` will collide.
- Prefer domain language over technical test language.

## Shared Context

- Use `Rule` to group scenarios around a single business rule inside a feature.
- Use `Background` only for incidental context that every scenario in the enclosing `Feature` or `Rule` needs.
- Keep `Background` short and memorable.
- Use at most one `Background` per `Feature` and one per `Rule`.
- Split scenarios into additional `Rule` or `Feature` groups if different backgrounds are needed.

## Parameterization And Step Arguments

- Use `Scenario Outline` when the same scenario structure repeats with different values.
- Put placeholders in angle brackets, such as `<user>` or `<amount>`.
- Add one or more `Examples` tables below the outline.
- Remember that a `Scenario Outline` is a template and is not executed directly.
- Use parameters in descriptions and multiline step arguments when helpful.

- Use `Doc Strings` for larger text payloads.
- Delimit a Doc String with `"""` on its own line.
- Use triple backticks if the project tooling handles them cleanly, but remember that editor support can lag behind Cucumber support.
- Add a content type such as `"""markdown` when useful.
- Remember that Doc String indentation is significant relative to the opening delimiter.

- Use `Data Tables` for lists or structured row data.
- Remember that the table is passed as the last argument to the step definition.
- Escape newlines as `\n`, pipe characters as `\|`, and backslashes as `\\` inside table cells.

## Tags And Language

- Use tags to organize features and scenarios, run subsets of scenarios, or scope hooks.
- Place tags above:
  - `Feature`
  - `Rule`
  - `Scenario`
  - `Scenario Outline`
  - `Examples`
- Do not place tags above `Background` or individual steps.
- Separate multiple tags with spaces on the same line when convenient.
- Use tagged `Examples` blocks in `Scenario Outline` when different example sets need different metadata or filters.

- Use the same spoken language your users and domain experts use for the domain.
- Add `# language: xx` on the first line when the file uses a localized keyword dialect.
- Assume English if no language header or equivalent config is present.
- Check the official localization table before mixing dialects or introducing non-English keywords.

## Compact Templates

```gherkin
Feature: Billing
  Rule: Calculate tax for taxable invoices
    Background:
      Given a taxable invoice exists

    Scenario: Apply sales tax
      When the invoice is finalized
      Then the total includes sales tax
```

```gherkin
Scenario Outline: Withdraw funds
  Given an account has a balance of <starting_balance>
  When the user withdraws <withdrawal_amount>
  Then the remaining balance is <remaining_balance>

  Examples:
    | starting_balance | withdrawal_amount | remaining_balance |
    | 100              | 40                | 60                |
    | 75               | 25                | 50                |
```

## Do Not

- Do not add a colon after step keywords.
- Do not use more than one `Feature` per file.
- Do not use block comments.
- Do not verify hidden internals in `Then` unless they are externally observable.
- Do not use `Background` for long or complicated setup.
- Do not invent syntax that you have not verified against the official docs.
