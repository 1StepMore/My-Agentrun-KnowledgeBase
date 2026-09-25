---
title: 5 Agent Skill Design Patterns Every ADK Developer Should Know
source: Google Cloud Tech 博客 | 编译：Hermes Agent
related: []
keywords:
- AI-Agent
- Design-Patterns
- ADK
- Skill-Design
- ai-coding
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
  time_wiki: '2026-07-01T12:42:24'
sources: []
---
# 5 Agent Skill Design Patterns Every ADK Developer Should Know

> 来源：Google Cloud Tech 博客 | 编译：Hermes Agent

## 视频概述

很多开发者遇到这样的困惑：Skill 写好了、Skill.md 也写了，但 Agent 输出依然不稳定——格式混乱、遗漏步骤、或者自信地给出错误答案。

Google Cloud Tech 团队研究 Entropic、Versal、Google 内部的 Skill 构建方式后，认为问题很少出在格式规范上，而在**内容设计层面**——Skill 里的逻辑究竟该怎么组织。

他们总结了五种设计模式，对应 Agent 最常失控的五类问题。

---

## 五种设计模式

### 1. Tool Wrapper — 知识何时加载

**问题**：很多人把某技术栈的全部规范提前塞进 System Prompt（React 规范、FastAPI 规范、团队约定等），导致 Context 浪费、模型被无关知识干扰。

**方案**：把这些内容放进 References 作为专家手册。Skill 只负责判断当前任务是否进入某个领域，只有命中时才加载对应知识。

**本质**：按需注入知识，让 Context 保持干净。

---

### 2. Generator — 输出结构稳定

**问题**：模型每次都在现场重新决定输出该长什么样，导致结果不稳定。

**方案**：把输出结构固定在模板里，把表达方式固定在风格指南里。模板回答 "What to produce"，风格指南回答 "How to write"。

**适用场景**：API 文档、标准化报告、Commit Message、Changelog 生成。

**本质**：不让模型现场发挥，只让它补全缺失内容并填充框架。

---

### 3. Reviewer — 审查标准与流程分离

**问题**：团队把 "检查什么" 和 "怎么检查" 混在一起，导致审查规则难以切换。

**方案**：将两者硬拆开——Checklist 定义要检查的内容，Skill.md 定义具体检查方法。输出统一成 Error、Warning、Info 三个级别。

**价值**：今天做代码风格审查，明天换成 OWASP 安全审查，后天换成合规规则，只需替换 Checklist 而非重写 Skill。

---

### 4. Inversion — 先问后做

**问题**：Agent 太爱猜——拿到模糊需求就急着生成，信息不足就自信地自己补全。

**方案**：反转流程，让 Agent 先发问再输出，分三个阶段：
- **Discovery**：确认要解决什么问题
- **Constraints**：问清平台、技术栈、限制条件、交付要求
- **Synthesis**：信息齐全后才开始生成

**关键**：门控指令——信息没齐，不准开工。

**典型场景**：规划客服机器人时，Agent 应先问服务对象、接入渠道、是否对接工单系统、有无合规要求等。

---

### 5. Pipeline — 多步骤不跳步

**问题**：复杂任务有强顺序依赖（分析输入 → 生成中间产物 → 组装最终结果 → 验证），用单一 Prompt 处理时模型容易中途偷懒。

**方案**：把 Skill.md 写成工作流定义，第一步做什么、第二步做什么、什么时候能进入下一步，全都写清楚，中间设置显式门控（Gate）。

**适用场景**：文档生成、复杂代码修改、发布流程、合规流程。

**价值**：每步只加载当前所需的 references 和 templates，Context 保持干净。

---

## 如何选择模式

| 问题类型 | 对应模式 |
|---------|---------|
| 知识何时加载 | Tool Wrapper |
| 输出结构不稳定 | Generator |
| 审查标准和流程混在一起 | Reviewer |
| 信息不全却急着开工 | Inversion |
| 复杂任务容易跳步骤 | Pipeline |

**判断路径**：
1. 先问 Skill 是否要产出内容？
   - 要产出且从模板产出 → Generator
   - 要产出但本质是运行时加载知识 → Tool Wrapper
2. 是否在评估已有输入？ → Reviewer
3. 是否必须先向用户补全信息？ → Inversion
4. 是否有严格步骤确认点不能跳过？ → Pipeline

**可以叠加**：Generator 前面可接 Inversion，Pipeline 结尾可接 Reviewer，Tool Wrapper 可叠在任何模式上补知识。

---

## 核心要点

别把所有指令都塞进 System Prompt。可靠的 Skill 靠的是更合适的结构：
- 先判断遇到的是知识问题、结构问题、审查问题、澄清问题还是流程问题
- 模式选对了，Agent 才会稳定

---

## 相关概念

- Skill.md
- System Prompt
- Context
- References
- Template / Style Guide
- Gate（门控）
- ADK (Agent Development Kit)
