---
title: 【2026/Agent】一期讲透！理论+代码从ToolCall到Harness、Claw，告诉你Agent的一切
keywords:
- AI-Agent
- tool-calling
- ReAct
- LangChain
- LangGraph
- Multi-Agent
state:
  phase: draft-archived
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
sources:
- Bilibili/bilibili-BV1dw526tEMA-toolcall-to-harness-claw-agent-101.md
related: []
promoted_to: '[[从ToolCall到Harness-Claw-Agent一切]]'
---
# 【2026/Agent】一期讲透！理论+代码从ToolCall到Harness、Claw，告诉你Agent的一切

> 此文档为Draft版本，由原始素材编译整理

---

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | 【2026/Agent】一期讲透！理论+代码从ToolCall到Harness、Claw，告诉你Agent的一切 |
| 作者 | 木乔_Mokio |
| 发布时间 | 2026-05-13 |
| 总时长 | 121分03秒（13个分P） |
| BV号 | BV1dw526tEMA |
| 播放量 | 1823（截至抓取时） |

---

## 核心概念

### 1. LangChain 和 LangGraph 基础

**LangChain** 是做大模型应用的一个组件工具箱，帮助把各种东西拼接起来。它提供模型（Model）、提示词（Prompt）、消息（Message）、工具（Tool）等组件。

**LangGraph** 建立在LangChain基础之上，专门做Agent流程编排，适合长期任务、多步循环执行。图由节点（Node）和边（Edge）组成，核心是**State**——整个图的共享数据类型，节点都可以读写它。

### 2. Function Calling / ToolCall

**本质**：让模型去结构化输出，由本地的代码翻译并执行。

**痛点解决**：早期模型只能交流不能交互，无法获取实时数据。OpenAI推出Function Calling让模型调用工具，并通过大量训练保证模型输出严格遵循JSON格式，避免解析错误。

**实现方式**：
- 制定协议，用tag包裹工具和参数
- 模型输出结构化字符串
- 本地代码解析并执行对应函数

### 3. Agent Loop

**定义**：从做一步到做一件事。

ToolCall只能完成单轮对话，无法完成复杂任务。Agent Loop通过循环机制，把工具结果反馈给模型，让模型继续进行下一步动作，形成任务链。

### 4. ReAct 范式

**ReAct = Reasoning（推理） + Action（行动）**

三个关键节点：
1. **思考（Reasoning）**：模型分析情况
2. **行动（Action）**：决定是否调用工具
3. **观察（Observation）**：执行并观察结果

模型内部维护一个消息列表，把思考产生的内容和工具结果都放进状态里，带着State在循环里反复执行。

### 5. Reflection 范式

**核心**："无日三省吾身"——引入批判节点。

**问题**：ReAct模型只完成任务但不检查对错，像急于表现的实习生。

**解决**：在思考、行动、反馈基础上多加一个**Critic（批判）**节点。模型完成后优先把任务输给Critic，Critic对比原始任务判断是否打回。

### 6. Plan and Execute 范式

**核心**："先谋而后动"——解决模型短视和遗忘问题。

**架构**：
- **Planer**：先分析任务，拆解成多个Todo
- **Executor**：按计划执行工具
- **Reflection**：检查执行情况
- **Replanner**：判断是否需要重新规划

当任务复杂到几百上千轮时，State里的Plan和Task能实时提醒模型不忘记原始任务。

### 7. Multi-Agent 架构

**问题**：单体Agent像全能工程师，给它长串Prompt让它身兼多职会"大脑串台"、效率下降、前后端混淆。

**解决**：引入多个专业Agent分工合作。
- **Router/Supervisor**：直接面向用户，判断任务派给谁
- **专家Agent**：每个只专注1000字左右的专属Prompt，保证注意力纯粹

---

## 关键技术栈

- **框架**：LangChain、LangGraph
- **模型**：OpenAI GPT、DeepSeek V3 Flash
- **工具**：UV（包管理）、Whisper（语音转文字）
- **核心范式**：ReAct、Reflection、Plan and Execute、Multi-Agent

---

## 视频大纲

1. **理论讲解**：ToolCall、ReAct、Context Engineering、Harness等概念白板解析
2. **代码编写**：最小代码实现各个概念
3. **项目推进**：从ToolCall到Cloud Code手动做项目
4. **资料推荐**：Notion笔记 + GitHub仓库

---

## 重点摘录

> "Agent它的本质，所有后续的处理都是针对模型输入和输出的文本进行操作的。"
> 
> "Function Calling它的本质就是让模型去结构化输出，然后由本地的代码翻译并执行。"
> 
> "Plan and Execute，成功解决了我们模型的一个短视问题。当我的任务足够复杂，我们的循环次数几百上千轮的时候，这样一个State里的Plan和Task就能够实时提醒模型，不要忘记原来的任务是什么。"

---

## 相关资源

- GitHub仓库：视频简介里有链接
- Notion笔记：包含推荐项目资料

---

## 抓取备注

- 抓取时间：2026-05-14
- 抓取工具：yt-dlp + Whisper small GPU + MiniMax-M2.7
