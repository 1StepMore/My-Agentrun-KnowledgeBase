---
title: 从零部署 Hermes Agent 安装教程
source: 掘金文章（1 篇）；本页为我们的提炼
keywords:
- Hermes-Agent
- AI-Agent
- setup
- beginner-tutorial
state:
  phase: draft
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
sources:
- juejin-7628180482584608794-hermes-agent-from-scratch-deploy.md
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---
# 从零部署 Hermes Agent：一只"会成长的 AI 马"保姆级安装教程

## 前言

2026 年 AI Agent 赛道竞争激烈。Hermes Agent（爱马仕）主打"the agent that grows with you"，与 OpenClaw 的多 Agent 协同不同，Hermes 专注于单一 Agent 的深度自我进化。

核心特点：
- 从每次交互中学习、沉淀技能、记住偏好
- 成长型搭档，用得越久越懂你

部署流程：环境准备 → 一键安装 → 模型配置 → 网关部署 → 常见问题排查

---

## 一、Hermes Agent 是什么

| 项目 | 说明 |
|------|------|
| 开发团队 | Nous Research |
| 开源协议 | MIT（完全免费） |
| 核心卖点 | 闭环学习系统 + 四层记忆架构 + 40+ 内置工具 |
| 支持平台 | Linux、macOS、WSL2、Android（Termux） |
| 消息平台 | Telegram、Discord、Slack、WhatsApp、飞书 |
| 支持模型 | Claude、OpenRouter、DeepSeek、Qwen、Ollama 本地模型等 |

官方资源：
- 官网：hermes-agent.nousresearch.com
- 文档：hermes-agent.nousresearch.com/docs
- GitHub：github.com/NousResearch/hermes-agent
- Discord 社区

---

## 二、环境准备

### 2.1 系统要求

支持平台：Linux、macOS、WSL2

> ⚠️ **注意**：不支持原生 Windows，Windows 用户必须先安装 WSL2

推荐配置：
- CPU：2 核以上
- 内存：4GB 以上（推荐 8GB+）
- 磁盘：10GB+ 可用空间
- 网络：能访问 GitHub（或配置镜像）

### 2.2 前置依赖

几乎不需要手动安装任何东西，安装脚本会自动处理：
- Python 3.11
- Node.js v22
- uv（Python 包管理器）
- ripgrep
- ffmpeg
- 虚拟环境

唯一需要确保的是 **git**：

```bash
# 检查 git 是否已安装
git --version

# Ubuntu/Debian
sudo apt install git

# macOS（通常自带，或用 Homebrew）
brew install git
```

### 2.3 网络加速（国内用户必看）

#### Git 镜像加速

```bash
git config --global url."https://mirror.ghproxy.com/https://github.com".insteadOf "https://github.com"
```

#### pip 镜像加速

```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com
```

#### npm 镜像加速

```bash
npm config set registry https://mirrors.cloud.tencent.com/npm/ --global
```

> 💡 安装完成后如果不需要加速了，可以用 `git config --global --unset-all url.https://mirror.ghproxy.com/https://github.com".insteadOf` 清除配置

---

## 三、一键安装

### 3.1 执行安装脚本

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

脚本自动完成：
- 检测系统架构（x86_64 / arm64）
- 安装 uv、Python 3.11、Node.js v22
- 克隆 Hermes Agent 仓库
- 创建 Python 虚拟环境并安装依赖
- `hermes` 全局命令

> 安装时间：约 3-10 分钟（取决于网络速度）

### 3.2 重新加载 Shell 配置

安装完成后**必须**重新加载 shell 配置才能使用 `hermes` 命令：

```bash
# bash 用户
source ~/.bashrc

# zsh 用户（macOS 默认）
source ~/.zshrc
```

### 3.3 验证安装

```bash
hermes --version
```

如果输出了版本号，说明安装成功！

---

## 四、模型配置

### 4.1 交互式配置（推荐）

```bash
hermes setup
```

这会启动一个交互式向导，引导完成：
- 选择模型提供商
- 输入 API Key
- 基本偏好设置

或者直接用模型选择命令：

```bash
hermes model
```

### 4.2 支持的模型提供商

| 提供商 | 配置方式 | 说明 |
|--------|----------|------|
| Nous Portal | OAuth 登录，零配置 | 官方订阅服务，最简单 |
| Anthropic Claude | API Key 或 Claude Code 授权 | 注意：目前尚未被封禁 |
| OpenRouter | API Key | 支持 200+ 模型，灵活度高 |
| DeepSeek | API Key | 国内用户友好，性价比高 |

---

## 五、核心概念

- [[Hermes Agent]]：Nous Research 出品的开源 AI Agent 框架
- [[Nous Research]]：开发团队
- [[闭环学习系统]]：核心卖点之一
- [[四层记忆架构]]：核心卖点之一
- [[WSL2]]：Windows 用户必须使用
- [[uv]]：Python 包管理器
- [[OpenRouter]]：支持 200+ 模型的聚合平台
- [[DeepSeek]]：国内友好的模型提供商
