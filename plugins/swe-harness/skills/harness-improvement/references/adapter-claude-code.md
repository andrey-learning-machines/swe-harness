# Adapter: Claude Code

Use this reference only when the target harness is Claude Code. Keep generic
recommendations in the main skill and map them to Claude-specific files here.

## Surface Map

| Generic harness concept | Claude Code surface |
|---|---|
| Project instructions | `CLAUDE.md`, imported memory files |
| User instructions | user memory and settings |
| Tool permissions | `.claude/settings.json`, `.claude/settings.local.json`, managed settings |
| Sensitive file denial | `permissions.deny` in settings |
| Lifecycle checks | hooks such as `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, and `SubagentStop` |
| Specialist delegation | project or user subagents in `.claude/agents/` or `~/.claude/agents/` |
| Reusable workflows | skills, slash commands, and project commands |
| Tool integrations | Model Context Protocol servers, often abbreviated as MCP servers |
| Observability | transcript files, hook logs, command artifacts, evaluation reports |

## Practical Improvements

- Put durable project rules in `CLAUDE.md`; put personal preferences in user
  settings or user memory.
- Add `.claude/settings.json` when the team needs shared allow, ask, or deny
  behavior.
- Deny reads of `.env`, `.env.*`, secrets folders, service account files, and
  generated build output unless there is a specific reason.
- Use `SessionStart` hooks to load current issue, branch, or active-work context.
- Use `PreToolUse` hooks to block dangerous commands or require approval.
- Use `PostToolUse` hooks for format checks, type checks, or artifact capture.
- Use `Stop` hooks to prevent completion until required gates pass.
- Use `SubagentStop` hooks when delegated work must report evidence before the
  main agent accepts it.
- Use project subagents for repeatable specialist work, and keep their tool
  permissions narrower than the main agent where practical.

## Claude-Specific Review Questions

1. Does `CLAUDE.md` say which files are authoritative and how conflicts resolve?
2. Are project settings checked in for team-wide safety, with local settings kept
   out of source control?
3. Are dangerous files denied explicitly?
4. Do hooks enforce checks that humans currently repeat by hand?
5. Are subagents scoped by expertise and permissions instead of being generic
   clones of the main agent?
6. Are transcripts and hook outputs retained long enough to debug regressions?
7. Can a task be replayed from a fresh checkout with the same settings?

## Source Notes

- Claude Code settings document project and user settings, permissions, sensitive
  file denial, and subagent locations:
  https://docs.anthropic.com/en/docs/claude-code/settings
- Claude Code hooks document lifecycle events and decision control:
  https://docs.anthropic.com/en/docs/claude-code/hooks
- Claude Code subagents document project and user subagent scopes:
  https://docs.anthropic.com/en/docs/claude-code/sub-agents
