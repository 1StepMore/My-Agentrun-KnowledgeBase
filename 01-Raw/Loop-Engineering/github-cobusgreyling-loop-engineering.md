---
title: Loop Engineering — cobusgreyling/loop-engineering
keywords:
- agentic-loop
- github
- tools
- patterns
- cli
- safety
- loop-tools
- pattern-catalog
- loop-audit
- loop-cost
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://github.com/cobusgreyling/loop-engineering
source_type: link
source_platform: github
author: Cobus Greyling
publish_date: 2026-06
fetch_date: '2026-06-23'
priority: 1
language: en
notes: Loop Engineering 的工具包仓库。含 loop-audit/loop-init/loop-cost 三个 CLI 工具、7 个生产级 Loop Pattern（Daily Triage/PR Babysitter/CI Sweeper 等）、安全检查清单和失效模式文档。MIT 协议。
---
# Loop Engineering — cobusgreyling/loop-engineering

## Core Philosophy

> "Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."

> "Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go." — Addy Osmani

## CLI Tools

Three npm packages published from the repo:

- **`@cobusgreyling/loop-audit`** v1.4+: Loop Readiness Score CLI (L1/L2/L3 levels)
- **`@cobusgreyling/loop-init`** v1.2: Scaffold starters + budget/run-log
- **`@cobusgreyling/loop-cost`**: Daily token spend estimator

**Quickstart:**
```bash
npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1
npx @cobusgreyling/loop-audit . --suggest
```

**Phased Rollout:** L1 Report → L2 Assisted Fixes → L3 Unattended

## Patterns (7 Production Patterns)

| Pattern | Cadence | Token Cost | Week 1 Goal |
|---|---|---|---|
| Daily Triage | 1d–2h | Low | L1 report |
| PR Babysitter | 5–15m | High | L1 watch |
| CI Sweeper | 5–15m | Very High | L2 cautious |
| Dependency Sweeper | 6h–1d | Medium | L2 patch-only |
| Changelog Drafter | 1d or tag | Low | L1 draft |
| Post-Merge Cleanup | 1d–6h | Low | L1 off-peak |
| Issue Triage | 2h–1d | Low | L1 propose-only |

## Safety & Operating

- Token costs can explode with sub-agents and long-running loops
- Verification is still on you. Unattended loops make unattended mistakes
- Comprehension debt grows faster unless you read what the loop ships
- Loop engineering amplifies judgment — both good and bad

**Operating Docs:** Failure Modes, Anti-Patterns, Multi-Loop Coordination
