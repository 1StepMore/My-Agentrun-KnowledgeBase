---
title: Loop Engineering by Addy Osmani
keywords:
- agentic-loop
- addy-osmani
- framework
- six-primitives
- prompt-engineering
- context-engineering
- harness-engineering
- agent-automation
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://addyosmani.com/blog/loop-engineering/
source_type: article
source_platform: blog
author: Addy Osmani
publish_date: '2026-06-14'
fetch_date: '2026-06-23'
priority: 1
language: en
notes: Loop Engineering 框架创始文章。系统定义六构件+State架构，是这一领域的地基文献。
---
# Loop Engineering by Addy Osmani

## Core Thesis & Key Quotes

> "Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — **Peter Steinberger**

> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops." — **Boris Cherny**

A loop is a recursive goal where you define a purpose and the AI iterates until complete. It sits one floor above the agent harness (environment a single agent runs in).

## The Six Primitives of a Loop

A loop requires five components and a memory store:

| Primitive | Job in the Loop | Codex App | Claude Code |
| :--- | :--- | :--- | :--- |
| **Automations** | Discovery + scheduled triage | Automations tab; `/goal` (run-until-done) | Scheduled tasks, cron, `/loop`, `/goal`, hooks |
| **Worktrees** | Isolate parallel features | Built-in worktree per thread | `git worktree`, `--worktree`, `isolation: worktree` |
| **Skills** | Codify project knowledge | `SKILL.md`, invoked via `$name` | `SKILL.md` |
| **Plugins / Connectors** | Connect agent to real tools | Connectors (MCP) + Plugins | MCP servers + Plugins |
| **Sub-agents** | Split "maker" from "checker" | `.codex/agents/` TOML | `.claude/agents/`, agent teams |
| **State / Memory** | Track done/next steps (survives resets) | Markdown or Linear via connector | `AGENTS.md` or Linear via MCP |

### Detailed Breakdown

**Automations:** The heartbeat. Keeps running unattended. Codex uses an Automations tab (findings go to Triage inbox; empty runs archive themselves). Claude Code uses `/loop` for intervals and `/goal` for running until a condition is met. Critical detail: `/goal` uses a *separate small model* to check the stop condition, not the agent that did the work.

**Worktrees:** Essential for parallelism. Agents cannot touch the same file. The limiting factor becomes your *review bandwidth*, not the tool.

**Skills:** The cure for "Intent Debt". Without them, the loop re-derives the project from scratch every cycle. A `SKILL.md` is the authoring format.

**Plugins / Connectors:** Built on MCP. This is the difference between an agent that suggests a fix and a loop that opens the PR, links the ticket, and pings Slack automatically.

**Sub-agents:** "The model that wrote the code is way too nice grading its own homework." A second agent (often a stronger model) acts as the verifier. The same "maker/checker" split is used internally by `/goal` for the stop condition.

**State:** "The model forgets everything between runs so the memory has to be on disk and not in the context. The agent forgets, the repo doesn't."

## Example Loop Workflow

> "An automation runs every morning... calls a triage skill that reads yesterday's CI failures... writes findings into a markdown file. For each finding worth doing, it opens an isolated worktree, sends a sub-agent to draft the fix, and a second sub-agent reviews the draft. Connectors open the PR and update the ticket."

**Result:** You designed the system once. You prompted none of the individual steps.

## Critical Warnings & Limitations

1. **Verification is still on you.** An unattended loop is an unattended mistake generator.
2. **Comprehension Debt.** The faster the loop ships code you didn't write, the bigger the gap between the codebase and your understanding.
3. **Cognitive Surrender.** The most dangerous state: "just taking whatever it gives back."
4. **Token Costs.** You must be "token rich" or very careful.

## Conclusion

> "Two people can build the exact same loop and get completely opposite results. One uses it to move faster on work they understand; the other uses it to avoid understanding the work."
