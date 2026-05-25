# Cucumber Writing And Anti-Patterns

Use this file when the task involves reviewing, refactoring, or scaling a Cucumber codebase rather than only writing one feature file.

## Table Of Contents

- [Organize Step Definitions By Domain Concept](#organize-step-definitions-by-domain-concept)
- [Prefer Reuse Without Overfitting](#prefer-reuse-without-overfitting)
- [Recognize Common Anti-Patterns](#recognize-common-anti-patterns)
- [Review Heuristics](#review-heuristics)
- [Do Not](#do-not)
- [Practical Refactor Moves](#practical-refactor-moves)

Treat these official pages as the canonical references:

- https://cucumber.io/docs/gherkin/step-organization/
- https://cucumber.io/docs/guides/anti-patterns/
- https://cucumber.io/docs/cucumber/api/

## Organize Step Definitions By Domain Concept

- Start simple when a project is small, but split step definitions into meaningful groups as the project grows.
- Group step definitions by domain concept or major business object rather than by feature file.
- Use domain-oriented file names rather than scenario-oriented file names.
- Inspect the existing repo structure before adding new step-definition files.
- Keep feature files readable to non-programmers; keep code organization concerns in the implementation layer.

## Prefer Reuse Without Overfitting

- Implement only the step definitions that are actually used by current scenarios.
- Prefer parameterized steps over near-duplicate step definitions.
- Prefer helper methods in the implementation language for shared low-level behavior.
- Prefer higher-level domain steps over repetitive implementation-detail steps.
- Use `Data Tables` when many example inputs would otherwise create repetitive step text.

## Recognize Common Anti-Patterns

### Feature-Coupled Step Definitions

Smell:

- Step-definition files are named after individual feature files.
- Similar domain behavior is reimplemented across multiple step files.
- Changing one business concept requires edits across many feature-specific files.

Refactor:

- Rename and regroup step-definition files by domain concept.
- Consolidate duplicate behavior behind reusable helpers.
- Keep steps reusable across multiple scenarios and features.

### Conjunction Steps

Smell:

- A single step contains multiple actions or conditions joined together.
- The step is too specialized to reuse naturally.

Refactor:

- Split the step into atomic steps with `And` or `But`.
- Raise the abstraction level if the combined behavior is truly one domain concept.

### Unused Or Premature Step Definitions

Smell:

- The codebase contains step definitions that do not map to any scenario.
- Engineers create step definitions in anticipation of future scenarios.

Refactor:

- Remove unused steps.
- Add new step definitions only when a scenario needs them.

### Near-Duplicate Step Definitions

Smell:

- Several steps differ only by one noun, page, amount, or role.
- Multiple definitions perform the same underlying action with tiny wording differences.

Refactor:

- Use parameters.
- Extract shared helper methods.
- Normalize the domain vocabulary so the scenario language stays consistent.

### Hidden Setup In Hooks

Smell:

- Business-relevant setup happens in `Before` hooks where non-technical readers cannot see it.

Refactor:

- Prefer `Background` when the setup should be visible in the executable specification.
- Keep hooks for low-level concerns such as browser lifecycle, environment cleanup, or similar plumbing.

## Review Heuristics

- Ask whether a reader can understand the scenario without knowing the test framework.
- Ask whether the `Then` step asserts an outcome a user or external system could observe.
- Ask whether the scenario reads as business behavior instead of automation choreography.
- Ask whether repeated scenarios should become a `Scenario Outline`.
- Ask whether repeated setup should become a short `Background` or a higher-level `Given`.
- Ask whether the current wording will remain stable if the interface implementation changes.

## Do Not

- Do not organize step definitions by feature file when the codebase is large enough to need reuse.
- Do not write one giant step-definition file forever if the project has already outgrown it.
- Do not prewrite steps that no scenario uses.
- Do not create a new step definition for every minor wording variation.
- Do not call one step from another step definition as the primary reuse mechanism.
- Do not hide business setup in hooks if non-technical readers need to understand it.
- Do not let feature files drift into selector-level or script-level narration.

## Practical Refactor Moves

- Replace repeated literal values with `Scenario Outline` placeholders.
- Replace repeated low-level setup with a higher-level domain `Given`.
- Split conjunction-heavy steps into atomic steps.
- Rename step-definition files from feature names to domain names.
- Extract helper methods from duplicated step-definition bodies.
- Re-check the resulting Gherkin against the official docs if any syntax changed during refactoring.
