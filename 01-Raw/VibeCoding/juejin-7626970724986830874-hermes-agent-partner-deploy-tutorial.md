---
title: 养个AI 合伙人：Hermes Agent 保姆级部署教程
keywords:
- Hermes-Agent
- OpenClaw
- setup
- 对比
- AI-Agent
- 龙虾
- 技能
- 记忆
state:
  phase: raw
  time_raw: '2026-05-07T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:53:35'
source_url: https://juejin.cn/post/7626970724986830874
source_type: article
source_platform: juejin
publish_date: 2026-04
fetch_date: '2026-05-07'
priority: 3
language: zh
notes: 来源：掘金。对比了 OpenClaw（龙虾）和 Hermes Agent 的核心差异，详细介绍三层闭环学习引擎，以及 6 步部署指南。强调双 Agent 组合使用的工作流。
author: ''
author_id: ''
---
# 养个AI 合伙人：Hermes Agent 保姆级部署教程

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## OpenClaw vs Hermes 核心对比

| 对比维度 | OpenClaw (龙虾) | Hermes Agent |
|----------|----------------|--------------|
| **设计哲学** | 生态广度优先 | 学习闭环优先 |
| **记忆系统** | Markdown外挂（被动存储） | SQLite内生引擎（主动归纳） |
| **技能来源** | 人工编写 | 自动生成+人工干预 |
| **安全机制** | 需手动配置 | 开箱即用（沙盒+隔离+审批） |

**核心区别**：龙虾帮你干活，Hermes 帮你进化。

## 三层闭环学习引擎

### 第一层：深度持久化记忆
- FTS5 全文检索 + SQLite 存储
- 大模型驱动的自动分类、重组、摘要归纳

### 第二层：技能自主生成
- 完成复杂任务后，自动记录操作步骤、避坑指南、验证逻辑

### 第三层：自我进化训练闭环
- Atropos 强化学习框架
- 自动生成批量轨迹数据

## 推荐工作流：龙虾 + Hermes 双 Agent

| 场景 | 用龙虾 | 用Hermes |
|------|--------|----------|
| 跨平台发消息 | ✅ 50+平台 | ❌ |
| 浏览器自动化 | ✅ 成熟 | ✅ |
| 长期记忆积累 | ⚠️ Markdown外挂 | ✅ SQLite内生 |
| 自动技能生成 | ❌ | ✅ |
| 安全隔离 | ⚠️ 需手动配 | ✅ 开箱即用 |

## 成本算账

| 项目 | Hermes方案 | 人工助理 |
|------|------------|----------|
| 云服务器 | 68元/年 | — |
| API调用 | ~50-100元/月 | — |
| **月合计** | **~56-64元/月** | 3000-5000元/月 |

## 3 个踩坑提醒

1. **别一上来开全功能**——先开 `browser` 和 `shell`，跑稳了再逐步加
2. **记忆会"串"**——定期清理 `hermes memory prune --older-than 60`
3. **Windows 用户用 WSL2**
