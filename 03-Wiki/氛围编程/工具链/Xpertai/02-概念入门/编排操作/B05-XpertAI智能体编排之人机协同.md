---
title: Xpert AI 智能体编排之 人机协同
source: Xpertai/B站视频-Xpert智能体编排/05-XpertAI智能体编排-人机协同.md
related: []
keywords:
- Multi-Agent
- ai-coding
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
  time_wiki: '2026-07-01T12:42:24'
sources:
- Xpertai/B站视频-Xpert智能体编排/05-XpertAI智能体编排-人机协同.md
---
# Xpert AI 智能体编排之 人机协同

# Xpert AI 智能体编排之 人机协同

- **视频链接**：https://www.bilibili.com/video/BV1ATkjYaEJb/
- **作者**：XpertAI_元数信息技术
- **发布时间**：2024-12-17
- **时长**：06:24
- **播放量**：1564

## 视频简介

源代码仓库：https://github.com/xpert-ai/
官网：https://mtda.cloud/
在线系统：https://app.mtda.cloud/

## 内容总结

本视频介绍了 Xpert AI 平台中的"人机协同"（Human-in-the-loop，HITL）功能，展示了如何在智能体执行过程中嵌入人工干预。

### 什么是人机协同（HITL）
- 通过在人机协作系统中嵌入人工干预
- 在关键或敏感节点上打断 AI 智能体的自动执行过程
- 由人类进行实时决策或调整
- 确保系统在复杂和高风险情境下的可靠性和准确性

### 为什么需要人机协同
- AI 智能体可能产生幻觉或错误决策
- 某些业务场景（如财务审批、合同签署）必须有人工确认
- 提升用户对 AI 系统的信任度
- 合规要求：某些行业法规要求关键决策必须有人工参与

### Xpert AI 的人机协同实现
1. 在智能体编排中设置人工审批节点
2. 智能体执行到该节点时自动暂停
3. 等待人工审核并做出决策（通过/拒绝/修改）
4. 人工决策后智能体继续执行
5. 整个过程有完整的审计日志

### 典型应用场景
- **内容审核**：AI 生成内容后需人工确认再发布
- **审批流程**：AI 处理后需人工签字确认
- **决策辅助**：AI 提供建议，人工做最终决定
- **异常处理**：AI 遇到无法处理的情况时转交人工

## 标签

AI / BI / Copilot / Xpert / 人机 / OpenAI / Agent
