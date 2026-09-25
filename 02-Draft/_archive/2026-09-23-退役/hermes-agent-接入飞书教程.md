---
title: hermes-agent-接入飞书教程
keywords:
- Hermes-Agent
- 飞书
- IM工具
- integration-tutorial
state:
  phase: draft-archived
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
sources: []
superseded_by: '[[Hermes-Agent接入飞书-企业自建应用与长连接配置]]'
---
# Hermes Agent 接入飞书

## 核心概念

- [[Hermes Agent]] - 一个具有自学能力的AI智能体，可通过对话方式操控，支持定时任务执行和技能创建
- [[Gaway]] - Hermes内置的进程，专门负责接入各类聊天平台，目前支持14+平台如飞书、Discord、钉钉等
- [[飞书企业自建应用]] - 在飞书开放平台创建的应用，用于与Hermes Agent建立连接，支持长连接方式通信
- [[WebSocket 长连接]] - 推荐使用WebSocket协议接收飞书事件和回调，最便于与Hermes Agent交互
- [[白名单配置]] - 安全设置，用于限制只有指定用户ID能够与机器人对话，防止未授权访问
- [[定时任务]] - Hermes Agent的核心功能之一，可创建如每日刷新Hacker News等自动化任务
- [[技能(Skills)]] - Agent根据执行经验自动创建的工具能力，可被后续任务调用

## 总结

本教程详细介绍了将 [[Hermes Agent]] 接入[[飞书]]的完整流程：通过在飞书开放平台创建企业自建应用，配置权限和事件订阅（使用[[WebSocket 长连接]]），然后在终端完成网关配置并设置[[白名单配置]]实现安全访问。接入后可在飞书中直接与AI智能体对话，定时任务结果会推送至聊天窗口，且记忆在多平台间共享，提供更便捷的AI交互体验。

## 标签

#Hermes-Agent #飞书集成 #AI-Agent #聊天机器人 #自动化 #教程
