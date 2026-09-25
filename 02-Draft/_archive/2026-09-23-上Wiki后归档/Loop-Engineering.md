---
title: Loop-Engineering
keywords:
- agentic-loop
- AI-Agent
- automation
- ai-coding
state:
  phase: draft-archived
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
sources:
- Loop-Engineering/addy-osmani-loop-engineering.md
- Loop-Engineering/agent-factory-crash-course.md
- Loop-Engineering/github-cobusgreyling-loop-engineering.md
- Loop-Engineering/lennys-newsletter-agent-loops.md
- Loop-Engineering/louis-bouchard-loop-engineering-explained.md
- Loop-Engineering/lushbinary-loop-engineering-guide.md
- Loop-Engineering/mindstudio-what-is-loop-engineering.md
- Loop-Engineering/oreilly-loop-engineering.md
- Loop-Engineering/runoob-loop-engineering-zh.md
promoted_to: '[[Loop-Engineering]]'
---
# Loop Engineering（循环工程）

> 2026 年 6 月爆发的新范式。从"手动提示 Agent"转变为"设计让 Agent 自我驱动的闭环系统"。


## 核心定义

**Loop Engineering 是设计、运营和持续改进反馈循环，使 AI 编程 Agent 能自主完成规划、执行代码修改、观察结果并在多轮迭代中完成任务。**

### 三层技术栈

| 层次 | 优化对象 | 工作单位 |
|------|----------|---------|
| Prompt Engineering | 指令措辞 | 一次手动对话 |
| Context Engineering | 上下文窗口内容 | 回答的环境条件 |
| **Loop Engineering** | **提示什么、何时提示、结果是否可接受** | **跨越多个内循环的自动工作流** |

### 关键人物

| 人物 | 身份 | 核心观点 |
|------|------|---------|
| **Boris Cherny** | Claude Code 负责人 | "我不再手动提示 Claude 了。我跑着几个 Loop，它们自己在提示 Claude。我的工作是写 Loop。" |
| **Peter Steinberger** | OpenClaw 作者 | "你不该再手动提示编程 Agent 了。你应该设计 Loop 来提示你的 Agent。" |
| **Addy Osmani** | Google 工程师 | 系统整理出 Loop Engineering 的完整框架（六构件 + State） |
| **Geoffrey Huntley** | Ralph 技术首创者 | 用 `while` 循环 + 文件状态跑 coding Agent 的原型验证 |


## 核心架构

### 内循环 vs 外循环

```
外循环（你设计）
  └─ 按计划发现任务 → 分派 Agent → 验证 → 记录状态 → 下一轮
       └─ 内循环（Agent 内置）
            └─ 读文件 → 修改 → 运行测试 → 读错误 → 再修改
```

### 六构件 + 状态（The Six Primitives + State）

| 构件 | 作用 | Claude Code | Codex |
|------|------|-------------|-------|
| **Automations** | 定时/条件触发发现和分派 | `/loop`, cron, `/goal` | Automations tab, `/goal` |
| **Worktrees** | 并行隔离防冲突 | `--worktree`, `isolation: worktree` | 内置 per thread |
| **Skills** | 项目知识固化免重复解释 | `SKILL.md` | `SKILL.md` |
| **Connectors/MCP** | 连接外部工具 | MCP Servers | MCP Connectors |
| **Sub-agents** | 制造者-检查者分离 | `.claude/agents/` | `.codex/agents/` |
| **State** | 跨对话持久状态 | AGENTS.md / Linear | Markdown / Linear |

**关键洞察：** "Both products have all six now. The names differ, but the capability is the same. Design a loop that works no matter which tool you are sitting in." — Addy Osmani


## /goal 原语

运行到条件满足为止，用**另一个小模型**判定完成（避免写代码的给自己的作业打分）。

| 合同字段 | 弱版本 | 可验证版本 |
|----------|--------|-----------|
| 结束状态 | "提升测试覆盖率" | "src/billing 覆盖率 ≥ 90%" |
| 证据 | "看起来好了" | "npm test exit 0 + 覆盖率报告" |
| 约束 | (未说明) | "不碰 public API，不删现有测试" |
| 预算 | (无上限) | "25 步或 $5，先到先停" |

> "A goal is only as good as the evidence that proves it."


## 五种 Loop 模式

| 模式 | 停止条件 | 典型场景 |
|------|----------|----------|
| 测试驱动 Loop | 目标测试全部通过 | Bug 修复、回归测试 |
| 编译器驱动 Loop | 类型检查零错误 | TypeScript 迁移、重构 |
| Review 驱动 Loop | 全部通过或超时 | PR 自动化跟进 |
| 安全审计 Loop | 队列清空或到时间 | CVE 扫描、漏洞发现 |
| CI 复盘 Loop | 所有 Failing 被分类 | 每日 CI 检查 |


## Ralph 技术（原型验证）

Geoffrey Huntley 最早的原型——`while` 循环跑 coding agent，每次全新上下文，状态写磁盘：

```bash
while ! grep -q "ALL TASKS DONE" STATUS.md; do
  claude -p "Read PLAN.md and STATUS.md. Pick next task,
             implement it, run tests, commit on success,
             and update STATUS.md. Then stop."
done
```

**核心洞察：** 上下文重置防止 session 退化 + 状态在磁盘不在模型记忆里。Loop Engineering 就是"Ralph 产品化"——`while` 循环变成 Automation，上下文重置变成 Worktree/Sub-agent，完成检查变成 `/goal`。


## 实战案例：Mozilla 一个月修 423 个 Firefox 安全 Bug

**来源：** Lenny's Newsletter（Brian Grinstead, Mozilla Distinguished Engineer）

关键经验：
1. **Harness > Model** — 真正的解锁不是模型本身，而是评分文件、跑 goal loop、子 Agent 验证的脚手架
2. **Agent 不知疲倦** — 一个 Bug 试了 14 种不同方法才触发崩溃，人类早放弃了
3. **两级验证消除误报** — Agent 触发实际崩溃 → 验证子 Agent 确认报告合理 → 达到零误报
4. **人类泛化修复** — Agent 只修精确漏洞点，人类工程师把修复扩展到代码库其他类似位置
5. **简单优先级评分** — 一个 LLM Judge 按两个维度打分：内存安全问题可能性 × 网页端可访问性

> "Cognitive energy declines over time in a way that agents don't."


## Claude Code vs OpenCode 实现对比

| 能力 | Claude Code | OpenCode |
|------|-------------|----------|
| 限时循环 | `/loop 5m check deploy` | `while true; do opencode run "..."; sleep 300; done` |
| 目标驱动 | `/goal "all tests pass"`（内置小模型判断） | `for i in 1..8; do opencode run "..."; if npm test; then break; fi; done` |
| 无人值守 | Cloud Routines（Anthropic 云端） | cron + `opencode run` |
| 启动优化 | 内置 | `opencode serve --port 4096` + `--attach` |

> **Learn the loop, not the keybind.** "If a technique works in both, it is a real skill, not a trick for one tool."


## 实用工具：7 个生产 Pattern

| Pattern | 节奏 | Token 成本 | 第一周目标 |
|---------|------|-----------|-----------|
| Daily Triage | 每天 | 低 | L1 报告 |
| PR Babysitter | 5-15min | 高 | L1 观察 |
| CI Sweeper | 5-15min | 很高 | L2 谨慎 |
| Dependency Sweeper | 6h-1d | 中 | L2 仅补丁 |
| Changelog Drafter | 每天 | 低 | L1 草稿 |
| Post-Merge Cleanup | 每天 | 低 | L1 非高峰 |
| Issue Triage | 2h-1d | 低 | L1 仅提议 |

**CLI 工具：** `@cobusgreyling/loop-init`（脚手架）、`loop-audit`（就绪度评分）、`loop-cost`（费用预估）


## 三大警告

1. **验证责任在你** — 无人值守的 Loop = 无人值守的错误生成器。Maker/Checker 分离有帮助，但"完成了"是声称不是证据
2. **理解债** — Loop 越快产出你没写过的代码，代码库和你的理解差距越大
3. **认知投降** — 最危险的状态："Agent 给什么就收什么"。设计 Loop 可以放大判断力，也可以放大懒惰

> "Two people can build the exact same loop and get completely opposite results. One uses it to move faster on work they understand; the other uses it to avoid understanding the work." — Addy Osmani


## 来源

原始素材：`01-Raw/Loop-Engineering/`

| # | 文件 | 来源 |
|---|------|------|
| 1 | `addy-osmani-loop-engineering.md` | Addy Osmani |
| 2 | `runoob-loop-engineering-zh.md` | 菜鸟教程 |
| 3 | `lennys-newsletter-agent-loops.md` | Lenny's Newsletter |
| 4 | `lushbinary-loop-engineering-guide.md` | Lush Binary |
| 5 | `oreilly-loop-engineering.md` | O'Reilly Radar |
| 6 | `github-cobusgreyling-loop-engineering.md` | GitHub |
| 7 | `agent-factory-crash-course.md` | AI Agent Factory |
| 8 | `louis-bouchard-loop-engineering-explained.md` | Louis Bouchard |
| 9 | `mindstudio-what-is-loop-engineering.md` | MindStudio |
