---
title: 'Loop Engineering: The Guide for AI Agents'
keywords:
- agentic-loop
- ralph-technique
- guide
- claude-code
- Codex
- goal-contract
- maker-checker
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/
source_type: article
source_platform: blog
author: Lush Binary
publish_date: '2026-06-09'
fetch_date: '2026-06-23'
priority: 1
language: en
notes: 深度技术指南。含 Ralph 技术（while 循环跑 coding agent）的完整解析、Claude Code vs Codex 的详细实现对照表、/goal 合同规范。
---
# Loop Engineering: The Guide for AI Agents

## Core Definition & Paradigm Shift

> "Loop engineering is building a system that prompts your agent on a schedule and against a goal, instead of typing each prompt yourself. The leverage moves from the quality of a single prompt to the design of the system that generates and verifies prompts."

**The Mental Model:**
- **Inner loop:** The agent's own perceive → reason → act → observe cycle (one turn).
- **Outer loop (Loop Engineering):** The system that spawns inner loops, feeds them work, verifies results, and persists state.

## The Origin: The Ralph Technique

Named by **Geoffrey Huntley** in early 2026. A `while` loop that runs the agent fresh each iteration.

```bash
while ! grep -q "ALL TASKS DONE" STATUS.md; do
  claude -p "Read PLAN.md and STATUS.md. Pick the next unchecked
             task, implement it, run the tests, commit on success,
             and update STATUS.md. Then stop." \
         --dangerously-skip-permissions
done
```

> "Loop engineering is Ralph, productized." The `while` loop becomes a scheduled automation. The context reset becomes a worktree and sub-agent. The "ALL TASKS DONE" check becomes a `/goal` condition.

## The Stop Condition (Write it Like a Contract)

> "A goal is only as good as the evidence that proves it."

| Contract field | Weak version | Verifiable version |
|---|---|---|
| End state | "Improve test coverage" | "Coverage for `src/billing` is at or above 90%" |
| Evidence | "It looks done" | "`npm test` exits 0 and the coverage report confirms" |
| Constraints | (unstated) | "Do not touch public APIs or delete existing tests" |
| Budget | (unbounded) | "Stop after 25 turns or $5, whichever comes first" |

**Three changes that make a loop trustworthy:**
- Preserve mistakes so the loop can learn from them
- Build verification into the loop rather than bolting it on after
- Treat the failing test as the signal that keeps the agent honest
