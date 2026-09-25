---
title: hermes-agent高级玩法-微信LLM-Wiki-Obsidian
source: 来源待补（历史文件）
keywords:
- Hermes-Agent
- 微信
- LLM-Wiki
- Obsidian
- knowledge-base
state:
  phase: draft
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
sources: []
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---
# Hermes Agent 高级玩法与 LLM Wiki 知识库

## 核心概念

### 1. Hermes Agent
基于希腊神话中奥林匹斯神赫尔墨斯命名的 AI Agent 项目，意为"众神的使者"。该项目已原生支持个人微信连接，通过扫码即可使用，支持私聊、圈聊及多媒体交互。

### 2. 微信集成
Hermes Agent 通过微信扫码方式连接，支持多种消息类型包括图像、视频、文件、语音等。用户可以在微信中直接与 Agent 对话，测试显示响应速度快，使用 MiniMax 模型。

### 3. LLM Wiki
基于 Andrea Ke Transition 提出的 [[RAG]] to Wiki 模式，通过 skill 方式内置于 Hermes Agent 中。可用于构建、管理和使用知识库，支持直接导入 PDF 论文或链接，自动提取内容并更新概念页面。

### 4. RRM Wiki 三层架构
- **原始来源层**：存储文档、论文、图像等原始文件，大模型只读不改
- **Wiki 页面层**：包含摘要、实体、概念、分析等页面及导航文件
- **协同进化层**：定义结构约束，将大模型转变为 Wiki 维护者，人机共同维护

### 5. 知识飞轮
Wiki 模式相比传统 [[RAG]] 的核心优势：从无状态碎片检索升级为有状态的知识积累，实现知识的持续增长和复用，避免每次查询重复发现相同知识。

### 6. 传统 RAG vs RRM Wiki
传统 RAG 每次查询从零开始，知识不积累、不关联；而 RRM Wiki 能实现知识累积、交叉引用，最终形成数据飞轮效应。

### 7. Graphify 适用场景
[[Graphify]] 更适合代码库分析，对于日常学习和工作中积累的笔记文档，使用 RRM Wiki 模式更为适合。

---

## 总结

Hermes Agent 不仅是一个 AI 对话工具，更是一个强大的 [[知识管理]] 平台。通过微信扫码即可快速接入，配合内置的 LLM Wiki 工作流，可以将散落的文档、论文转化为结构化的知识库。其 RRM Wiki 三层架构实现了从被动检索到主动积累的跃迁，让 [[Agent]] 能够持续学习和进化知识，最终形成知识飞轮。与传统 [[RAG]] 相比，这种模式更适合个人知识管理和长期学习场景。

---

## 推荐标签

#HermesAgent #LLMWiki #知识管理 #AI #RAG #Agent #Obsidian
