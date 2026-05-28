---
name: helloagents-launcher
description: Use when the user wants to start, run, launch, or use the local HelloAgents setup from Codex on this machine.
---

# HelloAgents Launcher

Launch the local HelloAgents environment that is already configured on this machine.

## When to Use

Use this skill when the user asks to:

- run HelloAgents
- launch HelloAgents
- use HelloAgents in Codex
- start the local HelloAgents demo

## What to Do

Run the local launcher script:

```powershell
C:\Users\Zemin\helloagents\run-helloagents.ps1
```

This starts the interactive HelloAgents demo in the terminal.

## Notes

- The HelloAgents project lives at `C:\Users\Zemin\helloagents`
- The virtual environment lives at `C:\Users\Zemin\.venvs\helloagents`
- The launcher script reads the saved user environment variables for `LLM_BASE_URL`, `LLM_MODEL_ID`, `LLM_API_KEY`, and `LLM_TIMEOUT`
- If the user has just changed environment variables and HelloAgents still uses old values, restart Codex first
