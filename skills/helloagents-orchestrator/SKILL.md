---
name: helloagents-orchestrator
description: Use when the user wants Codex to hand a task to the local HelloAgents orchestrator so it can dispatch work to Claude Code and persist task state on this machine.
---

# HelloAgents Orchestrator

Use the local HelloAgents orchestrator when the user wants Codex to route a task through the local collaboration layer instead of answering directly.

## Trigger Phrases

Examples:

- use helloagent to ask Claude Code
- hand this task to helloagent
- let helloagent orchestrate this with Claude Code
- route this through helloagent

## What to Run

```powershell
C:\Users\Zemin\helloagents-orchestrator\run-orchestrator-task.ps1 -Task "<user task>" -Cwd "<working directory>"
```

Use the current workspace path for `-Cwd` when the task is about files in the current project.

## Expected Output

The command returns JSON with:

- `task.task_id`
- `task.status`
- `task.result_text`
- persisted task and trace files under `C:\Users\Zemin\helloagents-orchestrator\storage`

## Notes

- This first-stage orchestrator currently supports the `claude` executor
- The orchestrator project lives at `C:\Users\Zemin\helloagents-orchestrator`
- If the user wants the raw persisted files, read from `storage\tasks` and `storage\traces`
