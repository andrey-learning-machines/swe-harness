# Evaluation Design For Agents

Use this reference when creating replay suites for coding agents and other
multi-step artificial intelligence workflows.

## Core Terms

- Task: one problem with input, starting state, and success criteria.
- Trial: one attempt at a task. Run multiple trials when model variation matters.
- Grader: logic that scores the result. Prefer deterministic tests when possible.
- Transcript: the full record of messages, tool calls, errors, and artifacts.
- Outcome: the final state that matters to the user.
- Evaluation suite: a collection of tasks that measure a capability or risk.
- Evaluation harness: the infrastructure that runs tasks, records traces, grades
  outcomes, and aggregates results.

## Design Process

1. Define the objective in product terms.
2. Collect representative tasks from production failures, support requests,
   historical tasks, synthetic edge cases, and domain expert examples.
3. Specify the clean starting state for each task.
4. Choose graders:
   - deterministic tests for code behavior,
   - state checks for database or file outcomes,
   - tool-use checks for required or forbidden operations,
   - transcript checks for policy violations,
   - model-based judging only when deterministic checks miss the real quality.
5. Run baseline trials before changing the harness.
6. Compare candidate changes against the same task set.
7. Inspect transcripts before trusting aggregate scores.
8. Promote production failures into new regression tasks.

## Good Agent Evaluation Traits

- Mirrors real task distribution and includes edge cases.
- Starts each trial from isolated, clean state.
- Grades the outcome more than the exact path.
- Records enough trace detail to debug failures.
- Separates capability failures from harness failures.
- Tracks cost, latency, and tool-call volume.
- Has ownership and maintenance expectations.

## Common Anti-Patterns

- Vibe checks instead of explicit criteria.
- Generic scores unrelated to the product task.
- Only grading final prose.
- Punishing a valid alternate path because it used different tools.
- Letting shared state leak between trials.
- Building many hand-graded examples but no automated suite.
- Trusting model-based graders without human calibration.

## Source Notes

- Anthropic recommends clean, isolated evaluation environments and thoughtful
  graders that focus on outcomes rather than brittle paths:
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic's test guidance recommends task-specific cases, automation where
  possible, and broad coverage:
  https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests
- OpenAI recommends defining objectives, collecting datasets, defining metrics,
  comparing runs, and continuously evaluating:
  https://platform.openai.com/docs/guides/evaluation-best-practices
