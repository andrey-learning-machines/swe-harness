# Tool Contract Patterns

Use this reference when designing or reviewing the tools and commands a coding
agent can call. A tool contract is the agreement between the agent and the
environment: inputs, outputs, boundaries, side effects, and failure behavior.

## Strong Defaults

- Prefer absolute paths for file operations when the harness supports them.
- Require an explicit working directory for shell commands.
- Make destructive actions opt-in with a separate command or approval gate.
- Return structured output when the next step needs to parse it.
- Keep human-facing logs concise, but preserve full machine-readable artifacts.
- Include preconditions in tool descriptions: required files, running services,
  authentication, and expected branch state.
- Include postconditions: files changed, artifacts created, services started, or
  state mutated.
- Make idempotent operations easy. Re-running setup should not corrupt state.
- Make rollback obvious. If a tool mutates state, document how to undo it.

## Tool Design Checklist

- Purpose is one sentence and not overloaded.
- Inputs have names that reveal units and expected format.
- Path handling is unambiguous.
- The tool reports missing prerequisites before doing partial work.
- The tool fails closed for permissions, secrets, and destructive actions.
- Output separates summary, warnings, errors, and artifact paths.
- Examples include one common case and one edge case.
- Large outputs are summarized with a pointer to the full artifact.
- The contract says whether network access is used.
- The contract says whether it reads or writes user data.

## Dangerous Surfaces

Gate or deny these by default:

- Credential reads and environment files.
- Data deletion, destructive migrations, and force pushes.
- Production deploys and infrastructure changes.
- Payment, authentication, authorization, legal, and personal-data flows.
- External network calls that can exfiltrate data.
- Tools that execute generated code outside a sandbox.

## Validation Ideas

- Unit test the tool parser or wrapper.
- Run a dry-run mode before real mutation.
- Capture before and after state for mutable tools.
- Add a hook that blocks known-dangerous command patterns.
- Add a small adversarial prompt set for tools exposed to untrusted data.

## Source Notes

- Anthropic's tool guidance recommends designing agent-computer interfaces with
  the same care as human-computer interfaces:
  https://www.anthropic.com/engineering/building-effective-agents
- OpenAI's Agents software development kit documents guardrails around input,
  output, and tool invocation:
  https://openai.github.io/openai-agents-python/guardrails/
