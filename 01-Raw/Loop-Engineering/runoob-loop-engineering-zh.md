---
title: Loop Engineering（循环工程）— 菜鸟教程
keywords:
- agentic-loop
- chinese
- tutorial
- full-guide
- 提示工程
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://www.runoob.com/ai-agent/loop-engineering.html
source_type: article
source_platform: blog
author: 菜鸟教程 (runoob.com)
publish_date: 2026-06
fetch_date: '2026-06-23'
priority: 1
language: zh
notes: Loop Engineering 的中文完整翻译版，含三层技术栈、六构件、五种 Loop 模式、完整代码示例。适合中文读者入门。
---
# Loop Engineering（循环工程）— 菜鸟教程

## 概述

Loop Engineering 是 2026 年 6 月在 AI 编程社区兴起的新概念。由 Google 工程师 **Addy Osmani** 系统整理，Anthropic Claude Code 负责人 **Boris Cherny** 和开发者 **Peter Steinberger**（OpenClaw 作者）分别提出了相同观点。

核心思想：从"提示 Agent 的人"转变为"设计提示 Agent 的循环系统的工程师"。

## AI 工程演进

```
Prompt → Context → Harness → Loop
```

| 阶段 | 核心思想 | 关注点 | AI 能力 | 人的角色 |
|------|----------|--------|---------|----------|
| Prompt Engineering | 设计提示词 | 怎么问 | 单轮生成 | 提问者 |
| Context Engineering | 组织背景信息 | 给什么信息 | 上下文理解 | 信息组织者 |
| Harness Engineering | 连接模型、工具、数据 | 如何调用能力 | 执行任务 | 系统设计者 |
| **Loop Engineering** | 目标驱动的自主闭环 | 持续完成目标 | 规划→执行→验证→持续运行 | 规则制定者 |

## 核心定义

> "设计、运营和持续改进反馈循环，使 AI 编程 Agent 能自主完成规划、执行代码修改、观察结果并在多轮迭代中完成任务。"

### 内循环 vs 外循环

| 层级 | 驱动 | 工作内容 |
|------|------|---------|
| 内循环（Agent 内置） | Agent | 读文件→修改→运行测试→读错误→再修改 |
| 外循环（你设计） | 你设计的系统 | 按计划发现任务→分派 Agent→验证→记录状态→开启下一轮 |

## 六构件

1. **自动触发器（Automations）** — 定义"什么时候？做什么？"。Claude Code `/loop`、`/goal`；Codex Automations tab
2. **并行隔离（Worktrees）** — Git Worktree 为每个 Agent 提供独立工作目录
3. **技能文件（Skills）** — `SKILL.md`，项目约定/构建步骤/禁止事项
4. **连接器（Connectors / MCP）** — 基于 MCP 协议，读 Issue、查数据库、调 API、发 Slack
5. **子 Agent（Sub-Agents）** — "制作者-检查者"模式，用不同指令和模型
6. **持久记忆（Memory）** — 状态写在文件里，文件放在仓库中

## 五种常见 Loop 模式

| 模式 | 核心观察信号 | 停止条件 | 典型场景 |
|------|-------------|----------|----------|
| 测试驱动 Loop | 测试通过/失败 | 目标测试全部通过 | Bug 修复、回归测试 |
| 编译器驱动 Loop | 类型/编译错误 | 类型检查零错误 | TypeScript 迁移 |
| Review 驱动 Loop | Reviewer 评论 | 全部通过或超时 | PR 自动化 |
| 安全审计 Loop | CVE/告警 | 队列清空或到时间 | 漏洞扫描 |
| CI 复盘 Loop | CI 状态 | 所有 Failing 被分类 | 每日 CI 检查 |
