---
title: hermes-agent-guide-draft
source: 掘金文章、知乎回答（2 篇）；本页为我们的提炼
keywords:
- Hermes-Agent
- AI-Agent
- LLM
- setup
- Skill
state:
  phase: draft
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
sources:
- zhihu-2027128115831260939.md
- juejin-7628180482584608794-hermes-agent-from-scratch-deploy.md
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---
# Hermes Agent 完整指南

[[Hermes Agent]] 是 Nous Research 开发的开源 AI Agent 框架，核心特性：**模型无关 + 多平台 + 持久记忆 + 自进化**。截至 2026 年，GitHub 74K+ stars，MIT 协议，完全免费。

## 环境要求

- Python 版本：3.11 或以上
- 检查命令：`python3 --version`
- macOS：`brew install python@3.11`
- Linux/WSL2：`sudo apt update && sudo apt install python3.11 python3.11-venv`

## 安装

一行命令完成安装和 PATH 注册：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装后重载 shell 配置：
```bash
source ~/.zshrc   # macOS
source ~/.bashrc  # Linux
```

**注意**：不要用 `sudo` 运行安装脚本，避免权限问题。

## 配置向导

首次运行 `hermes setup`，向导引导完成：
- 选择 [[LLM]] 提供商（OpenRouter、Anthropic、MiniMax 等）
- 填入 API Key
- 配置默认工具集
- 设置基础偏好

## 模型配置

[[Hermes Model]] 支持随时切换：

```bash
hermes model   # 交互式菜单选择
```

同一对话内可临时切换模型，实现"便宜模型跑初稿 → 强模型做精修"：

```bash
/model openrouter:nous/hermes-3-405b
```

支持兼容 [[OpenAI API]] 格式的国内模型（Kimi、Moonshot、MiniMax 等），无需翻墙。

## 验证安装

```bash
hermes doctor
```

检查项：Python 版本、依赖完整性、模型配置、工具链状态。80% 的问题可在此直接定位解决。

## 斜杠命令

| 命令 | 作用 |
|------|------|
| `/skills` | 查看 agent 自进化积累的技能库 |
| `/model` | 切换模型 |
| `/insights --days 7` | AI 周报：学习总结、技能调用统计 |
| `/reset` | 重置会话 |

## 多平台网关

[[Hermes Gateway]] 支持同时接入多个聊天平台：

```bash
hermes gateway
```

支持平台：Telegram、Discord、Slack、WhatsApp、Signal、Matrix、Email、飞书（Feishu）、钉钉（DingTalk）、企业微信（WeCom）等。

**跨平台上下文连续**：在一个平台聊到一半，切到另一平台继续，上下文不丢失。适合多平台运营场景。

## 从 OpenClaw 迁移

[[OpenClaw]]（小龙虾）迁移工具：

```bash
hermes claw migrate              # 交互式迁移（推荐）
hermes claw migrate --dry-run    # 预览不执行
hermes claw migrate --preset user-data  # 只迁移用户数据
```

迁移内容：人格文件（SOUL.md）、记忆数据（MEMORY.md、USER.md）、自建技能、命令审批白名单、各平台 API Key、TTS 语音资源、工作区指令（AGENTS.md）。

迁移后 OpenClaw 原始数据不删除，原来的龙虾还在。

## 技能系统

[[Hermes Skills]] 是 Agent 自进化的核心机制。完成复杂任务后，agent 自动将解决路径沉淀为可复用技能，存入 `~/.hermes/skills/`。

查看和安装技能：
```bash
hermes skills list        # 列出已安装技能
hermes skills browse       # 浏览技能市场
hermes skills install <id> # 安装新技能
```

## 记忆系统

[[Hermes Memory]]：持久跨会话记忆，包含用户画像（偏好、习惯）、任务记忆（学会的工作方式）、技能积累（沉淀的解决路径）。

## 核心差异化价值

1. **模型无关**：积累的技能和记忆不受模型切换影响，是 AI 变化时代的护城河
2. **跨平台上下文连续**：一份记忆走天下，AI 客服体验革新
3. **自进化**：[[Hermes Skills]] + /insights 周报让 AI 员工第一次有"绩效数据"可看
4. **一键迁移**：[[OpenClaw]] → Hermes 的平滑迁移路径，生态收敛信号
