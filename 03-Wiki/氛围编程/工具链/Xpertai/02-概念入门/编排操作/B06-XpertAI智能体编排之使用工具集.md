---
title: Xpert AI 智能体编排之 使用工具集
source: Xpertai/B站视频-Xpert智能体编排/06-XpertAI智能体编排-使用工具集.md
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
- Xpertai/B站视频-Xpert智能体编排/06-XpertAI智能体编排-使用工具集.md
---
# Xpert AI 智能体编排之 使用工具集

# Xpert AI 智能体编排之 使用工具集

- **视频链接**：https://www.bilibili.com/video/BV1N2qbYREJa/
- **作者**：XpertAI_元数信息技术
- **发布时间**：约2024年12月
- **时长**：10:38

## 视频简介

源代码仓库：https://github.com/xpert-ai/
官网：https://mtda.cloud/
在线系统：https://app.mtda.cloud/

## 内容总结

本视频是 Xpert AI 智能体编排系列教程的第二集，重点讲解如何为智能体配置和使用工具集（Toolset），让智能体具备调用外部工具的能力。

### 什么是工具集（Toolset）
- 工具集是智能体与外部世界交互的桥梁
- 包含一系列可被智能体调用的工具/函数
- 让智能体不仅能"说"，还能"做"

### Xpert AI 内置工具集类型
1. **BI 工具集**：语义建模、指标管理、仪表盘等数据分析能力
2. **ChatBI 工具集**：自然语言查询数据库，生成图表和报告
3. **编程工具集**：代码执行、项目管理等开发能力
4. **飞书/钉钉工具集**：企业 IM 集成
5. **MCP 工具集**：Model Context Protocol，标准化的工具调用协议
6. **虚拟环境工具集**：浏览器、文件操作、Python 执行等沙箱能力
7. **自定义工具集**：用户可自行开发工具集扩展智能体能力

### 如何在编排中使用工具集
1. 在智能体编排界面选择目标智能体节点
2. 为该智能体绑定所需的工具集
3. 配置工具集参数（如 API Key、数据源等）
4. 智能体在对话中会自动判断何时调用哪个工具
5. 工具执行结果返回给智能体，继续生成回复

### 工具集与知识库的配合
- 知识库提供"知道什么"
- 工具集提供"能做什么"
- 两者结合让智能体成为真正的专家

## 标签

AI / Xpert / 智能体 / 工具集 / Agent / Toolset
