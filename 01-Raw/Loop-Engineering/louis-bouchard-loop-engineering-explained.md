---
title: Loop Engineering Explained — Louis Bouchard
keywords:
- agentic-loop
- explainer
- video
- anatomy
- loop-anatomy
- token-budget
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://www.louisbouchard.ai/loop-engineering/
source_type: article
source_platform: blog
author: Louis Bouchard
publish_date: 2026-06
fetch_date: '2026-06-23'
priority: 2
language: en
notes: 视频+文章的 Loop Engineering 概念科普。重点讲清楚了 Loop vs Cron Job 的区别、两个核心要求（触发器+可验证目标）、以及 Loop 的五个组成部分。
---
# Loop Engineering Explained — Louis Bouchard

## The Problem: The Babysitting Trap

> "You are babysitting the exact process you wanted to offload and you're doing the dumb work, not the thinking."

**The Standard Cycle:** Write prompt → Agent edits → Accept permissions → Run tests → Something breaks → Ask to fix → Paste error → Repeat.

## The New Paradigm

> "You should not be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger

> "My job is to write loops." — Boris Cherny

## A Cron Job vs. A Loop

- **Cron Job:** Runs a fixed script on a schedule.
- **Loop Engineering:** Runs an **agent** that acts as a decision-maker inside the loop. It looks at the current state, chooses the next action, executes it, checks the result, and decides what to do next (Continue/Retry/Rollback/Stop).

**The Two Core Requirements:**
1. **The Trigger:** What starts the loop? (PR opening, CI failure, daily schedule, Slack message)
2. **The Verifiable Goal:** What tells the loop to stop? (all tests pass, CI is green, reviewer model approval)
   > "Otherwise you did not build a loop. You built a very confident token furnace."

## The Anatomy of a Loop (5 Parts + Memory)

1. **Automations:** The loop wakes up on its own (trigger) or you start it manually.
2. **Worktrees:** Allows parallel agents to work without overwriting each other.
3. **Skills:** Prevents the agent from guessing your project rules every time.
4. **Plugins/Connectors:** Allows the agent to use tools like GitHub, Linear, Slack, or a database.
5. **Sub-agents:** Separates the writer from the judge.
6. **+ Memory:** "The model forgets, but the repo does not."

## The Two Big Problems

**Problem 1: Defining the Goal is Hard**
- Goals must be precise and verifiable.
- Software development is **exploratory**. If the end state is fuzzy, the loop will optimize indefinitely.
- "The reward or just overall goal is where you need to put a lot of thought and consideration into, and experiment."

**Problem 2: Cost (The Token Furnace)**
- Loops can burn through millions of tokens quickly (especially unattended ones).
- **Every serious loop needs Hard Brakes:**
  - Maximum number of iterations
  - No-progress detection
  - Token or dollar budget per day
  - **Strong Verification:** Verification must be stronger than the agent claiming it is done.
