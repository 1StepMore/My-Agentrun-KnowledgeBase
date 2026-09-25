---
title: Hermes-Agent-一步API-微信接入教程
source: 掘金文章（1 篇）；本页为我们的提炼
keywords:
- Hermes-Agent
- 微信
- API
- setup
- integration-tutorial
state:
  phase: draft
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
sources:
- juejin-7627535697524211763-hermes-agent-api-wechat-integration.md
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---
# Hermes Agent 完整配置指南

## 概述

Hermes Agent 是一个 AI 助理项目，支持通过 API 配置后接入微信进行交互。项目地址：NousResearch/hermes-agent

## 安装部署

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## API Token 配置

### 推荐方案：一步API（yibuapi.com）

| 配置项 | 值 |
|--------|-----|
| 模型提供商 | `Custom endpoint (OpenAI compatible)` |
| API Base URL | `https://yibuapi.com/v1` |
| 推荐默认模型 | `glm-5.1` |

**配置文件示例：**

```yaml
model:
  provider: custom
  base_url: https://yibuapi.com/v1
  api_key: sk-xxxxxxx
  default: glm-5.1
```

## 微信接入

```bash
hermes gateway setup  # 选择 WeChat (ilink / ClawBot)
hermes gateway start
```

> ⚠️ 建议使用**微信小号**扫码，避免主号风险

## 故障排查

| 问题 | 解决方案 |
|------|---------|
| AI 不回复 | 1. 测试模型是否正常（`hermes` 命令）<br>2. 检查网关是否启动成功 |
| 空响应错误 | 99% 是 URL 或 Key 错误 |

## 相关链接

- [[AI-Agent]] - AI 智能体相关概念
- [[微信机器人]] - 微信接入配置
- [[API-Key]] - API 密钥管理

## 总结

Hermes Agent 提供了**一键安装 + 配置**的 AI 助理部署方案。核心步骤：1) 安装脚本 → 2) 配置 [[yibuapi.com]] 的 OpenAI 兼容 API → 3) 运行 `hermes gateway setup` 接入微信。遇到问题时优先检查 API 地址和 Key 是否正确。

---

**标签：** #Hermes-Agent #AI-Agent #微信接入 #部署教程 #yibuapi
