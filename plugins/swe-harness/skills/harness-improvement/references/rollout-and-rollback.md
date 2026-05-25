# Rollout And Rollback

Use this reference when planning how harness changes reach real users.

## Rollout Ladder

1. Local dry run: one task, clean checkout, no production state.
2. Local replay suite: representative tasks with recorded outputs.
3. Internal pilot: trusted operator, low-risk repository or task class.
4. Limited production scope: narrow command, branch, team, or feature area.
5. Broader rollout: default behavior after passing stop-condition monitoring.

## Required For Each Harness Change

- Owner.
- Intended improvement.
- Affected users, repositories, and tools.
- Known risks.
- Validation evidence.
- Stop conditions.
- Rollback action.
- Monitoring window.
- Follow-up date.

## Stop Conditions

Stop or roll back when any of these appear:

- Increase in failed or abandoned agent runs.
- New unsafe tool attempts.
- More human interventions for the same task class.
- Higher cost or latency without matching quality gain.
- Regression in critical evaluation tasks.
- Secret, personal data, or protected file exposure.
- Repeated user confusion caused by new instructions or workflow.

## Rollback Patterns

- Revert instruction or hook changes from source control.
- Disable a project-level configuration while keeping user-level defaults.
- Turn a new tool permission from allow to ask or deny.
- Fall back from autonomous execution to plan-only mode.
- Remove a task class from automatic delegation.
- Restore the previous evaluation threshold if a new grader is noisy.

## Source Notes

- OpenAI's agent guide emphasizes layered guardrails for privacy, brand, and
  safety risks:
  https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- OpenAI evaluation guidance treats evaluation as a continuous process rather
  than a one-time launch gate:
  https://platform.openai.com/docs/guides/evaluation-best-practices
