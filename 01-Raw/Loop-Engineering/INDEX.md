---
title: Loop Engineering（循环工程）资源集合
keywords:
- loop-engineering
- agent-loop
- ai-agent
- harness-engineering
state:
  phase: raw
  time_raw: '2026-06-23T00:00:00'
compile: false          # 索引页/集合页，非可编译素材（走文档化的豁免通道，不参与 C1 流转）
source_url: ''
source_type: collection
source_platform: loop-engineering
author: ''
publish_date: ''
fetch_date: '2026-06-23'
status: processed
tags: [loop-engineering, collection, index]
notes: "Loop Engineering 专题资源集合——10 篇精选文章的原始素材。2026 年 6 月新范式：从「提示 Agent」到「设计让 Agent 自我驱动的闭环系统」。"
priority: 1
language: 'en, zh'
related_concepts: [loop-engineering, ai-agent, automation, agent-loop]
---


# Loop Engineering（循环工程）资源集合

## 一句话

Loop Engineering 是 2026 年 6 月爆发的新范式——不再手动提示 Agent，而是设计一个闭环系统让 Agent 自己持续运转。

## 资源清单

| # | 文件 | 来源 | 优先级 | 说明 |
|---|------|------|--------|------|
| 1 | `addy-osmani-loop-engineering.md` | Addy Osmani | ⭐ 必读 | 框架地基，系统定义六构件+State |
| 2 | `runoob-loop-engineering-zh.md` | 菜鸟教程 | ⭐ 必读 | 中文完整版，含三层栈和五种 Loop 模式 |
| 3 | `lennys-newsletter-agent-loops.md` | Lenny's Newsletter | ⭐ 必读 | 实战指南 + Mozilla 423 安全修复案例 |
| 4 | `lushbinary-loop-engineering-guide.md` | Lush Binary | ⭐ 必读 | Ralph 技术深度解析 + /goal 合同规范 |
| 5 | `oreilly-loop-engineering.md` | O'Reilly Radar | ✅ 推荐 | 权威行业分析，与 Addy 原文互补 |
| 6 | `github-cobusgreyling-loop-engineering.md` | GitHub | ✅ 推荐 | 7 个生产 Pattern + CLI 工具包 |
| 7 | `agent-factory-crash-course.md` | AI Agent Factory | ✅ 推荐 | Claude Code vs OpenCode 双工具对比 |
| 8 | `louis-bouchard-loop-engineering-explained.md` | Louis Bouchard | 📖 参考 | 概念科普，Loop vs Cron 区别讲得清楚 |
| 9 | `mindstudio-what-is-loop-engineering.md` | MindStudio | 📖 参考 | ReAct 模式切入，五种 Loop 模式目录 |
| 10 | `substack-loop-engineering-complete-guide.md` | Substack | ⚠️ 部分 | 付费墙后完整内容不可用，仅引言 |

### 阅读顺序建议

1. **先** `runoob-loop-engineering-zh.md`（中文概览，建立整体认知）
2. **再** `addy-osmani-loop-engineering.md`（英文原文，深入框架）
3. **然后** `lushbinary-loop-engineering-guide.md`（Ralph 技术 + /goal 合同）
4. **接着** `lennys-newsletter-agent-loops.md`（实战案例）
5. **最后** `github-cobusgreyling-loop-engineering.md`（可直接用的 Pattern + CLI）

## 核心共识（贯穿所有文章）

| 共识点 | 所有文章一致 |
|--------|-------------|
| Prompt Engineering 未消亡 | Loop 由多个 Prompt 组成，Loop Engineering 是更高层 |
| 制造者-检查者分离 | 写代码的 Agent 不该给自己的作业打分 |
| 状态在磁盘不在上下文 | "模型会忘记，仓库不会" |
| 验证是你的责任 | 无人值守的 Loop = 无人值守的错误生成器 |
| 先慢后快 | 先慢节奏观察成本，再加速 |

## 消化建议

- 消化优先级：**六构件架构 → /goal 合同规范 → 生产 Pattern → 实操 CLI**
- 与当前 Hermes 实践对比：已有 skills+cron+subagents，缺系统化的外循环设计和 `/goal` 式停止条件
