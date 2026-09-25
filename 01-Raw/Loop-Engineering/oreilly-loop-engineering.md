---
title: Loop Engineering — O'Reilly Radar
keywords:
- agentic-loop
- oreilly
- industry-analysis
- six-primitives
- agent-harness
- automation
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://www.oreilly.com/radar/loop-engineering/
source_type: article
source_platform: blog
author: Addy Osmani (O'Reilly Radar)
publish_date: '2026-06-22'
fetch_date: '2026-06-23'
priority: 1
language: en
notes: O'Reilly Radar 权威版本。与 Addy Osmani 个人博客内容互补，结构更精炼，多了行业视角。
---
# Loop Engineering — O'Reilly Radar

## Core Thesis

> "Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."

A loop is a recursive goal where you define a purpose and the AI iterates until complete. This sits one floor above **Agent Harness Engineering** and the **Factory Model**. The harness runs on a timer, spawns helpers, and feeds itself.

## The Shift: Manual → Loop

| **Old Way** | **Loop Way** |
|---|---|
| You write a prompt → Agent returns → You write the next prompt | You build a system that finds work, hands it out, checks it, plans the next step |
| Human is the active loop | Human *designs* the loop, then steps aside |
| Prompt engineering is the skill | Loop design is the skill |

## The 6 Primitives

| Primitive | Job in the Loop | Codex App | Claude Code |
|---|---|---|---|
| **Automations** | Discovery + triage on a schedule | Automations tab, `/goal` | `/loop`, `cron`, hooks, `/goal` |
| **Worktrees** | Isolate parallel features | Built-in per thread | `git worktree`, `--worktree`, `isolation: worktree` |
| **Skills** | Codify project knowledge | `SKILL.md`, invoked with `$name` | `SKILL.md` |
| **Plugins/Connectors** | Connect to real tools | MCP Connectors + Plugins | MCP servers + Plugins |
| **Subagents** | Split maker & checker | `.codex/agents/` | `.claude/agents/`, agent teams |
| **State (Memory)** | Track what's done / next | Markdown or Linear via connector | `AGENTS.md`, progress files, Linear via MCP |

> "Both products have all five now. The names differ, but the capability is the same. Design a loop that works no matter which tool you are sitting in."

### Automations (The Heartbeat)

Scheduled discovery that surfaces work to *you* instead of you hunting for it.
- Codex: Results → Triage inbox. Empty runs archive themselves.
- Claude Code: `/loop` for interval, `/goal` for run-until-condition.
- `/goal` uses a separate small model to check the stop condition.

### Worktrees (Parallelism Without Chaos)

> "Two agents writing the same file is the exact same headache as two engineers committing to the same lines and nobody talked to each other first."

Wall: *Your review bandwidth* limits how many you can run, not the tool.

### Skills (Codified Project Knowledge)

The cure for **Intent Debt**—the cold-start problem where agents make confident guesses to fill gaps in your instructions. "A skill is that intent written down on the outside."

### Subagents (Maker/Checker Split)

"The model that wrote the code is way too nice grading its own homework." Common split: One explores → one implements → one verifies against spec.

### State/Memory (The Spine)

"The model forgets everything between runs so the memory has to be on disk and not in the context."
