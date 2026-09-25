---
title: 'Loop Engineering: A Crash Course'
keywords:
- agentic-loop
- crash-course
- 15-concepts
- OpenCode
- claude-code
- heartbeat
- cloud-routines
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://agentfactory.panaversity.org/docs/loop-engineering-crash-course
source_type: article
source_platform: blog
author: The AI Agent Factory / Panaversity
publish_date: 2026-06
fetch_date: '2026-06-23'
priority: 2
language: en
notes: 15 概念速成课。含 Claude Code 和 OpenCode 双工具的 Loop 实现对比（Cloud Routines vs opencode serve）、Heartbeat 三种模式（限时/目标/定时）、Worktree 策略。
---
# Loop Engineering: A Crash Course

## The Core Mindset Shift

> "I don't prompt Claude anymore. I have loops running that prompt Claude… my job is to write loops." — Boris Cherny

**What the loop automates:** The middle steps.
**What a loop can never automate (the ends that stay yours):**
- **Intent** — saying precisely what you want
- **Accountability** — owning what ships

### Prompting vs Looping

| Prompting | Looping |
|---|---|
| You start each turn | A schedule/event starts each turn |
| You read output and decide next step | A checker checks output; the loop decides |
| Stops when you stop typing | Keeps running while you sleep |
| One task, one session, your full attention | Many small runs, unattended |

## The Loop's Anatomy (Six Parts)

1. **Heartbeat** — A schedule (or event) that starts the loop.
2. **Worktree** — Isolation, so two agents working at once do not overwrite each other's files.
3. **Skill** — Project knowledge written down once (`SKILL.md`).
4. **Sub-agents** — The Maker–Checker split.
5. **Connector (MCP)** — So the loop can *act* in real tools.
6. **State / Memory (The Spine)** — A file on disk (`progress.md`). **No spine, no loop.**

## Two Roads to the Same Loop

### Claude Code (Ships the Parts)
- `/loop` (in-session timer), `/goal` (run-until-done with built-in checker)
- **Cloud Routines** (scheduled tasks on Anthropic's servers — runs even with laptop closed)
- `--worktree`, Channels (event-driven input), `.claude/agents/`

### OpenCode (The Layer Below)
You bring the heartbeat. OpenCode is the worker:
- `opencode run "<prompt>"` — one beat, no chat screen
- `opencode serve --port 4096` + `--attach` (skip startup cost on every beat)
- Cron / `launchd` / Task Scheduler / **GitHub Actions** as the heartbeat
- `.opencode/agents/` for custom subagents

> **Learn the loop, not the keybind.** "If a technique works in both, it is a real skill, not a trick for one tool."

## Part 2: The Heartbeat (Making Something Run on Its Own)

### 1. In-Session Loops (Repeat While You Watch)
**Claude Code:** `/loop 5m check if the deployment finished`
**OpenCode:** `while true; do opencode run "check deploy" ; sleep 300; done`

### 2. Run-Until-Done (Loop Decides When to Stop)
**Claude Code:** `/goal All tests in test/auth pass and \`npm run lint\` is clean.` — separate small model checks.
**OpenCode:** `for i in $(seq 1 8); do opencode run "..."; if npm test && npm run lint; then break; fi; done`

> **Always give a loop a way to stop.** A **success condition** AND a **ceiling** (max tries, minutes, or spend).

### 3. Unattended Schedules (Runs While You Sleep)
**Claude Code Cloud Routines:** Bundles prompt, repo permissions, connectors, triggers. Runs on Anthropic servers.
**OpenCode:** Cron + `opencode run`. `opencode serve` + `--attach` to skip boot cost.
