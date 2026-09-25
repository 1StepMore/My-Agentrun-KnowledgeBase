---
title: 'How I AI: Agent Loops & AI-Powered Bug Hunting'
keywords:
- agentic-loop
- tutorial
- mozilla
- security
- firefox
- claude-mythos
- security-automation
- bug-hunting
- verification-loop
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://www.lennysnewsletter.com/p/how-i-ai-how-to-write-ai-agent-loops
source_type: article
source_platform: blog
author: Lenny's Newsletter (Claire / Brian Grinstead)
publish_date: '2026-06-22'
fetch_date: '2026-06-23'
priority: 1
language: en
notes: 两集播客精华：(1) Loop 工程设计实战——PR-review agent、skills agent 代码级实现；(2) Mozilla 用 Claude Mythos 一个月修 423 个 Firefox 安全 Bug 的完整案例。
---
# How I AI: Agent Loops & AI-Powered Bug Hunting

## Part 1: How to Design AI Agent Loops (Claude Code / Codex)

**Host:** Claire

### Key Takeaways

> "A loop is just a prompt that fires itself... Heartbeats, crons, and webhooks have been around forever. What's new is pointing them at an AI agent instead of a batch job."

1. **Goals > Timers:** A goal loop runs until the outcome is validated. Fuzzy success criteria causes infinite token burn.
2. **Think of Loops as Employees:** Define the job clearly. "Every Friday at 10 a.m., review all merged PRs and identify skills our agents are missing."
3. **Subagents (The Power Move):** Your agent can spawn its own agents. The PR-review loop spins off dedicated subagents to babysit individual PRs.
4. **Cost Control:** Monitor both cost and output quality from day one.
5. **Start Simple:** The morning briefing in Claude Cowork (scheduled task that checks calendar/email and sends a Slack summary) is a fully functional loop with zero custom code.

> "The ceiling on loop-based automation is basically 'how well can you define the job?' not 'how complex is the engineering?'"

## Part 2: How Claude Mythos Found a 15-Year-Old Bug in Mozilla Firefox

**Guest:** Brian Grinstead, Distinguished Engineer, Mozilla
**Achievement:** 423 Firefox security fixes in one month

### Major Takeaways

- **The Harness > The Model:** Custom harness for scoring files, running goal loops, verifying bugs with subagents.
- **Relentless Persistence:** Agents try 14+ different approaches without fatigue. "Cognitive energy declines over time in a way that agents don't."
- **Two-Stage Verification:**
  1. Agent triggers an actual crash in the fuzzing build
  2. Verifier subagent confirms the bug report makes sense
  *Result: almost zero false positives reach humans.*
- **Human Oversight:** Agents fix the exact vulnerability. Human engineers generalize the fix to similar patterns elsewhere.
- **Simple Prioritization:** An LLM judge scores each file on: likelihood of memory safety issue × ease of access from a webpage.
- **Build Harness in an Afternoon:** Use vendor SDKs (Claude Agent SDK, OpenAI Agent SDK). Avoid third-party frameworks.
- **Defend with Diversity:** Run multiple models/harnesses for security scanning.
