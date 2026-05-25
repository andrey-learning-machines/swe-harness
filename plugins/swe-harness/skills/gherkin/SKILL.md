---
name: gherkin
description: Draft, review, refactor, and explain Cucumber Gherkin `.feature` files and executable specifications. Use when Codex needs to write or validate Given/When/Then scenarios, Scenario Outlines, Backgrounds, Rules, Examples tables, tags, Doc Strings, Data Tables, localized Gherkin keywords, or step-organization guidance for Cucumber projects.
---

# Gherkin

## Overview

Use this skill to write precise, readable Cucumber Gherkin and to review existing feature files for syntax errors, ambiguity, and anti-patterns.

Treat the official Cucumber documentation as the source of truth. Use this skill as a distilled working guide, not as a replacement for the live documentation. If syntax, keyword support, localization behavior, or tag behavior is uncertain, open the official docs before finalizing:

- [Gherkin overview](https://cucumber.io/docs/gherkin/)
- [Gherkin reference](https://cucumber.io/docs/gherkin/reference/)
- [Gherkin localisation](https://cucumber.io/docs/gherkin/languages/)
- [Step organization](https://cucumber.io/docs/gherkin/step-organization/)
- [Anti-patterns](https://cucumber.io/docs/guides/anti-patterns/)
- [Cucumber reference: tags and hooks](https://cucumber.io/docs/cucumber/api/)

## Workflow

1. Identify the task:
   - write a new `.feature` file
   - review or refactor an existing `.feature` file
   - explain Gherkin syntax or Cucumber authoring choices
   - propose or review step-definition organization
2. Inspect the repository before drafting:
   - detect whether the repo uses English or localized keywords
   - inspect existing `.feature` files, tags, and step definitions
   - preserve repo conventions unless they contradict official syntax or create an obvious anti-pattern
3. Draft or review the feature file using the core rules in this file.
4. Open [references/gherkin-reference.md](references/gherkin-reference.md) for exact keyword behavior, multiline arguments, Scenario Outline rules, tags, or localization details.
5. Open [references/cucumber-writing-and-anti-patterns.md](references/cucumber-writing-and-anti-patterns.md) for step-definition organization, reuse strategy, and refactoring guidance.
6. Re-open the official Cucumber docs whenever there is uncertainty. Do not guess on syntax.
7. Finalize only after the review checklist passes.

## Codex Execution Notes

- Load the reference files selectively to preserve context. Do not load both unless the task genuinely needs both.
- Cite the official Cucumber URLs in user-facing responses when the user asks for the rule source, an explanation of syntax, or the most up-to-date guidance.
- Inspect the repo’s existing Gherkin and step-definition style before normalizing phrasing or file structure.
- Keep feature files business-facing. Put implementation detail, framework detail, and code reuse in step definitions and helper methods.
- Treat this skill as syntax and authoring guidance, not as a substitute for reading the local test harness.

## Core Authoring Rules

- Start each `.feature` file with a single `Feature:` block. Keep exactly one `Feature` per file.
- Use `Rule:` when a feature contains distinct business rules that deserve separate scenario groupings.
- Use `Scenario:` or `Example:` for a concrete behavior example. Treat them as synonyms.
- Prefer 3 to 5 steps per scenario when possible. Split oversized scenarios instead of narrating an entire workflow.
- Use `Given` for initial context or preconditions.
- Use `When` for the event or action.
- Use `Then` for an observable outcome.
- Use `And` and `But` to improve readability when repeating the same step type.
- Use `*` only when a list-style rhythm is clearer than repeated conjunctions.
- Use free-form descriptions under `Feature`, `Rule`, `Background`, `Scenario`, or `Scenario Outline` only when they clarify business intent.
- Use `Scenario Outline` with one or more `Examples` tables when the same behavior repeats with varying values.
- Use `Background` only for incidental shared context that truly applies to every scenario in the containing `Feature` or `Rule`.
- Use `Doc Strings` or `Data Tables` instead of packing large structured payloads into step text.
- Use tags intentionally for grouping, filtering, or metadata. Mirror the repo’s existing tag strategy if one exists.

## Language And Tone

- Write scenarios in domain language that a product owner, analyst, tester, or user can follow.
- Hide implementation details in step definitions, not in feature files.
- Prefer observable outcomes over internal implementation checks.
- Prefer stable domain vocabulary over selector names, route names, endpoint names, or database names unless the team explicitly treats those as user-facing concepts.
- Prefer behavior phrased independently of a specific interface unless the interface itself is the behavior under test.

## Do Not

- Do not assume this skill is more current than the official Cucumber documentation.
- Do not guess on syntax, keyword aliases, localization details, or tag placement when the official docs can answer it.
- Do not put more than one `Feature` in a `.feature` file.
- Do not add a colon after keywords that should not have one. Incorrect colons can cause tests to be ignored.
- Do not use block comments. Gherkin supports line comments only.
- Do not write a `Given` step for the user action under test.
- Do not write a `Then` step that checks hidden internal state such as raw database rows unless that state is itself the observable outcome for an external system.
- Do not duplicate step text across `Given`, `When`, `Then`, `And`, or `But`. Cucumber matches step definitions without considering the keyword.
- Do not bundle several distinct behaviors into one conjunction-heavy step when `And` or `But` should split the meaning.
- Do not leak selectors, clicks, DOM details, HTTP plumbing, or other implementation mechanics into Gherkin unless the product language genuinely depends on them.
- Do not overuse `Background`, especially for long or complicated setup.
- Do not write step definitions for hypothetical scenarios that do not exist yet.
- Do not couple step-definition file names or organization to individual feature files.
- Do not create near-duplicate step definitions when a parameterized step or shared helper method would keep the language cleaner.
- Do not call one step from another step definition as a reuse strategy when ordinary helper methods in the implementation language would be clearer.
- Do not invent nonstandard syntax or unsupported keyword combinations.

## Review Checklist

- Confirm the file has exactly one `Feature`.
- Confirm each scenario expresses one business example clearly.
- Confirm step roles follow `Given` context, `When` action, `Then` observable outcome.
- Confirm no duplicate step text exists across different step keywords.
- Confirm `Background` is short, memorable, and truly shared, or remove it.
- Confirm `Scenario Outline` actually removes duplication and that each placeholder has a matching column.
- Confirm `Doc Strings` and `Data Tables` are a better fit than overlong steps.
- Confirm wording is domain-facing rather than implementation-facing.
- Confirm the result is compatible with the repo’s existing step-definition and tag strategy.
- Confirm any uncertain rule against the official Cucumber docs before presenting the result as final.

## References

- Read [references/gherkin-reference.md](references/gherkin-reference.md) for syntax, keyword behavior, multiline arguments, tags, and localization guidance.
- Read [references/cucumber-writing-and-anti-patterns.md](references/cucumber-writing-and-anti-patterns.md) for step organization, reuse guidance, anti-patterns, and refactoring heuristics.
- Use the official Cucumber docs as the canonical source:
  - [Gherkin](https://cucumber.io/docs/gherkin/)
  - [Reference](https://cucumber.io/docs/gherkin/reference/)
  - [Localisation](https://cucumber.io/docs/gherkin/languages/)
  - [Step organization](https://cucumber.io/docs/gherkin/step-organization/)
  - [Anti-patterns](https://cucumber.io/docs/guides/anti-patterns/)
  - [Cucumber reference](https://cucumber.io/docs/cucumber/api/)
