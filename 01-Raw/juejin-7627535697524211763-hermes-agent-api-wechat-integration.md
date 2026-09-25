---
title: Hermes Agent：一步API+微信接入完整教程，扫码即用AI助理
keywords:
- Hermes-Agent
- 微信
- integration-tutorial
- API
- ilink
- yibuapi
state:
  phase: raw
  time_raw: '2026-05-07T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:53:35'
source_url: https://juejin.cn/post/7627535697524211763
source_type: article
source_platform: juejin
publish_date: 2026-04
fetch_date: '2026-05-07'
priority: 3
language: zh
notes: 来源：掘金。详细介绍 Hermes Agent 通过一步API（yibuapi.com）配置模型，以及接入微信个人号的完整流程。包含故障排查部分。
author: ''
author_id: ''
---
# Hermes Agent：一步API+微信接入完整教程，扫码即用AI助理

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 安装命令

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## API Token 配置

### 推荐：一步API（yibuapi.com）

1. 访问 yibuapi.com 控制台
2. 创建 API-KEY
3. 配置：
   - 模型提供商选择：`Custom endpoint (OpenAI compatible)`
   - API Base URL：`https://yibuapi.com/v1`
   - 推荐默认模型：`glm-5.1`

```yaml
model:
  provider: custom
  base_url: https://yibuapi.com/v1
  api_key: sk-xxxxxxx
  default: glm-5.1
```

## 微信接入

```bash
hermes gateway setup
# 选择 WeChat (ilink / ClawBot)
hermes gateway start
```

> ⚠️ 建议使用**微信小号**扫码，避免主号风险

## 故障排查

| 问题 | 解决方案 |
|------|---------|
| AI 不回复 | 1. 测试模型是否正常（`hermes` 命令）<br>2. 检查网关是否启动成功 |
| 空响应错误 | 99% 是 URL 或 Key 错误 |
