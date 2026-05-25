# Failure Taxonomy

Use this taxonomy to avoid treating every failure as a prompt problem. Most
production harness failures come from unclear boundaries, weak tools, drifting
environments, or missing evaluation.

## Symptom To Layer Map

| Symptom | Likely layer | Better first fix |
|---|---|---|
| Agent ignores project process | Instructions | Shorten, reorder, or add conflict rules |
| Agent asks the same setup question repeatedly | Context loading | Add session-start context or a current-state file |
| Agent edits the wrong file | Tool contract | Require absolute paths or ownership boundaries |
| Agent runs unsafe commands | Permissions | Deny or ask on destructive commands |
| Agent passes tests locally but fails elsewhere | Environment | Pin dependencies and document clean setup |
| Agent output looks right but state is wrong | Evaluation | Grade final state, not just final text |
| Agent succeeds once and fails on replay | State isolation | Reset environment per trial |
| Agent over-engineers simple tasks | Task intake | Add scope, cost, and simplicity gates |
| Agent leaks secrets into logs | Data safety | Deny reads, redact traces, block outputs |
| Agent cannot recover from tool errors | Tool design | Return structured, actionable failure messages |
| Review catches same issue every time | Harness policy | Add a hook, checklist, or deterministic check |

## Failure Layers

1. Instruction layer: missing, stale, conflicting, or too verbose.
2. Context layer: the agent sees too much, too little, or low-priority context.
3. Tool layer: tool inputs are ambiguous, hard to produce, unsafe, or brittle.
4. Permission layer: risky actions are too easy or useful actions are blocked.
5. Environment layer: setup, dependency, seed data, or external service drift.
6. Observability layer: no transcript, trace, artifact, or failure category.
7. Evaluation layer: no replay suite, wrong graders, or brittle path grading.
8. Operator layer: humans do not know when to approve, stop, or roll back.

## Triage Heuristic

Prefer fixes in this order unless evidence points elsewhere:

1. Clarify the task and success criteria.
2. Narrow or improve context loading.
3. Make the tool easier and safer to use.
4. Add permission gates for high-risk actions.
5. Stabilize the environment and starting state.
6. Add deterministic checks.
7. Add model-based or human grading.
8. Add more autonomous orchestration only after simpler controls fail.

## Source Notes

- Anthropic's agent guidance emphasizes simple designs, transparent planning,
  and careful agent-computer interfaces:
  https://www.anthropic.com/engineering/building-effective-agents
- OpenAI's agent safety guidance recommends preventing untrusted data from
  directly driving agent behavior:
  https://platform.openai.com/docs/guides/agent-builder-safety
