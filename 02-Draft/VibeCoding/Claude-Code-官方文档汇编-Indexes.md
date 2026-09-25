---
title: Claude Code 官方文档汇编 · Indexes
source: Claude Code 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/claude-code/claude-code-_llms-cn.md
- VibeCoding/claude-code/claude-code-_llms-de.md
- VibeCoding/claude-code/claude-code-_llms-es.md
- VibeCoding/claude-code/claude-code-_llms-fr.md
- VibeCoding/claude-code/claude-code-_llms-id.md
- VibeCoding/claude-code/claude-code-_llms-it.md
- VibeCoding/claude-code/claude-code-_llms-jp.md
- VibeCoding/claude-code/claude-code-_llms-ko.md
- VibeCoding/claude-code/claude-code-_llms-pt-br.md
- VibeCoding/claude-code/claude-code-_llms-ru.md
- VibeCoding/claude-code/claude-code-_llms-zh-hant.md
evidence: E1
domain: VibeCoding
keywords:
- claude-code
- vibe-coding
- AI编程
- AI-Agent
- context-engineering
state:
  phase: draft
  time_raw: 2026-09-23 02:42:51+08:00
  time_draft: 2026-09-23 03:14:06+08:00
  time_wiki: null
wiki_target: false
wiki_note: 参考层：多源官方汇编（11 源，供 Wiki 引用，不单独成篇）
---

> **汇编性质**：Claude Code 官方文档 官方原文 11 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## Claude Code Docs: Chinese

- 官方原文：https://code.claude.com/docs/_llms/cn.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-cn.md`

# Claude Code Docs: Chinese

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Chinese

### 快速开始

#### 快速开始

- [概述](https://code.claude.com/docs/zh-CN/overview.md): Claude Code 是一个代理编码工具，可以读取你的代码库、编辑文件、运行命令，并与你的开发工具集成。可在终端、IDE、桌面应用和浏览器中使用。
- [快速开始](https://code.claude.com/docs/zh-CN/quickstart.md): 欢迎使用 Claude Code！
- [更新日志](https://code.claude.com/docs/zh-CN/changelog.md)

#### 核心概念

- [Claude Code 如何工作](https://code.claude.com/docs/zh-CN/how-claude-code-works.md): 了解代理循环、内置工具以及 Claude Code 如何与您的项目交互。
- [扩展 Claude Code](https://code.claude.com/docs/zh-CN/features-overview.md): 了解何时使用 CLAUDE.md、Skills、subagents、hooks、MCP 和 plugins。
- [探索 .claude 目录](https://code.claude.com/docs/zh-CN/claude-directory.md): Claude Code 读取 CLAUDE.md、settings.json、hooks、skills、commands、subagents、workflows、rules 和自动内存的位置。探索项目中的 .claude 目录和主目录中的 ~/.claude。
- [探索上下文窗口](https://code.claude.com/docs/zh-CN/context-window.md): Claude Code 上下文窗口在会话期间如何填充的交互式模拟。查看自动加载的内容、每个文件读取的成本以及规则和 hooks 何时触发。
- [Claude Code 如何使用 prompt caching](https://code.claude.com/docs/zh-CN/prompt-caching.md): Claude Code 自动管理 prompt caching。了解为什么模型切换会触发缓慢的未缓存回合、`/compact` 的成本、为什么 CLAUDE.md 编辑在会话中期不适用，以及如何检查缓存命中率。

#### 使用 Claude Code

- [Claude 如何记住您的项目](https://code.claude.com/docs/zh-CN/memory.md): 使用 CLAUDE.md 或 AGENTS.md 文件为 Claude 提供持久指令，并让 Claude 通过自动记忆自动积累学习。
- [管理会话](https://code.claude.com/docs/zh-CN/sessions.md): 命名、恢复、分支和在 Claude Code 对话之间切换。涵盖 `--continue`、`--resume`、`--from-pr`、`/resume` 选择器、会话命名、导出文本记录和文本记录存储位置。
- [常见工作流程](https://code.claude.com/docs/zh-CN/common-workflows.md): 使用 Claude Code 探索代码库、修复错误、重构、测试和其他日常任务的分步指南。
- [提示词库](https://code.claude.com/docs/zh-CN/prompt-library.md): 复制粘贴提示词到 Claude Code，按任务和角色标记。
- [Claude Code 最佳实践](https://code.claude.com/docs/zh-CN/best-practices.md): 从配置环境到跨并行会话扩展，充分利用 Claude Code 的提示和模式。

#### 平台和集成

- [平台和集成](https://code.claude.com/docs/zh-CN/platforms.md): 选择在哪里运行 Claude Code 以及连接什么工具。比较 CLI、Desktop、VS Code、JetBrains、Web 以及 Chrome、Slack 和 CI/CD 等集成。
- [使用 Remote Control 从任何设备继续本地会话](https://code.claude.com/docs/zh-CN/remote-control.md): 使用 Remote Control 从您的手机、平板电脑或任何浏览器继续本地 Claude Code 会话。适用于 claude.ai/code 和 Claude 移动应用。
- [让 Claude 通过 Projects 协调持续进行的工作](https://code.claude.com/docs/zh-CN/claude-projects.md): 在一个对话中为 Claude 提供一组相关工作，让它协调共享存储库、说明和内存的并行云会话。
- [Claude Code 移动版](https://code.claude.com/docs/zh-CN/mobile.md): 从您的手机使用 Claude 应用程序启动、监控和指导 Claude Code 任务，支持 iOS 和 Android。
- [在 Chrome 中使用 Claude Code](https://code.claude.com/docs/zh-CN/chrome.md): 将 Claude Code 连接到 Chrome 浏览器，以测试网络应用、使用控制台日志进行调试、自动填充表单以及从网页中提取数据。
- [让 Claude 从 CLI 使用您的计算机](https://code.claude.com/docs/zh-CN/computer-use.md): 在 Claude Code CLI 中启用 computer use，使 Claude 能够在 macOS 上打开应用、点击、输入和查看您的屏幕。测试原生应用、调试视觉问题，以及自动化仅限 GUI 的工具，无需离开您的终端。
- [在 VS Code 中使用 Claude Code](https://code.claude.com/docs/zh-CN/vs-code.md): 安装和配置 VS Code 的 Claude Code 扩展。获得 AI 编码协助，包括内联差异、@-提及、计划审查和快捷键。
- [JetBrains IDEs](https://code.claude.com/docs/zh-CN/jetbrains.md): 在 JetBrains IDE（包括 IntelliJ、PyCharm、WebStorm 等）中使用 Claude Code
- [Slack 中的 Claude Code](https://code.claude.com/docs/zh-CN/slack.md): 直接从 Slack 工作区委派编码任务。Anthropic 正在为 Team 和 Enterprise 工作区停用此早期版本，转而使用 Claude Tag；它仍然是 Pro 和 Max 计划上的设置路径。
- [Claude Tag](https://code.claude.com/docs/zh-CN/claude-tag.md): 通过 Claude Tag 将 Claude 引入您团队的 Slack 频道，并在 claude.com 上查找其设置和使用文档。

##### Claude Code 云端版

- [在云中开始使用 Claude Code](https://code.claude.com/docs/zh-CN/web-quickstart.md): 从浏览器或手机在云中运行 Claude Code。连接 GitHub 仓库、提交任务，并在无需本地设置的情况下审查 PR。
- [在云端使用 Claude Code](https://code.claude.com/docs/zh-CN/claude-code-on-the-web.md): 从浏览器、手机、桌面应用或终端在云端运行 Claude Code 会话，使用 --cloud 和 --teleport 移动会话，以及自动修复拉取请求。
- [使用例程自动化工作](https://code.claude.com/docs/zh-CN/routines.md): 让 Claude Code 自动运行。定义在计划上运行、通过 API 调用触发或对来自云基础设施的 GitHub 事件做出反应的例程。
- [使用 Ultrareview 查找错误](https://code.claude.com/docs/zh-CN/ultrareview.md): 使用 /code-review ultra 在云中运行深度多代理代码审查，在合并前查找和验证错误。

##### Claude Code 桌面版

- [开始使用桌面应用](https://code.claude.com/docs/zh-CN/desktop-quickstart.md): 在桌面上安装 Claude Code 并开始您的第一个编码会话
- [Desktop application](https://code.claude.com/docs/zh-CN/desktop.md): 充分利用 Claude Code Desktop：使用 Git 隔离的并行会话、拖放窗格布局、集成终端和文件编辑器、侧边聊天、计算机使用、从手机 Dispatch 会话、可视化 diff 审查、应用预览、PR 监控、连接器和企业配置。
- [Linux 上的 Claude Desktop（测试版）](https://code.claude.com/docs/zh-CN/desktop-linux.md): 在 Ubuntu 和 Debian 上安装和更新 Claude 桌面应用
- [Claude Code Desktop 在 WSL 中](https://code.claude.com/docs/zh-CN/desktop-wsl.md): 在 Windows 上的 WSL 2 发行版内运行 Code 会话
- [在 Claude Code Desktop 中安排定期任务](https://code.claude.com/docs/zh-CN/desktop-scheduled-tasks.md): 在 Claude Code Desktop 中设置定期任务，以定期自动运行 Claude 进行日常代码审查、依赖项审计或早晨简报。
- [在模拟器中测试 iOS 应用](https://code.claude.com/docs/zh-CN/desktop-ios-simulator.md): Claude Code Desktop 在 Claude 构建、运行或检查应用时，会在 iOS Simulator 窗格中打开你的应用，每个会话都有一个单独的模拟器。

##### 代码审查与 CI/CD

- [在 Claude 编写代码时捕获安全问题](https://code.claude.com/docs/zh-CN/security-guidance.md): 安装 security-guidance 插件，让 Claude 在编写代码时自动审查其代码更改中的漏洞，并在同一会话中修复这些问题。
- [扫描代码库中的漏洞](https://code.claude.com/docs/zh-CN/claude-security.md): 安装 Claude Security 插件以在 Claude Code 会话中扫描代码库中的漏洞，并将发现的问题转化为您可以审查和应用的补丁。
- [Code Review](https://code.claude.com/docs/zh-CN/code-review.md): 设置自动化 PR 审查，通过对完整代码库的多代理分析来捕获逻辑错误、安全漏洞和回归问题
- [Claude Code GitHub Actions](https://code.claude.com/docs/zh-CN/github-actions.md): 在 GitHub Actions 工作流中运行 Claude Code，响应 @claude 提及、自动化任务并将 issue 转换为拉取请求
- [通过云提供商使用 Claude Code GitHub Actions](https://code.claude.com/docs/zh-CN/github-actions-cloud-providers.md): 通过 Amazon Bedrock、Google Cloud 的 Agent Platform 或 Microsoft Foundry 而不是 Claude API 运行 Claude Code GitHub Actions
- [Claude Code 与 GitHub Enterprise Server](https://code.claude.com/docs/zh-CN/github-enterprise-server.md): 将 Claude Code 连接到自托管的 GitHub Enterprise Server 实例，用于云会话、代码审查和插件市场。
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/zh-CN/gitlab-ci-cd.md): 了解如何将 Claude Code 集成到您的 GitLab CI/CD 开发工作流中

### 使用 Claude Code 构建

#### 代理和并行工作

- [并行运行代理](https://code.claude.com/docs/zh-CN/agents.md): 比较 Claude Code 同时处理多个任务的方式：子代理、代理视图、代理团队、动态工作流和项目。
- [创建自定义 subagents](https://code.claude.com/docs/zh-CN/sub-agents.md): 在 Claude Code 中创建和使用专门的 AI subagents，用于特定任务的工作流和改进的上下文管理。
- [使用 agent view 管理多个代理](https://code.claude.com/docs/zh-CN/agent-view.md): 从一个屏幕调度和管理多个 Claude Code 会话。Agent view 显示每个会话正在做什么以及哪些会话需要你的输入。
- [协调 Claude Code 会话团队](https://code.claude.com/docs/zh-CN/agent-teams.md): 协调多个 Claude Code 实例作为一个团队一起工作，具有共享任务、代理间消息传递和集中管理。
- [消息传递到您的其他 Claude Code 会话](https://code.claude.com/docs/zh-CN/cross-session-messaging.md): 让 Claude 列出并消息传递到您在此机器上的其他 Claude Code 会话，并到达您在其他机器或网络上的会话。
- [使用动态工作流大规模编排子代理](https://code.claude.com/docs/zh-CN/workflows.md): 动态工作流从 Claude 编写的脚本中编排许多子代理，您可以重新运行。用于代码库审计、大型迁移和交叉检查研究。
- [使用 worktrees 运行并行会话](https://code.claude.com/docs/zh-CN/worktrees.md): 在单独的 git worktrees 中隔离并行 Claude Code 会话，以便更改不会相互冲突。涵盖 `--worktree` 标志、子代理隔离、`.worktreeinclude`、清理和非 git VCS hooks。

#### MCP

- [连接到 MCP 服务器](https://code.claude.com/docs/zh-CN/mcp-quickstart.md): 将 MCP 服务器添加到 Claude Code，验证连接，并在磁盘上找到配置。
- [通过 MCP 将 Claude Code 连接到工具](https://code.claude.com/docs/zh-CN/mcp.md): 了解如何使用 Model Context Protocol 将 Claude Code 连接到您的工具。

#### 技能

- [使用 skills 扩展 Claude](https://code.claude.com/docs/zh-CN/skills.md): 创建、管理和共享 skills 以在 Claude Code 中扩展 Claude 的功能。包括自定义命令和捆绑的 skills。

#### 插件

- [通过市场发现和安装预构建插件](https://code.claude.com/docs/zh-CN/discover-plugins.md): 从市场发现和安装插件，以使用新 skills、agents 和功能扩展 Claude Code。
- [创建插件](https://code.claude.com/docs/zh-CN/plugins.md): 创建自定义插件以使用 skills、agents、hooks 和 MCP servers 扩展 Claude Code。
- [使用 evals 测试插件](https://code.claude.com/docs/zh-CN/plugin-evals.md): 为您的 Claude Code 插件编写 eval 用例，使用 claude plugin eval 运行它们，对结果进行评分，与无插件基线进行比较，并在 CI 中基于分数进行门控。

#### 制品

- [将会话输出作为 artifacts 共享](https://code.claude.com/docs/zh-CN/artifacts.md): Artifacts 将 Claude Code 的工作转化为 claude.ai 上的实时交互式页面，您可以将其保持私密、与您的组织共享或发布到公开链接。

#### 自动化

- [使用 hooks 自动化操作](https://code.claude.com/docs/zh-CN/hooks-guide.md): 当 Claude Code 编辑文件、完成任务或需要输入时自动运行 shell 命令。格式化代码、发送通知、验证命令并强制执行项目规则。
- [使用 channels 将事件推送到运行中的会话](https://code.claude.com/docs/zh-CN/channels.md): 使用 channels 从 MCP 服务器将消息、警报和 webhooks 推送到您的 Claude Code 会话中。转发 CI 结果、聊天消息和监控事件，以便 Claude 在您离开时做出反应。
- [按计划运行提示词](https://code.claude.com/docs/zh-CN/scheduled-tasks.md): 使用 /loop 和 cron 调度工具在 Claude Code 会话中重复运行提示词、轮询状态或设置一次性提醒。
- [让 Claude 朝着目标工作](https://code.claude.com/docs/zh-CN/goal.md): 使用 /goal 设置完成条件，Claude 会持续工作直到条件满足、模型判断其不可能实现或需要修复的错误清除目标。
- [以编程方式运行 Claude Code](https://code.claude.com/docs/zh-CN/headless.md): 使用 Agent SDK 从 CLI、Python 或 TypeScript 以编程方式运行 Claude Code。
- [从链接启动会话](https://code.claude.com/docs/zh-CN/deep-links.md): 从 URL 打开 Claude Code 终端会话。在运行手册、警报和仪表板中嵌入 `claude-cli://` 链接，这样点击即可在正确的仓库中打开 Claude Code，并使用正确的提示。

#### 指南

- [在 monorepo 或大型代码库中设置 Claude Code](https://code.claude.com/docs/zh-CN/large-codebases.md): 为 monorepo 和大型单树代码库配置 Claude Code，使用嵌套的 CLAUDE.md 文件、稀疏 worktrees、代码智能和按包技能，使 Claude 专注于你正在处理的代码。

#### 故障排除

- [排查安装和登录问题](https://code.claude.com/docs/zh-CN/troubleshoot-install.md): 修复安装或登录 Claude Code 时出现的命令未找到、PATH、权限、网络和身份验证错误。
- [故障排除](https://code.claude.com/docs/zh-CN/troubleshooting.md): 修复 Claude Code 中的高 CPU 或内存使用、挂起、自动压缩抖动和搜索问题，并找到其他问题的正确页面。
- [调试你的配置](https://code.claude.com/docs/zh-CN/debug-your-config.md): 诊断为什么 CLAUDE.md、settings、hooks、MCP 服务器或 skills 没有生效。使用 /context、/doctor、/hooks 和 /mcp 来查看实际加载了什么。
- [错误参考](https://code.claude.com/docs/zh-CN/errors.md): 查找 Claude Code 运行时错误消息，了解每个错误的含义以及如何修复。

### 管理

#### 设置和访问

- [为您的组织设置 Claude Code](https://code.claude.com/docs/zh-CN/admin-setup.md): 针对部署 Claude Code 的管理员的决策地图，涵盖 API 提供商、托管设置、策略执行、使用情况监控和数据处理。
- [高级设置](https://code.claude.com/docs/zh-CN/setup.md): Claude Code 的系统要求、特定平台安装、版本管理和卸载。
- [身份验证](https://code.claude.com/docs/zh-CN/authentication.md): 登录 Claude Code 并为个人、团队和组织配置身份验证。
- [部署托管设置](https://code.claude.com/docs/zh-CN/managed-settings.md): 将托管设置部署到每个开发者的机器上：按操作系统的交付机制、Claude Code 如何组合托管源，以及如何验证强制执行。
- [配置服务器管理的设置](https://code.claude.com/docs/zh-CN/server-managed-settings.md): 通过服务器交付的设置为您的组织集中配置 Claude Code，无需设备管理基础设施。
- [控制组织的 MCP 服务器访问权限](https://code.claude.com/docs/zh-CN/managed-mcp.md): 使用托管配置文件、托管设置、允许列表和拒绝列表，限制用户可以添加或连接的 MCP 服务器，或为每个用户提供服务器。
- [配置自动模式](https://code.claude.com/docs/zh-CN/auto-mode-config.md): 告诉自动模式分类器您的组织信任哪些代码库、存储桶和域。设置环境上下文，覆盖默认的阻止和允许规则，并使用自动模式 CLI 子命令检查您的有效配置。

#### 部署

- [企业部署概览](https://code.claude.com/docs/zh-CN/third-party-integrations.md): 了解 Claude Code 如何与各种第三方服务和基础设施集成，以满足企业部署需求。
- [功能可用性](https://code.claude.com/docs/zh-CN/feature-availability.md): 比较 Claude Code 功能在 Anthropic 订阅计划、Anthropic Console、Amazon Bedrock、AWS 上的 Claude Platform、Google Cloud 的 Agent Platform 和 Microsoft Foundry 中的可用性。
- [Amazon Bedrock 上的 Claude Code](https://code.claude.com/docs/zh-CN/amazon-bedrock.md): 了解如何通过 Amazon Bedrock 配置 Claude Code，包括设置、IAM 配置和故障排除。
- [AWS 上的 Claude Platform 中的 Claude Code](https://code.claude.com/docs/zh-CN/claude-platform-on-aws.md): 配置 Claude Code 以使用 Anthropic 运营的 Claude API，支持 AWS 身份验证、IAM 访问控制和 AWS Marketplace 计费。
- [Google Cloud 的 Agent Platform 上的 Claude Code](https://code.claude.com/docs/zh-CN/google-vertex-ai.md): 了解如何通过 Google Cloud 的 Agent Platform（原 Vertex AI）配置 Claude Code，包括设置、IAM 配置和故障排除。
- [Microsoft Foundry 上的 Claude Code](https://code.claude.com/docs/zh-CN/microsoft-foundry.md): 了解如何通过 Microsoft Foundry 配置 Claude Code，包括设置、配置和故障排除。
- [企业网络配置](https://code.claude.com/docs/zh-CN/network-config.md): 为企业环境配置 Claude Code，支持代理服务器、自定义证书颁发机构 (CA) 和相互传输层安全 (mTLS) 身份验证。
- [在企业启动器后面运行 Claude Code](https://code.claude.com/docs/zh-CN/corporate-launcher.md): 通过 CLAUDE_CODE_PROCESS_WRAPPER 或 processWrapper 设置，使用必需的启动器路由 Claude Code 从其自身二进制文件启动的进程，包括后台服务和每个代理视图会话。
- [开发容器](https://code.claude.com/docs/zh-CN/devcontainer.md): 在开发容器中运行 Claude Code，为您的团队提供一致、隔离的环境。

#### 网关

- [通过网关运行 Claude Code](https://code.claude.com/docs/zh-CN/gateways.md): 通过自托管网关路由 Claude Code，实现集中式凭证管理、使用情况跟踪和成本控制。涵盖架构、Anthropic 的 Claude 应用网关以及使用其他网关产品。

##### Claude 应用网关

- [Amazon Bedrock、Claude Platform on AWS、Google Cloud 和 Microsoft Foundry 的 Claude 应用网关](https://code.claude.com/docs/zh-CN/claude-apps-gateway.md): 通过自托管网关在 Amazon Bedrock、Claude Platform on AWS、Google Cloud 或 Microsoft Foundry 上运行 Claude Code，支持 SSO 登录、按组模型访问和 OTLP 遥测。
- [Claude 应用网关配置](https://code.claude.com/docs/zh-CN/claude-apps-gateway-config.md): 每个 gateway.yaml 选项的参考：监听器和 TLS、OIDC、会话、Postgres 存储、Amazon Bedrock、Claude Platform on AWS、Google Cloud 的 Agent Platform 和 Microsoft Foundry 上游、模型路由、托管策略和遥测。
- [Claude 应用网关支出限制](https://code.claude.com/docs/zh-CN/claude-apps-gateway-spend-limits.md): 通过 Claude 应用网关为每个开发者按天、周或月设置支出上限。使用 Admin API 设置限制，网关在每个请求上实时执行这些限制。
- [Claude 应用网关部署和运维](https://code.claude.com/docs/zh-CN/claude-apps-gateway-deploy.md): 向身份提供商注册网关，构建容器，在 Kubernetes 或 Cloud Run 上部署，并运维它：健康检查、密钥轮换、升级和安全。
- [在 AWS 上部署 Claude apps gateway](https://code.claude.com/docs/zh-CN/claude-apps-gateway-on-aws.md): 在 AWS 上运行 Claude apps gateway 的完整示例：ECS Fargate 或 EKS、Amazon RDS for PostgreSQL、AWS Secrets Manager 和 IAM 角色身份验证到 Amazon Bedrock。
- [在 Google Cloud 上部署 Claude apps gateway](https://code.claude.com/docs/zh-CN/claude-apps-gateway-on-gcp.md): 在 Google Cloud 上运行 Claude apps gateway 的实际示例：Cloud Run 或 GKE、Cloud SQL for PostgreSQL、Secret Manager 和 Google Cloud 的 Agent Platform 的服务账户身份验证。

##### 其他网关

- [其他 LLM 网关](https://code.claude.com/docs/zh-CN/llm-gateway.md): 通过您的组织已运行的 LLM 网关路由 Claude Code。涵盖将 Claude Code 连接到网关、为您的组织部署网关以及 Claude Code 发送到网关的内容。
- [将 Claude Code 连接到 LLM 网关](https://code.claude.com/docs/zh-CN/llm-gateway-connect.md): 将 Claude Code 指向您组织的 LLM 网关。检查您的管理员是否已配置它，或自行设置基础 URL 和凭证，然后验证连接并修复网关错误。
- [为您的组织推出 LLM 网关](https://code.claude.com/docs/zh-CN/llm-gateway-rollout.md): 为 Claude Code 部署网关产品：配置它以转发 Claude Code 发送的内容，颁发开发者凭证，通过托管设置分发配置，并验证推出。
- [Claude Code 网关兼容性指南](https://code.claude.com/docs/zh-CN/llm-gateway-protocol.md): 保持 LLM 网关与 Claude Code 兼容：它调用的端点、必须转发的标头和正文字段，以及删除它们时会破坏的功能。

#### 使用情况和成本

- [监控](https://code.claude.com/docs/zh-CN/monitoring-usage.md): 了解如何为 Claude Code 启用和配置 OpenTelemetry。
- [有效管理成本](https://code.claude.com/docs/zh-CN/costs.md): 跟踪令牌使用情况，设置团队支出限制，并通过上下文管理、模型选择、扩展思考设置和预处理 hooks 来降低 Claude Code 成本。
- [使用分析跟踪团队使用情况](https://code.claude.com/docs/zh-CN/analytics.md): 在分析仪表板中查看 Claude Code 使用指标、跟踪采用情况并衡量工程速度。

#### 插件分发

- [创建和分发 plugin marketplace](https://code.claude.com/docs/zh-CN/plugin-marketplaces.md): 构建和托管 plugin marketplace，以在团队和社区中分发 Claude Code 扩展。
- [约束插件依赖版本](https://code.claude.com/docs/zh-CN/plugin-dependencies.md): 在插件依赖上声明版本约束，并将精选插件集合捆绑在一个安装后面。
- [从您的 CLI 推荐您的插件](https://code.claude.com/docs/zh-CN/plugin-hints.md): 从您的 CLI 发出一行标记，以便 Claude Code 提示用户安装您的官方插件。
- [为您的组织推荐插件](https://code.claude.com/docs/zh-CN/plugin-relevance.md): 向marketplace插件条目添加relevance块，以便当用户的工作与之匹配时，Claude Code会建议他们安装。

#### 安全和数据

- [安全性](https://code.claude.com/docs/zh-CN/security.md): 了解 Claude Code 的安全防护措施和安全使用的最佳实践。
- [数据使用](https://code.claude.com/docs/zh-CN/data-usage.md): 了解 Anthropic 对 Claude 数据使用的政策
- [零数据保留](https://code.claude.com/docs/zh-CN/zero-data-retention.md): 了解 Claude for Enterprise 上 Claude Code 的零数据保留 (ZDR)，包括范围、禁用功能以及如何请求启用。

#### 采用

- [通信工具包](https://code.claude.com/docs/zh-CN/communications-kit.md): 推出公告、滴灌式营销信息和常见问题解答，用于在您的工程组织中推出 Claude Code。
- [Champion kit](https://code.claude.com/docs/zh-CN/champion-kit.md): 工程师在内部倡导 Claude Code 的行动手册：分享什么、如何回答问题以及如何在团队中推动采用。

### 配置

#### 设置

- [设置文件和优先级](https://code.claude.com/docs/zh-CN/settings.md): 更改 Claude Code 设置，选择键所属的作用域，验证更改，并了解当键在多个位置设置时 Claude Code 使用哪个值。
- [所有设置](https://code.claude.com/docs/zh-CN/settings-reference.md): Claude Code settings.json 的完整参考：每个键的位置、类型和默认值，以及可直接粘贴的示例，包含每个键的索引。
- [示例设置文件](https://code.claude.com/docs/zh-CN/settings-example.md): 为开发者、团队和组织提供的现实 settings.json 文件：复制一个，保留你想要的键，并更改值。

#### 权限和沙箱隔离

- [配置权限](https://code.claude.com/docs/zh-CN/permissions.md): 通过细粒度权限规则、模式和托管策略来控制 Claude Code 可以访问和执行的操作。
- [选择权限模式](https://code.claude.com/docs/zh-CN/permission-modes.md): 控制 Claude 在采取行动前是否需要征求您的同意。在 CLI 中使用 Shift+Tab 切换权限模式，在 VS Code 中使用模式指示器，或在 Desktop 中使用模式选择器。
- [配置沙箱化 Bash 工具](https://code.claude.com/docs/zh-CN/sandboxing.md): 了解 Claude Code 的沙箱化 Bash 工具如何提供文件系统和网络隔离，以实现更安全、更自主的代理执行。
- [选择沙箱环境](https://code.claude.com/docs/zh-CN/sandbox-environments.md): 比较 Claude Code 沙箱选项：内置沙箱化 Bash 工具、沙箱运行时、开发容器、Docker 和虚拟机。为您的威胁模型选择合适的隔离方案。

#### 环境

- [配置云环境](https://code.claude.com/docs/zh-CN/cloud-environments.md): 为 Claude Code 云会话配置云环境：网络访问级别、环境变量、设置脚本和环境缓存。

##### 自托管环境

- [自托管环境](https://code.claude.com/docs/zh-CN/self-hosted-environments.md): 在您控制的基础设施上运行 Claude Code 云会话：设置自托管环境、部署运行器，并将会话路由到您自己的计算资源。
- [自托管环境快速入门](https://code.claude.com/docs/zh-CN/self-hosted-environments-quickstart.md): 设置您的第一个自托管环境：安装 Claude Code、创建环境、启动运行器，并将会话路由到该环境。
- [将自托管环境部署到生产环境](https://code.claude.com/docs/zh-CN/self-hosted-environments-deploy.md): 在生产环境中运行自托管运行器：安全加固、网络出站流量控制、git 凭证、Kubernetes 和 Compose 配方以及故障排除。
- [在自托管环境中自定义会话](https://code.claude.com/docs/zh-CN/self-hosted-environments-configuration.md): 使用包装脚本在自托管环境会话中自定义每个会话的凭证、生命周期钩子和按需运行程序生成。
- [端到端测试自托管环境](https://code.claude.com/docs/zh-CN/self-hosted-environments-testing.md): 从 CI 验证自托管运行器镜像：使用 CLI 分派会话，通过 Stop hook 读取 Claude 的回复，并编写完整循环脚本。
- [自托管环境参考](https://code.claude.com/docs/zh-CN/self-hosted-environments-reference.md): 自托管运行器和编排器的完整参考：CLI 标志、环境变量和 Prometheus 指标。
- [在自托管环境中验证会话身份](https://code.claude.com/docs/zh-CN/self-hosted-environments-identity.md): 验证 CLAUDE_CODE_SESSION_ACCESS_TOKEN JWT，以便网络上的服务可以信任来自自托管环境中会话的请求。

#### 模型和响应

- [模型配置](https://code.claude.com/docs/zh-CN/model-config.md): 配置 Claude Code 使用的模型、工作量级别、扩展上下文和自动压缩窗口
- [使用快速模式加快响应速度](https://code.claude.com/docs/zh-CN/fast-mode.md): 通过切换快速模式在 Claude Code 中获得更快的 Opus 响应。
- [使用顾问工具升级困难决策](https://code.claude.com/docs/zh-CN/advisor.md): 将您的主模型与更强大的顾问模型配对，Claude 在任务期间的关键时刻咨询该模型。
- [输出样式](https://code.claude.com/docs/zh-CN/output-styles.md): 将 Claude Code 适配用于软件工程之外的用途

#### 界面

- [为 Claude Code 配置您的终端](https://code.claude.com/docs/zh-CN/terminal-config.md): 修复 Shift+Enter 以插入新行、在 Claude 完成时获得终端铃声、配置 tmux、匹配颜色主题，以及在 Claude Code CLI 中启用 Vim 模式。
- [全屏渲染](https://code.claude.com/docs/zh-CN/fullscreen.md): 启用更流畅、无闪烁的渲染模式，支持鼠标操作，在长对话中保持稳定的内存使用。
- [使用 Claude Code 与屏幕阅读器](https://code.claude.com/docs/zh-CN/accessibility.md): 为 VoiceOver 和 NVDA 等屏幕阅读器设置 Claude Code，以及屏幕放大镜、减少动画和色盲友好主题的设置。
- [语音听写](https://code.claude.com/docs/zh-CN/voice-dictation.md): 在 Claude Code CLI 中使用按住录音或点击录音的语音听写功能来说出你的提示词。
- [自定义你的状态行](https://code.claude.com/docs/zh-CN/statusline.md): 配置自定义状态栏以监控 Claude Code 中的上下文窗口使用情况、成本和 git 状态
- [自定义快捷键](https://code.claude.com/docs/zh-CN/keybindings.md): 使用快捷键配置文件在 Claude Code 中自定义快捷键。

### 参考

#### 参考

- [CLI 参考](https://code.claude.com/docs/zh-CN/cli-reference.md): Claude Code 命令行界面的完整参考，包括命令和标志。
- [Commands](https://code.claude.com/docs/zh-CN/commands.md): Claude Code 中可用命令的完整参考，包括内置命令和捆绑的 skills。
- [环境变量](https://code.claude.com/docs/zh-CN/env-vars.md): 控制 Claude Code 行为的环境变量参考。
- [工具参考](https://code.claude.com/docs/zh-CN/tools-reference.md): Claude Code 可以使用的工具的完整参考，包括权限要求和每个工具的行为。
- [交互模式](https://code.claude.com/docs/zh-CN/interactive-mode.md): Claude Code 会话中键盘快捷键、输入模式和交互功能的完整参考。
- [Checkpointing](https://code.claude.com/docs/zh-CN/checkpointing.md): 跟踪、回溯和总结 Claude 的编辑和对话以管理会话状态。
- [Hooks 参考](https://code.claude.com/docs/zh-CN/hooks.md): Claude Code hook 事件、配置架构、JSON 输入/输出格式、退出代码、异步 hooks、HTTP hooks、提示 hooks 和 MCP 工具 hooks 的参考。
- [Plugins 参考](https://code.claude.com/docs/zh-CN/plugins-reference.md): Claude Code 插件系统的完整技术参考，包括模式、CLI 命令和组件规范。
- [Channels 参考](https://code.claude.com/docs/zh-CN/channels-reference.md): 构建一个 MCP 服务器，将 webhooks、警报和聊天消息推送到 Claude Code 会话中。频道合约的参考：能力声明、通知事件、回复工具、发送者门控和权限中继。

#### 术语表

- [术语表](https://code.claude.com/docs/zh-CN/glossary.md): Claude Code 术语定义。了解 agentic loop、compaction、CLAUDE.md、hooks、subagents、MCP 和其他核心概念的含义。

### Agent SDK

#### Agent SDK

- [Agent SDK 概览](https://code.claude.com/docs/zh-CN/agent-sdk/overview.md): 使用 Claude Code 作为库构建生产级 AI 代理
- [快速开始](https://code.claude.com/docs/zh-CN/agent-sdk/quickstart.md): 使用 Python 或 TypeScript Agent SDK 开始构建能够自主工作的 AI 代理
- [迁移到 Claude Agent SDK](https://code.claude.com/docs/zh-CN/agent-sdk/migration-guide.md): 将 Claude Code TypeScript 和 Python SDK 迁移到 Claude Agent SDK 的指南
- [Agent SDK 故障排除](https://code.claude.com/docs/zh-CN/agent-sdk/troubleshooting.md): 通过您看到的确切错误消息修复 Agent SDK 错误，包括 TypeScript 和 Python SDK 中每个错误的原因和修复方法。

#### 构建代理

- [配置你的代理](https://code.claude.com/docs/zh-CN/agent-sdk/configuration.md): 配置 Agent SDK 会话：组合选项对象、设置模型、环境和限制，并找到每个功能选项的页面。
- [示例](https://code.claude.com/docs/zh-CN/agent-sdk/examples.md): 查找完整的、可运行的 Agent SDK 项目或 Claude Cookbook 中的指导食谱，以匹配您想要构建的内容。

#### 核心概念

- [代理循环如何工作](https://code.claude.com/docs/zh-CN/agent-sdk/agent-loop.md): 了解消息生命周期、工具执行、上下文窗口和支持 SDK 代理的架构。
- [在 SDK 中使用 Claude Code 功能](https://code.claude.com/docs/zh-CN/agent-sdk/claude-code-features.md): 将项目说明、skills、hooks 和其他 Claude Code 功能加载到您的 SDK 代理中。
- [使用会话](https://code.claude.com/docs/zh-CN/agent-sdk/sessions.md): 会话如何保持代理对话历史记录，以及何时使用 continue、resume 和 fork 返回到之前的运行。
- [将会话持久化到外部存储](https://code.claude.com/docs/zh-CN/agent-sdk/session-storage.md): 将 Agent SDK 会话记录镜像到您自己的对象存储、键值存储或数据库，以便其他主机可以恢复您的会话。

#### 输入和输出

- [流式输入](https://code.claude.com/docs/zh-CN/agent-sdk/streaming-vs-single-mode.md): 理解 Claude Agent SDK 的两种输入模式及何时使用每种模式
- [处理批准和用户输入](https://code.claude.com/docs/zh-CN/agent-sdk/user-input.md): 向用户显示 Claude 的批准请求和澄清问题，然后将他们的决定返回给 SDK。
- [实时流式传输响应](https://code.claude.com/docs/zh-CN/agent-sdk/streaming-output.md): 当文本和工具调用流入时，从 Agent SDK 获取实时响应
- [从代理获取结构化输出](https://code.claude.com/docs/zh-CN/agent-sdk/structured-outputs.md): 使用 JSON Schema、Zod 或 Pydantic 从代理工作流返回验证的 JSON。在多轮工具使用后获取类型安全的结构化数据。

#### 使用工具扩展

- [为 Claude 提供自定义工具](https://code.claude.com/docs/zh-CN/agent-sdk/custom-tools.md): 使用 Claude Agent SDK 的进程内 MCP 服务器定义自定义工具，以便 Claude 可以调用您的函数、访问您的 API 并执行特定领域的操作。
- [使用 MCP 连接外部工具](https://code.claude.com/docs/zh-CN/agent-sdk/mcp.md): 配置 MCP 服务器以扩展您的代理的外部工具。涵盖传输类型、大型工具集的工具搜索、身份验证和错误处理。
- [使用工具搜索扩展到多个工具](https://code.claude.com/docs/zh-CN/agent-sdk/tool-search.md): 通过动态发现和按需加载，将您的代理扩展到数千个工具。
- [SDK 中的子代理](https://code.claude.com/docs/zh-CN/agent-sdk/subagents.md): 定义和调用子代理以隔离上下文、并行运行任务，以及在 Claude Agent SDK 应用程序中应用专门的指令。

#### 自定义行为

- [修改系统提示词](https://code.claude.com/docs/zh-CN/agent-sdk/modifying-system-prompts.md): 在 `claude_code` 预设和自定义系统提示词之间进行选择，并通过 CLAUDE.md、输出样式、追加或完全自定义提示词来自定义行为。
- [使用 skills 扩展 agents](https://code.claude.com/docs/zh-CN/agent-sdk/skills.md): 控制 Claude 在 Claude Agent SDK 会话中可以调用哪些 skills，按名称分派命令，以及编写会话发现的 skills
- [SDK 中的 Plugins](https://code.claude.com/docs/zh-CN/agent-sdk/plugins.md): 通过 Agent SDK 加载自定义 plugins，以向 agent 会话添加 skills、agents、hooks 和 MCP servers

#### 控制和可观测性

- [配置权限](https://code.claude.com/docs/zh-CN/agent-sdk/permissions.md): 使用权限模式、hooks 和声明式允许/拒绝规则来控制您的代理如何使用工具。
- [使用 hooks 拦截和控制代理行为](https://code.claude.com/docs/zh-CN/agent-sdk/hooks.md): 在代理执行的关键点使用 hooks 拦截和自定义代理行为
- [使用checkpointing回滚文件更改](https://code.claude.com/docs/zh-CN/agent-sdk/file-checkpointing.md): 在agent会话期间跟踪文件更改，并将文件恢复到任何之前的状态
- [追踪成本和使用情况](https://code.claude.com/docs/zh-CN/agent-sdk/cost-tracking.md): 了解如何追踪令牌使用情况、估算成本，以及使用 Claude Agent SDK 配置 prompt caching。
- [使用 OpenTelemetry 进行可观测性](https://code.claude.com/docs/zh-CN/agent-sdk/observability.md): 使用 OpenTelemetry 将来自 Agent SDK 的跟踪、指标和事件导出到您的可观测性后端。
- [跟踪待办事项](https://code.claude.com/docs/zh-CN/agent-sdk/todo-tracking.md): 在 Agent SDK 会话中跟踪待办事项，并从结构化工具调用中呈现 Claude 的进度

#### 部署

- [托管 Agent SDK](https://code.claude.com/docs/zh-CN/agent-sdk/hosting.md): 在生产环境中部署 Agent SDK：子进程架构、会话持久化、扩展、可观测性以及针对 Docker、Kubernetes 和沙箱提供商的多租户隔离。
- [安全部署 AI 代理](https://code.claude.com/docs/zh-CN/agent-sdk/secure-deployment.md): 关于使用隔离、凭证管理和网络控制来保护 Claude Code 和 Agent SDK 部署的指南

#### SDK 参考

- [Agent SDK 参考 - TypeScript](https://code.claude.com/docs/zh-CN/agent-sdk/typescript.md): TypeScript Agent SDK 的完整 API 参考，包括所有函数、类型和接口。
- [TypeScript SDK V2 session API（已移除）](https://code.claude.com/docs/zh-CN/agent-sdk/typescript-v2-preview.md): 已移除的 V2 TypeScript Agent SDK session API 参考，具有用于多轮对话的基于会话的 send/stream 模式。
- [Agent SDK 参考 - Python](https://code.claude.com/docs/zh-CN/agent-sdk/python.md): Python Agent SDK 的完整 API 参考，包括所有函数、类型和类。

### 最新动态

#### 最新动态

- [最新动态](https://code.claude.com/docs/zh-CN/whats-new/index.md): Claude Code 功能的每周摘要，包含代码片段、演示和背景信息，说明为什么这些功能很重要。
- [第37周 · 2026年9月7日–11日](https://code.claude.com/docs/zh-CN/whats-new/2026-w37.md): 使用 claude plugin eval 测试您的插件，并将 Claude Code Desktop 窗格弹出到各自的窗口中。
- [第 36 周 · 8 月 31 日 – 9 月 4 日，2026 年](https://code.claude.com/docs/zh-CN/whats-new/2026-w36.md): 切换到 Claude Fable 5.1，让计算机使用在 Desktop 上后台运行，并在实时 /diff 面板中观看 Claude 的编辑。
- [第 35 周 · 2026 年 8 月 24–28 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w35.md): 在 Claude Code Desktop 应用中恢复终端会话，查看 Claude 为您起草的反馈报告，并在受限模式下启动会话。
- [第 34 周 · 2026 年 8 月 17–21 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w34.md): 使用 /design skill 草拟可编辑的 UI 画板，设置 Concise 输出样式，并从手机在您的机器上启动 Claude Code 会话。
- [第 33 周 · 2026 年 8 月 10–14 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w33.md): Claude Code Desktop 在使用限制重置后自动继续，fork 模式默认启用，GitLab 合并请求和市场加入 GitHub。
- [第 32 周 · 2026 年 8 月 3–7 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w32.md): Claude Code 会话可以相互发送消息，自托管环境在您的基础设施上运行云会话，自动模式成为默认权限模式。
- [第 30 周 · 7 月 20–24 日，2026 年](https://code.claude.com/docs/zh-CN/whats-new/2026-w30.md): Opus 5 成为默认的 Opus 模型，Claude Code Desktop 添加了 iOS 模拟器窗格，Claude Security 插件扫描您的代码以查找漏洞。
- [第29周 · 2026年7月13–17日](https://code.claude.com/docs/zh-CN/whats-new/2026-w29.md): 通过MCP连接器将实时数据拉入已发布的工件中，并在新的屏幕阅读器模式下使用Claude Code。
- [第 28 周 · 2026 年 7 月 6–10 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w28.md): 从 Desktop 应用的内置浏览器浏览外部网站，使用 /doctor 运行完整的设置检查，并获取自动模式的文本记录保护和代理视图升级。
- [第 27 周 · 6 月 29 日 – 7 月 3 日，2026 年](https://code.claude.com/docs/zh-CN/whats-new/2026-w27.md): Claude Sonnet 5 成为默认模型，Claude in Chrome 正式推出，子代理默认在后台运行，Claude Desktop 在 Linux 上推出测试版，/radio 调入 Claude FM。
- [第 26 周 · 2026 年 6 月 22–26 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w26.md): 使用 claude mcp login 从 shell 中对 MCP 服务器进行身份验证，使用 ! 前缀获取对 shell 模式命令输出的响应，以及使用 /rewind 从 /clear 之前恢复对话。
- [第 25 周 · 2026 年 6 月 15–19 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w25.md): 从您的会话中使用 Artifacts 发布实时可共享页面，在拒绝和询问规则中匹配工具参数，以及使用 /config 从提示中设置任何设置。
- [第24周 · 2026年6月8日–12日](https://code.claude.com/docs/zh-CN/whats-new/2026-w24.md): 使用 /cd 将会话移动到新目录，让子代理生成自己的子代理，并使用安全模式排查损坏的配置。
- [第 23 周 · 2026 年 6 月 1–5 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w23.md): 在 Amazon Bedrock、Google Cloud 的 Agent Platform 和 Microsoft Foundry 上运行自动模式，在 acceptEdits 模式下提示写入可运行代码的文件，使用 /plugin list 列出已安装的插件，以及为托管部署要求批准的版本范围。
- [第 22 周 · 2026 年 5 月 25–29 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w22.md): 在 Claude Opus 4.8 上运行 Claude Code，使用动态工作流编排大型任务，使用 security-guidance 插件捕获安全问题，并以更低的价格在 Opus 4.8 上使用快速模式。
- [第 21 周 · 2026 年 5 月 18–22 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w21.md): 在 Pro 计划上使用自动模式并支持 Sonnet 4.6，在 /usage 中查看哪些 skills、subagents 和 MCP servers 驱动您的计划限制，并使用新的 /code-review 命令查看差异。
- [第 20 周 · 2026 年 5 月 11–15 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w20.md): 从一个屏幕管理每个 Claude Code 会话，使用 agent view，让 Claude 持续朝着目标工作直到条件满足，并在 Opus 4.7 上默认运行快速模式。
- [第19周 · 2026年5月4–8日](https://code.claude.com/docs/zh-CN/whats-new/2026-w19.md): 从.zip存档和URL加载插件，使用Ctrl+R跨每个项目搜索命令历史，从本地HEAD或远程默认分支创建新worktrees，以及使用自动模式硬拒绝规则无条件阻止操作。
- [第 18 周 · 2026 年 4 月 27 日 – 5 月 1 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w18.md): Claude Code 在 Windows 上无需 Git Bash 即可运行，claude auth login 在浏览器回调无法到达 localhost 时接受粘贴的 OAuth 代码，claude project purge 清理每个项目的本地状态，将 PR URL 粘贴到 /resume 中可找到创建该会话的会话。
- [第17周 · 2026年4月20–24日](https://code.claude.com/docs/zh-CN/whats-new/2026-w17.md): /ultrareview 作为研究预览版开放，返回终端时自动生成会话摘要，可以在插件中构建和发布自定义颜色主题，以及重新设计的网页版 Claude Code。
- [第 16 周 · 2026 年 4 月 13–17 日](https://code.claude.com/docs/zh-CN/whats-new/2026-w16.md): Claude Opus 4.7 配备新的 xhigh 努力级别、Claude Code 网页版上的 Routines、移动推送通知在 Claude 需要您时 ping 您的手机、显示限制驱动因素的 /usage 分解，以及替代捆绑 JavaScript 的原生二进制文件。
- [第15周 · 2026年4月6–10日](https://code.claude.com/docs/zh-CN/whats-new/2026-w15.md): Ultraplan 云规划、具有自适应 /loop 的 Monitor 工具、用于打包设置的 /team-onboarding 以及从终端运行的 /autofix-pr。
- [第 14 周 · 3 月 30 日 – 4 月 3 日，2026 年](https://code.claude.com/docs/zh-CN/whats-new/2026-w14.md): CLI 中的计算机使用、交互式产品内课程、无闪烁渲染、按工具 MCP 结果大小覆盖以及 PATH 上的插件可执行文件。
- [第13周 · 2026年3月23–27日](https://code.claude.com/docs/zh-CN/whats-new/2026-w13.md): 自动模式用于免提权限、内置计算机使用、云端PR自动修复、转录搜索和Windows PowerShell工具。

### 资源

#### 资源

- [法律和合规](https://code.claude.com/docs/zh-CN/legal-and-compliance.md): Claude Code 的法律协议、合规认证和安全信息。

---

## Claude Code Docs: German

- 官方原文：https://code.claude.com/docs/_llms/de.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-de.md`

# Claude Code Docs: German

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## German

### Erste Schritte

#### Erste Schritte

- [Übersicht](https://code.claude.com/docs/de/overview.md): Claude Code ist ein agentengestütztes Codierungswerkzeug, das Ihre Codebasis liest, Dateien bearbeitet, Befehle ausführt und sich in Ihre Entwicklungstools integriert. Verfügbar in Ihrem Terminal, IDE, Desktop-App und Browser.
- [Schnellstart](https://code.claude.com/docs/de/quickstart.md): Willkommen bei Claude Code!
- [Changelog](https://code.claude.com/docs/de/changelog.md)

#### Kernkonzepte

- [So funktioniert Claude Code](https://code.claude.com/docs/de/how-claude-code-works.md): Verstehen Sie die agentengesteuerte Schleife, integrierte Tools und wie Claude Code mit Ihrem Projekt interagiert.
- [Claude Code erweitern](https://code.claude.com/docs/de/features-overview.md): Verstehen Sie, wann Sie CLAUDE.md, Skills, Subagents, Hooks, MCP und Plugins verwenden.
- [Erkunden Sie das .claude-Verzeichnis](https://code.claude.com/docs/de/claude-directory.md): Wo Claude Code CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules und auto memory liest. Erkunden Sie das .claude-Verzeichnis in Ihrem Projekt und ~/.claude in Ihrem Home-Verzeichnis.
- [Erkunden Sie das Kontextfenster](https://code.claude.com/docs/de/context-window.md): Eine interaktive Simulation, wie sich das Kontextfenster von Claude Code während einer Sitzung füllt. Sehen Sie, was automatisch geladen wird, welche Kosten jeder Dateilesevorgang hat, und wann Regeln und Hooks ausgelöst werden.
- [Wie Claude Code Prompt Caching nutzt](https://code.claude.com/docs/de/prompt-caching.md): Claude Code verwaltet Prompt Caching automatisch. Erfahren Sie, warum ein Modellwechsel einen langsamen unkachedten Turn auslöst, was `/compact` kostet, warum CLAUDE.md-Änderungen mid-session nicht angewendet werden, und wie Sie Ihre Cache-Hit-Rate überprüfen.

#### Claude Code verwenden

- [Wie Claude sich Ihr Projekt merkt](https://code.claude.com/docs/de/memory.md): Geben Sie Claude persistente Anweisungen mit CLAUDE.md- oder AGENTS.md-Dateien, und lassen Sie Claude automatisch Erkenntnisse mit Auto-Memory sammeln.
- [Sitzungen verwalten](https://code.claude.com/docs/de/sessions.md): Benennen, fortsetzen, verzweigen und wechseln Sie zwischen Claude Code-Gesprächen. Behandelt `--continue`, `--resume`, `--from-pr`, die `/resume`-Auswahl, Sitzungsbenennung, Exportieren von Transkripten und wo Transkripte gespeichert werden.
- [Häufige Workflows](https://code.claude.com/docs/de/common-workflows.md): Schritt-für-Schritt-Anleitungen zum Erkunden von Codebases, Beheben von Fehlern, Refaktorierung, Testen und anderen alltäglichen Aufgaben mit Claude Code.
- [Prompt-Bibliothek](https://code.claude.com/docs/de/prompt-library.md): Kopieren Sie Prompts für Claude Code, kategorisiert nach Aufgabe und Rolle.
- [Best Practices für Claude Code](https://code.claude.com/docs/de/best-practices.md): Tipps und Muster, um das Beste aus Claude Code herauszuholen – von der Konfiguration Ihrer Umgebung bis zur Skalierung über parallele Sessions.

#### Plattformen und Integrationen

- [Plattformen und Integrationen](https://code.claude.com/docs/de/platforms.md): Wählen Sie, wo Sie Claude Code ausführen möchten, und was Sie damit verbinden. Vergleichen Sie die CLI, Desktop, VS Code, JetBrains, Web und Integrationen wie Chrome, Slack und CI/CD.
- [Lokale Sitzungen von jedem Gerät aus mit Remote Control fortsetzen](https://code.claude.com/docs/de/remote-control.md): Setzen Sie eine lokale Claude Code-Sitzung von Ihrem Telefon, Tablet oder einem beliebigen Browser aus mit Remote Control fort. Funktioniert mit claude.ai/code und der Claude-Mobile-App.
- [Lassen Sie Claude laufende Arbeiten mit Projekten koordinieren](https://code.claude.com/docs/de/claude-projects.md): Geben Sie Claude einen Bestand zusammenhängender Arbeiten in einem Gespräch und lassen Sie ihn parallele Cloud-Sitzungen koordinieren, die Repositorys, Anweisungen und Speicher gemeinsam nutzen.
- [Claude Code auf Mobilgeräten](https://code.claude.com/docs/de/mobile.md): Starten, überwachen und steuern Sie Claude Code-Aufgaben von Ihrem Telefon aus mit der Claude-App für iOS und Android.
- [Claude Code mit Chrome verwenden](https://code.claude.com/docs/de/chrome.md): Verbinden Sie Claude Code mit Ihrem Chrome-Browser, um Web-Apps zu testen, mit Konsolenprotokollen zu debuggen, Formularausfüllungen zu automatisieren und Daten von Webseiten zu extrahieren.
- [Claude von der CLI aus Ihren Computer nutzen lassen](https://code.claude.com/docs/de/computer-use.md): Aktivieren Sie die Computernutzung in der Claude Code CLI, damit Claude Apps öffnen, klicken, tippen und Ihren Bildschirm auf macOS sehen kann. Testen Sie native Apps, debuggen Sie visuelle Probleme und automatisieren Sie GUI-only-Tools, ohne Ihr Terminal zu verlassen.
- [Claude Code in VS Code verwenden](https://code.claude.com/docs/de/vs-code.md): Installieren und konfigurieren Sie die Claude Code-Erweiterung für VS Code. Erhalten Sie KI-Codierungshilfe mit Inline-Diffs, @-Erwähnungen, Planüberprüfung und Tastaturkürzeln.
- [JetBrains IDEs](https://code.claude.com/docs/de/jetbrains.md): Verwenden Sie Claude Code mit JetBrains IDEs einschließlich IntelliJ, PyCharm, WebStorm und mehr
- [Claude Code in Slack](https://code.claude.com/docs/de/slack.md): Delegieren Sie Codierungsaufgaben direkt aus Ihrem Slack-Arbeitsbereich. Anthropic stellt diese frühere Version für Team- und Enterprise-Arbeitsbereiche zugunsten von Claude Tag ein; sie bleibt der Einrichtungspfad für Pro- und Max-Pläne.
- [Claude Tag](https://code.claude.com/docs/de/claude-tag.md): Bringen Sie Claude mit Claude Tag in die Slack-Kanäle Ihres Teams und finden Sie die Setup- und Nutzungsdokumentation auf claude.com.

##### Claude Code in der Cloud

- [Erste Schritte mit Claude Code in der Cloud](https://code.claude.com/docs/de/web-quickstart.md): Führen Sie Claude Code in der Cloud aus Ihrem Browser oder Telefon aus. Verbinden Sie ein GitHub-Repository, übermitteln Sie eine Aufgabe und überprüfen Sie den PR ohne lokales Setup.
- [Claude Code in der Cloud verwenden](https://code.claude.com/docs/de/claude-code-on-the-web.md): Führen Sie Claude Code-Sitzungen in der Cloud aus Ihrem Browser, Telefon, Desktop-App oder Terminal aus, verschieben Sie sie mit --cloud und --teleport, und beheben Sie Pull Requests automatisch.
- [Automatisieren Sie Arbeitsabläufe mit Routinen](https://code.claude.com/docs/de/routines.md): Setzen Sie Claude Code auf Autopilot. Definieren Sie Routinen, die nach einem Zeitplan ausgeführt werden, durch API-Aufrufe ausgelöst werden oder auf GitHub-Ereignisse von der Cloud-Infrastruktur reagieren.
- [Bugs mit Ultrareview finden](https://code.claude.com/docs/de/ultrareview.md): Führen Sie eine tiefe, Multi-Agent-Code-Review in der Cloud mit /code-review ultra durch, um Bugs vor dem Merge zu finden und zu verifizieren.

##### Claude Code auf dem Desktop

- [Erste Schritte mit der Desktop-App](https://code.claude.com/docs/de/desktop-quickstart.md): Installieren Sie Claude Code auf dem Desktop und starten Sie Ihre erste Coding-Sitzung
- [Desktop-Anwendung](https://code.claude.com/docs/de/desktop.md): Nutzen Sie Claude Code Desktop optimal: parallele Sitzungen mit Git-Isolation, Drag-and-Drop-Pane-Layout, integriertes Terminal und Datei-Editor, Seitenchats, Computernutzung, Dispatch-Sitzungen von Ihrem Telefon, visuelle Diff-Überprüfung, App-Vorschau, PR-Überwachung, Konnektoren und Unternehmensk…
- [Claude Desktop unter Linux (Beta)](https://code.claude.com/docs/de/desktop-linux.md): Installieren und aktualisieren Sie die Claude-Desktop-App unter Ubuntu und Debian
- [Claude Code Desktop in WSL](https://code.claude.com/docs/de/desktop-wsl.md): Führen Sie Code-Sitzungen in einer WSL 2-Distribution unter Windows aus
- [Wiederkehrende Aufgaben in Claude Code Desktop planen](https://code.claude.com/docs/de/desktop-scheduled-tasks.md): Richten Sie geplante Aufgaben in Claude Code Desktop ein, um Claude automatisch in regelmäßigen Abständen für tägliche Code-Reviews, Abhängigkeitsprüfungen oder morgendliche Briefings auszuführen.
- [iOS-Apps im Simulator testen](https://code.claude.com/docs/de/desktop-ios-simulator.md): Claude Code Desktop öffnet Ihre App im iOS-Simulator-Bereich, wenn Claude sie erstellt, ausführt oder überprüft. Jede Sitzung hat einen separaten Simulator.

##### Code-Review & CI/CD

- [Sicherheitsprobleme erfassen, während Claude Code schreibt](https://code.claude.com/docs/de/security-guidance.md): Installieren Sie das security-guidance-Plugin, damit Claude seine eigenen Code-Änderungen auf Sicherheitslücken überprüft und diese in derselben Sitzung behebt.
- [Scannen Sie Ihre Codebasis auf Sicherheitslücken](https://code.claude.com/docs/de/claude-security.md): Installieren Sie das Claude Security Plugin, um Ihre Codebasis in einer Claude Code-Sitzung auf Sicherheitslücken zu scannen und Erkenntnisse in Patches umzuwandeln, die Sie überprüfen und anwenden.
- [Code Review](https://code.claude.com/docs/de/code-review.md): Richten Sie automatisierte PR-Reviews ein, die Logikfehler, Sicherheitslücken und Regressionen durch Multi-Agent-Analyse Ihrer vollständigen Codebasis erkennen
- [Claude Code GitHub Actions](https://code.claude.com/docs/de/github-actions.md): Führen Sie Claude Code in GitHub Actions-Workflows aus, um auf @claude-Erwähnungen zu reagieren, Aufgaben zu automatisieren und Issues in Pull Requests umzuwandeln
- [Claude Code GitHub Actions mit Cloud-Anbietern verwenden](https://code.claude.com/docs/de/github-actions-cloud-providers.md): Führen Sie Claude Code GitHub Actions über Amazon Bedrock, Google Cloud's Agent Platform oder Microsoft Foundry statt über die Claude API aus
- [Claude Code mit GitHub Enterprise Server](https://code.claude.com/docs/de/github-enterprise-server.md): Verbinden Sie Claude Code mit Ihrer selbstgehosteten GitHub Enterprise Server-Instanz für Web-Sitzungen, Code-Review und Plugin-Marktplätze.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/de/gitlab-ci-cd.md): Erfahren Sie, wie Sie Claude Code in Ihren Entwicklungs-Workflow mit GitLab CI/CD integrieren

### Mit Claude Code erstellen

#### Agenten und parallele Arbeit

- [Agenten parallel ausführen](https://code.claude.com/docs/de/agents.md): Vergleichen Sie die Möglichkeiten, wie Claude Code mehrere Aufgaben gleichzeitig bewältigen kann: Subagenten, Agent-Ansicht, Agent-Teams, dynamische Workflows und Projekte.
- [Benutzerdefinierte Subagenten erstellen](https://code.claude.com/docs/de/sub-agents.md): Erstellen und verwenden Sie spezialisierte KI-Subagenten in Claude Code für aufgabenspezifische Workflows und verbesserte Kontextverwaltung.
- [Mehrere Agenten mit der Agenten-Ansicht verwalten](https://code.claude.com/docs/de/agent-view.md): Versenden und verwalten Sie viele Claude Code-Sitzungen von einem Bildschirm aus. Die Agenten-Ansicht zeigt, was jede Sitzung tut und welche Ihre Eingabe benötigen.
- [Orchestrieren Sie Teams von Claude Code-Sitzungen](https://code.claude.com/docs/de/agent-teams.md): Koordinieren Sie mehrere Claude Code-Instanzen, die zusammen als Team arbeiten, mit gemeinsamen Aufgaben, Messaging zwischen Agenten und zentraler Verwaltung.
- [Nachrichten an Ihre anderen Claude Code-Sitzungen](https://code.claude.com/docs/de/cross-session-messaging.md): Lassen Sie Claude Ihre anderen Claude Code-Sitzungen auf diesem Computer auflisten und anschreiben, und erreichen Sie Ihre Sitzungen auf anderen Computern oder im Web.
- [Orchestrieren Sie Subagenten im großen Maßstab mit dynamischen Workflows](https://code.claude.com/docs/de/workflows.md): Dynamische Workflows orchestrieren viele Subagenten aus einem Skript, das Claude schreibt und das Sie erneut ausführen können. Verwenden Sie sie für Codebase-Audits, große Migrationen und überprüfte Recherchen.
- [Parallele Sitzungen mit Worktrees ausführen](https://code.claude.com/docs/de/worktrees.md): Isolieren Sie parallele Claude Code-Sitzungen in separaten Git-Worktrees, damit Änderungen nicht kollidieren. Behandelt das Flag `--worktree`, Subagent-Isolation, `.worktreeinclude`, Bereinigung und Non-Git-VCS-Hooks.

#### MCP

- [Mit MCP-Servern verbinden](https://code.claude.com/docs/de/mcp-quickstart.md): Fügen Sie einen MCP-Server zu Claude Code hinzu, überprüfen Sie die Verbindung und finden Sie die Konfiguration auf der Festplatte.
- [Claude Code mit Tools über MCP verbinden](https://code.claude.com/docs/de/mcp.md): Erfahren Sie, wie Sie Claude Code mit Ihren Tools über das Model Context Protocol verbinden.

#### Skills

- [Claude mit Skills erweitern](https://code.claude.com/docs/de/skills.md): Erstellen, verwalten und teilen Sie Skills, um die Funktionen von Claude in Claude Code zu erweitern. Umfasst benutzerdefinierte Befehle und gebündelte Skills.

#### Plugins

- [Entdecken und installieren Sie vorgefertigte Plugins über Marktplätze](https://code.claude.com/docs/de/discover-plugins.md): Finden und installieren Sie Plugins aus Marktplätzen, um Claude Code mit neuen Befähigungen, Agenten und Funktionen zu erweitern.
- [Plugins erstellen](https://code.claude.com/docs/de/plugins.md): Erstellen Sie benutzerdefinierte Plugins, um Claude Code mit Skills, Agents, Hooks und MCP-Servern zu erweitern.
- [Plugins mit Evals testen](https://code.claude.com/docs/de/plugin-evals.md): Schreiben Sie Eval-Fälle für Ihr Claude Code Plugin, führen Sie sie mit claude plugin eval aus, bewerten Sie die Ergebnisse, vergleichen Sie sie mit einer Baseline ohne Plugin und gaten Sie CI basierend auf dem Score.

#### Artefakte

- [Sitzungsausgabe als Artefakte freigeben](https://code.claude.com/docs/de/artifacts.md): Artefakte verwandeln die Arbeit von Claude Code in Live-Seiten, die interaktiv sind und auf claude.ai verfügbar sind. Sie können diese privat halten, mit Ihrer Organisation teilen oder über einen öffentlichen Link veröffentlichen.

#### Automatisierung

- [Automatisieren Sie Aktionen mit Hooks](https://code.claude.com/docs/de/hooks-guide.md): Führen Sie Shell-Befehle automatisch aus, wenn Claude Code Dateien bearbeitet, Aufgaben abschließt oder Eingaben benötigt. Formatieren Sie Code, senden Sie Benachrichtigungen, validieren Sie Befehle und erzwingen Sie Projektregeln.
- [Ereignisse mit Kanälen in eine laufende Sitzung übertragen](https://code.claude.com/docs/de/channels.md): Verwenden Sie Kanäle, um Nachrichten, Benachrichtigungen und Webhooks von einem MCP-Server in Ihre Claude Code-Sitzung zu übertragen. Leiten Sie CI-Ergebnisse, Chat-Nachrichten und Überwachungsereignisse weiter, damit Claude reagieren kann, während Sie weg sind.
- [Prompts nach Zeitplan ausführen](https://code.claude.com/docs/de/scheduled-tasks.md): Verwenden Sie /loop und die Cron-Planungstools, um Prompts wiederholt auszuführen, den Status abzurufen oder einmalige Erinnerungen innerhalb einer Claude Code-Sitzung zu setzen.
- [Claude auf ein Ziel hinarbeiten lassen](https://code.claude.com/docs/de/goal.md): Legen Sie mit /goal eine Abschlussbedingung fest und Claude arbeitet über mehrere Turns hinweg daran, bis die Bedingung erfüllt ist, ein Modell sie für unmöglich hält oder ein Fehler, den Sie beheben müssen, das Ziel löscht.
- [Claude Code programmgesteuert ausführen](https://code.claude.com/docs/de/headless.md): Verwenden Sie das Agent SDK, um Claude Code programmgesteuert über die CLI, Python oder TypeScript auszuführen.
- [Sitzungen über Links starten](https://code.claude.com/docs/de/deep-links.md): Öffnen Sie eine Claude Code-Terminalsitzung über eine URL. Betten Sie `claude-cli://`-Links in Runbooks, Warnungen und Dashboards ein, damit ein Klick Claude Code im richtigen Repository mit der richtigen Eingabeaufforderung öffnet.

#### Leitfäden

- [Claude Code in einem Monorepo oder großen Codebase einrichten](https://code.claude.com/docs/de/large-codebases.md): Konfigurieren Sie Claude Code für Monorepos und große Single-Tree-Codebases mit verschachtelten CLAUDE.md-Dateien, Sparse Worktrees, Code Intelligence und Skills pro Paket, damit Claude sich auf den Code konzentriert, an dem Sie arbeiten.

#### Fehlerbehebung

- [Installationsfehler und Anmeldungsprobleme beheben](https://code.claude.com/docs/de/troubleshoot-install.md): Beheben Sie Fehler wie „Befehl nicht gefunden", PATH, Berechtigungen, Netzwerk und Authentifizierungsfehler bei der Installation oder Anmeldung bei Claude Code.
- [Fehlerbehebung](https://code.claude.com/docs/de/troubleshooting.md): Beheben Sie hohe CPU- oder Speichernutzung, Hänger, Auto-Compact-Thrashing und Suchprobleme in Claude Code und finden Sie die richtige Seite für andere Probleme.
- [Konfiguration debuggen](https://code.claude.com/docs/de/debug-your-config.md): Diagnostizieren Sie, warum CLAUDE.md, Einstellungen, Hooks, MCP-Server oder Skills nicht wirksam werden. Verwenden Sie /context, /doctor, /hooks und /mcp, um zu sehen, was tatsächlich geladen wurde.
- [Fehlerreferenz](https://code.claude.com/docs/de/errors.md): Schlagen Sie Claude Code-Laufzeitfehlermeldungen nach und erfahren Sie, was jede bedeutet und wie Sie sie beheben.

### Verwaltung

#### Einrichtung und Zugriff

- [Claude Code für Ihre Organisation einrichten](https://code.claude.com/docs/de/admin-setup.md): Eine Entscheidungskarte für Administratoren, die Claude Code bereitstellen, mit Abdeckung von API-Anbietern, verwalteten Einstellungen, Richtliniendurchsetzung, Nutzungsüberwachung und Datenbehandlung.
- [Erweiterte Einrichtung](https://code.claude.com/docs/de/setup.md): Systemanforderungen, plattformspezifische Installation, Versionsverwaltung und Deinstallation für Claude Code.
- [Authentifizierung](https://code.claude.com/docs/de/authentication.md): Melden Sie sich bei Claude Code an und konfigurieren Sie die Authentifizierung für Einzelpersonen, Teams und Organisationen.
- [Verwaltete Einstellungen bereitstellen](https://code.claude.com/docs/de/managed-settings.md): Stellen Sie verwaltete Einstellungen auf jedem Entwicklerrechner bereit: Bereitstellungsmechanismen pro Betriebssystem, wie Claude Code verwaltete Quellen kombiniert und wie Sie die Durchsetzung überprüfen.
- [Serververwaltete Einstellungen konfigurieren](https://code.claude.com/docs/de/server-managed-settings.md): Konfigurieren Sie Claude Code zentral für Ihre Organisation durch serververwaltete Einstellungen, ohne dass eine Geräteverwaltungsinfrastruktur erforderlich ist.
- [Kontrollieren Sie den MCP-Serverzugriff für Ihre Organisation](https://code.claude.com/docs/de/managed-mcp.md): Beschränken Sie, welche MCP-Server Benutzer hinzufügen oder verbinden können, oder stellen Sie Server für jeden Benutzer bereit, mit verwalteten Konfigurationsdateien, verwalteten Einstellungen, Zulassungslisten und Ablehnungslisten.
- [Auto-Modus konfigurieren](https://code.claude.com/docs/de/auto-mode-config.md): Teilen Sie dem Auto-Modus-Klassifizierer mit, welche Repos, Buckets und Domains Ihre Organisation vertraut. Legen Sie den Umgebungskontext fest, überschreiben Sie die Standard-Block- und Allow-Regeln, und überprüfen Sie Ihre effektive Konfiguration mit den Auto-Modus-CLI-Unterbefehlen.

#### Bereitstellung

- [Übersicht zur Enterprise-Bereitstellung](https://code.claude.com/docs/de/third-party-integrations.md): Erfahren Sie, wie Claude Code mit verschiedenen Drittanbieterdiensten und Infrastrukturen integriert werden kann, um Enterprise-Bereitstellungsanforderungen zu erfüllen.
- [Verfügbarkeit von Funktionen](https://code.claude.com/docs/de/feature-availability.md): Vergleichen Sie, welche Claude Code-Funktionen in Anthropic-Abonnementplänen, der Anthropic Console, Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform und Microsoft Foundry verfügbar sind.
- [Claude Code auf Amazon Bedrock](https://code.claude.com/docs/de/amazon-bedrock.md): Erfahren Sie, wie Sie Claude Code über Amazon Bedrock konfigurieren, einschließlich Setup, IAM-Konfiguration und Fehlerbehebung.
- [Claude Code auf Claude Platform on AWS](https://code.claude.com/docs/de/claude-platform-on-aws.md): Konfigurieren Sie Claude Code für die Verwendung der von Anthropic betriebenen Claude API mit AWS-Authentifizierung, IAM-Zugriffskontrolle und AWS Marketplace-Abrechnung.
- [Claude Code auf Google Clouds Agent Platform](https://code.claude.com/docs/de/google-vertex-ai.md): Erfahren Sie, wie Sie Claude Code über Google Clouds Agent Platform konfigurieren, ehemals Vertex AI, einschließlich Setup, IAM-Konfiguration und Fehlerbehebung.
- [Claude Code auf Microsoft Foundry](https://code.claude.com/docs/de/microsoft-foundry.md): Erfahren Sie, wie Sie Claude Code über Microsoft Foundry konfigurieren, einschließlich Setup, Konfiguration und Fehlerbehebung.
- [Enterprise-Netzwerkkonfiguration](https://code.claude.com/docs/de/network-config.md): Konfigurieren Sie Claude Code für Enterprise-Umgebungen mit Proxy-Servern, benutzerdefinierten Zertifizierungsstellen (CA) und gegenseitiger Transport Layer Security (mTLS)-Authentifizierung.
- [Claude Code hinter einem Corporate Launcher ausführen](https://code.claude.com/docs/de/corporate-launcher.md): Leiten Sie die Prozesse, die Claude Code von seiner eigenen Binärdatei aus startet, einschließlich des Hintergrunddienstes und jeder Agent-View-Sitzung, durch einen erforderlichen Launcher mit CLAUDE_CODE_PROCESS_WRAPPER oder der processWrapper-Einstellung.
- [Entwicklungscontainer](https://code.claude.com/docs/de/devcontainer.md): Führen Sie Claude Code in einem Entwicklungscontainer aus, um konsistente, isolierte Umgebungen für Ihr Team zu schaffen.

#### Gateways

- [Claude Code über ein Gateway ausführen](https://code.claude.com/docs/de/gateways.md): Leiten Sie Claude Code über ein selbstgehostetes Gateway für zentralisierte Anmeldedaten, Nutzungsverfolgung und Kostenkontrolle weiter. Behandelt die Architektur, Anthropics Claude-Apps-Gateway und die Verwendung anderer Gateway-Produkte.

##### Claude Apps Gateway

- [Claude-Apps-Gateway für Amazon Bedrock, Claude Platform auf AWS, Google Cloud und Microsoft Foundry](https://code.claude.com/docs/de/claude-apps-gateway.md): Führen Sie Claude Code über Amazon Bedrock, Claude Platform auf AWS, Google Cloud oder Microsoft Foundry hinter einem selbstgehosteten Gateway mit SSO-Anmeldung, Modellzugriff pro Gruppe und OTLP-Telemetrie aus.
- [Claude Apps Gateway-Konfiguration](https://code.claude.com/docs/de/claude-apps-gateway-config.md): Referenz für jede gateway.yaml-Option: Listener und TLS, OIDC, Session, Postgres-Speicher, Amazon Bedrock, Claude Platform auf AWS, Google Cloud's Agent Platform und Microsoft Foundry-Upstreams, Modellrouting, verwaltete Richtlinien und Telemetrie.
- [Ausgabenlimits für Claude-Apps-Gateway](https://code.claude.com/docs/de/claude-apps-gateway-spend-limits.md): Begrenzen Sie die Ausgaben jedes Entwicklers über das Claude-Apps-Gateway pro Tag, Woche oder Monat. Legen Sie Limits mit einer Admin-API fest und das Gateway erzwingt sie live bei jeder Anfrage.
- [Bereitstellung und Betrieb des Claude-Apps-Gateways](https://code.claude.com/docs/de/claude-apps-gateway-deploy.md): Registrieren Sie das Gateway bei Ihrem IdP, erstellen Sie den Container, stellen Sie ihn auf Kubernetes oder Cloud Run bereit, und betreiben Sie ihn: Integritätsprüfungen, Geheimnisrotation, Upgrades und Sicherheit.
- [Claude-Apps-Gateway auf AWS bereitstellen](https://code.claude.com/docs/de/claude-apps-gateway-on-aws.md): Ein praktisches Beispiel für die Ausführung von Claude-Apps-Gateway auf AWS: ECS Fargate oder EKS, Amazon RDS für PostgreSQL, AWS Secrets Manager und IAM-rollenbasierte Authentifizierung bei Amazon Bedrock.
- [Claude-Apps-Gateway auf Google Cloud bereitstellen](https://code.claude.com/docs/de/claude-apps-gateway-on-gcp.md): Ein praktisches Beispiel für die Ausführung von Claude-Apps-Gateway auf Google Cloud: Cloud Run oder GKE, Cloud SQL für PostgreSQL, Secret Manager und Service-Account-Authentifizierung für Google Clouds Agent Platform.

##### Andere Gateways

- [Andere LLM-Gateways](https://code.claude.com/docs/de/llm-gateway.md): Leiten Sie Claude Code über ein LLM-Gateway weiter, das Ihre Organisation bereits betreibt. Behandelt die Verbindung von Claude Code mit einem Gateway, die Bereitstellung für Ihre Organisation und was Claude Code an ein Gateway sendet.
- [Claude Code mit einem LLM-Gateway verbinden](https://code.claude.com/docs/de/llm-gateway-connect.md): Richten Sie Claude Code auf das LLM-Gateway Ihrer Organisation aus. Überprüfen Sie, ob Ihr Administrator es bereits konfiguriert hat, oder legen Sie die Basis-URL und die Anmeldedaten selbst fest, überprüfen Sie dann die Verbindung und beheben Sie Gateway-Fehler.
- [Stellen Sie ein LLM-Gateway für Ihre Organisation bereit](https://code.claude.com/docs/de/llm-gateway-rollout.md): Stellen Sie ein Gateway-Produkt für Claude Code bereit: Konfigurieren Sie es so, dass es das weiterleitet, was Claude Code sendet, geben Sie Entwickleranmeldedaten aus, verteilen Sie die Konfiguration über verwaltete Einstellungen, und überprüfen Sie den Rollout.
- [Claude Code Gateway-Kompatibilitätsleitfaden](https://code.claude.com/docs/de/llm-gateway-protocol.md): Halten Sie ein LLM-Gateway mit Claude Code kompatibel: die Endpunkte, die es aufruft, die Header und Body-Felder, die weitergeleitet werden müssen, und was bricht, wenn sie entfernt werden.

#### Nutzung und Kosten

- [Überwachung](https://code.claude.com/docs/de/monitoring-usage.md): Erfahren Sie, wie Sie OpenTelemetry für Claude Code aktivieren und konfigurieren.
- [Kosten effektiv verwalten](https://code.claude.com/docs/de/costs.md): Verfolgen Sie die Token-Nutzung, legen Sie Ausgabenlimits für Teams fest und reduzieren Sie Claude Code-Kosten durch Kontextverwaltung, Modellauswahl, Einstellungen für erweitertes Denken und Preprocessing-Hooks.
- [Teamnutzung mit Analysen verfolgen](https://code.claude.com/docs/de/analytics.md): Zeigen Sie Claude Code-Nutzungsmetriken an, verfolgen Sie die Einführung und messen Sie die Engineering-Geschwindigkeit im Analytics-Dashboard.

#### Plugin-Verteilung

- [Erstellen und Verteilen eines Plugin-Marktplatzes](https://code.claude.com/docs/de/plugin-marketplaces.md): Erstellen und hosten Sie Plugin-Marktplätze, um Claude Code-Erweiterungen in Teams und Communities zu verteilen.
- [Versionsbeschränkungen für Plugin-Abhängigkeiten](https://code.claude.com/docs/de/plugin-dependencies.md): Deklarieren Sie Versionsbeschränkungen für Plugin-Abhängigkeiten, und bündeln Sie einen kuratierten Plugin-Satz hinter einer Installation.
- [Empfehlen Sie Ihr Plugin von Ihrer CLI aus](https://code.claude.com/docs/de/plugin-hints.md): Geben Sie einen einzeiligen Marker von Ihrer CLI aus, damit Claude Code Benutzer auffordert, Ihr offizielles Plugin zu installieren.
- [Plugins für Ihre Organisation empfehlen](https://code.claude.com/docs/de/plugin-relevance.md): Fügen Sie einen Relevanzblock zu Marketplace-Plugin-Einträgen hinzu, damit Claude Code diese vorschlägt, wenn die Arbeit eines Benutzers passt.

#### Sicherheit und Daten

- [Sicherheit](https://code.claude.com/docs/de/security.md): Erfahren Sie mehr über die Sicherheitsvorkehrungen von Claude Code und Best Practices für sichere Nutzung.
- [Datennutzung](https://code.claude.com/docs/de/data-usage.md): Erfahren Sie mehr über die Datennutzungsrichtlinien von Anthropic für Claude
- [Null-Datenspeicherung](https://code.claude.com/docs/de/zero-data-retention.md): Erfahren Sie mehr über Null-Datenspeicherung (ZDR) für Claude Code, verfügbar für qualifizierte Konten auf Claude for Enterprise, einschließlich Umfang, deaktivierter Funktionen und wie Sie die Aktivierung anfordern.

#### Einführung

- [Kommunikations-Kit](https://code.claude.com/docs/de/communications-kit.md): Startankündigungen, Drip-Campaign-Nachrichten und FAQ-Antworten für die Einführung von Claude Code in Ihrer Entwicklungsorganisation.
- [Champion-Kit](https://code.claude.com/docs/de/champion-kit.md): Ein Leitfaden für Ingenieure, die Claude Code intern fördern: was man teilen sollte, wie man Fragen beantwortet und wie man die Akzeptanz im Team erhöht.

### Konfiguration

#### Einstellungen

- [Einstellungsdateien und Priorität](https://code.claude.com/docs/de/settings.md): Ändern Sie Claude Code-Einstellungen, wählen Sie den Bereich aus, zu dem ein Schlüssel gehört, überprüfen Sie die Änderung, und erfahren Sie, welchen Wert Claude Code verwendet, wenn ein Schlüssel an mehreren Stellen gesetzt ist.
- [Alle Einstellungen](https://code.claude.com/docs/de/settings-reference.md): Vollständige Referenz für jeden Claude Code settings.json-Schlüssel: wo jeder hingehört, sein Typ und Standard, sowie ein einsatzbereites Beispiel, mit einem Index aller Schlüssel.
- [Beispiel-Einstellungsdateien](https://code.claude.com/docs/de/settings-example.md): Realistische settings.json-Dateien für einen Entwickler, ein Team und eine Organisation: Kopieren Sie eine, behalten Sie die gewünschten Schlüssel und ändern Sie die Werte.

#### Berechtigungen und Sandboxing

- [Berechtigungen konfigurieren](https://code.claude.com/docs/de/permissions.md): Kontrollieren Sie, worauf Claude Code zugreifen kann und was es mit granularen Berechtigungsregeln, Modi und verwalteten Richtlinien tun kann.
- [Wählen Sie einen Berechtigungsmodus](https://code.claude.com/docs/de/permission-modes.md): Steuern Sie, ob Claude vor dem Bearbeiten von Dateien oder dem Ausführen von Befehlen fragt. Wechseln Sie Modi mit Shift+Tab in der CLI, dem Modusindikator in VS Code oder dem Moduswahlschalter in Desktop.
- [Konfigurieren Sie das Sandboxed-Bash-Tool](https://code.claude.com/docs/de/sandboxing.md): Erfahren Sie, wie das Sandboxed-Bash-Tool von Claude Code Dateisystem- und Netzwerkisolation für sicherere und autonomere Agent-Ausführung bietet.
- [Wählen Sie eine Sandbox-Umgebung](https://code.claude.com/docs/de/sandbox-environments.md): Vergleichen Sie Claude Code Sandbox-Optionen: das integrierte Bash-Tool mit Sandbox, Sandbox-Runtime, Dev Container, Docker und VMs. Wählen Sie die richtige Isolation für Ihr Bedrohungsmodell.

#### Umgebungen

- [Cloud-Umgebungen konfigurieren](https://code.claude.com/docs/de/cloud-environments.md): Konfigurieren Sie Cloud-Umgebungen für Claude Code Cloud-Sitzungen: Netzwerkzugriffsstufen, Umgebungsvariablen, Setup-Skripte und Umgebungs-Caching.

##### Selbst gehostete Umgebungen

- [Selbst gehostete Umgebungen](https://code.claude.com/docs/de/self-hosted-environments.md): Führen Sie Claude Code Cloud-Sitzungen auf einer Infrastruktur aus, die Sie kontrollieren: Richten Sie eine selbst gehostete Umgebung ein, stellen Sie Runner bereit und leiten Sie Sitzungen zu Ihrem eigenen Compute weiter.
- [Schnellstart für selbstgehostete Umgebungen](https://code.claude.com/docs/de/self-hosted-environments-quickstart.md): Richten Sie Ihre erste selbstgehostete Umgebung ein: Installieren Sie Claude Code, erstellen Sie die Umgebung, starten Sie einen Runner und leiten Sie eine Sitzung dorthin weiter.
- [Selbstgehostete Umgebungen in der Produktion bereitstellen](https://code.claude.com/docs/de/self-hosted-environments-deploy.md): Führen Sie selbstgehostete Runner in der Produktion aus: Sicherheitshärtung, Netzwerk-Egress-Kontrolle, Git-Anmeldedaten, Kubernetes- und Compose-Rezepte und Fehlerbehebung.
- [Sitzungen in selbstgehosteten Umgebungen anpassen](https://code.claude.com/docs/de/self-hosted-environments-configuration.md): Passen Sie selbstgehostete Umgebungssitzungen mit Wrapper-Skripten für Anmeldedaten pro Sitzung, Lifecycle-Hooks und On-Demand-Runner-Spawning an.
- [Self-Hosted-Umgebungen end-to-end testen](https://code.claude.com/docs/de/self-hosted-environments-testing.md): Überprüfen Sie ein selbstgehostetes Runner-Image aus CI: Starten Sie eine Sitzung mit der CLI, lesen Sie Claudes Antworten über einen Stop-Hook und schreiben Sie die vollständige Schleife.
- [Referenz für selbstgehostete Umgebungen](https://code.claude.com/docs/de/self-hosted-environments-reference.md): Vollständige Referenz für den selbstgehosteten Runner und Orchestrator: CLI-Flags, Umgebungsvariablen und Prometheus-Metriken.
- [Sitzungsidentität in selbstgehosteten Umgebungen überprüfen](https://code.claude.com/docs/de/self-hosted-environments-identity.md): Überprüfen Sie das CLAUDE_CODE_SESSION_ACCESS_TOKEN JWT, damit Dienste in Ihrem Netzwerk Anfragen von Sitzungen in Ihrer selbstgehosteten Umgebung vertrauen können.

#### Modell und Antworten

- [Modellkonfiguration](https://code.claude.com/docs/de/model-config.md): Konfigurieren Sie, welches Modell Claude Code verwendet, Aufwandsstufen, erweiterten Kontext und das Auto-Compact-Fenster
- [Beschleunigen Sie Antworten mit dem Schnellmodus](https://code.claude.com/docs/de/fast-mode.md): Erhalten Sie schnellere Opus-Antworten in Claude Code durch Aktivierung des Schnellmodus.
- [Schwierige Entscheidungen mit dem Advisor-Tool eskalieren](https://code.claude.com/docs/de/advisor.md): Kombinieren Sie Ihr Hauptmodell mit einem stärkeren Advisor-Modell, das Claude an wichtigen Momenten während einer Aufgabe konsultiert.
- [Ausgabestile](https://code.claude.com/docs/de/output-styles.md): Passen Sie Claude Code für Anwendungsfälle über Softwareentwicklung hinaus an

#### Benutzeroberfläche

- [Konfigurieren Sie Ihr Terminal für Claude Code](https://code.claude.com/docs/de/terminal-config.md): Beheben Sie Shift+Enter für Zeilenumbrüche, erhalten Sie einen Terminal-Gong, wenn Claude fertig ist, konfigurieren Sie tmux, passen Sie das Farbschema an, und aktivieren Sie den Vim-Modus in der Claude Code CLI.
- [Vollbildrendering](https://code.claude.com/docs/de/fullscreen.md): Aktivieren Sie einen sanfteren, flimmerfreien Rendering-Modus mit Mausunterstützung und stabiler Speichernutzung in langen Gesprächen.
- [Claude Code mit einem Bildschirmleser verwenden](https://code.claude.com/docs/de/accessibility.md): Richten Sie Claude Code für Bildschirmleser wie VoiceOver und NVDA ein, sowie Einstellungen für Bildschirmlupe, reduzierte Bewegung und farbenblindfreundliche Designs.
- [Spracherfassung](https://code.claude.com/docs/de/voice-dictation.md): Sprechen Sie Ihre Eingabeaufforderungen in der Claude Code CLI mit Halten-zum-Aufnehmen oder Tippen-zum-Aufnehmen Spracherfassung.
- [Passen Sie Ihre Statuszeile an](https://code.claude.com/docs/de/statusline.md): Konfigurieren Sie eine benutzerdefinierte Statusleiste zur Überwachung der Kontextfensternutzung, Kosten und Git-Status in Claude Code
- [Tastaturkürzel anpassen](https://code.claude.com/docs/de/keybindings.md): Passen Sie Tastaturkürzel in Claude Code mit einer Keybindings-Konfigurationsdatei an.

### Referenz

#### Referenz

- [CLI-Referenz](https://code.claude.com/docs/de/cli-reference.md): Vollständige Referenz für die Claude Code Befehlszeilenschnittstelle, einschließlich Befehle und Flags.
- [Befehle](https://code.claude.com/docs/de/commands.md): Vollständige Referenz für Befehle in Claude Code, einschließlich integrierter Befehle und gebündelter Skills.
- [Umgebungsvariablen](https://code.claude.com/docs/de/env-vars.md): Referenz für Umgebungsvariablen, die das Verhalten von Claude Code steuern.
- [Tools-Referenz](https://code.claude.com/docs/de/tools-reference.md): Vollständige Referenz für die Tools, die Claude Code verwenden kann, einschließlich Berechtigungsanforderungen und Verhalten pro Tool.
- [Interaktiver Modus](https://code.claude.com/docs/de/interactive-mode.md): Vollständige Referenz für Tastaturkürzel, Eingabemodi und interaktive Funktionen in Claude Code-Sitzungen.
- [Checkpointing](https://code.claude.com/docs/de/checkpointing.md): Verfolgen, zurückspulen und fassen Sie Claudes Bearbeitungen und Konversation zusammen, um den Sitzungsstatus zu verwalten.
- [Hooks-Referenz](https://code.claude.com/docs/de/hooks.md): Referenz für Claude Code Hook-Ereignisse, Konfigurationsschema, JSON-Ein-/Ausgabeformate, Exit-Codes, asynchrone Hooks, HTTP-Hooks, Prompt-Hooks und MCP-Tool-Hooks.
- [Plugins-Referenz](https://code.claude.com/docs/de/plugins-reference.md): Vollständige technische Referenz für das Claude Code Plugin-System, einschließlich Schemas, CLI-Befehle und Komponentenspezifikationen.
- [Channels-Referenz](https://code.claude.com/docs/de/channels-reference.md): Erstellen Sie einen MCP-Server, der Webhooks, Benachrichtigungen und Chat-Nachrichten in eine Claude Code-Sitzung pusht. Referenz für den Channel-Vertrag: Funktionsdeklaration, Benachrichtigungsereignisse, Antwort-Tools, Sender-Gating und Berechtigungsweitergabe.

#### Glossar

- [Glossar](https://code.claude.com/docs/de/glossary.md): Definitionen für Claude Code-Terminologie. Erfahren Sie, was Agentic Loop, Komprimierung, CLAUDE.md, Hooks, Subagenten, MCP und andere Kernkonzepte bedeuten.

### Agent SDK

#### Agent SDK

- [Agent SDK – Übersicht](https://code.claude.com/docs/de/agent-sdk/overview.md): Erstellen Sie produktive KI-Agenten mit Claude Code als Bibliothek
- [Schnellstart](https://code.claude.com/docs/de/agent-sdk/quickstart.md): Erste Schritte mit dem Python- oder TypeScript-Agent-SDK zum Erstellen von KI-Agenten, die autonom funktionieren
- [Migrieren zum Claude Agent SDK](https://code.claude.com/docs/de/agent-sdk/migration-guide.md): Leitfaden für die Migration der Claude Code TypeScript- und Python-SDKs zum Claude Agent SDK
- [Fehlerbehebung im Agent SDK](https://code.claude.com/docs/de/agent-sdk/troubleshooting.md): Beheben Sie Agent SDK-Fehler anhand der genauen Meldung, die Sie sehen, mit der Ursache und Lösung für jeden Fehler in den TypeScript- und Python-SDKs.

#### Agenten erstellen

- [Konfigurieren Sie Ihren Agent](https://code.claude.com/docs/de/agent-sdk/configuration.md): Konfigurieren Sie Agent SDK-Sitzungen: stellen Sie das Optionsobjekt zusammen, legen Sie das Modell, die Umgebung und Limits fest, und finden Sie die Seite jeder Funktionsoption.
- [Beispiele](https://code.claude.com/docs/de/agent-sdk/examples.md): Finden Sie ein vollständiges, ausführbares Agent SDK-Projekt oder ein geführtes Rezept aus dem Claude Cookbook, das zu dem passt, was Sie erstellen möchten.

#### Kernkonzepte

- [So funktioniert die Agent-Schleife](https://code.claude.com/docs/de/agent-sdk/agent-loop.md): Verstehen Sie den Nachrichtenlebenszyklus, die Werkzeugausführung, das Kontextfenster und die Architektur, die Ihre SDK-Agenten antreibt.
- [Claude Code-Funktionen im SDK verwenden](https://code.claude.com/docs/de/agent-sdk/claude-code-features.md): Laden Sie Projektanweisungen, Skills, Hooks und andere Claude Code-Funktionen in Ihre SDK-Agenten.
- [Mit Sitzungen arbeiten](https://code.claude.com/docs/de/agent-sdk/sessions.md): Wie Sitzungen die Gesprächsverlauf des Agenten speichern, und wann Sie continue, resume und fork verwenden, um zu einem früheren Durchlauf zurückzukehren.
- [Sitzungen in externem Speicher persistieren](https://code.claude.com/docs/de/agent-sdk/session-storage.md): Spiegeln Sie Agent SDK-Sitzungstranskripte in Ihren eigenen Objektspeicher, Key-Value-Store oder Ihre Datenbank, damit andere Hosts Ihre Sitzungen fortsetzen können.

#### Eingabe und Ausgabe

- [Streaming-Eingabe](https://code.claude.com/docs/de/agent-sdk/streaming-vs-single-mode.md): Verständnis der zwei Eingabemodi für Claude Agent SDK und wann jeder verwendet wird
- [Genehmigungen und Benutzereingaben verarbeiten](https://code.claude.com/docs/de/agent-sdk/user-input.md): Zeigen Sie Claudes Genehmigungsanfragen und Klärungsfragen den Benutzern an und geben Sie deren Entscheidungen an das SDK zurück.
- [Antworten in Echtzeit streamen](https://code.claude.com/docs/de/agent-sdk/streaming-output.md): Erhalten Sie Echtzeit-Antworten vom Agent SDK, während Text und Tool-Aufrufe gestreamt werden
- [Strukturierte Ausgaben von Agenten abrufen](https://code.claude.com/docs/de/agent-sdk/structured-outputs.md): Validiertes JSON aus Agent-Workflows mit JSON Schema, Zod oder Pydantic zurückgeben. Erhalten Sie typsichere, strukturierte Daten nach Multi-Turn-Tool-Nutzung.

#### Mit Tools erweitern

- [Geben Sie Claude benutzerdefinierte Tools](https://code.claude.com/docs/de/agent-sdk/custom-tools.md): Definieren Sie benutzerdefinierte Tools mit dem In-Process-MCP-Server des Claude Agent SDK, damit Claude Ihre Funktionen aufrufen, Ihre APIs treffen und domänenspezifische Operationen ausführen kann.
- [Mit MCP zu externen Tools verbinden](https://code.claude.com/docs/de/agent-sdk/mcp.md): Konfigurieren Sie MCP-Server, um Ihren Agenten mit externen Tools zu erweitern. Behandelt Transporttypen, Tool-Suche für große Tool-Sets, Authentifizierung und Fehlerbehandlung.
- [Mit Tool-Suche zu vielen Tools skalieren](https://code.claude.com/docs/de/agent-sdk/tool-search.md): Skalieren Sie Ihren Agenten auf Tausende von Tools, indem Sie nur das Nötigste entdecken und bei Bedarf laden.
- [Subagents im SDK](https://code.claude.com/docs/de/agent-sdk/subagents.md): Definieren und rufen Sie Subagents auf, um den Kontext zu isolieren, Aufgaben parallel auszuführen und spezialisierte Anweisungen in Ihren Claude Agent SDK-Anwendungen anzuwenden.

#### Verhalten anpassen

- [Ändern von Systemaufforderungen](https://code.claude.com/docs/de/agent-sdk/modifying-system-prompts.md): Wählen Sie zwischen der `claude_code`-Voreinstellung und einer benutzerdefinierten Systemaufforderung, und passen Sie das Verhalten mit CLAUDE.md, Ausgabestilen, Append oder einer vollständig benutzerdefinierten Aufforderung an.
- [Agent Skills erweitern](https://code.claude.com/docs/de/agent-sdk/skills.md): Steuern Sie, welche Skills Claude in Claude Agent SDK-Sitzungen aufrufen kann, versenden Sie Befehle nach Name und erstellen Sie Skills, die Ihre Sitzungen entdecken
- [Plugins im SDK](https://code.claude.com/docs/de/agent-sdk/plugins.md): Laden Sie benutzerdefinierte Plugins, um Claude Code mit Skills, Agenten, Hooks und MCP-Servern über das Agent SDK zu erweitern

#### Kontrolle und Beobachtbarkeit

- [Berechtigungen konfigurieren](https://code.claude.com/docs/de/agent-sdk/permissions.md): Kontrollieren Sie, wie Ihr Agent Tools mit Berechtigungsmodi, Hooks und deklarativen Allow/Deny-Regeln verwendet.
- [Agentverhalten mit Hooks abfangen und steuern](https://code.claude.com/docs/de/agent-sdk/hooks.md): Fangen Sie Agentverhalten an wichtigen Ausführungspunkten mit Hooks ab und passen Sie es an
- [Dateiänderungen mit Checkpointing rückgängig machen](https://code.claude.com/docs/de/agent-sdk/file-checkpointing.md): Verfolgen Sie Dateiänderungen während Agent-Sitzungen und stellen Sie Dateien in jeden vorherigen Zustand wieder her
- [Kosten und Nutzung verfolgen](https://code.claude.com/docs/de/agent-sdk/cost-tracking.md): Erfahren Sie, wie Sie die Token-Nutzung verfolgen, Kosten schätzen und Prompt Caching mit dem Claude Agent SDK konfigurieren.
- [Observabilität mit OpenTelemetry](https://code.claude.com/docs/de/agent-sdk/observability.md): Exportieren Sie Traces, Metriken und Events aus dem Agent SDK in Ihr Observability-Backend mit OpenTelemetry.
- [Todos verfolgen](https://code.claude.com/docs/de/agent-sdk/todo-tracking.md): Verfolgen Sie Todos in Agent SDK-Sitzungen und rendern Sie Claudes Fortschritt in Ihrer Anwendung aus strukturierten Tool-Aufrufen

#### Bereitstellung

- [Hosting des Agent SDK](https://code.claude.com/docs/de/agent-sdk/hosting.md): Stellen Sie das Agent SDK in der Produktion bereit: Subprocess-Architektur, Sitzungspersistenz, Skalierung, Observability und Multi-Tenant-Isolation für Docker, Kubernetes und Sandbox-Provider.
- [Sichere Bereitstellung von KI-Agenten](https://code.claude.com/docs/de/agent-sdk/secure-deployment.md): Ein Leitfaden zur Sicherung von Claude Code und Agent SDK-Bereitstellungen mit Isolation, Verwaltung von Anmeldedaten und Netzwerkkontrollen

#### SDK-Referenzen

- [Agent SDK Referenz - TypeScript](https://code.claude.com/docs/de/agent-sdk/typescript.md): Vollständige API-Referenz für das TypeScript Agent SDK, einschließlich aller Funktionen, Typen und Schnittstellen.
- [TypeScript SDK V2 Sitzungs-API (entfernt)](https://code.claude.com/docs/de/agent-sdk/typescript-v2-preview.md): Referenz für die entfernte V2 TypeScript Agent SDK Sitzungs-API mit sitzungsbasiertem Send/Stream-Muster für mehrteilige Gespräche.
- [Agent SDK Referenz - Python](https://code.claude.com/docs/de/agent-sdk/python.md): Vollständige API-Referenz für das Python Agent SDK, einschließlich aller Funktionen, Typen und Klassen.

### Neuigkeiten

#### Neuigkeiten

- [Neuigkeiten](https://code.claude.com/docs/de/whats-new/index.md): Eine wöchentliche Zusammenfassung der bemerkenswertesten Claude Code-Funktionen mit Code-Snippets, Demos und Kontext, warum sie wichtig sind.
- [Woche 37 · 7.–11. September 2026](https://code.claude.com/docs/de/whats-new/2026-w37.md): Testen Sie Ihre Plugins mit claude plugin eval und öffnen Sie Claude Code Desktop-Bereiche in eigenen Fenstern.
- [Woche 36 · 31. August – 4. September 2026](https://code.claude.com/docs/de/whats-new/2026-w36.md): Wechseln Sie zu Claude Fable 5.1, lassen Sie die Computernutzung im Hintergrund auf dem Desktop laufen, und beobachten Sie Claudes Änderungen in einem Live-/diff-Panel.
- [Woche 35 · 24.–28. August 2026](https://code.claude.com/docs/de/whats-new/2026-w35.md): Setzen Sie Terminal-Sitzungen in der Claude Code Desktop-App fort, überprüfen Sie Feedback-Berichte, die Claude für Sie entwirft, und starten Sie eine Sitzung im eingeschränkten Modus.
- [Woche 34 · 17.–21. August 2026](https://code.claude.com/docs/de/whats-new/2026-w34.md): Entwerfen Sie bearbeitbare UI-Artboards mit dem /design-Skill, stellen Sie den Concise-Ausgabestil ein, und starten Sie eine Claude Code-Sitzung auf Ihrem Computer von Ihrem Telefon aus.
- [Woche 33 · 10.–14. August 2026](https://code.claude.com/docs/de/whats-new/2026-w33.md): Claude Code Desktop setzt sich nach dem Zurücksetzen eines Nutzungslimits automatisch fort, der Fork-Modus ist standardmäßig aktiviert, und GitLab-Merge-Requests und Marktplätze treten GitHub bei.
- [Woche 32 · 3.–7. August 2026](https://code.claude.com/docs/de/whats-new/2026-w32.md): Claude Code-Sitzungen können sich gegenseitig Nachrichten senden, selbstgehostete Umgebungen führen Cloud-Sitzungen auf Ihrer Infrastruktur aus, und der Auto-Modus wird zum Standard-Berechtigungsmodus.
- [Woche 30 · 20.–24. Juli 2026](https://code.claude.com/docs/de/whats-new/2026-w30.md): Opus 5 wird zum Standard-Opus-Modell, Claude Code Desktop erhält einen iOS-Simulator-Bereich, und das Claude-Sicherheits-Plugin scannt Ihren Code auf Sicherheitslücken.
- [Woche 29 · 13.–17. Juli 2026](https://code.claude.com/docs/de/whats-new/2026-w29.md): Rufen Sie Live-Daten in veröffentlichte Artefakte über MCP-Konnektoren auf, und verwenden Sie Claude Code mit einem Bildschirmleser im neuen Bildschirmleser-Modus.
- [Woche 28 · 6.–10. Juli 2026](https://code.claude.com/docs/de/whats-new/2026-w28.md): Durchsuchen Sie externe Websites über den integrierten Browser der Desktop-App, führen Sie eine vollständige Setup-Überprüfung mit /doctor durch, und nutzen Sie neue Transkriptschutzmaßnahmen im Auto-Modus sowie verbesserte Agent-View-Funktionen.
- [Woche 27 · 29. Juni – 3. Juli 2026](https://code.claude.com/docs/de/whats-new/2026-w27.md): Claude Sonnet 5 wird zum Standard-Modell, Claude in Chrome erreicht allgemeine Verfügbarkeit, Subagenten laufen standardmäßig im Hintergrund, Claude Desktop kommt in Beta auf Linux an, und /radio stimmt sich auf Claude FM ein.
- [Woche 26 · 22.–26. Juni 2026](https://code.claude.com/docs/de/whats-new/2026-w26.md): Authentifizieren Sie MCP-Server von Ihrer Shell mit claude mcp login, erhalten Sie eine Antwort auf die Ausgabe von Shell-Mode-Befehlen mit dem !-Präfix, und setzen Sie ein Gespräch vor /clear mit /rewind fort.
- [Woche 25 · 15.–19. Juni 2026](https://code.claude.com/docs/de/whats-new/2026-w25.md): Veröffentlichen Sie eine Live-Seite, die Sie freigeben können, aus Ihrer Sitzung mit Artifacts, gleichen Sie Tool-Parameter in Deny- und Ask-Regeln ab, und legen Sie jede Einstellung über die Eingabeaufforderung mit /config fest.
- [Woche 24 · 8.–12. Juni 2026](https://code.claude.com/docs/de/whats-new/2026-w24.md): Verschieben Sie eine Sitzung mit /cd in ein neues Verzeichnis, lassen Sie Sub-Agenten ihre eigenen Sub-Agenten spawnen, und beheben Sie eine fehlerhafte Konfiguration mit dem abgesicherten Modus.
- [Woche 23 · 1.–5. Juni 2026](https://code.claude.com/docs/de/whats-new/2026-w23.md): Führen Sie den Auto-Modus auf Amazon Bedrock, Google Cloud's Agent Platform und Microsoft Foundry aus, fordern Sie vor dem Schreiben von Dateien auf, die Code im acceptEdits-Modus ausführen können, listen Sie installierte Plugins mit /plugin list auf, und erfordern Sie einen genehmigten Versionsbere…
- [Woche 22 · 25.–29. Mai 2026](https://code.claude.com/docs/de/whats-new/2026-w22.md): Führen Sie Claude Code auf Claude Opus 4.8 aus, orchestrieren Sie große Aufgaben mit dynamischen Workflows, fangen Sie Sicherheitsprobleme mit dem security-guidance-Plugin auf und nutzen Sie den schnellen Modus auf Opus 4.8 zu einem niedrigeren Preis.
- [Woche 21 · 18.–22. Mai 2026](https://code.claude.com/docs/de/whats-new/2026-w21.md): Nutzen Sie den Auto-Modus im Pro-Plan mit Sonnet 4.6, sehen Sie in /usage, welche Skills, Subagenten und MCP-Server Ihre Plan-Limits antreiben, und überprüfen Sie Unterschiede mit dem neuen /code-review-Befehl.
- [Woche 20 · 11.–15. Mai 2026](https://code.claude.com/docs/de/whats-new/2026-w20.md): Verwalten Sie jede Claude Code-Sitzung von einem Bildschirm aus mit der Agent-Ansicht, halten Sie Claude an der Verfolgung eines Ziels, bis eine Bedingung erfüllt ist, und führen Sie den Schnellmodus standardmäßig auf Opus 4.7 aus.
- [Woche 19 · 4.–8. Mai 2026](https://code.claude.com/docs/de/whats-new/2026-w19.md): Laden Sie Plugins aus .zip-Archiven und URLs, durchsuchen Sie den Befehlsverlauf über alle Projekte hinweg mit Strg+R, erstellen Sie neue Worktrees aus lokalem HEAD oder dem Remote-Standard, und blockieren Sie Aktionen bedingungslos mit Auto-Modus-Hard-Deny-Regeln.
- [Woche 18 · 27. April – 1. Mai 2026](https://code.claude.com/docs/de/whats-new/2026-w18.md): Claude Code unter Windows läuft ohne Git Bash, claude auth login akzeptiert einen eingefügten OAuth-Code, wenn der Browser-Callback localhost nicht erreichen kann, claude project purge bereinigt den lokalen Status pro Projekt, und das Einfügen einer PR-URL in /resume findet die Sitzung, die sie erst…
- [Woche 17 · 20.–24. April 2026](https://code.claude.com/docs/de/whats-new/2026-w17.md): /ultrareview öffnet sich als Forschungsvorschau, automatische Sitzungsübersichten bei Rückkehr zu einem Terminal, benutzerdefinierte Farbthemen, die Sie in Plugins erstellen und bereitstellen können, und ein neu gestaltetes Claude Code im Web.
- [Woche 16 · 13.–17. April 2026](https://code.claude.com/docs/de/whats-new/2026-w16.md): Claude Opus 4.7 mit der neuen xhigh-Anstrengungsstufe, Routinen auf Claude Code im Web, mobile Push-Benachrichtigungen, die Ihr Telefon anpingen, wenn Claude Sie braucht, eine /usage-Aufschlüsselung, die zeigt, was Ihre Limits antreibt, und native Binärdateien ersetzen das gebündelte JavaScript.
- [Woche 15 · 6.–10. April 2026](https://code.claude.com/docs/de/whats-new/2026-w15.md): Ultraplan Cloud-Planung, das Monitor-Tool mit Selbststeuerung /loop, /team-onboarding zum Verpacken Ihres Setups und /autofix-pr von Ihrem Terminal.
- [Woche 14 · 30. März – 3. April 2026](https://code.claude.com/docs/de/whats-new/2026-w14.md): Computernutzung in der CLI, interaktive In-Product-Lektionen, flimmerfreies Rendering, MCP-Ergebnisgröße-Overrides pro Tool und Plugin-Ausführbare auf PATH.
- [Woche 13 · 23.–27. März 2026](https://code.claude.com/docs/de/whats-new/2026-w13.md): Auto-Modus für freihändige Berechtigungen, integrierte Computersteuerung, PR-Auto-Fix in der Cloud, Transkriptsuche und ein PowerShell-Tool für Windows.

### Ressourcen

#### Ressourcen

- [Rechtliche Bestimmungen und Compliance](https://code.claude.com/docs/de/legal-and-compliance.md): Rechtliche Vereinbarungen, Compliance-Zertifizierungen und Sicherheitsinformationen für Claude Code.

---

## Claude Code Docs: Spanish

- 官方原文：https://code.claude.com/docs/_llms/es.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-es.md`

# Claude Code Docs: Spanish

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Spanish

### Primeros pasos

#### Primeros pasos

- [Descripción general](https://code.claude.com/docs/es/overview.md): Claude Code es una herramienta de codificación agencial que lee tu base de código, edita archivos, ejecuta comandos e integra con tus herramientas de desarrollo. Disponible en tu terminal, IDE, aplicación de escritorio y navegador.
- [Inicio rápido](https://code.claude.com/docs/es/quickstart.md): ¡Bienvenido a Claude Code!
- [Registro de cambios](https://code.claude.com/docs/es/changelog.md)

#### Conceptos fundamentales

- [Cómo funciona Claude Code](https://code.claude.com/docs/es/how-claude-code-works.md): Comprenda el bucle agentico, las herramientas integradas y cómo Claude Code interactúa con su proyecto.
- [Extender Claude Code](https://code.claude.com/docs/es/features-overview.md): Comprenda cuándo usar CLAUDE.md, Skills, subagents, hooks, MCP y plugins.
- [Explorar el directorio .claude](https://code.claude.com/docs/es/claude-directory.md): Dónde Claude Code lee CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules y auto memory. Explore el directorio .claude en su proyecto y ~/.claude en su directorio de inicio.
- [Explorar la ventana de contexto](https://code.claude.com/docs/es/context-window.md): Una simulación interactiva de cómo se llena la ventana de contexto de Claude Code durante una sesión. Vea qué se carga automáticamente, cuánto cuesta cada lectura de archivo y cuándo se activan las reglas y hooks.
- [Cómo Claude Code utiliza el almacenamiento en caché de prompts](https://code.claude.com/docs/es/prompt-caching.md): Claude Code gestiona automáticamente el almacenamiento en caché de prompts. Vea por qué un cambio de modelo desencadena un turno lento sin caché, qué cuesta `/compact`, por qué las ediciones de CLAUDE.md no se aplican a mitad de sesión, y cómo verificar su tasa de aciertos de caché.

#### Usar Claude Code

- [Cómo Claude recuerda su proyecto](https://code.claude.com/docs/es/memory.md): Proporcione a Claude instrucciones persistentes con archivos CLAUDE.md o AGENTS.md, y permita que Claude acumule aprendizajes automáticamente con auto memory.
- [Gestionar sesiones](https://code.claude.com/docs/es/sessions.md): Nombre, reanude, ramifique y cambie entre conversaciones de Claude Code. Cubre `--continue`, `--resume`, `--from-pr`, el selector `/resume`, nombres de sesión, exportación de transcripciones y dónde se almacenan las transcripciones.
- [Flujos de trabajo comunes](https://code.claude.com/docs/es/common-workflows.md): Guías paso a paso para explorar bases de código, corregir errores, refactorizar, probar y otras tareas cotidianas con Claude Code.
- [Biblioteca de prompts](https://code.claude.com/docs/es/prompt-library.md): Copie y pegue prompts para Claude Code, etiquetados por tarea y rol.
- [Mejores prácticas para Claude Code](https://code.claude.com/docs/es/best-practices.md): Consejos y patrones para aprovechar al máximo Claude Code, desde configurar su entorno hasta escalar entre sesiones paralelas.

#### Plataformas e integraciones

- [Plataformas e integraciones](https://code.claude.com/docs/es/platforms.md): Elija dónde ejecutar Claude Code y qué conectar. Compare la CLI, Desktop, VS Code, JetBrains, web, móvil e integraciones como Chrome, Slack e CI/CD.
- [Continúe sesiones locales desde cualquier dispositivo con Remote Control](https://code.claude.com/docs/es/remote-control.md): Continúe una sesión local de Claude Code desde su teléfono, tableta o cualquier navegador usando Remote Control. Funciona con claude.ai/code y la aplicación móvil de Claude.
- [Deje que Claude coordine el trabajo en curso con Projects](https://code.claude.com/docs/es/claude-projects.md): Proporcione a Claude un conjunto de trabajo relacionado en una conversación y deje que coordine sesiones en la nube paralelas que compartan repositorios, instrucciones y memoria.
- [Claude Code en dispositivos móviles](https://code.claude.com/docs/es/mobile.md): Inicie, supervise y dirija tareas de Claude Code desde su teléfono con la aplicación Claude para iOS y Android.
- [Usar Claude Code con Chrome](https://code.claude.com/docs/es/chrome.md): Conecta Claude Code a tu navegador Chrome para probar aplicaciones web, depurar con registros de consola, automatizar el relleno de formularios y extraer datos de páginas web.
- [Permitir que Claude use su computadora desde la CLI](https://code.claude.com/docs/es/computer-use.md): Habilite computer use en la CLI de Claude Code para que Claude pueda abrir aplicaciones, hacer clic, escribir y ver su pantalla en macOS. Pruebe aplicaciones nativas, depure problemas visuales y automatice herramientas solo GUI sin salir de su terminal.
- [Usar Claude Code en VS Code](https://code.claude.com/docs/es/vs-code.md): Instala y configura la extensión Claude Code para VS Code. Obtén asistencia de codificación con IA con diffs en línea, menciones @, revisión de planes y atajos de teclado.
- [JetBrains IDEs](https://code.claude.com/docs/es/jetbrains.md): Utiliza Claude Code con JetBrains IDEs incluyendo IntelliJ, PyCharm, WebStorm y más
- [Claude Code en Slack](https://code.claude.com/docs/es/slack.md): Delega tareas de codificación directamente desde tu espacio de trabajo de Slack. Anthropic está retirando esta versión anterior para espacios de trabajo de Team y Enterprise en favor de Claude Tag; permanece como la ruta de configuración en planes Pro y Max.
- [Claude Tag](https://code.claude.com/docs/es/claude-tag.md): Integra Claude en los canales de Slack de tu equipo con Claude Tag y encuentra su documentación de configuración y uso en claude.com.

##### Claude Code en la nube

- [Comienza con Claude Code en la nube](https://code.claude.com/docs/es/web-quickstart.md): Ejecuta Claude Code en la nube desde tu navegador o teléfono. Conecta un repositorio de GitHub, envía una tarea y revisa el PR sin configuración local.
- [Usar Claude Code en la nube](https://code.claude.com/docs/es/claude-code-on-the-web.md): Ejecute sesiones de Claude Code en la nube desde su navegador, teléfono, aplicación de escritorio o terminal, muévalas con --cloud y --teleport, y corrija automáticamente solicitudes de extracción.
- [Automatizar el trabajo con rutinas](https://code.claude.com/docs/es/routines.md): Ponga Claude Code en piloto automático. Defina rutinas que se ejecuten en un horario, se activen en llamadas API o reaccionen a eventos de GitHub desde la infraestructura en la nube.
- [Encuentra errores con ultrareview](https://code.claude.com/docs/es/ultrareview.md): Ejecuta una revisión de código profunda y multiagente en la nube con /code-review ultra para encontrar y verificar errores antes de fusionar.

##### Claude Code en el escritorio

- [Comenzar con la aplicación de escritorio](https://code.claude.com/docs/es/desktop-quickstart.md): Instale Claude Code en el escritorio e inicie su primera sesión de codificación
- [Aplicación de escritorio](https://code.claude.com/docs/es/desktop.md): Aproveche al máximo Claude Code Desktop: sesiones paralelas con aislamiento de Git, diseño de panel de arrastrar y soltar, terminal integrada y editor de archivos, chats laterales, uso de computadora, envíe sesiones desde su teléfono, revisión visual de diferencias, vistas previas de aplicaciones, m…
- [Claude Desktop en Linux (beta)](https://code.claude.com/docs/es/desktop-linux.md): Instala y actualiza la aplicación de escritorio Claude en Ubuntu y Debian
- [Claude Code Desktop en WSL](https://code.claude.com/docs/es/desktop-wsl.md): Ejecutar sesiones de Code dentro de una distribución WSL 2 en Windows
- [Programar tareas recurrentes en Claude Code Desktop](https://code.claude.com/docs/es/desktop-scheduled-tasks.md): Configure tareas programadas en Claude Code Desktop para ejecutar Claude automáticamente de forma recurrente para revisiones de código diarias, auditorías de dependencias o resúmenes matutinos.
- [Prueba aplicaciones iOS en el simulador](https://code.claude.com/docs/es/desktop-ios-simulator.md): Claude Code Desktop abre tu aplicación en el panel del Simulador de iOS cuando Claude la compila, ejecuta o verifica, con un simulador separado para cada sesión.

##### Revisión de código e CI/CD

- [Detectar problemas de seguridad mientras Claude escribe código](https://code.claude.com/docs/es/security-guidance.md): Instale el plugin security-guidance para que Claude revise sus propios cambios de código en busca de vulnerabilidades y las corrija en la misma sesión.
- [Escanea tu base de código en busca de vulnerabilidades](https://code.claude.com/docs/es/claude-security.md): Instala el plugin de seguridad de Claude para escanear tu base de código en busca de vulnerabilidades en una sesión de Claude Code y convierte los hallazgos en parches que revisas y aplicas.
- [Code Review](https://code.claude.com/docs/es/code-review.md): Configure revisiones automatizadas de PR que detecten errores lógicos, vulnerabilidades de seguridad y regresiones mediante análisis multiagente de su base de código completa
- [Claude Code GitHub Actions](https://code.claude.com/docs/es/github-actions.md): Ejecute Claude Code en flujos de trabajo de GitHub Actions para responder a menciones @claude, automatizar tareas y convertir problemas en solicitudes de extracción
- [Usar Claude Code GitHub Actions con proveedores en la nube](https://code.claude.com/docs/es/github-actions-cloud-providers.md): Ejecute Claude Code GitHub Actions a través de Amazon Bedrock, Google Cloud's Agent Platform o Microsoft Foundry en lugar de la API de Claude
- [Claude Code con GitHub Enterprise Server](https://code.claude.com/docs/es/github-enterprise-server.md): Conecte Claude Code a su instancia de GitHub Enterprise Server autohospedada para sesiones en la nube, revisión de código y mercados de plugins.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/es/gitlab-ci-cd.md): Aprenda a integrar Claude Code en su flujo de trabajo de desarrollo con GitLab CI/CD

### Crear con Claude Code

#### Agentes y trabajo en paralelo

- [Ejecutar agentes en paralelo](https://code.claude.com/docs/es/agents.md): Compare las formas en que Claude Code puede realizar múltiples tareas simultáneamente: subagentes, vista de agentes, equipos de agentes, flujos de trabajo dinámicos y proyectos.
- [Crear subagentes personalizados](https://code.claude.com/docs/es/sub-agents.md): Cree y utilice subagentes de IA especializados en Claude Code para flujos de trabajo específicos de tareas y una mejor gestión del contexto.
- [Gestionar múltiples agentes con la vista de agentes](https://code.claude.com/docs/es/agent-view.md): Distribuya y gestione muchas sesiones de Claude Code desde una pantalla. La vista de agentes muestra qué está haciendo cada sesión y cuáles necesitan su entrada.
- [Orquestar equipos de sesiones de Claude Code](https://code.claude.com/docs/es/agent-teams.md): Coordine múltiples instancias de Claude Code trabajando juntas como un equipo, con tareas compartidas, mensajería entre agentes y gestión centralizada.
- [Mensajería entre tus otras sesiones de Claude Code](https://code.claude.com/docs/es/cross-session-messaging.md): Permite que Claude liste y envíe mensajes a tus otras sesiones de Claude Code en esta máquina, y alcance tus sesiones en otras máquinas o en la web.
- [Orquestar subagentes a escala con flujos de trabajo dinámicos](https://code.claude.com/docs/es/workflows.md): Los dynamic workflows orquestan muchos subagentes a partir de un script que Claude escribe y que puede volver a ejecutar. Úselos para auditorías de base de código, migraciones grandes e investigación con verificación cruzada.
- [Ejecutar sesiones paralelas con worktrees](https://code.claude.com/docs/es/worktrees.md): Aisle sesiones paralelas de Claude Code en worktrees de git separados para que los cambios no colisionen. Cubre la bandera `--worktree`, aislamiento de subagentes, `.worktreeinclude`, limpieza y hooks de VCS no-git.

#### MCP

- [Conectarse a servidores MCP](https://code.claude.com/docs/es/mcp-quickstart.md): Agregue un servidor MCP a Claude Code, verifique la conexión y encuentre la configuración en el disco.
- [Conectar Claude Code a herramientas mediante MCP](https://code.claude.com/docs/es/mcp.md): Aprenda cómo conectar Claude Code a sus herramientas con el Model Context Protocol.

#### Skills

- [Extender Claude con skills](https://code.claude.com/docs/es/skills.md): Cree, gestione y comparta skills para extender las capacidades de Claude en Claude Code. Incluye comandos personalizados y skills agrupados.

#### Plugins

- [Descubra e instale plugins pregenerados a través de mercados](https://code.claude.com/docs/es/discover-plugins.md): Encuentre e instale plugins de mercados para extender Claude Code con nuevas skills, agentes y capacidades.
- [Crear plugins](https://code.claude.com/docs/es/plugins.md): Crea plugins personalizados para extender Claude Code con skills, agentes, hooks y servidores MCP.
- [Prueba plugins con evals](https://code.claude.com/docs/es/plugin-evals.md): Escriba casos de eval para su plugin de Claude Code, ejecútelos con claude plugin eval, califique los resultados, compare con una línea base sin plugin y controle CI en la puntuación.

#### Artefactos

- [Compartir salida de sesión como artefactos](https://code.claude.com/docs/es/artifacts.md): Los artefactos convierten el trabajo de Claude Code en páginas interactivas en vivo en claude.ai que puede mantener privadas, compartir con su organización o publicar en un enlace público.

#### Automatización

- [Automatizar acciones con hooks](https://code.claude.com/docs/es/hooks-guide.md): Ejecuta comandos de shell automáticamente cuando Claude Code edita archivos, finaliza tareas o necesita entrada. Formatea código, envía notificaciones, valida comandos y aplica reglas del proyecto.
- [Enviar eventos a una sesión en ejecución con channels](https://code.claude.com/docs/es/channels.md): Utilice channels para enviar mensajes, alertas y webhooks a su sesión de Claude Code desde un servidor MCP. Reenvíe resultados de CI, mensajes de chat y eventos de monitoreo para que Claude pueda reaccionar mientras está fuera.
- [Ejecutar prompts en un horario](https://code.claude.com/docs/es/scheduled-tasks.md): Utilice /loop y las herramientas de programación cron para ejecutar prompts repetidamente, sondear el estado o establecer recordatorios únicos dentro de una sesión de Claude Code.
- [Mantener a Claude trabajando hacia un objetivo](https://code.claude.com/docs/es/goal.md): Establezca una condición de finalización con /goal y Claude seguirá trabajando hasta que se cumpla, un modelo juzgue que es imposible, o un error que deba corregir borre el objetivo.
- [Ejecutar Claude Code mediante programación](https://code.claude.com/docs/es/headless.md): Utilice el Agent SDK para ejecutar Claude Code mediante programación desde la CLI, Python o TypeScript.
- [Iniciar sesiones desde enlaces](https://code.claude.com/docs/es/deep-links.md): Abra una sesión de terminal de Claude Code desde una URL. Incruste enlaces `claude-cli://` en runbooks, alertas y paneles para que un clic abra Claude Code en el repositorio correcto con el mensaje correcto.

#### Guías

- [Configurar Claude Code en un monorepo o codebase grande](https://code.claude.com/docs/es/large-codebases.md): Configure Claude Code para monorepos y codebases de árbol único grande con archivos CLAUDE.md anidados, worktrees dispersos, inteligencia de código y skills por paquete para que Claude se mantenga enfocado en el código en el que está trabajando.

#### Solución de problemas

- [Solucionar problemas de instalación e inicio de sesión](https://code.claude.com/docs/es/troubleshoot-install.md): Corrija errores de comando no encontrado, PATH, permisos, red y autenticación al instalar o iniciar sesión en Claude Code.
- [Solución de problemas](https://code.claude.com/docs/es/troubleshooting.md): Corrige el alto uso de CPU o memoria, cuelgues, thrashing de auto-compact, y problemas de búsqueda en Claude Code, y encuentra la página correcta para otros problemas.
- [Depura tu configuración](https://code.claude.com/docs/es/debug-your-config.md): Diagnostica por qué CLAUDE.md, configuración, hooks, servidores MCP o skills no están surtiendo efecto. Usa /context, /doctor, /hooks y /mcp para ver qué se cargó realmente.
- [Referencia de errores](https://code.claude.com/docs/es/errors.md): Busque mensajes de error en tiempo de ejecución de Claude Code con lo que cada uno significa y cómo solucionarlo.

### Administración

#### Configuración y acceso

- [Configurar Claude Code para su organización](https://code.claude.com/docs/es/admin-setup.md): Un mapa de decisiones para administradores que implementan Claude Code, cubriendo proveedores de API, configuración administrada, aplicación de políticas, monitoreo de uso y manejo de datos.
- [Configuración avanzada](https://code.claude.com/docs/es/setup.md): Requisitos del sistema, instalación específica de plataforma, gestión de versiones y desinstalación para Claude Code.
- [Autenticación](https://code.claude.com/docs/es/authentication.md): Inicie sesión en Claude Code y configure la autenticación para individuos, equipos y organizaciones.
- [Implementar configuración administrada](https://code.claude.com/docs/es/managed-settings.md): Implementar configuración administrada en la máquina de cada desarrollador: mecanismos de entrega por SO, cómo Claude Code combina fuentes administradas y cómo verificar la aplicación.
- [Configurar la configuración administrada por servidor](https://code.claude.com/docs/es/server-managed-settings.md): Configure Claude Code centralmente para su organización a través de configuración entregada por servidor, sin requerir infraestructura de administración de dispositivos.
- [Controlar el acceso a servidores MCP para su organización](https://code.claude.com/docs/es/managed-mcp.md): Restrinja qué servidores MCP pueden agregar o conectar los usuarios, o proporcione servidores a todos los usuarios, con archivos de configuración administrados, configuración administrada, listas de permitidos y listas de denegados.
- [Configurar el modo automático](https://code.claude.com/docs/es/auto-mode-config.md): Indique al clasificador del modo automático qué repositorios, buckets y dominios confía su organización. Establezca el contexto del entorno, anule las reglas de bloqueo y permiso predeterminadas e inspeccione su configuración efectiva con los subcomandos de la CLI del modo automático.

#### Implementación

- [Descripción general de implementación empresarial](https://code.claude.com/docs/es/third-party-integrations.md): Aprenda cómo Claude Code puede integrarse con varios servicios de terceros e infraestructura para cumplir con los requisitos de implementación empresarial.
- [Disponibilidad de características](https://code.claude.com/docs/es/feature-availability.md): Compare qué características de Claude Code están disponibles en los planes de suscripción de Anthropic, la Consola de Anthropic, Amazon Bedrock, Claude Platform en AWS, Google Cloud's Agent Platform y Microsoft Foundry.
- [Claude Code en Amazon Bedrock](https://code.claude.com/docs/es/amazon-bedrock.md): Aprenda a configurar Claude Code a través de Amazon Bedrock, incluyendo configuración, configuración de IAM y solución de problemas.
- [Claude Code en Claude Platform on AWS](https://code.claude.com/docs/es/claude-platform-on-aws.md): Configure Claude Code para usar la API de Claude operada por Anthropic con autenticación de AWS, control de acceso IAM y facturación de AWS Marketplace.
- [Claude Code en la Plataforma de Agentes de Google Cloud](https://code.claude.com/docs/es/google-vertex-ai.md): Aprenda a configurar Claude Code a través de la Plataforma de Agentes de Google Cloud, anteriormente Vertex AI, incluida la configuración, la configuración de IAM y la solución de problemas.
- [Claude Code en Microsoft Foundry](https://code.claude.com/docs/es/microsoft-foundry.md): Aprende a configurar Claude Code a través de Microsoft Foundry, incluyendo configuración, instalación y solución de problemas.
- [Configuración de red empresarial](https://code.claude.com/docs/es/network-config.md): Configure Claude Code para entornos empresariales con servidores proxy, Autoridades de Certificación (CA) personalizadas y autenticación mutua de Seguridad de la Capa de Transporte (mTLS).
- [Ejecutar Claude Code detrás de un lanzador corporativo](https://code.claude.com/docs/es/corporate-launcher.md): Enrute los procesos que Claude Code inicia desde su propio binario, incluido el servicio de fondo y cada sesión de vista de agente, a través de un lanzador requerido con CLAUDE_CODE_PROCESS_WRAPPER o la configuración processWrapper.
- [Contenedores de desarrollo](https://code.claude.com/docs/es/devcontainer.md): Ejecuta Claude Code dentro de un contenedor de desarrollo para entornos consistentes e aislados en todo tu equipo.

#### Puertas de enlace

- [Ejecutar Claude Code a través de una puerta de enlace](https://code.claude.com/docs/es/gateways.md): Enrute Claude Code a través de una puerta de enlace autohospedada para credenciales centralizadas, seguimiento de uso y controles de costos. Cubre la arquitectura, la puerta de enlace de aplicaciones Claude de Anthropic y el uso de otros productos de puerta de enlace.

##### Puerta de enlace de aplicaciones Claude

- [Puerta de enlace de aplicaciones Claude para Amazon Bedrock, Claude Platform en AWS, Google Cloud y Microsoft Foundry](https://code.claude.com/docs/es/claude-apps-gateway.md): Ejecute Claude Code a través de Amazon Bedrock, Claude Platform en AWS, Google Cloud o Microsoft Foundry detrás de una puerta de enlace autohospedada con inicio de sesión SSO, acceso a modelos por grupo y telemetría OTLP.
- [Configuración de la puerta de enlace de aplicaciones Claude](https://code.claude.com/docs/es/claude-apps-gateway-config.md): Referencia para cada opción de gateway.yaml: listener y TLS, OIDC, sesión, almacén Postgres, upstream de Bedrock, Claude Platform en AWS, Agent Platform de Google Cloud y Microsoft Foundry, enrutamiento de modelos, políticas administradas y telemetría.
- [Límites de gasto de la puerta de enlace de aplicaciones Claude](https://code.claude.com/docs/es/claude-apps-gateway-spend-limits.md): Limite el gasto de cada desarrollador a través de la puerta de enlace de aplicaciones Claude por día, semana o mes. Establezca límites con una API de administrador y la puerta de enlace los aplica en vivo en cada solicitud.
- [Implementación y operaciones de la puerta de enlace de aplicaciones Claude](https://code.claude.com/docs/es/claude-apps-gateway-deploy.md): Registre la puerta de enlace con su IdP, construya el contenedor, implemente en Kubernetes o Cloud Run, y opérelo: verificaciones de salud, rotación de secretos, actualizaciones y seguridad.
- [Implementar Claude apps gateway en AWS](https://code.claude.com/docs/es/claude-apps-gateway-on-aws.md): Un ejemplo práctico de ejecutar Claude apps gateway en AWS: ECS Fargate o EKS, Amazon RDS para PostgreSQL, AWS Secrets Manager, y autenticación basada en roles de IAM a Amazon Bedrock.
- [Implementar Claude apps gateway en Google Cloud](https://code.claude.com/docs/es/claude-apps-gateway-on-gcp.md): Un ejemplo práctico de ejecutar Claude apps gateway en Google Cloud: Cloud Run o GKE, Cloud SQL para PostgreSQL, Secret Manager y autenticación de cuenta de servicio en Agent Platform de Google Cloud.

##### Otras puertas de enlace

- [Otras puertas de enlace LLM](https://code.claude.com/docs/es/llm-gateway.md): Enrute Claude Code a través de una puerta de enlace LLM que su organización ya ejecuta. Cubre la conexión de Claude Code a una puerta de enlace, el despliegue de una para su organización, y qué envía Claude Code a una puerta de enlace.
- [Conectar Claude Code a una puerta de enlace LLM](https://code.claude.com/docs/es/llm-gateway-connect.md): Apunte Claude Code a la puerta de enlace LLM de su organización. Compruebe si su administrador ya la configuró, o establezca la URL base y las credenciales usted mismo, luego verifique la conexión y corrija los errores de la puerta de enlace.
- [Implementar una puerta de enlace LLM para su organización](https://code.claude.com/docs/es/llm-gateway-rollout.md): Implemente un producto de puerta de enlace para Claude Code: configúrelo para reenviar lo que Claude Code envía, emita credenciales de desarrollador, distribuya la configuración a través de ajustes administrados y verifique la implementación.
- [Guía de compatibilidad de Claude Code gateway](https://code.claude.com/docs/es/llm-gateway-protocol.md): Mantenga un gateway LLM compatible con Claude Code: los endpoints que llama, los encabezados y campos de cuerpo a reenviar, y qué se rompe cuando se eliminan.

#### Uso y costos

- [Monitoreo](https://code.claude.com/docs/es/monitoring-usage.md): Aprende cómo habilitar y configurar OpenTelemetry para Claude Code.
- [Gestionar costos de manera efectiva](https://code.claude.com/docs/es/costs.md): Realice un seguimiento del uso de tokens, establezca límites de gasto del equipo y reduzca los costos de Claude Code con la gestión del contexto, la selección de modelos, la configuración del pensamiento extendido y los hooks de preprocesamiento.
- [Rastrear el uso del equipo con análisis](https://code.claude.com/docs/es/analytics.md): Ver métricas de uso de Claude Code, rastrear la adopción y medir la velocidad de ingeniería en el panel de análisis.

#### Distribución de plugins

- [Crear y distribuir un marketplace de plugins](https://code.claude.com/docs/es/plugin-marketplaces.md): Cree y aloje marketplaces de plugins para distribuir extensiones de Claude Code en equipos y comunidades.
- [Restringir versiones de dependencias de plugins](https://code.claude.com/docs/es/plugin-dependencies.md): Declare restricciones de versión en las dependencias de plugins e incluya un conjunto de plugins curado detrás de una única instalación.
- [Recomienda tu plugin desde tu CLI](https://code.claude.com/docs/es/plugin-hints.md): Emite un marcador de una línea desde tu CLI para que Claude Code solicite a los usuarios instalar tu plugin oficial.
- [Recomendar plugins para su organización](https://code.claude.com/docs/es/plugin-relevance.md): Agregue un bloque de relevancia a las entradas de plugins del marketplace para que Claude Code los sugiera cuando el trabajo de un usuario coincida.

#### Seguridad y datos

- [Seguridad](https://code.claude.com/docs/es/security.md): Aprenda sobre las medidas de seguridad de Claude Code y las mejores prácticas para un uso seguro.
- [Uso de datos](https://code.claude.com/docs/es/data-usage.md): Conozca las políticas de uso de datos de Anthropic para Claude
- [Retención cero de datos](https://code.claude.com/docs/es/zero-data-retention.md): Obtenga información sobre la Retención Cero de Datos (ZDR) para Claude Code, disponible para cuentas calificadas en Claude for Enterprise, incluido el alcance, las características deshabilitadas y cómo solicitar la habilitación.

#### Adopción

- [Kit de comunicaciones](https://code.claude.com/docs/es/communications-kit.md): Anuncios de lanzamiento, mensajes de campaña de goteo y respuestas de preguntas frecuentes para implementar Claude Code en su organización de ingeniería.
- [Kit de campeón](https://code.claude.com/docs/es/champion-kit.md): Un manual para ingenieros que defienden Claude Code internamente: qué compartir, cómo responder preguntas y cómo aumentar la adopción en su equipo.

### Configuración

#### Configuración

- [Archivos de configuración y precedencia](https://code.claude.com/docs/es/settings.md): Cambie la configuración de Claude Code, elija el ámbito al que pertenece una clave, verifique el cambio y aprenda qué valor usa Claude Code cuando una clave se establece en varios lugares.
- [Toda la configuración](https://code.claude.com/docs/es/settings-reference.md): Referencia completa para cada clave settings.json de Claude Code: dónde va cada una, su tipo y valor predeterminado, y un ejemplo listo para pegar, con un índice de cada clave.
- [Archivos de configuración de ejemplo](https://code.claude.com/docs/es/settings-example.md): Archivos settings.json realistas para un desarrollador, un equipo y una organización: copie uno, mantenga las claves que desee y cambie los valores.

#### Permisos y sandboxing

- [Configurar permisos](https://code.claude.com/docs/es/permissions.md): Controle lo que Claude Code puede acceder y hacer con reglas de permisos granulares, modos y políticas administradas.
- [Elegir un modo de permisos](https://code.claude.com/docs/es/permission-modes.md): Controle si Claude solicita aprobación antes de actuar. Cambie de modo de permisos con Mayús+Tab en la CLI, el indicador de modo en VS Code, o el selector de modo en Desktop.
- [Configurar la herramienta Bash aislada](https://code.claude.com/docs/es/sandboxing.md): Aprenda cómo la herramienta Bash aislada de Claude Code proporciona aislamiento del sistema de archivos y la red para una ejecución de agentes más segura y autónoma.
- [Elegir un entorno sandbox](https://code.claude.com/docs/es/sandbox-environments.md): Compare las opciones de sandbox de Claude Code: la herramienta Bash aislada integrada, el tiempo de ejecución sandbox, contenedores de desarrollo, Docker y máquinas virtuales. Elija el aislamiento adecuado para su modelo de amenaza.

#### Entornos

- [Configurar entornos en la nube](https://code.claude.com/docs/es/cloud-environments.md): Configure entornos en la nube para sesiones en la nube de Claude Code: niveles de acceso a la red, variables de entorno, scripts de configuración y almacenamiento en caché de entornos.

##### Entornos autohospedados

- [Entornos autohospedados](https://code.claude.com/docs/es/self-hosted-environments.md): Ejecute sesiones en la nube de Claude Code en la infraestructura que controla: configure un entorno autohospedado, implemente ejecutores y enrute sesiones a su propio cómputo.
- [Guía de inicio rápido de entornos autohospedados](https://code.claude.com/docs/es/self-hosted-environments-quickstart.md): Configure su primer entorno autohospedado: instale Claude Code, cree el entorno, inicie un runner y enrute una sesión hacia él.
- [Implementar entornos autohospedados en producción](https://code.claude.com/docs/es/self-hosted-environments-deploy.md): Ejecutar runners autohospedados en producción: endurecimiento de seguridad, control de salida de red, credenciales de git, recetas de Kubernetes y Compose, y solución de problemas.
- [Personalizar sesiones en entornos autohospedados](https://code.claude.com/docs/es/self-hosted-environments-configuration.md): Personaliza sesiones de entornos autohospedados con scripts contenedores para credenciales por sesión, hooks de ciclo de vida y generación de ejecutores bajo demanda.
- [Probar entornos autohospedados de extremo a extremo](https://code.claude.com/docs/es/self-hosted-environments-testing.md): Verifique una imagen de ejecutor autohospedado desde CI: envíe una sesión con la CLI, lea las respuestas de Claude a través de un hook Stop y ejecute el bucle completo.
- [Referencia de entornos autohospedados](https://code.claude.com/docs/es/self-hosted-environments-reference.md): Referencia completa para el ejecutor y orquestador autohospedados: banderas CLI, variables de entorno y métricas de Prometheus.
- [Verificar la identidad de la sesión en entornos autohospedados](https://code.claude.com/docs/es/self-hosted-environments-identity.md): Verifique el JWT CLAUDE_CODE_SESSION_ACCESS_TOKEN para que los servicios en su red puedan confiar en las solicitudes de sesiones en su entorno autohospedado.

#### Modelo y respuestas

- [Configuración del modelo](https://code.claude.com/docs/es/model-config.md): Configure qué modelo utiliza Claude Code, niveles de esfuerzo, contexto extendido y la ventana de auto-compact
- [Acelera las respuestas con el modo rápido](https://code.claude.com/docs/es/fast-mode.md): Obtén respuestas más rápidas de Opus en Claude Code al activar el modo rápido.
- [Escalar decisiones difíciles con la herramienta advisor](https://code.claude.com/docs/es/advisor.md): Empareje su modelo principal con un modelo advisor más fuerte que Claude consulta en momentos clave durante una tarea.
- [Estilos de salida](https://code.claude.com/docs/es/output-styles.md): Adapte Claude Code para usos más allá de la ingeniería de software

#### Interfaz

- [Configura tu terminal para Claude Code](https://code.claude.com/docs/es/terminal-config.md): Corrige Shift+Enter para saltos de línea, obtén una campana de terminal cuando Claude termine, configura tmux, coincide con el tema de color y habilita el modo Vim en la CLI de Claude Code.
- [Renderizado a pantalla completa](https://code.claude.com/docs/es/fullscreen.md): Habilite un modo de renderizado más suave y sin parpadeos con soporte de ratón y uso de memoria estable en conversaciones largas.
- [Usar Claude Code con un lector de pantalla](https://code.claude.com/docs/es/accessibility.md): Configure Claude Code para lectores de pantalla como VoiceOver y NVDA, además de configuración para ampliadores de pantalla, movimiento reducido y temas seguros para daltónicos.
- [Dictado de voz](https://code.claude.com/docs/es/voice-dictation.md): Hable sus indicaciones en la CLI de Claude Code con dictado de voz de mantener para grabar o tocar para grabar.
- [Personaliza tu línea de estado](https://code.claude.com/docs/es/statusline.md): Configura una barra de estado personalizada para monitorear el uso de la ventana de contexto, costos y estado de git en Claude Code
- [Personalizar atajos de teclado](https://code.claude.com/docs/es/keybindings.md): Personaliza atajos de teclado en Claude Code con un archivo de configuración de keybindings.

### Referencia

#### Referencia

- [Referencia de CLI](https://code.claude.com/docs/es/cli-reference.md): Referencia completa de la interfaz de línea de comandos de Claude Code, incluyendo comandos y banderas.
- [Comandos](https://code.claude.com/docs/es/commands.md): Referencia completa de comandos disponibles en Claude Code, incluidos comandos integrados y skills incluidas.
- [Variables de entorno](https://code.claude.com/docs/es/env-vars.md): Referencia para variables de entorno que controlan el comportamiento de Claude Code.
- [Referencia de herramientas](https://code.claude.com/docs/es/tools-reference.md): Referencia completa de las herramientas que Claude Code puede usar, incluidos los requisitos de permisos y el comportamiento por herramienta.
- [Modo interactivo](https://code.claude.com/docs/es/interactive-mode.md): Referencia completa de atajos de teclado, modos de entrada y características interactivas en sesiones de Claude Code.
- [Checkpointing](https://code.claude.com/docs/es/checkpointing.md): Realiza un seguimiento, revierte y resume las ediciones y conversaciones de Claude para gestionar el estado de la sesión.
- [Referencia de hooks](https://code.claude.com/docs/es/hooks.md): Referencia para eventos de hooks de Claude Code, esquema de configuración, formatos de entrada/salida JSON, códigos de salida, hooks asincronos, hooks HTTP, hooks de prompt y hooks de herramientas MCP.
- [Referencia de plugins](https://code.claude.com/docs/es/plugins-reference.md): Referencia técnica completa para el sistema de plugins de Claude Code, incluyendo esquemas, comandos CLI y especificaciones de componentes.
- [Referencia de canales](https://code.claude.com/docs/es/channels-reference.md): Construye un servidor MCP que envíe webhooks, alertas y mensajes de chat a una sesión de Claude Code. Referencia para el contrato de canal: declaración de capacidad, eventos de notificación, herramientas de respuesta, compuerta de remitente y retransmisión de permisos.

#### Glosario

- [Glosario](https://code.claude.com/docs/es/glossary.md): Definiciones de terminología de Claude Code. Aprenda qué significan agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP y otros conceptos centrales.

### SDK de Agente

#### SDK de Agente

- [Descripción general del Agent SDK](https://code.claude.com/docs/es/agent-sdk/overview.md): Construya agentes de IA en producción con Claude Code como una biblioteca
- [Inicio rápido](https://code.claude.com/docs/es/agent-sdk/quickstart.md): Comience con el SDK de Agent de Python o TypeScript para crear agentes de IA que funcionen de forma autónoma
- [Migrar a Claude Agent SDK](https://code.claude.com/docs/es/agent-sdk/migration-guide.md): Guía para migrar los SDK de TypeScript y Python de Claude Code al Claude Agent SDK
- [Solucionar problemas del Agent SDK](https://code.claude.com/docs/es/agent-sdk/troubleshooting.md): Corrija los errores del Agent SDK por el mensaje exacto que ve, con la causa y la solución para cada error en los SDK de TypeScript y Python.

#### Crear agentes

- [Configura tu agente](https://code.claude.com/docs/es/agent-sdk/configuration.md): Configura sesiones del Agent SDK: compone el objeto de opciones, establece el modelo, el entorno y los límites, y encuentra la página de cada opción de característica.
- [Ejemplos](https://code.claude.com/docs/es/agent-sdk/examples.md): Encuentra un proyecto completo y ejecutable del Agent SDK o una receta guiada en el Claude Cookbook que coincida con lo que deseas construir.

#### Conceptos fundamentales

- [Cómo funciona el bucle del agente](https://code.claude.com/docs/es/agent-sdk/agent-loop.md): Comprenda el ciclo de vida de los mensajes, la ejecución de herramientas, la ventana de contexto y la arquitectura que potencia sus agentes SDK.
- [Usar características de Claude Code en el SDK](https://code.claude.com/docs/es/agent-sdk/claude-code-features.md): Cargue instrucciones de proyecto, skills, hooks y otras características de Claude Code en sus agentes SDK.
- [Trabajar con sesiones](https://code.claude.com/docs/es/agent-sdk/sessions.md): Cómo las sesiones persisten el historial de conversación del agente, y cuándo usar continue, resume y fork para volver a una ejecución anterior.
- [Persistir sesiones en almacenamiento externo](https://code.claude.com/docs/es/agent-sdk/session-storage.md): Refleja transcripciones de sesiones del SDK de Agent en su propio almacén de objetos, almacén de clave-valor o base de datos para que otros hosts puedan reanudar sus sesiones.

#### Entrada y salida

- [Entrada de Streaming](https://code.claude.com/docs/es/agent-sdk/streaming-vs-single-mode.md): Comprensión de los dos modos de entrada para Claude Agent SDK y cuándo usar cada uno
- [Gestionar aprobaciones e entrada de usuario](https://code.claude.com/docs/es/agent-sdk/user-input.md): Presente las solicitudes de aprobación y preguntas aclaratorias de Claude a los usuarios, luego devuelva sus decisiones al SDK.
- [Transmitir respuestas en tiempo real](https://code.claude.com/docs/es/agent-sdk/streaming-output.md): Obtener respuestas en tiempo real del Agent SDK mientras el texto y las llamadas de herramientas se transmiten
- [Obtener salida estructurada de agentes](https://code.claude.com/docs/es/agent-sdk/structured-outputs.md): Devuelve JSON validado desde flujos de trabajo de agentes usando JSON Schema, Zod o Pydantic. Obtén datos estructurados seguros en tipos después del uso de herramientas de múltiples turnos.

#### Extender con herramientas

- [Dale a Claude herramientas personalizadas](https://code.claude.com/docs/es/agent-sdk/custom-tools.md): Define herramientas personalizadas con el servidor MCP en proceso del SDK del Agente Claude para que Claude pueda llamar a sus funciones, acceder a sus APIs y realizar operaciones específicas del dominio.
- [Conectar con herramientas externas usando MCP](https://code.claude.com/docs/es/agent-sdk/mcp.md): Configure servidores MCP para extender su agente con herramientas externas. Cubre tipos de transporte, búsqueda de herramientas para conjuntos grandes de herramientas, autenticación y manejo de errores.
- [Escala a muchas herramientas con búsqueda de herramientas](https://code.claude.com/docs/es/agent-sdk/tool-search.md): Escala tu agente a miles de herramientas descubriendo y cargando solo lo que se necesita, bajo demanda.
- [Subagentes en el SDK](https://code.claude.com/docs/es/agent-sdk/subagents.md): Define e invoque subagentes para aislar contexto, ejecutar tareas en paralelo y aplicar instrucciones especializadas en sus aplicaciones de Claude Agent SDK.

#### Personalizar comportamiento

- [Modificación de indicaciones del sistema](https://code.claude.com/docs/es/agent-sdk/modifying-system-prompts.md): Elija entre el preset `claude_code` y una indicación del sistema personalizada, y personalice el comportamiento con CLAUDE.md, estilos de salida, append, o una indicación completamente personalizada.
- [Extienda agentes con skills](https://code.claude.com/docs/es/agent-sdk/skills.md): Controle qué skills puede invocar Claude en sesiones del Claude Agent SDK, despache comandos por nombre y cree skills que sus sesiones descubran
- [Plugins en el SDK](https://code.claude.com/docs/es/agent-sdk/plugins.md): Cargue plugins personalizados para extender Claude Code con skills, agentes, hooks y servidores MCP a través del Agent SDK

#### Control y observabilidad

- [Configurar permisos](https://code.claude.com/docs/es/agent-sdk/permissions.md): Controle cómo su agente utiliza herramientas con modos de permiso, hooks y reglas declarativas de permitir/denegar.
- [Interceptar y controlar el comportamiento del agente con hooks](https://code.claude.com/docs/es/agent-sdk/hooks.md): Interceptar y personalizar el comportamiento del agente en puntos clave de ejecución con hooks
- [Revertir cambios de archivos con checkpointing](https://code.claude.com/docs/es/agent-sdk/file-checkpointing.md): Rastrear cambios de archivos durante sesiones de agente y restaurar archivos a cualquier estado anterior
- [Rastrear costo y uso](https://code.claude.com/docs/es/agent-sdk/cost-tracking.md): Aprenda a rastrear el uso de tokens, estimar costos y configurar el almacenamiento en caché de prompts con el SDK del Agente Claude.
- [Observabilidad con OpenTelemetry](https://code.claude.com/docs/es/agent-sdk/observability.md): Exporte trazas, métricas y eventos del Agent SDK a su backend de observabilidad usando OpenTelemetry.
- [Rastrear tareas](https://code.claude.com/docs/es/agent-sdk/todo-tracking.md): Rastrear tareas en sesiones del SDK del Agente y renderizar el progreso de Claude en su aplicación desde llamadas de herramientas estructuradas

#### Implementación

- [Alojamiento del Agent SDK](https://code.claude.com/docs/es/agent-sdk/hosting.md): Implemente el Agent SDK en producción: arquitectura de subprocesos, persistencia de sesiones, escalado, observabilidad e aislamiento multiinquilino para Docker, Kubernetes y proveedores de sandbox.
- [Despliegue seguro de agentes de IA](https://code.claude.com/docs/es/agent-sdk/secure-deployment.md): Una guía para asegurar despliegues de Claude Code y Agent SDK con aislamiento, gestión de credenciales y controles de red

#### Referencias de SDK

- [Referencia del SDK de Agent - TypeScript](https://code.claude.com/docs/es/agent-sdk/typescript.md): Referencia completa de la API del SDK de Agent de TypeScript, incluyendo todas las funciones, tipos e interfaces.
- [API de sesión de TypeScript SDK V2 (eliminada)](https://code.claude.com/docs/es/agent-sdk/typescript-v2-preview.md): Referencia para la API de sesión eliminada V2 del SDK del Agente TypeScript, con patrones de envío/transmisión basados en sesiones para conversaciones de múltiples turnos.
- [Referencia del SDK de Agent - Python](https://code.claude.com/docs/es/agent-sdk/python.md): Referencia completa de la API del SDK de Agent de Python, incluyendo todas las funciones, tipos y clases.

### Novedades

#### Novedades

- [Novedades](https://code.claude.com/docs/es/whats-new/index.md): Un resumen semanal de las características notables de Claude Code, con fragmentos de código, demostraciones y contexto sobre por qué importan.
- [Semana 37 · 7–11 de septiembre de 2026](https://code.claude.com/docs/es/whats-new/2026-w37.md): Prueba tus plugins con claude plugin eval y extrae los paneles de Claude Code Desktop en sus propias ventanas.
- [Semana 36 · 31 de agosto – 4 de septiembre de 2026](https://code.claude.com/docs/es/whats-new/2026-w36.md): Cambia a Claude Fable 5.1, permite que el computer use se ejecute en segundo plano en Desktop, y observa las ediciones de Claude en un panel /diff en vivo.
- [Semana 35 · 24–28 de agosto de 2026](https://code.claude.com/docs/es/whats-new/2026-w35.md): Reanude sesiones de terminal en la aplicación Claude Code Desktop, revise informes de comentarios que Claude redacta para usted e inicie una sesión en modo restringido.
- [Semana 34 · 17–21 de agosto de 2026](https://code.claude.com/docs/es/whats-new/2026-w34.md): Cree artboards de interfaz de usuario editables con la skill /design, establezca el estilo de salida Concise y comience una sesión de Claude Code en su máquina desde su teléfono.
- [Semana 33 · 10–14 de agosto de 2026](https://code.claude.com/docs/es/whats-new/2026-w33.md): Claude Code Desktop continúa automáticamente después de que se restablece un límite de uso, el modo fork se activa de forma predeterminada, y las solicitudes de fusión de GitLab y los marketplaces se unen a GitHub.
- [Semana 32 · 3–7 de agosto de 2026](https://code.claude.com/docs/es/whats-new/2026-w32.md): Las sesiones de Claude Code se envían mensajes entre sí, los entornos autohospedados ejecutan sesiones en la nube en su infraestructura, y el modo automático se convierte en el modo de permiso predeterminado.
- [Semana 30 · 20–24 de julio de 2026](https://code.claude.com/docs/es/whats-new/2026-w30.md): Opus 5 se convierte en el modelo Opus predeterminado, Claude Code Desktop añade un panel del Simulador de iOS, y el plugin Claude Security escanea su código en busca de vulnerabilidades.
- [Semana 29 · 13–17 de julio de 2026](https://code.claude.com/docs/es/whats-new/2026-w29.md): Extraiga datos en vivo en artefactos publicados a través de conectores MCP y use Claude Code con un lector de pantalla en el nuevo modo de lector de pantalla.
- [Semana 28 · 6–10 de julio de 2026](https://code.claude.com/docs/es/whats-new/2026-w28.md): Navegue por sitios externos desde el navegador integrado de la aplicación de escritorio, ejecute una verificación completa de configuración con /doctor, y obtenga protecciones de transcripción en modo automático y mejoras en la vista de agentes.
- [Semana 27 · 29 de junio – 3 de julio de 2026](https://code.claude.com/docs/es/whats-new/2026-w27.md): Claude Sonnet 5 se convierte en el modelo predeterminado, Claude en Chrome alcanza disponibilidad general, los subagentes se ejecutan en segundo plano de forma predeterminada, Claude Desktop llega a Linux en versión beta, y /radio sintoniza Claude FM.
- [Semana 26 · 22–26 de junio de 2026](https://code.claude.com/docs/es/whats-new/2026-w26.md): Autentique servidores MCP desde su shell con claude mcp login, obtenga una respuesta a la salida del comando del modo shell con el prefijo !, y reanude una conversación anterior a /clear con /rewind.
- [Semana 25 · 15–19 de junio de 2026](https://code.claude.com/docs/es/whats-new/2026-w25.md): Publique una página en vivo y compartible desde su sesión con Artifacts, haga coincidir parámetros de herramientas en reglas de denegación y solicitud, y configure cualquier ajuste desde el prompt con /config.
- [Semana 24 · 8–12 de junio de 2026](https://code.claude.com/docs/es/whats-new/2026-w24.md): Mueva una sesión a un nuevo directorio con /cd, permita que los sub-agentes generen sus propios sub-agentes, y solucione problemas de una configuración rota con modo seguro.
- [Semana 23 · 1–5 de junio de 2026](https://code.claude.com/docs/es/whats-new/2026-w23.md): Ejecutar modo automático en Amazon Bedrock, Google Cloud's Agent Platform y Microsoft Foundry, solicitar confirmación antes de escribir archivos que pueden ejecutar código en modo acceptEdits, listar plugins instalados con /plugin list, y requerir un rango de versión aprobado para implementaciones a…
- [Semana 22 · 25–29 de mayo de 2026](https://code.claude.com/docs/es/whats-new/2026-w22.md): Ejecuta Claude Code en Claude Opus 4.8, orquesta tareas grandes con flujos de trabajo dinámicos, detecta problemas de seguridad con el plugin security-guidance, y usa el modo rápido en Opus 4.8 a un precio más bajo.
- [Semana 21 · 18–22 de mayo de 2026](https://code.claude.com/docs/es/whats-new/2026-w21.md): Utilice el modo automático en el plan Pro y con Sonnet 4.6, vea qué skills, subagentes y servidores MCP impulsan los límites de su plan en /usage, y revise diffs con el nuevo comando /code-review.
- [Semana 20 · 11–15 de mayo de 2026](https://code.claude.com/docs/es/whats-new/2026-w20.md): Gestione todas las sesiones de Claude Code desde una pantalla con la vista de agente, mantenga a Claude trabajando hacia un objetivo hasta que se cumpla una condición, y ejecute el modo rápido en Opus 4.7 de forma predeterminada.
- [Semana 19 · 4–8 de mayo de 2026](https://code.claude.com/docs/es/whats-new/2026-w19.md): Cargue plugins desde archivos .zip y URLs, busque en el historial de comandos en todos los proyectos con Ctrl+R, cree nuevas worktrees desde HEAD local o la rama predeterminada remota, y bloquee acciones incondicionalmente con reglas de negación dura en modo automático.
- [Semana 18 · 27 de abril – 1 de mayo de 2026](https://code.claude.com/docs/es/whats-new/2026-w18.md): Claude Code en Windows se ejecuta sin Git Bash, claude auth login acepta un código OAuth pegado cuando la devolución de llamada del navegador no puede alcanzar localhost, claude project purge limpia el estado local por proyecto, y pegar una URL de PR en /resume encuentra la sesión que la creó.
- [Semana 17 · 20–24 de abril de 2026](https://code.claude.com/docs/es/whats-new/2026-w17.md): /ultrareview abre como vista previa de investigación, recapitulaciones automáticas de sesión cuando regresa a una terminal, temas de color personalizados que puede crear e implementar en plugins, y un Claude Code rediseñado en la web.
- [Semana 16 · 13–17 de abril de 2026](https://code.claude.com/docs/es/whats-new/2026-w16.md): Claude Opus 4.7 con el nuevo nivel de esfuerzo xhigh, Routines en Claude Code en la web, notificaciones push móviles que alertan a su teléfono cuando Claude lo necesita, un desglose de /usage que muestra qué está impulsando sus límites, y binarios nativos reemplazando el JavaScript empaquetado.
- [Semana 15 · 6–10 de abril de 2026](https://code.claude.com/docs/es/whats-new/2026-w15.md): Planificación en la nube Ultraplan, la herramienta Monitor con /loop de ritmo automático, /team-onboarding para empaquetar su configuración, y /autofix-pr desde su terminal.
- [Semana 14 · 30 de marzo – 3 de abril de 2026](https://code.claude.com/docs/es/whats-new/2026-w14.md): Computer use en la CLI, lecciones interactivas en el producto, renderizado sin parpadeos, anulaciones de tamaño de resultado de MCP por herramienta y ejecutables de plugins en PATH.
- [Semana 13 · 23–27 de marzo de 2026](https://code.claude.com/docs/es/whats-new/2026-w13.md): Modo automático para permisos sin intervención, control de computadora integrado, auto-corrección de PR en la nube, búsqueda de transcripciones y una herramienta PowerShell para Windows.

### Recursos

#### Recursos

- [Legal y cumplimiento](https://code.claude.com/docs/es/legal-and-compliance.md): Acuerdos legales, certificaciones de cumplimiento e información de seguridad para Claude Code.

---

## Claude Code Docs: French

- 官方原文：https://code.claude.com/docs/_llms/fr.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-fr.md`

# Claude Code Docs: French

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## French

### Démarrer

#### Démarrer

- [Aperçu](https://code.claude.com/docs/fr/overview.md): Claude Code est un outil de codage agentique qui lit votre base de code, modifie les fichiers, exécute des commandes et s'intègre à vos outils de développement. Disponible dans votre terminal, IDE, application de bureau et navigateur.
- [Démarrage rapide](https://code.claude.com/docs/fr/quickstart.md): Bienvenue dans Claude Code !
- [Journal des modifications](https://code.claude.com/docs/fr/changelog.md)

#### Concepts fondamentaux

- [Comment fonctionne Claude Code](https://code.claude.com/docs/fr/how-claude-code-works.md): Comprenez la boucle agentive, les outils intégrés et comment Claude Code interagit avec votre projet.
- [Étendre Claude Code](https://code.claude.com/docs/fr/features-overview.md): Comprenez quand utiliser CLAUDE.md, Skills, subagents, hooks, MCP et plugins.
- [Explorez le répertoire .claude](https://code.claude.com/docs/fr/claude-directory.md): Où Claude Code lit CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules et auto memory. Explorez le répertoire .claude dans votre projet et ~/.claude dans votre répertoire personnel.
- [Explorez la fenêtre de contexte](https://code.claude.com/docs/fr/context-window.md): Une simulation interactive de la façon dont la fenêtre de contexte de Claude Code se remplit pendant une session. Voyez ce qui se charge automatiquement, ce que coûte chaque lecture de fichier, et quand les règles et les hooks s'exécutent.
- [Comment Claude Code utilise le prompt caching](https://code.claude.com/docs/fr/prompt-caching.md): Claude Code gère le prompt caching automatiquement. Découvrez pourquoi un changement de modèle déclenche un tour lent sans cache, ce que coûte `/compact`, pourquoi les modifications de CLAUDE.md ne s'appliquent pas en cours de session, et comment vérifier votre taux de cache hit.

#### Utiliser Claude Code

- [Comment Claude se souvient de votre projet](https://code.claude.com/docs/fr/memory.md): Donnez à Claude des instructions persistantes avec les fichiers CLAUDE.md ou AGENTS.md, et laissez Claude accumuler automatiquement les apprentissages avec la mémoire automatique.
- [Gérer les sessions](https://code.claude.com/docs/fr/sessions.md): Nommez, reprenez, créez des branches et basculez entre les conversations Claude Code. Couvre `--continue`, `--resume`, `--from-pr`, le sélecteur `/resume`, la dénomination des sessions, l'export des transcriptions et l'emplacement des transcriptions.
- [Flux de travail courants](https://code.claude.com/docs/fr/common-workflows.md): Guides étape par étape pour explorer les bases de code, corriger les bogues, refactoriser, tester et autres tâches quotidiennes avec Claude Code.
- [Bibliothèque de prompts](https://code.claude.com/docs/fr/prompt-library.md): Copiez-collez des prompts pour Claude Code, étiquetés par tâche et rôle.
- [Meilleures pratiques pour Claude Code](https://code.claude.com/docs/fr/best-practices.md): Conseils et modèles pour tirer le meilleur parti de Claude Code, de la configuration de votre environnement à la mise à l'échelle sur plusieurs sessions parallèles.

#### Plateformes et intégrations

- [Plateformes et intégrations](https://code.claude.com/docs/fr/platforms.md): Choisissez où exécuter Claude Code et ce que vous y connecter. Comparez le CLI, Desktop, VS Code, JetBrains, le web et les intégrations comme Chrome, Slack et CI/CD.
- [Continuer les sessions locales depuis n'importe quel appareil avec Remote Control](https://code.claude.com/docs/fr/remote-control.md): Continuez une session Claude Code locale depuis votre téléphone, tablette ou n'importe quel navigateur en utilisant Remote Control. Fonctionne avec claude.ai/code et l'application Claude mobile.
- [Laissez Claude coordonner le travail en cours avec Projects](https://code.claude.com/docs/fr/claude-projects.md): Donnez à Claude un ensemble de travaux connexes dans une conversation et laissez-le coordonner des sessions cloud parallèles qui partagent des référentiels, des instructions et la mémoire.
- [Claude Code sur mobile](https://code.claude.com/docs/fr/mobile.md): Démarrez, surveillez et pilotez les tâches Claude Code depuis votre téléphone avec l'application Claude pour iOS et Android.
- [Utiliser Claude Code avec Chrome](https://code.claude.com/docs/fr/chrome.md): Connectez Claude Code à votre navigateur Chrome pour tester des applications web, déboguer avec les journaux de console, automatiser le remplissage de formulaires et extraire des données des pages web.
- [Laisser Claude utiliser votre ordinateur depuis la CLI](https://code.claude.com/docs/fr/computer-use.md): Activez l'utilisation de l'ordinateur dans la CLI Claude Code pour que Claude puisse ouvrir des applications, cliquer, taper et voir votre écran sur macOS. Testez les applications natives, déboguez les problèmes visuels et automatisez les outils GUI uniquement sans quitter votre terminal.
- [Utiliser Claude Code dans VS Code](https://code.claude.com/docs/fr/vs-code.md): Installez et configurez l'extension Claude Code pour VS Code. Obtenez une assistance de codage IA avec des diffs en ligne, des mentions @, un examen du plan et des raccourcis clavier.
- [JetBrains IDEs](https://code.claude.com/docs/fr/jetbrains.md): Utilisez Claude Code avec les IDEs JetBrains, notamment IntelliJ, PyCharm, WebStorm et bien d'autres
- [Claude Code dans Slack](https://code.claude.com/docs/fr/slack.md): Déléguez les tâches de codage directement depuis votre espace de travail Slack. Anthropic retire cette version antérieure pour les espaces de travail Team et Enterprise au profit de Claude Tag ; elle reste le chemin de configuration pour les plans Pro et Max.
- [Claude Tag](https://code.claude.com/docs/fr/claude-tag.md): Intégrez Claude dans les canaux Slack de votre équipe avec Claude Tag et trouvez sa documentation de configuration et d'utilisation sur claude.com.

##### Claude Code dans le cloud

- [Démarrer avec Claude Code dans le cloud](https://code.claude.com/docs/fr/web-quickstart.md): Exécutez Claude Code dans le cloud depuis votre navigateur ou téléphone. Connectez un référentiel GitHub, soumettez une tâche et examinez la PR sans configuration locale.
- [Utiliser Claude Code dans le cloud](https://code.claude.com/docs/fr/claude-code-on-the-web.md): Exécutez les sessions Claude Code dans le cloud depuis votre navigateur, téléphone, application de bureau ou terminal, déplacez-les avec --cloud et --teleport, et corrigez automatiquement les demandes de tirage.
- [Automatiser le travail avec les routines](https://code.claude.com/docs/fr/routines.md): Mettez Claude Code en pilotage automatique. Définissez des routines qui s'exécutent selon un calendrier, se déclenchent sur des appels API, ou réagissent aux événements GitHub à partir de l'infrastructure cloud.
- [Trouver des bugs avec ultrareview](https://code.claude.com/docs/fr/ultrareview.md): Exécutez une révision de code approfondie et multi-agents dans le cloud avec /code-review ultra pour trouver et vérifier les bugs avant de fusionner.

##### Claude Code sur ordinateur

- [Démarrer avec l'application de bureau](https://code.claude.com/docs/fr/desktop-quickstart.md): Installez Claude Code sur le bureau et commencez votre première session de codage
- [Application de bureau](https://code.claude.com/docs/fr/desktop.md): Tirez le meilleur parti de Claude Code Desktop : sessions parallèles avec isolation Git, disposition des volets par glisser-déposer, terminal intégré et éditeur de fichiers, chats latéraux, utilisation informatique, sessions Dispatch depuis votre téléphone, examen visuel des différences, aperçus d'a…
- [Claude Desktop sur Linux (bêta)](https://code.claude.com/docs/fr/desktop-linux.md): Installez et mettez à jour l'application de bureau Claude sur Ubuntu et Debian
- [Claude Code Desktop dans WSL](https://code.claude.com/docs/fr/desktop-wsl.md): Exécuter des sessions Code dans une distribution WSL 2 sur Windows
- [Planifier des tâches récurrentes dans Claude Code Desktop](https://code.claude.com/docs/fr/desktop-scheduled-tasks.md): Configurez des tâches planifiées dans Claude Code Desktop pour exécuter Claude automatiquement de manière récurrente pour les révisions de code quotidiennes, les audits de dépendances ou les briefings matinaux.
- [Tester les applications iOS dans le simulateur](https://code.claude.com/docs/fr/desktop-ios-simulator.md): Claude Code Desktop ouvre votre application dans le volet Simulateur iOS lorsque Claude la crée, l'exécute ou la vérifie, avec un simulateur distinct pour chaque session.

##### Révision de code et CI/CD

- [Détecter les problèmes de sécurité au fur et à mesure que Claude écrit du code](https://code.claude.com/docs/fr/security-guidance.md): Installez le plugin security-guidance pour que Claude examine ses propres modifications de code à la recherche de vulnérabilités et les corrige dans la même session.
- [Analysez votre base de code pour détecter les vulnérabilités](https://code.claude.com/docs/fr/claude-security.md): Installez le plugin Claude Security pour analyser votre base de code afin de détecter les vulnérabilités dans une session Claude Code et transformez les résultats en correctifs que vous examinez et appliquez.
- [Révision de code](https://code.claude.com/docs/fr/code-review.md): Configurez des révisions de PR automatisées qui détectent les erreurs logiques, les vulnérabilités de sécurité et les régressions en utilisant l'analyse multi-agents de votre base de code complète
- [Claude Code GitHub Actions](https://code.claude.com/docs/fr/github-actions.md): Exécutez Claude Code dans les workflows GitHub Actions pour répondre aux mentions @claude, automatiser les tâches et transformer les issues en pull requests
- [Utiliser Claude Code GitHub Actions avec les fournisseurs cloud](https://code.claude.com/docs/fr/github-actions-cloud-providers.md): Exécutez Claude Code GitHub Actions via Amazon Bedrock, Google Cloud's Agent Platform ou Microsoft Foundry au lieu de l'API Claude
- [Claude Code avec GitHub Enterprise Server](https://code.claude.com/docs/fr/github-enterprise-server.md): Connectez Claude Code à votre instance GitHub Enterprise Server auto-hébergée pour les sessions cloud, la révision de code et les marketplaces de plugins.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/fr/gitlab-ci-cd.md): Découvrez comment intégrer Claude Code dans votre flux de travail de développement avec GitLab CI/CD

### Créer avec Claude Code

#### Agents et travail parallèle

- [Exécuter des agents en parallèle](https://code.claude.com/docs/fr/agents.md): Comparez les façons dont Claude Code peut gérer plusieurs tâches à la fois : sous-agents, vue agent, équipes d'agents, workflows dynamiques et projets.
- [Créer des sous-agents personnalisés](https://code.claude.com/docs/fr/sub-agents.md): Créez et utilisez des sous-agents IA spécialisés dans Claude Code pour des workflows spécifiques à des tâches et une meilleure gestion du contexte.
- [Gérer plusieurs agents avec la vue agent](https://code.claude.com/docs/fr/agent-view.md): Lancez et gérez plusieurs sessions Claude Code à partir d'un seul écran. La vue agent affiche ce que chaque session fait et lesquelles ont besoin de votre intervention.
- [Orchestrer des équipes de sessions Claude Code](https://code.claude.com/docs/fr/agent-teams.md): Coordonnez plusieurs instances Claude Code travaillant ensemble en tant qu'équipe, avec des tâches partagées, la messagerie inter-agents et la gestion centralisée.
- [Messagerie entre vos autres sessions Claude Code](https://code.claude.com/docs/fr/cross-session-messaging.md): Laissez Claude lister et envoyer des messages à vos autres sessions Claude Code sur cette machine, et atteindre vos sessions sur d'autres machines ou sur le web.
- [Orchestrer des sous-agents à grande échelle avec des workflows dynamiques](https://code.claude.com/docs/fr/workflows.md): Les workflows dynamiques orchestrent de nombreux sous-agents à partir d'un script que Claude écrit et que vous pouvez relancer. Utilisez-les pour les audits de base de code, les migrations importantes et la recherche avec vérification croisée.
- [Exécuter des sessions parallèles avec worktrees](https://code.claude.com/docs/fr/worktrees.md): Isolez les sessions Claude Code parallèles dans des git worktrees séparés pour que les modifications ne se heurtent pas. Couvre le flag `--worktree`, l'isolation des subagents, `.worktreeinclude`, le nettoyage et les hooks VCS non-git.

#### MCP

- [Se connecter aux serveurs MCP](https://code.claude.com/docs/fr/mcp-quickstart.md): Ajoutez un serveur MCP à Claude Code, vérifiez la connexion et trouvez la configuration sur le disque.
- [Connecter Claude Code aux outils via MCP](https://code.claude.com/docs/fr/mcp.md): Découvrez comment connecter Claude Code à vos outils avec le Model Context Protocol.

#### Skills

- [Étendre Claude avec des skills](https://code.claude.com/docs/fr/skills.md): Créez, gérez et partagez des skills pour étendre les capacités de Claude dans Claude Code. Inclut les commandes personnalisées et les skills groupées.

#### Plugins

- [Découvrir et installer des plugins prédéfinis via les marketplaces](https://code.claude.com/docs/fr/discover-plugins.md): Trouvez et installez des plugins depuis les marketplaces pour étendre Claude Code avec de nouvelles compétences, agents et capacités.
- [Créer des plugins](https://code.claude.com/docs/fr/plugins.md): Créez des plugins personnalisés pour étendre Claude Code avec des skills, des agents, des hooks et des serveurs MCP.
- [Tester les plugins avec des evals](https://code.claude.com/docs/fr/plugin-evals.md): Écrivez des cas d'eval pour votre plugin Claude Code, exécutez-les avec claude plugin eval, notez les résultats, comparez-les avec une base de référence sans plugin et contrôlez CI sur le score.

#### Artefacts

- [Partager la sortie de session en tant qu'artefacts](https://code.claude.com/docs/fr/artifacts.md): Les artefacts transforment le travail de Claude Code en pages en direct et interactives sur claude.ai que vous pouvez garder privées, partager avec votre organisation ou publier via un lien public.

#### Automatisation

- [Automatiser les actions avec les hooks](https://code.claude.com/docs/fr/hooks-guide.md): Exécutez automatiquement des commandes shell lorsque Claude Code modifie des fichiers, termine des tâches ou a besoin d'une entrée. Formatez le code, envoyez des notifications, validez les commandes et appliquez les règles du projet.
- [Envoyer des événements dans une session active avec les canaux](https://code.claude.com/docs/fr/channels.md): Utilisez les canaux pour envoyer des messages, des alertes et des webhooks dans votre session Claude Code à partir d'un serveur MCP. Transférez les résultats CI, les messages de chat et les événements de surveillance pour que Claude puisse réagir en votre absence.
- [Exécuter des prompts selon un calendrier](https://code.claude.com/docs/fr/scheduled-tasks.md): Utilisez /loop et les outils de planification cron pour exécuter des prompts de manière répétée, interroger l'état ou définir des rappels ponctuels dans une session Claude Code.
- [Garder Claude orienté vers un objectif](https://code.claude.com/docs/fr/goal.md): Définissez une condition d'achèvement avec /goal et Claude continue de travailler jusqu'à ce qu'elle soit satisfaite, qu'un modèle la juge impossible, ou qu'une erreur que vous devez corriger efface l'objectif.
- [Exécuter Claude Code par programmation](https://code.claude.com/docs/fr/headless.md): Utilisez l'Agent SDK pour exécuter Claude Code par programmation depuis la CLI, Python ou TypeScript.
- [Lancer des sessions à partir de liens](https://code.claude.com/docs/fr/deep-links.md): Ouvrir une session de terminal Claude Code à partir d'une URL. Intégrez des liens `claude-cli://` dans les runbooks, les alertes et les tableaux de bord pour qu'un clic ouvre Claude Code dans le bon dépôt avec la bonne invite.

#### Guides

- [Configurer Claude Code dans un monorepo ou un grand dépôt de code](https://code.claude.com/docs/fr/large-codebases.md): Configurez Claude Code pour les monorepos et les grands dépôts à arborescence unique avec des fichiers CLAUDE.md imbriqués, des worktrees clairsemés, l'intelligence du code et des skills par package afin que Claude reste concentré sur le code sur lequel vous travaillez.

#### Dépannage

- [Dépanner l'installation et la connexion](https://code.claude.com/docs/fr/troubleshoot-install.md): Corrigez les erreurs de commande introuvable, PATH, permission, réseau et authentification lors de l'installation ou de la connexion à Claude Code.
- [Dépannage](https://code.claude.com/docs/fr/troubleshooting.md): Corrigez l'utilisation élevée du CPU ou de la mémoire, les blocages, le thrashing de l'auto-compaction et les problèmes de recherche dans Claude Code, et trouvez la bonne page pour d'autres problèmes.
- [Déboguer votre configuration](https://code.claude.com/docs/fr/debug-your-config.md): Diagnostiquez pourquoi CLAUDE.md, les paramètres, les hooks, les serveurs MCP ou les skills ne prennent pas effet. Utilisez /context, /doctor, /hooks et /mcp pour voir ce qui a réellement été chargé.
- [Référence des erreurs](https://code.claude.com/docs/fr/errors.md): Consultez les messages d'erreur d'exécution de Claude Code avec leur signification et comment les corriger.

### Administration

#### Configuration et accès

- [Configurer Claude Code pour votre organisation](https://code.claude.com/docs/fr/admin-setup.md): Une carte de décision pour les administrateurs déployant Claude Code, couvrant les fournisseurs d'API, les paramètres gérés, l'application des politiques, la surveillance de l'utilisation et la gestion des données.
- [Configuration avancée](https://code.claude.com/docs/fr/setup.md): Configuration requise, installation spécifique à la plateforme, gestion des versions et désinstallation pour Claude Code.
- [Authentification](https://code.claude.com/docs/fr/authentication.md): Connectez-vous à Claude Code et configurez l'authentification pour les particuliers, les équipes et les organisations.
- [Déployer les paramètres gérés](https://code.claude.com/docs/fr/managed-settings.md): Déployez les paramètres gérés sur la machine de chaque développeur : mécanismes de livraison par système d'exploitation, comment Claude Code combine les sources gérées, et comment vérifier l'application.
- [Configurer les paramètres gérés par le serveur](https://code.claude.com/docs/fr/server-managed-settings.md): Configurez centralement Claude Code pour votre organisation via des paramètres livrés par le serveur, sans nécessiter d'infrastructure de gestion des appareils.
- [Contrôlez l'accès aux serveurs MCP pour votre organisation](https://code.claude.com/docs/fr/managed-mcp.md): Limitez les serveurs MCP que les utilisateurs peuvent ajouter ou connecter, ou fournissez des serveurs à tous les utilisateurs, avec des fichiers de configuration gérés, des paramètres gérés, des listes blanches et des listes noires.
- [Configurer le mode auto](https://code.claude.com/docs/fr/auto-mode-config.md): Indiquez au classificateur du mode auto quels dépôts, buckets et domaines votre organisation approuve. Définissez le contexte d'environnement, remplacez les règles de blocage et d'autorisation par défaut, et inspectez votre configuration effective avec les sous-commandes CLI du mode auto.

#### Déploiement

- [Aperçu du déploiement en entreprise](https://code.claude.com/docs/fr/third-party-integrations.md): Découvrez comment Claude Code peut s'intégrer à divers services tiers et infrastructures pour répondre aux exigences de déploiement en entreprise.
- [Disponibilité des fonctionnalités](https://code.claude.com/docs/fr/feature-availability.md): Comparez les fonctionnalités de Claude Code disponibles sur les plans d'abonnement Anthropic, la Console Anthropic, Amazon Bedrock, Claude Platform sur AWS, Google Cloud's Agent Platform et Microsoft Foundry.
- [Claude Code sur Amazon Bedrock](https://code.claude.com/docs/fr/amazon-bedrock.md): Découvrez comment configurer Claude Code via Amazon Bedrock, y compris la configuration, la configuration IAM et le dépannage.
- [Claude Code sur Claude Platform on AWS](https://code.claude.com/docs/fr/claude-platform-on-aws.md): Configurez Claude Code pour utiliser l'API Claude exploitée par Anthropic avec l'authentification AWS, le contrôle d'accès IAM et la facturation AWS Marketplace.
- [Claude Code sur la Plateforme Agent de Google Cloud](https://code.claude.com/docs/fr/google-vertex-ai.md): Découvrez comment configurer Claude Code via la Plateforme Agent de Google Cloud, anciennement Vertex AI, y compris la configuration, la configuration IAM et la résolution des problèmes.
- [Claude Code sur Microsoft Foundry](https://code.claude.com/docs/fr/microsoft-foundry.md): Découvrez comment configurer Claude Code via Microsoft Foundry, y compris la configuration, les paramètres et la résolution des problèmes.
- [Configuration réseau d'entreprise](https://code.claude.com/docs/fr/network-config.md): Configurez Claude Code pour les environnements d'entreprise avec des serveurs proxy, des autorités de certification (CA) personnalisées et l'authentification mutuelle Transport Layer Security (mTLS).
- [Exécuter Claude Code via un lanceur d'entreprise](https://code.claude.com/docs/fr/corporate-launcher.md): Acheminez les processus que Claude Code démarre à partir de son propre binaire, y compris le service d'arrière-plan et chaque session de vue agent, via un lanceur obligatoire avec CLAUDE_CODE_PROCESS_WRAPPER ou le paramètre processWrapper.
- [Conteneurs de développement](https://code.claude.com/docs/fr/devcontainer.md): Exécutez Claude Code dans un conteneur de développement pour des environnements cohérents et isolés dans toute votre équipe.

#### Passerelles

- [Exécuter Claude Code via une passerelle](https://code.claude.com/docs/fr/gateways.md): Acheminez Claude Code via une passerelle auto-hébergée pour les identifiants centralisés, le suivi de l'utilisation et les contrôles de coûts. Couvre l'architecture, la passerelle d'applications Claude d'Anthropic et l'utilisation d'autres produits de passerelle.

##### Passerelle d'applications Claude

- [Passerelle Claude apps pour Amazon Bedrock, Claude Platform sur AWS, Google Cloud et Microsoft Foundry](https://code.claude.com/docs/fr/claude-apps-gateway.md): Exécutez Claude Code via Amazon Bedrock, Claude Platform sur AWS, Google Cloud ou Microsoft Foundry derrière une passerelle auto-hébergée avec authentification SSO, accès aux modèles par groupe et télémétrie OTLP.
- [Configuration de la passerelle Claude apps](https://code.claude.com/docs/fr/claude-apps-gateway-config.md): Référence pour chaque option gateway.yaml : écouteur et TLS, OIDC, session, magasin Postgres, amonts Amazon Bedrock, Claude Platform sur AWS, Agent Platform de Google Cloud et Microsoft Foundry, routage des modèles, politiques gérées et télémétrie.
- [Limites de dépenses de la passerelle Claude apps](https://code.claude.com/docs/fr/claude-apps-gateway-spend-limits.md): Limitez les dépenses de chaque développeur via la passerelle Claude apps par jour, semaine ou mois. Définissez les limites avec une API Admin et la passerelle les applique en direct à chaque requête.
- [Déploiement et exploitation de la passerelle Claude apps](https://code.claude.com/docs/fr/claude-apps-gateway-deploy.md): Enregistrez la passerelle auprès de votre fournisseur d'identité, créez le conteneur, déployez sur Kubernetes ou Cloud Run, et exploitez-la : vérifications de santé, rotation des secrets, mises à jour et sécurité.
- [Déployer la passerelle Claude apps sur AWS](https://code.claude.com/docs/fr/claude-apps-gateway-on-aws.md): Un exemple concret d'exécution de la passerelle Claude apps sur AWS : ECS Fargate ou EKS, Amazon RDS pour PostgreSQL, AWS Secrets Manager et authentification par rôle IAM vers Amazon Bedrock.
- [Déployer la passerelle Claude apps sur Google Cloud](https://code.claude.com/docs/fr/claude-apps-gateway-on-gcp.md): Un exemple concret d'exécution de la passerelle Claude apps sur Google Cloud : Cloud Run ou GKE, Cloud SQL pour PostgreSQL, Secret Manager et authentification par compte de service vers Agent Platform.

##### Autres passerelles

- [Autres passerelles LLM](https://code.claude.com/docs/fr/llm-gateway.md): Acheminez Claude Code via une passerelle LLM que votre organisation exécute déjà. Couvre la connexion de Claude Code à une passerelle, le déploiement d'une passerelle pour votre organisation et ce que Claude Code envoie à une passerelle.
- [Connecter Claude Code à une passerelle LLM](https://code.claude.com/docs/fr/llm-gateway-connect.md): Pointez Claude Code vers la passerelle LLM de votre organisation. Vérifiez si votre administrateur l'a déjà configurée, ou définissez vous-même l'URL de base et les identifiants, puis vérifiez la connexion et corrigez les erreurs de passerelle.
- [Déployer une passerelle LLM pour votre organisation](https://code.claude.com/docs/fr/llm-gateway-rollout.md): Déployez un produit de passerelle pour Claude Code : configurez-le pour transférer ce que Claude Code envoie, émettez des identifiants de développeur, distribuez la configuration via les paramètres gérés, et vérifiez le déploiement.
- [Guide de compatibilité de la passerelle Claude Code](https://code.claude.com/docs/fr/llm-gateway-protocol.md): Maintenez une passerelle LLM compatible avec Claude Code : les points de terminaison qu'elle appelle, les en-têtes et champs de corps à transmettre, et ce qui se casse quand ils sont supprimés.

#### Utilisation et coûts

- [Surveillance](https://code.claude.com/docs/fr/monitoring-usage.md): Découvrez comment activer et configurer OpenTelemetry pour Claude Code.
- [Gérer les coûts efficacement](https://code.claude.com/docs/fr/costs.md): Suivez l'utilisation des tokens, définissez des limites de dépenses pour l'équipe, et réduisez les coûts de Claude Code grâce à la gestion du contexte, la sélection du modèle, les paramètres de réflexion étendue et les hooks de prétraitement.
- [Suivre l'utilisation de l'équipe avec l'analytique](https://code.claude.com/docs/fr/analytics.md): Consultez les métriques d'utilisation de Claude Code, suivez l'adoption et mesurez la vélocité d'ingénierie dans le tableau de bord analytique.

#### Distribution de plugins

- [Créer et distribuer une place de marché de plugins](https://code.claude.com/docs/fr/plugin-marketplaces.md): Créez et hébergez des places de marché de plugins pour distribuer les extensions Claude Code dans vos équipes et communautés.
- [Contraindre les versions des dépendances de plugin](https://code.claude.com/docs/fr/plugin-dependencies.md): Déclarez des contraintes de version sur les dépendances de plugin, et regroupez un ensemble de plugins organisé derrière une seule installation.
- [Recommander votre plugin depuis votre CLI](https://code.claude.com/docs/fr/plugin-hints.md): Émettez un marqueur d'une ligne depuis votre CLI pour que Claude Code invite les utilisateurs à installer votre plugin officiel.
- [Recommander des plugins pour votre organisation](https://code.claude.com/docs/fr/plugin-relevance.md): Ajoutez un bloc de pertinence aux entrées de plugins de la marketplace afin que Claude Code les suggère lorsque le travail d'un utilisateur correspond.

#### Sécurité et données

- [Sécurité](https://code.claude.com/docs/fr/security.md): Découvrez les protections de sécurité de Claude Code et les meilleures pratiques pour une utilisation sûre.
- [Utilisation des données](https://code.claude.com/docs/fr/data-usage.md): Découvrez les politiques d'utilisation des données d'Anthropic pour Claude
- [Zéro conservation des données](https://code.claude.com/docs/fr/zero-data-retention.md): Découvrez la conservation zéro des données (ZDR) pour Claude Code, disponible pour les comptes qualifiés sur Claude for Enterprise, y compris la portée, les fonctionnalités désactivées et comment demander l'activation.

#### Adoption

- [Kit de communication](https://code.claude.com/docs/fr/communications-kit.md): Annonces de lancement, messages de campagne progressive et réponses FAQ pour déployer Claude Code dans votre organisation d'ingénierie.
- [Kit du champion](https://code.claude.com/docs/fr/champion-kit.md): Un guide pratique pour les ingénieurs qui défendent Claude Code en interne : quoi partager, comment répondre aux questions et comment augmenter l'adoption dans votre équipe.

### Configuration

#### Paramètres

- [Fichiers de paramètres et précédence](https://code.claude.com/docs/fr/settings.md): Modifiez les paramètres Claude Code, choisissez la portée à laquelle appartient une clé, vérifiez la modification, et apprenez quelle valeur Claude Code utilise quand une clé est définie à plusieurs endroits.
- [Tous les paramètres](https://code.claude.com/docs/fr/settings-reference.md): Référence complète pour chaque clé settings.json de Claude Code : où chacune se trouve, son type et sa valeur par défaut, et un exemple prêt à coller, avec un index de chaque clé.
- [Fichiers de paramètres d'exemple](https://code.claude.com/docs/fr/settings-example.md): Fichiers settings.json réalistes pour un développeur, une équipe et une organisation : copiez-en un, conservez les clés que vous voulez et modifiez les valeurs.

#### Autorisations et sandboxing

- [Configurer les autorisations](https://code.claude.com/docs/fr/permissions.md): Contrôlez ce que Claude Code peut accéder et faire avec des règles d'autorisation granulaires, des modes et des politiques gérées.
- [Choisir un mode de permission](https://code.claude.com/docs/fr/permission-modes.md): Contrôlez si Claude demande une approbation avant d'agir. Basculez entre les modes avec Maj+Tab dans la CLI, l'indicateur de mode dans VS Code, ou le sélecteur de mode dans Desktop.
- [Configurer l'outil Bash en sandbox](https://code.claude.com/docs/fr/sandboxing.md): Découvrez comment l'outil Bash en sandbox de Claude Code fournit une isolation du système de fichiers et du réseau pour une exécution d'agent plus sûre et plus autonome.
- [Choisir un environnement sandbox](https://code.claude.com/docs/fr/sandbox-environments.md): Comparez les options de sandbox Claude Code : l'outil Bash sandboxé intégré, le runtime sandbox, les dev containers, Docker et les machines virtuelles. Choisissez l'isolation appropriée pour votre modèle de menace.

#### Environnements

- [Configurer les environnements cloud](https://code.claude.com/docs/fr/cloud-environments.md): Configurez les environnements cloud pour les sessions Claude Code cloud : niveaux d'accès réseau, variables d'environnement, scripts de configuration et mise en cache d'environnement.

##### Environnements auto-hébergés

- [Environnements auto-hébergés](https://code.claude.com/docs/fr/self-hosted-environments.md): Exécutez les sessions cloud Claude Code sur l'infrastructure que vous contrôlez : configurez un environnement auto-hébergé, déployez des runners, et routez les sessions vers votre propre calcul.
- [Démarrage rapide des environnements auto-hébergés](https://code.claude.com/docs/fr/self-hosted-environments-quickstart.md): Configurez votre premier environnement auto-hébergé : installez Claude Code, créez l'environnement, démarrez un runner et routez une session vers celui-ci.
- [Déployer des environnements auto-hébergés en production](https://code.claude.com/docs/fr/self-hosted-environments-deploy.md): Exécuter des runners auto-hébergés en production : durcissement de la sécurité, contrôle de la sortie réseau, identifiants git, recettes Kubernetes et Compose, et dépannage.
- [Personnaliser les sessions dans les environnements auto-hébergés](https://code.claude.com/docs/fr/self-hosted-environments-configuration.md): Personnalisez les sessions d'environnement auto-hébergé avec des scripts wrapper pour les identifiants par session, les hooks de cycle de vie et le spawning de runners à la demande.
- [Tester les environnements auto-hébergés de bout en bout](https://code.claude.com/docs/fr/self-hosted-environments-testing.md): Vérifiez une image de runner auto-hébergée à partir de CI : envoyez une session avec la CLI, lisez les réponses de Claude via un hook Stop, et scriptez la boucle complète.
- [Référence des environnements auto-hébergés](https://code.claude.com/docs/fr/self-hosted-environments-reference.md): Référence complète pour le runner et l'orchestrateur auto-hébergés : drapeaux CLI, variables d'environnement et métriques Prometheus.
- [Vérifier l'identité de session dans les environnements auto-hébergés](https://code.claude.com/docs/fr/self-hosted-environments-identity.md): Vérifiez le JWT CLAUDE_CODE_SESSION_ACCESS_TOKEN afin que les services de votre réseau puissent faire confiance aux demandes provenant de sessions dans votre environnement auto-hébergé.

#### Modèle et réponses

- [Configuration du modèle](https://code.claude.com/docs/fr/model-config.md): Configurez le modèle utilisé par Claude Code, les niveaux d'effort, le contexte étendu et la fenêtre d'auto-compaction
- [Accélérez les réponses avec le mode rapide](https://code.claude.com/docs/fr/fast-mode.md): Obtenez des réponses Opus plus rapides dans Claude Code en activant le mode rapide.
- [Escalader les décisions difficiles avec l'outil advisor](https://code.claude.com/docs/fr/advisor.md): Associez votre modèle principal à un modèle advisor plus puissant que Claude consulte aux moments clés pendant une tâche.
- [Styles de sortie](https://code.claude.com/docs/fr/output-styles.md): Adaptez Claude Code pour des usages au-delà de l'ingénierie logicielle

#### Interface

- [Configurez votre terminal pour Claude Code](https://code.claude.com/docs/fr/terminal-config.md): Corrigez Maj+Entrée pour les sauts de ligne, recevez une alerte sonore du terminal quand Claude a terminé, configurez tmux, adaptez le thème de couleur et activez le mode Vim dans l'interface de ligne de commande Claude Code.
- [Rendu en plein écran](https://code.claude.com/docs/fr/fullscreen.md): Activez un mode de rendu plus fluide et sans scintillement avec support de la souris et une utilisation mémoire stable dans les longues conversations.
- [Utiliser Claude Code avec un lecteur d'écran](https://code.claude.com/docs/fr/accessibility.md): Configurez Claude Code pour les lecteurs d'écran tels que VoiceOver et NVDA, ainsi que les paramètres pour les loupes d'écran, le mouvement réduit et les thèmes adaptés aux daltoniens.
- [Dictée vocale](https://code.claude.com/docs/fr/voice-dictation.md): Parlez vos invites dans l'interface de ligne de commande Claude Code avec la dictée vocale en maintenant ou en appuyant.
- [Personnalisez votre barre de statut](https://code.claude.com/docs/fr/statusline.md): Configurez une barre de statut personnalisée pour surveiller l'utilisation de la fenêtre de contexte, les coûts et l'état git dans Claude Code
- [Personnaliser les raccourcis clavier](https://code.claude.com/docs/fr/keybindings.md): Personnalisez les raccourcis clavier dans Claude Code avec un fichier de configuration des liaisons de touches.

### Référence

#### Référence

- [Référence CLI](https://code.claude.com/docs/fr/cli-reference.md): Référence complète pour l'interface de ligne de commande Claude Code, incluant les commandes et les drapeaux.
- [Commandes](https://code.claude.com/docs/fr/commands.md): Référence complète des commandes disponibles dans Claude Code, y compris les commandes intégrées et les compétences groupées.
- [Variables d'environnement](https://code.claude.com/docs/fr/env-vars.md): Référence pour les variables d'environnement qui contrôlent le comportement de Claude Code.
- [Référence des outils](https://code.claude.com/docs/fr/tools-reference.md): Référence complète des outils que Claude Code peut utiliser, y compris les exigences de permission et le comportement par outil.
- [Mode interactif](https://code.claude.com/docs/fr/interactive-mode.md): Référence complète des raccourcis clavier, modes d'entrée et fonctionnalités interactives dans les sessions Claude Code.
- [Checkpointing](https://code.claude.com/docs/fr/checkpointing.md): Suivez, rembobinez et résumez les modifications et la conversation de Claude pour gérer l'état de la session.
- [Référence des hooks](https://code.claude.com/docs/fr/hooks.md): Référence pour les événements de hook Claude Code, le schéma de configuration, les formats d'entrée/sortie JSON, les codes de sortie, les hooks asynchrones, les hooks HTTP, les hooks de prompt et les hooks d'outils MCP.
- [Référence des plugins](https://code.claude.com/docs/fr/plugins-reference.md): Référence technique complète pour le système de plugins Claude Code, incluant les schémas, les commandes CLI et les spécifications des composants.
- [Référence des canaux](https://code.claude.com/docs/fr/channels-reference.md): Créez un serveur MCP qui envoie des webhooks, des alertes et des messages de chat dans une session Claude Code. Référence du contrat de canal : déclaration de capacité, événements de notification, outils de réponse, contrôle de l'expéditeur et relais de permission.

#### Glossaire

- [Glossaire](https://code.claude.com/docs/fr/glossary.md): Définitions de la terminologie Claude Code. Découvrez ce que signifient agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP et autres concepts fondamentaux.

### Agent SDK

#### Agent SDK

- [Présentation du SDK Agent](https://code.claude.com/docs/fr/agent-sdk/overview.md): Créez des agents IA de production avec Claude Code en tant que bibliothèque
- [Démarrage rapide](https://code.claude.com/docs/fr/agent-sdk/quickstart.md): Commencez avec le SDK Agent Python ou TypeScript pour créer des agents IA qui fonctionnent de manière autonome
- [Migrer vers Claude Agent SDK](https://code.claude.com/docs/fr/agent-sdk/migration-guide.md): Guide pour migrer les SDK TypeScript et Python de Claude Code vers Claude Agent SDK
- [Dépanner le SDK Agent](https://code.claude.com/docs/fr/agent-sdk/troubleshooting.md): Corrigez les erreurs du SDK Agent en fonction du message exact que vous voyez, avec la cause et la correction pour chaque erreur dans les SDK TypeScript et Python.

#### Créer des agents

- [Configurer votre agent](https://code.claude.com/docs/fr/agent-sdk/configuration.md): Configurez les sessions du SDK Agent : composez l'objet options, définissez le modèle, l'environnement et les limites, et trouvez la page de chaque option de fonctionnalité.
- [Exemples](https://code.claude.com/docs/fr/agent-sdk/examples.md): Trouvez un projet Agent SDK complet et exécutable ou une recette guidée du Claude Cookbook qui correspond à ce que vous souhaitez construire.

#### Concepts fondamentaux

- [Fonctionnement de la boucle d'agent](https://code.claude.com/docs/fr/agent-sdk/agent-loop.md): Comprenez le cycle de vie des messages, l'exécution des outils, la fenêtre de contexte et l'architecture qui alimentent vos agents SDK.
- [Utiliser les fonctionnalités de Claude Code dans le SDK](https://code.claude.com/docs/fr/agent-sdk/claude-code-features.md): Chargez les instructions de projet, les compétences, les hooks et autres fonctionnalités de Claude Code dans vos agents SDK.
- [Travailler avec les sessions](https://code.claude.com/docs/fr/agent-sdk/sessions.md): Comment les sessions conservent l'historique des conversations de l'agent, et quand utiliser continue, resume et fork pour revenir à une exécution antérieure.
- [Persister les sessions dans un stockage externe](https://code.claude.com/docs/fr/agent-sdk/session-storage.md): Miroir les transcriptions de session Agent SDK vers votre propre magasin d'objets, magasin clé-valeur ou base de données afin que d'autres hôtes puissent reprendre vos sessions.

#### Entrée et sortie

- [Streaming Input](https://code.claude.com/docs/fr/agent-sdk/streaming-vs-single-mode.md): Comprendre les deux modes d'entrée du Claude Agent SDK et quand utiliser chacun
- [Gérer les approbations et les entrées utilisateur](https://code.claude.com/docs/fr/agent-sdk/user-input.md): Présentez les demandes d'approbation et les questions de clarification de Claude aux utilisateurs, puis renvoyez leurs décisions au SDK.
- [Diffuser les réponses en temps réel](https://code.claude.com/docs/fr/agent-sdk/streaming-output.md): Recevez les réponses en temps réel du SDK Agent à mesure que le texte et les appels d'outils sont diffusés
- [Obtenir une sortie structurée des agents](https://code.claude.com/docs/fr/agent-sdk/structured-outputs.md): Retourner du JSON validé à partir de workflows d'agents en utilisant JSON Schema, Zod ou Pydantic. Obtenir des données structurées et type-safe après une utilisation multi-tour d'outils.

#### Étendre avec des outils

- [Donner à Claude des outils personnalisés](https://code.claude.com/docs/fr/agent-sdk/custom-tools.md): Définissez des outils personnalisés avec le serveur MCP en processus du SDK Agent pour que Claude puisse appeler vos fonctions, accéder à vos API et effectuer des opérations spécifiques au domaine.
- [Connecter à des outils externes avec MCP](https://code.claude.com/docs/fr/agent-sdk/mcp.md): Configurez les serveurs MCP pour étendre votre agent avec des outils externes. Couvre les types de transport, la recherche d'outils pour les grands ensembles d'outils, l'authentification et la gestion des erreurs.
- [Adapter à de nombreux outils avec la recherche d'outils](https://code.claude.com/docs/fr/agent-sdk/tool-search.md): Adaptez votre agent à des milliers d'outils en découvrant et chargeant uniquement ce qui est nécessaire, à la demande.
- [Sous-agents dans le SDK](https://code.claude.com/docs/fr/agent-sdk/subagents.md): Définissez et invoquez des sous-agents pour isoler le contexte, exécuter des tâches en parallèle et appliquer des instructions spécialisées dans vos applications Claude Agent SDK.

#### Personnaliser le comportement

- [Modification des invites système](https://code.claude.com/docs/fr/agent-sdk/modifying-system-prompts.md): Choisissez entre le préréglage `claude_code` et une invite système personnalisée, et personnalisez le comportement avec CLAUDE.md, les styles de sortie, append, ou une invite entièrement personnalisée.
- [Étendre les agents avec des skills](https://code.claude.com/docs/fr/agent-sdk/skills.md): Contrôlez les skills que Claude peut invoquer dans les sessions du Claude Agent SDK, distribuez les commandes par nom et créez des skills que vos sessions découvrent
- [Plugins dans le SDK](https://code.claude.com/docs/fr/agent-sdk/plugins.md): Chargez des plugins personnalisés pour étendre Claude Code avec des skills, des agents, des hooks et des serveurs MCP via le SDK Agent

#### Contrôle et observabilité

- [Configurer les permissions](https://code.claude.com/docs/fr/agent-sdk/permissions.md): Contrôlez comment votre agent utilise les outils avec les modes de permission, les hooks et les règles déclaratives d'autorisation/refus.
- [Intercepter et contrôler le comportement des agents avec des hooks](https://code.claude.com/docs/fr/agent-sdk/hooks.md): Interceptez et personnalisez le comportement des agents aux points d'exécution clés avec des hooks
- [Rembobiner les modifications de fichiers avec les points de contrôle](https://code.claude.com/docs/fr/agent-sdk/file-checkpointing.md): Suivre les modifications de fichiers pendant les sessions d'agent et restaurer les fichiers à n'importe quel état antérieur
- [Suivre les coûts et l'utilisation](https://code.claude.com/docs/fr/agent-sdk/cost-tracking.md): Découvrez comment suivre l'utilisation des tokens, estimer les coûts et configurer la mise en cache des invites avec le Claude Agent SDK.
- [Observabilité avec OpenTelemetry](https://code.claude.com/docs/fr/agent-sdk/observability.md): Exportez les traces, les métriques et les événements du SDK Agent vers votre backend d'observabilité en utilisant OpenTelemetry.
- [Suivre les tâches](https://code.claude.com/docs/fr/agent-sdk/todo-tracking.md): Suivre les tâches dans les sessions du SDK Agent et afficher la progression de Claude dans votre application à partir d'appels d'outils structurés

#### Déploiement

- [Héberger l'Agent SDK](https://code.claude.com/docs/fr/agent-sdk/hosting.md): Déployez l'Agent SDK en production : architecture de sous-processus, persistance des sessions, mise à l'échelle, observabilité et isolation multi-locataire pour Docker, Kubernetes et fournisseurs de sandbox.
- [Déployer des agents IA de manière sécurisée](https://code.claude.com/docs/fr/agent-sdk/secure-deployment.md): Un guide pour sécuriser les déploiements de Claude Code et du SDK Agent avec l'isolation, la gestion des identifiants et les contrôles réseau

#### Références SDK

- [Référence du SDK Agent - TypeScript](https://code.claude.com/docs/fr/agent-sdk/typescript.md): Référence API complète du SDK Agent TypeScript, incluant toutes les fonctions, types et interfaces.
- [API de session TypeScript SDK V2 (supprimée)](https://code.claude.com/docs/fr/agent-sdk/typescript-v2-preview.md): Référence pour l'API de session supprimée V2 du SDK Agent TypeScript, avec des modèles send/stream basés sur les sessions pour les conversations multi-tours.
- [Référence du SDK Agent - Python](https://code.claude.com/docs/fr/agent-sdk/python.md): Référence API complète du SDK Agent Python, incluant toutes les fonctions, types et classes.

### Nouveautés

#### Nouveautés

- [Quoi de neuf](https://code.claude.com/docs/fr/whats-new/index.md): Un digest hebdomadaire des fonctionnalités notables de Claude Code, avec des extraits de code, des démos et du contexte sur leur importance.
- [Semaine 37 · 7–11 septembre 2026](https://code.claude.com/docs/fr/whats-new/2026-w37.md): Testez vos plugins avec claude plugin eval et détachez les volets de Claude Code Desktop dans leurs propres fenêtres.
- [Semaine 36 · 31 août – 4 septembre 2026](https://code.claude.com/docs/fr/whats-new/2026-w36.md): Basculez vers Claude Fable 5.1, laissez l'utilisation de l'ordinateur s'exécuter en arrière-plan sur Desktop, et regardez les modifications de Claude dans un panneau /diff en direct.
- [Semaine 35 · 24-28 août 2026](https://code.claude.com/docs/fr/whats-new/2026-w35.md): Reprenez les sessions de terminal dans l'application Claude Code Desktop, examinez les rapports de commentaires que Claude rédige pour vous, et démarrez une session en mode restreint.
- [Semaine 34 · 17–21 août 2026](https://code.claude.com/docs/fr/whats-new/2026-w34.md): Créez des tableaux de bord d'interface utilisateur modifiables avec la compétence /design, définissez le style de sortie Concis, et démarrez une session Claude Code sur votre machine depuis votre téléphone.
- [Semaine 33 · 10–14 août 2026](https://code.claude.com/docs/fr/whats-new/2026-w33.md): Claude Code Desktop continue automatiquement après une réinitialisation de limite d'utilisation, le mode fork s'active par défaut, et les demandes de fusion GitLab et les marketplaces rejoignent GitHub.
- [Semaine 32 · 3–7 août 2026](https://code.claude.com/docs/fr/whats-new/2026-w32.md): Les sessions Claude Code s'envoient des messages entre elles, les environnements auto-hébergés exécutent les sessions cloud sur votre infrastructure, et le mode auto devient le mode de permission par défaut.
- [Semaine 30 · 20–24 juillet 2026](https://code.claude.com/docs/fr/whats-new/2026-w30.md): Opus 5 devient le modèle Opus par défaut, Claude Code Desktop ajoute un volet iOS Simulator, et le plugin Claude Security analyse votre code pour détecter les vulnérabilités.
- [Semaine 29 · 13–17 juillet 2026](https://code.claude.com/docs/fr/whats-new/2026-w29.md): Tirez les données en direct dans les artifacts publiés via les connecteurs MCP, et utilisez Claude Code avec un lecteur d'écran dans le nouveau mode lecteur d'écran.
- [Semaine 28 · 6–10 juillet 2026](https://code.claude.com/docs/fr/whats-new/2026-w28.md): Parcourez des sites externes depuis le navigateur intégré de l'application de bureau, exécutez une vérification complète de la configuration avec /doctor, et découvrez les protections de transcription en mode automatique et les améliorations de la vue agent.
- [Semaine 27 · 29 juin – 3 juillet 2026](https://code.claude.com/docs/fr/whats-new/2026-w27.md): Claude Sonnet 5 devient le modèle par défaut, Claude dans Chrome atteint la disponibilité générale, les sous-agents s'exécutent en arrière-plan par défaut, Claude Desktop arrive sur Linux en bêta, et /radio se connecte à Claude FM.
- [Semaine 26 · 22–26 juin 2026](https://code.claude.com/docs/fr/whats-new/2026-w26.md): Authentifiez les serveurs MCP depuis votre shell avec claude mcp login, obtenez une réponse à la sortie des commandes du mode shell avec le préfixe !, et reprenez une conversation antérieure à /clear avec /rewind.
- [Semaine 25 · 15–19 juin 2026](https://code.claude.com/docs/fr/whats-new/2026-w25.md): Publiez une page en direct et partageable à partir de votre session avec Artifacts, faites correspondre les paramètres d'outils dans les règles de refus et de demande, et définissez n'importe quel paramètre à partir de l'invite avec /config.
- [Semaine 24 · 8–12 juin 2026](https://code.claude.com/docs/fr/whats-new/2026-w24.md): Déplacez une session vers un nouveau répertoire avec /cd, laissez les sous-agents créer leurs propres sous-agents, et dépannez une configuration cassée avec le mode sécurisé.
- [Semaine 23 · 1er–5 juin 2026](https://code.claude.com/docs/fr/whats-new/2026-w23.md): Exécutez le mode auto sur Amazon Bedrock, Google Cloud's Agent Platform et Microsoft Foundry, demandez une confirmation avant d'écrire des fichiers pouvant exécuter du code en mode acceptEdits, listez les plugins installés avec /plugin list, et exigez une plage de version approuvée pour les déploiem…
- [Semaine 22 · 25–29 mai 2026](https://code.claude.com/docs/fr/whats-new/2026-w22.md): Exécutez Claude Code sur Claude Opus 4.8, orchestrez des tâches volumineuses avec des workflows dynamiques, détectez les problèmes de sécurité avec le plugin security-guidance, et utilisez le mode rapide sur Opus 4.8 à un prix inférieur.
- [Semaine 21 · 18–22 mai 2026](https://code.claude.com/docs/fr/whats-new/2026-w21.md): Utilisez le mode auto sur le plan Pro et avec Sonnet 4.6, consultez les compétences, sous-agents et serveurs MCP qui limitent votre plan dans /usage, et examinez les différences avec la nouvelle commande /code-review.
- [Semaine 20 · 11–15 mai 2026](https://code.claude.com/docs/fr/whats-new/2026-w20.md): Gérez chaque session Claude Code depuis un seul écran avec la vue agent, maintenez Claude en travail vers un objectif jusqu'à ce qu'une condition soit remplie, et exécutez le mode rapide sur Opus 4.7 par défaut.
- [Semaine 19 · 4–8 mai 2026](https://code.claude.com/docs/fr/whats-new/2026-w19.md): Chargez les plugins à partir d'archives .zip et d'URL, recherchez l'historique des commandes dans tous les projets avec Ctrl+R, créez de nouvelles worktrees à partir de HEAD local ou de la branche par défaut distante, et bloquez les actions sans condition avec les règles de refus inconditionnels en…
- [Semaine 18 · 27 avril – 1er mai 2026](https://code.claude.com/docs/fr/whats-new/2026-w18.md): Claude Code sur Windows s'exécute sans Git Bash, claude auth login accepte un code OAuth collé lorsque le rappel du navigateur ne peut pas atteindre localhost, claude project purge nettoie l'état local par projet, et coller une URL de PR dans /resume trouve la session qui l'a créée.
- [Semaine 17 · 20–24 avril 2026](https://code.claude.com/docs/fr/whats-new/2026-w17.md): /ultrareview s'ouvre en aperçu de recherche, récapitulatifs de session automatiques lorsque vous revenez à un terminal, thèmes de couleurs personnalisés que vous pouvez créer et déployer dans les plugins, et une Claude Code redessinée sur le web.
- [Semaine 16 · 13–17 avril 2026](https://code.claude.com/docs/fr/whats-new/2026-w16.md): Claude Opus 4.7 avec le nouveau niveau d'effort xhigh, Routines sur Claude Code sur le web, notifications push mobiles qui vous signalent sur votre téléphone quand Claude a besoin de vous, une ventilation /usage qui montre ce qui limite votre utilisation, et les binaires natifs remplaçant le JavaScr…
- [Semaine 15 · 6–10 avril 2026](https://code.claude.com/docs/fr/whats-new/2026-w15.md): Ultraplan pour la planification cloud, l'outil Monitor avec /loop auto-cadencé, /team-onboarding pour packager votre configuration, et /autofix-pr depuis votre terminal.
- [Semaine 14 · 30 mars – 3 avril 2026](https://code.claude.com/docs/fr/whats-new/2026-w14.md): Computer use dans la CLI, leçons interactives intégrées, rendu sans scintillement, remplacements de taille de résultat MCP par outil, et exécutables de plugin sur PATH.
- [Semaine 13 · 23–27 mars 2026](https://code.claude.com/docs/fr/whats-new/2026-w13.md): Mode auto pour les permissions sans intervention, utilisation d'ordinateur intégrée, correction automatique des PR dans le cloud, recherche de transcription et un outil PowerShell pour Windows.

### Ressources

#### Ressources

- [Aspects juridiques et conformité](https://code.claude.com/docs/fr/legal-and-compliance.md): Accords juridiques, certifications de conformité et informations de sécurité pour Claude Code.

---

## Claude Code Docs: Indonesian

- 官方原文：https://code.claude.com/docs/_llms/id.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-id.md`

# Claude Code Docs: Indonesian

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Indonesian

### Memulai

#### Memulai

- [Ikhtisar](https://code.claude.com/docs/id/overview.md): Claude Code adalah alat pengkodean agentic yang membaca basis kode Anda, mengedit file, menjalankan perintah, dan terintegrasi dengan alat pengembangan Anda. Tersedia di terminal, IDE, aplikasi desktop, dan browser.
- [Panduan Cepat](https://code.claude.com/docs/id/quickstart.md): Selamat datang di Claude Code!
- [Changelog](https://code.claude.com/docs/id/changelog.md)

#### Konsep Inti

- [Cara Kerja Claude Code](https://code.claude.com/docs/id/how-claude-code-works.md): Pahami loop agentic, tools bawaan, dan bagaimana Claude Code berinteraksi dengan proyek Anda.
- [Perluas Claude Code](https://code.claude.com/docs/id/features-overview.md): Pahami kapan menggunakan CLAUDE.md, Skills, subagents, hooks, MCP, dan plugins.
- [Jelajahi direktori .claude](https://code.claude.com/docs/id/claude-directory.md): Tempat Claude Code membaca CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules, dan auto memory. Jelajahi direktori .claude di proyek Anda dan ~/.claude di direktori home Anda.
- [Jelajahi jendela konteks](https://code.claude.com/docs/id/context-window.md): Simulasi interaktif tentang bagaimana jendela konteks Claude Code terisi selama sesi. Lihat apa yang dimuat secara otomatis, berapa biaya setiap pembacaan file, dan kapan aturan dan hook dijalankan.
- [Bagaimana Claude Code menggunakan prompt caching](https://code.claude.com/docs/id/prompt-caching.md): Claude Code mengelola prompt caching secara otomatis. Lihat mengapa perubahan model memicu giliran tanpa cache yang lambat, berapa biaya `/compact`, mengapa pengeditan CLAUDE.md tidak berlaku di tengah sesi, dan cara memeriksa tingkat cache hit Anda.

#### Gunakan Claude Code

- [Bagaimana Claude mengingat proyek Anda](https://code.claude.com/docs/id/memory.md): Berikan Claude instruksi persisten dengan file CLAUDE.md atau AGENTS.md, dan biarkan Claude mengumpulkan pembelajaran secara otomatis dengan auto memory.
- [Kelola sesi](https://code.claude.com/docs/id/sessions.md): Beri nama, lanjutkan, cabang, dan beralih antar percakapan Claude Code. Mencakup `--continue`, `--resume`, `--from-pr`, pemilih `/resume`, penamaan sesi, ekspor transkrip, dan tempat penyimpanan transkrip.
- [Alur kerja umum](https://code.claude.com/docs/id/common-workflows.md): Panduan langkah demi langkah untuk menjelajahi basis kode, memperbaiki bug, refactoring, pengujian, dan tugas sehari-hari lainnya dengan Claude Code.
- [Perpustakaan prompt](https://code.claude.com/docs/id/prompt-library.md): Salin-tempel prompt untuk Claude Code, diberi tag berdasarkan tugas dan peran.
- [Praktik Terbaik untuk Claude Code](https://code.claude.com/docs/id/best-practices.md): Tips dan pola untuk memaksimalkan Claude Code, dari mengonfigurasi lingkungan Anda hingga menskalakan di seluruh sesi paralel.

#### Platform dan integrasi

- [Platform dan integrasi](https://code.claude.com/docs/id/platforms.md): Pilih di mana menjalankan Claude Code dan apa yang akan dihubungkan. Bandingkan CLI, Desktop, VS Code, JetBrains, web, mobile, dan integrasi seperti Chrome, Slack, dan CI/CD.
- [Lanjutkan sesi lokal dari perangkat apa pun dengan Remote Control](https://code.claude.com/docs/id/remote-control.md): Lanjutkan sesi Claude Code lokal dari ponsel, tablet, atau browser apa pun menggunakan Remote Control. Bekerja dengan claude.ai/code dan aplikasi Claude mobile.
- [Biarkan Claude mengoordinasikan pekerjaan berkelanjutan dengan Projects](https://code.claude.com/docs/id/claude-projects.md): Berikan Claude sekumpulan pekerjaan terkait dalam satu percakapan dan biarkan ia mengoordinasikan sesi cloud paralel yang berbagi repositori, instruksi, dan memori.
- [Claude Code di mobile](https://code.claude.com/docs/id/mobile.md): Mulai, pantau, dan arahkan tugas Claude Code dari ponsel Anda dengan aplikasi Claude untuk iOS dan Android.
- [Gunakan Claude Code dengan Chrome](https://code.claude.com/docs/id/chrome.md): Hubungkan Claude Code ke browser Chrome Anda untuk menguji aplikasi web, debug dengan console logs, otomatisasi pengisian formulir, dan ekstrak data dari halaman web.
- [Biarkan Claude menggunakan komputer Anda dari CLI](https://code.claude.com/docs/id/computer-use.md): Aktifkan computer use di Claude Code CLI sehingga Claude dapat membuka aplikasi, mengklik, mengetik, dan melihat layar Anda di macOS. Uji aplikasi native, debug masalah visual, dan otomatisasi alat GUI-only tanpa meninggalkan terminal Anda.
- [Gunakan Claude Code di VS Code](https://code.claude.com/docs/id/vs-code.md): Instal dan konfigurasi ekstensi Claude Code untuk VS Code. Dapatkan bantuan pengkodean AI dengan diff inline, @-mentions, review rencana, dan pintasan keyboard.
- [JetBrains IDEs](https://code.claude.com/docs/id/jetbrains.md): Gunakan Claude Code dengan JetBrains IDEs termasuk IntelliJ, PyCharm, WebStorm, dan lainnya
- [Claude Code di Slack](https://code.claude.com/docs/id/slack.md): Delegasikan tugas coding langsung dari workspace Slack Anda. Anthropic sedang menghentikan versi awal ini untuk workspace Team dan Enterprise demi Claude Tag; versi ini tetap menjadi jalur setup pada paket Pro dan Max.
- [Claude Tag](https://code.claude.com/docs/id/claude-tag.md): Bawa Claude ke saluran Slack tim Anda dengan Claude Tag dan temukan dokumentasi setup dan penggunaan di claude.com.

##### Claude Code di cloud

- [Mulai dengan Claude Code di cloud](https://code.claude.com/docs/id/web-quickstart.md): Jalankan Claude Code di cloud dari browser atau ponsel Anda. Hubungkan repositori GitHub, kirimkan tugas, dan tinjau PR tanpa setup lokal.
- [Gunakan Claude Code di cloud](https://code.claude.com/docs/id/claude-code-on-the-web.md): Jalankan sesi Claude Code di cloud dari browser, ponsel, aplikasi desktop, atau terminal Anda, pindahkan dengan --cloud dan --teleport, dan auto-fix pull request.
- [Otomatisasi pekerjaan dengan rutinitas](https://code.claude.com/docs/id/routines.md): Letakkan Claude Code pada autopilot. Tentukan rutinitas yang berjalan sesuai jadwal, dipicu oleh panggilan API, atau bereaksi terhadap peristiwa GitHub dari infrastruktur cloud.
- [Temukan bug dengan ultrareview](https://code.claude.com/docs/id/ultrareview.md): Jalankan tinjauan kode multi-agen yang mendalam di cloud dengan /code-review ultra untuk menemukan dan memverifikasi bug sebelum Anda merge.

##### Claude Code di desktop

- [Memulai dengan aplikasi desktop](https://code.claude.com/docs/id/desktop-quickstart.md): Instal Claude Code di desktop dan mulai sesi coding pertama Anda
- [Aplikasi desktop](https://code.claude.com/docs/id/desktop.md): Dapatkan lebih banyak dari Claude Code Desktop: sesi paralel dengan isolasi Git, tata letak pane drag-and-drop, terminal terintegrasi dan editor file, side chats, computer use, Dispatch sessions dari ponsel Anda, tinjauan diff visual, pratinjau aplikasi, pemantauan PR, konektor, dan konfigurasi ente…
- [Claude Desktop di Linux (beta)](https://code.claude.com/docs/id/desktop-linux.md): Instal dan perbarui aplikasi desktop Claude di Ubuntu dan Debian
- [Claude Code Desktop di WSL](https://code.claude.com/docs/id/desktop-wsl.md): Jalankan sesi Code di dalam distribusi WSL 2 di Windows
- [Jadwalkan tugas berulang di Claude Code Desktop](https://code.claude.com/docs/id/desktop-scheduled-tasks.md): Atur tugas terjadwal di Claude Code Desktop untuk menjalankan Claude secara otomatis pada basis berulang untuk tinjauan kode harian, audit dependensi, atau briefing pagi.
- [Uji aplikasi iOS di simulator](https://code.claude.com/docs/id/desktop-ios-simulator.md): Claude Code Desktop membuka aplikasi Anda di pane iOS Simulator ketika Claude membangun, menjalankan, atau memeriksanya, dengan simulator terpisah untuk setiap sesi.

##### Tinjauan kode & CI/CD

- [Tangkap masalah keamanan saat Claude menulis kode](https://code.claude.com/docs/id/security-guidance.md): Instal plugin security-guidance untuk membuat Claude meninjau perubahan kodenya sendiri untuk kerentanan dan memperbaikinya dalam sesi yang sama.
- [Pindai basis kode Anda untuk menemukan kerentanan](https://code.claude.com/docs/id/claude-security.md): Instal plugin Claude Security untuk memindai basis kode Anda mencari kerentanan dalam sesi Claude Code dan ubah temuan menjadi patch yang Anda tinjau dan terapkan.
- [Code Review](https://code.claude.com/docs/id/code-review.md): Siapkan ulasan PR otomatis yang menangkap kesalahan logika, kerentanan keamanan, dan regresi menggunakan analisis multi-agen dari seluruh basis kode Anda
- [Claude Code GitHub Actions](https://code.claude.com/docs/id/github-actions.md): Jalankan Claude Code dalam alur kerja GitHub Actions untuk merespons penyebutan @claude, mengotomatisasi tugas, dan mengubah issue menjadi pull request
- [Gunakan Claude Code GitHub Actions dengan penyedia cloud](https://code.claude.com/docs/id/github-actions-cloud-providers.md): Jalankan Claude Code GitHub Actions melalui Amazon Bedrock, Google Cloud's Agent Platform, atau Microsoft Foundry alih-alih Claude API
- [Claude Code dengan GitHub Enterprise Server](https://code.claude.com/docs/id/github-enterprise-server.md): Hubungkan Claude Code ke instans GitHub Enterprise Server yang di-host sendiri untuk sesi cloud, tinjauan kode, dan pasar plugin.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/id/gitlab-ci-cd.md): Pelajari tentang mengintegrasikan Claude Code ke dalam alur kerja pengembangan Anda dengan GitLab CI/CD

### Bangun dengan Claude Code

#### Agen dan pekerjaan paralel

- [Jalankan agen secara paralel](https://code.claude.com/docs/id/agents.md): Bandingkan cara Claude Code dapat menangani beberapa tugas sekaligus: subagents, agent view, agent teams, dynamic workflows, dan projects.
- [Buat subagent khusus](https://code.claude.com/docs/id/sub-agents.md): Buat dan gunakan subagent AI khusus di Claude Code untuk alur kerja khusus tugas dan manajemen konteks yang lebih baik.
- [Kelola banyak agen dengan tampilan agen](https://code.claude.com/docs/id/agent-view.md): Kirim dan kelola banyak sesi Claude Code dari satu layar. Tampilan agen menunjukkan apa yang dilakukan setiap sesi dan mana yang membutuhkan masukan Anda.
- [Koordinasikan tim Claude Code sessions](https://code.claude.com/docs/id/agent-teams.md): Koordinasikan beberapa instance Claude Code yang bekerja bersama sebagai tim, dengan tugas bersama, pesan antar-agent, dan manajemen terpusat.
- [Pesan sesi Claude Code Anda yang lain](https://code.claude.com/docs/id/cross-session-messaging.md): Biarkan Claude mencantumkan dan mengirim pesan ke sesi Claude Code Anda yang lain di mesin ini, dan jangkau sesi Anda di mesin lain atau di web.
- [Orkestrasi subagen dalam skala besar dengan alur kerja dinamis](https://code.claude.com/docs/id/workflows.md): Alur kerja dinamis mengorkestrasi banyak subagen dari skrip yang ditulis Claude dan dapat Anda jalankan kembali. Gunakan untuk audit basis kode, migrasi besar, dan penelitian lintas-periksa.
- [Jalankan sesi paralel dengan worktrees](https://code.claude.com/docs/id/worktrees.md): Isolasi sesi Claude Code paralel dalam git worktrees terpisah sehingga perubahan tidak bertabrakan. Mencakup flag `--worktree`, isolasi subagent, `.worktreeinclude`, pembersihan, dan hook VCS non-git.

#### MCP

- [Terhubung ke server MCP](https://code.claude.com/docs/id/mcp-quickstart.md): Tambahkan server MCP ke Claude Code, verifikasi koneksi, dan temukan konfigurasi di disk.
- [Hubungkan Claude Code ke alat melalui MCP](https://code.claude.com/docs/id/mcp.md): Pelajari cara menghubungkan Claude Code ke alat Anda dengan Model Context Protocol.

#### Skills

- [Perluas Claude dengan skills](https://code.claude.com/docs/id/skills.md): Buat, kelola, dan bagikan skills untuk memperluas kemampuan Claude di Claude Code. Mencakup perintah kustom dan skills bundel.

#### Plugin

- [Temukan dan instal plugin yang sudah dibuat melalui marketplace](https://code.claude.com/docs/id/discover-plugins.md): Temukan dan instal plugin dari marketplace untuk memperluas Claude Code dengan skills, agen, dan kemampuan baru.
- [Buat plugins](https://code.claude.com/docs/id/plugins.md): Buat plugins kustom untuk memperluas Claude Code dengan skills, agents, hooks, dan MCP servers.
- [Uji plugin dengan evals](https://code.claude.com/docs/id/plugin-evals.md): Tulis kasus eval untuk plugin Claude Code Anda, jalankan dengan claude plugin eval, nilai hasilnya, bandingkan dengan baseline tanpa plugin, dan gating CI pada skor.

#### Artefak

- [Bagikan output sesi sebagai artifacts](https://code.claude.com/docs/id/artifacts.md): Artifacts mengubah pekerjaan Claude Code menjadi halaman interaktif langsung di claude.ai yang dapat Anda simpan pribadi, bagikan dengan organisasi Anda, atau publikasikan ke tautan publik.

#### Otomasi

- [Otomatisasi tindakan dengan hooks](https://code.claude.com/docs/id/hooks-guide.md): Jalankan perintah shell secara otomatis ketika Claude Code mengedit file, menyelesaikan tugas, atau memerlukan input. Format kode, kirim notifikasi, validasi perintah, dan terapkan aturan proyek.
- [Dorong acara ke dalam sesi yang sedang berjalan dengan channels](https://code.claude.com/docs/id/channels.md): Gunakan channels untuk mendorong pesan, peringatan, dan webhooks ke dalam sesi Claude Code Anda dari server MCP. Teruskan hasil CI, pesan obrolan, dan acara pemantauan sehingga Claude dapat bereaksi saat Anda tidak ada.
- [Jalankan prompt sesuai jadwal](https://code.claude.com/docs/id/scheduled-tasks.md): Gunakan /loop dan alat penjadwalan cron untuk menjalankan prompt berulang kali, polling status, atau mengatur pengingat sekali jalan dalam sesi Claude Code.
- [Jaga Claude tetap bekerja menuju tujuan](https://code.claude.com/docs/id/goal.md): Tetapkan kondisi penyelesaian dengan /goal dan Claude terus bekerja hingga kondisi terpenuhi, model menilai tidak mungkin, atau kesalahan yang harus Anda perbaiki menghapus tujuan.
- [Jalankan Claude Code secara programatis](https://code.claude.com/docs/id/headless.md): Gunakan Agent SDK untuk menjalankan Claude Code secara programatis dari CLI, Python, atau TypeScript.
- [Luncurkan sesi dari tautan](https://code.claude.com/docs/id/deep-links.md): Buka sesi terminal Claude Code dari URL. Sematkan tautan `claude-cli://` dalam runbook, peringatan, dan dasbor sehingga klik membuka Claude Code di repo yang tepat dengan prompt yang tepat.

#### Panduan

- [Siapkan Claude Code di monorepo atau codebase besar](https://code.claude.com/docs/id/large-codebases.md): Konfigurasikan Claude Code untuk monorepos dan codebase pohon tunggal besar dengan file CLAUDE.md bersarang, worktrees sparse, code intelligence, dan skills per-paket sehingga Claude tetap fokus pada kode yang sedang Anda kerjakan.

#### Pemecahan Masalah

- [Troubleshoot installation and login](https://code.claude.com/docs/id/troubleshoot-install.md): Perbaiki command not found, PATH, permission, network, dan authentication errors saat menginstal atau masuk ke Claude Code.
- [Troubleshooting](https://code.claude.com/docs/id/troubleshooting.md): Perbaiki penggunaan CPU atau memori yang tinggi, hang, thrashing auto-compact, dan masalah pencarian di Claude Code, dan temukan halaman yang tepat untuk masalah lainnya.
- [Debug konfigurasi Anda](https://code.claude.com/docs/id/debug-your-config.md): Diagnosis mengapa CLAUDE.md, settings, hooks, server MCP, atau skills tidak berlaku. Gunakan /context, /doctor, /hooks, dan /mcp untuk melihat apa yang benar-benar dimuat.
- [Referensi kesalahan](https://code.claude.com/docs/id/errors.md): Cari pesan kesalahan runtime Claude Code dengan arti masing-masing dan cara memperbaikinya.

### Administrasi

#### Pengaturan dan akses

- [Siapkan Claude Code untuk organisasi Anda](https://code.claude.com/docs/id/admin-setup.md): Peta keputusan untuk administrator yang menerapkan Claude Code, mencakup penyedia API, pengaturan terkelola, penegakan kebijakan, pemantauan penggunaan, dan penanganan data.
- [Pengaturan lanjutan](https://code.claude.com/docs/id/setup.md): Persyaratan sistem, instalasi khusus platform, manajemen versi, dan penghapusan instalasi untuk Claude Code.
- [Autentikasi](https://code.claude.com/docs/id/authentication.md): Masuk ke Claude Code dan konfigurasikan autentikasi untuk individu, tim, dan organisasi.
- [Terapkan pengaturan terkelola](https://code.claude.com/docs/id/managed-settings.md): Terapkan pengaturan terkelola ke mesin setiap pengembang: mekanisme pengiriman per OS, bagaimana Claude Code menggabungkan sumber terkelola, dan cara memverifikasi penegakan.
- [Konfigurasi pengaturan yang dikelola server](https://code.claude.com/docs/id/server-managed-settings.md): Konfigurasi Claude Code secara terpusat untuk organisasi Anda melalui pengaturan yang dikirimkan server, tanpa memerlukan infrastruktur manajemen perangkat.
- [Kontrol akses server MCP untuk organisasi Anda](https://code.claude.com/docs/id/managed-mcp.md): Batasi server MCP mana yang dapat ditambahkan atau dihubungkan pengguna, atau sediakan server untuk setiap pengguna, dengan file konfigurasi yang dikelola, pengaturan yang dikelola, daftar izin, dan daftar penolakan.
- [Konfigurasi mode otomatis](https://code.claude.com/docs/id/auto-mode-config.md): Beri tahu pengklasifikasi mode otomatis repositori, bucket, dan domain mana yang dipercaya organisasi Anda. Atur konteks lingkungan, ganti aturan blokir dan izin default, dan periksa konfigurasi efektif Anda dengan subperintah CLI mode otomatis.

#### Penyebaran

- [Ikhtisar penyebaran enterprise](https://code.claude.com/docs/id/third-party-integrations.md): Pelajari bagaimana Claude Code dapat terintegrasi dengan berbagai layanan pihak ketiga dan infrastruktur untuk memenuhi persyaratan penyebaran enterprise.
- [Ketersediaan fitur](https://code.claude.com/docs/id/feature-availability.md): Bandingkan fitur Claude Code mana yang tersedia di seluruh paket langganan Anthropic, Anthropic Console, Amazon Bedrock, Claude Platform di AWS, Platform Agent Google Cloud, dan Microsoft Foundry.
- [Claude Code di Amazon Bedrock](https://code.claude.com/docs/id/amazon-bedrock.md): Pelajari tentang mengonfigurasi Claude Code melalui Amazon Bedrock, termasuk pengaturan, konfigurasi IAM, dan pemecahan masalah.
- [Claude Code pada Claude Platform on AWS](https://code.claude.com/docs/id/claude-platform-on-aws.md): Konfigurasi Claude Code untuk menggunakan Claude API yang dioperasikan Anthropic dengan autentikasi AWS, kontrol akses IAM, dan penagihan AWS Marketplace.
- [Claude Code di Platform Agen Google Cloud](https://code.claude.com/docs/id/google-vertex-ai.md): Pelajari tentang mengonfigurasi Claude Code melalui Platform Agen Google Cloud, yang sebelumnya bernama Vertex AI, termasuk pengaturan, konfigurasi IAM, dan pemecahan masalah.
- [Claude Code di Microsoft Foundry](https://code.claude.com/docs/id/microsoft-foundry.md): Pelajari tentang mengonfigurasi Claude Code melalui Microsoft Foundry, termasuk setup, konfigurasi, dan pemecahan masalah.
- [Konfigurasi jaringan enterprise](https://code.claude.com/docs/id/network-config.md): Konfigurasikan Claude Code untuk lingkungan enterprise dengan server proxy, Certificate Authorities (CA) kustom, dan autentikasi mutual Transport Layer Security (mTLS).
- [Jalankan Claude Code di balik peluncur korporat](https://code.claude.com/docs/id/corporate-launcher.md): Arahkan proses yang dimulai Claude Code dari binernya sendiri, termasuk layanan latar belakang dan setiap sesi tampilan agen, melalui peluncur yang diperlukan dengan CLAUDE_CODE_PROCESS_WRAPPER atau pengaturan processWrapper.
- [Kontainer pengembangan](https://code.claude.com/docs/id/devcontainer.md): Jalankan Claude Code di dalam kontainer pengembangan untuk lingkungan yang konsisten dan terisolasi di seluruh tim Anda.

#### Gateway

- [Jalankan Claude Code melalui gateway](https://code.claude.com/docs/id/gateways.md): Arahkan Claude Code melalui gateway yang di-host sendiri untuk kredensial terpusat, pelacakan penggunaan, dan kontrol biaya. Mencakup arsitektur, gateway aplikasi Claude Anthropic, dan menggunakan produk gateway lainnya.

##### Claude apps gateway

- [Claude apps gateway untuk Amazon Bedrock, Claude Platform di AWS, Google Cloud, dan Microsoft Foundry](https://code.claude.com/docs/id/claude-apps-gateway.md): Jalankan Claude Code melalui Amazon Bedrock, Claude Platform di AWS, Google Cloud, atau Microsoft Foundry di balik gateway yang di-host sendiri dengan SSO sign-in, akses model per-grup, dan telemetri OTLP.
- [Konfigurasi gateway aplikasi Claude](https://code.claude.com/docs/id/claude-apps-gateway-config.md): Referensi untuk setiap opsi gateway.yaml: listener dan TLS, OIDC, session, Postgres store, Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, dan Microsoft Foundry upstreams, model routing, managed policies, dan telemetry.
- [Batas pengeluaran gateway aplikasi Claude](https://code.claude.com/docs/id/claude-apps-gateway-spend-limits.md): Batasi pengeluaran setiap pengembang melalui gateway aplikasi Claude berdasarkan hari, minggu, atau bulan. Tetapkan batas dengan Admin API dan gateway memberlakukannya secara langsung pada setiap permintaan.
- [Penyebaran dan operasi gateway aplikasi Claude](https://code.claude.com/docs/id/claude-apps-gateway-deploy.md): Daftarkan gateway dengan IdP Anda, bangun kontainer, sebarkan di Kubernetes atau Cloud Run, dan operasikan: pemeriksaan kesehatan, rotasi rahasia, peningkatan, dan keamanan.
- [Terapkan gateway aplikasi Claude di AWS](https://code.claude.com/docs/id/claude-apps-gateway-on-aws.md): Contoh praktis menjalankan gateway aplikasi Claude di AWS: ECS Fargate atau EKS, Amazon RDS untuk PostgreSQL, AWS Secrets Manager, dan autentikasi berbasis peran IAM ke Amazon Bedrock.
- [Terapkan gateway aplikasi Claude di Google Cloud](https://code.claude.com/docs/id/claude-apps-gateway-on-gcp.md): Contoh praktis menjalankan gateway aplikasi Claude di Google Cloud: Cloud Run atau GKE, Cloud SQL untuk PostgreSQL, Secret Manager, dan autentikasi service-account ke Agent Platform Google Cloud.

##### Gateway lainnya

- [Gateway LLM lainnya](https://code.claude.com/docs/id/llm-gateway.md): Arahkan Claude Code melalui gateway LLM yang sudah dijalankan organisasi Anda. Mencakup menghubungkan Claude Code ke gateway, meluncurkannya untuk organisasi Anda, dan apa yang Claude Code kirimkan ke gateway.
- [Hubungkan Claude Code ke gateway LLM](https://code.claude.com/docs/id/llm-gateway-connect.md): Arahkan Claude Code ke gateway LLM organisasi Anda. Periksa apakah admin Anda sudah mengonfigurasinya, atau atur URL dasar dan kredensial sendiri, kemudian verifikasi koneksi dan perbaiki kesalahan gateway.
- [Luncurkan gateway LLM untuk organisasi Anda](https://code.claude.com/docs/id/llm-gateway-rollout.md): Terapkan produk gateway untuk Claude Code: konfigurasikan untuk meneruskan apa yang dikirim Claude Code, keluarkan kredensial pengembang, distribusikan konfigurasi melalui pengaturan terkelola, dan verifikasi peluncuran.
- [Panduan kompatibilitas gateway Claude Code](https://code.claude.com/docs/id/llm-gateway-protocol.md): Jaga gateway LLM tetap kompatibel dengan Claude Code: endpoint yang dipanggilnya, header dan field body yang harus diteruskan, dan apa yang rusak saat dihapus.

#### Penggunaan dan biaya

- [Pemantauan](https://code.claude.com/docs/id/monitoring-usage.md): Pelajari cara mengaktifkan dan mengonfigurasi OpenTelemetry untuk Claude Code.
- [Kelola biaya secara efektif](https://code.claude.com/docs/id/costs.md): Lacak penggunaan token, tetapkan batas pengeluaran tim, dan kurangi biaya Claude Code dengan manajemen konteks, pemilihan model, pengaturan pemikiran yang diperluas, dan hook prapemrosesan.
- [Lacak penggunaan tim dengan analitik](https://code.claude.com/docs/id/analytics.md): Lihat metrik penggunaan Claude Code, lacak adopsi, dan ukur kecepatan teknik dalam dasbor analitik.

#### Distribusi Plugin

- [Buat dan distribusikan marketplace plugin](https://code.claude.com/docs/id/plugin-marketplaces.md): Bangun dan host marketplace plugin untuk mendistribusikan ekstensi Claude Code di seluruh tim dan komunitas.
- [Batasi versi dependensi plugin](https://code.claude.com/docs/id/plugin-dependencies.md): Deklarasikan batasan versi pada dependensi plugin, dan bundel satu set plugin yang dikurasi di balik satu instalasi.
- [Rekomendasikan plugin Anda dari CLI Anda](https://code.claude.com/docs/id/plugin-hints.md): Keluarkan penanda satu baris dari CLI Anda sehingga Claude Code meminta pengguna untuk memasang plugin resmi Anda.
- [Rekomendasikan plugins untuk organisasi Anda](https://code.claude.com/docs/id/plugin-relevance.md): Tambahkan blok relevance ke entri plugin marketplace sehingga Claude Code menyarankannya ketika pekerjaan pengguna cocok.

#### Keamanan dan data

- [Keamanan](https://code.claude.com/docs/id/security.md): Pelajari tentang perlindungan keamanan Claude Code dan praktik terbaik untuk penggunaan yang aman.
- [Penggunaan data](https://code.claude.com/docs/id/data-usage.md): Pelajari kebijakan penggunaan data Anthropic untuk Claude
- [Retensi data nol](https://code.claude.com/docs/id/zero-data-retention.md): Pelajari tentang Zero Data Retention (ZDR) untuk Claude Code, tersedia untuk akun yang memenuhi syarat di Claude for Enterprise, termasuk cakupan, fitur yang dinonaktifkan, dan cara meminta pengaktifan.

#### Adopsi

- [Kit komunikasi](https://code.claude.com/docs/id/communications-kit.md): Luncurkan pengumuman, pesan kampanye bertahap, dan respons FAQ untuk meluncurkan Claude Code ke organisasi teknik Anda.
- [Champion kit](https://code.claude.com/docs/id/champion-kit.md): Panduan untuk insinyur yang mengadvokasi Claude Code secara internal: apa yang harus dibagikan, cara menjawab pertanyaan, dan cara meningkatkan adopsi di tim Anda.

### Konfigurasi

#### Pengaturan

- [File pengaturan dan urutan prioritas](https://code.claude.com/docs/id/settings.md): Ubah pengaturan Claude Code, pilih cakupan kunci, verifikasi perubahan, dan pelajari nilai mana yang digunakan Claude Code saat kunci diatur di beberapa tempat.
- [Semua pengaturan](https://code.claude.com/docs/id/settings-reference.md): Referensi lengkap untuk setiap kunci settings.json Claude Code: di mana masing-masing berada, tipe dan defaultnya, serta contoh siap tempel, dengan indeks setiap kunci.
- [Contoh file pengaturan](https://code.claude.com/docs/id/settings-example.md): File settings.json realistis untuk pengembang, tim, dan organisasi: salin satu, pertahankan kunci yang Anda inginkan, dan ubah nilainya.

#### Izin dan sandboxing

- [Konfigurasi izin](https://code.claude.com/docs/id/permissions.md): Kontrol apa yang dapat diakses Claude Code dan lakukan dengan aturan izin terperinci, mode, dan kebijakan terkelola.
- [Pilih mode izin](https://code.claude.com/docs/id/permission-modes.md): Kontrol apakah Claude meminta izin sebelum bertindak. Alihkan mode izin dengan Shift+Tab di CLI, indikator mode di VS Code, atau pemilih mode di Desktop.
- [Konfigurasi alat Bash sandboxed](https://code.claude.com/docs/id/sandboxing.md): Pelajari bagaimana alat Bash sandboxed Claude Code menyediakan isolasi filesystem dan jaringan untuk eksekusi agen yang lebih aman dan mandiri.
- [Pilih lingkungan sandbox](https://code.claude.com/docs/id/sandbox-environments.md): Bandingkan opsi sandbox Claude Code: alat Bash bersandbox bawaan, runtime sandbox, dev container, Docker, dan VM. Pilih isolasi yang tepat untuk model ancaman Anda.

#### Lingkungan

- [Konfigurasi lingkungan cloud](https://code.claude.com/docs/id/cloud-environments.md): Konfigurasi lingkungan cloud untuk sesi Claude Code cloud: tingkat akses jaringan, variabel lingkungan, skrip setup, dan caching lingkungan.

##### Lingkungan yang di-host sendiri

- [Lingkungan yang di-host sendiri](https://code.claude.com/docs/id/self-hosted-environments.md): Jalankan sesi cloud Claude Code pada infrastruktur yang Anda kontrol: siapkan lingkungan yang di-host sendiri, deploy runner, dan arahkan sesi ke komputasi Anda sendiri.
- [Panduan cepat lingkungan yang di-host sendiri](https://code.claude.com/docs/id/self-hosted-environments-quickstart.md): Siapkan lingkungan yang di-host sendiri pertama Anda: instal Claude Code, buat lingkungan, mulai runner, dan arahkan sesi ke sana.
- [Terapkan lingkungan yang di-host sendiri ke produksi](https://code.claude.com/docs/id/self-hosted-environments-deploy.md): Jalankan runner yang di-host sendiri dalam produksi: pengerasan keamanan, kontrol egress jaringan, kredensial git, resep Kubernetes dan Compose, serta pemecahan masalah.
- [Sesuaikan sesi di lingkungan yang di-host sendiri](https://code.claude.com/docs/id/self-hosted-environments-configuration.md): Sesuaikan sesi lingkungan yang di-host sendiri dengan skrip wrapper untuk kredensial per-sesi, hook siklus hidup, dan pemijahan runner sesuai permintaan.
- [Uji lingkungan self-hosted end to end](https://code.claude.com/docs/id/self-hosted-environments-testing.md): Verifikasi gambar runner self-hosted dari CI: dispatch sesi dengan CLI, baca balasan Claude melalui hook Stop, dan skrip loop lengkapnya.
- [Referensi lingkungan yang di-host sendiri](https://code.claude.com/docs/id/self-hosted-environments-reference.md): Referensi lengkap untuk runner dan orchestrator yang di-host sendiri: flag CLI, variabel lingkungan, dan metrik Prometheus.
- [Verifikasi identitas sesi di lingkungan yang di-host sendiri](https://code.claude.com/docs/id/self-hosted-environments-identity.md): Verifikasi JWT CLAUDE_CODE_SESSION_ACCESS_TOKEN sehingga layanan di jaringan Anda dapat mempercayai permintaan dari sesi di lingkungan yang di-host sendiri Anda.

#### Model dan respons

- [Konfigurasi model](https://code.claude.com/docs/id/model-config.md): Konfigurasikan model mana yang digunakan Claude Code, tingkat upaya, konteks yang diperluas, dan jendela auto-compact
- [Percepat respons dengan mode cepat](https://code.claude.com/docs/id/fast-mode.md): Dapatkan respons Opus yang lebih cepat di Claude Code dengan mengaktifkan mode cepat.
- [Eskalasi keputusan sulit dengan alat advisor](https://code.claude.com/docs/id/advisor.md): Pasangkan model utama Anda dengan model advisor yang lebih kuat yang dikonsultasikan Claude pada momen-momen kunci selama tugas.
- [Output styles](https://code.claude.com/docs/id/output-styles.md): Sesuaikan Claude Code untuk penggunaan di luar rekayasa perangkat lunak

#### Antarmuka

- [Konfigurasi terminal Anda untuk Claude Code](https://code.claude.com/docs/id/terminal-config.md): Perbaiki Shift+Enter untuk baris baru, dapatkan bel terminal saat Claude selesai, konfigurasi tmux, cocokkan tema warna, dan aktifkan mode Vim di CLI Claude Code.
- [Rendering fullscreen](https://code.claude.com/docs/id/fullscreen.md): Aktifkan mode rendering yang lebih halus dan bebas flicker dengan dukungan mouse dan penggunaan memori yang stabil dalam percakapan panjang.
- [Gunakan Claude Code dengan pembaca layar](https://code.claude.com/docs/id/accessibility.md): Atur Claude Code untuk pembaca layar seperti VoiceOver dan NVDA, plus pengaturan untuk pembesar layar, gerakan berkurang, dan tema ramah buta warna.
- [Dikte suara](https://code.claude.com/docs/id/voice-dictation.md): Ucapkan prompt Anda di Claude Code CLI dengan dikte suara tahan-untuk-merekam atau ketuk-untuk-merekam.
- [Sesuaikan baris status Anda](https://code.claude.com/docs/id/statusline.md): Konfigurasikan bilah status khusus untuk memantau penggunaan jendela konteks, biaya, dan status git di Claude Code
- [Sesuaikan pintasan keyboard](https://code.claude.com/docs/id/keybindings.md): Sesuaikan pintasan keyboard di Claude Code dengan file konfigurasi keybindings.

### Referensi

#### Referensi

- [Referensi CLI](https://code.claude.com/docs/id/cli-reference.md): Referensi lengkap untuk antarmuka baris perintah Claude Code, termasuk perintah dan flag.
- [Commands](https://code.claude.com/docs/id/commands.md): Referensi lengkap untuk perintah yang tersedia di Claude Code, termasuk perintah bawaan dan skills yang disertakan.
- [Variabel lingkungan](https://code.claude.com/docs/id/env-vars.md): Referensi untuk variabel lingkungan yang mengontrol perilaku Claude Code.
- [Referensi Tools](https://code.claude.com/docs/id/tools-reference.md): Referensi lengkap untuk tools yang dapat digunakan Claude Code, termasuk persyaratan izin dan perilaku per-tool.
- [Mode interaktif](https://code.claude.com/docs/id/interactive-mode.md): Referensi lengkap untuk pintasan keyboard, mode input, dan fitur interaktif dalam sesi Claude Code.
- [Checkpointing](https://code.claude.com/docs/id/checkpointing.md): Lacak, putar ulang, dan ringkas edit dan percakapan Claude untuk mengelola status sesi.
- [Referensi hooks](https://code.claude.com/docs/id/hooks.md): Referensi untuk event hook Claude Code, skema konfigurasi, format JSON input/output, kode keluar, hooks asinkron, hooks HTTP, prompt hooks, dan MCP tool hooks.
- [Referensi Plugins](https://code.claude.com/docs/id/plugins-reference.md): Referensi teknis lengkap untuk sistem plugin Claude Code, termasuk skema, perintah CLI, dan spesifikasi komponen.
- [Referensi Channels](https://code.claude.com/docs/id/channels-reference.md): Bangun server MCP yang mendorong webhooks, alerts, dan pesan chat ke dalam sesi Claude Code. Referensi untuk kontrak channel: deklarasi kemampuan, event notifikasi, tools balasan, gating pengirim, dan relay izin.

#### Glosarium

- [Glosarium](https://code.claude.com/docs/id/glossary.md): Definisi untuk terminologi Claude Code. Pelajari apa itu agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP, dan konsep inti lainnya.

### Agent SDK

#### Agent SDK

- [Gambaran Umum Agent SDK](https://code.claude.com/docs/id/agent-sdk/overview.md): Bangun agen AI produksi dengan Claude Code sebagai perpustakaan
- [Panduan Cepat](https://code.claude.com/docs/id/agent-sdk/quickstart.md): Mulai dengan Agent SDK Python atau TypeScript untuk membangun agen AI yang bekerja secara mandiri
- [Migrasi ke Claude Agent SDK](https://code.claude.com/docs/id/agent-sdk/migration-guide.md): Panduan untuk migrasi Claude Code TypeScript dan Python SDKs ke Claude Agent SDK
- [Troubleshoot the Agent SDK](https://code.claude.com/docs/id/agent-sdk/troubleshooting.md): Perbaiki kesalahan Agent SDK berdasarkan pesan yang tepat yang Anda lihat, dengan penyebab dan solusi untuk setiap kesalahan di SDK TypeScript dan Python.

#### Bangun agen

- [Konfigurasi agen Anda](https://code.claude.com/docs/id/agent-sdk/configuration.md): Konfigurasi sesi Agent SDK: susun objek opsi, atur model, lingkungan, dan batas, serta temukan halaman opsi setiap fitur.
- [Contoh](https://code.claude.com/docs/id/agent-sdk/examples.md): Temukan proyek Agent SDK yang lengkap dan dapat dijalankan atau resep terpandu di Claude Cookbook yang sesuai dengan apa yang ingin Anda bangun.

#### Konsep Inti

- [Cara kerja agent loop](https://code.claude.com/docs/id/agent-sdk/agent-loop.md): Pahami lifecycle pesan, eksekusi tool, context window, dan arsitektur yang menggerakkan agent SDK Anda.
- [Gunakan fitur Claude Code di SDK](https://code.claude.com/docs/id/agent-sdk/claude-code-features.md): Muat instruksi proyek, skills, hooks, dan fitur Claude Code lainnya ke dalam agen SDK Anda.
- [Bekerja dengan sesi](https://code.claude.com/docs/id/agent-sdk/sessions.md): Bagaimana sesi mempertahankan riwayat percakapan agen, dan kapan menggunakan continue, resume, dan fork untuk kembali ke run sebelumnya.
- [Simpan sesi ke penyimpanan eksternal](https://code.claude.com/docs/id/agent-sdk/session-storage.md): Cerminkan transkrip sesi Agent SDK ke object store, key-value store, atau database Anda sendiri sehingga host lain dapat melanjutkan sesi Anda.

#### Input dan output

- [Streaming Input](https://code.claude.com/docs/id/agent-sdk/streaming-vs-single-mode.md): Memahami dua mode input untuk Claude Agent SDK dan kapan menggunakan masing-masing
- [Menangani persetujuan dan input pengguna](https://code.claude.com/docs/id/agent-sdk/user-input.md): Tampilkan permintaan persetujuan Claude dan pertanyaan klarifikasi kepada pengguna, kemudian kembalikan keputusan mereka ke SDK.
- [Stream responses in real-time](https://code.claude.com/docs/id/agent-sdk/streaming-output.md): Dapatkan respons real-time dari Agent SDK saat teks dan tool calls streaming masuk
- [Dapatkan output terstruktur dari agen](https://code.claude.com/docs/id/agent-sdk/structured-outputs.md): Kembalikan JSON yang divalidasi dari alur kerja agen menggunakan JSON Schema, Zod, atau Pydantic. Dapatkan data terstruktur yang aman tipe setelah penggunaan alat multi-putaran.

#### Perluas dengan tools

- [Berikan Claude alat kustom](https://code.claude.com/docs/id/agent-sdk/custom-tools.md): Tentukan alat kustom dengan server MCP dalam proses SDK Agent sehingga Claude dapat memanggil fungsi Anda, mengakses API Anda, dan melakukan operasi khusus domain.
- [Hubungkan ke alat eksternal dengan MCP](https://code.claude.com/docs/id/agent-sdk/mcp.md): Konfigurasi server MCP untuk memperluas agen Anda dengan alat eksternal. Mencakup jenis transport, pencarian alat untuk set alat besar, autentikasi, dan penanganan kesalahan.
- [Skalakan ke banyak tools dengan pencarian tools](https://code.claude.com/docs/id/agent-sdk/tool-search.md): Skalakan agen Anda ke ribuan tools dengan menemukan dan memuat hanya yang diperlukan, sesuai permintaan.
- [Subagents dalam SDK](https://code.claude.com/docs/id/agent-sdk/subagents.md): Tentukan dan panggil subagents untuk mengisolasi konteks, menjalankan tugas secara paralel, dan menerapkan instruksi khusus dalam aplikasi Claude Agent SDK Anda.

#### Sesuaikan perilaku

- [Memodifikasi system prompts](https://code.claude.com/docs/id/agent-sdk/modifying-system-prompts.md): Pilih antara preset `claude_code` dan system prompt kustom, serta sesuaikan perilaku dengan CLAUDE.md, output styles, append, atau prompt yang sepenuhnya kustom.
- [Perluas agen dengan skills](https://code.claude.com/docs/id/agent-sdk/skills.md): Kontrol skill mana yang dapat Claude panggil dalam sesi Claude Agent SDK, dispatch perintah berdasarkan nama, dan buat skills yang sesi Anda temukan
- [Plugins dalam SDK](https://code.claude.com/docs/id/agent-sdk/plugins.md): Muat plugin kustom untuk memperluas Claude Code dengan skills, agen, hooks, dan server MCP melalui Agent SDK

#### Kontrol dan observabilitas

- [Konfigurasi izin](https://code.claude.com/docs/id/agent-sdk/permissions.md): Kontrol bagaimana agen Anda menggunakan alat dengan mode izin, hooks, dan aturan allow/deny deklaratif.
- [Intercept dan kontrol perilaku agent dengan hooks](https://code.claude.com/docs/id/agent-sdk/hooks.md): Intercept dan customize perilaku agent pada titik eksekusi kunci dengan hooks
- [Kembalikan perubahan file dengan checkpointing](https://code.claude.com/docs/id/agent-sdk/file-checkpointing.md): Lacak perubahan file selama sesi agen dan pulihkan file ke status sebelumnya
- [Lacak biaya dan penggunaan](https://code.claude.com/docs/id/agent-sdk/cost-tracking.md): Pelajari cara melacak penggunaan token, memperkirakan biaya, dan mengonfigurasi prompt caching dengan Claude Agent SDK.
- [Observability dengan OpenTelemetry](https://code.claude.com/docs/id/agent-sdk/observability.md): Ekspor traces, metrics, dan events dari Agent SDK ke backend observability Anda menggunakan OpenTelemetry.
- [Lacak todos](https://code.claude.com/docs/id/agent-sdk/todo-tracking.md): Lacak todos dalam sesi Agent SDK dan tampilkan kemajuan Claude dalam aplikasi Anda dari panggilan alat terstruktur

#### Penyebaran

- [Hosting the Agent SDK](https://code.claude.com/docs/id/agent-sdk/hosting.md): Terapkan Agent SDK dalam produksi: arsitektur subprocess, persistensi sesi, penskalaan, observabilitas, dan isolasi multi-tenant untuk Docker, Kubernetes, dan penyedia sandbox.
- [Mengamankan penyebaran agen AI](https://code.claude.com/docs/id/agent-sdk/secure-deployment.md): Panduan untuk mengamankan penyebaran Claude Code dan Agent SDK dengan isolasi, manajemen kredensial, dan kontrol jaringan

#### Referensi SDK

- [Agent SDK reference - TypeScript](https://code.claude.com/docs/id/agent-sdk/typescript.md): Referensi API lengkap untuk TypeScript Agent SDK, termasuk semua fungsi, tipe, dan antarmuka.
- [TypeScript SDK V2 session API (dihapus)](https://code.claude.com/docs/id/agent-sdk/typescript-v2-preview.md): Referensi untuk API sesi SDK Agent TypeScript V2 yang dihapus, dengan pola send/stream berbasis sesi untuk percakapan multi-turn.
- [Referensi Agent SDK - Python](https://code.claude.com/docs/id/agent-sdk/python.md): Referensi API lengkap untuk Python Agent SDK, termasuk semua fungsi, tipe, dan kelas.

### Apa yang Baru

#### Apa yang Baru

- [Apa yang baru](https://code.claude.com/docs/id/whats-new/index.md): Ringkasan mingguan fitur Claude Code yang penting, dengan cuplikan kode, demo, dan konteks tentang mengapa hal-hal ini penting.
- [Minggu 37 · 7–11 September 2026](https://code.claude.com/docs/id/whats-new/2026-w37.md): Uji plugin Anda dengan claude plugin eval dan keluarkan panel Claude Code Desktop ke jendela terpisah mereka sendiri.
- [Minggu 36 · 31 Agustus – 4 September 2026](https://code.claude.com/docs/id/whats-new/2026-w36.md): Beralih ke Claude Fable 5.1, biarkan computer use berjalan di latar belakang di Desktop, dan tonton edit Claude di panel /diff langsung.
- [Minggu 35 · 24–28 Agustus 2026](https://code.claude.com/docs/id/whats-new/2026-w35.md): Lanjutkan sesi terminal di aplikasi Claude Code Desktop, tinjau laporan umpan balik yang Claude buat untuk Anda, dan mulai sesi dalam mode terbatas.
- [Minggu 34 · 17–21 Agustus 2026](https://code.claude.com/docs/id/whats-new/2026-w34.md): Buat papan seni UI yang dapat diedit dengan skill /design, atur gaya output Concise, dan mulai sesi Claude Code di mesin Anda dari ponsel Anda.
- [Minggu 33 · 10–14 Agustus 2026](https://code.claude.com/docs/id/whats-new/2026-w33.md): Claude Code Desktop melanjutkan secara otomatis setelah batas penggunaan direset, mode fork aktif secara default, dan permintaan penggabungan GitLab serta marketplace bergabung dengan GitHub.
- [Minggu 32 · 3–7 Agustus, 2026](https://code.claude.com/docs/id/whats-new/2026-w32.md): Sesi Claude Code saling berkirim pesan, lingkungan yang di-host sendiri menjalankan sesi cloud di infrastruktur Anda, dan mode otomatis menjadi mode izin default.
- [Minggu 30 · 20–24 Juli, 2026](https://code.claude.com/docs/id/whats-new/2026-w30.md): Opus 5 menjadi model Opus default, Claude Code Desktop menambahkan panel iOS Simulator, dan plugin Claude Security memindai kode Anda untuk menemukan kerentanan.
- [Minggu 29 · 13–17 Juli, 2026](https://code.claude.com/docs/id/whats-new/2026-w29.md): Tarik data langsung ke dalam artefak yang dipublikasikan melalui konektor MCP, dan gunakan Claude Code dengan pembaca layar dalam mode pembaca layar baru.
- [Minggu 28 · 6–10 Juli, 2026](https://code.claude.com/docs/id/whats-new/2026-w28.md): Jelajahi situs eksternal dari browser bawaan aplikasi Desktop, jalankan pemeriksaan pengaturan lengkap dengan /doctor, dan dapatkan perlindungan transkrip mode otomatis dan peningkatan tampilan agen.
- [Minggu 27 · 29 Juni – 3 Juli 2026](https://code.claude.com/docs/id/whats-new/2026-w27.md): Claude Sonnet 5 menjadi model default, Claude di Chrome mencapai ketersediaan umum, subagents berjalan di latar belakang secara default, Claude Desktop tiba di Linux dalam beta, dan /radio menyetel Claude FM.
- [Minggu 26 · 22–26 Juni 2026](https://code.claude.com/docs/id/whats-new/2026-w26.md): Autentikasi server MCP dari shell Anda dengan claude mcp login, dapatkan respons terhadap output perintah shell mode dengan awalan !, dan lanjutkan percakapan dari sebelum /clear dengan /rewind.
- [Minggu 25 · 15–19 Juni 2026](https://code.claude.com/docs/id/whats-new/2026-w25.md): Publikasikan halaman langsung yang dapat dibagikan dari sesi Anda dengan Artifacts, cocokkan parameter alat dalam aturan deny dan ask, dan atur pengaturan apa pun dari prompt dengan /config.
- [Minggu 24 · 8–12 Juni 2026](https://code.claude.com/docs/id/whats-new/2026-w24.md): Pindahkan sesi ke direktori baru dengan /cd, biarkan sub-agen menjalankan sub-agen mereka sendiri, dan selesaikan konfigurasi yang rusak dengan mode aman.
- [Minggu 23 · 1–5 Juni 2026](https://code.claude.com/docs/id/whats-new/2026-w23.md): Jalankan auto mode di Amazon Bedrock, Google Cloud's Agent Platform, dan Microsoft Foundry, minta persetujuan sebelum menulis file yang dapat menjalankan kode dalam mode acceptEdits, daftar plugin yang terinstal dengan /plugin list, dan perlukan rentang versi yang disetujui untuk penerapan terkelola…
- [Minggu 22 · 25–29 Mei, 2026](https://code.claude.com/docs/id/whats-new/2026-w22.md): Jalankan Claude Code di Claude Opus 4.8, orkestrasi tugas besar dengan alur kerja dinamis, tangkap masalah keamanan dengan plugin security-guidance, dan gunakan fast mode di Opus 4.8 dengan harga lebih rendah.
- [Minggu 21 · 18–22 Mei, 2026](https://code.claude.com/docs/id/whats-new/2026-w21.md): Gunakan auto mode pada paket Pro dan dengan Sonnet 4.6, lihat skill, subagent, dan server MCP mana yang mendorong batas paket Anda di /usage, dan tinjau diff dengan perintah /code-review yang baru.
- [Minggu 20 · 11–15 Mei, 2026](https://code.claude.com/docs/id/whats-new/2026-w20.md): Kelola setiap sesi Claude Code dari satu layar dengan tampilan agen, biarkan Claude bekerja menuju tujuan hingga kondisi terpenuhi, dan jalankan mode cepat di Opus 4.7 secara default.
- [Minggu 19 · 4–8 Mei 2026](https://code.claude.com/docs/id/whats-new/2026-w19.md): Muat plugin dari arsip .zip dan URL, cari riwayat perintah di seluruh proyek dengan Ctrl+R, cabang worktree baru dari HEAD lokal atau default jarak jauh, dan blokir tindakan tanpa syarat dengan aturan hard deny mode otomatis.
- [Minggu 18 · 27 April – 1 Mei, 2026](https://code.claude.com/docs/id/whats-new/2026-w18.md): Claude Code di Windows berjalan tanpa Git Bash, claude auth login menerima kode OAuth yang ditempel langsung, claude project purge membersihkan status lokal per proyek, dan menempel URL PR ke /resume menemukan sesi yang membuatnya.
- [Minggu 17 · 20–24 April 2026](https://code.claude.com/docs/id/whats-new/2026-w17.md): /ultrareview dibuka sebagai pratinjau penelitian, ringkasan sesi otomatis saat Anda kembali ke terminal, tema warna khusus yang dapat Anda buat dan kirim dalam plugin, dan Claude Code yang dirancang ulang di web.
- [Minggu 16 · 13–17 April 2026](https://code.claude.com/docs/id/whats-new/2026-w16.md): Claude Opus 4.7 dengan tingkat upaya xhigh baru, Routines di Claude Code di web, notifikasi push mobile yang mengirim ping ke ponsel Anda ketika Claude membutuhkan Anda, /usage breakdown yang menunjukkan apa yang mendorong batas Anda, dan binari asli menggantikan JavaScript yang dibundel.
- [Minggu 15 · 6–10 April 2026](https://code.claude.com/docs/id/whats-new/2026-w15.md): Ultraplan perencanaan cloud, alat Monitor dengan self-pacing /loop, /team-onboarding untuk mengemas setup Anda, dan /autofix-pr dari terminal Anda.
- [Minggu 14 · 30 Maret – 3 April 2026](https://code.claude.com/docs/id/whats-new/2026-w14.md): Computer use di CLI, pelajaran interaktif dalam produk, rendering tanpa flicker, override ukuran hasil MCP per-tool, dan executable plugin di PATH.
- [Minggu 13 · 23–27 Maret 2026](https://code.claude.com/docs/id/whats-new/2026-w13.md): Mode otomatis untuk izin tanpa tangan, penggunaan komputer bawaan, perbaikan PR otomatis di cloud, pencarian transkrip, dan alat PowerShell untuk Windows.

### Sumber Daya

#### Sumber Daya

- [Hukum dan kepatuhan](https://code.claude.com/docs/id/legal-and-compliance.md): Perjanjian hukum, sertifikasi kepatuhan, dan informasi keamanan untuk Claude Code.

---

## Claude Code Docs: Italian

- 官方原文：https://code.claude.com/docs/_llms/it.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-it.md`

# Claude Code Docs: Italian

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Italian

### Guida introduttiva

#### Guida introduttiva

- [Panoramica](https://code.claude.com/docs/it/overview.md): Claude Code è uno strumento di codifica agentivo che legge la tua base di codice, modifica i file, esegue comandi e si integra con i tuoi strumenti di sviluppo. Disponibile nel tuo terminale, IDE, app desktop e browser.
- [Guida rapida](https://code.claude.com/docs/it/quickstart.md): Benvenuto in Claude Code!
- [Changelog](https://code.claude.com/docs/it/changelog.md)

#### Concetti fondamentali

- [Come funziona Claude Code](https://code.claude.com/docs/it/how-claude-code-works.md): Comprendi il ciclo agentico, gli strumenti integrati e come Claude Code interagisce con il tuo progetto.
- [Estendi Claude Code](https://code.claude.com/docs/it/features-overview.md): Comprendi quando utilizzare CLAUDE.md, Skills, subagents, hooks, MCP e plugins.
- [Esplora la directory .claude](https://code.claude.com/docs/it/claude-directory.md): Dove Claude Code legge CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules e auto memory. Esplora la directory .claude nel tuo progetto e ~/.claude nella tua home directory.
- [Esplora la finestra di contesto](https://code.claude.com/docs/it/context-window.md): Una simulazione interattiva di come la finestra di contesto di Claude Code si riempie durante una sessione. Vedi cosa si carica automaticamente, quanto costa ogni lettura di file e quando si attivano le regole e gli hook.
- [Come Claude Code utilizza il prompt caching](https://code.claude.com/docs/it/prompt-caching.md): Claude Code gestisce il prompt caching automaticamente. Scopri perché un cambio di modello attiva un turno lento senza cache, quanto costa `/compact`, perché le modifiche a CLAUDE.md non si applicano a metà sessione e come controllare il tasso di cache hit.

#### Usa Claude Code

- [Come Claude ricorda il tuo progetto](https://code.claude.com/docs/it/memory.md): Fornisci a Claude istruzioni persistenti con file CLAUDE.md o AGENTS.md e lascia che Claude accumuli apprendimenti automaticamente con la memoria automatica.
- [Gestire le sessioni](https://code.claude.com/docs/it/sessions.md): Assegnare nomi, riprendere, creare rami e passare tra conversazioni di Claude Code. Copre `--continue`, `--resume`, `--from-pr`, il selezionatore `/resume`, la denominazione delle sessioni, l'esportazione dei trascritti e dove vengono archiviati i trascritti.
- [Flussi di lavoro comuni](https://code.claude.com/docs/it/common-workflows.md): Guide passo dopo passo per esplorare basi di codice, correggere bug, effettuare refactoring, testare e altri compiti quotidiani con Claude Code.
- [Libreria di prompt](https://code.claude.com/docs/it/prompt-library.md): Copia e incolla prompt per Claude Code, etichettati per attività e ruolo.
- [Best practices for Claude Code](https://code.claude.com/docs/it/best-practices.md): Suggerimenti e modelli per ottenere il massimo da Claude Code, dalla configurazione dell'ambiente al ridimensionamento tra sessioni parallele.

#### Piattaforme e integrazioni

- [Piattaforme e integrazioni](https://code.claude.com/docs/it/platforms.md): Scegli dove eseguire Claude Code e cosa collegare. Confronta CLI, Desktop, VS Code, JetBrains, web, mobile e integrazioni come Chrome, Slack e CI/CD.
- [Continua le sessioni locali da qualsiasi dispositivo con Remote Control](https://code.claude.com/docs/it/remote-control.md): Continua una sessione locale di Claude Code dal tuo telefono, tablet o da qualsiasi browser utilizzando Remote Control. Funziona con claude.ai/code e l'app Claude per dispositivi mobili.
- [Lascia che Claude coordini il lavoro in corso con Projects](https://code.claude.com/docs/it/claude-projects.md): Fornisci a Claude un corpo di lavoro correlato in una conversazione e lascia che coordini sessioni cloud parallele che condividono repository, istruzioni e memoria.
- [Claude Code su mobile](https://code.claude.com/docs/it/mobile.md): Avvia, monitora e guida i task di Claude Code dal tuo telefono con l'app Claude per iOS e Android.
- [Usa Claude Code con Chrome](https://code.claude.com/docs/it/chrome.md): Connetti Claude Code al tuo browser Chrome per testare app web, eseguire il debug con i log della console, automatizzare la compilazione di moduli ed estrarre dati dalle pagine web.
- [Consenti a Claude di usare il tuo computer dalla CLI](https://code.claude.com/docs/it/computer-use.md): Abilita computer use in Claude Code CLI affinché Claude possa aprire app, fare clic, digitare e vedere il tuo schermo su macOS. Testa app native, esegui il debug di problemi visivi e automatizza strumenti solo GUI senza lasciare il tuo terminale.
- [Usa Claude Code in VS Code](https://code.claude.com/docs/it/vs-code.md): Installa e configura l'estensione Claude Code per VS Code. Ottieni assistenza di codifica con IA con diff inline, @-mention, revisione del piano e scorciatoie da tastiera.
- [JetBrains IDEs](https://code.claude.com/docs/it/jetbrains.md): Usa Claude Code con JetBrains IDEs inclusi IntelliJ, PyCharm, WebStorm e altri
- [Claude Code in Slack](https://code.claude.com/docs/it/slack.md): Delega i compiti di codifica direttamente dal tuo workspace Slack. Anthropic sta ritirando questa versione precedente per i workspace Team ed Enterprise a favore di Claude Tag; rimane il percorso di configurazione per i piani Pro e Max.
- [Claude Tag](https://code.claude.com/docs/it/claude-tag.md): Porta Claude nei canali Slack del tuo team con Claude Tag e trova la documentazione di configurazione e utilizzo su claude.com.

##### Claude Code nel cloud

- [Iniziare con Claude Code nel cloud](https://code.claude.com/docs/it/web-quickstart.md): Esegui Claude Code nel cloud dal tuo browser o telefono. Connetti un repository GitHub, invia un'attività e rivedi la PR senza configurazione locale.
- [Usa Claude Code nel cloud](https://code.claude.com/docs/it/claude-code-on-the-web.md): Esegui sessioni Claude Code nel cloud dal tuo browser, telefono, app desktop o terminale, spostale con --cloud e --teleport, e correggi automaticamente le pull request.
- [Automatizzare il lavoro con le routine](https://code.claude.com/docs/it/routines.md): Metti Claude Code in modalità automatica. Definisci routine che vengono eseguite secondo una pianificazione, attivate da chiamate API o che reagiscono agli eventi di GitHub dall'infrastruttura cloud gestita da Anthropic.
- [Trova bug con ultrareview](https://code.claude.com/docs/it/ultrareview.md): Esegui una revisione del codice profonda e multi-agente nel cloud con /code-review ultra per trovare e verificare i bug prima di eseguire il merge.

##### Claude Code sul desktop

- [Iniziare con l'app desktop](https://code.claude.com/docs/it/desktop-quickstart.md): Installa Claude Code su desktop e avvia la tua prima sessione di codifica
- [Applicazione desktop](https://code.claude.com/docs/it/desktop.md): Sfrutta al massimo Claude Code Desktop: sessioni parallele con isolamento Git, layout dei pannelli drag-and-drop, terminale integrato e editor di file, chat laterali, utilizzo del computer, Dispatch sessioni dal tuo telefono, revisione visiva dei diff, anteprime delle app, monitoraggio dei PR, conne…
- [Claude Desktop su Linux (beta)](https://code.claude.com/docs/it/desktop-linux.md): Installa e aggiorna l'app desktop di Claude su Ubuntu e Debian
- [Claude Code Desktop in WSL](https://code.claude.com/docs/it/desktop-wsl.md): Esegui sessioni Code all'interno di una distribuzione WSL 2 su Windows
- [Pianificare attività ricorrenti in Claude Code Desktop](https://code.claude.com/docs/it/desktop-scheduled-tasks.md): Configura attività pianificate in Claude Code Desktop per eseguire Claude automaticamente su base ricorrente per revisioni del codice giornaliere, audit delle dipendenze o briefing mattutini.
- [Testare app iOS nel simulatore](https://code.claude.com/docs/it/desktop-ios-simulator.md): Claude Code Desktop apre la tua app nel riquadro iOS Simulator quando Claude la compila, esegue o la verifica, con un simulatore separato per ogni sessione.

##### Revisione del codice e CI/CD

- [Rileva problemi di sicurezza mentre Claude scrive il codice](https://code.claude.com/docs/it/security-guidance.md): Installa il plugin security-guidance per far sì che Claude riveda le proprie modifiche al codice per individuare vulnerabilità e correggerle nella stessa sessione.
- [Scansiona il tuo codebase per le vulnerabilità](https://code.claude.com/docs/it/claude-security.md): Installa il plugin Claude Security per scansionare il tuo codebase alla ricerca di vulnerabilità in una sessione Claude Code e trasforma i risultati in patch che esamini e applichi.
- [Code Review](https://code.claude.com/docs/it/code-review.md): Configura revisioni automatiche dei PR che rilevano errori logici, vulnerabilità di sicurezza e regressioni utilizzando l'analisi multi-agente dell'intero codebase
- [Claude Code GitHub Actions](https://code.claude.com/docs/it/github-actions.md): Esegui Claude Code nei flussi di lavoro di GitHub Actions per rispondere alle menzioni @claude, automatizzare attività e trasformare issue in pull request
- [Usa Claude Code GitHub Actions con i provider cloud](https://code.claude.com/docs/it/github-actions-cloud-providers.md): Esegui Claude Code GitHub Actions tramite Amazon Bedrock, Google Cloud's Agent Platform o Microsoft Foundry invece dell'API Claude
- [Claude Code con GitHub Enterprise Server](https://code.claude.com/docs/it/github-enterprise-server.md): Connetti Claude Code alla tua istanza GitHub Enterprise Server auto-ospitata per sessioni cloud, revisione del codice e marketplace di plugin.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/it/gitlab-ci-cd.md): Scopri come integrare Claude Code nel tuo flusso di lavoro di sviluppo con GitLab CI/CD

### Sviluppa con Claude Code

#### Agenti e lavoro parallelo

- [Eseguire agenti in parallelo](https://code.claude.com/docs/it/agents.md): Confronta i modi in cui Claude Code può affrontare più attività contemporaneamente: subagenti, visualizzazione agenti, team di agenti, flussi di lavoro dinamici e progetti.
- [Creare subagent personalizzati](https://code.claude.com/docs/it/sub-agents.md): Creare e utilizzare subagent AI specializzati in Claude Code per flussi di lavoro specifici di attività e una migliore gestione del contesto.
- [Gestire più agenti con agent view](https://code.claude.com/docs/it/agent-view.md): Invia e gestisci molte sessioni di Claude Code da una sola schermata. Agent view mostra cosa sta facendo ogni sessione e quali hanno bisogno del tuo input.
- [Orchestrare team di sessioni Claude Code](https://code.claude.com/docs/it/agent-teams.md): Coordinare più istanze di Claude Code che lavorano insieme come un team, con attività condivise, messaggistica tra agenti e gestione centralizzata.
- [Messaggi tra le tue altre sessioni di Claude Code](https://code.claude.com/docs/it/cross-session-messaging.md): Consenti a Claude di elencare e inviare messaggi alle tue altre sessioni di Claude Code su questa macchina, e raggiungi le tue sessioni su altre macchine o nel cloud.
- [Orchestrare subagenti su larga scala con flussi di lavoro dinamici](https://code.claude.com/docs/it/workflows.md): I flussi di lavoro dinamici orchestrano molti subagenti da uno script che Claude scrive e che puoi rieseguire. Usali per audit di codebase, migrazioni su larga scala e ricerche con verifica incrociata.
- [Eseguire sessioni parallele con worktrees](https://code.claude.com/docs/it/worktrees.md): Isolare sessioni parallele di Claude Code in worktrees git separati in modo che i cambiamenti non si scontrino. Copre il flag `--worktree`, l'isolamento dei subagent, `.worktreeinclude`, la pulizia e gli hook VCS non-git.

#### MCP

- [Connettere i server MCP](https://code.claude.com/docs/it/mcp-quickstart.md): Aggiungere un server MCP a Claude Code, verificare la connessione e trovare la configurazione su disco.
- [Connetti Claude Code ai tuoi strumenti tramite MCP](https://code.claude.com/docs/it/mcp.md): Scopri come connettere Claude Code ai tuoi strumenti con il Model Context Protocol.

#### Skills

- [Estendi Claude con skills](https://code.claude.com/docs/it/skills.md): Crea, gestisci e condividi skills per estendere le capacità di Claude in Claude Code. Include comandi personalizzati e skills raggruppate.

#### Plugin

- [Scopri e installa plugin precostruiti tramite marketplace](https://code.claude.com/docs/it/discover-plugins.md): Trova e installa plugin dai marketplace per estendere Claude Code con nuove skills, agenti e funzionalità.
- [Creare plugin](https://code.claude.com/docs/it/plugins.md): Crea plugin personalizzati per estendere Claude Code con skills, agents, hooks e MCP servers.
- [Testare i plugin con evals](https://code.claude.com/docs/it/plugin-evals.md): Scrivi casi di eval per il tuo plugin Claude Code, eseguili con claude plugin eval, valuta i risultati, confrontali con una baseline senza plugin e gating CI sul punteggio.

#### Artefatti

- [Condividi l'output della sessione come artifact](https://code.claude.com/docs/it/artifacts.md): Gli artifact trasformano il lavoro di Claude Code in pagine live e interattive su claude.ai che puoi mantenere private, condividere con la tua organizzazione o pubblicare con un link pubblico.

#### Automazione

- [Automatizzare le azioni con hooks](https://code.claude.com/docs/it/hooks-guide.md): Esegui comandi shell automaticamente quando Claude Code modifica file, completa attività o ha bisogno di input. Formatta il codice, invia notifiche, convalida comandi e applica le regole del progetto.
- [Invia eventi in una sessione in esecuzione con i canali](https://code.claude.com/docs/it/channels.md): Utilizza i canali per inviare messaggi, avvisi e webhook nella tua sessione Claude Code da un server MCP. Inoltra i risultati CI, i messaggi di chat e gli eventi di monitoraggio in modo che Claude possa reagire mentre sei assente.
- [Eseguire prompt in base a una pianificazione](https://code.claude.com/docs/it/scheduled-tasks.md): Utilizzare /loop e gli strumenti di pianificazione cron per eseguire prompt ripetutamente, eseguire il polling dello stato o impostare promemoria una tantum all'interno di una sessione Claude Code.
- [Mantenere Claude al lavoro verso un obiettivo](https://code.claude.com/docs/it/goal.md): Imposta una condizione di completamento con /goal e Claude continua a lavorare finché non è soddisfatta, un modello la giudica impossibile, o un errore che Lei deve correggere cancella l'obiettivo.
- [Eseguire Claude Code a livello programmatico](https://code.claude.com/docs/it/headless.md): Utilizza l'Agent SDK per eseguire Claude Code a livello programmatico dalla CLI, Python o TypeScript.
- [Avviare sessioni dai link](https://code.claude.com/docs/it/deep-links.md): Apri una sessione di terminale Claude Code da un URL. Incorpora link `claude-cli://` in runbook, avvisi e dashboard in modo che un clic apra Claude Code nel repository corretto con il prompt corretto.

#### Guide

- [Configurare Claude Code in un monorepo o in un codebase di grandi dimensioni](https://code.claude.com/docs/it/large-codebases.md): Configura Claude Code per monorepo e codebase a singolo albero di grandi dimensioni con file CLAUDE.md annidati, worktree sparse, code intelligence e skills per pacchetto in modo che Claude rimanga focalizzato sul codice su cui stai lavorando.

#### Risoluzione dei problemi

- [Risolvi i problemi di installazione e accesso](https://code.claude.com/docs/it/troubleshoot-install.md): Correggi gli errori di comando non trovato, PATH, permessi, rete e autenticazione durante l'installazione o l'accesso a Claude Code.
- [Troubleshooting](https://code.claude.com/docs/it/troubleshooting.md): Risolvi i problemi di utilizzo elevato di CPU o memoria, blocchi, thrashing auto-compact e problemi di ricerca in Claude Code, e trova la pagina giusta per altri problemi.
- [Esegui il debug della tua configurazione](https://code.claude.com/docs/it/debug-your-config.md): Diagnostica perché CLAUDE.md, impostazioni, hooks, server MCP o skills non hanno effetto. Usa /context, /doctor, /hooks e /mcp per vedere cosa è stato effettivamente caricato.
- [Riferimento degli errori](https://code.claude.com/docs/it/errors.md): Cercate i messaggi di errore di runtime di Claude Code con il significato di ciascuno e come risolverlo.

### Amministrazione

#### Configurazione e accesso

- [Configurare Claude Code per la tua organizzazione](https://code.claude.com/docs/it/admin-setup.md): Una mappa decisionale per gli amministratori che distribuiscono Claude Code, che copre i provider API, le impostazioni gestite, l'applicazione delle policy, il monitoraggio dell'utilizzo e la gestione dei dati.
- [Configurazione avanzata](https://code.claude.com/docs/it/setup.md): Requisiti di sistema, installazione specifica per piattaforma, gestione delle versioni e disinstallazione per Claude Code.
- [Autenticazione](https://code.claude.com/docs/it/authentication.md): Accedi a Claude Code e configura l'autenticazione per singoli utenti, team e organizzazioni.
- [Distribuire impostazioni gestite](https://code.claude.com/docs/it/managed-settings.md): Distribuire impostazioni gestite su ogni macchina dello sviluppatore: meccanismi di consegna per sistema operativo, come Claude Code combina le fonti gestite e come verificare l'applicazione.
- [Configurare le impostazioni gestite dal server](https://code.claude.com/docs/it/server-managed-settings.md): Configurare centralmente Claude Code per la vostra organizzazione tramite impostazioni consegnate dal server, senza richiedere infrastrutture di gestione dei dispositivi.
- [Controllare l'accesso ai server MCP per la vostra organizzazione](https://code.claude.com/docs/it/managed-mcp.md): Limitare quali server MCP gli utenti possono aggiungere o connettere, o fornire server a ogni utente, con file di configurazione gestiti, impostazioni gestite, allowlist e denylists.
- [Configurare la modalità auto](https://code.claude.com/docs/it/auto-mode-config.md): Comunica al classificatore della modalità auto quali repository, bucket e domini la tua organizzazione ritiene affidabili. Imposta il contesto dell'ambiente, sostituisci le regole di blocco e autorizzazione predefinite e ispeziona la tua configurazione effettiva con i sottocomandi CLI della modalità…

#### Distribuzione

- [Panoramica della distribuzione aziendale](https://code.claude.com/docs/it/third-party-integrations.md): Scopri come Claude Code può integrarsi con vari servizi di terze parti e infrastrutture per soddisfare i requisiti di distribuzione aziendale.
- [Disponibilità delle funzionalità](https://code.claude.com/docs/it/feature-availability.md): Confronta quali funzionalità di Claude Code sono disponibili nei piani di abbonamento Anthropic, nella Console Anthropic, in Amazon Bedrock, su Claude Platform on AWS, in Google Cloud's Agent Platform e in Microsoft Foundry.
- [Claude Code su Amazon Bedrock](https://code.claude.com/docs/it/amazon-bedrock.md): Scopri come configurare Claude Code tramite Amazon Bedrock, inclusa la configurazione, la configurazione IAM e la risoluzione dei problemi.
- [Claude Code su Claude Platform on AWS](https://code.claude.com/docs/it/claude-platform-on-aws.md): Configura Claude Code per utilizzare l'API Claude gestita da Anthropic con autenticazione AWS, controllo dell'accesso IAM e fatturazione tramite AWS Marketplace.
- [Claude Code su Google Cloud's Agent Platform](https://code.claude.com/docs/it/google-vertex-ai.md): Scopri come configurare Claude Code tramite Google Cloud's Agent Platform, precedentemente Vertex AI, inclusa la configurazione, la configurazione IAM e la risoluzione dei problemi.
- [Claude Code su Microsoft Foundry](https://code.claude.com/docs/it/microsoft-foundry.md): Scopri come configurare Claude Code tramite Microsoft Foundry, inclusi setup, configurazione e risoluzione dei problemi.
- [Configurazione di rete aziendale](https://code.claude.com/docs/it/network-config.md): Configurare Claude Code per ambienti aziendali con server proxy, Autorità di Certificazione (CA) personalizzate e autenticazione Transport Layer Security (mTLS) reciproca.
- [Eseguire Claude Code dietro un launcher aziendale](https://code.claude.com/docs/it/corporate-launcher.md): Instradare i processi che Claude Code avvia dal suo binario, incluso il servizio in background e ogni sessione di agent view, attraverso un launcher obbligatorio con CLAUDE_CODE_PROCESS_WRAPPER o l'impostazione processWrapper.
- [Contenitori di sviluppo](https://code.claude.com/docs/it/devcontainer.md): Esegui Claude Code all'interno di un contenitore di sviluppo per ambienti coerenti e isolati in tutto il tuo team.

#### Gateway

- [Eseguire Claude Code attraverso un gateway](https://code.claude.com/docs/it/gateways.md): Instrada Claude Code attraverso un gateway auto-ospitato per credenziali centralizzate, tracciamento dell'utilizzo e controlli dei costi. Copre l'architettura, il gateway delle app Claude di Anthropic e l'utilizzo di altri prodotti gateway.

##### Gateway app Claude

- [Gateway di app Claude per Amazon Bedrock, Claude Platform su AWS, Google Cloud e Microsoft Foundry](https://code.claude.com/docs/it/claude-apps-gateway.md): Esegui Claude Code attraverso Amazon Bedrock, Claude Platform su AWS, Google Cloud o Microsoft Foundry dietro un gateway auto-ospitato con accesso SSO, accesso ai modelli per gruppo e telemetria OTLP.
- [Configurazione del gateway delle app Claude](https://code.claude.com/docs/it/claude-apps-gateway-config.md): Riferimento per ogni opzione di gateway.yaml: listener e TLS, OIDC, sessione, archivio Postgres, upstream Amazon Bedrock, Claude Platform su AWS, Agent Platform di Google Cloud e Microsoft Foundry, routing dei modelli, criteri gestiti e telemetria.
- [Limiti di spesa del gateway delle app Claude](https://code.claude.com/docs/it/claude-apps-gateway-spend-limits.md): Limita la spesa di ogni sviluppatore attraverso il gateway delle app Claude per giorno, settimana o mese. Imposta i limiti con un'API Admin e il gateway li applica in tempo reale su ogni richiesta.
- [Distribuzione e operazioni del gateway delle app Claude](https://code.claude.com/docs/it/claude-apps-gateway-deploy.md): Registrare il gateway con il vostro IdP, costruire il container, distribuire su Kubernetes o Cloud Run, e gestirlo: controlli di integrità, rotazione dei segreti, aggiornamenti e sicurezza.
- [Distribuire il gateway delle app Claude su AWS](https://code.claude.com/docs/it/claude-apps-gateway-on-aws.md): Un esempio pratico di esecuzione del gateway delle app Claude su AWS: ECS Fargate o EKS, Amazon RDS per PostgreSQL, AWS Secrets Manager e autenticazione basata su ruoli IAM ad Amazon Bedrock.
- [Distribuire il gateway delle app Claude su Google Cloud](https://code.claude.com/docs/it/claude-apps-gateway-on-gcp.md): Un esempio pratico di esecuzione del gateway delle app Claude su Google Cloud: Cloud Run o GKE, Cloud SQL per PostgreSQL, Secret Manager e autenticazione tramite account di servizio verso Agent Platform di Google Cloud.

##### Altri gateway

- [Gateway LLM altri](https://code.claude.com/docs/it/llm-gateway.md): Instrada Claude Code attraverso un gateway LLM che la tua organizzazione già esegue. Copre il collegamento di Claude Code a un gateway, il rollout per la tua organizzazione e cosa Claude Code invia a un gateway.
- [Connetti Claude Code a un gateway LLM](https://code.claude.com/docs/it/llm-gateway-connect.md): Indirizza Claude Code al gateway LLM della tua organizzazione. Verifica se il tuo amministratore lo ha già configurato, oppure imposta l'URL di base e le credenziali da solo, quindi verifica la connessione e risolvi gli errori del gateway.
- [Distribuire un gateway LLM per la vostra organizzazione](https://code.claude.com/docs/it/llm-gateway-rollout.md): Distribuire un prodotto gateway per Claude Code: configurarlo per inoltrare ciò che Claude Code invia, emettere credenziali per sviluppatori, distribuire la configurazione tramite impostazioni gestite e verificare la distribuzione.
- [Guida di compatibilità del gateway Claude Code](https://code.claude.com/docs/it/llm-gateway-protocol.md): Mantieni un gateway LLM compatibile con Claude Code: gli endpoint che chiama, le intestazioni e i campi del corpo da inoltrare, e cosa si interrompe quando vengono rimossi.

#### Utilizzo e costi

- [Monitoraggio](https://code.claude.com/docs/it/monitoring-usage.md): Scopri come abilitare e configurare OpenTelemetry per Claude Code.
- [Gestisci i costi in modo efficace](https://code.claude.com/docs/it/costs.md): Traccia l'utilizzo dei token, imposta i limiti di spesa del team e riduci i costi di Claude Code con la gestione del contesto, la selezione del modello, le impostazioni del pensiero esteso e gli hook di pre-elaborazione.
- [Traccia l'utilizzo del team con l'analittica](https://code.claude.com/docs/it/analytics.md): Visualizza le metriche di utilizzo di Claude Code, traccia l'adozione e misura la velocità di ingegneria nel dashboard di analittica.

#### Distribuzione dei plugin

- [Creare e distribuire un marketplace di plugin](https://code.claude.com/docs/it/plugin-marketplaces.md): Crea e ospita marketplace di plugin per distribuire estensioni Claude Code tra team e comunità.
- [Vincola le versioni delle dipendenze dei plugin](https://code.claude.com/docs/it/plugin-dependencies.md): Dichiara vincoli di versione sulle dipendenze dei plugin e raggruppa un set di plugin curato dietro un'unica installazione.
- [Consiglia il tuo plugin dalla tua CLI](https://code.claude.com/docs/it/plugin-hints.md): Emetti un marcatore su una riga dalla tua CLI in modo che Claude Code chieda agli utenti di installare il tuo plugin ufficiale.
- [Consigliare plugin per la vostra organizzazione](https://code.claude.com/docs/it/plugin-relevance.md): Aggiungere un blocco di rilevanza alle voci dei plugin del marketplace in modo che Claude Code li suggerisca quando il lavoro di un utente corrisponde.

#### Sicurezza e dati

- [Sicurezza](https://code.claude.com/docs/it/security.md): Scopri le misure di sicurezza di Claude Code e le migliori pratiche per un utilizzo sicuro.
- [Utilizzo dei dati](https://code.claude.com/docs/it/data-usage.md): Scopri le politiche di utilizzo dei dati di Anthropic per Claude
- [Zero data retention](https://code.claude.com/docs/it/zero-data-retention.md): Scopri Zero Data Retention (ZDR) per Claude Code, disponibile per account qualificati su Claude for Enterprise, inclusi ambito, funzionalità disabilitate e come richiedere l'abilitazione.

#### Adozione

- [Kit di comunicazione](https://code.claude.com/docs/it/communications-kit.md): Annunci di lancio, messaggi di campagna a goccia e risposte FAQ per il rollout di Claude Code nella vostra organizzazione di ingegneria.
- [Champion kit](https://code.claude.com/docs/it/champion-kit.md): Una guida pratica per gli ingegneri che promuovono Claude Code internamente: cosa condividere, come rispondere alle domande e come aumentare l'adozione nel tuo team.

### Configurazione

#### Impostazioni

- [File di impostazioni e precedenza](https://code.claude.com/docs/it/settings.md): Modifica le impostazioni di Claude Code, scegli l'ambito a cui appartiene una chiave, verifica la modifica e scopri quale valore Claude Code utilizza quando una chiave è impostata in più posizioni.
- [Tutte le impostazioni](https://code.claude.com/docs/it/settings-reference.md): Riferimento completo per ogni chiave settings.json di Claude Code: dove va ciascuna, il suo tipo e valore predefinito, e un esempio pronto da incollare, con un indice di ogni chiave.
- [File di impostazioni di esempio](https://code.claude.com/docs/it/settings-example.md): File settings.json realistici per uno sviluppatore, un team e un'organizzazione: copia uno, mantieni le chiavi che desideri e modifica i valori.

#### Autorizzazioni e sandboxing

- [Configurare le autorizzazioni](https://code.claude.com/docs/it/permissions.md): Controlla cosa Claude Code può accedere e fare con regole di autorizzazione granulari, modalità e criteri gestiti.
- [Scegli una modalità di autorizzazione](https://code.claude.com/docs/it/permission-modes.md): Controlla se Claude chiede prima di agire. Cambia le modalità di autorizzazione con Shift+Tab nella CLI, l'indicatore di modalità in VS Code, o il selettore di modalità in Desktop.
- [Configura lo strumento Bash in sandbox](https://code.claude.com/docs/it/sandboxing.md): Scopri come lo strumento Bash in sandbox di Claude Code fornisce isolamento del filesystem e della rete per un'esecuzione dell'agente più sicura e autonoma.
- [Scegliere un ambiente sandbox](https://code.claude.com/docs/it/sandbox-environments.md): Confronta le opzioni di sandbox di Claude Code: lo strumento Bash sandboxed integrato, il runtime sandbox, i dev container, Docker e le VM. Scegli l'isolamento giusto per il tuo modello di minaccia.

#### Ambienti

- [Configurare ambienti cloud](https://code.claude.com/docs/it/cloud-environments.md): Configurare ambienti cloud per le sessioni cloud di Claude Code: livelli di accesso di rete, variabili di ambiente, script di configurazione e caching dell'ambiente.

##### Ambienti self-hosted

- [Ambienti self-hosted](https://code.claude.com/docs/it/self-hosted-environments.md): Esegui sessioni cloud di Claude Code su infrastrutture che controlli: configura un ambiente self-hosted, distribuisci runner e instrada le sessioni al tuo calcolo.
- [Guida rapida agli ambienti self-hosted](https://code.claude.com/docs/it/self-hosted-environments-quickstart.md): Configura il tuo primo ambiente self-hosted: installa Claude Code, crea l'ambiente, avvia un runner e indirizza una sessione ad esso.
- [Distribuisci ambienti self-hosted in produzione](https://code.claude.com/docs/it/self-hosted-environments-deploy.md): Esegui runner self-hosted in produzione: hardening della sicurezza, controllo dell'egress di rete, credenziali git, ricette Kubernetes e Compose, e risoluzione dei problemi.
- [Personalizzare le sessioni negli ambienti self-hosted](https://code.claude.com/docs/it/self-hosted-environments-configuration.md): Personalizzare le sessioni degli ambienti self-hosted con script wrapper per credenziali per sessione, hook del ciclo di vita e spawning di runner su richiesta.
- [Testare gli ambienti self-hosted end to end](https://code.claude.com/docs/it/self-hosted-environments-testing.md): Verificare un'immagine di runner self-hosted da CI: inviare una sessione con la CLI, leggere le risposte di Claude attraverso un hook Stop e scrivere lo script del ciclo completo.
- [Riferimento per ambienti self-hosted](https://code.claude.com/docs/it/self-hosted-environments-reference.md): Riferimento completo per il runner self-hosted e l'orchestrator: flag CLI, variabili d'ambiente e metriche Prometheus.
- [Verificare l'identità della sessione negli ambienti self-hosted](https://code.claude.com/docs/it/self-hosted-environments-identity.md): Verificare il JWT CLAUDE_CODE_SESSION_ACCESS_TOKEN in modo che i servizi sulla vostra rete possano fidarsi delle richieste provenienti da sessioni nel vostro ambiente self-hosted.

#### Modello e risposte

- [Configurazione del modello](https://code.claude.com/docs/it/model-config.md): Configurare quale modello Claude Code utilizza, livelli di impegno, contesto esteso e la finestra di auto-compattazione
- [Accelera le risposte con la modalità veloce](https://code.claude.com/docs/it/fast-mode.md): Ottieni risposte più veloci di Opus in Claude Code attivando la modalità veloce.
- [Escalate hard decisions with the advisor tool](https://code.claude.com/docs/it/advisor.md): Abbina il tuo modello principale con un modello advisor più potente che Claude consulta nei momenti chiave durante un'attività.
- [Output styles](https://code.claude.com/docs/it/output-styles.md): Adattare Claude Code per usi oltre l'ingegneria del software

#### Interfaccia

- [Configura il tuo terminale per Claude Code](https://code.claude.com/docs/it/terminal-config.md): Correggi Shift+Invio per le nuove righe, ricevi un segnale acustico del terminale quando Claude termina, configura tmux, abbina il tema dei colori e abilita la modalità Vim nella CLI di Claude Code.
- [Rendering a schermo intero](https://code.claude.com/docs/it/fullscreen.md): Abilita una modalità di rendering più fluida e senza sfarfallio con supporto del mouse e utilizzo stabile della memoria nelle conversazioni lunghe.
- [Usa Claude Code con un lettore di schermo](https://code.claude.com/docs/it/accessibility.md): Configura Claude Code per lettori di schermo come VoiceOver e NVDA, oltre alle impostazioni per ingranditori dello schermo, movimento ridotto e temi adatti ai daltonici.
- [Dettatura vocale](https://code.claude.com/docs/it/voice-dictation.md): Pronuncia i tuoi prompt nella CLI di Claude Code con dettatura vocale a pressione prolungata o a tocco.
- [Personalizza la tua barra di stato](https://code.claude.com/docs/it/statusline.md): Configura una barra di stato personalizzata per monitorare l'utilizzo della finestra di contesto, i costi e lo stato git in Claude Code
- [Personalizzare le scorciatoie da tastiera](https://code.claude.com/docs/it/keybindings.md): Personalizzare le scorciatoie da tastiera in Claude Code con un file di configurazione keybindings.

### Riferimento

#### Riferimento

- [Riferimento CLI](https://code.claude.com/docs/it/cli-reference.md): Riferimento completo per l'interfaccia da riga di comando di Claude Code, inclusi comandi e flag.
- [Commands](https://code.claude.com/docs/it/commands.md): Riferimento completo per i comandi disponibili in Claude Code, inclusi i comandi integrati e le skills in bundle.
- [Variabili d'ambiente](https://code.claude.com/docs/it/env-vars.md): Riferimento per le variabili d'ambiente che controllano il comportamento di Claude Code.
- [Riferimento degli strumenti](https://code.claude.com/docs/it/tools-reference.md): Riferimento completo per gli strumenti che Claude Code può utilizzare, inclusi i requisiti di autorizzazione e il comportamento per strumento.
- [Modalità interattiva](https://code.claude.com/docs/it/interactive-mode.md): Riferimento completo per le scorciatoie da tastiera, le modalità di input e le funzioni interattive nelle sessioni di Claude Code.
- [Checkpointing](https://code.claude.com/docs/it/checkpointing.md): Traccia, riavvolgi e riassumi le modifiche e la conversazione di Claude per gestire lo stato della sessione.
- [Riferimento dei hooks](https://code.claude.com/docs/it/hooks.md): Riferimento per gli eventi dei hook di Claude Code, schema di configurazione, formati JSON di input/output, codici di uscita, hook asincroni, hook HTTP, hook di prompt e hook degli strumenti MCP.
- [Plugins reference](https://code.claude.com/docs/it/plugins-reference.md): Riferimento tecnico completo per il sistema di plugin di Claude Code, inclusi schemi, comandi CLI e specifiche dei componenti.
- [Riferimento dei canali](https://code.claude.com/docs/it/channels-reference.md): Crea un server MCP che invia webhook, avvisi e messaggi di chat in una sessione di Claude Code. Riferimento per il contratto del canale: dichiarazione di capacità, eventi di notifica, strumenti di risposta, gating del mittente e inoltro delle autorizzazioni.

#### Glossario

- [Glossario](https://code.claude.com/docs/it/glossary.md): Definizioni della terminologia di Claude Code. Scopri cosa significano agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP e altri concetti fondamentali.

### Agent SDK

#### Agent SDK

- [Panoramica dell'Agent SDK](https://code.claude.com/docs/it/agent-sdk/overview.md): Costruisci agenti AI di produzione con Claude Code come libreria
- [Guida rapida](https://code.claude.com/docs/it/agent-sdk/quickstart.md): Inizia con l'Agent SDK per Python o TypeScript per creare agenti AI che funzionano autonomamente
- [Migrazione a Claude Agent SDK](https://code.claude.com/docs/it/agent-sdk/migration-guide.md): Guida per la migrazione dei Claude Code SDK TypeScript e Python a Claude Agent SDK
- [Risolvere i problemi dell'Agent SDK](https://code.claude.com/docs/it/agent-sdk/troubleshooting.md): Correggi gli errori dell'Agent SDK in base al messaggio esatto che vedi, con la causa e la soluzione per ogni errore negli SDK TypeScript e Python.

#### Creare agenti

- [Configura il tuo agente](https://code.claude.com/docs/it/agent-sdk/configuration.md): Configura le sessioni dell'Agent SDK: componi l'oggetto options, imposta il modello, l'ambiente e i limiti, e trova la pagina di ogni opzione di funzionalità.
- [Esempi](https://code.claude.com/docs/it/agent-sdk/examples.md): Trova un progetto Agent SDK completo e eseguibile o una ricetta guidata nel Claude Cookbook che corrisponda a ciò che desideri costruire.

#### Concetti fondamentali

- [Come funziona il ciclo dell'agente](https://code.claude.com/docs/it/agent-sdk/agent-loop.md): Comprendere il ciclo di vita dei messaggi, l'esecuzione degli strumenti, la finestra di contesto e l'architettura che alimentano gli agenti SDK.
- [Usa le funzionalità di Claude Code nell'SDK](https://code.claude.com/docs/it/agent-sdk/claude-code-features.md): Carica le istruzioni del progetto, le skills, gli hooks e altre funzionalità di Claude Code nei tuoi agenti SDK.
- [Lavorare con le sessioni](https://code.claude.com/docs/it/agent-sdk/sessions.md): Come le sessioni mantengono la cronologia della conversazione dell'agente, e quando utilizzare continue, resume e fork per tornare a un'esecuzione precedente.
- [Persistere le sessioni nell'archiviazione esterna](https://code.claude.com/docs/it/agent-sdk/session-storage.md): Eseguire il mirroring dei trascritti di sessione Agent SDK nel vostro object store, key-value store o database in modo che altri host possano riprendere le vostre sessioni.

#### Input e output

- [Streaming Input](https://code.claude.com/docs/it/agent-sdk/streaming-vs-single-mode.md): Comprensione delle due modalità di input per Claude Agent SDK e quando utilizzare ciascuna
- [Gestire approvazioni e input dell'utente](https://code.claude.com/docs/it/agent-sdk/user-input.md): Presenta le richieste di approvazione e le domande di chiarimento di Claude agli utenti, quindi restituisci le loro decisioni all'SDK.
- [Trasmettere risposte in tempo reale](https://code.claude.com/docs/it/agent-sdk/streaming-output.md): Ricevere risposte in tempo reale dall'Agent SDK mentre il testo e le chiamate di strumenti vengono trasmessi
- [Ottenere output strutturati dagli agenti](https://code.claude.com/docs/it/agent-sdk/structured-outputs.md): Restituire JSON convalidato dai flussi di lavoro degli agenti utilizzando JSON Schema, Zod o Pydantic. Ottenere dati strutturati e type-safe dopo l'uso di strumenti multi-turno.

#### Estendi con strumenti

- [Fornisci a Claude strumenti personalizzati](https://code.claude.com/docs/it/agent-sdk/custom-tools.md): Definisci strumenti personalizzati con il server MCP in-process dell'Agent SDK di Claude in modo che Claude possa chiamare le tue funzioni, accedere alle tue API ed eseguire operazioni specifiche del dominio.
- [Connettiti a strumenti esterni con MCP](https://code.claude.com/docs/it/agent-sdk/mcp.md): Configura i server MCP per estendere il tuo agente con strumenti esterni. Copre i tipi di trasporto, la ricerca di strumenti per set di strumenti di grandi dimensioni, l'autenticazione e la gestione degli errori.
- [Scalare a molti strumenti con la ricerca di strumenti](https://code.claude.com/docs/it/agent-sdk/tool-search.md): Scalare il vostro agente a migliaia di strumenti scoprendo e caricando solo ciò che è necessario, su richiesta.
- [Subagents nell'SDK](https://code.claude.com/docs/it/agent-sdk/subagents.md): Definisci e richiama subagenti per isolare il contesto, eseguire attività in parallelo e applicare istruzioni specializzate nelle tue applicazioni Claude Agent SDK.

#### Personalizza il comportamento

- [Modifica dei system prompt](https://code.claude.com/docs/it/agent-sdk/modifying-system-prompts.md): Scegli tra il preset `claude_code` e un system prompt personalizzato, e personalizza il comportamento con CLAUDE.md, stili di output, append, o un prompt completamente personalizzato.
- [Estendi gli agenti con skills](https://code.claude.com/docs/it/agent-sdk/skills.md): Controlla quali skills Claude può invocare nelle sessioni dell'Agent SDK, invia comandi per nome e crea skills che le tue sessioni scoprono
- [Plugin nell'SDK](https://code.claude.com/docs/it/agent-sdk/plugins.md): Carica plugin personalizzati per estendere Claude Code con skills, agenti, hooks e server MCP tramite l'Agent SDK

#### Controllo e osservabilità

- [Configurare i permessi](https://code.claude.com/docs/it/agent-sdk/permissions.md): Controlla come il tuo agente utilizza gli strumenti con modalità di permesso, hook e regole dichiarative di consentimento/negazione.
- [Intercettare e controllare il comportamento dell'agente con hooks](https://code.claude.com/docs/it/agent-sdk/hooks.md): Intercettare e personalizzare il comportamento dell'agente nei punti chiave di esecuzione con hooks
- [Ripristina le modifiche ai file con checkpointing](https://code.claude.com/docs/it/agent-sdk/file-checkpointing.md): Traccia le modifiche ai file durante le sessioni dell'agente e ripristina i file a qualsiasi stato precedente
- [Tracciare costi e utilizzo](https://code.claude.com/docs/it/agent-sdk/cost-tracking.md): Scopri come tracciare l'utilizzo dei token, stimare i costi e configurare la memorizzazione nella cache dei prompt con Claude Agent SDK.
- [Osservabilità con OpenTelemetry](https://code.claude.com/docs/it/agent-sdk/observability.md): Esporta tracce, metriche ed eventi dall'Agent SDK al tuo backend di osservabilità utilizzando OpenTelemetry.
- [Traccia todo](https://code.claude.com/docs/it/agent-sdk/todo-tracking.md): Traccia i todo nelle sessioni di Agent SDK e visualizza i progressi di Claude nella tua applicazione da chiamate di strumenti strutturate

#### Distribuzione

- [Hosting dell'Agent SDK](https://code.claude.com/docs/it/agent-sdk/hosting.md): Distribuisci l'Agent SDK in produzione: architettura subprocess, persistenza della sessione, scalabilità, osservabilità e isolamento multi-tenant per Docker, Kubernetes e provider sandbox.
- [Distribuzione sicura di agenti AI](https://code.claude.com/docs/it/agent-sdk/secure-deployment.md): Una guida per proteggere le distribuzioni di Claude Code e Agent SDK con isolamento, gestione delle credenziali e controlli di rete

#### Riferimenti SDK

- [Riferimento Agent SDK - TypeScript](https://code.claude.com/docs/it/agent-sdk/typescript.md): Riferimento API completo per l'Agent SDK TypeScript, incluse tutte le funzioni, i tipi e le interfacce.
- [API sessione TypeScript SDK V2 (rimosso)](https://code.claude.com/docs/it/agent-sdk/typescript-v2-preview.md): Riferimento per l'API sessione rimosso V2 TypeScript Agent SDK, con pattern send/stream basati su sessione per conversazioni multi-turno.
- [Riferimento SDK Agent - Python](https://code.claude.com/docs/it/agent-sdk/python.md): Riferimento API completo per Python Agent SDK, incluse tutte le funzioni, i tipi e le classi.

### Novità

#### Novità

- [Novità](https://code.claude.com/docs/it/whats-new/index.md): Un digest settimanale delle notevoli funzionalità di Claude Code, con frammenti di codice, demo e contesto su perché sono importanti.
- [Settimana 37 · 7–11 settembre 2026](https://code.claude.com/docs/it/whats-new/2026-w37.md): Testate i vostri plugin con claude plugin eval e staccate i riquadri di Claude Code Desktop in finestre separate.
- [Settimana 36 · 31 agosto – 4 settembre 2026](https://code.claude.com/docs/it/whats-new/2026-w36.md): Passa a Claude Fable 5.1, lascia che l'uso del computer funzioni in background su Desktop e guarda gli editing di Claude in un pannello /diff dal vivo.
- [Settimana 35 · 24–28 agosto 2026](https://code.claude.com/docs/it/whats-new/2026-w35.md): Riprendere le sessioni di terminale nell'app Claude Code Desktop, esaminare i rapporti di feedback che Claude redige per voi e avviare una sessione in modalità limitata.
- [Settimana 34 · 17–21 agosto 2026](https://code.claude.com/docs/it/whats-new/2026-w34.md): Crea artboard UI modificabili con la skill /design, imposta lo stile di output Concise e avvia una sessione Claude Code sulla tua macchina dal tuo telefono.
- [Settimana 33 · 10–14 agosto 2026](https://code.claude.com/docs/it/whats-new/2026-w33.md): Claude Code Desktop continua automaticamente dopo il ripristino di un limite di utilizzo, la modalità fork è attivata per impostazione predefinita e le richieste di merge GitLab e i marketplace si uniscono a GitHub.
- [Settimana 32 · 3–7 agosto 2026](https://code.claude.com/docs/it/whats-new/2026-w32.md): Le sessioni di Claude Code si messaggiano tra loro, gli ambienti self-hosted eseguono sessioni cloud sulla vostra infrastruttura, e la modalità auto diventa la modalità di autorizzazione predefinita.
- [Settimana 30 · 20–24 luglio 2026](https://code.claude.com/docs/it/whats-new/2026-w30.md): Opus 5 diventa il modello Opus predefinito, Claude Code Desktop aggiunge un riquadro iOS Simulator, e il plugin Claude Security esegue la scansione del codice per individuare vulnerabilità.
- [Settimana 29 · 13–17 luglio 2026](https://code.claude.com/docs/it/whats-new/2026-w29.md): Estrai dati live negli artifact pubblicati tramite connettori MCP e utilizza Claude Code con un lettore di schermo nella nuova modalità screen reader.
- [Settimana 28 · 6–10 luglio 2026](https://code.claude.com/docs/it/whats-new/2026-w28.md): Sfoglia siti esterni dal browser integrato dell'app Desktop, esegui un controllo completo della configurazione con /doctor e scopri le protezioni dei transcript in modalità automatica e gli aggiornamenti della visualizzazione degli agenti.
- [Settimana 27 · 29 giugno – 3 luglio 2026](https://code.claude.com/docs/it/whats-new/2026-w27.md): Claude Sonnet 5 diventa il modello predefinito, Claude in Chrome raggiunge la disponibilità generale, i subagent vengono eseguiti in background per impostazione predefinita, Claude Desktop arriva su Linux in versione beta, e /radio si sintonizza su Claude FM.
- [Settimana 26 · 22–26 giugno 2026](https://code.claude.com/docs/it/whats-new/2026-w26.md): Autenticate i server MCP dalla shell con claude mcp login, ottenete una risposta all'output del comando della modalità shell con il prefisso !, e riprendete una conversazione da prima di /clear con /rewind.
- [Settimana 25 · 15–19 giugno 2026](https://code.claude.com/docs/it/whats-new/2026-w25.md): Pubblica una pagina live e condivisibile dalla tua sessione con Artifacts, abbina i parametri degli strumenti nelle regole di negazione e richiesta, e imposta qualsiasi impostazione dal prompt con /config.
- [Settimana 24 · 8–12 giugno 2026](https://code.claude.com/docs/it/whats-new/2026-w24.md): Sposta una sessione in una nuova directory con /cd, consenti ai sub-agent di generare i propri sub-agent e risolvi i problemi di una configurazione non funzionante con la modalità sicura.
- [Settimana 23 · 1–5 giugno 2026](https://code.claude.com/docs/it/whats-new/2026-w23.md): Esegui la modalità auto su Amazon Bedrock, Google Cloud's Agent Platform e Microsoft Foundry, richiedi conferma prima di scrivere file che possono eseguire codice in modalità acceptEdits, elenca i plugin installati con /plugin list e richiedi un intervallo di versione approvato per le distribuzioni…
- [Settimana 22 · 25–29 maggio 2026](https://code.claude.com/docs/it/whats-new/2026-w22.md): Esegui Claude Code su Claude Opus 4.8, orchestrate attività di grandi dimensioni con flussi di lavoro dinamici, rileva i problemi di sicurezza con il plugin security-guidance e utilizza la modalità veloce su Opus 4.8 a un prezzo inferiore.
- [Settimana 21 · 18–22 maggio 2026](https://code.claude.com/docs/it/whats-new/2026-w21.md): Utilizza la modalità auto nel piano Pro e con Sonnet 4.6, visualizza quali skills, subagents e server MCP determinano i limiti del vostro piano in /usage, e rivedi i diff con il nuovo comando /code-review.
- [Settimana 20 · 11–15 maggio 2026](https://code.claude.com/docs/it/whats-new/2026-w20.md): Gestisci ogni sessione di Claude Code da una sola schermata con la visualizzazione agente, mantieni Claude al lavoro verso un obiettivo finché non si verifica una condizione, ed esegui la modalità veloce su Opus 4.7 per impostazione predefinita.
- [Settimana 19 · 4–8 maggio 2026](https://code.claude.com/docs/it/whats-new/2026-w19.md): Carica i plugin da archivi .zip e URL, cerca la cronologia dei comandi in tutti i progetti con Ctrl+R, crea nuovi worktrees dal HEAD locale o dal ramo predefinito remoto, e blocca le azioni in modo incondizionato con le regole di hard deny in modalità auto.
- [Settimana 18 · 27 aprile – 1 maggio 2026](https://code.claude.com/docs/it/whats-new/2026-w18.md): Claude Code su Windows funziona senza Git Bash, claude auth login accetta un codice OAuth incollato quando il callback del browser non può raggiungere localhost, claude project purge pulisce lo stato locale per progetto, e incollare un URL di PR in /resume trova la sessione che l'ha creata.
- [Settimana 17 · 20–24 aprile 2026](https://code.claude.com/docs/it/whats-new/2026-w17.md): /ultrareview si apre come anteprima di ricerca, riepiloghi automatici della sessione quando tornate a un terminale, temi di colore personalizzati che potete creare e distribuire nei plugin, e un Claude Code riprogettato sul web.
- [Settimana 16 · 13–17 aprile 2026](https://code.claude.com/docs/it/whats-new/2026-w16.md): Claude Opus 4.7 con il nuovo livello di sforzo xhigh, Routines su Claude Code sul web, notifiche push mobili che avvisano il vostro telefono quando Claude ha bisogno di voi, un breakdown di /usage che mostra cosa sta guidando i vostri limiti, e binari nativi che sostituiscono il JavaScript raggruppa…
- [Settimana 15 · 6–10 aprile 2026](https://code.claude.com/docs/it/whats-new/2026-w15.md): Pianificazione cloud Ultraplan, lo strumento Monitor con /loop auto-paced, /team-onboarding per confezionare la vostra configurazione, e /autofix-pr dal vostro terminale.
- [Settimana 14 · 30 marzo – 3 aprile 2026](https://code.claude.com/docs/it/whats-new/2026-w14.md): Computer use nella CLI, lezioni interattive nel prodotto, rendering senza sfarfallio, override della dimensione dei risultati MCP per strumento e eseguibili plugin su PATH.
- [Settimana 13 · 23–27 marzo 2026](https://code.claude.com/docs/it/whats-new/2026-w13.md): Modalità auto per permessi senza intervento, computer use integrato, auto-fix PR nel cloud, ricerca trascrizioni e uno strumento PowerShell per Windows.

### Risorse

#### Risorse

- [Aspetti legali e conformità](https://code.claude.com/docs/it/legal-and-compliance.md): Accordi legali, certificazioni di conformità e informazioni sulla sicurezza per Claude Code.

---

## Claude Code Docs: Japanese

- 官方原文：https://code.claude.com/docs/_llms/jp.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-jp.md`

# Claude Code Docs: Japanese

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Japanese

### はじめに

#### はじめに

- [概要](https://code.claude.com/docs/ja/overview.md): Claude Code は agentic coding ツールで、コードベースを読み取り、ファイルを編集し、コマンドを実行し、開発ツールと統合します。ターミナル、IDE、デスクトップアプリ、ブラウザで利用できます。
- [クイックスタート](https://code.claude.com/docs/ja/quickstart.md): Claude Code へようこそ！
- [変更履歴](https://code.claude.com/docs/ja/changelog.md)

#### コアコンセプト

- [Claude Code の仕組み](https://code.claude.com/docs/ja/how-claude-code-works.md): agentic ループ、組み込みツール、Claude Code がプロジェクトとどのように相互作用するかを理解します。
- [Claude Code を拡張する](https://code.claude.com/docs/ja/features-overview.md): CLAUDE.md、Skills、subagents、hooks、MCP、plugins をいつ使用するかを理解します。
- [.claude ディレクトリを探索する](https://code.claude.com/docs/ja/claude-directory.md): Claude Code が CLAUDE.md、settings.json、hooks、skills、commands、subagents、workflows、rules、auto memory を読み込む場所。プロジェクト内の .claude ディレクトリとホームディレクトリの ~/.claude を探索します。
- [コンテキストウィンドウを探索する](https://code.claude.com/docs/ja/context-window.md): Claude Code のコンテキストウィンドウがセッション中にどのように満たされるかのインタラクティブなシミュレーション。自動的に読み込まれるもの、各ファイル読み込みのコスト、ルールとフックが発火するタイミングを確認できます。
- [Claude Code がプロンプトキャッシングを使用する方法](https://code.claude.com/docs/ja/prompt-caching.md): Claude Code はプロンプトキャッシングを自動的に管理します。モデル切り替えがキャッシュなしの遅いターンをトリガーする理由、`/compact` のコスト、CLAUDE.md の編集がセッション中に適用されない理由、キャッシュヒット率を確認する方法を確認してください。

#### Claude Code を使用する

- [Claude があなたのプロジェクトを記憶する方法](https://code.claude.com/docs/ja/memory.md): CLAUDE.md ファイルで Claude に永続的な指示を与え、自動メモリで Claude が自動的に学習を蓄積できるようにします。
- [セッションの管理](https://code.claude.com/docs/ja/sessions.md): Claude Code の会話に名前を付け、再開し、分岐し、切り替えます。`--continue`、`--resume`、`--from-pr`、`/resume` ピッカー、セッション命名、トランスクリプトのエクスポート、およびトランスクリプトの保存場所について説明します。
- [一般的なワークフロー](https://code.claude.com/docs/ja/common-workflows.md): Claude Code を使用してコードベースの探索、バグ修正、リファクタリング、テスト、その他の日常的なタスクを実行するためのステップバイステップガイド。
- [プロンプトライブラリ](https://code.claude.com/docs/ja/prompt-library.md): Claude Code 用のコピー＆ペーストプロンプト。タスクと役割でタグ付けされています。
- [Claude Code のベストプラクティス](https://code.claude.com/docs/ja/best-practices.md): 環境設定から並列セッションでのスケーリングまで、Claude Code を最大限に活用するためのヒントとパターン。

#### プラットフォームと統合

- [プラットフォームと統合](https://code.claude.com/docs/ja/platforms.md): Claude Code を実行する場所を選択し、何に接続するかを決定します。CLI、Desktop、VS Code、JetBrains、Web、モバイル、および Chrome、Slack、CI/CD などの統合を比較します。
- [任意のデバイスからローカルセッションを続行する Remote Control](https://code.claude.com/docs/ja/remote-control.md): Remote Control を使用して、電話、タブレット、または任意のブラウザから Claude Code のローカルセッションを続行します。claude.ai/code と Claude モバイルアプリで動作します。
- [Claude がプロジェクトで進行中の作業を調整する](https://code.claude.com/docs/ja/claude-projects.md): 関連する作業の本体を 1 つの会話で Claude に提供し、リポジトリ、指示、メモリを共有する並列クラウドセッションを調整させます。
- [モバイルの Claude Code](https://code.claude.com/docs/ja/mobile.md): Claude アプリ for iOS と Android を使用して、携帯電話から Claude Code タスクを開始、監視、操作します。
- [Chrome で Claude Code を使用する](https://code.claude.com/docs/ja/chrome.md): Claude Code を Chrome ブラウザに接続して、Web アプリをテストし、コンソールログでデバッグし、フォーム入力を自動化し、Web ページからデータを抽出します。
- [Claude に CLI からコンピュータを使用させる](https://code.claude.com/docs/ja/computer-use.md): Claude Code CLI でコンピュータ使用を有効にして、Claude がアプリを開いたり、クリックしたり、入力したり、macOS でスクリーンを表示したりできるようにします。ネイティブアプリをテストし、ビジュアルの問題をデバッグし、ターミナルを離れることなく GUI のみのツールを自動化します。
- [VS Code で Claude Code を使用する](https://code.claude.com/docs/ja/vs-code.md): Claude Code 拡張機能を VS Code にインストールして設定します。インラインの差分表示、@-メンション、プラン確認、キーボードショートカットを使用した AI コーディング支援を取得します。
- [JetBrains IDEs](https://code.claude.com/docs/ja/jetbrains.md): Claude Code を IntelliJ、PyCharm、WebStorm など JetBrains IDEs で使用する
- [Slack での Claude Code](https://code.claude.com/docs/ja/slack.md): Slack ワークスペースから直接コーディングタスクを委任する。Anthropic は Team および Enterprise ワークスペース向けにこの以前のバージョンを Claude Tag に置き換えています。Pro および Max プランではセットアップパスのままです。
- [Claude Tag](https://code.claude.com/docs/ja/claude-tag.md): Claude Tag を使用して Claude をチームの Slack チャネルに導入し、claude.com で設定と使用方法のドキュメントを確認できます。

##### クラウド内の Claude Code

- [Claude Code をクラウドで始める](https://code.claude.com/docs/ja/web-quickstart.md): ブラウザまたはスマートフォンからクラウドで Claude Code を実行します。GitHub リポジトリを接続し、タスクを送信し、ローカルセットアップなしで PR をレビューします。
- [クラウドで Claude Code を使用する](https://code.claude.com/docs/ja/claude-code-on-the-web.md): ブラウザ、携帯電話、デスクトップアプリ、またはターミナルからクラウドで Claude Code セッションを実行し、--cloud と --teleport で移動し、プルリクエストを自動修正します。
- [ルーティンで作業を自動化する](https://code.claude.com/docs/ja/routines.md): Claude Code を自動操縦に設定します。スケジュールで実行するルーティンを定義したり、API 呼び出しでトリガーしたり、Anthropic が管理するクラウドインフラストラクチャから GitHub イベントに反応させたりできます。
- [ultrareview でバグを見つける](https://code.claude.com/docs/ja/ultrareview.md): /code-review ultra でクラウド上で深い複数エージェント型のコードレビューを実行し、マージ前にバグを見つけて検証します。

##### Claude Code デスクトップ版

- [デスクトップアプリを始める](https://code.claude.com/docs/ja/desktop-quickstart.md): Claude Code をデスクトップにインストールして、最初のコーディングセッションを開始します
- [Desktop application](https://code.claude.com/docs/ja/desktop.md): Claude Code Desktop をさらに活用する：Git 分離による並列セッション、ドラッグアンドドロップペインレイアウト、統合ターミナルとファイルエディタ、サイドチャット、コンピュータ使用、電話から Dispatch セッションを送信、ビジュアル diff レビュー、アプリプレビュー、PR 監視、コネクタ、エンタープライズ設定。
- [Claude Desktop on Linux (beta)](https://code.claude.com/docs/ja/desktop-linux.md): Ubuntu と Debian に Claude デスクトップアプリをインストールおよび更新する
- [Claude Code Desktop in WSL](https://code.claude.com/docs/ja/desktop-wsl.md): WSL 2 ディストリビューション内で Code セッションを実行する
- [Claude Code Desktop でスケジュール設定されたタスクを実行する](https://code.claude.com/docs/ja/desktop-scheduled-tasks.md): Claude Code Desktop でスケジュール設定されたタスクを設定して、毎日のコードレビュー、依存関係の監査、または朝のブリーフィングなど、定期的に Claude を自動的に実行します。
- [iOS シミュレータでアプリをテストする](https://code.claude.com/docs/ja/desktop-ios-simulator.md): Claude Code Desktop は、Claude がアプリをビルド、実行、またはチェックするときに、iOS シミュレータペインでアプリを開きます。各セッションに対して個別のシミュレータが用意されます。

##### コードレビュー & CI/CD

- [Claude がコードを書く際のセキュリティ問題をキャッチする](https://code.claude.com/docs/ja/security-guidance.md): security-guidance プラグインをインストールして、Claude が自身のコード変更の脆弱性をレビューし、同じセッション内で修正するようにします。
- [コードベースの脆弱性をスキャンする](https://code.claude.com/docs/ja/claude-security.md): Claude Security プラグインをインストールして、Claude Code セッション内でコードベースの脆弱性をスキャンし、検出結果をレビューして適用できるパッチに変換します。
- [Code Review](https://code.claude.com/docs/ja/code-review.md): マルチエージェント分析を使用してコードベース全体を検査し、ロジックエラー、セキュリティ脆弱性、リグレッションを検出する自動化された PR レビューを設定します
- [Claude Code GitHub Actions](https://code.claude.com/docs/ja/github-actions.md): @claude メンションに応答し、タスクを自動化し、イシューをプルリクエストに変換するために GitHub Actions ワークフロー内で Claude Code を実行します
- [Claude Code GitHub Actions をクラウドプロバイダーで使用する](https://code.claude.com/docs/ja/github-actions-cloud-providers.md): Claude Code GitHub Actions を Claude API の代わりに Amazon Bedrock、Google Cloud の Agent Platform、または Microsoft Foundry を通じて実行する
- [Claude Code と GitHub Enterprise Server](https://code.claude.com/docs/ja/github-enterprise-server.md): Claude Code を自社ホストの GitHub Enterprise Server インスタンスに接続して、クラウドセッション、コードレビュー、プラグインマーケットプレイスを利用できます。
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/ja/gitlab-ci-cd.md): Claude Code を GitLab CI/CD で開発ワークフローに統合する方法を学びます

### Claude Code で構築する

#### エージェントと並列処理

- [エージェントを並列実行する](https://code.claude.com/docs/ja/agents.md): Claude Code が複数のタスクを同時に実行する 5 つの方法を比較します。サブエージェント、エージェントビュー、エージェントチーム、動的ワークフロー、およびプロジェクトについて説明します。
- [カスタムサブエージェントの作成](https://code.claude.com/docs/ja/sub-agents.md): Claude Code でタスク固有のワークフローと改善されたコンテキスト管理のための特化した AI サブエージェントを作成して使用します。
- [複数のエージェントをエージェントビューで管理する](https://code.claude.com/docs/ja/agent-view.md): 1 つの画面から多くの Claude Code セッションをディスパッチして管理します。エージェントビューは、すべてのセッションが何をしているか、どのセッションが入力を必要としているかを表示します。
- [Claude Code セッションのチームを調整する](https://code.claude.com/docs/ja/agent-teams.md): 複数の Claude Code インスタンスがチームとして連携して動作するように調整し、共有タスク、エージェント間メッセージング、および一元管理を実現します。
- [他の Claude Code セッションにメッセージを送信する](https://code.claude.com/docs/ja/cross-session-messaging.md): Claude が同じマシン上の他の Claude Code セッションをリストアップしてメッセージを送信できるようにし、他のマシンまたはクラウド上のセッションに到達します。
- [動的ワークフローで大規模にサブエージェントをオーケストレーションする](https://code.claude.com/docs/ja/workflows.md): 動的ワークフローは、Claude が作成したスクリプトから多くのサブエージェントをオーケストレーションし、再実行できます。コードベース監査、大規模マイグレーション、相互検証研究に使用します。
- [worktree を使用して並列セッションを実行する](https://code.claude.com/docs/ja/worktrees.md): 並列 Claude Code セッションを個別の git worktree に分離して、変更が衝突しないようにします。`--worktree` フラグ、subagent の分離、`.worktreeinclude`、クリーンアップ、および非 git VCS フックについて説明します。

#### Model Context Protocol（MCP）

- [MCP サーバーに接続する](https://code.claude.com/docs/ja/mcp-quickstart.md): MCP サーバーを Claude Code に追加し、接続を確認し、ディスク上の設定を見つけます。
- [MCP を使用して Claude Code をツールに接続する](https://code.claude.com/docs/ja/mcp.md): Model Context Protocol を使用して Claude Code をツールに接続する方法を学びます。

#### Skills

- [スキルで Claude を拡張する](https://code.claude.com/docs/ja/skills.md): Claude Code でスキルを作成、管理、共有して Claude の機能を拡張します。カスタムコマンドとバンドルされたスキルが含まれます。

#### プラグイン

- [マーケットプレイスから事前構築されたプラグインを発見してインストールする](https://code.claude.com/docs/ja/discover-plugins.md): マーケットプレイスからプラグインを検索してインストールし、Claude Code を新しいスキル、エージェント、機能で拡張します。
- [プラグインを作成する](https://code.claude.com/docs/ja/plugins.md): スキル、エージェント、フック、MCP サーバーで Claude Code を拡張するカスタムプラグインを作成します。
- [evals でプラグインをテストする](https://code.claude.com/docs/ja/plugin-evals.md): Claude Code プラグイン用の eval ケースを作成し、claude plugin eval で実行し、結果をグレード化し、プラグインなしのベースラインと比較し、CI でスコアをゲートする。

#### Artifacts

- [セッション出力をアーティファクトとして共有する](https://code.claude.com/docs/ja/artifacts.md): Artifacts は Claude Code の成果物を claude.ai 上のライブでインタラクティブなページに変え、プライベートに保つ、組織と共有する、または公開リンクで公開することができます。

#### オートメーション

- [hooks でアクションを自動化する](https://code.claude.com/docs/ja/hooks-guide.md): Claude Code がファイルを編集したり、タスクを完了したり、入力が必要になったりしたときに、シェルコマンドを自動的に実行します。コードをフォーマットし、通知を送信し、コマンドを検証し、プロジェクトルールを適用します。
- [チャネルを使用して実行中のセッションにイベントをプッシュする](https://code.claude.com/docs/ja/channels.md): チャネルを使用して、MCP サーバーから実行中の Claude Code セッションにメッセージ、アラート、ウェブフックをプッシュします。CI 結果、チャットメッセージ、監視イベントを転送して、あなたが不在の間に Claude が対応できるようにします。
- [スケジュールに従ってプロンプトを実行する](https://code.claude.com/docs/ja/scheduled-tasks.md): /loop と cron スケジューリングツールを使用して、Claude Code セッション内でプロンプトを繰り返し実行したり、ステータスをポーリングしたり、1 回限りのリマインダーを設定したりします。
- [Claude をゴールに向かって動作させ続ける](https://code.claude.com/docs/ja/goal.md): /goal でコンプリーション条件を設定すると、Claude はターン間でプロンプトなしに条件が満たされるまで動作し続けます。モデルが不可能と判断するか、修正が必要なエラーが発生するとゴールがクリアされます。
- [Claude Code をプログラムで実行する](https://code.claude.com/docs/ja/headless.md): Agent SDK を使用して、CLI、Python、または TypeScript からプログラムで Claude Code を実行します。
- [リンクからセッションを起動する](https://code.claude.com/docs/ja/deep-links.md): URL から Claude Code ターミナルセッションを開きます。ランブック、アラート、ダッシュボードに `claude-cli://` リンクを埋め込むと、クリックで Claude Code が正しいリポジトリで正しいプロンプトを使って開きます。

#### ガイド

- [モノレポまたは大規模コードベースで Claude Code をセットアップする](https://code.claude.com/docs/ja/large-codebases.md): ネストされた CLAUDE.md ファイル、スパースワークツリー、コード インテリジェンス、パッケージごとのスキルを使用して、モノレポと大規模シングルツリーコードベース向けに Claude Code を設定し、Claude が作業中のコードに焦点を当てるようにします。

#### トラブルシューティング

- [インストールとログインのトラブルシューティング](https://code.claude.com/docs/ja/troubleshoot-install.md): Claude Code のインストールまたはサインイン時に、コマンドが見つからない、PATH、権限、ネットワーク、認証エラーを修正します。
- [トラブルシューティング](https://code.claude.com/docs/ja/troubleshooting.md): Claude Code の高い CPU またはメモリ使用量、ハング、auto-compact スラッシング、検索の問題を修正し、その他の問題に対応する適切なページを見つけます。
- [設定をデバッグする](https://code.claude.com/docs/ja/debug-your-config.md): CLAUDE.md、設定、hooks、MCP サーバー、またはスキルが機能していない理由を診断します。/context、/doctor、/hooks、/mcp を使用して、実際に読み込まれた内容を確認します。
- [エラーリファレンス](https://code.claude.com/docs/ja/errors.md): Claude Code のランタイムエラーメッセージを検索し、各エラーの意味と修正方法を確認できます。

### 管理

#### セットアップとアクセス

- [組織向けに Claude Code をセットアップする](https://code.claude.com/docs/ja/admin-setup.md): Claude Code を展開する管理者向けの決定マップ。API プロバイダー、マネージド設定、ポリシー実行、使用状況監視、データ処理をカバーしています。
- [高度なセットアップ](https://code.claude.com/docs/ja/setup.md): Claude Code のシステム要件、プラットフォーム固有のインストール、バージョン管理、およびアンインストール。
- [認証](https://code.claude.com/docs/ja/authentication.md): Claude Code にログインし、個人、チーム、組織向けの認証を設定します。
- [マネージド設定をデプロイする](https://code.claude.com/docs/ja/managed-settings.md): すべての開発者のマシンにマネージド設定をデプロイします。OS ごとの配信メカニズム、Claude Code がマネージドソースを組み合わせる方法、および強制の検証方法について説明します。
- [サーバー管理設定を構成する](https://code.claude.com/docs/ja/server-managed-settings.md): デバイス管理インフラストラクチャを必要とせずに、サーバー配信設定を通じて組織全体で Claude Code を一元的に構成します。
- [組織の MCP サーバーアクセスを制御する](https://code.claude.com/docs/ja/managed-mcp.md): 管理対象設定ファイル、管理対象設定、許可リスト、拒否リストを使用して、ユーザーが追加または接続できる MCP サーバーを制限するか、すべてのユーザーにサーバーを提供します。
- [オートモードの設定](https://code.claude.com/docs/ja/auto-mode-config.md): オートモード分類器に、組織が信頼するリポジトリ、バケット、ドメインを指定します。環境コンテキストを設定し、デフォルトのブロックおよび許可ルールをオーバーライドし、オートモード CLI サブコマンドで有効な設定を検査します。

#### デプロイメント

- [エンタープライズデプロイメント概要](https://code.claude.com/docs/ja/third-party-integrations.md): Claude Code が様々なサードパーティサービスとインフラストラクチャと統合して、エンタープライズデプロイメント要件を満たす方法について学びます。
- [機能の利用可能性](https://code.claude.com/docs/ja/feature-availability.md): Anthropic のサブスクリプションプラン、Anthropic Console、Amazon Bedrock、Claude Platform on AWS、Google Cloud の Agent Platform、Microsoft Foundry 全体で利用可能な Claude Code 機能を比較します。
- [Amazon Bedrock 上の Claude Code](https://code.claude.com/docs/ja/amazon-bedrock.md): Amazon Bedrock を通じた Claude Code の設定方法（セットアップ、IAM 設定、トラブルシューティングを含む）について学習します。
- [AWS 上の Claude Platform での Claude Code](https://code.claude.com/docs/ja/claude-platform-on-aws.md): AWS 認証、IAM アクセス制御、AWS Marketplace 請求を使用して、Anthropic が運営する Claude API を使用するように Claude Code を設定します。
- [Google Cloud の Agent Platform 上の Claude Code](https://code.claude.com/docs/ja/google-vertex-ai.md): Google Cloud の Agent Platform（旧 Vertex AI）を通じた Claude Code の設定方法について学びます。セットアップ、IAM 設定、トラブルシューティングを含みます。
- [Claude Code on Microsoft Foundry](https://code.claude.com/docs/ja/microsoft-foundry.md): Microsoft Foundry を通じて Claude Code を構成する方法について学びます。セットアップ、構成、トラブルシューティングを含みます。
- [エンタープライズネットワーク設定](https://code.claude.com/docs/ja/network-config.md): プロキシサーバー、カスタム認証局（CA）、相互 Transport Layer Security（mTLS）認証を使用して、エンタープライズ環境向けに Claude Code を設定します。
- [企業ランチャーの背後で Claude Code を実行する](https://code.claude.com/docs/ja/corporate-launcher.md): CLAUDE_CODE_PROCESS_WRAPPER または processWrapper 設定を使用して、Claude Code がそのバイナリから起動するプロセス（バックグラウンドサービスとすべてのエージェントビューセッションを含む）を必須ランチャーを通じてルーティングします。
- [開発コンテナ](https://code.claude.com/docs/ja/devcontainer.md): チーム全体で一貫した分離環境を実現するため、開発コンテナ内で Claude Code を実行します。

#### ゲートウェイ

- [ゲートウェイを通じて Claude Code を実行する](https://code.claude.com/docs/ja/gateways.md): Claude Code を自社ホスト型ゲートウェイ経由でルーティングして、認証情報の一元管理、使用状況の追跡、コスト管理を実現します。アーキテクチャ、Anthropic の Claude apps ゲートウェイ、および他のゲートウェイ製品の使用方法について説明します。

##### Claude apps gateway

- [Amazon Bedrock、Claude Platform on AWS、Google Cloud、Microsoft Foundry 向け Claude アプリゲートウェイ](https://code.claude.com/docs/ja/claude-apps-gateway.md): SSO サインイン、グループごとのモデルアクセス、OTLP テレメトリを備えた自己ホスト型ゲートウェイを通じて、Amazon Bedrock、Claude Platform on AWS、Google Cloud、または Microsoft Foundry で Claude Code を実行します。
- [Claude apps gateway 設定](https://code.claude.com/docs/ja/claude-apps-gateway-config.md): gateway.yaml のすべてのオプションのリファレンス：リスナーと TLS、OIDC、セッション、Postgres ストア、Amazon Bedrock、Claude Platform on AWS、Google Cloud の Agent Platform、Microsoft Foundry アップストリーム、モデルルーティング、マネージドポリシー、テレメトリー。
- [Claude apps gateway の支出制限](https://code.claude.com/docs/ja/claude-apps-gateway-spend-limits.md): Claude apps gateway を通じて各開発者の支出を日単位、週単位、または月単位で制限します。Admin API で制限を設定すると、gateway はすべてのリクエストでそれらを実行します。
- [Claude apps gateway のデプロイと運用](https://code.claude.com/docs/ja/claude-apps-gateway-deploy.md): IdP にゲートウェイを登録し、コンテナをビルドして Kubernetes または Cloud Run にデプロイし、ヘルスチェック、シークレットローテーション、アップグレード、セキュリティを運用します。
- [AWS に Claude apps gateway をデプロイする](https://code.claude.com/docs/ja/claude-apps-gateway-on-aws.md): AWS で Claude apps gateway を実行する実装例：ECS Fargate または EKS、Amazon RDS for PostgreSQL、AWS Secrets Manager、および Amazon Bedrock への IAM ロール認証。
- [Google Cloud に Claude apps gateway をデプロイする](https://code.claude.com/docs/ja/claude-apps-gateway-on-gcp.md): Google Cloud で Claude apps gateway を実行する実装例：Cloud Run または GKE、Cloud SQL for PostgreSQL、Secret Manager、および Google Cloud の Agent Platform への service account 認証。

##### その他のゲートウェイ

- [その他の LLM gateway](https://code.claude.com/docs/ja/llm-gateway.md): 組織が既に実行している LLM gateway を通じて Claude Code をルーティングします。Claude Code をゲートウェイに接続する方法、組織向けのロールアウト、Claude Code がゲートウェイに送信する内容について説明します。
- [Claude Code を LLM ゲートウェイに接続する](https://code.claude.com/docs/ja/llm-gateway-connect.md): Claude Code を組織の LLM ゲートウェイに指定します。管理者がすでに設定しているかどうかを確認するか、基本 URL と認証情報を自分で設定してから、接続を確認し、ゲートウェイエラーを修正します。
- [組織向けの LLM ゲートウェイをロールアウトする](https://code.claude.com/docs/ja/llm-gateway-rollout.md): Claude Code 用のゲートウェイ製品をデプロイします。Claude Code が送信する内容を転送するように設定し、開発者認証情報を発行し、マネージド設定を通じて設定を配布し、ロールアウトを検証します。
- [Claude Code ゲートウェイ互換性ガイド](https://code.claude.com/docs/ja/llm-gateway-protocol.md): Claude Code と互換性のある LLM ゲートウェイを保つ：呼び出すエンドポイント、転送する必要があるヘッダーとボディフィールド、および削除されると機能しなくなるもの。

#### 使用状況とコスト

- [監視](https://code.claude.com/docs/ja/monitoring-usage.md): Claude Code の OpenTelemetry を有効にして設定する方法を学びます。
- [コストを効果的に管理する](https://code.claude.com/docs/ja/costs.md): トークン使用量を追跡し、チームの支出制限を設定し、コンテキスト管理、モデル選択、拡張思考設定、前処理フックを使用して Claude Code のコストを削減します。
- [チームの使用状況を分析で追跡する](https://code.claude.com/docs/ja/analytics.md): Claude Code の使用メトリクスを表示し、採用状況を追跡し、分析ダッシュボードでエンジニアリング速度を測定します。

#### Plugin 配布

- [プラグインマーケットプレイスの作成と配布](https://code.claude.com/docs/ja/plugin-marketplaces.md): Claude Code 拡張機能を配布するためのプラグインマーケットプレイスを構築およびホストします。
- [プラグイン依存関係のバージョンを制約する](https://code.claude.com/docs/ja/plugin-dependencies.md): プラグイン依存関係のバージョン制約を宣言して、キュレーションされたプラグインセットを 1 つのインストールの背後にバンドルします。
- [CLI からプラグインを推奨する](https://code.claude.com/docs/ja/plugin-hints.md): CLI から 1 行のマーカーを出力して、Claude Code ユーザーに公式プラグインのインストールを促します。
- [組織向けプラグインを推奨する](https://code.claude.com/docs/ja/plugin-relevance.md): マーケットプレイスプラグインエントリに関連性ブロックを追加して、ユーザーの作業が一致したときに Claude Code がそれらを提案するようにします。

#### セキュリティとデータ

- [セキュリティ](https://code.claude.com/docs/ja/security.md): Claude Code のセキュリティ対策とセキュアな使用方法のベストプラクティスについて学びます。
- [データ使用](https://code.claude.com/docs/ja/data-usage.md): Anthropic の Claude のデータ使用ポリシーについて学習します
- [ゼロデータ保持](https://code.claude.com/docs/ja/zero-data-retention.md): Claude for Enterprise での Claude Code のゼロデータ保持（ZDR）について、スコープ、無効化される機能、有効化のリクエスト方法を学びます。

#### 導入

- [コミュニケーションキット](https://code.claude.com/docs/ja/communications-kit.md): Claude Code をエンジニアリング組織全体にロールアウトするための、ローンチアナウンスメント、ドリップキャンペーンメッセージ、FAQ 回答。
- [チャンピオンキット](https://code.claude.com/docs/ja/champion-kit.md): Claude Code を社内で推進するエンジニア向けの実行計画：何を共有するか、質問にどう答えるか、チーム内での採用を拡大する方法。

### 設定

#### 設定

- [設定ファイルと優先順位](https://code.claude.com/docs/ja/settings.md): Claude Code の設定を変更し、キーが属するスコープを選択し、変更を確認し、複数の場所でキーが設定されている場合に Claude Code が使用する値を学びます。
- [すべての設定](https://code.claude.com/docs/ja/settings-reference.md): Claude Code の settings.json キーの完全なリファレンス：各キーの場所、型とデフォルト値、貼り付け可能な例、およびすべてのキーのインデックス。
- [設定ファイルの例](https://code.claude.com/docs/ja/settings-example.md): 開発者、チーム、組織向けの現実的な settings.json ファイル：1 つをコピーして、必要なキーを保持し、値を変更してください。

#### 権限とサンドボックス

- [権限を設定する](https://code.claude.com/docs/ja/permissions.md): きめ細かい権限ルール、モード、管理ポリシーを使用して、Claude Code がアクセスして実行できる内容を制御します。
- [権限モードを選択する](https://code.claude.com/docs/ja/permission-modes.md): Claude がアクションを実行する前に確認するかどうかを制御します。CLI で Shift+Tab でモードを切り替えるか、VS Code のモード指示器、Desktop のモードセレクター、または Web のモードドロップダウンを使用します。
- [サンドボックス化された Bash ツールを設定する](https://code.claude.com/docs/ja/sandboxing.md): Claude Code のサンドボックス化された Bash ツールがファイルシステムとネットワークの分離を提供し、より安全で自律的なエージェント実行を実現する方法について学びます。
- [サンドボックス環境を選択する](https://code.claude.com/docs/ja/sandbox-environments.md): Claude Code のサンドボックスオプションを比較します。組み込みのサンドボックス化された Bash ツール、サンドボックスランタイム、dev コンテナ、Docker、VM があります。脅威モデルに適した分離を選択してください。

#### 環境

- [クラウド環境を設定する](https://code.claude.com/docs/ja/cloud-environments.md): Claude Code クラウドセッション用のクラウド環境を設定します。ネットワークアクセスレベル、環境変数、セットアップスクリプト、環境キャッシュを構成できます。

##### セルフホスト環境

- [自己ホスト環境](https://code.claude.com/docs/ja/self-hosted-environments.md): 自分たちが管理するインフラストラクチャで Claude Code クラウドセッションを実行します。自己ホスト環境をセットアップし、ランナーをデプロイし、セッションを自分たちのコンピュートにルーティングします。
- [セルフホストされた環境のクイックスタート](https://code.claude.com/docs/ja/self-hosted-environments-quickstart.md): セルフホストされた環境を初めてセットアップします。Claude Code をインストールし、環境を作成し、ランナーを起動し、セッションをルーティングします。
- [本番環境へのセルフホスト環境のデプロイ](https://code.claude.com/docs/ja/self-hosted-environments-deploy.md): 本番環境でセルフホストランナーを実行する：セキュリティ強化、ネットワーク出力制御、git 認証情報、Kubernetes と Compose レシピ、トラブルシューティング。
- [セルフホストされた環境でセッションをカスタマイズする](https://code.claude.com/docs/ja/self-hosted-environments-configuration.md): ラッパースクリプト、ライフサイクルフック、オンデマンドランナースポーニングを使用して、セルフホストされた環境セッションをセッションごとの認証情報、ライフサイクルフック、オンデマンドランナースポーニングでカスタマイズします。
- [自己ホスト環境をエンドツーエンドでテストする](https://code.claude.com/docs/ja/self-hosted-environments-testing.md): CI から自己ホスト実行イメージを検証します。CLI でセッションをディスパッチし、Stop フックを通じて Claude の返信を読み取り、完全なループをスクリプト化します。
- [セルフホスト環境リファレンス](https://code.claude.com/docs/ja/self-hosted-environments-reference.md): セルフホストランナーとオーケストレーターの完全なリファレンス：CLI フラグ、環境変数、Prometheus メトリクス。
- [自己ホスト環境でセッション ID を検証する](https://code.claude.com/docs/ja/self-hosted-environments-identity.md): CLAUDE_CODE_SESSION_ACCESS_TOKEN JWT を検証して、自己ホスト環境内のセッションからのリクエストをネットワーク上のサービスが信頼できるようにします。

#### モデルと応答

- [モデル設定](https://code.claude.com/docs/ja/model-config.md): Claude Code のモデル設定について学習します。`opusplan` などのモデルエイリアスを含みます
- [高速モードでレスポンスを高速化](https://code.claude.com/docs/ja/fast-mode.md): Claude Code で高速モードを切り替えて、Opus のレスポンスを高速化します。
- [advisor ツールで難しい判断をエスカレートする](https://code.claude.com/docs/ja/advisor.md): メインモデルをより強力な advisor モデルと組み合わせて、タスク中の重要な瞬間に Claude が相談できるようにします。
- [出力スタイル](https://code.claude.com/docs/ja/output-styles.md): ソフトウェアエンジニアリング以外の用途に合わせて Claude Code を適応させる

#### インターフェース

- [Claude Code 用にターミナルを設定する](https://code.claude.com/docs/ja/terminal-config.md): Shift+Enter で改行を挿入する、Claude の処理完了時にターミナルベルを鳴らす、tmux を設定する、カラーテーマを合わせる、Claude Code CLI で Vim モードを有効にする方法を説明します。
- [フルスクリーンレンダリング](https://code.claude.com/docs/ja/fullscreen.md): マウスサポートと安定したメモリ使用量を備えた、より滑らかでちらつきのないレンダリングモードを有効にします。長い会話でも安定した動作を実現します。
- [スクリーンリーダーで Claude Code を使用する](https://code.claude.com/docs/ja/accessibility.md): VoiceOver や NVDA などのスクリーンリーダー、スクリーン拡大鏡、モーション削減、色覚異常対応テーマの設定で Claude Code をセットアップします。
- [音声ディクテーション](https://code.claude.com/docs/ja/voice-dictation.md): Claude Code CLI で音声ディクテーション機能を使用して、プロンプトを話して入力できます。長押しまたはタップで録音できます。
- [ステータスラインをカスタマイズする](https://code.claude.com/docs/ja/statusline.md): Claude Code でコンテキストウィンドウの使用状況、コスト、git ステータスを監視するカスタムステータスバーを設定します
- [キーボードショートカットのカスタマイズ](https://code.claude.com/docs/ja/keybindings.md): キーボードショートカットをカスタマイズして、Claude Code でキーバインディング設定ファイルを使用します。

### リファレンス

#### リファレンス

- [CLI リファレンス](https://code.claude.com/docs/ja/cli-reference.md): Claude Code コマンドラインインターフェースの完全なリファレンス。コマンドとフラグを含みます。
- [コマンド](https://code.claude.com/docs/ja/commands.md): Claude Code で利用可能なコマンドの完全なリファレンス。ビルトインコマンドとバンドルされたスキルを含みます。
- [環境変数](https://code.claude.com/docs/ja/env-vars.md): Claude Code の動作を制御する環境変数のリファレンス。
- [ツールリファレンス](https://code.claude.com/docs/ja/tools-reference.md): Claude Code が使用できるツールの完全なリファレンス。権限要件とツール別の動作を含みます。
- [インタラクティブモード](https://code.claude.com/docs/ja/interactive-mode.md): Claude Code セッションのキーボードショートカット、入力モード、インタラクティブ機能の完全なリファレンス。
- [チェックポイント](https://code.claude.com/docs/ja/checkpointing.md): Claude のエディット内容と会話を追跡、巻き戻し、要約してセッション状態を管理します。
- [Hooks リファレンス](https://code.claude.com/docs/ja/hooks.md): Claude Code のフック イベント、設定スキーマ、JSON 入出力形式、終了コード、非同期フック、HTTP フック、プロンプト フック、MCP ツール フックのリファレンス。
- [プラグインリファレンス](https://code.claude.com/docs/ja/plugins-reference.md): Claude Code プラグインシステムの完全な技術リファレンス。スキーマ、CLI コマンド、コンポーネント仕様を含みます。
- [チャネルリファレンス](https://code.claude.com/docs/ja/channels-reference.md): webhook、アラート、チャットメッセージを Claude Code セッションにプッシュする MCP サーバーを構築します。チャネルコントラクトのリファレンス：機能宣言、通知イベント、返信ツール、送信者ゲーティング、権限リレー。

#### 用語集

- [用語集](https://code.claude.com/docs/ja/glossary.md): Claude Code の用語の定義。agentic loop、compaction、CLAUDE.md、hooks、subagents、MCP などのコア概念の意味を学びます。

### Agent SDK

#### Agent SDK

- [Agent SDK の概要](https://code.claude.com/docs/ja/agent-sdk/overview.md): Claude Code をライブラリとして使用して、本番環境対応の AI エージェントを構築します
- [クイックスタート](https://code.claude.com/docs/ja/agent-sdk/quickstart.md): Python または TypeScript Agent SDK を使用して、自律的に動作する AI エージェントを構築する方法を学びます
- [Claude Agent SDK への移行](https://code.claude.com/docs/ja/agent-sdk/migration-guide.md): Claude Code TypeScript および Python SDK を Claude Agent SDK に移行するためのガイド
- [Agent SDK のトラブルシューティング](https://code.claude.com/docs/ja/agent-sdk/troubleshooting.md): Agent SDK エラーを表示されたメッセージで修正します。TypeScript と Python SDK の各エラーについて、原因と対処方法を説明します。

#### エージェントを構築

- [エージェントを設定する](https://code.claude.com/docs/ja/agent-sdk/configuration.md): Agent SDK セッションを設定する：options オブジェクトを構成し、モデル、環境、制限を設定し、各機能オプションのページを見つけます。
- [例](https://code.claude.com/docs/ja/agent-sdk/examples.md): 構築したいものに合致する完全で実行可能な Agent SDK プロジェクト、または Claude Cookbook のガイド付きレシピを見つけてください。

#### コアコンセプト

- [エージェントループの仕組み](https://code.claude.com/docs/ja/agent-sdk/agent-loop.md): メッセージライフサイクル、ツール実行、コンテキストウィンドウ、および SDK エージェントを支えるアーキテクチャを理解します。
- [SDK で Claude Code 機能を使用する](https://code.claude.com/docs/ja/agent-sdk/claude-code-features.md): プロジェクト指示、スキル、フック、その他の Claude Code 機能を SDK エージェントに読み込みます。
- [セッションの操作](https://code.claude.com/docs/ja/agent-sdk/sessions.md): セッションがエージェント会話履歴をどのように保持するか、および以前の実行に戻るために continue、resume、fork をいつ使用するかについて説明します。
- [セッションを外部ストレージに永続化する](https://code.claude.com/docs/ja/agent-sdk/session-storage.md): Agent SDK セッションのトランスクリプトを独自のオブジェクトストア、キーバリューストア、またはデータベースにミラーリングして、他のホストがセッションを再開できるようにします。

#### 入力と出力

- [ストリーミング入力](https://code.claude.com/docs/ja/agent-sdk/streaming-vs-single-mode.md): Claude Agent SDK の 2 つの入力モードを理解し、各モードをいつ使用するかを学ぶ
- [承認とユーザー入力を処理する](https://code.claude.com/docs/ja/agent-sdk/user-input.md): Claude の承認リクエストと確認質問をユーザーに表示し、その決定を SDK に返します。
- [リアルタイムでレスポンスをストリーミングする](https://code.claude.com/docs/ja/agent-sdk/streaming-output.md): テキストとツール呼び出しがストリーミングされるときに、Agent SDK からリアルタイムレスポンスを取得します
- [エージェントから構造化された出力を取得する](https://code.claude.com/docs/ja/agent-sdk/structured-outputs.md): JSON Schema、Zod、または Pydantic を使用して、エージェントワークフローから検証済みの JSON を返します。マルチターンツール使用後に型安全で構造化されたデータを取得します。

#### ツールで拡張する

- [Claude にカスタムツールを提供する](https://code.claude.com/docs/ja/agent-sdk/custom-tools.md): Claude Agent SDK のインプロセス MCP サーバーでカスタムツールを定義し、Claude が関数を呼び出し、API にアクセスし、ドメイン固有の操作を実行できるようにします。
- [MCP を使用して外部ツールに接続する](https://code.claude.com/docs/ja/agent-sdk/mcp.md): MCP サーバーを設定してエージェントを外部ツールで拡張します。トランスポートタイプ、大規模なツールセット向けのツール検索、認証、エラーハンドリングについて説明します。
- [多くのツールにスケーリングするツール検索](https://code.claude.com/docs/ja/agent-sdk/tool-search.md): 必要なものだけをオンデマンドで検出して読み込むことで、エージェントを数千のツールにスケーリングします。
- [SDK のサブエージェント](https://code.claude.com/docs/ja/agent-sdk/subagents.md): コンテキストを分離し、タスクを並列実行し、Claude Agent SDK アプリケーションで特化した指示を適用するサブエージェントを定義および呼び出します。

#### 動作をカスタマイズする

- [システムプロンプトの変更](https://code.claude.com/docs/ja/agent-sdk/modifying-system-prompts.md): `claude_code` プリセットとカスタムシステムプロンプトの間で選択し、CLAUDE.md、出力スタイル、append、または完全にカスタムなプロンプトで動作をカスタマイズします。
- [Agent Skills でエージェントを拡張する](https://code.claude.com/docs/ja/agent-sdk/skills.md): Claude Agent SDK セッションで Claude が呼び出せる Skills を制御し、名前でコマンドをディスパッチし、セッションが検出する Skills を作成します
- [SDK のプラグイン](https://code.claude.com/docs/ja/agent-sdk/plugins.md): Agent SDK を通じてカスタムプラグインを読み込み、スキル、エージェント、フック、MCP サーバーで Claude Code を拡張します

#### 制御と可観測性

- [権限の設定](https://code.claude.com/docs/ja/agent-sdk/permissions.md): 権限モード、hooks、および宣言的な許可/拒否ルールを使用して、エージェントがツールをどのように使用するかを制御します。
- [フックを使用してエージェントの動作をインターセプトして制御する](https://code.claude.com/docs/ja/agent-sdk/hooks.md): フックを使用して、エージェント実行の重要なポイントでエージェントの動作をインターセプトしてカスタマイズします
- [checkpointing でファイル変更を巻き戻す](https://code.claude.com/docs/ja/agent-sdk/file-checkpointing.md): エージェントセッション中のファイル変更を追跡し、ファイルを以前の任意の状態に復元します
- [コストと使用状況を追跡する](https://code.claude.com/docs/ja/agent-sdk/cost-tracking.md): Claude Agent SDK でトークン使用状況を追跡し、コストを見積もり、プロンプトキャッシングを設定する方法を学びます。
- [OpenTelemetry を使用した可観測性](https://code.claude.com/docs/ja/agent-sdk/observability.md): Agent SDK からトレース、メトリクス、イベントを OpenTelemetry を使用して可観測性バックエンドにエクスポートします。
- [Todo を追跡する](https://code.claude.com/docs/ja/agent-sdk/todo-tracking.md): Agent SDK セッションで todo を追跡し、構造化されたツール呼び出しから Claude の進捗をアプリケーションでレンダリングします

#### デプロイメント

- [Agent SDK のホスティング](https://code.claude.com/docs/ja/agent-sdk/hosting.md): Agent SDK を本番環境にデプロイする：サブプロセスアーキテクチャ、セッション永続化、スケーリング、可観測性、Docker、Kubernetes、サンドボックスプロバイダー向けのマルチテナント分離。
- [AI エージェントの安全なデプロイ](https://code.claude.com/docs/ja/agent-sdk/secure-deployment.md): 分離、認証情報管理、ネットワーク制御を使用して Claude Code と Agent SDK のデプロイを保護するためのガイド

#### SDK リファレンス

- [Agent SDK リファレンス - TypeScript](https://code.claude.com/docs/ja/agent-sdk/typescript.md): TypeScript Agent SDK の完全な API リファレンス。すべての関数、型、インターフェースを含みます。
- [TypeScript SDK V2 セッション API（削除済み）](https://code.claude.com/docs/ja/agent-sdk/typescript-v2-preview.md): マルチターン会話向けのセッションベースの send/stream パターンを備えた、削除済みの V2 TypeScript Agent SDK セッション API のリファレンス。
- [Agent SDK リファレンス - Python](https://code.claude.com/docs/ja/agent-sdk/python.md): Python Agent SDK の完全な API リファレンス。すべての関数、型、クラスを含みます。

### 新機能

#### 新機能

- [新機能](https://code.claude.com/docs/ja/whats-new/index.md): Claude Code の注目すべき機能を毎週紹介するダイジェスト。コードスニペット、デモ、およびそれらが重要である理由についての説明が含まれています。
- [Week 36 · 8月31日～9月4日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w36.md): Claude Fable 5.1に切り替え、Desktop でコンピュータ使用をバックグラウンドで実行し、ライブ /diff パネルで Claude の編集を確認します。
- [第 35 週・2026 年 8 月 24～28 日](https://code.claude.com/docs/ja/whats-new/2026-w35.md): Claude Code デスクトップアプリでターミナルセッションを再開し、Claude が作成したフィードバックレポートを確認し、制限モードでセッションを開始します。
- [Week 34 · 8月17～21日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w34.md): /design スキルでドラフト可能な UI アートボードを作成し、Concise 出力スタイルを設定し、スマートフォンからマシン上で Claude Code セッションを開始します。
- [第 33 週・8 月 10～14 日、2026 年](https://code.claude.com/docs/ja/whats-new/2026-w33.md): Claude Code Desktop は使用制限がリセットされた後に自動継続し、フォークモードがデフォルトで有効になり、GitLab マージリクエストとマーケットプレイスが GitHub に参加します。
- [Week 32 · 8月3日～7日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w32.md): Claude Code セッションが相互にメッセージを送信でき、自己ホスト環境がクラウドセッションをお客様のインフラストラクチャで実行でき、自動モードがデフォルトの権限モードになります。
- [Week 30 · 7月20～24日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w30.md): Opus 5 が Opus のデフォルトモデルになり、Claude Code Desktop に iOS Simulator ペインが追加され、Claude Security プラグインがコードの脆弱性をスキャンします。
- [第 29 週・2026 年 7 月 13～17 日](https://code.claude.com/docs/ja/whats-new/2026-w29.md): MCP コネクタを通じてライブデータを公開アーティファクトに取り込み、新しいスクリーンリーダーモードで Claude Code をスクリーンリーダーと共に使用します。
- [Week 28 · 7月6日～10日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w28.md): Desktop アプリの組み込みブラウザから外部サイトを閲覧し、/doctor で完全なセットアップチェックアップを実行し、オートモードのトランスクリプト保護とエージェントビューのアップグレードを取得します。
- [Week 27 · 6月29日～7月3日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w27.md): Claude Sonnet 5 がデフォルトモデルになり、Claude in Chrome が一般提供開始、サブエージェントがデフォルトでバックグラウンド実行、Claude Desktop が Linux でベータ版提供開始、/radio が Claude FM にチューニングします。
- [Week 26 · 2026 年 6 月 22 日～26 日](https://code.claude.com/docs/ja/whats-new/2026-w26.md): シェルから claude mcp login で MCP サーバーを認証し、! プレフィックスでシェルモードコマンド出力に応答を取得し、/clear の前の会話を /rewind で再開します。
- [Week 25 · 2026年6月15日～19日](https://code.claude.com/docs/ja/whats-new/2026-w25.md): Artifacts を使用してセッションからライブで共有可能なページを公開し、deny ルールと ask ルールでツールパラメータをマッチングし、/config でプロンプトから任意の設定を行います。
- [Week 24 · 2026年6月8日～12日](https://code.claude.com/docs/ja/whats-new/2026-w24.md): /cd でセッションを新しいディレクトリに移動し、サブエージェントが独自のサブエージェントをスポーンでき、セーフモードで壊れた設定をトラブルシューティングします。
- [Week 23 · 2026 年 6 月 1 日～5 日](https://code.claude.com/docs/ja/whats-new/2026-w23.md): Amazon Bedrock、Google Cloud の Agent Platform、Microsoft Foundry で auto mode を実行し、acceptEdits モードでコードを実行できるファイルを書き込む前にプロンプトを表示し、/plugin list でインストール済みプラグインをリストアップし、マネージドデプロイメント向けに承認されたバージョン範囲を要求します。
- [Week 22 · 5月25～29日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w22.md): Claude Opus 4.8 で Claude Code を実行し、動的ワークフローで大規模なタスクを調整し、security-guidance プラグインでセキュリティの問題をキャッチし、Opus 4.8 でファストモードをより低い価格で使用します。
- [Week 21 · 5月18～22日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w21.md): Pro プランで auto mode を使用し、Sonnet 4.6 でサポートされ、/usage でどのスキル、サブエージェント、MCP サーバーがプラン制限を駆動しているかを確認し、新しい /code-review コマンドでdiff を確認します。
- [Week 20 · 2026年5月11日～15日](https://code.claude.com/docs/ja/whats-new/2026-w20.md): 1つの画面からすべての Claude Code セッションを管理できるエージェントビュー、条件が満たされるまで Claude を目標に向かって動作させ続け、Opus 4.7 でデフォルトでファストモードを実行します。
- [Week 19 · 2026年5月4日～8日](https://code.claude.com/docs/ja/whats-new/2026-w19.md): .zip アーカイブと URL からプラグインを読み込み、Ctrl+R ですべてのプロジェクト全体のコマンド履歴を検索し、ローカル HEAD またはリモートデフォルトから新しいワークツリーをブランチし、オートモードのハードデニールルールで無条件にアクションをブロックします。
- [Week 18 · 4月27日～5月1日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w18.md): Claude Code は Windows で Git Bash なしで実行でき、claude auth login はブラウザコールバックが localhost に到達できない場合に貼り付けられた OAuth コードを受け入れ、claude project purge はプロジェクトごとにローカル状態をクリーンアップし、PR URL を /resume に貼り付けるとそれを作成したセッションが見つかります。
- [Week 17 · 2026年4月20～24日](https://code.claude.com/docs/ja/whats-new/2026-w17.md): /ultrareview がリサーチプレビューとしてオープン、ターミナルに戻ったときの自動セッションリキャップ、プラグインで構築・配布できるカスタムカラーテーマ、ウェブ上で再設計された Claude Code。
- [Week 16 · 4月13～17日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w16.md): 新しい xhigh エフォートレベルを備えた Claude Opus 4.7、Claude Code ウェブ版の Routines、Claude が必要なときにあなたの電話に ping を送信するモバイルプッシュ通知、使用制限を駆動している要因を表示する /usage 内訳、およびバンドルされた JavaScript に代わるネイティブバイナリ。
- [Week 15 · 2026年4月6日～10日](https://code.claude.com/docs/ja/whats-new/2026-w15.md): Ultraplan クラウドプランニング、セルフペーシング /loop を備えた Monitor ツール、セットアップをパッケージ化するための /team-onboarding、およびターミナルからの /autofix-pr。
- [Week 14 · 3月30日～4月3日、2026年](https://code.claude.com/docs/ja/whats-new/2026-w14.md): CLI でのコンピュータ使用、インタラクティブなプロダクト内レッスン、ちらつきのないレンダリング、ツール別 MCP 結果サイズオーバーライド、および PATH 上のプラグイン実行ファイル。
- [Week 13 · 2026年3月23日～27日](https://code.claude.com/docs/ja/whats-new/2026-w13.md): 自動モード（ハンズオフ権限）、コンピュータ使用機能の組み込み、クラウド内の PR 自動修正、トランスクリプト検索、Windows 用 PowerShell ツール。

### リソース

#### リソース

- [法的および規制対応](https://code.claude.com/docs/ja/legal-and-compliance.md): Claude Code の法的契約、規制認証、およびセキュリティ情報。

---

## Claude Code Docs: Korean

- 官方原文：https://code.claude.com/docs/_llms/ko.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-ko.md`

# Claude Code Docs: Korean

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Korean

### 시작하기

#### 시작하기

- [개요](https://code.claude.com/docs/ko/overview.md): Claude Code는 코드베이스를 읽고, 파일을 편집하고, 명령을 실행하고, 개발 도구와 통합하는 에이전트 코딩 도구입니다. 터미널, IDE, 데스크톱 앱 및 브라우저에서 사용할 수 있습니다.
- [빠른 시작](https://code.claude.com/docs/ko/quickstart.md): Claude Code에 오신 것을 환영합니다!
- [변경 로그](https://code.claude.com/docs/ko/changelog.md)

#### 핵심 개념

- [Claude Code의 작동 방식](https://code.claude.com/docs/ko/how-claude-code-works.md): 에이전트 루프, 내장 도구, Claude Code가 프로젝트와 상호작용하는 방식을 이해합니다.
- [Claude Code 확장하기](https://code.claude.com/docs/ko/features-overview.md): CLAUDE.md, Skills, subagents, hooks, MCP, 플러그인을 언제 사용할지 이해합니다.
- [.claude 디렉토리 탐색](https://code.claude.com/docs/ko/claude-directory.md): Claude Code가 CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules, auto memory를 읽는 위치입니다. 프로젝트의 .claude 디렉토리와 홈 디렉토리의 ~/.claude를 탐색합니다.
- [컨텍스트 윈도우 살펴보기](https://code.claude.com/docs/ko/context-window.md): Claude Code의 컨텍스트 윈도우가 세션 중에 어떻게 채워지는지 보여주는 대화형 시뮬레이션입니다. 자동으로 로드되는 항목, 각 파일 읽기의 비용, 규칙과 훅이 언제 실행되는지 확인하세요.
- [Claude Code가 prompt caching을 사용하는 방법](https://code.claude.com/docs/ko/prompt-caching.md): Claude Code는 prompt caching을 자동으로 관리합니다. 모델 전환이 느린 캐시되지 않은 턴을 트리거하는 이유, `/compact`의 비용, CLAUDE.md 편집이 세션 중에 적용되지 않는 이유, 캐시 히트율을 확인하는 방법을 알아봅니다.

#### Claude Code 사용하기

- [Claude가 프로젝트를 기억하는 방법](https://code.claude.com/docs/ko/memory.md): CLAUDE.md 또는 AGENTS.md 파일로 Claude에 지속적인 지침을 제공하고, 자동 메모리를 통해 Claude가 자동으로 학습을 축적하도록 합니다.
- [세션 관리](https://code.claude.com/docs/ko/sessions.md): Claude Code 대화의 이름을 지정하고, 재개하고, 분기하고, 전환합니다. `--continue`, `--resume`, `--from-pr`, `/resume` 선택기, 세션 이름 지정, 대화 기록 내보내기 및 대화 기록 저장 위치를 다룹니다.
- [일반적인 워크플로우](https://code.claude.com/docs/ko/common-workflows.md): Claude Code를 사용하여 코드베이스 탐색, 버그 수정, 리팩토링, 테스트 및 기타 일상적인 작업을 위한 단계별 가이드입니다.
- [프롬프트 라이브러리](https://code.claude.com/docs/ko/prompt-library.md): Claude Code에 복사하여 붙여넣을 수 있는 프롬프트 모음으로, 작업과 역할별로 태그가 지정되어 있습니다.
- [Claude Code 모범 사례](https://code.claude.com/docs/ko/best-practices.md): 환경 구성부터 병렬 세션 확장까지 Claude Code를 최대한 활용하기 위한 팁과 패턴입니다.

#### 플랫폼 및 통합

- [플랫폼 및 통합](https://code.claude.com/docs/ko/platforms.md): Claude Code를 실행할 위치를 선택하고 연결할 항목을 결정합니다. CLI, Desktop, VS Code, JetBrains, 웹, 모바일 및 Chrome, Slack, CI/CD와 같은 통합을 비교합니다.
- [모든 기기에서 로컬 세션 계속하기 (Remote Control)](https://code.claude.com/docs/ko/remote-control.md): Remote Control을 사용하여 휴대폰, 태블릿 또는 모든 브라우저에서 로컬 Claude Code 세션을 계속할 수 있습니다. claude.ai/code 및 Claude 모바일 앱과 함께 작동합니다.
- [Claude가 프로젝트로 진행 중인 작업을 조율하도록 하기](https://code.claude.com/docs/ko/claude-projects.md): Claude에게 한 대화에서 관련된 작업 모음을 제공하고 저장소, 지침 및 메모리를 공유하는 병렬 클라우드 세션을 조율하도록 합니다.
- [모바일에서 Claude Code](https://code.claude.com/docs/ko/mobile.md): Claude 앱(iOS 및 Android)을 통해 휴대폰에서 Claude Code 작업을 시작, 모니터링 및 조종합니다.
- [Chrome에서 Claude Code 사용하기](https://code.claude.com/docs/ko/chrome.md): Claude Code를 Chrome 브라우저에 연결하여 웹 앱을 테스트하고, 콘솔 로그로 디버깅하며, 양식 작성을 자동화하고, 웹 페이지에서 데이터를 추출합니다.
- [Claude가 CLI에서 컴퓨터를 사용하도록 설정](https://code.claude.com/docs/ko/computer-use.md): Claude Code CLI에서 컴퓨터 사용을 활성화하여 Claude가 macOS에서 앱을 열고, 클릭하고, 입력하고, 화면을 볼 수 있도록 합니다. 터미널을 떠나지 않고 네이티브 앱을 테스트하고, 시각적 문제를 디버깅하고, GUI 전용 도구를 자동화합니다.
- [VS Code에서 Claude Code 사용하기](https://code.claude.com/docs/ko/vs-code.md): VS Code용 Claude Code 확장 프로그램을 설치하고 구성합니다. 인라인 diff, @-멘션, 계획 검토 및 키보드 단축키를 통해 AI 코딩 지원을 받습니다.
- [JetBrains IDEs](https://code.claude.com/docs/ko/jetbrains.md): Claude Code를 IntelliJ, PyCharm, WebStorm 등 JetBrains IDE와 함께 사용합니다
- [Slack의 Claude Code](https://code.claude.com/docs/ko/slack.md): Slack 워크스페이스에서 직접 코딩 작업을 위임합니다. Anthropic은 Team 및 Enterprise 워크스페이스를 위해 이 이전 버전을 Claude Tag로 대체하고 있으며, Pro 및 Max 플랜에서는 이것이 설정 경로로 유지됩니다.
- [Claude Tag](https://code.claude.com/docs/ko/claude-tag.md): Claude Tag를 사용하여 팀의 Slack 채널에 Claude를 가져오고 claude.com에서 설정 및 사용 설명서를 찾습니다.

##### 클라우드의 Claude Code

- [클라우드에서 Claude Code 시작하기](https://code.claude.com/docs/ko/web-quickstart.md): 브라우저나 휴대폰에서 클라우드에서 Claude Code를 실행합니다. GitHub 저장소를 연결하고, 작업을 제출하고, 로컬 설정 없이 PR을 검토합니다.
- [클라우드에서 Claude Code 사용하기](https://code.claude.com/docs/ko/claude-code-on-the-web.md): 브라우저, 휴대폰, 데스크톱 앱 또는 터미널에서 클라우드의 Claude Code 세션을 실행하고, --cloud 및 --teleport로 이동하며, pull request를 자동 수정합니다.
- [루틴으로 작업 자동화하기](https://code.claude.com/docs/ko/routines.md): Claude Code를 자동 조종 장치에 올려놓으세요. 클라우드 인프라에서 일정에 따라 실행되거나 API 호출로 트리거되거나 GitHub 이벤트에 반응하는 루틴을 정의하세요.
- [ultrareview로 버그 찾기](https://code.claude.com/docs/ko/ultrareview.md): /code-review ultra를 사용하여 클라우드에서 심층적인 다중 에이전트 코드 리뷰를 실행하여 병합 전에 버그를 찾고 검증합니다.

##### Claude Code 데스크톱

- [데스크톱 앱 시작하기](https://code.claude.com/docs/ko/desktop-quickstart.md): 데스크톱에 Claude Code를 설치하고 첫 번째 코딩 세션을 시작합니다
- [Desktop 애플리케이션](https://code.claude.com/docs/ko/desktop.md): Claude Code Desktop을 더 활용하기: Git 격리를 통한 병렬 세션, 드래그 앤 드롭 패널 레이아웃, 통합 터미널 및 파일 편집기, 사이드 채팅, 컴퓨터 사용, 휴대폰에서 Dispatch 세션 전송, 시각적 diff 검토, 앱 미리보기, PR 모니터링, 커넥터, 엔터프라이즈 구성.
- [Linux의 Claude Desktop (베타)](https://code.claude.com/docs/ko/desktop-linux.md): Ubuntu 및 Debian에서 Claude 데스크톱 앱 설치 및 업데이트
- [WSL의 Claude Code Desktop](https://code.claude.com/docs/ko/desktop-wsl.md): WSL 2 배포판 내에서 Code 세션 실행
- [Claude Code Desktop에서 반복 작업 예약하기](https://code.claude.com/docs/ko/desktop-scheduled-tasks.md): Claude Code Desktop에서 예약된 작업을 설정하여 일일 코드 리뷰, 종속성 감사 또는 아침 브리핑을 위해 Claude를 자동으로 반복 실행합니다.
- [iOS 시뮬레이터에서 앱 테스트하기](https://code.claude.com/docs/ko/desktop-ios-simulator.md): Claude Code Desktop은 Claude가 앱을 빌드, 실행 또는 확인할 때 iOS 시뮬레이터 창에서 앱을 열며, 각 세션마다 별도의 시뮬레이터를 제공합니다.

##### 코드 검토 및 CI/CD

- [Claude가 코드를 작성할 때 보안 문제 포착](https://code.claude.com/docs/ko/security-guidance.md): security-guidance 플러그인을 설치하여 Claude가 자신의 코드 변경 사항을 취약점에 대해 검토하고 동일한 세션에서 수정하도록 합니다.
- [코드베이스에서 취약점 스캔하기](https://code.claude.com/docs/ko/claude-security.md): Claude Security 플러그인을 설치하여 Claude Code 세션에서 코드베이스의 취약점을 스캔하고 발견 사항을 검토 및 적용할 수 있는 패치로 변환합니다.
- [Code Review](https://code.claude.com/docs/ko/code-review.md): 다중 에이전트 분석을 통해 전체 코드베이스를 검토하여 논리 오류, 보안 취약점 및 회귀를 감지하는 자동화된 PR 검토를 설정합니다
- [Claude Code GitHub Actions](https://code.claude.com/docs/ko/github-actions.md): @claude 멘션에 응답하고, 작업을 자동화하고, 이슈를 풀 리퀘스트로 변환하기 위해 GitHub Actions 워크플로우에서 Claude Code를 실행합니다
- [Claude Code GitHub Actions를 클라우드 제공자와 함께 사용하기](https://code.claude.com/docs/ko/github-actions-cloud-providers.md): Claude API 대신 Amazon Bedrock, Google Cloud의 Agent Platform 또는 Microsoft Foundry를 통해 Claude Code GitHub Actions 실행하기
- [GitHub Enterprise Server와 Claude Code](https://code.claude.com/docs/ko/github-enterprise-server.md): 자체 호스팅되는 GitHub Enterprise Server 인스턴스에 Claude Code를 연결하여 클라우드 세션, 코드 리뷰 및 플러그인 마켓플레이스를 사용합니다.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/ko/gitlab-ci-cd.md): Claude Code를 GitLab CI/CD와 함께 개발 워크플로우에 통합하는 방법을 알아봅니다

### Claude Code로 빌드하기

#### 에이전트 및 병렬 작업

- [에이전트를 병렬로 실행하기](https://code.claude.com/docs/ko/agents.md): Claude Code가 여러 작업을 동시에 처리하는 방법들을 비교합니다: 서브에이전트, 에이전트 뷰, 에이전트 팀, 동적 워크플로우, 프로젝트.
- [사용자 정의 subagent 만들기](https://code.claude.com/docs/ko/sub-agents.md): Claude Code에서 작업별 워크플로우 및 향상된 컨텍스트 관리를 위한 특화된 AI subagent를 만들고 사용합니다.
- [여러 에이전트를 에이전트 뷰로 관리하기](https://code.claude.com/docs/ko/agent-view.md): 하나의 화면에서 많은 Claude Code 세션을 디스패치하고 관리합니다. 에이전트 뷰는 모든 세션이 무엇을 하고 있는지, 어떤 세션이 입력을 필요로 하는지 보여줍니다.
- [Claude Code 세션 팀 조율하기](https://code.claude.com/docs/ko/agent-teams.md): 공유 작업, 에이전트 간 메시징, 중앙 집중식 관리를 통해 함께 작동하는 여러 Claude Code 인스턴스를 조율합니다.
- [다른 Claude Code 세션에 메시지 보내기](https://code.claude.com/docs/ko/cross-session-messaging.md): Claude가 이 머신의 다른 Claude Code 세션을 나열하고 메시지를 보낼 수 있도록 하며, 다른 머신이나 클라우드의 세션에 도달합니다.
- [동적 워크플로우로 대규모 서브에이전트 조율하기](https://code.claude.com/docs/ko/workflows.md): 동적 워크플로우는 Claude가 작성한 스크립트에서 많은 서브에이전트를 조율하며, 이를 다시 실행할 수 있습니다. 코드베이스 감사, 대규모 마이그레이션, 교차 검증 연구에 사용합니다.
- [worktree를 사용하여 병렬 세션 실행](https://code.claude.com/docs/ko/worktrees.md): git worktree에서 병렬 Claude Code 세션을 격리하여 변경 사항이 충돌하지 않도록 합니다. `--worktree` 플래그, 서브에이전트 격리, `.worktreeinclude`, 정리 및 비git VCS 훅을 다룹니다.

#### MCP

- [MCP 서버에 연결하기](https://code.claude.com/docs/ko/mcp-quickstart.md): Claude Code에 MCP 서버를 추가하고, 연결을 확인하며, 디스크에서 구성을 찾습니다.
- [MCP를 통해 Claude Code를 도구에 연결하기](https://code.claude.com/docs/ko/mcp.md): Model Context Protocol을 사용하여 Claude Code를 도구에 연결하는 방법을 알아봅니다.

#### Skills

- [Claude를 skills로 확장하기](https://code.claude.com/docs/ko/skills.md): Claude Code에서 skills를 생성, 관리 및 공유하여 Claude의 기능을 확장합니다. 사용자 정의 명령어 및 번들 skills를 포함합니다.

#### 플러그인

- [마켓플레이스를 통해 미리 빌드된 플러그인 발견 및 설치](https://code.claude.com/docs/ko/discover-plugins.md): 마켓플레이스에서 플러그인을 찾아 설치하여 Claude Code를 새로운 skills, agents 및 기능으로 확장합니다.
- [플러그인 만들기](https://code.claude.com/docs/ko/plugins.md): skills, agents, hooks, MCP servers를 사용하여 Claude Code를 확장하는 사용자 정의 플러그인을 만듭니다.
- [evals로 플러그인 테스트하기](https://code.claude.com/docs/ko/plugin-evals.md): Claude Code 플러그인에 대한 eval 케이스를 작성하고, claude plugin eval로 실행하며, 결과를 채점하고, 플러그인 없는 기준선과 비교하고, CI에서 점수를 기준으로 게이트합니다.

#### 아티팩트

- [세션 출력을 아티팩트로 공유하기](https://code.claude.com/docs/ko/artifacts.md): 아티팩트는 Claude Code의 작업을 claude.ai의 라이브 인터랙티브 페이지로 변환하여 비공개로 유지하거나, 조직과 공유하거나, 공개 링크로 게시할 수 있습니다.

#### 자동화

- [hooks를 사용하여 작업 자동화](https://code.claude.com/docs/ko/hooks-guide.md): Claude Code가 파일을 편집하거나 작업을 완료하거나 입력이 필요할 때 자동으로 셸 명령을 실행합니다. 코드 형식 지정, 알림 전송, 명령 검증 및 프로젝트 규칙 적용합니다.
- [채널을 사용하여 실행 중인 세션으로 이벤트 푸시하기](https://code.claude.com/docs/ko/channels.md): 채널을 사용하여 MCP 서버에서 실행 중인 Claude Code 세션으로 메시지, 알림 및 웹훅을 푸시합니다. CI 결과, 채팅 메시지 및 모니터링 이벤트를 전달하여 Claude가 자리를 비웠을 때 반응할 수 있도록 합니다.
- [일정에 따라 프롬프트 실행하기](https://code.claude.com/docs/ko/scheduled-tasks.md): /loop와 cron 스케줄링 도구를 사용하여 Claude Code 세션 내에서 프롬프트를 반복 실행하거나, 상태를 폴링하거나, 일회성 알림을 설정합니다.
- [Claude를 목표를 향해 계속 작동하게 하기](https://code.claude.com/docs/ko/goal.md): /goal로 완료 조건을 설정하면 Claude가 조건이 충족될 때까지 계속 작동하며, 모델이 불가능하다고 판단하거나 수정해야 할 오류가 발생하면 목표가 지워집니다.
- [Claude Code를 프로그래밍 방식으로 실행하기](https://code.claude.com/docs/ko/headless.md): Agent SDK를 사용하여 CLI, Python 또는 TypeScript에서 Claude Code를 프로그래밍 방식으로 실행합니다.
- [링크에서 세션 시작하기](https://code.claude.com/docs/ko/deep-links.md): URL에서 Claude Code 터미널 세션을 엽니다. 런북, 알림 및 대시보드에 `claude-cli://` 링크를 포함하여 클릭하면 Claude Code가 올바른 저장소에서 올바른 프롬프트와 함께 열립니다.

#### 가이드

- [모노레포 또는 대규모 코드베이스에서 Claude Code 설정하기](https://code.claude.com/docs/ko/large-codebases.md): 중첩된 CLAUDE.md 파일, 스파스 워크트리, 코드 인텔리전스, 패키지별 스킬을 사용하여 모노레포 및 대규모 단일 트리 코드베이스에 대해 Claude Code를 구성하여 Claude가 작업 중인 코드에 집중하도록 유지합니다.

#### 문제 해결

- [설치 및 로그인 문제 해결](https://code.claude.com/docs/ko/troubleshoot-install.md): Claude Code 설치 또는 로그인 시 command not found, PATH, 권한, 네트워크 및 인증 오류를 수정합니다.
- [문제 해결](https://code.claude.com/docs/ko/troubleshooting.md): Claude Code에서 높은 CPU 또는 메모리 사용량, 중단, 자동 압축 스래싱 및 검색 문제를 해결하고 다른 문제에 대한 올바른 페이지를 찾습니다.
- [구성 디버깅하기](https://code.claude.com/docs/ko/debug-your-config.md): CLAUDE.md, 설정, 훅, MCP 서버 또는 스킬이 적용되지 않는 이유를 진단합니다. /context, /doctor, /hooks, /mcp를 사용하여 실제로 로드된 항목을 확인합니다.
- [오류 참조](https://code.claude.com/docs/ko/errors.md): Claude Code 런타임 오류 메시지를 조회하고 각 오류의 의미와 해결 방법을 확인합니다.

### 관리

#### 설정 및 액세스

- [조직을 위한 Claude Code 설정](https://code.claude.com/docs/ko/admin-setup.md): Claude Code를 배포하는 관리자를 위한 의사결정 맵으로, API 제공자, 관리 설정, 정책 시행, 사용량 모니터링 및 데이터 처리를 다룹니다.
- [고급 설정](https://code.claude.com/docs/ko/setup.md): Claude Code의 시스템 요구사항, 플랫폼별 설치, 버전 관리 및 제거.
- [인증](https://code.claude.com/docs/ko/authentication.md): Claude Code에 로그인하고 개인, 팀, 조직을 위한 인증을 구성합니다.
- [관리형 설정 배포](https://code.claude.com/docs/ko/managed-settings.md): 모든 개발자의 머신에 관리형 설정을 배포합니다: OS별 전달 메커니즘, Claude Code가 관리형 소스를 결합하는 방식, 그리고 적용 여부를 확인하는 방법입니다.
- [서버 관리 설정 구성](https://code.claude.com/docs/ko/server-managed-settings.md): 기기 관리 인프라 없이 서버 전달 설정을 통해 조직을 위해 Claude Code를 중앙에서 구성합니다.
- [조직의 MCP 서버 접근 제어](https://code.claude.com/docs/ko/managed-mcp.md): 관리형 구성 파일, 관리형 설정, 허용 목록 및 거부 목록을 사용하여 사용자가 추가하거나 연결할 수 있는 MCP 서버를 제한하거나 모든 사용자에게 서버를 제공합니다.
- [자동 모드 구성](https://code.claude.com/docs/ko/auto-mode-config.md): 자동 모드 분류기에 조직이 신뢰하는 저장소, 버킷 및 도메인을 알려줍니다. 환경 컨텍스트를 설정하고, 기본 차단 및 허용 규칙을 재정의하며, 자동 모드 CLI 하위 명령으로 유효한 구성을 검사합니다.

#### 배포

- [엔터프라이즈 배포 개요](https://code.claude.com/docs/ko/third-party-integrations.md): Claude Code가 다양한 타사 서비스 및 인프라와 통합되어 엔터프라이즈 배포 요구사항을 충족하는 방법을 알아봅니다.
- [기능 가용성](https://code.claude.com/docs/ko/feature-availability.md): Anthropic 구독 플랜, Anthropic Console, Amazon Bedrock, AWS의 Claude Platform, Google Cloud의 Agent Platform, Microsoft Foundry에서 사용 가능한 Claude Code 기능을 비교합니다.
- [Amazon Bedrock의 Claude Code](https://code.claude.com/docs/ko/amazon-bedrock.md): Amazon Bedrock을 통한 Claude Code 구성, 설정, IAM 구성 및 문제 해결에 대해 알아봅니다.
- [AWS의 Claude Platform에서 Claude Code](https://code.claude.com/docs/ko/claude-platform-on-aws.md): AWS 인증, IAM 액세스 제어 및 AWS Marketplace 청구를 사용하여 Anthropic 운영 Claude API를 사용하도록 Claude Code를 구성합니다.
- [Google Cloud의 Agent Platform에서 Claude Code 사용하기](https://code.claude.com/docs/ko/google-vertex-ai.md): Google Cloud의 Agent Platform(이전 Vertex AI)을 통해 Claude Code를 구성하는 방법을 알아봅니다. 설정, IAM 구성 및 문제 해결을 포함합니다.
- [Microsoft Foundry의 Claude Code](https://code.claude.com/docs/ko/microsoft-foundry.md): 설정, 구성 및 문제 해결을 포함하여 Microsoft Foundry를 통해 Claude Code를 구성하는 방법을 알아봅니다.
- [엔터프라이즈 네트워크 구성](https://code.claude.com/docs/ko/network-config.md): 프록시 서버, 사용자 정의 인증 기관(CA), 상호 전송 계층 보안(mTLS) 인증을 통해 엔터프라이즈 환경에서 Claude Code를 구성합니다.
- [기업 런처 뒤에서 Claude Code 실행](https://code.claude.com/docs/ko/corporate-launcher.md): CLAUDE_CODE_PROCESS_WRAPPER 또는 processWrapper 설정을 사용하여 Claude Code가 자체 바이너리에서 시작하는 프로세스(백그라운드 서비스 및 모든 에이전트 뷰 세션 포함)를 필수 런처를 통해 라우팅합니다.
- [개발 컨테이너](https://code.claude.com/docs/ko/devcontainer.md): 팀 전체에서 일관되고 격리된 환경을 위해 Claude Code를 개발 컨테이너 내에서 실행합니다.

#### 게이트웨이

- [게이트웨이를 통해 Claude Code 실행](https://code.claude.com/docs/ko/gateways.md): Claude Code를 자체 호스팅 게이트웨이를 통해 라우팅하여 중앙 집중식 자격 증명, 사용량 추적 및 비용 제어를 수행합니다. 아키텍처, Anthropic의 Claude 앱 게이트웨이 및 다른 게이트웨이 제품 사용을 다룹니다.

##### Claude 앱 게이트웨이

- [Amazon Bedrock, AWS의 Claude Platform, Google Cloud 및 Microsoft Foundry용 Claude 앱 게이트웨이](https://code.claude.com/docs/ko/claude-apps-gateway.md): SSO 로그인, 그룹별 모델 액세스, OTLP 텔레메트리를 갖춘 자체 호스팅 게이트웨이를 통해 Amazon Bedrock, AWS의 Claude Platform, Google Cloud 또는 Microsoft Foundry에서 Claude Code를 실행합니다.
- [Claude 앱 게이트웨이 구성](https://code.claude.com/docs/ko/claude-apps-gateway-config.md): 모든 gateway.yaml 옵션에 대한 참조: 리스너 및 TLS, OIDC, 세션, Postgres 저장소, Amazon Bedrock, Claude Platform on AWS, Google Cloud의 Agent Platform, Microsoft Foundry 업스트림, 모델 라우팅, 관리형 정책 및 텔레메트리.
- [Claude 앱 게이트웨이 지출 한도](https://code.claude.com/docs/ko/claude-apps-gateway-spend-limits.md): Claude 앱 게이트웨이를 통해 각 개발자의 지출을 일, 주 또는 월 단위로 제한합니다. Admin API로 한도를 설정하면 게이트웨이가 모든 요청에서 실시간으로 이를 적용합니다.
- [Claude 앱 게이트웨이 배포 및 운영](https://code.claude.com/docs/ko/claude-apps-gateway-deploy.md): IdP에 게이트웨이를 등록하고, 컨테이너를 빌드하며, Kubernetes 또는 Cloud Run에 배포하고 운영합니다: 상태 확인, 시크릿 로테이션, 업그레이드 및 보안.
- [AWS에서 Claude 앱 게이트웨이 배포](https://code.claude.com/docs/ko/claude-apps-gateway-on-aws.md): AWS에서 Claude 앱 게이트웨이를 실행하는 실제 예제입니다: ECS Fargate 또는 EKS, PostgreSQL용 Amazon RDS, AWS Secrets Manager, Amazon Bedrock에 대한 IAM 역할 인증.
- [Google Cloud에 Claude 앱 게이트웨이 배포](https://code.claude.com/docs/ko/claude-apps-gateway-on-gcp.md): Google Cloud에서 Claude 앱 게이트웨이를 실행하는 실제 예제: Cloud Run 또는 GKE, Cloud SQL for PostgreSQL, Secret Manager, 그리고 Google Cloud의 Agent Platform에 대한 서비스 계정 인증.

##### 기타 게이트웨이

- [다른 LLM gateway](https://code.claude.com/docs/ko/llm-gateway.md): 조직이 이미 실행 중인 LLM gateway를 통해 Claude Code를 라우팅합니다. Claude Code를 gateway에 연결하고, 조직을 위해 gateway를 배포하고, Claude Code가 gateway에 전송하는 내용을 다룹니다.
- [Claude Code를 LLM 게이트웨이에 연결](https://code.claude.com/docs/ko/llm-gateway-connect.md): 조직의 LLM 게이트웨이에 Claude Code를 연결합니다. 관리자가 이미 구성했는지 확인하거나, 기본 URL과 자격 증명을 직접 설정한 후 연결을 확인하고 게이트웨이 오류를 해결합니다.
- [조직을 위한 LLM 게이트웨이 배포](https://code.claude.com/docs/ko/llm-gateway-rollout.md): Claude Code용 게이트웨이 제품 배포: Claude Code가 전송하는 내용을 전달하도록 구성하고, 개발자 자격증명을 발급하며, 관리되는 설정을 통해 구성을 배포하고, 롤아웃을 확인합니다.
- [Claude Code 게이트웨이 호환성 가이드](https://code.claude.com/docs/ko/llm-gateway-protocol.md): Claude Code와 호환되는 LLM 게이트웨이 유지: 호출하는 엔드포인트, 전달해야 할 헤더 및 본문 필드, 그리고 제거될 때 중단되는 기능.

#### 사용량 및 비용

- [모니터링](https://code.claude.com/docs/ko/monitoring-usage.md): Claude Code에 대한 OpenTelemetry를 활성화하고 구성하는 방법을 알아봅니다.
- [비용을 효과적으로 관리하기](https://code.claude.com/docs/ko/costs.md): 토큰 사용량을 추적하고, 팀 지출 한도를 설정하며, 컨텍스트 관리, 모델 선택, 확장 사고 설정 및 전처리 hooks를 통해 Claude Code 비용을 절감합니다.
- [팀 사용량을 분석으로 추적하기](https://code.claude.com/docs/ko/analytics.md): Claude Code 사용량 지표를 확인하고, 채택 현황을 추적하며, 분석 대시보드에서 엔지니어링 속도를 측정합니다.

#### 플러그인 배포

- [플러그인 마켓플레이스 생성 및 배포](https://code.claude.com/docs/ko/plugin-marketplaces.md): Claude Code 확장 프로그램을 팀과 커뮤니티에 배포하기 위한 플러그인 마켓플레이스를 구축하고 호스팅합니다.
- [플러그인 종속성 버전 제약](https://code.claude.com/docs/ko/plugin-dependencies.md): 플러그인 종속성에 대한 버전 제약을 선언하고 선별된 플러그인 세트를 하나의 설치 뒤에 번들로 제공합니다.
- [CLI에서 플러그인 추천하기](https://code.claude.com/docs/ko/plugin-hints.md): CLI에서 한 줄 마커를 내보내어 Claude Code가 사용자에게 공식 플러그인 설치를 권유하도록 합니다.
- [조직을 위한 플러그인 추천](https://code.claude.com/docs/ko/plugin-relevance.md): 마켓플레이스 플러그인 항목에 관련성 블록을 추가하여 사용자의 작업이 일치할 때 Claude Code가 플러그인을 제안하도록 합니다.

#### 보안 및 데이터

- [보안](https://code.claude.com/docs/ko/security.md): Claude Code의 보안 보호 기능과 안전한 사용을 위한 모범 사례에 대해 알아봅니다.
- [데이터 사용](https://code.claude.com/docs/ko/data-usage.md): Anthropic의 Claude 데이터 사용 정책에 대해 알아봅니다
- [Zero data retention](https://code.claude.com/docs/ko/zero-data-retention.md): Claude for Enterprise에서 Claude Code의 Zero Data Retention(ZDR)에 대해 알아보세요. 범위, 비활성화된 기능, 활성화 요청 방법을 포함합니다.

#### 도입

- [커뮤니케이션 키트](https://code.claude.com/docs/ko/communications-kit.md): 엔지니어링 조직에 Claude Code를 배포할 때 사용할 수 있는 출시 공지, 드립 캠페인 메시지, FAQ 응답입니다.
- [Champion kit](https://code.claude.com/docs/ko/champion-kit.md): Claude Code를 내부적으로 옹호하는 엔지니어를 위한 플레이북: 공유할 내용, 질문에 답하는 방법, 팀 내 도입 확대 방법.

### 구성

#### 설정

- [설정 파일 및 우선순위](https://code.claude.com/docs/ko/settings.md): Claude Code 설정을 변경하고, 키가 속할 범위를 선택하고, 변경을 확인하고, 키가 여러 위치에 설정되어 있을 때 Claude Code가 사용하는 값을 알아봅니다.
- [모든 설정](https://code.claude.com/docs/ko/settings-reference.md): Claude Code settings.json의 모든 키에 대한 완전한 참조: 각 키의 위치, 유형 및 기본값, 붙여넣기 가능한 예제, 모든 키의 인덱스.
- [예제 설정 파일](https://code.claude.com/docs/ko/settings-example.md): 개발자, 팀, 조직을 위한 현실적인 settings.json 파일: 하나를 복사하고 원하는 키를 유지한 후 값을 변경하세요.

#### 권한 및 샌드박싱

- [권한 구성](https://code.claude.com/docs/ko/permissions.md): 세분화된 권한 규칙, 모드 및 관리형 정책을 통해 Claude Code가 액세스하고 수행할 수 있는 작업을 제어합니다.
- [권한 모드 선택](https://code.claude.com/docs/ko/permission-modes.md): Claude가 작업하기 전에 묻는지 여부를 제어합니다. CLI에서 Shift+Tab, VS Code의 모드 표시기 또는 Desktop의 모드 선택기로 권한 모드를 전환합니다.
- [샌드박싱된 Bash 도구 구성](https://code.claude.com/docs/ko/sandboxing.md): Claude Code의 샌드박싱된 Bash 도구가 파일시스템 및 네트워크 격리를 제공하여 더 안전하고 자율적인 에이전트 실행을 가능하게 하는 방법을 알아봅니다.
- [샌드박스 환경 선택](https://code.claude.com/docs/ko/sandbox-environments.md): Claude Code 샌드박스 옵션 비교: 기본 제공 샌드박스 Bash 도구, 샌드박스 런타임, 개발 컨테이너, Docker, VM. 위협 모델에 맞는 적절한 격리를 선택합니다.

#### 환경

- [클라우드 환경 구성](https://code.claude.com/docs/ko/cloud-environments.md): Claude Code 클라우드 세션을 위한 클라우드 환경 구성: 네트워크 액세스 수준, 환경 변수, 설정 스크립트 및 환경 캐싱.

##### 자체 호스팅 환경

- [자체 호스팅 환경](https://code.claude.com/docs/ko/self-hosted-environments.md): 조직이 제어하는 인프라에서 Claude Code 클라우드 세션을 실행합니다: 자체 호스팅 환경을 설정하고, 러너를 배포하고, 세션을 자신의 컴퓨팅으로 라우팅합니다.
- [자체 호스팅 환경 빠른 시작](https://code.claude.com/docs/ko/self-hosted-environments-quickstart.md): 첫 번째 자체 호스팅 환경 설정: Claude Code 설치, 환경 생성, 러너 시작, 세션 라우팅.
- [자체 호스팅 환경을 프로덕션에 배포](https://code.claude.com/docs/ko/self-hosted-environments-deploy.md): 프로덕션에서 자체 호스팅 러너 실행: 보안 강화, 네트워크 이그레스 제어, git 자격증명, Kubernetes 및 Compose 레시피, 그리고 문제 해결.
- [자체 호스팅 환경에서 세션 사용자 정의](https://code.claude.com/docs/ko/self-hosted-environments-configuration.md): 세션별 자격 증명, 라이프사이클 훅, 온디맨드 러너 생성을 위한 래퍼 스크립트로 자체 호스팅 환경 세션을 사용자 정의합니다.
- [자체 호스팅 환경을 엔드투엔드로 테스트하기](https://code.claude.com/docs/ko/self-hosted-environments-testing.md): CI에서 자체 호스팅 러너 이미지 검증: CLI로 세션을 디스패치하고, Stop 훅을 통해 Claude의 응답을 읽으며, 전체 루프를 스크립트로 작성합니다.
- [자체 호스팅 환경 참조](https://code.claude.com/docs/ko/self-hosted-environments-reference.md): 자체 호스팅 러너 및 오케스트레이터에 대한 완전한 참조: CLI 플래그, 환경 변수 및 Prometheus 메트릭.
- [자체 호스팅 환경에서 세션 ID 확인](https://code.claude.com/docs/ko/self-hosted-environments-identity.md): 자체 호스팅 환경의 세션에서 요청을 신뢰할 수 있도록 네트워크의 서비스가 CLAUDE_CODE_SESSION_ACCESS_TOKEN JWT를 확인합니다.

#### 모델 및 응답

- [모델 구성](https://code.claude.com/docs/ko/model-config.md): Claude Code가 사용하는 모델, 노력 수준, 확장된 컨텍스트 및 자동 압축 윈도우를 구성합니다
- [빠른 모드로 응답 속도 향상](https://code.claude.com/docs/ko/fast-mode.md): Claude Code에서 빠른 모드를 전환하여 더 빠른 Opus 응답을 받습니다.
- [어려운 결정을 조언자 도구로 에스컬레이션하기](https://code.claude.com/docs/ko/advisor.md): 주 모델을 더 강력한 조언자 모델과 쌍으로 만들어 Claude가 작업 중 핵심 순간에 조언자를 참고하도록 합니다.
- [출력 스타일](https://code.claude.com/docs/ko/output-styles.md): 소프트웨어 엔지니어링 이상의 용도로 Claude Code 적응시키기

#### 인터페이스

- [Claude Code를 위한 터미널 구성](https://code.claude.com/docs/ko/terminal-config.md): Shift+Enter를 개행으로 수정하고, Claude가 완료되면 터미널 벨을 받으며, tmux를 구성하고, 색상 테마를 일치시키고, Claude Code CLI에서 Vim 모드를 활성화합니다.
- [전체 화면 렌더링](https://code.claude.com/docs/ko/fullscreen.md): 마우스 지원과 안정적인 메모리 사용으로 더 부드럽고 깜빡임 없는 렌더링 모드를 활성화합니다.
- [스크린 리더로 Claude Code 사용하기](https://code.claude.com/docs/ko/accessibility.md): VoiceOver 및 NVDA와 같은 스크린 리더, 스크린 확대기, 감소된 모션, 색맹 친화적 테마에 대한 Claude Code 설정하기.
- [음성 받아쓰기](https://code.claude.com/docs/ko/voice-dictation.md): Claude Code CLI에서 누르고 있기 또는 탭하기 음성 받아쓰기로 프롬프트를 말씀하세요.
- [상태 표시줄 사용자 정의](https://code.claude.com/docs/ko/statusline.md): Claude Code에서 컨텍스트 윈도우 사용량, 비용 및 git 상태를 모니터링하기 위해 사용자 정의 상태 표시줄 구성
- [키보드 단축키 사용자 정의](https://code.claude.com/docs/ko/keybindings.md): keybindings 구성 파일을 사용하여 Claude Code에서 키보드 단축키를 사용자 정의합니다.

### 참고

#### 참고

- [CLI 참조](https://code.claude.com/docs/ko/cli-reference.md): Claude Code 명령줄 인터페이스의 완전한 참조로, 명령어와 플래그를 포함합니다.
- [명령어](https://code.claude.com/docs/ko/commands.md): Claude Code에서 사용 가능한 명령어의 완전한 참조 자료로, 기본 제공 명령어 및 번들 스킬을 포함합니다.
- [환경 변수](https://code.claude.com/docs/ko/env-vars.md): Claude Code 동작을 제어하는 환경 변수에 대한 참고 자료입니다.
- [도구 참조](https://code.claude.com/docs/ko/tools-reference.md): Claude Code가 사용할 수 있는 도구의 완전한 참조로, 권한 요구사항 및 도구별 동작을 포함합니다.
- [대화형 모드](https://code.claude.com/docs/ko/interactive-mode.md): Claude Code 세션의 키보드 단축키, 입력 모드 및 대화형 기능에 대한 완전한 참조입니다.
- [Checkpointing](https://code.claude.com/docs/ko/checkpointing.md): Claude의 편집 및 대화를 추적, 되돌리기 및 요약하여 세션 상태를 관리합니다.
- [Hooks 참조](https://code.claude.com/docs/ko/hooks.md): Claude Code hook 이벤트, 구성 스키마, JSON 입출력 형식, 종료 코드, 비동기 hook, HTTP hook, 프롬프트 hook, MCP 도구 hook에 대한 참조입니다.
- [플러그인 참조](https://code.claude.com/docs/ko/plugins-reference.md): 스키마, CLI 명령어, 컴포넌트 사양을 포함한 Claude Code 플러그인 시스템의 완전한 기술 참조입니다.
- [채널 참조](https://code.claude.com/docs/ko/channels-reference.md): 웹훅, 알림, 채팅 메시지를 Claude Code 세션으로 푸시하는 MCP 서버를 구축합니다. 채널 계약 참조: 기능 선언, 알림 이벤트, 회신 도구, 발신자 게이팅, 권한 릴레이.

#### 용어집

- [용어집](https://code.claude.com/docs/ko/glossary.md): Claude Code 용어 정의. 에이전트 루프, 컴팩션, CLAUDE.md, 훅, 서브에이전트, MCP 및 기타 핵심 개념의 의미를 알아봅니다.

### Agent SDK

#### Agent SDK

- [Agent SDK 개요](https://code.claude.com/docs/ko/agent-sdk/overview.md): Claude Code를 라이브러리로 사용하여 프로덕션 AI 에이전트 구축하기
- [빠른 시작](https://code.claude.com/docs/ko/agent-sdk/quickstart.md): Python 또는 TypeScript Agent SDK를 사용하여 자율적으로 작동하는 AI 에이전트를 구축하기 시작합니다
- [Claude Agent SDK로 마이그레이션](https://code.claude.com/docs/ko/agent-sdk/migration-guide.md): Claude Code TypeScript 및 Python SDK를 Claude Agent SDK로 마이그레이션하기 위한 가이드
- [Agent SDK 문제 해결](https://code.claude.com/docs/ko/agent-sdk/troubleshooting.md): 정확한 오류 메시지로 Agent SDK 오류를 수정합니다. TypeScript 및 Python SDK의 각 오류에 대한 원인과 해결 방법을 제공합니다.

#### 에이전트 구축하기

- [에이전트 구성](https://code.claude.com/docs/ko/agent-sdk/configuration.md): Agent SDK 세션 구성: 옵션 객체 작성, 모델 설정, 환경 및 제한 설정, 각 기능 옵션의 페이지 찾기.
- [예제](https://code.claude.com/docs/ko/agent-sdk/examples.md): 구축하려는 것과 일치하는 완전하고 실행 가능한 Agent SDK 프로젝트 또는 Claude Cookbook의 가이드 레시피를 찾습니다.

#### 핵심 개념

- [에이전트 루프의 작동 원리](https://code.claude.com/docs/ko/agent-sdk/agent-loop.md): 메시지 생명주기, 도구 실행, 컨텍스트 윈도우, 그리고 SDK 에이전트를 구동하는 아키텍처를 이해합니다.
- [SDK에서 Claude Code 기능 사용하기](https://code.claude.com/docs/ko/agent-sdk/claude-code-features.md): 프로젝트 지침, 스킬, 훅 및 기타 Claude Code 기능을 SDK 에이전트에 로드합니다.
- [세션으로 작업하기](https://code.claude.com/docs/ko/agent-sdk/sessions.md): 세션이 에이전트 대화 기록을 어떻게 유지하는지, 그리고 이전 실행으로 돌아가기 위해 continue, resume, fork를 언제 사용할지에 대해 알아봅니다.
- [세션을 외부 스토리지에 유지하기](https://code.claude.com/docs/ko/agent-sdk/session-storage.md): Agent SDK 세션 트랜스크립트를 자신의 객체 저장소, 키-값 저장소 또는 데이터베이스에 미러링하여 다른 호스트에서 세션을 재개할 수 있습니다.

#### 입력 및 출력

- [스트리밍 입력](https://code.claude.com/docs/ko/agent-sdk/streaming-vs-single-mode.md): Claude Agent SDK의 두 가지 입력 모드를 이해하고 각각을 언제 사용할지 알아보기
- [승인 및 사용자 입력 처리](https://code.claude.com/docs/ko/agent-sdk/user-input.md): Claude의 승인 요청 및 명확화 질문을 사용자에게 표시한 후 SDK에 사용자의 결정을 반환합니다.
- [실시간으로 응답 스트리밍하기](https://code.claude.com/docs/ko/agent-sdk/streaming-output.md): 텍스트와 도구 호출이 스트리밍될 때 Agent SDK에서 실시간 응답 받기
- [에이전트에서 구조화된 출력 얻기](https://code.claude.com/docs/ko/agent-sdk/structured-outputs.md): JSON Schema, Zod 또는 Pydantic을 사용하여 에이전트 워크플로우에서 검증된 JSON을 반환합니다. 다중 턴 도구 사용 후 타입 안전 구조화된 데이터를 얻습니다.

#### 도구로 확장하기

- [Claude에 사용자 정의 도구 제공](https://code.claude.com/docs/ko/agent-sdk/custom-tools.md): Claude Agent SDK의 인프로세스 MCP 서버로 사용자 정의 도구를 정의하여 Claude가 함수를 호출하고, API를 사용하며, 도메인별 작업을 수행할 수 있도록 합니다.
- [외부 도구와 MCP로 연결하기](https://code.claude.com/docs/ko/agent-sdk/mcp.md): MCP 서버를 구성하여 에이전트를 외부 도구로 확장합니다. 전송 유형, 대규모 도구 세트를 위한 도구 검색, 인증 및 오류 처리를 다룹니다.
- [많은 도구로 확장하기 - 도구 검색](https://code.claude.com/docs/ko/agent-sdk/tool-search.md): 수백 개 또는 수천 개의 도구로 에이전트를 확장하고, 필요한 것만 동적으로 발견하여 로드합니다.
- [SDK의 서브에이전트](https://code.claude.com/docs/ko/agent-sdk/subagents.md): Claude Agent SDK 애플리케이션에서 서브에이전트를 정의하고 호출하여 컨텍스트를 격리하고, 작업을 병렬로 실행하며, 메인 에이전트의 프롬프트에 추가하지 않고 특화된 지시사항을 적용합니다.

#### 동작 사용자 정의

- [시스템 프롬프트 수정](https://code.claude.com/docs/ko/agent-sdk/modifying-system-prompts.md): `claude_code` 프리셋과 사용자 정의 시스템 프롬프트 중에서 선택하고, CLAUDE.md, 출력 스타일, append, 또는 완전히 사용자 정의된 프롬프트로 동작을 사용자 정의합니다.
- [Skills로 에이전트 확장하기](https://code.claude.com/docs/ko/agent-sdk/skills.md): Claude Agent SDK 세션에서 Claude가 호출할 수 있는 Skills를 제어하고, 이름으로 명령을 전달하며, 세션이 발견하는 Skills를 작성합니다
- [SDK의 플러그인](https://code.claude.com/docs/ko/agent-sdk/plugins.md): Agent SDK를 통해 스킬, 에이전트, 훅 및 MCP 서버를 추가하여 Claude Code를 확장하는 사용자 정의 플러그인 로드

#### 제어 및 관찰성

- [권한 구성](https://code.claude.com/docs/ko/agent-sdk/permissions.md): 권한 모드, 훅, 선언적 허용/거부 규칙을 사용하여 에이전트가 도구를 사용하는 방식을 제어합니다.
- [훅으로 에이전트 동작 가로채기 및 제어](https://code.claude.com/docs/ko/agent-sdk/hooks.md): 훅을 사용하여 에이전트 실행의 주요 지점에서 에이전트 동작을 가로채고 사용자 정의합니다
- [체크포인팅으로 파일 변경 사항 되돌리기](https://code.claude.com/docs/ko/agent-sdk/file-checkpointing.md): 에이전트 세션 중 파일 변경 사항을 추적하고 파일을 이전의 모든 상태로 복원합니다
- [비용 및 사용량 추적](https://code.claude.com/docs/ko/agent-sdk/cost-tracking.md): Claude Agent SDK를 사용하여 토큰 사용량을 추적하고, 비용을 예측하며, 프롬프트 캐싱을 구성하는 방법을 알아봅니다.
- [OpenTelemetry를 통한 관찰성](https://code.claude.com/docs/ko/agent-sdk/observability.md): Agent SDK에서 OpenTelemetry를 사용하여 추적, 메트릭 및 이벤트를 관찰성 백엔드로 내보냅니다.
- [할일 추적](https://code.claude.com/docs/ko/agent-sdk/todo-tracking.md): Agent SDK 세션에서 할일을 추적하고 구조화된 도구 호출에서 Claude의 진행 상황을 애플리케이션에 렌더링합니다

#### 배포

- [Agent SDK 호스팅](https://code.claude.com/docs/ko/agent-sdk/hosting.md): 프로덕션에서 Agent SDK 배포: 서브프로세스 아키텍처, 세션 지속성, 확장성, 관찰성, Docker, Kubernetes 및 샌드박스 제공자를 위한 멀티테넌트 격리.
- [AI 에이전트 안전하게 배포하기](https://code.claude.com/docs/ko/agent-sdk/secure-deployment.md): 격리, 자격증명 관리, 네트워크 제어를 통해 Claude Code 및 Agent SDK 배포를 보호하는 가이드

#### SDK 참고자료

- [Agent SDK 참조 - TypeScript](https://code.claude.com/docs/ko/agent-sdk/typescript.md): TypeScript Agent SDK의 완전한 API 참조로, 모든 함수, 타입 및 인터페이스를 포함합니다.
- [TypeScript SDK V2 세션 API (지원 중단됨)](https://code.claude.com/docs/ko/agent-sdk/typescript-v2-preview.md): 다중 턴 대화를 위한 세션 기반 send/stream 패턴을 사용하는 지원 중단된 V2 TypeScript Agent SDK 세션 API 참조입니다.
- [Agent SDK 참조 - Python](https://code.claude.com/docs/ko/agent-sdk/python.md): Python Agent SDK의 완전한 API 참조로, 모든 함수, 타입 및 클래스를 포함합니다.

### 새로운 소식

#### 새로운 소식

- [새로운 기능](https://code.claude.com/docs/ko/whats-new/index.md): Claude Code 기능의 주간 요약으로, 코드 스니펫, 데모, 그리고 그 중요성에 대한 맥락을 포함합니다.
- [주간 37 · 2026년 9월 7–11일](https://code.claude.com/docs/ko/whats-new/2026-w37.md): claude plugin eval로 플러그인을 테스트하고 Claude Code Desktop 창을 별도의 윈도우로 팝아웃합니다.
- [주간 36 · 8월 31일 – 9월 4일, 2026년](https://code.claude.com/docs/ko/whats-new/2026-w36.md): Claude Fable 5.1로 전환하고, Desktop에서 컴퓨터 사용을 백그라운드에서 실행하며, /diff 패널에서 Claude의 편집 내용을 실시간으로 확인합니다.
- [35주 · 2026년 8월 24–28일](https://code.claude.com/docs/ko/whats-new/2026-w35.md): Claude Code 데스크톱 앱에서 터미널 세션을 재개하고, Claude가 작성한 피드백 보고서를 검토하며, 제한된 모드에서 세션을 시작합니다.
- [34주차 · 2026년 8월 17–21일](https://code.claude.com/docs/ko/whats-new/2026-w34.md): /design 스킬로 편집 가능한 UI 아트보드를 작성하고, Concise 출력 스타일을 설정하며, 휴대폰에서 머신의 Claude Code 세션을 시작합니다.
- [33주차 · 8월 10–14일, 2026년](https://code.claude.com/docs/ko/whats-new/2026-w33.md): Claude Code Desktop이 사용량 제한 리셋 후 자동으로 계속 진행되며, 포크 모드가 기본적으로 켜지고, GitLab 병합 요청 및 마켓플레이스가 GitHub에 합류합니다.
- [32주차 · 2026년 8월 3–7일](https://code.claude.com/docs/ko/whats-new/2026-w32.md): Claude Code 세션이 서로 메시지를 주고받으며, 자체 호스팅 환경이 클라우드 세션을 사용자의 인프라에서 실행하고, 자동 모드가 기본 권한 모드가 됩니다.
- [주간 30 · 7월 20–24, 2026](https://code.claude.com/docs/ko/whats-new/2026-w30.md): Opus 5가 기본 Opus 모델이 되고, Claude Code Desktop에 iOS Simulator 창이 추가되며, Claude Security 플러그인이 코드의 취약점을 스캔합니다.
- [29주차 · 2026년 7월 13–17일](https://code.claude.com/docs/ko/whats-new/2026-w29.md): MCP 커넥터를 통해 라이브 데이터를 게시된 아티팩트로 가져오고, 새로운 스크린 리더 모드에서 Claude Code를 스크린 리더와 함께 사용합니다.
- [28주차 · 2026년 7월 6–10일](https://code.claude.com/docs/ko/whats-new/2026-w28.md): Desktop 앱의 내장 브라우저에서 외부 사이트를 탐색하고, /doctor로 전체 설정 점검을 실행하며, 자동 모드 트랜스크립트 보호 및 에이전트 뷰 업그레이드를 확인합니다.
- [27주차 · 6월 29일 – 7월 3일, 2026](https://code.claude.com/docs/ko/whats-new/2026-w27.md): Claude Sonnet 5가 기본 모델이 되었으며, Chrome의 Claude가 정식 출시되었고, 서브에이전트가 기본적으로 백그라운드에서 실행되며, Claude Desktop이 Linux에서 베타로 출시되었고, /radio가 Claude FM으로 튜닝됩니다.
- [26주차 · 2026년 6월 22–26일](https://code.claude.com/docs/ko/whats-new/2026-w26.md): 셸에서 claude mcp login으로 MCP 서버를 인증하고, ! 접두사로 셸 모드 명령 출력에 응답을 받으며, /clear 이전 대화를 /rewind로 재개합니다.
- [25주차 · 2026년 6월 15–19일](https://code.claude.com/docs/ko/whats-new/2026-w25.md): Artifacts를 사용하여 세션에서 라이브 공유 가능한 페이지를 게시하고, 거부 및 요청 규칙에서 도구 매개변수를 일치시키며, /config를 사용하여 프롬프트에서 모든 설정을 지정합니다.
- [24주차 · 2026년 6월 8–12일](https://code.claude.com/docs/ko/whats-new/2026-w24.md): /cd로 세션을 새 디렉토리로 이동하고, 하위 에이전트가 자신의 하위 에이전트를 생성하도록 하며, 안전 모드로 손상된 구성을 문제 해결합니다.
- [23주차 · 2026년 6월 1–5일](https://code.claude.com/docs/ko/whats-new/2026-w23.md): Amazon Bedrock, Google Cloud의 Agent Platform, Microsoft Foundry에서 자동 모드 실행, acceptEdits 모드에서 코드를 실행할 수 있는 파일 작성 전 프롬프트 표시, /plugin list로 설치된 플러그인 나열, 관리형 배포를 위한 승인된 버전 범위 필수.
- [Week 22 · May 25–29, 2026](https://code.claude.com/docs/ko/whats-new/2026-w22.md): Claude Opus 4.8에서 Claude Code를 실행하고, 동적 워크플로우로 대규모 작업을 조율하며, security-guidance 플러그인으로 보안 문제를 포착하고, Opus 4.8의 빠른 모드를 더 낮은 가격으로 사용합니다.
- [21주차 · 2026년 5월 18–22일](https://code.claude.com/docs/ko/whats-new/2026-w21.md): Pro 플랜에서 자동 모드를 사용하고 Sonnet 4.6을 지원하며, /usage에서 플랜 한도를 주도하는 스킬, 서브에이전트, MCP 서버를 확인하고, 새로운 /code-review 명령으로 diff를 검토합니다.
- [20주차 · 2026년 5월 11–15일](https://code.claude.com/docs/ko/whats-new/2026-w20.md): 에이전트 뷰로 모든 Claude Code 세션을 한 화면에서 관리하고, Claude가 조건을 만족할 때까지 목표를 향해 작동하도록 유지하며, Opus 4.7에서 기본적으로 빠른 모드를 실행합니다.
- [19주차 · 2026년 5월 4–8일](https://code.claude.com/docs/ko/whats-new/2026-w19.md): .zip 아카이브 및 URL에서 플러그인을 로드하고, Ctrl+R로 모든 프로젝트의 명령 기록을 검색하고, 로컬 HEAD 또는 원격 기본값에서 새 worktree를 분기하고, 자동 모드 하드 거부 규칙으로 작업을 무조건 차단합니다.
- [18주차 · 4월 27일 – 5월 1일, 2026년](https://code.claude.com/docs/ko/whats-new/2026-w18.md): Claude Code가 Windows에서 Git Bash 없이 실행되며, claude auth login은 브라우저 콜백이 localhost에 도달할 수 없을 때 붙여넣은 OAuth 코드를 허용하고, claude project purge는 프로젝트별 로컬 상태를 정리하며, PR URL을 /resume에 붙여넣으면 이를 생성한 세션을 찾습니다.
- [17주차 · 2026년 4월 20–24일](https://code.claude.com/docs/ko/whats-new/2026-w17.md): /ultrareview가 연구 미리보기로 공개되며, 터미널로 돌아올 때 자동 세션 요약, 플러그인으로 빌드하고 배포할 수 있는 커스텀 색상 테마, 그리고 재설계된 웹용 Claude Code가 제공됩니다.
- [16주차 · 2026년 4월 13–17일](https://code.claude.com/docs/ko/whats-new/2026-w16.md): 새로운 xhigh 노력 수준이 포함된 Claude Opus 4.7, Claude Code 웹의 루틴, Claude가 필요할 때 휴대폰에 알림을 보내는 모바일 푸시 알림, 사용 한도를 주도하는 요소를 보여주는 /usage 분석, 그리고 번들된 JavaScript를 대체하는 네이티브 바이너리.
- [15주차 · 2026년 4월 6–10일](https://code.claude.com/docs/ko/whats-new/2026-w15.md): Ultraplan 클라우드 계획, 자동 페이싱 /loop이 있는 Monitor 도구, 설정을 패키징하기 위한 /team-onboarding, 그리고 터미널에서 /autofix-pr을 사용합니다.
- [14주차 · 3월 30일 – 4월 3일, 2026](https://code.claude.com/docs/ko/whats-new/2026-w14.md): CLI의 컴퓨터 사용, 인터랙티브 인제품 레슨, 깜빡임 없는 렌더링, 도구별 MCP 결과 크기 오버라이드, PATH의 플러그인 실행 파일.
- [13주차 · 2026년 3월 23–27일](https://code.claude.com/docs/ko/whats-new/2026-w13.md): 자동 모드의 무인 권한 관리, 내장된 컴퓨터 사용, 클라우드의 PR 자동 수정, 트랜스크립트 검색, Windows용 PowerShell 도구.

### 리소스

#### 리소스

- [법률 및 규정 준수](https://code.claude.com/docs/ko/legal-and-compliance.md): Claude Code의 법률 계약, 규정 준수 인증 및 보안 정보입니다.

---

## Claude Code Docs: Brazilian Portuguese

- 官方原文：https://code.claude.com/docs/_llms/pt-br.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-pt-br.md`

# Claude Code Docs: Brazilian Portuguese

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Brazilian Portuguese

### Primeiros passos

#### Primeiros passos

- [Visão geral](https://code.claude.com/docs/pt/overview.md): Claude Code é uma ferramenta de codificação agentic que lê sua base de código, edita arquivos, executa comandos e se integra com suas ferramentas de desenvolvimento. Disponível em seu terminal, IDE, aplicativo de desktop e navegador.
- [Guia de Início Rápido](https://code.claude.com/docs/pt/quickstart.md): Bem-vindo ao Claude Code!
- [Changelog](https://code.claude.com/docs/pt/changelog.md)

#### Conceitos principais

- [Como Claude Code funciona](https://code.claude.com/docs/pt/how-claude-code-works.md): Entenda o loop agentic, as ferramentas integradas e como Claude Code interage com seu projeto.
- [Estender Claude Code](https://code.claude.com/docs/pt/features-overview.md): Entenda quando usar CLAUDE.md, Skills, subagents, hooks, MCP e plugins.
- [Explore o diretório .claude](https://code.claude.com/docs/pt/claude-directory.md): Onde Claude Code lê CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules e auto memory. Explore o diretório .claude em seu projeto e ~/.claude em seu diretório home.
- [Explore a janela de contexto](https://code.claude.com/docs/pt/context-window.md): Uma simulação interativa de como a janela de contexto do Claude Code se preenche durante uma sessão. Veja o que é carregado automaticamente, quanto cada leitura de arquivo custa e quando regras e hooks são acionados.
- [Como Claude Code usa prompt caching](https://code.claude.com/docs/pt/prompt-caching.md): Claude Code gerencia prompt caching automaticamente. Veja por que uma mudança de modelo dispara um turno lento sem cache, o que `/compact` custa, por que edições de CLAUDE.md não se aplicam no meio da sessão e como verificar sua taxa de acerto de cache.

#### Usar Claude Code

- [Como Claude se lembra do seu projeto](https://code.claude.com/docs/pt/memory.md): Dê a Claude instruções persistentes com arquivos CLAUDE.md ou AGENTS.md, e deixe Claude acumular aprendizados automaticamente com memória automática.
- [Gerenciar sessões](https://code.claude.com/docs/pt/sessions.md): Nomeie, retome, ramifique e alterne entre conversas do Claude Code. Abrange `--continue`, `--resume`, `--from-pr`, o seletor `/resume`, nomeação de sessão, exportação de transcritos e onde os transcritos são armazenados.
- [Fluxos de trabalho comuns](https://code.claude.com/docs/pt/common-workflows.md): Guias passo a passo para explorar bases de código, corrigir bugs, refatorar, testar e outras tarefas cotidianas com Claude Code.
- [Biblioteca de prompts](https://code.claude.com/docs/pt/prompt-library.md): Copie e cole prompts para Claude Code, marcados por tarefa e função.
- [Melhores práticas para Claude Code](https://code.claude.com/docs/pt/best-practices.md): Dicas e padrões para aproveitar ao máximo o Claude Code, desde a configuração do seu ambiente até o dimensionamento em sessões paralelas.

#### Plataformas e integrações

- [Plataformas e integrações](https://code.claude.com/docs/pt/platforms.md): Escolha onde executar Claude Code e o que conectar a ele. Compare a CLI, Desktop, VS Code, JetBrains, web, mobile e integrações como Chrome, Slack e CI/CD.
- [Continue sessões locais de qualquer dispositivo com Remote Control](https://code.claude.com/docs/pt/remote-control.md): Continue uma sessão local do Claude Code do seu telefone, tablet ou qualquer navegador usando Remote Control. Funciona com claude.ai/code e o aplicativo Claude para dispositivos móveis.
- [Deixe Claude coordenar trabalho contínuo com Projects](https://code.claude.com/docs/pt/claude-projects.md): Dê a Claude um corpo de trabalho relacionado em uma conversa e deixe-o coordenar sessões em nuvem paralelas que compartilham repositórios, instruções e memória.
- [Claude Code no celular](https://code.claude.com/docs/pt/mobile.md): Inicie, monitore e dirija tarefas do Claude Code do seu telefone com o aplicativo Claude para iOS e Android.
- [Use Claude Code with Chrome](https://code.claude.com/docs/pt/chrome.md): Conecte Claude Code ao seu navegador Chrome para testar aplicativos web, depurar com logs de console, automatizar preenchimento de formulários e extrair dados de páginas web.
- [Deixe Claude usar seu computador a partir da CLI](https://code.claude.com/docs/pt/computer-use.md): Ative o computer use na Claude Code CLI para que Claude possa abrir aplicativos, clicar, digitar e ver sua tela no macOS. Teste aplicativos nativos, depure problemas visuais e automatize ferramentas apenas com GUI sem sair do seu terminal.
- [Use Claude Code in VS Code](https://code.claude.com/docs/pt/vs-code.md): Instale e configure a extensão Claude Code para VS Code. Obtenha assistência de codificação com IA com diffs inline, @-mentions, revisão de planos e atalhos de teclado.
- [JetBrains IDEs](https://code.claude.com/docs/pt/jetbrains.md): Use Claude Code with JetBrains IDEs including IntelliJ, PyCharm, WebStorm, and more
- [Claude Code no Slack](https://code.claude.com/docs/pt/slack.md): Delegue tarefas de codificação diretamente do seu espaço de trabalho Slack. A Anthropic está descontinuando esta versão anterior para espaços de trabalho Team e Enterprise em favor do Claude Tag; ela permanece como o caminho de configuração nos planos Pro e Max.
- [Claude Tag](https://code.claude.com/docs/pt/claude-tag.md): Traga Claude para os canais Slack da sua equipe com Claude Tag e encontre a documentação de configuração e uso em claude.com.

##### Claude Code na nuvem

- [Comece com Claude Code na nuvem](https://code.claude.com/docs/pt/web-quickstart.md): Execute Claude Code na nuvem a partir do seu navegador ou telefone. Conecte um repositório GitHub, envie uma tarefa e revise o PR sem configuração local.
- [Use Claude Code na nuvem](https://code.claude.com/docs/pt/claude-code-on-the-web.md): Execute sessões Claude Code na nuvem a partir do seu navegador, telefone, aplicativo desktop ou terminal, mova-as com --cloud e --teleport, e corrija automaticamente pull requests.
- [Automatizar trabalho com rotinas](https://code.claude.com/docs/pt/routines.md): Coloque Claude Code no piloto automático. Defina rotinas que são executadas em um cronograma, acionadas em chamadas de API ou reagem a eventos do GitHub a partir da infraestrutura em nuvem.
- [Encontre bugs com ultrareview](https://code.claude.com/docs/pt/ultrareview.md): Execute uma revisão de código profunda e multi-agente na nuvem com /code-review ultra para encontrar e verificar bugs antes de fazer merge.

##### Claude Code no desktop

- [Comece com o aplicativo de desktop](https://code.claude.com/docs/pt/desktop-quickstart.md): Instale Claude Code no desktop e inicie sua primeira sessão de codificação
- [Aplicativo Desktop](https://code.claude.com/docs/pt/desktop.md): Aproveite ao máximo o Claude Code Desktop: sessões paralelas com isolamento Git, layout de painel com arrastar e soltar, terminal integrado e editor de arquivo, chats laterais, computer use, Dispatch sessions do seu telefone, revisão visual de diff, visualizações de aplicativos, monitoramento de PR,…
- [Claude Desktop no Linux (beta)](https://code.claude.com/docs/pt/desktop-linux.md): Instale e atualize o aplicativo desktop Claude no Ubuntu e Debian
- [Claude Code Desktop em WSL](https://code.claude.com/docs/pt/desktop-wsl.md): Execute sessões de Code dentro de uma distribuição WSL 2 no Windows
- [Agendar tarefas recorrentes no Claude Code Desktop](https://code.claude.com/docs/pt/desktop-scheduled-tasks.md): Configure tarefas agendadas no Claude Code Desktop para executar Claude automaticamente em uma base recorrente para análises de código diárias, auditorias de dependências ou briefings matinais.
- [Testar aplicativos iOS no simulador](https://code.claude.com/docs/pt/desktop-ios-simulator.md): Claude Code Desktop abre seu aplicativo no painel iOS Simulator quando Claude constrói, executa ou verifica, com um simulador separado para cada sessão.

##### Revisão de código e CI/CD

- [Detectar problemas de segurança enquanto Claude escreve código](https://code.claude.com/docs/pt/security-guidance.md): Instale o plugin security-guidance para que Claude revise suas próprias alterações de código em busca de vulnerabilidades e as corrija na mesma sessão.
- [Digitalize seu código em busca de vulnerabilidades](https://code.claude.com/docs/pt/claude-security.md): Instale o plugin Claude Security para digitalizar seu código em busca de vulnerabilidades em uma sessão Claude Code e transforme as descobertas em patches que você revisa e aplica.
- [Code Review](https://code.claude.com/docs/pt/code-review.md): Configure análises automatizadas de PR que detectam erros de lógica, vulnerabilidades de segurança e regressões usando análise multi-agente de sua base de código completa
- [Claude Code GitHub Actions](https://code.claude.com/docs/pt/github-actions.md): Execute Claude Code em fluxos de trabalho do GitHub Actions para responder a menções @claude, automatizar tarefas e transformar issues em pull requests
- [Use Claude Code GitHub Actions com provedores de nuvem](https://code.claude.com/docs/pt/github-actions-cloud-providers.md): Execute Claude Code GitHub Actions através do Amazon Bedrock, Google Cloud's Agent Platform ou Microsoft Foundry em vez da Claude API
- [Claude Code com GitHub Enterprise Server](https://code.claude.com/docs/pt/github-enterprise-server.md): Conecte Claude Code à sua instância auto-hospedada do GitHub Enterprise Server para sessões na nuvem, revisão de código e marketplaces de plugins.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/pt/gitlab-ci-cd.md): Saiba como integrar Claude Code no seu fluxo de trabalho de desenvolvimento com GitLab CI/CD

### Construir com Claude Code

#### Agentes e trabalho paralelo

- [Executar agentes em paralelo](https://code.claude.com/docs/pt/agents.md): Compare as formas como Claude Code pode assumir múltiplas tarefas simultaneamente: subagentes, visualização de agentes, equipes de agentes, workflows dinâmicos e projetos.
- [Criar subagentes personalizados](https://code.claude.com/docs/pt/sub-agents.md): Crie e use subagentes de IA especializados no Claude Code para fluxos de trabalho específicos de tarefas e gerenciamento de contexto aprimorado.
- [Gerenciar múltiplos agentes com agent view](https://code.claude.com/docs/pt/agent-view.md): Despache e gerencie muitas sessões Claude Code a partir de uma tela. Agent view mostra o que cada sessão está fazendo e quais precisam de sua entrada.
- [Orquestre equipes de sessões Claude Code](https://code.claude.com/docs/pt/agent-teams.md): Coordene múltiplas instâncias Claude Code trabalhando juntas como uma equipe, com tarefas compartilhadas, mensagens entre agentes e gerenciamento centralizado.
- [Mensagem para suas outras sessões do Claude Code](https://code.claude.com/docs/pt/cross-session-messaging.md): Deixe Claude listar e enviar mensagens para suas outras sessões do Claude Code nesta máquina, e alcance suas sessões em outras máquinas ou na web.
- [Orquestre subagentos em escala com fluxos de trabalho dinâmicos](https://code.claude.com/docs/pt/workflows.md): Fluxos de trabalho dinâmicos orquestram muitos subagentos a partir de um script que Claude escreve e você pode executar novamente. Use-os para auditorias de base de código, grandes migrações e pesquisa com verificação cruzada.
- [Executar sessões paralelas com worktrees](https://code.claude.com/docs/pt/worktrees.md): Isole sessões paralelas do Claude Code em worktrees git separadas para que as alterações não colidam. Abrange o sinalizador `--worktree`, isolamento de subagentes, `.worktreeinclude`, limpeza e hooks de VCS não-git.

#### MCP

- [Conectar a servidores MCP](https://code.claude.com/docs/pt/mcp-quickstart.md): Adicione um servidor MCP ao Claude Code, verifique a conexão e encontre a configuração no disco.
- [Conectar Claude Code a ferramentas via MCP](https://code.claude.com/docs/pt/mcp.md): Aprenda como conectar Claude Code às suas ferramentas com o Model Context Protocol.

#### Skills

- [Estender Claude com skills](https://code.claude.com/docs/pt/skills.md): Crie, gerencie e compartilhe skills para estender as capacidades do Claude no Claude Code. Inclui comandos personalizados e skills agrupadas.

#### Plugins

- [Descubra e instale plugins pré-construídos através de marketplaces](https://code.claude.com/docs/pt/discover-plugins.md): Encontre e instale plugins de marketplaces para estender Claude Code com novas skills, agentes e capacidades.
- [Criar plugins](https://code.claude.com/docs/pt/plugins.md): Crie plugins personalizados para estender Claude Code com skills, agents, hooks e MCP servers.
- [Testar plugins com evals](https://code.claude.com/docs/pt/plugin-evals.md): Escreva casos de eval para seu plugin Claude Code, execute-os com claude plugin eval, classifique os resultados, compare com uma linha de base sem plugin e gate CI na pontuação.

#### Artefatos

- [Compartilhar saída de sessão como artifacts](https://code.claude.com/docs/pt/artifacts.md): Artifacts transformam o trabalho do Claude Code em páginas ao vivo e interativas no claude.ai que você pode manter privadas, compartilhar com sua organização ou publicar em um link público.

#### Automação

- [Automatizar ações com hooks](https://code.claude.com/docs/pt/hooks-guide.md): Execute comandos shell automaticamente quando Claude Code edita arquivos, conclui tarefas ou precisa de entrada. Formate código, envie notificações, valide comandos e aplique regras do projeto.
- [Enviar eventos para uma sessão em execução com canais](https://code.claude.com/docs/pt/channels.md): Use canais para enviar mensagens, alertas e webhooks para sua sessão Claude Code de um servidor MCP. Encaminhe resultados de CI, mensagens de chat e eventos de monitoramento para que Claude possa reagir enquanto você está ausente.
- [Executar prompts em um cronograma](https://code.claude.com/docs/pt/scheduled-tasks.md): Use /loop e as ferramentas de agendamento cron para executar prompts repetidamente, pesquisar status ou definir lembretes únicos em uma sessão do Claude Code.
- [Manter Claude trabalhando em direção a um objetivo](https://code.claude.com/docs/pt/goal.md): Defina uma condição de conclusão com /goal e Claude continua trabalhando até que seja atendida, um modelo a julgue impossível ou um erro que você tenha que corrigir limpe o objetivo.
- [Executar Claude Code programaticamente](https://code.claude.com/docs/pt/headless.md): Use o Agent SDK para executar Claude Code programaticamente a partir da CLI, Python ou TypeScript.
- [Iniciar sessões a partir de links](https://code.claude.com/docs/pt/deep-links.md): Abra uma sessão de terminal Claude Code a partir de uma URL. Incorpore links `claude-cli://` em runbooks, alertas e dashboards para que um clique abra Claude Code no repositório correto com o prompt correto.

#### Guias

- [Configurar Claude Code em um monorepo ou grande base de código](https://code.claude.com/docs/pt/large-codebases.md): Configure Claude Code para monorepos e grandes bases de código de árvore única com arquivos CLAUDE.md aninhados, worktrees esparsos, inteligência de código e skills por pacote para que Claude permaneça focado no código em que você está trabalhando.

#### Solução de Problemas

- [Solucionar problemas de instalação e login](https://code.claude.com/docs/pt/troubleshoot-install.md): Corrija erros de comando não encontrado, PATH, permissão, rede e autenticação ao instalar ou fazer login no Claude Code.
- [Troubleshooting](https://code.claude.com/docs/pt/troubleshooting.md): Corrija o alto uso de CPU ou memória, travamentos, thrashing de auto-compact e problemas de pesquisa no Claude Code, e encontre a página correta para outros problemas.
- [Depure sua configuração](https://code.claude.com/docs/pt/debug-your-config.md): Diagnostique por que CLAUDE.md, configurações, hooks, servidores MCP ou skills não estão tendo efeito. Use /context, /doctor, /hooks e /mcp para ver o que realmente foi carregado.
- [Referência de erros](https://code.claude.com/docs/pt/errors.md): Procure mensagens de erro de tempo de execução do Claude Code com o que cada uma significa e como corrigi-la.

### Administração

#### Configuração e acesso

- [Configure Claude Code para sua organização](https://code.claude.com/docs/pt/admin-setup.md): Um mapa de decisão para administradores que implantam Claude Code, cobrindo provedores de API, configurações gerenciadas, aplicação de políticas, monitoramento de uso e tratamento de dados.
- [Configuração avançada](https://code.claude.com/docs/pt/setup.md): Requisitos do sistema, instalação específica da plataforma, gerenciamento de versão e desinstalação do Claude Code.
- [Autenticação](https://code.claude.com/docs/pt/authentication.md): Faça login no Claude Code e configure a autenticação para indivíduos, equipes e organizações.
- [Implantar configurações gerenciadas](https://code.claude.com/docs/pt/managed-settings.md): Implante configurações gerenciadas na máquina de cada desenvolvedor: mecanismos de entrega por SO, como Claude Code combina fontes gerenciadas e como verificar a aplicação.
- [Configurar configurações gerenciadas pelo servidor](https://code.claude.com/docs/pt/server-managed-settings.md): Configure centralmente o Claude Code para sua organização através de configurações entregues pelo servidor, sem exigir infraestrutura de gerenciamento de dispositivos.
- [Controle o acesso ao servidor MCP para sua organização](https://code.claude.com/docs/pt/managed-mcp.md): Restrinja quais servidores MCP os usuários podem adicionar ou conectar, ou forneça servidores para cada usuário, com arquivos de configuração gerenciados, configurações gerenciadas, listas de permissão e listas de bloqueio.
- [Configurar modo automático](https://code.claude.com/docs/pt/auto-mode-config.md): Diga ao classificador do modo automático quais repositórios, buckets e domínios sua organização confia. Defina o contexto do ambiente, substitua as regras de bloqueio e permissão padrão e inspecione sua configuração efetiva com os subcomandos da CLI do modo automático.

#### Implantação

- [Visão geral da implantação empresarial](https://code.claude.com/docs/pt/third-party-integrations.md): Saiba como Claude Code pode se integrar com vários serviços de terceiros e infraestrutura para atender aos requisitos de implantação empresarial.
- [Disponibilidade de recursos](https://code.claude.com/docs/pt/feature-availability.md): Compare quais recursos do Claude Code estão disponíveis em planos de assinatura Anthropic, Anthropic Console, Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform e Microsoft Foundry.
- [Claude Code no Amazon Bedrock](https://code.claude.com/docs/pt/amazon-bedrock.md): Saiba como configurar Claude Code através do Amazon Bedrock, incluindo configuração, configuração de IAM e resolução de problemas.
- [Claude Code no Claude Platform on AWS](https://code.claude.com/docs/pt/claude-platform-on-aws.md): Configure Claude Code para usar a API Claude operada pela Anthropic com autenticação AWS, controle de acesso IAM e faturamento do AWS Marketplace.
- [Claude Code na Plataforma de Agentes do Google Cloud](https://code.claude.com/docs/pt/google-vertex-ai.md): Saiba como configurar Claude Code através da Plataforma de Agentes do Google Cloud, anteriormente Vertex AI, incluindo configuração, configuração de IAM e resolução de problemas.
- [Claude Code no Microsoft Foundry](https://code.claude.com/docs/pt/microsoft-foundry.md): Saiba como configurar Claude Code através do Microsoft Foundry, incluindo configuração, instalação e resolução de problemas.
- [Configuração de rede empresarial](https://code.claude.com/docs/pt/network-config.md): Configure Claude Code para ambientes empresariais com servidores proxy, Autoridades de Certificação (CA) personalizadas e autenticação mútua de Transport Layer Security (mTLS).
- [Executar Claude Code atrás de um launcher corporativo](https://code.claude.com/docs/pt/corporate-launcher.md): Rotear os processos que Claude Code inicia a partir de seu próprio binário, incluindo o serviço de fundo e cada sessão de visualização de agente, através de um launcher obrigatório com CLAUDE_CODE_PROCESS_WRAPPER ou a configuração processWrapper.
- [Contêineres de desenvolvimento](https://code.claude.com/docs/pt/devcontainer.md): Execute Claude Code dentro de um contêiner de desenvolvimento para ambientes consistentes e isolados em toda sua equipe.

#### Gateways

- [Executar Claude Code através de um gateway](https://code.claude.com/docs/pt/gateways.md): Rotear Claude Code através de um gateway auto-hospedado para credenciais centralizadas, rastreamento de uso e controles de custo. Abrange a arquitetura, o gateway de aplicativos Claude da Anthropic e o uso de outros produtos de gateway.

##### Gateway de aplicativos Claude

- [Gateway de aplicativos Claude para Amazon Bedrock, Claude Platform on AWS, Google Cloud e Microsoft Foundry](https://code.claude.com/docs/pt/claude-apps-gateway.md): Execute Claude Code através do Amazon Bedrock, Claude Platform on AWS, Google Cloud ou Microsoft Foundry atrás de um gateway auto-hospedado com sign-in SSO, acesso a modelos por grupo e telemetria OTLP.
- [Configuração do gateway de aplicativos Claude](https://code.claude.com/docs/pt/claude-apps-gateway-config.md): Referência para cada opção de gateway.yaml: listener e TLS, OIDC, sessão, armazenamento Postgres, Amazon Bedrock, Claude Platform on AWS, Agent Platform do Google Cloud e upstreams Microsoft Foundry, roteamento de modelos, políticas gerenciadas e telemetria.
- [Limites de gastos do gateway de aplicativos Claude](https://code.claude.com/docs/pt/claude-apps-gateway-spend-limits.md): Limite o gasto de cada desenvolvedor através do gateway de aplicativos Claude por dia, semana ou mês. Defina limites com uma API de administrador e o gateway os aplica em tempo real em cada solicitação.
- [Implantação e operação do gateway de aplicativos Claude](https://code.claude.com/docs/pt/claude-apps-gateway-deploy.md): Registre o gateway com seu IdP, crie o contêiner, implante no Kubernetes ou Cloud Run e o opere: verificações de integridade, rotação de segredos, atualizações e segurança.
- [Implantar gateway de aplicativos Claude na AWS](https://code.claude.com/docs/pt/claude-apps-gateway-on-aws.md): Um exemplo prático de execução do gateway de aplicativos Claude na AWS: ECS Fargate ou EKS, Amazon RDS para PostgreSQL, AWS Secrets Manager e autenticação de função IAM para Amazon Bedrock.
- [Implantar gateway de aplicativos Claude no Google Cloud](https://code.claude.com/docs/pt/claude-apps-gateway-on-gcp.md): Um exemplo prático de execução do gateway de aplicativos Claude no Google Cloud: Cloud Run ou GKE, Cloud SQL para PostgreSQL, Secret Manager e autenticação de conta de serviço para Agent Platform do Google Cloud.

##### Outros gateways

- [Outros gateways LLM](https://code.claude.com/docs/pt/llm-gateway.md): Rotear Claude Code através de um gateway LLM que sua organização já executa. Abrange conectar Claude Code a um gateway, implantar um para sua organização e o que Claude Code envia a um gateway.
- [Conectar Claude Code a um gateway LLM](https://code.claude.com/docs/pt/llm-gateway-connect.md): Aponte Claude Code para o gateway LLM da sua organização. Verifique se seu administrador já o configurou ou defina a URL base e a credencial você mesmo, depois verifique a conexão e corrija erros do gateway.
- [Implante um gateway LLM para sua organização](https://code.claude.com/docs/pt/llm-gateway-rollout.md): Implante um produto de gateway para Claude Code: configure-o para encaminhar o que Claude Code envia, emita credenciais de desenvolvedor, distribua a configuração através de configurações gerenciadas e verifique a implantação.
- [Guia de compatibilidade do gateway Claude Code](https://code.claude.com/docs/pt/llm-gateway-protocol.md): Mantenha um gateway LLM compatível com Claude Code: os endpoints que ele chama, os headers e campos de corpo a encaminhar, e o que quebra quando são removidos.

#### Uso e custos

- [Monitoramento](https://code.claude.com/docs/pt/monitoring-usage.md): Saiba como ativar e configurar OpenTelemetry para Claude Code.
- [Gerencie custos de forma eficaz](https://code.claude.com/docs/pt/costs.md): Rastreie o uso de tokens, defina limites de gastos da equipe e reduza os custos do Claude Code com gerenciamento de contexto, seleção de modelo, configurações de pensamento estendido e hooks de pré-processamento.
- [Rastrear o uso da equipe com análise](https://code.claude.com/docs/pt/analytics.md): Visualize as métricas de uso do Claude Code, rastreie a adoção e meça a velocidade de engenharia no painel de análise.

#### Distribuição de plugins

- [Criar e distribuir um marketplace de plugins](https://code.claude.com/docs/pt/plugin-marketplaces.md): Crie e hospede marketplaces de plugins para distribuir extensões Claude Code em equipes e comunidades.
- [Restringir versões de dependências de plugins](https://code.claude.com/docs/pt/plugin-dependencies.md): Declare restrições de versão em dependências de plugins e agrupe um conjunto de plugins curado atrás de uma única instalação.
- [Recomende seu plugin a partir de sua CLI](https://code.claude.com/docs/pt/plugin-hints.md): Emita um marcador de uma linha a partir de sua CLI para que Claude Code solicite aos usuários que instalem seu plugin oficial.
- [Recomende plugins para sua organização](https://code.claude.com/docs/pt/plugin-relevance.md): Adicione um bloco de relevância às entradas de plugins do marketplace para que Claude Code os sugira quando o trabalho de um usuário corresponder.

#### Segurança e dados

- [Segurança](https://code.claude.com/docs/pt/security.md): Aprenda sobre as proteções de segurança do Claude Code e as melhores práticas para uso seguro.
- [Uso de dados](https://code.claude.com/docs/pt/data-usage.md): Saiba mais sobre as políticas de uso de dados da Anthropic para Claude
- [Retenção zero de dados](https://code.claude.com/docs/pt/zero-data-retention.md): Saiba mais sobre Retenção Zero de Dados (ZDR) para Claude Code, disponível para contas qualificadas no Claude for Enterprise, incluindo escopo, recursos desabilitados e como solicitar ativação.

#### Adoção

- [Kit de comunicações](https://code.claude.com/docs/pt/communications-kit.md): Anúncios de lançamento, mensagens de campanha contínua e respostas de FAQ para implementar Claude Code em sua organização de engenharia.
- [Kit do campeão](https://code.claude.com/docs/pt/champion-kit.md): Um guia prático para engenheiros que defendem Claude Code internamente: o que compartilhar, como responder perguntas e como aumentar a adoção na sua equipe.

### Configuração

#### Configurações

- [Arquivos de configurações e precedência](https://code.claude.com/docs/pt/settings.md): Altere as configurações do Claude Code, escolha o escopo ao qual uma chave pertence, verifique a alteração e aprenda qual valor o Claude Code usa quando uma chave é definida em vários locais.
- [Todas as configurações](https://code.claude.com/docs/pt/settings-reference.md): Referência completa para cada chave settings.json do Claude Code: onde cada uma vai, seu tipo e padrão, e um exemplo pronto para colar, com um índice de cada chave.
- [Arquivos de configuração de exemplo](https://code.claude.com/docs/pt/settings-example.md): Arquivos settings.json realistas para um desenvolvedor, uma equipe e uma organização: copie um, mantenha as chaves que deseja e altere os valores.

#### Permissões e sandboxing

- [Configurar permissões](https://code.claude.com/docs/pt/permissions.md): Controle o que Claude Code pode acessar e fazer com regras de permissão refinadas, modos e políticas gerenciadas.
- [Escolha um modo de permissão](https://code.claude.com/docs/pt/permission-modes.md): Controle se Claude pede permissão antes de agir. Alterne modos de permissão com Shift+Tab na CLI, o indicador de modo no VS Code ou o seletor de modo no Desktop.
- [Configurar a ferramenta Bash em sandbox](https://code.claude.com/docs/pt/sandboxing.md): Aprenda como a ferramenta Bash em sandbox do Claude Code fornece isolamento de sistema de arquivos e rede para execução de agentes mais segura e autônoma.
- [Escolha um ambiente sandbox](https://code.claude.com/docs/pt/sandbox-environments.md): Compare as opções de sandbox do Claude Code: a ferramenta Bash em sandbox integrada, runtime sandbox, dev containers, Docker e VMs. Escolha o isolamento certo para seu modelo de ameaça.

#### Ambientes

- [Configurar ambientes na nuvem](https://code.claude.com/docs/pt/cloud-environments.md): Configure ambientes na nuvem para sessões na nuvem do Claude Code: níveis de acesso à rede, variáveis de ambiente, scripts de configuração e cache de ambiente.

##### Ambientes auto-hospedados

- [Ambientes auto-hospedados](https://code.claude.com/docs/pt/self-hosted-environments.md): Execute sessões de Claude Code na nuvem em infraestrutura que você controla: configure um ambiente auto-hospedado, implante runners e roteie sessões para sua própria computação.
- [Guia de início rápido de ambientes auto-hospedados](https://code.claude.com/docs/pt/self-hosted-environments-quickstart.md): Configure seu primeiro ambiente auto-hospedado: instale Claude Code, crie o ambiente, inicie um runner e roteie uma sessão para ele.
- [Implantar ambientes auto-hospedados em produção](https://code.claude.com/docs/pt/self-hosted-environments-deploy.md): Execute runners auto-hospedados em produção: endurecimento de segurança, controle de saída de rede, credenciais git, receitas Kubernetes e Compose, e solução de problemas.
- [Personalizar sessões em ambientes auto-hospedados](https://code.claude.com/docs/pt/self-hosted-environments-configuration.md): Personalize sessões de ambientes auto-hospedados com scripts wrapper para credenciais por sessão, hooks de ciclo de vida e geração de runners sob demanda.
- [Testar ambientes auto-hospedados de ponta a ponta](https://code.claude.com/docs/pt/self-hosted-environments-testing.md): Verifique uma imagem de executor auto-hospedado a partir de CI: despache uma sessão com a CLI, leia as respostas do Claude através de um hook Stop e execute o loop completo.
- [Referência de ambientes auto-hospedados](https://code.claude.com/docs/pt/self-hosted-environments-reference.md): Referência completa para o executor e orquestrador auto-hospedados: sinalizadores CLI, variáveis de ambiente e métricas Prometheus.
- [Verificar identidade de sessão em ambientes auto-hospedados](https://code.claude.com/docs/pt/self-hosted-environments-identity.md): Verifique o JWT CLAUDE_CODE_SESSION_ACCESS_TOKEN para que os serviços em sua rede possam confiar em solicitações de sessões em seu ambiente auto-hospedado.

#### Modelo e respostas

- [Configuração de modelo](https://code.claude.com/docs/pt/model-config.md): Configure qual modelo Claude Code usa, níveis de esforço, contexto estendido e a janela de auto-compactação
- [Acelere respostas com modo rápido](https://code.claude.com/docs/pt/fast-mode.md): Obtenha respostas mais rápidas do Opus no Claude Code alternando o modo rápido.
- [Escale decisões difíceis com a ferramenta advisor](https://code.claude.com/docs/pt/advisor.md): Combine seu modelo principal com um modelo advisor mais forte que Claude consulta em momentos-chave durante uma tarefa.
- [Estilos de saída](https://code.claude.com/docs/pt/output-styles.md): Adapte Claude Code para usos além da engenharia de software

#### Interface

- [Configure seu terminal para Claude Code](https://code.claude.com/docs/pt/terminal-config.md): Corrija Shift+Enter para novas linhas, obtenha um sinal sonoro do terminal quando Claude terminar, configure tmux, corresponda ao tema de cores e ative o modo Vim na CLI do Claude Code.
- [Renderização em tela cheia](https://code.claude.com/docs/pt/fullscreen.md): Ative um modo de renderização mais suave e sem cintilação com suporte a mouse e uso de memória estável em conversas longas.
- [Use Claude Code com um leitor de tela](https://code.claude.com/docs/pt/accessibility.md): Configure Claude Code para leitores de tela como VoiceOver e NVDA, além de configurações para ampliadores de tela, movimento reduzido e temas amigáveis para daltônicos.
- [Ditado por voz](https://code.claude.com/docs/pt/voice-dictation.md): Fale seus prompts no Claude Code CLI com ditado por voz com manutenção ou toque para gravar.
- [Personalize sua linha de status](https://code.claude.com/docs/pt/statusline.md): Configure uma barra de status personalizada para monitorar o uso da janela de contexto, custos e status do git no Claude Code
- [Personalizar atalhos de teclado](https://code.claude.com/docs/pt/keybindings.md): Personalize atalhos de teclado no Claude Code com um arquivo de configuração de keybindings.

### Referência

#### Referência

- [Referência de CLI](https://code.claude.com/docs/pt/cli-reference.md): Referência completa para a interface de linha de comando Claude Code, incluindo comandos e sinalizadores.
- [Comandos](https://code.claude.com/docs/pt/commands.md): Referência completa para comandos disponíveis no Claude Code, incluindo comandos integrados e skills agrupadas.
- [Variáveis de ambiente](https://code.claude.com/docs/pt/env-vars.md): Referência para variáveis de ambiente que controlam o comportamento do Claude Code.
- [Referência de ferramentas](https://code.claude.com/docs/pt/tools-reference.md): Referência completa das ferramentas que Claude Code pode usar, incluindo requisitos de permissão e comportamento por ferramenta.
- [Modo interativo](https://code.claude.com/docs/pt/interactive-mode.md): Referência completa para atalhos de teclado, modos de entrada e recursos interativos em sessões do Claude Code.
- [Checkpointing](https://code.claude.com/docs/pt/checkpointing.md): Rastreie, reverta e resuma as edições e conversas do Claude para gerenciar o estado da sessão.
- [Referência de hooks](https://code.claude.com/docs/pt/hooks.md): Referência para eventos de hooks do Claude Code, esquema de configuração, formatos de entrada/saída JSON, códigos de saída, hooks assíncronos, hooks HTTP, hooks de prompt e hooks de ferramentas MCP.
- [Referência de plugins](https://code.claude.com/docs/pt/plugins-reference.md): Referência técnica completa para o sistema de plugins do Claude Code, incluindo esquemas, comandos CLI e especificações de componentes.
- [Referência de Channels](https://code.claude.com/docs/pt/channels-reference.md): Construa um servidor MCP que envia webhooks, alertas e mensagens de chat para uma sessão Claude Code. Referência para o contrato de channel: declaração de capacidade, eventos de notificação, ferramentas de resposta, gating de remetente e retransmissão de permissão.

#### Glossário

- [Glossário](https://code.claude.com/docs/pt/glossary.md): Definições da terminologia do Claude Code. Aprenda o que significam agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP e outros conceitos principais.

### Agent SDK

#### Agent SDK

- [Visão geral do Agent SDK](https://code.claude.com/docs/pt/agent-sdk/overview.md): Construa agentes de IA em produção com Claude Code como uma biblioteca
- [Início Rápido](https://code.claude.com/docs/pt/agent-sdk/quickstart.md): Comece com o Agent SDK Python ou TypeScript para construir agentes de IA que funcionam autonomamente
- [Migrar para Claude Agent SDK](https://code.claude.com/docs/pt/agent-sdk/migration-guide.md): Guia para migrar os SDKs TypeScript e Python do Claude Code para o Claude Agent SDK
- [Solucionar problemas do Agent SDK](https://code.claude.com/docs/pt/agent-sdk/troubleshooting.md): Corrija erros do Agent SDK pela mensagem exata que você vê, com a causa e correção para cada erro nos SDKs TypeScript e Python.

#### Criar agentes

- [Configure seu agente](https://code.claude.com/docs/pt/agent-sdk/configuration.md): Configure sessões do Agent SDK: componha o objeto de opções, defina o modelo, ambiente e limites, e encontre a página de cada opção de recurso.
- [Exemplos](https://code.claude.com/docs/pt/agent-sdk/examples.md): Encontre um projeto completo e executável do Agent SDK ou uma receita guiada no Claude Cookbook que corresponda ao que você deseja construir.

#### Conceitos principais

- [Como o loop do agente funciona](https://code.claude.com/docs/pt/agent-sdk/agent-loop.md): Entenda o ciclo de vida das mensagens, execução de ferramentas, janela de contexto e arquitetura que alimentam seus agentes SDK.
- [Use Claude Code features in the SDK](https://code.claude.com/docs/pt/agent-sdk/claude-code-features.md): Load project instructions, skills, hooks, and other Claude Code features into your SDK agents.
- [Trabalhar com sessões](https://code.claude.com/docs/pt/agent-sdk/sessions.md): Como as sessões persistem o histórico de conversas do agente e quando usar continue, resume e fork para retornar a uma execução anterior.
- [Persistir sessões em armazenamento externo](https://code.claude.com/docs/pt/agent-sdk/session-storage.md): Espelhe transcrições de sessão do Agent SDK para seu próprio armazenamento de objetos, armazenamento de chave-valor ou banco de dados para que outros hosts possam retomar suas sessões.

#### Entrada e saída

- [Streaming Input](https://code.claude.com/docs/pt/agent-sdk/streaming-vs-single-mode.md): Compreendendo os dois modos de entrada para Claude Agent SDK e quando usar cada um
- [Lidar com aprovações e entrada do usuário](https://code.claude.com/docs/pt/agent-sdk/user-input.md): Apresente as solicitações de aprovação e perguntas de esclarecimento do Claude aos usuários e retorne suas decisões ao SDK.
- [Transmitir respostas em tempo real](https://code.claude.com/docs/pt/agent-sdk/streaming-output.md): Obtenha respostas em tempo real do Agent SDK conforme o texto e as chamadas de ferramentas são transmitidas
- [Obter saída estruturada de agentes](https://code.claude.com/docs/pt/agent-sdk/structured-outputs.md): Retorne JSON validado de fluxos de trabalho de agentes usando JSON Schema, Zod ou Pydantic. Obtenha dados estruturados e type-safe após o uso de múltiplas ferramentas.

#### Estender com ferramentas

- [Dê a Claude ferramentas personalizadas](https://code.claude.com/docs/pt/agent-sdk/custom-tools.md): Defina ferramentas personalizadas com o servidor MCP em processo do Agent SDK do Claude para que Claude possa chamar suas funções, acessar suas APIs e executar operações específicas do domínio.
- [Conectar a ferramentas externas com MCP](https://code.claude.com/docs/pt/agent-sdk/mcp.md): Configure servidores MCP para estender seu agente com ferramentas externas. Abrange tipos de transporte, busca de ferramentas para grandes conjuntos de ferramentas, autenticação e tratamento de erros.
- [Dimensione para muitas ferramentas com busca de ferramentas](https://code.claude.com/docs/pt/agent-sdk/tool-search.md): Dimensione seu agente para milhares de ferramentas descobrindo e carregando apenas o que é necessário, sob demanda.
- [Subagentes no SDK](https://code.claude.com/docs/pt/agent-sdk/subagents.md): Defina e invoque subagentes para isolar contexto, executar tarefas em paralelo e aplicar instruções especializadas em suas aplicações Claude Agent SDK.

#### Personalizar comportamento

- [Modificando prompts do sistema](https://code.claude.com/docs/pt/agent-sdk/modifying-system-prompts.md): Escolha entre a predefinição `claude_code` e um prompt do sistema personalizado, e personalize o comportamento com CLAUDE.md, estilos de saída, append ou um prompt totalmente personalizado.
- [Estenda agentes com skills](https://code.claude.com/docs/pt/agent-sdk/skills.md): Controle quais skills Claude pode invocar em sessões do Claude Agent SDK, despache comandos por nome e crie skills que suas sessões descobrem
- [Plugins no SDK](https://code.claude.com/docs/pt/agent-sdk/plugins.md): Carregue plugins personalizados para estender Claude Code com skills, agentes, hooks e servidores MCP através do Agent SDK

#### Controle e observabilidade

- [Configurar permissões](https://code.claude.com/docs/pt/agent-sdk/permissions.md): Controle como seu agente usa ferramentas com modos de permissão, hooks e regras declarativas de permissão/negação.
- [Interceptar e controlar o comportamento do agente com hooks](https://code.claude.com/docs/pt/agent-sdk/hooks.md): Interceptar e personalizar o comportamento do agente em pontos-chave de execução com hooks
- [Rewind de alterações de arquivo com checkpointing](https://code.claude.com/docs/pt/agent-sdk/file-checkpointing.md): Rastreie alterações de arquivo durante sessões de agente e restaure arquivos para qualquer estado anterior
- [Rastrear custo e uso](https://code.claude.com/docs/pt/agent-sdk/cost-tracking.md): Aprenda como rastrear o uso de tokens, estimar custos e configurar cache de prompt com o Claude Agent SDK.
- [Observabilidade com OpenTelemetry](https://code.claude.com/docs/pt/agent-sdk/observability.md): Exporte traces, métricas e eventos do Agent SDK para seu backend de observabilidade usando OpenTelemetry.
- [Rastrear tarefas](https://code.claude.com/docs/pt/agent-sdk/todo-tracking.md): Rastreie tarefas em sessões do Agent SDK e renderize o progresso do Claude em sua aplicação a partir de chamadas de ferramentas estruturadas

#### Implantação

- [Hospedagem do Agent SDK](https://code.claude.com/docs/pt/agent-sdk/hosting.md): Implante o Agent SDK em produção: arquitetura de subprocess, persistência de sessão, dimensionamento, observabilidade e isolamento multi-tenant para Docker, Kubernetes e provedores de sandbox.
- [Implantação segura de agentes de IA](https://code.claude.com/docs/pt/agent-sdk/secure-deployment.md): Um guia para proteger implantações do Claude Code e Agent SDK com isolamento, gerenciamento de credenciais e controles de rede

#### Referências do SDK

- [Referência do Agent SDK - TypeScript](https://code.claude.com/docs/pt/agent-sdk/typescript.md): Referência completa da API para o Agent SDK TypeScript, incluindo todas as funções, tipos e interfaces.
- [API de sessão TypeScript SDK V2 (removida)](https://code.claude.com/docs/pt/agent-sdk/typescript-v2-preview.md): Referência para a API de sessão removida V2 do SDK do Agent TypeScript, com padrões de envio/stream baseados em sessão para conversas multi-turno.
- [Referência do Agent SDK - Python](https://code.claude.com/docs/pt/agent-sdk/python.md): Referência completa da API para o Python Agent SDK, incluindo todas as funções, tipos e classes.

### O Que Há de Novo

#### O Que Há de Novo

- [Novidades](https://code.claude.com/docs/pt/whats-new/index.md): Um resumo semanal de recursos notáveis do Claude Code, com trechos de código, demonstrações e contexto sobre por que são importantes.
- [Semana 37 · 7–11 de setembro de 2026](https://code.claude.com/docs/pt/whats-new/2026-w37.md): Teste seus plugins com claude plugin eval e abra painéis do Claude Code Desktop em suas próprias janelas.
- [Semana 36 · 31 de agosto – 4 de setembro de 2026](https://code.claude.com/docs/pt/whats-new/2026-w36.md): Mude para Claude Fable 5.1, deixe o computer use rodar em segundo plano no Desktop e veja as edições do Claude em um painel /diff ao vivo.
- [Semana 35 · 24–28 de agosto de 2026](https://code.claude.com/docs/pt/whats-new/2026-w35.md): Retome sessões de terminal no aplicativo Claude Code Desktop, revise relatórios de feedback que Claude elabora para você e inicie uma sessão em modo restrito.
- [Semana 34 · 17–21 de agosto de 2026](https://code.claude.com/docs/pt/whats-new/2026-w34.md): Crie artboards de UI editáveis com a skill /design, defina o estilo de saída Concise e inicie uma sessão Claude Code na sua máquina a partir do seu telefone.
- [Semana 33 · 10–14 de agosto de 2026](https://code.claude.com/docs/pt/whats-new/2026-w33.md): Claude Code Desktop continua automaticamente após um limite de uso ser redefinido, o modo fork ativa por padrão, e as solicitações de merge do GitLab e marketplaces se juntam ao GitHub.
- [Semana 32 · 3–7 de agosto de 2026](https://code.claude.com/docs/pt/whats-new/2026-w32.md): As sessões do Claude Code se comunicam entre si, ambientes auto-hospedados executam sessões em nuvem em sua infraestrutura, e o modo automático se torna o modo de permissão padrão.
- [Semana 30 · 20–24 de julho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w30.md): Opus 5 torna-se o modelo Opus padrão, Claude Code Desktop adiciona um painel iOS Simulator, e o plugin Claude Security verifica seu código em busca de vulnerabilidades.
- [Semana 29 · 13–17 de julho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w29.md): Puxe dados ao vivo para artefatos publicados através de conectores MCP e use Claude Code com um leitor de tela no novo modo de leitor de tela.
- [Semana 28 · 6–10 de julho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w28.md): Navegue em sites externos pelo navegador integrado do aplicativo Desktop, execute uma verificação completa de configuração com /doctor e aproveite as proteções de transcrição do modo automático e as atualizações da visualização de agentes.
- [Semana 27 · 29 de junho – 3 de julho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w27.md): Claude Sonnet 5 torna-se o modelo padrão, Claude no Chrome atinge disponibilidade geral, subagentes executam em segundo plano por padrão, Claude Desktop chega ao Linux em beta, e /radio sintoniza Claude FM.
- [Semana 26 · 22–26 de junho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w26.md): Autentique servidores MCP a partir do seu shell com claude mcp login, obtenha uma resposta para a saída do comando do modo shell com o prefixo !, e retome uma conversa anterior a /clear com /rewind.
- [Semana 25 · 15–19 de junho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w25.md): Publique uma página ao vivo e compartilhável a partir de sua sessão com Artifacts, corresponda parâmetros de ferramentas em regras deny e ask, e defina qualquer configuração a partir do prompt com /config.
- [Semana 24 · 8–12 de junho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w24.md): Mova uma sessão para um novo diretório com /cd, deixe sub-agentes gerarem seus próprios sub-agentes e solucione problemas de uma configuração quebrada com modo seguro.
- [Semana 23 · 1–5 de junho de 2026](https://code.claude.com/docs/pt/whats-new/2026-w23.md): Execute o modo auto no Amazon Bedrock, na Plataforma de Agentes do Google Cloud e no Microsoft Foundry, solicite confirmação antes de escrever arquivos que podem executar código no modo acceptEdits, liste plugins instalados com /plugin list e exija um intervalo de versão aprovado para implantações g…
- [Semana 22 · 25–29 de maio de 2026](https://code.claude.com/docs/pt/whats-new/2026-w22.md): Execute Claude Code no Claude Opus 4.8, orquestre tarefas grandes com fluxos de trabalho dinâmicos, detecte problemas de segurança com o plugin security-guidance e use o modo rápido no Opus 4.8 a um preço mais baixo.
- [Semana 21 · 18–22 de maio de 2026](https://code.claude.com/docs/pt/whats-new/2026-w21.md): Use o modo automático no plano Pro e com Sonnet 4.6, veja quais skills, subagentes e servidores MCP impulsionam seus limites de plano em /usage, e revise diffs com o novo comando /code-review.
- [Semana 20 · 11–15 de maio de 2026](https://code.claude.com/docs/pt/whats-new/2026-w20.md): Gerencie todas as sessões do Claude Code em uma única tela com a visualização de agentes, mantenha Claude trabalhando em direção a um objetivo até que uma condição seja atendida e execute o modo rápido no Opus 4.7 por padrão.
- [Semana 19 · 4–8 de maio de 2026](https://code.claude.com/docs/pt/whats-new/2026-w19.md): Carregue plugins de arquivos .zip e URLs, pesquise o histórico de comandos em todos os projetos com Ctrl+R, crie novas worktrees a partir do HEAD local ou do padrão remoto, e bloqueie ações incondicionalmente com regras de negação rígida do modo automático.
- [Semana 18 · 27 de abril – 1º de maio de 2026](https://code.claude.com/docs/pt/whats-new/2026-w18.md): Claude Code no Windows funciona sem Git Bash, claude auth login aceita um código OAuth colado quando o callback do navegador não consegue alcançar localhost, claude project purge limpa o estado local por projeto, e colar uma URL de PR em /resume encontra a sessão que a criou.
- [Semana 17 · 20–24 de abril de 2026](https://code.claude.com/docs/pt/whats-new/2026-w17.md): /ultrareview abre como uma visualização de pesquisa, recapitulações automáticas de sessão quando você retorna a um terminal, temas de cores personalizados que você pode criar e enviar em plugins, e um Claude Code redesenhado na web.
- [Semana 16 · 13–17 de abril de 2026](https://code.claude.com/docs/pt/whats-new/2026-w16.md): Claude Opus 4.7 com o novo nível de esforço xhigh, Routines no Claude Code na web, notificações push móveis que alertam seu telefone quando Claude precisa de você, um /usage breakdown que mostra o que está impulsionando seus limites, e binários nativos substituindo o JavaScript agrupado.
- [Semana 15 · 6–10 de abril de 2026](https://code.claude.com/docs/pt/whats-new/2026-w15.md): Planejamento em nuvem Ultraplan, a ferramenta Monitor com /loop auto-pacing, /team-onboarding para empacotar sua configuração, e /autofix-pr do seu terminal.
- [Semana 14 · 30 de março – 3 de abril de 2026](https://code.claude.com/docs/pt/whats-new/2026-w14.md): Computer use na CLI, lições interativas no produto, renderização sem cintilação, substituições de tamanho de resultado MCP por ferramenta e executáveis de plugin no PATH.
- [Semana 13 · 23–27 de março de 2026](https://code.claude.com/docs/pt/whats-new/2026-w13.md): Modo automático para permissões sem intervenção, controle de computador integrado, correção automática de PR na nuvem, busca de transcrição e uma ferramenta PowerShell para Windows.

### Recursos

#### Recursos

- [Legal e conformidade](https://code.claude.com/docs/pt/legal-and-compliance.md): Acordos legais, certificações de conformidade e informações de segurança para Claude Code.

---

## Claude Code Docs: Russian

- 官方原文：https://code.claude.com/docs/_llms/ru.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-ru.md`

# Claude Code Docs: Russian

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Russian

### Начало работы

#### Начало работы

- [Обзор](https://code.claude.com/docs/ru/overview.md): Claude Code — это агентский инструмент кодирования, который читает вашу кодовую базу, редактирует файлы, выполняет команды и интегрируется с вашими инструментами разработки. Доступен в вашем терминале, IDE, приложении для рабочего стола и браузере.
- [Быстрый старт](https://code.claude.com/docs/ru/quickstart.md): Добро пожаловать в Claude Code!
- [Журнал изменений](https://code.claude.com/docs/ru/changelog.md)

#### Основные концепции

- [Как работает Claude Code](https://code.claude.com/docs/ru/how-claude-code-works.md): Поймите агентивный цикл, встроенные инструменты и то, как Claude Code взаимодействует с вашим проектом.
- [Расширение Claude Code](https://code.claude.com/docs/ru/features-overview.md): Узнайте, когда использовать CLAUDE.md, Skills, subagents, hooks, MCP и plugins.
- [Изучите директорию .claude](https://code.claude.com/docs/ru/claude-directory.md): Где Claude Code читает CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules и auto memory. Изучите директорию .claude в вашем проекте и ~/.claude в вашей домашней директории.
- [Изучите контекстное окно](https://code.claude.com/docs/ru/context-window.md): Интерактивная симуляция того, как контекстное окно Claude Code заполняется во время сеанса. Посмотрите, что загружается автоматически, какую стоимость имеет каждое чтение файла и когда срабатывают правила и hooks.
- [Как Claude Code использует prompt caching](https://code.claude.com/docs/ru/prompt-caching.md): Claude Code управляет prompt caching автоматически. Узнайте, почему переключение модели вызывает медленный ход без кэша, что стоит `/compact`, почему изменения CLAUDE.md не применяются во время сеанса и как проверить коэффициент попадания в кэш.

#### Использовать Claude Code

- [Как Claude запоминает ваш проект](https://code.claude.com/docs/ru/memory.md): Дайте Claude постоянные инструкции с помощью файлов CLAUDE.md или AGENTS.md и позвольте Claude автоматически накапливать знания с помощью auto memory.
- [Управление сеансами](https://code.claude.com/docs/ru/sessions.md): Назовите, возобновите, создавайте ветви и переключайтесь между диалогами Claude Code. Охватывает `--continue`, `--resume`, `--from-pr`, средство выбора `/resume`, именование сеансов, экспорт стенограмм и место хранения стенограмм.
- [Распространённые рабочие процессы](https://code.claude.com/docs/ru/common-workflows.md): Пошаговые руководства по изучению кодовых баз, исправлению ошибок, рефакторингу, тестированию и другим повседневным задачам с Claude Code.
- [Библиотека промптов](https://code.claude.com/docs/ru/prompt-library.md): Копируйте и вставляйте промпты для Claude Code, отсортированные по задачам и ролям.
- [Лучшие практики для Claude Code](https://code.claude.com/docs/ru/best-practices.md): Советы и паттерны для максимального использования Claude Code, от настройки окружения до масштабирования на параллельные сеансы.

#### Платформы и интеграции

- [Платформы и интеграции](https://code.claude.com/docs/ru/platforms.md): Выберите, где запустить Claude Code и что к нему подключить. Сравните CLI, Desktop, VS Code, JetBrains, веб, мобильные приложения и интеграции, такие как Chrome, Slack и CI/CD.
- [Продолжайте локальные сеансы с любого устройства с помощью Remote Control](https://code.claude.com/docs/ru/remote-control.md): Продолжайте локальный сеанс Claude Code со своего телефона, планшета или любого браузера, используя Remote Control. Работает с claude.ai/code и мобильным приложением Claude.
- [Позвольте Claude координировать текущую работу с помощью Projects](https://code.claude.com/docs/ru/claude-projects.md): Предоставьте Claude набор связанной работы в одном разговоре и позвольте ему координировать параллельные облачные сеансы, которые совместно используют репозитории, инструкции и память.
- [Claude Code на мобильном устройстве](https://code.claude.com/docs/ru/mobile.md): Запускайте, отслеживайте и управляйте задачами Claude Code со своего телефона с помощью приложения Claude для iOS и Android.
- [Использование Claude Code с Chrome](https://code.claude.com/docs/ru/chrome.md): Подключите Claude Code к браузеру Chrome для тестирования веб-приложений, отладки с помощью логов консоли, автоматизации заполнения форм и извлечения данных со страниц.
- [Позвольте Claude использовать ваш компьютер из CLI](https://code.claude.com/docs/ru/computer-use.md): Включите computer use в Claude Code CLI, чтобы Claude мог открывать приложения, кликать, печатать и видеть ваш экран на macOS. Тестируйте нативные приложения, отлаживайте визуальные проблемы и автоматизируйте инструменты только с GUI без необходимости покидать терминал.
- [Использование Claude Code в VS Code](https://code.claude.com/docs/ru/vs-code.md): Установите и настройте расширение Claude Code для VS Code. Получите помощь AI при кодировании с встроенными diff, @-упоминаниями, проверкой плана и сочетаниями клавиш.
- [JetBrains IDEs](https://code.claude.com/docs/ru/jetbrains.md): Используйте Claude Code с JetBrains IDEs, включая IntelliJ, PyCharm, WebStorm и другие
- [Claude Code в Slack](https://code.claude.com/docs/ru/slack.md): Делегируйте задачи кодирования прямо из вашего рабочего пространства Slack. Anthropic снимает с производства эту более раннюю версию для рабочих пространств Team и Enterprise в пользу Claude Tag; она остается путем настройки для планов Pro и Max.
- [Claude Tag](https://code.claude.com/docs/ru/claude-tag.md): Интегрируйте Claude в каналы Slack вашей команды с помощью Claude Tag и найдите документацию по его настройке и использованию на claude.com.

##### Claude Code в облаке

- [Начало работы с Claude Code в облаке](https://code.claude.com/docs/ru/web-quickstart.md): Запустите Claude Code в облаке из браузера или мобильного приложения. Подключите репозиторий GitHub, отправьте задачу и просмотрите PR без локальной настройки.
- [Использование Claude Code в облаке](https://code.claude.com/docs/ru/claude-code-on-the-web.md): Запускайте сессии Claude Code в облаке из браузера, телефона, настольного приложения или терминала, перемещайте их с помощью --cloud и --teleport, а также автоматически исправляйте pull requests.
- [Автоматизация работы с помощью рутин](https://code.claude.com/docs/ru/routines.md): Переведите Claude Code на автопилот. Определите рутины, которые запускаются по расписанию, срабатывают при вызовах API или реагируют на события GitHub из облачной инфраструктуры.
- [Поиск ошибок с помощью ultrareview](https://code.claude.com/docs/ru/ultrareview.md): Запустите глубокий многоагентный анализ кода в облаке с помощью /code-review ultra, чтобы найти и проверить ошибки перед слиянием.

##### Claude Code на рабочем столе

- [Начало работы с настольным приложением](https://code.claude.com/docs/ru/desktop-quickstart.md): Установите Claude Code на рабочий стол и начните свой первый сеанс кодирования
- [Настольное приложение](https://code.claude.com/docs/ru/desktop.md): Получите больше возможностей от Claude Code Desktop: параллельные сеансы с изоляцией Git, макет панелей с перетаскиванием, интегрированный терминал и редактор файлов, боковые чаты, использование компьютера, отправка сеансов со своего телефона, визуальный просмотр различий, предпросмотр приложений, м…
- [Claude Desktop на Linux (бета)](https://code.claude.com/docs/ru/desktop-linux.md): Установка и обновление приложения Claude Desktop на Ubuntu и Debian
- [Claude Code Desktop в WSL](https://code.claude.com/docs/ru/desktop-wsl.md): Запуск сеансов Code внутри дистрибутива WSL 2 на Windows
- [Планирование повторяющихся задач в Claude Code Desktop](https://code.claude.com/docs/ru/desktop-scheduled-tasks.md): Настройте запланированные задачи в Claude Code Desktop для автоматического запуска Claude на регулярной основе для ежедневных проверок кода, аудитов зависимостей или утренних брифингов.
- [Тестирование iOS приложений в симуляторе](https://code.claude.com/docs/ru/desktop-ios-simulator.md): Claude Code Desktop открывает ваше приложение в панели iOS Simulator при сборке, запуске или проверке, с отдельным симулятором для каждой сессии.

##### Проверка кода и CI/CD

- [Выявляйте проблемы безопасности по мере написания кода Claude](https://code.claude.com/docs/ru/security-guidance.md): Установите плагин security-guidance, чтобы Claude проверял собственные изменения кода на уязвимости и исправлял их в одном сеансе.
- [Сканируйте вашу кодовую базу на уязвимости](https://code.claude.com/docs/ru/claude-security.md): Установите Claude Security plugin для сканирования вашей кодовой базы на уязвимости в сеансе Claude Code и преобразуйте результаты в патчи, которые вы проверяете и применяете.
- [Code Review](https://code.claude.com/docs/ru/code-review.md): Настройте автоматизированные проверки PR, которые выявляют логические ошибки, уязвимости безопасности и регрессии с помощью многоагентного анализа всей вашей кодовой базы
- [Claude Code GitHub Actions](https://code.claude.com/docs/ru/github-actions.md): Запускайте Claude Code в рабочих процессах GitHub Actions для ответа на упоминания @claude, автоматизации задач и преобразования issues в pull requests
- [Использование Claude Code GitHub Actions с облачными провайдерами](https://code.claude.com/docs/ru/github-actions-cloud-providers.md): Запускайте Claude Code GitHub Actions через Amazon Bedrock, Google Cloud's Agent Platform или Microsoft Foundry вместо Claude API
- [Claude Code с GitHub Enterprise Server](https://code.claude.com/docs/ru/github-enterprise-server.md): Подключите Claude Code к вашему самостоятельно размещённому экземпляру GitHub Enterprise Server для облачных сессий, проверки кода и маркетплейсов плагинов.
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/ru/gitlab-ci-cd.md): Узнайте об интеграции Claude Code в ваш рабочий процесс разработки с GitLab CI/CD

### Разработка с Claude Code

#### Агенты и параллельная работа

- [Запуск агентов параллельно](https://code.claude.com/docs/ru/agents.md): Сравните способы, которыми Claude Code может выполнять несколько задач одновременно: подагенты, представление агентов, команды агентов, динамические рабочие процессы и проекты.
- [Создание пользовательских subagents](https://code.claude.com/docs/ru/sub-agents.md): Создавайте и используйте специализированные AI subagents в Claude Code для рабочих процессов, ориентированных на конкретные задачи, и улучшенного управления контекстом.
- [Управление несколькими агентами с помощью agent view](https://code.claude.com/docs/ru/agent-view.md): Отправляйте и управляйте множеством сеансов Claude Code с одного экрана. Agent view показывает, что делает каждый сеанс и какие из них требуют вашего ввода.
- [Координируйте команды сеансов Claude Code](https://code.claude.com/docs/ru/agent-teams.md): Координируйте несколько экземпляров Claude Code, работающих вместе как команда, с общими задачами, обменом сообщениями между агентами и централизованным управлением.
- [Отправляйте сообщения другим сеансам Claude Code](https://code.claude.com/docs/ru/cross-session-messaging.md): Позвольте Claude перечислить и отправить сообщения другим вашим сеансам Claude Code на этом компьютере, а также достичь ваши сеансы на других компьютерах или в веб-версии.
- [Оркестрируйте множество подагентов с помощью динамических workflows](https://code.claude.com/docs/ru/workflows.md): Dynamic workflows оркестрируют множество подагентов из скрипта, который пишет Claude, и вы можете его переиспользовать. Используйте их для аудитов кодовой базы, крупных миграций и перекрёстной проверки исследований.
- [Запуск параллельных сеансов с worktrees](https://code.claude.com/docs/ru/worktrees.md): Изолируйте параллельные сеансы Claude Code в отдельных git worktrees, чтобы изменения не конфликтовали. Охватывает флаг `--worktree`, изоляцию subagent, `.worktreeinclude`, очистку и hooks для не-git VCS.

#### MCP

- [Подключение к серверам MCP](https://code.claude.com/docs/ru/mcp-quickstart.md): Добавьте сервер MCP в Claude Code, проверьте соединение и найдите конфигурацию на диске.
- [Подключите Claude Code к инструментам через MCP](https://code.claude.com/docs/ru/mcp.md): Узнайте, как подключить Claude Code к вашим инструментам с помощью Model Context Protocol.

#### Навыки

- [Расширение Claude с помощью skills](https://code.claude.com/docs/ru/skills.md): Создавайте, управляйте и делитесь skills для расширения возможностей Claude в Claude Code. Включает пользовательские команды и встроенные skills.

#### Плагины

- [Откройте и установите готовые плагины через маркетплейсы](https://code.claude.com/docs/ru/discover-plugins.md): Найдите и установите плагины из маркетплейсов, чтобы расширить Claude Code новыми skills, agents и возможностями.
- [Создание plugins](https://code.claude.com/docs/ru/plugins.md): Создавайте пользовательские plugins для расширения Claude Code с помощью skills, agents, hooks и MCP servers.
- [Тестирование plugins с помощью evals](https://code.claude.com/docs/ru/plugin-evals.md): Напишите eval-кейсы для вашего Claude Code plugin, запустите их с помощью claude plugin eval, оцените результаты, сравните с базовым вариантом без plugin и установите ограничение CI на основе оценки.

#### Артефакты

- [Поделитесь выходом сеанса как артефактами](https://code.claude.com/docs/ru/artifacts.md): Артефакты превращают работу Claude Code в живые интерактивные страницы на claude.ai, которые вы можете хранить в приватном режиме, делиться с вашей организацией или публиковать по общедоступной ссылке.

#### Автоматизация

- [Автоматизация действий с помощью hooks](https://code.claude.com/docs/ru/hooks-guide.md): Запускайте команды оболочки автоматически, когда Claude Code редактирует файлы, завершает задачи или требует ввода. Форматируйте код, отправляйте уведомления, проверяйте команды и применяйте правила проекта.
- [Отправка событий в активный сеанс через каналы](https://code.claude.com/docs/ru/channels.md): Используйте каналы для отправки сообщений, оповещений и вебхуков в ваш сеанс Claude Code из MCP-сервера. Перенаправляйте результаты CI, сообщения чата и события мониторинга, чтобы Claude мог реагировать, пока вас нет.
- [Запуск подсказок по расписанию](https://code.claude.com/docs/ru/scheduled-tasks.md): Используйте /loop и инструменты планирования cron для повторного запуска подсказок, опроса статуса или установки одноразовых напоминаний в сеансе Claude Code.
- [Держите Claude в работе над целью](https://code.claude.com/docs/ru/goal.md): Установите условие завершения с помощью /goal, и Claude будет работать над его достижением, пока условие не будет выполнено, модель не сочтет его невозможным или ошибка, которую вам нужно исправить, не очистит цель.
- [Запуск Claude Code программно](https://code.claude.com/docs/ru/headless.md): Используйте Agent SDK для программного запуска Claude Code из CLI, Python или TypeScript.
- [Запуск сеансов по ссылкам](https://code.claude.com/docs/ru/deep-links.md): Откройте сеанс терминала Claude Code по URL. Встраивайте ссылки `claude-cli://` в runbook'и, оповещения и панели мониторинга, чтобы при клике открывался Claude Code в нужном репозитории с нужным приглашением.

#### Руководства

- [Настройка Claude Code в монорепозитории или большой кодовой базе](https://code.claude.com/docs/ru/large-codebases.md): Настройте Claude Code для монорепозиториев и больших однодеревных кодовых баз с вложенными файлами CLAUDE.md, разреженными worktrees, интеллектом кода и навыками для каждого пакета, чтобы Claude оставался сосредоточенным на коде, над которым вы работаете.

#### Устранение неполадок

- [Устранение неполадок при установке и входе](https://code.claude.com/docs/ru/troubleshoot-install.md): Исправьте ошибки command not found, PATH, разрешений, сети и аутентификации при установке или входе в Claude Code.
- [Troubleshooting](https://code.claude.com/docs/ru/troubleshooting.md): Исправьте высокое использование CPU или памяти, зависания, auto-compact thrashing и проблемы поиска в Claude Code, и найдите нужную страницу для других проблем.
- [Отладка конфигурации](https://code.claude.com/docs/ru/debug-your-config.md): Диагностируйте, почему CLAUDE.md, параметры, hooks, MCP серверы или skills не вступают в силу. Используйте /context, /doctor, /hooks и /mcp, чтобы увидеть, что действительно загрузилось.
- [Справочник по ошибкам](https://code.claude.com/docs/ru/errors.md): Найдите сообщения об ошибках Claude Code с объяснением их значения и способов исправления.

### Администрирование

#### Настройка и доступ

- [Настройка Claude Code для вашей организации](https://code.claude.com/docs/ru/admin-setup.md): Карта решений для администраторов, развертывающих Claude Code, охватывающая поставщиков API, управляемые параметры, принудительное применение политики, мониторинг использования и обработку данных.
- [Расширенная настройка](https://code.claude.com/docs/ru/setup.md): Системные требования, установка для конкретной платформы, управление версиями и удаление Claude Code.
- [Аутентификация](https://code.claude.com/docs/ru/authentication.md): Войдите в Claude Code и настройте аутентификацию для отдельных пользователей, команд и организаций.
- [Развертывание управляемых параметров](https://code.claude.com/docs/ru/managed-settings.md): Развертывайте управляемые параметры на машину каждого разработчика: механизмы доставки для каждой ОС, как Claude Code объединяет управляемые источники и как проверить применение политики.
- [Настройка параметров, управляемых сервером](https://code.claude.com/docs/ru/server-managed-settings.md): Централизованно настраивайте Claude Code для вашей организации через параметры, доставляемые сервером, без необходимости инфраструктуры управления устройствами.
- [Контролируйте доступ к серверам MCP для вашей организации](https://code.claude.com/docs/ru/managed-mcp.md): Ограничьте, какие серверы MCP пользователи могут добавлять или подключать, или предоставьте серверы каждому пользователю с помощью управляемых файлов конфигурации, управляемых параметров, списков разрешений и списков запретов.
- [Настройка режима auto](https://code.claude.com/docs/ru/auto-mode-config.md): Сообщите классификатору режима auto, какие репозитории, бакеты и домены доверяет ваша организация. Установите контекст окружения, переопределите правила блокировки и разрешения по умолчанию и проверьте вашу эффективную конфигурацию с помощью подкоманд CLI auto-mode.

#### Развертывание

- [Обзор корпоративного развертывания](https://code.claude.com/docs/ru/third-party-integrations.md): Узнайте, как Claude Code может интегрироваться с различными сторонними сервисами и инфраструктурой для удовлетворения требований корпоративного развертывания.
- [Доступность функций](https://code.claude.com/docs/ru/feature-availability.md): Сравните, какие функции Claude Code доступны в планах подписки Anthropic, Anthropic Console, Amazon Bedrock, Claude Platform на AWS, Google Cloud's Agent Platform и Microsoft Foundry.
- [Claude Code на Amazon Bedrock](https://code.claude.com/docs/ru/amazon-bedrock.md): Узнайте о настройке Claude Code через Amazon Bedrock, включая установку, конфигурацию IAM и устранение неполадок.
- [Claude Code на Claude Platform on AWS](https://code.claude.com/docs/ru/claude-platform-on-aws.md): Настройте Claude Code для использования API Claude, управляемого Anthropic, с аутентификацией AWS, контролем доступа IAM и выставлением счетов через AWS Marketplace.
- [Claude Code на Google Cloud's Agent Platform](https://code.claude.com/docs/ru/google-vertex-ai.md): Узнайте о настройке Claude Code через Google Cloud's Agent Platform, ранее известную как Vertex AI, включая установку, конфигурацию IAM и устранение неполадок.
- [Claude Code на Microsoft Foundry](https://code.claude.com/docs/ru/microsoft-foundry.md): Узнайте о настройке Claude Code через Microsoft Foundry, включая установку, конфигурацию и устранение неполадок.
- [Конфигурация сети для предприятия](https://code.claude.com/docs/ru/network-config.md): Настройте Claude Code для корпоративных сред с прокси-серверами, пользовательскими центрами сертификации (CA) и взаимной аутентификацией Transport Layer Security (mTLS).
- [Запуск Claude Code через корпоративный launcher](https://code.claude.com/docs/ru/corporate-launcher.md): Маршрутизируйте процессы, которые Claude Code запускает из собственного бинарного файла, включая фоновый сервис и каждый сеанс agent view, через требуемый launcher с помощью CLAUDE_CODE_PROCESS_WRAPPER или параметра processWrapper.
- [Контейнеры разработки](https://code.claude.com/docs/ru/devcontainer.md): Запустите Claude Code внутри контейнера разработки для согласованных, изолированных сред во всей вашей команде.

#### Шлюзы

- [Запуск Claude Code через шлюз](https://code.claude.com/docs/ru/gateways.md): Маршрутизируйте Claude Code через самостоятельно размещаемый шлюз для централизованного управления учетными данными, отслеживания использования и контроля затрат. Охватывает архитектуру, шлюз Claude apps от Anthropic и использование других продуктов шлюзов.

##### Шлюз приложений Claude

- [Шлюз Claude apps для Amazon Bedrock, Claude Platform на AWS, Google Cloud и Microsoft Foundry](https://code.claude.com/docs/ru/claude-apps-gateway.md): Запускайте Claude Code через Amazon Bedrock, Claude Platform на AWS, Google Cloud или Microsoft Foundry за самостоятельно размещаемым шлюзом с входом SSO, доступом к моделям по группам и телеметрией OTLP.
- [Конфигурация Claude apps gateway](https://code.claude.com/docs/ru/claude-apps-gateway-config.md): Справочник по каждому параметру gateway.yaml: listener и TLS, OIDC, session, хранилище Postgres, upstreams Amazon Bedrock, Claude Platform на AWS, Agent Platform Google Cloud и Microsoft Foundry, маршрутизация моделей, управляемые политики и телеметрия.
- [Лимиты расходов Claude apps gateway](https://code.claude.com/docs/ru/claude-apps-gateway-spend-limits.md): Ограничьте расходы каждого разработчика через Claude apps gateway по дням, неделям или месяцам. Установите лимиты с помощью Admin API, и шлюз будет их соблюдать в реальном времени при каждом запросе.
- [Развертывание и эксплуатация шлюза Claude apps](https://code.claude.com/docs/ru/claude-apps-gateway-deploy.md): Зарегистрируйте шлюз в вашем поставщике идентификации, создайте контейнер, разверните на Kubernetes или Cloud Run и управляйте им: проверки здоровья, ротация секретов, обновления и безопасность.
- [Развёртывание Claude apps gateway на AWS](https://code.claude.com/docs/ru/claude-apps-gateway-on-aws.md): Практический пример запуска Claude apps gateway на AWS: ECS Fargate или EKS, Amazon RDS для PostgreSQL, AWS Secrets Manager и аутентификация на основе IAM-роли к Amazon Bedrock.
- [Развертывание Claude apps gateway на Google Cloud](https://code.claude.com/docs/ru/claude-apps-gateway-on-gcp.md): Практический пример запуска Claude apps gateway на Google Cloud: Cloud Run или GKE, Cloud SQL для PostgreSQL, Secret Manager и аутентификация через сервисный аккаунт для Agent Platform Google Cloud.

##### Другие шлюзы

- [Другие LLM gateways](https://code.claude.com/docs/ru/llm-gateway.md): Маршрутизируйте Claude Code через LLM gateway, который уже запускает ваша организация. Охватывает подключение Claude Code к шлюзу, развертывание шлюза для вашей организации и то, что Claude Code отправляет на шлюз.
- [Подключение Claude Code к шлюзу LLM](https://code.claude.com/docs/ru/llm-gateway-connect.md): Направьте Claude Code на шлюз LLM вашей организации. Проверьте, уже ли администратор его настроил, или установите базовый URL и учетные данные самостоятельно, затем проверьте соединение и исправьте ошибки шлюза.
- [Развертывание LLM-шлюза для вашей организации](https://code.claude.com/docs/ru/llm-gateway-rollout.md): Разверните продукт шлюза для Claude Code: настройте его для перенаправления того, что отправляет Claude Code, выдайте учетные данные разработчика, распределите конфигурацию через управляемые параметры и проверьте развертывание.
- [Руководство совместимости Claude Code gateway](https://code.claude.com/docs/ru/llm-gateway-protocol.md): Поддерживайте совместимость LLM gateway с Claude Code: конечные точки, которые он вызывает, заголовки и поля тела, которые необходимо передавать, и что перестает работать при их удалении.

#### Использование и затраты

- [Мониторинг](https://code.claude.com/docs/ru/monitoring-usage.md): Узнайте, как включить и настроить OpenTelemetry для Claude Code.
- [Эффективное управление затратами](https://code.claude.com/docs/ru/costs.md): Отслеживайте использование токенов, устанавливайте лимиты расходов команды и снижайте затраты Claude Code с помощью управления контекстом, выбора модели, настроек расширенного мышления и предварительной обработки hooks.
- [Отслеживание использования команды с помощью аналитики](https://code.claude.com/docs/ru/analytics.md): Просмотрите метрики использования Claude Code, отслеживайте внедрение и измеряйте скорость разработки на панели аналитики.

#### Распространение плагинов

- [Создание и распространение marketplace плагинов](https://code.claude.com/docs/ru/plugin-marketplaces.md): Создавайте и размещайте marketplace плагинов для распространения расширений Claude Code по командам и сообществам.
- [Ограничение версий зависимостей плагина](https://code.claude.com/docs/ru/plugin-dependencies.md): Объявляйте ограничения версий для зависимостей плагина и объедините подобранный набор плагинов в одну установку.
- [Рекомендуйте ваш плагин из вашего CLI](https://code.claude.com/docs/ru/plugin-hints.md): Выведите однострочный маркер из вашего CLI, чтобы Claude Code предложил пользователям установить ваш официальный плагин.
- [Рекомендуйте plugins для вашей организации](https://code.claude.com/docs/ru/plugin-relevance.md): Добавьте блок relevance к записям plugins на marketplace, чтобы Claude Code предлагал их, когда работа пользователя совпадает.

#### Безопасность и данные

- [Безопасность](https://code.claude.com/docs/ru/security.md): Узнайте о защитных механизмах Claude Code и лучших практиках безопасного использования.
- [Использование данных](https://code.claude.com/docs/ru/data-usage.md): Узнайте о политике использования данных Anthropic для Claude
- [Нулевое хранение данных](https://code.claude.com/docs/ru/zero-data-retention.md): Узнайте о нулевом хранении данных (ZDR) для Claude Code, доступном для квалифицированных учетных записей на Claude for Enterprise, включая область применения, отключенные функции и способы запроса активации.

#### Внедрение

- [Коммуникационный набор](https://code.claude.com/docs/ru/communications-kit.md): Объявления о запуске, сообщения для капельной кампании и ответы на часто задаваемые вопросы для развертывания Claude Code в вашей инженерной организации.
- [Набор инструментов чемпиона](https://code.claude.com/docs/ru/champion-kit.md): Руководство для инженеров, продвигающих Claude Code внутри организации: что делиться, как отвечать на вопросы и как увеличить внедрение в вашей команде.

### Конфигурация

#### Параметры

- [Файлы параметров и приоритет](https://code.claude.com/docs/ru/settings.md): Измените параметры Claude Code, выберите область, к которой принадлежит ключ, проверьте изменение и узнайте, какое значение Claude Code использует, когда ключ установлен в нескольких местах.
- [Все параметры](https://code.claude.com/docs/ru/settings-reference.md): Полный справочник по каждому ключу settings.json в Claude Code: где находится каждый ключ, его тип и значение по умолчанию, а также готовый к использованию пример и индекс всех ключей.
- [Примеры файлов settings](https://code.claude.com/docs/ru/settings-example.md): Реалистичные файлы settings.json для разработчика, команды и организации: скопируйте один, оставьте нужные вам ключи и измените значения.

#### Разрешения и sandboxing

- [Настройка разрешений](https://code.claude.com/docs/ru/permissions.md): Контролируйте, что Claude Code может использовать и делать, с помощью детальных правил разрешений, режимов и управляемых политик.
- [Выберите режим разрешений](https://code.claude.com/docs/ru/permission-modes.md): Контролируйте, будет ли Claude просить разрешение перед редактированием файлов или выполнением команд. Переключайте режимы с помощью Shift+Tab в CLI, индикатора режима в VS Code или селектора режима в Desktop.
- [Настройка изолированного инструмента Bash](https://code.claude.com/docs/ru/sandboxing.md): Узнайте, как изолированный инструмент Bash в Claude Code обеспечивает изоляцию файловой системы и сети для более безопасного и автономного выполнения агента.
- [Выберите среду sandbox](https://code.claude.com/docs/ru/sandbox-environments.md): Сравните варианты sandbox для Claude Code: встроенный инструмент Bash в песочнице, среда выполнения sandbox, контейнеры разработки, Docker и виртуальные машины. Выберите правильную изоляцию для вашей модели угроз.

#### Окружения

- [Настройка облачных сред](https://code.claude.com/docs/ru/cloud-environments.md): Настройте облачные среды для облачных сеансов Claude Code: уровни доступа в сети, переменные окружения, скрипты настройки и кэширование среды.

##### Самостоятельно размещаемые окружения

- [Самостоятельно размещаемые окружения](https://code.claude.com/docs/ru/self-hosted-environments.md): Запускайте сеансы Claude Code в облаке на инфраструктуре, которой вы управляете: настройте самостоятельно размещаемое окружение, разверните runners и маршрутизируйте сеансы на собственные вычислительные ресурсы.
- [Быстрый старт для самостоятельно размещаемых окружений](https://code.claude.com/docs/ru/self-hosted-environments-quickstart.md): Настройте своё первое самостоятельно размещаемое окружение: установите Claude Code, создайте окружение, запустите runner и маршрутизируйте сеанс на него.
- [Развертывание самостоятельно размещаемых окружений в production](https://code.claude.com/docs/ru/self-hosted-environments-deploy.md): Запуск самостоятельно размещаемых runners в production: усиление безопасности, контроль сетевого исходящего трафика, учетные данные git, рецепты Kubernetes и Compose, а также устранение неполадок.
- [Настройка сеансов в самостоятельно размещаемых окружениях](https://code.claude.com/docs/ru/self-hosted-environments-configuration.md): Настройте сеансы самостоятельно размещаемого окружения с помощью скриптов-оболочек для учетных данных для каждого сеанса, хуков жизненного цикла и порождения средств выполнения по требованию.
- [Тестирование самостоятельно размещённых сред от начала до конца](https://code.claude.com/docs/ru/self-hosted-environments-testing.md): Проверьте образ самостоятельно размещённого runner из CI: отправьте сеанс через CLI, прочитайте ответы Claude через hook Stop и напишите скрипт для полного цикла.
- [Справочник самостоятельно размещаемых окружений](https://code.claude.com/docs/ru/self-hosted-environments-reference.md): Полный справочник по самостоятельно размещаемому runner и orchestrator: флаги CLI, переменные окружения и метрики Prometheus.
- [Проверка идентификации сеанса в самостоятельно размещаемых окружениях](https://code.claude.com/docs/ru/self-hosted-environments-identity.md): Проверьте JWT CLAUDE_CODE_SESSION_ACCESS_TOKEN, чтобы сервисы в вашей сети могли доверять запросам от сеансов в вашем самостоятельно размещаемом окружении.

#### Модель и ответы

- [Конфигурация модели](https://code.claude.com/docs/ru/model-config.md): Настройте, какую модель использует Claude Code, уровни усилий, расширенный контекст и окно auto-compact
- [Ускорьте ответы с помощью быстрого режима](https://code.claude.com/docs/ru/fast-mode.md): Получайте более быстрые ответы Opus в Claude Code, включив быстрый режим.
- [Эскалация сложных решений с помощью инструмента advisor](https://code.claude.com/docs/ru/advisor.md): Объедините вашу основную модель с более мощной моделью-советником, которую Claude консультирует в ключевые моменты выполнения задачи.
- [Output styles](https://code.claude.com/docs/ru/output-styles.md): Адаптируйте Claude Code для использования за пределами разработки программного обеспечения

#### Интерфейс

- [Настройте ваш терминал для Claude Code](https://code.claude.com/docs/ru/terminal-config.md): Исправьте Shift+Enter для новых строк, получайте звуковой сигнал терминала при завершении Claude, настройте tmux, сопоставьте цветовую схему и включите режим Vim в CLI Claude Code.
- [Полноэкранный рендеринг](https://code.claude.com/docs/ru/fullscreen.md): Включите более плавный режим рендеринга без мерцания с поддержкой мыши и стабильным использованием памяти в длительных разговорах.
- [Использование Claude Code с программой чтения с экрана](https://code.claude.com/docs/ru/accessibility.md): Настройте Claude Code для программ чтения с экрана, таких как VoiceOver и NVDA, а также параметры для увеличения экрана, уменьшения движения и тем, удобных для дальтоников.
- [Голосовой ввод](https://code.claude.com/docs/ru/voice-dictation.md): Произносите свои запросы в Claude Code CLI с помощью удержания или нажатия для записи голоса.
- [Настройка строки состояния](https://code.claude.com/docs/ru/statusline.md): Настройте пользовательскую строку состояния для мониторинга использования контекстного окна, затрат и статуса git в Claude Code
- [Настройка сочетаний клавиш](https://code.claude.com/docs/ru/keybindings.md): Настройте сочетания клавиш в Claude Code с помощью файла конфигурации keybindings.

### Справочник

#### Справочник

- [Справочник CLI](https://code.claude.com/docs/ru/cli-reference.md): Полный справочник по интерфейсу командной строки Claude Code, включая команды и флаги.
- [Команды](https://code.claude.com/docs/ru/commands.md): Полный справочник команд, доступных в Claude Code, включая встроенные команды и встроенные skills.
- [Переменные окружения](https://code.claude.com/docs/ru/env-vars.md): Справочник по переменным окружения, которые управляют поведением Claude Code.
- [Справочник инструментов](https://code.claude.com/docs/ru/tools-reference.md): Полный справочник по инструментам, которые может использовать Claude Code, включая требования к разрешениям и поведение каждого инструмента.
- [Интерактивный режим](https://code.claude.com/docs/ru/interactive-mode.md): Полный справочник по сочетаниям клавиш, режимам ввода и интерактивным функциям в сеансах Claude Code.
- [Checkpointing](https://code.claude.com/docs/ru/checkpointing.md): Отслеживайте, перематывайте и суммируйте правки и беседу Claude для управления состоянием сеанса.
- [Справочник по hooks](https://code.claude.com/docs/ru/hooks.md): Справочник по событиям hook Claude Code, схеме конфигурации, форматам JSON входа/выхода, кодам выхода, асинхронным hooks, HTTP hooks, prompt hooks и MCP tool hooks.
- [Справочник по plugins](https://code.claude.com/docs/ru/plugins-reference.md): Полный технический справочник по системе plugins Claude Code, включая схемы, команды CLI и спецификации компонентов.
- [Справочник по каналам](https://code.claude.com/docs/ru/channels-reference.md): Создайте MCP-сервер, который отправляет вебхуки, оповещения и сообщения чата в сеанс Claude Code. Справочник по контракту канала: объявление возможностей, события уведомлений, инструменты ответа, проверка отправителя и трансляция разрешений.

#### Глоссарий

- [Глоссарий](https://code.claude.com/docs/ru/glossary.md): Определения терминологии Claude Code. Узнайте, что означают agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP и другие основные концепции.

### Agent SDK

#### Agent SDK

- [Обзор Agent SDK](https://code.claude.com/docs/ru/agent-sdk/overview.md): Создавайте производственные AI-агентов с Claude Code как библиотеку
- [Быстрый старт](https://code.claude.com/docs/ru/agent-sdk/quickstart.md): Начните работу с Python или TypeScript Agent SDK для создания AI-агентов, которые работают автономно
- [Миграция на Claude Agent SDK](https://code.claude.com/docs/ru/agent-sdk/migration-guide.md): Руководство по миграции Claude Code TypeScript и Python SDK на Claude Agent SDK
- [Устранение неполадок Agent SDK](https://code.claude.com/docs/ru/agent-sdk/troubleshooting.md): Исправьте ошибки Agent SDK по точному сообщению об ошибке, с указанием причины и способа исправления для каждой ошибки в TypeScript и Python SDK.

#### Создание агентов

- [Настройка вашего агента](https://code.claude.com/docs/ru/agent-sdk/configuration.md): Настройте сеансы Agent SDK: составьте объект параметров, установите модель, окружение и ограничения, и найдите страницу каждого параметра функции.
- [Примеры](https://code.claude.com/docs/ru/agent-sdk/examples.md): Найдите полный, готовый к запуску проект Agent SDK или пошаговый рецепт из Claude Cookbook, который соответствует тому, что вы хотите создать.

#### Основные концепции

- [Как работает цикл агента](https://code.claude.com/docs/ru/agent-sdk/agent-loop.md): Поймите жизненный цикл сообщений, выполнение инструментов, контекстное окно и архитектуру, которые питают ваших агентов SDK.
- [Использование функций Claude Code в SDK](https://code.claude.com/docs/ru/agent-sdk/claude-code-features.md): Загружайте инструкции проекта, skills, hooks и другие функции Claude Code в ваши SDK-агентов.
- [Работа с сеансами](https://code.claude.com/docs/ru/agent-sdk/sessions.md): Как сеансы сохраняют историю разговора агента, и когда использовать continue, resume и fork для возврата к предыдущему запуску.
- [Сохранение сеансов во внешнее хранилище](https://code.claude.com/docs/ru/agent-sdk/session-storage.md): Зеркалируйте стенограммы сеансов Agent SDK в собственное хранилище объектов, хранилище ключ-значение или базу данных, чтобы другие хосты могли возобновить ваши сеансы.

#### Ввод и вывод

- [Streaming Input](https://code.claude.com/docs/ru/agent-sdk/streaming-vs-single-mode.md): Понимание двух режимов ввода для Claude Agent SDK и когда использовать каждый
- [Обработка одобрений и пользовательского ввода](https://code.claude.com/docs/ru/agent-sdk/user-input.md): Выводите запросы на одобрение Claude и уточняющие вопросы пользователям, а затем возвращайте их решения в SDK.
- [Потоковая передача ответов в реальном времени](https://code.claude.com/docs/ru/agent-sdk/streaming-output.md): Получайте ответы в реальном времени от Agent SDK по мере поступления текста и вызовов инструментов
- [Получение структурированного вывода от агентов](https://code.claude.com/docs/ru/agent-sdk/structured-outputs.md): Возвращайте валидированный JSON из рабочих процессов агентов, используя JSON Schema, Zod или Pydantic. Получайте типобезопасные структурированные данные после многоходового использования инструментов.

#### Расширить с помощью инструментов

- [Предоставьте Claude пользовательские инструменты](https://code.claude.com/docs/ru/agent-sdk/custom-tools.md): Определите пользовательские инструменты с помощью встроенного MCP-сервера Agent SDK, чтобы Claude мог вызывать ваши функции, обращаться к вашим API и выполнять операции, специфичные для вашей области.
- [Подключение к внешним инструментам с помощью MCP](https://code.claude.com/docs/ru/agent-sdk/mcp.md): Настройте MCP серверы для расширения вашего агента внешними инструментами. Охватывает типы транспорта, поиск инструментов для больших наборов инструментов, аутентификацию и обработку ошибок.
- [Масштабирование на множество инструментов с помощью поиска инструментов](https://code.claude.com/docs/ru/agent-sdk/tool-search.md): Масштабируйте вашего агента на тысячи инструментов, обнаруживая и загружая только необходимое по требованию.
- [Subagents в SDK](https://code.claude.com/docs/ru/agent-sdk/subagents.md): Определяйте и вызывайте subagents для изоляции контекста, параллельного выполнения задач и применения специализированных инструкций в приложениях Claude Agent SDK.

#### Настройка поведения

- [Изменение системных подсказок](https://code.claude.com/docs/ru/agent-sdk/modifying-system-prompts.md): Выберите между предустановкой `claude_code` и пользовательской системной подсказкой, и настройте поведение с помощью CLAUDE.md, стилей вывода, append или полностью пользовательской подсказки.
- [Расширьте агентов с помощью skills](https://code.claude.com/docs/ru/agent-sdk/skills.md): Управляйте тем, какие skills может вызывать Claude в сеансах Claude Agent SDK, отправляйте команды по имени и создавайте skills, которые обнаруживают ваши сеансы
- [Plugins в SDK](https://code.claude.com/docs/ru/agent-sdk/plugins.md): Загружайте пользовательские plugins для расширения Claude Code с помощью skills, agents, hooks и MCP серверов через Agent SDK

#### Управление и наблюдаемость

- [Настройка разрешений](https://code.claude.com/docs/ru/agent-sdk/permissions.md): Контролируйте, как ваш агент использует инструменты, с помощью режимов разрешений, hooks и декларативных правил разрешения/запрета.
- [Перехватывайте и контролируйте поведение агента с помощью hooks](https://code.claude.com/docs/ru/agent-sdk/hooks.md): Перехватывайте и настраивайте поведение агента в ключевых точках выполнения с помощью hooks
- [Отмотка изменений файлов с помощью checkpointing](https://code.claude.com/docs/ru/agent-sdk/file-checkpointing.md): Отслеживайте изменения файлов во время сеансов агента и восстанавливайте файлы в любое предыдущее состояние
- [Отслеживание затрат и использования](https://code.claude.com/docs/ru/agent-sdk/cost-tracking.md): Узнайте, как отслеживать использование токенов, оценивать затраты и настраивать кэширование подсказок с помощью Claude Agent SDK.
- [Наблюдаемость с OpenTelemetry](https://code.claude.com/docs/ru/agent-sdk/observability.md): Экспортируйте трассировки, метрики и события из Agent SDK в ваш бэкенд наблюдаемости с помощью OpenTelemetry.
- [Отслеживание задач](https://code.claude.com/docs/ru/agent-sdk/todo-tracking.md): Отслеживайте задачи в сеансах Agent SDK и отображайте прогресс Claude в вашем приложении с помощью структурированных вызовов инструментов

#### Развертывание

- [Размещение Agent SDK](https://code.claude.com/docs/ru/agent-sdk/hosting.md): Развертывание Agent SDK в production: архитектура подпроцессов, сохранение сеансов, масштабирование, наблюдаемость и изоляция нескольких арендаторов для Docker, Kubernetes и поставщиков песочниц.
- [Безопасное развертывание AI-агентов](https://code.claude.com/docs/ru/agent-sdk/secure-deployment.md): Руководство по защите развертываний Claude Code и Agent SDK с использованием изоляции, управления учетными данными и сетевых элементов управления

#### Справочные материалы SDK

- [Справочник Agent SDK - TypeScript](https://code.claude.com/docs/ru/agent-sdk/typescript.md): Полный справочник API для TypeScript Agent SDK, включая все функции, типы и интерфейсы.
- [TypeScript SDK V2 session API (removed)](https://code.claude.com/docs/ru/agent-sdk/typescript-v2-preview.md): Справочник по удалённому V2 TypeScript Agent SDK session API с паттернами отправки/потока на основе сессий для многооборотных разговоров.
- [Справочник Agent SDK - Python](https://code.claude.com/docs/ru/agent-sdk/python.md): Полный справочник API для Python Agent SDK, включая все функции, типы и классы.

### Что нового

#### Что нового

- [Что нового](https://code.claude.com/docs/ru/whats-new/index.md): Еженедельный дайджест примечательных функций Claude Code с примерами кода, демонстрациями и контекстом о том, почему они важны.
- [Неделя 37 · 7–11 сентября 2026](https://code.claude.com/docs/ru/whats-new/2026-w37.md): Тестируйте свои плагины с помощью claude plugin eval и выводите панели Claude Code Desktop в отдельные окна.
- [Неделя 36 · 31 августа – 4 сентября 2026](https://code.claude.com/docs/ru/whats-new/2026-w36.md): Переключитесь на Claude Fable 5.1, запустите компьютерное управление в фоновом режиме на Desktop и смотрите правки Claude в живой панели /diff.
- [Неделя 35 · 24–28 августа 2026](https://code.claude.com/docs/ru/whats-new/2026-w35.md): Возобновляйте сеансы терминала в приложении Claude Code Desktop, просматривайте отчеты об обратной связи, которые Claude подготавливает для вас, и начните сеанс в режиме ограничений.
- [Неделя 34 · 17–21 августа 2026](https://code.claude.com/docs/ru/whats-new/2026-w34.md): Создавайте редактируемые UI-макеты с помощью навыка /design, установите стиль вывода Concise и запустите сеанс Claude Code на своей машине со своего телефона.
- [Неделя 33 · 10–14 августа 2026](https://code.claude.com/docs/ru/whats-new/2026-w33.md): Claude Code Desktop автоматически продолжает работу после сброса лимита использования, режим fork включается по умолчанию, а запросы на слияние GitLab и маркетплейсы присоединяются к GitHub.
- [Неделя 32 · 3–7 августа 2026](https://code.claude.com/docs/ru/whats-new/2026-w32.md): Сеансы Claude Code обмениваются сообщениями друг с другом, самостоятельно размещённые окружения запускают облачные сеансы на вашей инфраструктуре, и режим auto становится режимом разрешений по умолчанию.
- [Неделя 30 · 20–24 июля 2026](https://code.claude.com/docs/ru/whats-new/2026-w30.md): Opus 5 становится моделью Opus по умолчанию, Claude Code Desktop добавляет панель iOS Simulator, а плагин Claude Security сканирует ваш код на уязвимости.
- [Неделя 29 · 13–17 июля 2026](https://code.claude.com/docs/ru/whats-new/2026-w29.md): Подтягивайте живые данные в опубликованные артефакты через MCP коннекторы и используйте Claude Code с программой чтения с экрана в новом режиме чтения с экрана.
- [Неделя 28 · 6–10 июля 2026 г.](https://code.claude.com/docs/ru/whats-new/2026-w28.md): Просматривайте внешние сайты из встроенного браузера приложения Desktop, запустите полную проверку настройки с помощью /doctor и получите защиту транскриптов в автоматическом режиме и обновления представления агента.
- [Неделя 27 · 29 июня – 3 июля 2026](https://code.claude.com/docs/ru/whats-new/2026-w27.md): Claude Sonnet 5 становится моделью по умолчанию, Claude в Chrome достигает общей доступности, подагенты работают в фоновом режиме по умолчанию, Claude Desktop появляется на Linux в бета-версии, и /radio настраивается на Claude FM.
- [Неделя 26 · 22–26 июня 2026](https://code.claude.com/docs/ru/whats-new/2026-w26.md): Аутентифицируйте MCP серверы из вашей оболочки с помощью claude mcp login, получайте ответ на вывод команды режима shell с префиксом !, и возобновляйте беседу перед /clear с помощью /rewind.
- [Неделя 25 · 15–19 июня 2026](https://code.claude.com/docs/ru/whats-new/2026-w25.md): Опубликуйте живую, доступную для совместного использования страницу из вашей сессии с Artifacts, сопоставляйте параметры инструментов в правилах deny и ask, и устанавливайте любой параметр из приглашения с помощью /config.
- [Неделя 24 · 8–12 июня 2026](https://code.claude.com/docs/ru/whats-new/2026-w24.md): Переместите сеанс в новый каталог с помощью /cd, позвольте подагентам создавать собственных подагентов и устраняйте неисправности в конфигурации с помощью безопасного режима.
- [Неделя 23 · 1–5 июня 2026](https://code.claude.com/docs/ru/whats-new/2026-w23.md): Запуск режима auto на Amazon Bedrock, Google Cloud's Agent Platform и Microsoft Foundry, запрос перед записью файлов, которые могут выполнять код в режиме acceptEdits, список установленных плагинов с помощью /plugin list и требование утвержденного диапазона версий для управляемых развертываний.
- [Неделя 22 · 25–29 мая 2026](https://code.claude.com/docs/ru/whats-new/2026-w22.md): Запускайте Claude Code на Claude Opus 4.8, организуйте крупные задачи с помощью динамических workflows, выявляйте проблемы безопасности с помощью плагина security-guidance и используйте fast mode на Opus 4.8 по более низкой цене.
- [Неделя 21 · 18–22 мая 2026](https://code.claude.com/docs/ru/whats-new/2026-w21.md): Используйте режим auto на плане Pro и с Sonnet 4.6, посмотрите, какие skills, subagents и MCP servers влияют на ограничения вашего плана в /usage, и просмотрите различия с помощью новой команды /code-review.
- [Неделя 20 · 11–15 мая 2026](https://code.claude.com/docs/ru/whats-new/2026-w20.md): Управляйте каждой сессией Claude Code с одного экрана с помощью представления агента, держите Claude в работе до выполнения условия и запускайте быстрый режим на Opus 4.7 по умолчанию.
- [Неделя 19 · 4–8 мая 2026](https://code.claude.com/docs/ru/whats-new/2026-w19.md): Загружайте плагины из архивов .zip и URL-адресов, ищите историю команд во всех проектах с помощью Ctrl+R, создавайте новые worktrees из локального HEAD или удаленной ветки по умолчанию и блокируйте действия безусловно с помощью правил hard deny в режиме auto.
- [Неделя 18 · 27 апреля – 1 мая 2026](https://code.claude.com/docs/ru/whats-new/2026-w18.md): Claude Code на Windows работает без Git Bash, claude auth login принимает вставленный код OAuth, когда обратный вызов браузера не может достичь localhost, claude project purge очищает локальное состояние для каждого проекта, и вставка URL PR в /resume находит сеанс, который его создал.
- [Неделя 17 · 20–24 апреля 2026](https://code.claude.com/docs/ru/whats-new/2026-w17.md): /ultrareview открывается как исследовательский предпросмотр, автоматические сводки сеансов при возврате в терминал, пользовательские цветовые темы, которые вы можете создавать и распространять в плагинах, и переработанный Claude Code в веб-версии.
- [Неделя 16 · 13–17 апреля 2026](https://code.claude.com/docs/ru/whats-new/2026-w16.md): Claude Opus 4.7 с новым уровнем усилий xhigh, Routines на Claude Code в веб-версии, мобильные push-уведомления, которые уведомляют ваш телефон, когда Claude нуждается в вас, /usage с разбивкой, показывающей, что ограничивает вас, и нативные бинарные файлы вместо упакованного JavaScript.
- [Неделя 15 · 6–10 апреля 2026](https://code.claude.com/docs/ru/whats-new/2026-w15.md): Облачное планирование Ultraplan, инструмент Monitor с самостоятельным темпом /loop, /team-onboarding для упаковки вашей конфигурации и /autofix-pr из вашего терминала.
- [Неделя 14 · 30 марта – 3 апреля 2026](https://code.claude.com/docs/ru/whats-new/2026-w14.md): Computer use в CLI, интерактивные встроенные уроки, рендеринг без мерцания, переопределение размера результатов MCP для каждого инструмента и исполняемые файлы плагинов в PATH.
- [Неделя 13 · 23–27 марта 2026](https://code.claude.com/docs/ru/whats-new/2026-w13.md): Auto mode для автоматических разрешений, встроенное управление компьютером, автоматическое исправление PR в облаке, поиск по транскриптам и инструмент PowerShell для Windows.

### Ресурсы

#### Ресурсы

- [Правовые и нормативные требования](https://code.claude.com/docs/ru/legal-and-compliance.md): Правовые соглашения, сертификаты соответствия и информация о безопасности для Claude Code.

---

## Claude Code Docs: Traditional Chinese

- 官方原文：https://code.claude.com/docs/_llms/zh-hant.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-_llms-zh-hant.md`

# Claude Code Docs: Traditional Chinese

> Official documentation for Claude Code, Anthropic's agentic coding tool available in the terminal, IDE, desktop app, and browser. Covers installation, configuration, skills, subagents, hooks, MCP, the Agent SDK, and reference material.

## Traditional Chinese

### 開始使用

#### 開始使用

- [概述](https://code.claude.com/docs/zh-TW/overview.md): Claude Code 是一個代理編碼工具，可以讀取您的程式碼庫、編輯檔案、執行命令，並與您的開發工具整合。可在您的終端機、IDE、桌面應用程式和瀏覽器中使用。
- [快速入門](https://code.claude.com/docs/zh-TW/quickstart.md): 歡迎使用 Claude Code！
- [變更日誌](https://code.claude.com/docs/zh-TW/changelog.md)

#### 核心概念

- [Claude Code 如何運作](https://code.claude.com/docs/zh-TW/how-claude-code-works.md): 了解代理迴圈、內建工具，以及 Claude Code 如何與您的專案互動。
- [擴展 Claude Code](https://code.claude.com/docs/zh-TW/features-overview.md): 了解何時使用 CLAUDE.md、Skills、subagents、hooks、MCP 和 plugins。
- [探索 .claude 目錄](https://code.claude.com/docs/zh-TW/claude-directory.md): Claude Code 讀取 CLAUDE.md、settings.json、hooks、skills、commands、subagents、workflows、rules 和自動記憶的位置。探索您專案中的 .claude 目錄和主目錄中的 ~/.claude。
- [探索上下文視窗](https://code.claude.com/docs/zh-TW/context-window.md): Claude Code 上下文視窗在會話期間如何填充的互動模擬。查看自動加載的內容、每個文件讀取的成本，以及規則和 hooks 何時觸發。
- [Claude Code 如何使用 prompt caching](https://code.claude.com/docs/zh-TW/prompt-caching.md): Claude Code 會自動管理 prompt caching。了解為什麼模型切換會觸發緩慢的未快取回應、`/compact` 的成本、為什麼 CLAUDE.md 編輯在工作階段中途不適用，以及如何檢查您的快取命中率。

#### 使用 Claude Code

- [Claude 如何記住您的專案](https://code.claude.com/docs/zh-TW/memory.md): 使用 CLAUDE.md 或 AGENTS.md 檔案為 Claude 提供持久指示，並讓 Claude 透過自動記憶自動累積學習。
- [管理 sessions](https://code.claude.com/docs/zh-TW/sessions.md): 命名、恢復、分支和在 Claude Code 對話之間切換。涵蓋 `--continue`、`--resume`、`--from-pr`、`/resume` 選擇器、session 命名、匯出文字記錄，以及文字記錄的儲存位置。
- [常見工作流程](https://code.claude.com/docs/zh-TW/common-workflows.md): 使用 Claude Code 探索程式碼庫、修復錯誤、重構、測試和其他日常任務的逐步指南。
- [提示詞庫](https://code.claude.com/docs/zh-TW/prompt-library.md): 複製貼上提示詞供 Claude Code 使用，按任務和角色標記。
- [Claude Code 最佳實踐](https://code.claude.com/docs/zh-TW/best-practices.md): 從設定環境到跨平行工作階段擴展，充分利用 Claude Code 的提示和模式。

#### 平台與整合

- [平台和整合](https://code.claude.com/docs/zh-TW/platforms.md): 選擇在何處執行 Claude Code 以及要連接什麼。比較 CLI、Desktop、VS Code、JetBrains、Web 和 Chrome、Slack 和 CI/CD 等整合。
- [使用 Remote Control 從任何裝置繼續本地會話](https://code.claude.com/docs/zh-TW/remote-control.md): 使用 Remote Control 從您的手機、平板電腦或任何瀏覽器繼續本地 Claude Code 會話。適用於 claude.ai/code 和 Claude 行動應用程式。
- [讓 Claude 使用 Projects 協調進行中的工作](https://code.claude.com/docs/zh-TW/claude-projects.md): 在一個對話中為 Claude 提供一組相關的工作，讓它協調共享儲存庫、指示和記憶的平行雲端工作階段。
- [Claude Code 行動版](https://code.claude.com/docs/zh-TW/mobile.md): 從您的手機使用 Claude iOS 和 Android 應用程式來啟動、監控和引導 Claude Code 工作。
- [在 Chrome 中使用 Claude Code](https://code.claude.com/docs/zh-TW/chrome.md): 將 Claude Code 連接到您的 Chrome 瀏覽器，以測試網頁應用程式、使用控制台日誌進行除錯、自動填充表單，以及從網頁中提取資料。
- [讓 Claude 從 CLI 使用您的電腦](https://code.claude.com/docs/zh-TW/computer-use.md): 在 Claude Code CLI 中啟用 computer use，讓 Claude 可以在 macOS 上開啟應用程式、點擊、輸入和查看您的螢幕。測試原生應用程式、除錯視覺問題，以及自動化僅限 GUI 的工具，無需離開您的終端機。
- [在 VS Code 中使用 Claude Code](https://code.claude.com/docs/zh-TW/vs-code.md): 安裝並配置 VS Code 的 Claude Code 擴充功能。透過內聯差異、@-提及、計畫審查和快捷鍵獲得 AI 編碼協助。
- [JetBrains IDEs](https://code.claude.com/docs/zh-TW/jetbrains.md): 使用 Claude Code 與 JetBrains IDEs（包括 IntelliJ、PyCharm、WebStorm 等）整合
- [Slack 中的 Claude Code](https://code.claude.com/docs/zh-TW/slack.md): 直接從您的 Slack 工作區委派編碼任務。Anthropic 正在為 Team 和 Enterprise 工作區停用此較早版本，改用 Claude Tag；它仍然是 Pro 和 Max 方案上的設定路徑。
- [Claude Tag](https://code.claude.com/docs/zh-TW/claude-tag.md): 透過 Claude Tag 將 Claude 帶入您的團隊 Slack 頻道，並在 claude.com 上找到其設定和使用文件。

##### 雲端 Claude Code

- [在雲端開始使用 Claude Code](https://code.claude.com/docs/zh-TW/web-quickstart.md): 在雲端從瀏覽器或手機執行 Claude Code。連接 GitHub 儲存庫、提交任務，並在無需本地設定的情況下檢查 PR。
- [在雲端使用 Claude Code](https://code.claude.com/docs/zh-TW/claude-code-on-the-web.md): 從您的瀏覽器、手機、桌面應用程式或終端在雲端執行 Claude Code 工作階段，使用 --cloud 和 --teleport 移動工作階段，以及自動修復拉取請求。
- [使用例行程序自動化工作](https://code.claude.com/docs/zh-TW/routines.md): 讓 Claude Code 自動運行。定義在排程上運行、在 API 呼叫時觸發或對來自雲端基礎設施的 GitHub 事件做出反應的例行程序。
- [使用 Ultrareview 尋找錯誤](https://code.claude.com/docs/zh-TW/ultrareview.md): 使用 /code-review ultra 在雲端執行深度多代理程式碼審查，在合併前尋找並驗證錯誤。

##### Claude Code 桌面版

- [開始使用桌面應用程式](https://code.claude.com/docs/zh-TW/desktop-quickstart.md): 在桌面上安裝 Claude Code 並開始您的第一個編碼會話
- [Desktop 應用程式](https://code.claude.com/docs/zh-TW/desktop.md): 充分利用 Claude Code Desktop：具有 Git 隔離的並行會話、拖放窗格佈局、整合終端機和檔案編輯器、側邊聊天、電腦使用、從您的手機 Dispatch 會話、視覺化差異檢查、應用程式預覽、PR 監控、連接器和企業配置。
- [Linux 上的 Claude Desktop（測試版）](https://code.claude.com/docs/zh-TW/desktop-linux.md): 在 Ubuntu 和 Debian 上安裝和更新 Claude 桌面應用程式
- [Claude Code Desktop in WSL](https://code.claude.com/docs/zh-TW/desktop-wsl.md): 在 Windows 上的 WSL 2 發行版內執行 Code 工作階段
- [在 Claude Code Desktop 中排程定期任務](https://code.claude.com/docs/zh-TW/desktop-scheduled-tasks.md): 在 Claude Code Desktop 中設定排程任務，以定期自動執行 Claude 進行每日程式碼審查、相依性稽核或早晨簡報。
- [在模擬器中測試 iOS 應用程式](https://code.claude.com/docs/zh-TW/desktop-ios-simulator.md): Claude Code Desktop 在 Claude 建置、執行或檢查應用程式時，會在 iOS Simulator 窗格中開啟您的應用程式，每個工作階段都有一個獨立的模擬器。

##### 程式碼審查與 CI/CD

- [在 Claude 編寫程式碼時捕捉安全問題](https://code.claude.com/docs/zh-TW/security-guidance.md): 安裝 security-guidance 外掛程式，讓 Claude 檢查自己的程式碼變更是否存在漏洞，並在同一個工作階段中修復它們。
- [掃描程式碼庫以尋找漏洞](https://code.claude.com/docs/zh-TW/claude-security.md): 安裝 Claude Security plugin 以在 Claude Code 工作階段中掃描程式碼庫以尋找漏洞，並將發現的問題轉換為您可以檢查和應用的修補程式。
- [Code Review](https://code.claude.com/docs/zh-TW/code-review.md): 設定自動化 PR 審查，使用多代理分析您的完整程式碼庫來捕捉邏輯錯誤、安全漏洞和迴歸
- [Claude Code GitHub Actions](https://code.claude.com/docs/zh-TW/github-actions.md): 在 GitHub Actions 工作流程中執行 Claude Code，以回應 @claude 提及、自動化任務，並將議題轉換為 pull request
- [使用 Claude Code GitHub Actions 搭配雲端提供者](https://code.claude.com/docs/zh-TW/github-actions-cloud-providers.md): 透過 Amazon Bedrock、Google Cloud 的 Agent Platform 或 Microsoft Foundry 執行 Claude Code GitHub Actions，而不是使用 Claude API
- [Claude Code 與 GitHub Enterprise Server](https://code.claude.com/docs/zh-TW/github-enterprise-server.md): 將 Claude Code 連接到您自託管的 GitHub Enterprise Server 實例，以進行雲端會話、代碼審查和插件市場。
- [Claude Code GitLab CI/CD](https://code.claude.com/docs/zh-TW/gitlab-ci-cd.md): 了解如何將 Claude Code 整合到您的開發工作流程中，使用 GitLab CI/CD

### 使用 Claude Code 建構

#### 代理程式與平行工作

- [平行執行代理](https://code.claude.com/docs/zh-TW/agents.md): 比較 Claude Code 同時執行多項任務的方式：子代理、代理檢視、代理團隊、動態工作流程和專案。
- [建立自訂 subagents](https://code.claude.com/docs/zh-TW/sub-agents.md): 在 Claude Code 中建立和使用專門的 AI subagents，用於特定任務的工作流程和改進的上下文管理。
- [使用 Agent view 管理多個代理](https://code.claude.com/docs/zh-TW/agent-view.md): 從一個螢幕分派和管理許多 Claude Code 工作階段。Agent view 顯示每個工作階段正在做什麼，以及哪些需要您的輸入。
- [協調 Claude Code 工作階段團隊](https://code.claude.com/docs/zh-TW/agent-teams.md): 協調多個 Claude Code 實例作為團隊一起工作，具有共享任務、代理間訊息傳遞和集中管理。
- [訊息傳送至您的其他 Claude Code 工作階段](https://code.claude.com/docs/zh-TW/cross-session-messaging.md): 讓 Claude 列出並訊息傳送至您在此機器上的其他 Claude Code 工作階段，並與您在其他機器或網路上的工作階段聯繫。
- [使用動態工作流程大規模協調子代理](https://code.claude.com/docs/zh-TW/workflows.md): 動態工作流程從 Claude 編寫的指令碼協調許多子代理，您可以重新執行。用於程式碼庫審計、大規模遷移和交叉檢查研究。
- [使用 worktrees 執行平行會話](https://code.claude.com/docs/zh-TW/worktrees.md): 在獨立的 git worktrees 中隔離平行的 Claude Code 會話，使變更不會相互衝突。涵蓋 `--worktree` 旗標、子代理隔離、`.worktreeinclude`、清理和非 git VCS hooks。

#### MCP

- [連接到 MCP 伺服器](https://code.claude.com/docs/zh-TW/mcp-quickstart.md): 將 MCP 伺服器新增至 Claude Code、驗證連接，並在磁碟上找到設定。
- [透過 MCP 將 Claude Code 連接到工具](https://code.claude.com/docs/zh-TW/mcp.md): 了解如何使用 Model Context Protocol 將 Claude Code 連接到您的工具。

#### 技能

- [使用 skills 擴展 Claude](https://code.claude.com/docs/zh-TW/skills.md): 在 Claude Code 中建立、管理和分享 skills 以擴展 Claude 的功能。包括自訂命令和捆綁的 skills。

#### 外掛程式

- [透過市場探索和安裝預建外掛程式](https://code.claude.com/docs/zh-TW/discover-plugins.md): 從市場探索和安裝外掛程式，以使用新技能、代理和功能擴展 Claude Code。
- [建立 plugins](https://code.claude.com/docs/zh-TW/plugins.md): 建立自訂 plugins 以使用 skills、agents、hooks 和 MCP servers 擴展 Claude Code。
- [使用 evals 測試 plugins](https://code.claude.com/docs/zh-TW/plugin-evals.md): 為您的 Claude Code plugin 編寫 eval 案例，使用 claude plugin eval 執行它們，評分結果，與無 plugin 基準線進行比較，並在 CI 中根據分數進行把關。

#### 成品

- [將工作階段輸出分享為成品](https://code.claude.com/docs/zh-TW/artifacts.md): 成品將 Claude Code 的工作轉化為 claude.ai 上的即時互動頁面，您可以保持私密、與您的組織分享，或發佈到公開連結。

#### 自動化

- [使用 hooks 自動化工作流程](https://code.claude.com/docs/zh-TW/hooks-guide.md): 當 Claude Code 編輯檔案、完成任務或需要輸入時，自動執行 shell 命令。格式化程式碼、發送通知、驗證命令並強制執行專案規則。
- [使用 channels 將事件推送到執行中的工作階段](https://code.claude.com/docs/zh-TW/channels.md): 使用 channels 從 MCP 伺服器將訊息、警報和 webhooks 推送到您的 Claude Code 工作階段。轉發 CI 結果、聊天訊息和監控事件，讓 Claude 在您不在時做出反應。
- [按排程執行提示](https://code.claude.com/docs/zh-TW/scheduled-tasks.md): 使用 /loop 和 cron 排程工具在 Claude Code 工作階段內重複執行提示、輪詢狀態或設定一次性提醒。
- [讓 Claude 朝著目標持續工作](https://code.claude.com/docs/zh-TW/goal.md): 使用 /goal 設定完成條件，Claude 會持續工作直到條件滿足、模型判斷不可能達成，或需要修復的錯誤清除目標。
- [以程式方式執行 Claude Code](https://code.claude.com/docs/zh-TW/headless.md): 使用 Agent SDK 從 CLI、Python 或 TypeScript 以程式方式執行 Claude Code。
- [從連結啟動工作階段](https://code.claude.com/docs/zh-TW/deep-links.md): 從 URL 開啟 Claude Code 終端機工作階段。在執行手冊、警報和儀表板中嵌入 `claude-cli://` 連結，只需點擊即可在正確的儲存庫中使用正確的提示開啟 Claude Code。

#### 指南

- [在 monorepo 或大型程式碼庫中設定 Claude Code](https://code.claude.com/docs/zh-TW/large-codebases.md): 使用巢狀 CLAUDE.md 檔案、稀疏 worktrees、程式碼智能和按套件技能為 monorepos 和大型單樹程式碼庫設定 Claude Code，讓 Claude 專注於您正在處理的程式碼。

#### 疑難排解

- [排除安裝和登入問題](https://code.claude.com/docs/zh-TW/troubleshoot-install.md): 修復安裝或登入 Claude Code 時的 command not found、PATH、權限、網路和身份驗證錯誤。
- [故障排除](https://code.claude.com/docs/zh-TW/troubleshooting.md): 修復 Claude Code 中的高 CPU 或記憶體使用、掛起、auto-compact 抖動和搜尋問題，並找到其他問題的正確頁面。
- [偵錯您的設定](https://code.claude.com/docs/zh-TW/debug-your-config.md): 診斷為什麼 CLAUDE.md、settings、hooks、MCP servers 或 skills 沒有生效。使用 /context、/doctor、/hooks 和 /mcp 查看實際載入的內容。
- [錯誤參考](https://code.claude.com/docs/zh-TW/errors.md): 查詢 Claude Code 執行時錯誤訊息，了解每個錯誤的含義及修復方法。

### 管理

#### 設定與存取

- [為您的組織設定 Claude Code](https://code.claude.com/docs/zh-TW/admin-setup.md): 管理員部署 Claude Code 的決策地圖，涵蓋 API 提供者、受管設定、政策執行、使用情況監控和資料處理。
- [進階設定](https://code.claude.com/docs/zh-TW/setup.md): Claude Code 的系統需求、平台特定安裝、版本管理和卸載。
- [驗證](https://code.claude.com/docs/zh-TW/authentication.md): 登入 Claude Code 並為個人、團隊和組織配置驗證。
- [部署受管設定](https://code.claude.com/docs/zh-TW/managed-settings.md): 將受管設定部署到每個開發者的機器：每個作業系統的傳遞機制、Claude Code 如何結合受管來源，以及如何驗證強制執行。
- [設定伺服器管理的設定](https://code.claude.com/docs/zh-TW/server-managed-settings.md): 透過伺服器傳遞的設定在您的組織中集中設定 Claude Code，無需裝置管理基礎設施。
- [控制組織的 MCP 伺服器存取](https://code.claude.com/docs/zh-TW/managed-mcp.md): 使用受管設定檔、受管設定、允許清單和拒絕清單，限制使用者可以新增或連線的 MCP 伺服器，或為每位使用者提供伺服器。
- [設定自動模式](https://code.claude.com/docs/zh-TW/auto-mode-config.md): 告訴自動模式分類器您的組織信任哪些儲存庫、儲存桶和網域。設定環境內容、覆蓋預設的封鎖和允許規則，並使用自動模式 CLI 子命令檢查您的有效設定。

#### 部署

- [企業部署概述](https://code.claude.com/docs/zh-TW/third-party-integrations.md): 了解 Claude Code 如何與各種第三方服務和基礎設施整合，以滿足企業部署需求。
- [功能可用性](https://code.claude.com/docs/zh-TW/feature-availability.md): 比較 Claude Code 功能在 Anthropic 訂閱計畫、Anthropic Console、Amazon Bedrock、AWS 上的 Claude Platform、Google Cloud 的 Agent Platform 和 Microsoft Foundry 中的可用性。
- [Amazon Bedrock 上的 Claude Code](https://code.claude.com/docs/zh-TW/amazon-bedrock.md): 了解如何透過 Amazon Bedrock 設定 Claude Code，包括設定、IAM 設定和故障排除。
- [AWS 上的 Claude Platform 上的 Claude Code](https://code.claude.com/docs/zh-TW/claude-platform-on-aws.md): 設定 Claude Code 以使用 Anthropic 營運的 Claude API，搭配 AWS 驗證、IAM 存取控制和 AWS Marketplace 計費。
- [Google Cloud 的 Agent Platform 上的 Claude Code](https://code.claude.com/docs/zh-TW/google-vertex-ai.md): 了解如何透過 Google Cloud 的 Agent Platform（前身為 Vertex AI）設定 Claude Code，包括設定、IAM 設定和故障排除。
- [Microsoft Foundry 上的 Claude Code](https://code.claude.com/docs/zh-TW/microsoft-foundry.md): 了解如何透過 Microsoft Foundry 配置 Claude Code，包括設定、配置和故障排除。
- [企業網路設定](https://code.claude.com/docs/zh-TW/network-config.md): 為企業環境設定 Claude Code，包括代理伺服器、自訂憑證授權單位 (CA) 和相互傳輸層安全性 (mTLS) 驗證。
- [在公司啟動程式後面執行 Claude Code](https://code.claude.com/docs/zh-TW/corporate-launcher.md): 使用 CLAUDE_CODE_PROCESS_WRAPPER 或 processWrapper 設定，透過必要的啟動程式路由 Claude Code 從其自身二進位檔案啟動的程序，包括背景服務和每個代理檢視工作階段。
- [開發容器](https://code.claude.com/docs/zh-TW/devcontainer.md): 在開發容器中執行 Claude Code，為您的團隊提供一致、隔離的環境。

#### 閘道

- [透過閘道執行 Claude Code](https://code.claude.com/docs/zh-TW/gateways.md): 透過自託管閘道路由 Claude Code，以實現集中式認證、使用情況追蹤和成本控制。涵蓋架構、Anthropic 的 Claude 應用程式閘道和使用其他閘道產品。

##### Claude 應用程式閘道

- [Amazon Bedrock、Claude Platform on AWS、Google Cloud 和 Microsoft Foundry 的 Claude 應用程式閘道](https://code.claude.com/docs/zh-TW/claude-apps-gateway.md): 透過自託管閘道在 Amazon Bedrock、Claude Platform on AWS、Google Cloud 或 Microsoft Foundry 上執行 Claude Code，具備 SSO 登入、按群組模型存取和 OTLP 遙測功能。
- [Claude 應用程式閘道設定](https://code.claude.com/docs/zh-TW/claude-apps-gateway-config.md): 每個 gateway.yaml 選項的參考資料：監聽器和 TLS、OIDC、工作階段、Postgres 存放區、Amazon Bedrock、Claude Platform on AWS、Google Cloud 的 Agent Platform 和 Microsoft Foundry 上游、模型路由、受管原則和遙測。
- [Claude 應用程式閘道支出限制](https://code.claude.com/docs/zh-TW/claude-apps-gateway-spend-limits.md): 透過 Claude 應用程式閘道限制每位開發人員的每日、每週或每月支出。使用管理員 API 設定限制，閘道會在每個請求上即時執行這些限制。
- [Claude 應用程式閘道部署和運營](https://code.claude.com/docs/zh-TW/claude-apps-gateway-deploy.md): 向您的身份提供者註冊閘道、建置容器、在 Kubernetes 或 Cloud Run 上部署，並運營它：健康檢查、祕密輪換、升級和安全性。
- [在 AWS 上部署 Claude apps gateway](https://code.claude.com/docs/zh-TW/claude-apps-gateway-on-aws.md): 在 AWS 上執行 Claude apps gateway 的實際範例：ECS Fargate 或 EKS、Amazon RDS for PostgreSQL、AWS Secrets Manager 和 IAM 角色驗證至 Amazon Bedrock。
- [在 Google Cloud 上部署 Claude 應用程式閘道](https://code.claude.com/docs/zh-TW/claude-apps-gateway-on-gcp.md): 在 Google Cloud 上執行 Claude 應用程式閘道的實際範例：Cloud Run 或 GKE、Cloud SQL for PostgreSQL、Secret Manager，以及對 Google Cloud 的 Agent Platform 的服務帳戶驗證。

##### 其他閘道

- [其他 LLM 閘道](https://code.claude.com/docs/zh-TW/llm-gateway.md): 透過貴組織已執行的 LLM 閘道路由 Claude Code。涵蓋將 Claude Code 連接到閘道、為貴組織推出閘道，以及 Claude Code 傳送到閘道的內容。
- [將 Claude Code 連接到 LLM 閘道](https://code.claude.com/docs/zh-TW/llm-gateway-connect.md): 將 Claude Code 指向您組織的 LLM 閘道。檢查您的管理員是否已配置它，或自行設定基礎 URL 和認證，然後驗證連接並修復閘道錯誤。
- [為您的組織推出 LLM 閘道](https://code.claude.com/docs/zh-TW/llm-gateway-rollout.md): 為 Claude Code 部署閘道產品：配置它以轉發 Claude Code 發送的內容、發放開發者認證、透過受管設定分發配置，並驗證推出。
- [Claude Code 閘道相容性指南](https://code.claude.com/docs/zh-TW/llm-gateway-protocol.md): 保持 LLM 閘道與 Claude Code 相容：它呼叫的端點、必須轉發的標頭和本體欄位，以及移除它們時會中斷的功能。

#### 使用量和成本

- [監控](https://code.claude.com/docs/zh-TW/monitoring-usage.md): 了解如何為 Claude Code 啟用和配置 OpenTelemetry。
- [有效管理成本](https://code.claude.com/docs/zh-TW/costs.md): 追蹤 token 使用情況、設定團隊支出限制，並透過上下文管理、模型選擇、延伸思考設定和預處理 hooks 來降低 Claude Code 成本。
- [使用分析追蹤團隊使用情況](https://code.claude.com/docs/zh-TW/analytics.md): 在分析儀表板中檢視 Claude Code 使用指標、追蹤採用情況，並衡量 Claude Code 對工程速度的影響。

#### 外掛程式發佈

- [建立並分發 plugin marketplace](https://code.claude.com/docs/zh-TW/plugin-marketplaces.md): 建立並託管 plugin marketplace，以在團隊和社群中分發 Claude Code 擴充功能。
- [限制 plugin 依賴版本](https://code.claude.com/docs/zh-TW/plugin-dependencies.md): 在 plugin 依賴上聲明版本約束，並將精選 plugin 集合捆綁在一個安裝後面。
- [從您的 CLI 推薦您的外掛程式](https://code.claude.com/docs/zh-TW/plugin-hints.md): 從您的 CLI 發出單行標記，以便 Claude Code 提示使用者安裝您的官方外掛程式。
- [為您的組織推薦外掛程式](https://code.claude.com/docs/zh-TW/plugin-relevance.md): 在 marketplace.json 中的外掛程式項目中新增相關性區塊，以便在使用者的工作相符時，Claude Code 會建議這些外掛程式。

#### 安全性和資料

- [安全性](https://code.claude.com/docs/zh-TW/security.md): 了解 Claude Code 的安全防護措施和安全使用的最佳實踐。
- [資料使用](https://code.claude.com/docs/zh-TW/data-usage.md): 了解 Anthropic 對 Claude 資料使用政策
- [零資料保留](https://code.claude.com/docs/zh-TW/zero-data-retention.md): 了解 Claude for Enterprise 合格帳戶可用的 Claude Code 零資料保留 (ZDR)，包括範圍、停用的功能，以及如何要求啟用。

#### 採用

- [通訊工具包](https://code.claude.com/docs/zh-TW/communications-kit.md): 推出公告、滴灌式行銷訊息和常見問題解答，用於在您的工程組織中推出 Claude Code。
- [Champion kit](https://code.claude.com/docs/zh-TW/champion-kit.md): 工程師在內部倡導 Claude Code 的行動手冊：分享什麼、如何回答問題，以及如何在團隊中推動採用。

### 設定

#### 設定

- [設定檔案和優先順序](https://code.claude.com/docs/zh-TW/settings.md): 變更 Claude Code 設定、選擇金鑰所屬的範圍、驗證變更，並了解當金鑰在多個位置設定時 Claude Code 使用哪個值。
- [所有設定](https://code.claude.com/docs/zh-TW/settings-reference.md): Claude Code settings.json 的完整參考：每個鍵的位置、類型和預設值，以及隨時可貼上的範例，包含每個鍵的索引。
- [設定檔範例](https://code.claude.com/docs/zh-TW/settings-example.md): 開發者、團隊和組織的實際 settings.json 檔案：複製其中一個，保留您想要的鍵，並變更數值。

#### 權限與 sandboxing

- [設定權限](https://code.claude.com/docs/zh-TW/permissions.md): 使用細粒度權限規則、模式和受管理原則來控制 Claude Code 可以存取和執行的操作。
- [選擇權限模式](https://code.claude.com/docs/zh-TW/permission-modes.md): 控制 Claude 在採取動作前是否詢問。在 CLI 中使用 Shift+Tab、在 VS Code 中使用模式指示器，或在 Desktop 中使用模式選擇器來切換權限模式。
- [設定沙箱化 Bash 工具](https://code.claude.com/docs/zh-TW/sandboxing.md): 了解 Claude Code 的沙箱化 Bash 工具如何提供檔案系統和網路隔離，以實現更安全、更自主的代理執行。
- [選擇沙箱環境](https://code.claude.com/docs/zh-TW/sandbox-environments.md): 比較 Claude Code 沙箱選項：內建的沙箱化 Bash 工具、sandbox runtime、dev containers、Docker 和虛擬機。為您的威脅模型選擇適當的隔離。

#### 環境

- [設定雲端環境](https://code.claude.com/docs/zh-TW/cloud-environments.md): 為 Claude Code 雲端工作階段設定雲端環境：網路存取層級、環境變數、設定指令碼和環境快取。

##### 自行託管環境

- [自託管環境](https://code.claude.com/docs/zh-TW/self-hosted-environments.md): 在您控制的基礎設施上執行 Claude Code 雲端工作階段：設定自託管環境、部署執行器，並將工作階段路由到您自己的運算資源。
- [自託管環境快速入門](https://code.claude.com/docs/zh-TW/self-hosted-environments-quickstart.md): 設定您的第一個自託管環境：安裝 Claude Code、建立環境、啟動執行器，並將工作階段路由到該環境。
- [將自託管環境部署到生產環境](https://code.claude.com/docs/zh-TW/self-hosted-environments-deploy.md): 在生產環境中執行自託管執行器：安全強化、網路出站流量控制、Git 認證、Kubernetes 和 Compose 配方，以及故障排除。
- [在自託管環境中自訂會話](https://code.claude.com/docs/zh-TW/self-hosted-environments-configuration.md): 使用包裝指令碼在自託管環境會話中自訂每個會話的認證、生命週期掛鉤和按需執行器生成。
- [端對端測試自託管環境](https://code.claude.com/docs/zh-TW/self-hosted-environments-testing.md): 從 CI 驗證自託管執行器映像：使用 CLI 分派工作階段、透過 Stop hook 讀取 Claude 的回覆，並編寫完整迴圈的指令碼。
- [自託管環境參考](https://code.claude.com/docs/zh-TW/self-hosted-environments-reference.md): 自託管執行器和協調器的完整參考：CLI 旗標、環境變數和 Prometheus 指標。
- [在自託管環境中驗證工作階段身分](https://code.claude.com/docs/zh-TW/self-hosted-environments-identity.md): 驗證 CLAUDE_CODE_SESSION_ACCESS_TOKEN JWT，以便您網路上的服務可以信任來自自託管環境中工作階段的請求。

#### 模型與回應

- [模型配置](https://code.claude.com/docs/zh-TW/model-config.md): 了解 Claude Code 模型配置，包括模型別名如 `opusplan`
- [使用快速模式加快回應速度](https://code.claude.com/docs/zh-TW/fast-mode.md): 在 Claude Code 中切換快速模式，以獲得更快的 Opus 回應。
- [使用顧問工具升級困難決策](https://code.claude.com/docs/zh-TW/advisor.md): 將您的主要模型與更強大的顧問模型配對，Claude 在任務期間的關鍵時刻會諮詢該模型。
- [輸出樣式](https://code.claude.com/docs/zh-TW/output-styles.md): 將 Claude Code 適配用於軟體工程以外的用途

#### 介面

- [為 Claude Code 設定您的終端機](https://code.claude.com/docs/zh-TW/terminal-config.md): 修正 Shift+Enter 以插入新行、在 Claude 完成時取得終端機鈴聲、設定 tmux、符合色彩主題，以及在 Claude Code CLI 中啟用 Vim 模式。
- [全螢幕渲染](https://code.claude.com/docs/zh-TW/fullscreen.md): 啟用更平順、無閃爍的渲染模式，具有滑鼠支援和穩定的記憶體使用，適用於長對話。
- [使用 Claude Code 搭配螢幕閱讀器](https://code.claude.com/docs/zh-TW/accessibility.md): 為 VoiceOver 和 NVDA 等螢幕閱讀器設定 Claude Code，以及螢幕放大鏡、減少動畫和色盲友善主題的設定。
- [語音聽寫](https://code.claude.com/docs/zh-TW/voice-dictation.md): 在 Claude Code CLI 中使用按住錄音或點擊錄音的語音聽寫功能來說出您的提示。
- [自訂您的狀態列](https://code.claude.com/docs/zh-TW/statusline.md): 設定自訂狀態列以監控 Claude Code 中的 context window 使用情況、成本和 git 狀態
- [自訂鍵盤快捷鍵](https://code.claude.com/docs/zh-TW/keybindings.md): 使用快捷鍵配置檔案在 Claude Code 中自訂鍵盤快捷鍵。

### 參考資料

#### 參考資料

- [CLI 參考](https://code.claude.com/docs/zh-TW/cli-reference.md): Claude Code 命令列介面的完整參考，包括命令和旗標。
- [Commands](https://code.claude.com/docs/zh-TW/commands.md): Claude Code 中可用命令的完整參考，包括內建命令和捆綁的 skills。
- [環境變數](https://code.claude.com/docs/zh-TW/env-vars.md): 控制 Claude Code 行為的環境變數參考。
- [工具參考](https://code.claude.com/docs/zh-TW/tools-reference.md): Claude Code 可以使用的工具完整參考，包括權限要求和各工具行為。
- [互動模式](https://code.claude.com/docs/zh-TW/interactive-mode.md): Claude Code 會話中鍵盤快捷鍵、輸入模式和互動功能的完整參考。
- [Checkpointing](https://code.claude.com/docs/zh-TW/checkpointing.md): 追蹤、回溯和總結 Claude 的編輯和對話以管理會話狀態。
- [Hooks 參考](https://code.claude.com/docs/zh-TW/hooks.md): Claude Code hook 事件、配置架構、JSON 輸入/輸出格式、退出代碼、非同步 hooks、HTTP hooks、提示 hooks 和 MCP 工具 hooks 的參考。
- [Plugins 參考](https://code.claude.com/docs/zh-TW/plugins-reference.md): Claude Code plugin 系統的完整技術參考，包括 schemas、CLI 命令和元件規格。
- [Channels 參考](https://code.claude.com/docs/zh-TW/channels-reference.md): 建立一個 MCP 伺服器，將 webhooks、警報和聊天訊息推送到 Claude Code 工作階段。頻道合約的參考：功能聲明、通知事件、回覆工具、寄件者閘道和權限中繼。

#### 詞彙表

- [詞彙表](https://code.claude.com/docs/zh-TW/glossary.md): Claude Code 術語定義。了解 agentic loop、compaction、CLAUDE.md、hooks、subagents、MCP 和其他核心概念的含義。

### Agent SDK

#### Agent SDK

- [Agent SDK 概述](https://code.claude.com/docs/zh-TW/agent-sdk/overview.md): 使用 Claude Code 作為程式庫構建生產級 AI 代理
- [快速開始](https://code.claude.com/docs/zh-TW/agent-sdk/quickstart.md): 使用 Python 或 TypeScript Agent SDK 開始構建能夠自主工作的 AI 代理
- [遷移至 Claude Agent SDK](https://code.claude.com/docs/zh-TW/agent-sdk/migration-guide.md): 將 Claude Code TypeScript 和 Python SDK 遷移至 Claude Agent SDK 的指南
- [排除 Agent SDK 的故障](https://code.claude.com/docs/zh-TW/agent-sdk/troubleshooting.md): 根據您看到的確切錯誤訊息修復 Agent SDK 錯誤，包括 TypeScript 和 Python SDK 中每個錯誤的原因和修復方法。

#### 建立代理程式

- [設定您的代理](https://code.claude.com/docs/zh-TW/agent-sdk/configuration.md): 設定 Agent SDK 工作階段：組合選項物件、設定模型、環境和限制，並找到每個功能選項的頁面。
- [範例](https://code.claude.com/docs/zh-TW/agent-sdk/examples.md): 尋找完整、可執行的 Agent SDK 專案或 Claude Cookbook 中的引導式配方，以符合您想要建置的內容。

#### 核心概念

- [代理程式迴圈如何運作](https://code.claude.com/docs/zh-TW/agent-sdk/agent-loop.md): 了解訊息生命週期、工具執行、上下文視窗和支援 SDK 代理程式的架構。
- [在 SDK 中使用 Claude Code 功能](https://code.claude.com/docs/zh-TW/agent-sdk/claude-code-features.md): 將專案指令、skills、hooks 和其他 Claude Code 功能載入到您的 SDK 代理中。
- [使用 sessions](https://code.claude.com/docs/zh-TW/agent-sdk/sessions.md): Sessions 如何保持代理對話歷史，以及何時使用 continue、resume 和 fork 返回到先前的運行。
- [將工作階段持久化到外部儲存](https://code.claude.com/docs/zh-TW/agent-sdk/session-storage.md): 將 Agent SDK 工作階段文字記錄鏡像到您自己的物件儲存、鍵值儲存或資料庫，以便其他主機可以繼續您的工作階段。

#### 輸入和輸出

- [串流輸入](https://code.claude.com/docs/zh-TW/agent-sdk/streaming-vs-single-mode.md): 了解 Claude Agent SDK 的兩種輸入模式及何時使用各種模式
- [處理批准和使用者輸入](https://code.claude.com/docs/zh-TW/agent-sdk/user-input.md): 將 Claude 的批准請求和澄清問題呈現給使用者，然後將他們的決定返回給 SDK。
- [即時串流回應](https://code.claude.com/docs/zh-TW/agent-sdk/streaming-output.md): 當文字和工具呼叫串流進來時，從 Agent SDK 取得即時回應
- [從代理獲取結構化輸出](https://code.claude.com/docs/zh-TW/agent-sdk/structured-outputs.md): 使用 JSON Schema、Zod 或 Pydantic 從代理工作流程返回驗證的 JSON。在多輪工具使用後獲得類型安全的結構化資料。

#### 使用工具擴充

- [為 Claude 提供自訂工具](https://code.claude.com/docs/zh-TW/agent-sdk/custom-tools.md): 使用 Claude Agent SDK 的同程序 MCP 伺服器定義自訂工具，讓 Claude 可以呼叫您的函數、存取您的 API，並執行特定領域的操作。
- [使用 MCP 連接外部工具](https://code.claude.com/docs/zh-TW/agent-sdk/mcp.md): 配置 MCP 伺服器以擴展您的代理程式的外部工具。涵蓋傳輸類型、大型工具集的工具搜尋、身份驗證和錯誤處理。
- [使用工具搜尋擴展到許多工具](https://code.claude.com/docs/zh-TW/agent-sdk/tool-search.md): 通過動態發現和按需加載，將您的代理擴展到數千個工具。
- [SDK 中的子代理](https://code.claude.com/docs/zh-TW/agent-sdk/subagents.md): 定義並調用子代理以隔離上下文、並行運行任務，以及在 Claude Agent SDK 應用程式中應用專門指令。

#### 自訂行為

- [修改系統提示詞](https://code.claude.com/docs/zh-TW/agent-sdk/modifying-system-prompts.md): 在 `claude_code` 預設和自訂系統提示詞之間選擇，並使用 CLAUDE.md、輸出樣式、append 或完全自訂提示詞來自訂行為。
- [使用 Skills 擴展 Agent](https://code.claude.com/docs/zh-TW/agent-sdk/skills.md): 控制 Claude 在 Claude Agent SDK 會話中可以調用的 Skills，按名稱分派命令，以及編寫會話發現的 Skills
- [SDK 中的 Plugins](https://code.claude.com/docs/zh-TW/agent-sdk/plugins.md): 通過 Agent SDK 加載自訂 plugins，以使用 skills、agents、hooks 和 MCP servers 擴展 Claude Code

#### 控制與可觀測性

- [設定權限](https://code.claude.com/docs/zh-TW/agent-sdk/permissions.md): 使用權限模式、hooks 和宣告式允許/拒絕規則來控制您的代理程式如何使用工具。
- [使用 hooks 攔截和控制代理行為](https://code.claude.com/docs/zh-TW/agent-sdk/hooks.md): 在代理執行的關鍵點使用 hooks 攔截和自訂代理行為
- [使用 checkpointing 回溯檔案變更](https://code.claude.com/docs/zh-TW/agent-sdk/file-checkpointing.md): 追蹤代理程式工作階段期間的檔案變更，並將檔案還原到任何先前的狀態
- [追蹤成本和使用量](https://code.claude.com/docs/zh-TW/agent-sdk/cost-tracking.md): 了解如何追蹤 token 使用量、估計成本，以及使用 Claude Agent SDK 設定 prompt caching。
- [使用 OpenTelemetry 進行可觀測性](https://code.claude.com/docs/zh-TW/agent-sdk/observability.md): 使用 OpenTelemetry 將追蹤、指標和事件從 Agent SDK 匯出到您的可觀測性後端。
- [追蹤待辦事項](https://code.claude.com/docs/zh-TW/agent-sdk/todo-tracking.md): 在 Agent SDK 工作階段中追蹤待辦事項，並從結構化工具呼叫在應用程式中呈現 Claude 的進度

#### 部署

- [代理 SDK 的託管](https://code.claude.com/docs/zh-TW/agent-sdk/hosting.md): 在生產環境中部署 Agent SDK：子程序架構、工作階段持久化、擴展、可觀測性，以及針對 Docker、Kubernetes 和沙箱提供者的多租戶隔離。
- [安全部署 AI 代理](https://code.claude.com/docs/zh-TW/agent-sdk/secure-deployment.md): 一份關於使用隔離、認證管理和網路控制來保護 Claude Code 和 Agent SDK 部署的指南

#### SDK 參考資料

- [Agent SDK 參考 - TypeScript](https://code.claude.com/docs/zh-TW/agent-sdk/typescript.md): TypeScript Agent SDK 的完整 API 參考，包括所有函數、類型和介面。
- [TypeScript SDK V2 會話 API（已移除）](https://code.claude.com/docs/zh-TW/agent-sdk/typescript-v2-preview.md): 已移除的 V2 TypeScript Agent SDK 會話 API 參考，具有用於多輪對話的基於會話的 send/stream 模式。
- [Agent SDK 參考 - Python](https://code.claude.com/docs/zh-TW/agent-sdk/python.md): Python Agent SDK 的完整 API 參考，包括所有函數、類型和類別。

### 最新消息

#### 最新消息

- [最新動態](https://code.claude.com/docs/zh-TW/whats-new/index.md): Claude Code 功能的每週摘要，包含程式碼片段、示範和背景說明。
- [第 37 週 · 2026 年 9 月 7–11 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w37.md): 使用 claude plugin eval 測試您的外掛程式，並將 Claude Code Desktop 窗格彈出到各自的視窗中。
- [第 36 週 · 8 月 31 日 – 9 月 4 日，2026 年](https://code.claude.com/docs/zh-TW/whats-new/2026-w36.md): 切換至 Claude Fable 5.1，讓電腦使用在 Desktop 上於背景執行，並在即時 /diff 面板中觀看 Claude 的編輯。
- [第 35 週 · 2026 年 8 月 24–28 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w35.md): 在 Claude Code Desktop 應用程式中復原終端機工作階段、檢閱 Claude 為您起草的意見回饋報告，以及在受限模式中啟動工作階段。
- [第 34 週 · 2026 年 8 月 17–21 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w34.md): 使用 /design 技能草擬可編輯的 UI 畫板、設定簡潔輸出風格，以及從手機在您的機器上啟動 Claude Code 工作階段。
- [第 33 週 · 2026 年 8 月 10–14 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w33.md): Claude Code Desktop 在使用限制重設後自動繼續，Fork 模式預設開啟，GitLab 合併請求和市集加入 GitHub。
- [第 32 週 · 2026 年 8 月 3–7 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w32.md): Claude Code 工作階段可以互相傳送訊息、自託管環境在您的基礎設施上執行雲端工作階段，以及自動模式成為預設權限模式。
- [第 30 週 · 7 月 20–24 日，2026 年](https://code.claude.com/docs/zh-TW/whats-new/2026-w30.md): Opus 5 成為預設的 Opus 模型，Claude Code Desktop 新增 iOS Simulator 窗格，Claude Security plugin 掃描您的程式碼以尋找漏洞。
- [第 29 週 · 2026 年 7 月 13–17 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w29.md): 透過 MCP 連接器將即時資料拉入已發佈的成品中，並在新的螢幕閱讀器模式中使用 Claude Code 搭配螢幕閱讀器。
- [第 28 週 · 2026 年 7 月 6–10 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w28.md): 從桌面應用程式的內建瀏覽器瀏覽外部網站、使用 /doctor 執行完整設定檢查，以及取得自動模式文字記錄保護和代理程式檢視升級。
- [第 27 週 · 6 月 29 日 – 7 月 3 日，2026 年](https://code.claude.com/docs/zh-TW/whats-new/2026-w27.md): Claude Sonnet 5 成為預設模型，Claude in Chrome 達到正式推出，子代理預設在背景執行，Claude Desktop 在 Linux 上推出測試版，/radio 調頻至 Claude FM。
- [第 26 週 · 2026 年 6 月 22–26 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w26.md): 使用 claude mcp login 從您的 shell 驗證 MCP 伺服器，使用 ! 前綴取得 shell 模式命令輸出的回應，以及使用 /rewind 從 /clear 之前恢復對話。
- [第 25 週 · 2026 年 6 月 15–19 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w25.md): 從您的工作階段使用 Artifacts 發佈即時可分享的頁面、在拒絕和詢問規則中比對工具參數，以及使用 /config 從提示設定任何設定。
- [第 24 週 · 2026 年 6 月 8–12 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w24.md): 使用 /cd 將工作階段移至新目錄、讓子代理程式產生自己的子代理程式，以及使用安全模式對損壞的設定進行故障排除。
- [第 23 週 · 2026 年 6 月 1–5 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w23.md): 在 Amazon Bedrock、Google Cloud 的 Agent Platform 和 Microsoft Foundry 上執行自動模式，在 acceptEdits 模式下提示寫入可執行程式碼的檔案，使用 /plugin list 列出已安裝的外掛程式，以及為受管部署要求已核准的版本範圍。
- [第 22 週 · 5 月 25–29 日，2026 年](https://code.claude.com/docs/zh-TW/whats-new/2026-w22.md): 在 Claude Opus 4.8 上執行 Claude Code、使用動態工作流程協調大型任務、使用 security-guidance 外掛程式捕捉安全問題，以及以更低的價格在 Opus 4.8 上使用快速模式。
- [第 21 週 · 2026 年 5 月 18–22 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w21.md): 在 Pro 方案上使用 auto mode 並搭配 Sonnet 4.6，在 /usage 中查看哪些 skills、subagents 和 MCP servers 推動您的方案限制，並使用新的 /code-review 命令檢查差異。
- [第 20 週 · 2026 年 5 月 11–15 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w20.md): 從一個螢幕管理每個 Claude Code 工作階段，使用代理檢視，讓 Claude 持續朝著目標工作直到條件成立，並在 Opus 4.7 上預設執行快速模式。
- [第 19 週 · 2026 年 5 月 4–8 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w19.md): 從 .zip 檔案和 URL 載入 plugins，使用 Ctrl+R 搜尋所有專案的命令歷史記錄，從本機 HEAD 或遠端預設分支建立新 worktrees，以及使用 auto mode hard deny 規則無條件地阻止操作。
- [第 18 週 · 4 月 27 日 – 5 月 1 日，2026 年](https://code.claude.com/docs/zh-TW/whats-new/2026-w18.md): Claude Code 在 Windows 上無需 Git Bash 即可運行，claude auth login 在瀏覽器回調無法到達 localhost 時接受貼上的 OAuth 代碼，claude project purge 清理每個專案的本地狀態，將 PR URL 貼到 /resume 中可找到建立該會話的會話。
- [第 17 週 · 2026 年 4 月 20–24 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w17.md): /ultrareview 作為研究預覽版開放，當您返回終端時自動生成會話摘要，您可以在插件中構建和發佈自訂色彩主題，以及重新設計的網頁版 Claude Code。
- [第 16 週 · 2026 年 4 月 13–17 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w16.md): Claude Opus 4.7 搭配新的 xhigh 努力等級、Claude Code 網頁版上的 Routines、行動推播通知在 Claude 需要您時 ping 您的手機、顯示限制驅動因素的 /usage 細目分析，以及取代捆綁 JavaScript 的原生二進位檔。
- [第 15 週 · 2026 年 4 月 6–10 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w15.md): Ultraplan 雲端規劃、具有自我調整 /loop 的 Monitor 工具、用於打包設定的 /team-onboarding，以及從終端執行的 /autofix-pr。
- [第 14 週 · 3 月 30 日 – 4 月 3 日，2026 年](https://code.claude.com/docs/zh-TW/whats-new/2026-w14.md): CLI 中的電腦使用、互動式產品內課程、無閃爍渲染、按工具 MCP 結果大小覆蓋，以及 PATH 上的外掛程式可執行檔。
- [第 13 週 · 2026 年 3 月 23–27 日](https://code.claude.com/docs/zh-TW/whats-new/2026-w13.md): 自動模式用於免提權限、內建電腦使用、雲端 PR 自動修復、文字稿搜尋，以及適用於 Windows 的 PowerShell 工具。

### 資源

#### 資源

- [法律和合規](https://code.claude.com/docs/zh-TW/legal-and-compliance.md): Claude Code 的法律協議、合規認證和安全資訊。
