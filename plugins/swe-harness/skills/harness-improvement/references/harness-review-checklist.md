# Harness Review Checklist

Use this checklist for production-readiness reviews of coding-agent harnesses.
A production harness is the full system that lets an artificial intelligence
assistant act: instructions, tools, permissions, environment, memory, logs,
evaluation, human checkpoints, rollout, and rollback.

## Quick Scan

- Instructions: project rules are discoverable, current, scoped, and conflict
  resolution is explicit.
- Task intake: each work item has success criteria, out-of-scope boundaries, and
  risk flags before implementation starts.
- Tool contracts: tools describe allowed inputs, path behavior, output shape,
  failure modes, examples, and destructive-action limits.
- Permissions: high-risk reads, writes, network calls, deployments, and deletion
  commands are denied, gated, or require approval.
- Environment: dependency setup, seed data, emulators, containers, and external
  services can be recreated from a clean checkout.
- State isolation: tests and evaluations do not share hidden state between
  trials unless the shared state is intentional and documented.
- Observability: transcripts, tool calls, command outputs, errors, artifacts,
  timing, and cost-relevant usage are captured in a retrievable place.
- Evaluation: there is a replayable task set with deterministic checks where
  possible and model-based grading only where useful.
- Human handoff: risky actions pause with enough context for a human to decide.
- Rollout: changes ship behind a limited scope first, with a clear owner and
  rollback trigger.

## Maturity Levels

| Level | Description | Typical evidence |
|---|---|---|
| 0 | Manual | Chat history and ad hoc testing are the only record |
| 1 | Documented | Instructions and commands exist, but replay is fragile |
| 2 | Gated | Tests, permissions, and review steps block obvious failures |
| 3 | Replayable | Representative tasks run from clean state with recorded traces |
| 4 | Measured | Results, failures, cost, and latency are tracked over time |
| 5 | Self-improving | Production failures become eval cases and harness updates |

## Review Questions

Ask these in order:

1. What user outcome is the harness supposed to make safer, faster, or more
   reliable?
2. What can the agent do without asking a human?
3. What can the agent never do?
4. Where does the agent get project truth: files, tickets, documents, databases,
   traces, or humans?
5. What mistakes are currently invisible until a user reports them?
6. Which failures can be detected deterministically with tests or state checks?
7. Which failures require human review or model-based grading?
8. What is the smallest harness change likely to reduce the top failure?
9. How will the team know the change helped?
10. How will the team revert the change if it hurts?

## Source Notes

- Anthropic recommends simple, composable agent patterns and increasing
  complexity only when it measurably improves outcomes:
  https://www.anthropic.com/engineering/building-effective-agents
- Anthropic defines an evaluation harness as infrastructure that runs tasks,
  records steps, grades outputs, and aggregates results:
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- OpenAI recommends task-specific evaluations, logging, automation, human
  calibration, and continuous evaluation:
  https://platform.openai.com/docs/guides/evaluation-best-practices
