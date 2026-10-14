---
title: 从零部署 Hermes Agent：一只"会成长的 AI 马"保姆级安装教程
keywords:
- Claude
- Hermes-Agent
- OpenClaw
- Telegram
- 飞书
state:
  phase: raw
  time_raw: '2026-05-07T00:00:00'
  time_draft: '2026-09-19T14:37:03'
  time_wiki: '2026-09-23T00:53:35'
source_url: https://juejin.cn/post/7628180482584608794
source_type: article
source_platform: juejin
author: vivo互联网技术
publish_date: '2026-04-14'
fetch_date: '2026-05-07'
priority: 3
language: zh
author_id: ''
notes: ''
---
# 从零部署 Hermes Agent：一只"会成长的 AI 马"保姆级安装教程

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容
从零部署 Hermes Agent：一只"会成长的 AI 马"保姆级安装教程前言 2026 年 AI Agent 赛道卷 - 掘金
                沸点
                课程
                数据标注
HOT
                AI Coding
更多
                    直播
                    APP
插件
                直播
                APP
插件
搜索历史
                        清空
    创作者中心
写文章
发沸点
写笔记
写代码
草稿箱
创作灵感
            查看更多
首次登录 / 注册免费领取
登录 / 注册
            从零部署 Hermes Agent：一只"会成长的 AI 马"保姆级安装教程
    90后晨仔
                    2,155
                    阅读9分钟
                      专栏： 
                      开发工具
Hermes Agent —— Nous Research 出品的开源 AI Agent 框架，主打"越用越聪明"。本文手把手带你从安装到配置到排坑，全流程实操记录。
前言
2026 年 AI Agent 赛道卷出了天际。OpenClaw（龙虾）凭借多 Agent 协同火爆出圈后，另一款产品悄然崛起——
Hermes Agent
（爱马仕），口号是 ** 
"the agent that grows with you"
 **，主打单一 Agent 的深度自我进化。
和 OpenClaw 最大的不同在于：Hermes 不是"用完归零"的工具，而是一个
会从每次交互中学习、沉淀技能、记住你偏好
的成长型搭档。用得越久，它越懂你。
本文将从
环境准备 → 一键安装 → 模型配置 → 网关部署 → 常见问题排查
，完整记录一次真实的部署过程，帮你少走弯路。
一、Hermes Agent 是什么？（30 秒速览）
| 项目 | 说明 |
开发团队
 | Nous Research |
开源协议
 | MIT（完全免费） |
核心卖点
 | 闭环学习系统 + 四层记忆架构 + 40+ 内置工具 |
支持平台
 | Linux、macOS、WSL2、Android（Termux） |
消息平台
 | Telegram、Discord、Slack、WhatsApp、飞书 |
支持模型
 | Claude、OpenRouter、DeepSeek、Qwen、Ollama 本地模型等 |
官方资源：
🏠 官网：
hermes-agent.nousresearch.com
📖 文档：
hermes-agent.nousresearch.com/docs
💻 GitHub：
github.com/NousResearc…
💬 Discord 社区：官网底部 Join Discord 入口
二、环境准备
2.1 系统要求
Hermes Agent 支持 
Linux、macOS、WSL2
，
不支持原生 Windows
。
⚠️ Windows 用户必须先安装 WSL2（Windows Subsystem for Linux），然后在 WSL2 内运行。
推荐配置：
CPU：2 核以上
内存：4GB 以上（推荐 8GB+）
磁盘：10GB+ 可用空间
网络：能访问 GitHub（或配置镜像）
2.2 前置依赖
好消息是——
几乎不需要手动装任何东西
。安装脚本会自动处理：
Python 3.11
Node.js v22
uv（Python 包管理器）
ripgrep
ffmpeg
虚拟环境
你唯一需要确保的是系统里有 
git
：
bash
体验AI代码助手
代码解读
复制代码
# 检查 git 是否已安装
git --version
# Ubuntu/Debian
sudo apt install git
# macOS（通常自带，或用 Homebrew）
brew install git
2.3 网络加速（国内用户必看）
如果你在国内服务器部署，GitHub 和 npm/pip 的访问速度可能很慢。建议提前配置镜像：
Git 镜像加速：
bash
体验AI代码助手
代码解读
复制代码
git config --global url.
"https://mirror.ghproxy.com/https://github.com"
.insteadOf 
"https://github.com"
pip 镜像加速：
bash
体验AI代码助手
代码解读
复制代码
pip config 
set
 global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config 
set
 install.trusted-host mirrors.aliyun.com
npm 镜像加速：
bash
体验AI代码助手
代码解读
复制代码
npm config 
set
 registry https://mirrors.cloud.tencent.com/npm/ --global
💡 安装完成后如果不需要加速了，可以用 
git config --global --unset-all url.https://mirror.ghproxy.com/https://github.com".insteadOf
 清除配置。
三、一键安装
3.1 执行安装脚本
打开终端，执行以下命令：
bash
体验AI代码助手
代码解读
复制代码
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
脚本会自动完成以下操作：
检测系统架构（x86_64 / arm64）
安装 uv、Python 3.11、Node.js v22
克隆 Hermes Agent 仓库
创建 Python 虚拟环境并安装依赖
hermes
 全局命令
整个安装过程大约需要 
3-10 分钟
（取决于网络速度）。
3.2 重新加载 Shell 配置
安装完成后，
必须重新加载 shell 配置
才能使用 
hermes
 命令：
bash
体验AI代码助手
代码解读
复制代码
# bash 用户
source
 ~/.bashrc
# zsh 用户（macOS 默认）
source
 ~/.zshrc
3.3 验证安装
bash
体验AI代码助手
代码解读
复制代码
hermes --version
如果输出了版本号，说明安装成功！🎉
四、模型配置
安装好之后，下一步是配置 LLM 提供商。Hermes 支持多种模型后端：
4.1 交互式配置（推荐）
bash
体验AI代码助手
代码解读
复制代码
hermes setup
这会启动一个交互式向导，引导你完成：
选择模型提供商
输入 API Key
基本偏好设置
或者直接用模型选择命令：
bash
体验AI代码助手
代码解读
复制代码
hermes model
4.2 支持的模型提供商
| 提供商 | 配置方式 | 说明 |
Nous Portal
 | OAuth 登录，零配置 | 官方订阅服务，最简单 |
Anthropic Claude
 | API Key 或 Claude Code 授权 | 注意：目前尚未被封禁 |
OpenRouter
 | API Key | 支持 200+ 模型，灵活度高 |
DeepSeek
 | API Key | 国内用户友好，性价比高 |