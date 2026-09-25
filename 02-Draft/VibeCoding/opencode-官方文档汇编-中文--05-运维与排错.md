---
title: opencode 官方文档汇编（中文） · 05-运维与排错
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-zh-ecosystem.md
- VibeCoding/opencode/opencode-zh-references.md
- VibeCoding/opencode/opencode-zh-troubleshooting.md
- VibeCoding/opencode/opencode-zh-windows-wsl.md
evidence: E1
domain: VibeCoding
keywords:
- opencode
- vibe-coding
- AI编程
- claude-code
state:
  phase: draft
  time_raw: 2026-09-23 02:44:23+08:00
  time_draft: 2026-09-23 03:14:06+08:00
  time_wiki: '2026-09-23T10:40:21+08:00'
wiki_ref: 03-Wiki/氛围编程/_MOC-氛围编程.md
---

> **汇编性质**：opencode 官方文档 官方原文 4 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## ecosystem

- 官方原文：https://opencode.ai/docs/zh-cn/ecosystem
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-ecosystem.md`

基于 OpenCode 构建的社区项目合集。

:::note
想将您的 OpenCode 相关项目添加到此列表中？欢迎提交 PR。

您还可以查看 [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) 和 [opencode.cafe](https://opencode.cafe)，这是一个聚合生态系统与社区资源的社区。

---

## 插件

| 名称                                                                                               | 描述                                                                   |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [opencode-daytona](https://github.com/daytonaio/daytona/tree/main/libs/opencode-plugin)            | 在隔离的 Daytona 沙箱中自动运行 OpenCode 会话，支持 git 同步和实时预览 |
| [opencode-helicone-session](https://github.com/H2Shami/opencode-helicone-session)                  | 自动注入 Helicone 会话头信息，用于请求分组                             |
| [opencode-type-inject](https://github.com/nick-vi/opencode-type-inject)                            | 通过查找工具自动将 TypeScript/Svelte 类型注入到文件读取中              |
| [opencode-openai-codex-auth](https://github.com/numman-ali/opencode-openai-codex-auth)             | 使用您的 ChatGPT Plus/Pro 订阅替代 API 额度                            |
| [opencode-gemini-auth](https://github.com/jenslys/opencode-gemini-auth)                            | 使用您现有的 Gemini 套餐替代 API 计费                                  |
| [opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)                | 使用 Antigravity 的免费模型替代 API 计费                               |
| [opencode-devcontainers](https://github.com/athal7/opencode-devcontainers)                         | 多分支开发容器隔离，支持浅克隆和自动分配端口                           |
| [opencode-google-antigravity-auth](https://github.com/shekohex/opencode-google-antigravity-auth)   | Google Antigravity OAuth 插件，支持 Google 搜索及更强健的 API 处理     |
| [opencode-dynamic-context-pruning](https://github.com/Tarquinen/opencode-dynamic-context-pruning)  | 通过修剪过时的工具输出来优化 Token 使用                                |
| [opencode-vibeguard](https://github.com/inkdust2021/opencode-vibeguard)                            | 在调用 LLM 之前将机密/PII 替换为 VibeGuard 风格的占位符；并在本地恢复  |
| [opencode-websearch-cited](https://github.com/ghoulr/opencode-websearch-cited.git)                 | 为受支持的提供商添加原生网页搜索支持，采用 Google grounded 风格        |
| [opencode-pty](https://github.com/shekohex/opencode-pty.git)                                       | 使 AI 代理能够在 PTY 中运行后台进程，并向其发送交互式输入              |
| [opencode-shell-strategy](https://github.com/JRedeker/opencode-shell-strategy)                     | 非交互式 shell 命令指令——防止依赖 TTY 的操作导致挂起                   |
| [opencode-wakatime](https://github.com/angristan/opencode-wakatime)                                | 使用 Wakatime 追踪 OpenCode 的使用情况                                 |
| [opencode-md-table-formatter](https://github.com/franlol/opencode-md-table-formatter/tree/main)    | 清理 LLM 生成的 Markdown 表格                                          |
| [opencode-morph-plugin](https://github.com/morphllm/opencode-morph-plugin)                         | 通过 Morph 提供 Fast Apply 编辑、WarpGrep 代码搜索和上下文压缩         |
| [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)                                   | 后台代理、预构建的 LSP/AST/MCP 工具、精选代理，兼容 Claude Code        |
| [opencode-notificator](https://github.com/panta82/opencode-notificator)                            | OpenCode 会话的桌面通知和声音提醒                                      |
| [opencode-notifier](https://github.com/mohak34/opencode-notifier)                                  | 针对权限请求、任务完成和错误事件的桌面通知与声音提醒                   |
| [opencode-zellij-namer](https://github.com/24601/opencode-zellij-namer)                            | 基于 OpenCode 上下文的 AI 驱动自动 Zellij 会话命名                     |
| [opencode-skillful](https://github.com/zenobi-us/opencode-skillful)                                | 允许 OpenCode 代理通过技能发现和注入按需延迟加载提示词                 |
| [opencode-supermemory](https://github.com/supermemoryai/opencode-supermemory)                      | 使用 Supermemory 实现跨会话的持久记忆                                  |
| [@plannotator/opencode](https://github.com/backnotprop/plannotator/tree/main/apps/opencode-plugin) | 支持可视化标注和私有/离线分享的交互式计划审查                          |
| [@openspoon/subtask2](https://github.com/spoons-and-mirrors/subtask2)                              | 将 OpenCode /commands 扩展为具有精细流程控制的强大编排系统             |
| [opencode-scheduler](https://github.com/different-ai/opencode-scheduler)                           | 使用 cron 语法通过 launchd (Mac) 或 systemd (Linux) 调度周期性任务     |
| [micode](https://github.com/vtemian/micode)                                                        | 结构化的头脑风暴 → 计划 → 实现工作流，支持会话连续性                   |
| [octto](https://github.com/vtemian/octto)                                                          | 用于 AI 头脑风暴的交互式浏览器 UI，支持多问题表单                      |
| [opencode-background-agents](https://github.com/kdcokenny/opencode-background-agents)              | Claude Code 风格的后台代理，支持异步委托和上下文持久化                 |
| [opencode-notify](https://github.com/kdcokenny/opencode-notify)                                    | OpenCode 的原生操作系统通知——随时了解任务完成情况                      |
| [opencode-workspace](https://github.com/kdcokenny/opencode-workspace)                              | 捆绑式多代理编排套件——16 个组件，一次安装                              |
| [opencode-worktree](https://github.com/kdcokenny/opencode-worktree)                                | OpenCode 的零摩擦 git worktree 管理                                    |
| [opencode-sentry-monitor](https://github.com/stolinski/opencode-sentry-monitor)                    | 使用 Sentry AI Monitoring 追踪和调试您的 AI 代理                       |

---

## 项目

| 名称                                                                                       | 描述                                                          |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| [kimaki](https://github.com/remorses/kimaki)                                               | 用于控制 OpenCode 会话的 Discord 机器人，基于 SDK 构建        |
| [opencode.nvim](https://github.com/NickvanDyke/opencode.nvim)                              | Neovim 插件，提供编辑器感知的提示词，基于 API 构建            |
| [portal](https://github.com/hosenur/portal)                                                | 通过 Tailscale/VPN 使用的移动优先 OpenCode Web UI             |
| [opencode plugin template](https://github.com/zenobi-us/opencode-plugin-template/)         | 用于构建 OpenCode 插件的模板                                  |
| [opencode.nvim](https://github.com/sudo-tee/opencode.nvim)                                 | OpenCode 的 Neovim 前端——基于终端的 AI 编码代理               |
| [ai-sdk-provider-opencode-sdk](https://github.com/ben-vargas/ai-sdk-provider-opencode-sdk) | Vercel AI SDK 提供商，用于通过 @opencode-ai/sdk 使用 OpenCode |
| [OpenChamber](https://github.com/btriapitsyn/openchamber)                                  | OpenCode 的 Web / 桌面应用和 VS Code 扩展                     |
| [OpenCode-Obsidian](https://github.com/mtymek/opencode-obsidian)                           | 将 OpenCode 嵌入 Obsidian UI 的 Obsidian 插件                 |
| [OpenWork](https://github.com/different-ai/openwork)                                       | Claude Cowork 的开源替代方案，由 OpenCode 驱动                |
| [ocx](https://github.com/kdcokenny/ocx)                                                    | OpenCode 扩展管理器，支持可移植的隔离配置                     |
| [CodeNomad](https://github.com/NeuralNomadsAI/CodeNomad)                                   | OpenCode 的桌面、Web、移动和远程客户端应用                    |

---

## 代理

| 名称                                                              | 描述                                     |
| ----------------------------------------------------------------- | ---------------------------------------- |
| [Agentic](https://github.com/Cluster444/agentic)                  | 用于结构化开发的模块化 AI 代理和命令     |
| [opencode-agents](https://github.com/darrenhinde/opencode-agents) | 用于增强工作流的配置、提示词、代理和插件 |

---

## References

- 官方原文：https://opencode.ai/docs/zh-cn/references
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-references.md`

# References

Add local directories and Git repositories as project references. 

此内容尚不支持你的语言。 

References give OpenCode access to directories outside the current project. Use them to make documentation, shared libraries, examples, or another repository available while you work.

References are configured by alias in opencode.json or opencode.jsonc.
 
- opencode.jsonc{ "$schema": "https://opencode.ai/config.json", "references": { "docs": { "path": "../product-docs", "description": "Use for product behavior and documentation conventions", }, "sdk": { "repository": "anomalyco/opencode-sdk-js", "branch": "main", "description": "Use for JavaScript SDK implementation details", }, },}

## Local directories

Use path to reference a local directory.
opencode.jsonc{ "references": { "docs": { "path": "../docs", }, },}
Paths can be:

Relative to the config file that defines the reference

- Absolute, such as /home/user/docs

- Relative to your home directory, such as ~/docs
 

You can also use a string shorthand:
 opencode.jsonc 

{ "references": { "docs": "../docs", },}

## Git repositories

Use repository to reference a Git repository. OpenCode materializes the repository in its local repository cache and makes the checked-out source available as a reference directory.
 opencode.jsonc 

{ "references": { "effect": { "repository": "Effect-TS/effect", "branch": "main", }, },}
repository accepts Git URLs, host/path references, and GitHub owner/repo shorthand. The optional branch field selects a branch or ref. Without branch, OpenCode uses the repository’s default branch.

You can use string shorthand when you do not need a branch, description, or other options:
 opencode.jsonc 

{ "references": { "effect": "Effect-TS/effect", },}
 Note 

Git references are refreshed asynchronously. A newly configured repository may take a moment to finish cloning or updating. 
 

## Describe usage

Add description to explain when an agent should use a reference.
 opencode.jsonc 

{ "references": { "design-system": { "path": "../design-system", "description": "Use when implementing UI components or design tokens", }, },}
OpenCode includes references with descriptions in agent context. Descriptions should be short and specific enough to distinguish references with similar content. References without descriptions remain available through autocomplete and direct use, but are not advertised to agents.
 

## Hide autocomplete entries

Set hidden to true to omit a reference from @ autocomplete in the TUI.
 opencode.jsonc 

{ "references": { "internal": { "path": "../internal", "description": "Use for internal implementation details", "hidden": true, }, },}
hidden only affects autocomplete. A hidden reference with a description remains included in agent context.
 

## Use references

Configured references appear in TUI @ autocomplete. Type @alias to attach the reference root, or @alias/ to search for files inside it.
 

Compare this implementation with @sdk/src/client.ts
Agents also receive the resolved paths and descriptions of configured references that have descriptions in their system context, so they can inspect a reference when it is relevant without you attaching it manually.

OpenCode automatically allows reference directories through its external-directory permission boundary. Normal tool permissions still apply; for example, an agent that cannot edit files does not gain edit access because a directory is configured as a reference.
 

## Configure fields

 Field Local Git Description path Yes No Local reference directory repository No Yes Git URL, host/path, or GitHub owner/repo value branch No Yes Optional Git branch or ref description Yes Yes Guidance describing when to use the reference hidden Yes Yes Hide the reference from TUI @ autocomplete 

Reference aliases cannot be empty or contain /, whitespace, backticks, or commas.

---

## or

- 官方原文：https://opencode.ai/docs/zh-cn/troubleshooting
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-troubleshooting.md`

要调试 OpenCode 的问题，请先检查其存储在磁盘上的日志和本地数据。

---

## 日志

日志文件写入位置：

- **macOS/Linux**: `~/.local/share/opencode/log/`
- **Windows**: 按 `WIN+R` 并粘贴 `%USERPROFILE%\.local\share\opencode\log`

日志文件以时间戳命名（例如 `2025-01-09T123456.log`），并保留最近的 10 个日志文件。

你可以通过 `--log-level` 命令行选项设置日志级别以获取更详细的调试信息。例如：`opencode --log-level DEBUG`。

---

## 存储

OpenCode 将会话数据和其他应用数据存储在磁盘上：

- **macOS/Linux**: `~/.local/share/opencode/`
- **Windows**: 按 `WIN+R` 并粘贴 `%USERPROFILE%\.local\share\opencode`

该目录包含：

- `auth.json` - 身份验证数据，如 API 密钥、OAuth Token
- `log/` - 应用日志
- `project/` - 项目特定数据，如会话和消息数据
  - 如果项目位于 Git 仓库中，则存储在 `./<project-slug>/storage/`
  - 如果不是 Git 仓库，则存储在 `./global/storage/`

---

## 桌面应用

OpenCode Desktop 会在后台运行一个本地 OpenCode 服务器（即 `opencode-cli` 附属进程）。大多数问题是由插件异常、缓存损坏或错误的服务器设置引起的。

### 快速检查

- 完全退出并重新启动应用。
- 如果应用显示错误页面，请点击**重新启动**并复制错误详情。
- 仅限 macOS：`OpenCode` 菜单 -> **Reload Webview**（当 UI 空白或冻结时有效）。

---

### 禁用插件

如果桌面应用在启动时崩溃、卡住或行为异常，请先禁用插件。

#### 检查全局配置

打开你的全局配置文件，查找 `plugin` 键。

- **macOS/Linux**: `~/.config/opencode/opencode.jsonc`（或 `~/.config/opencode/opencode.json`）
- **macOS/Linux**（旧版安装）: `~/.local/share/opencode/opencode.jsonc`
- **Windows**: 按 `WIN+R` 并粘贴 `%USERPROFILE%\.config\opencode\opencode.jsonc`

如果你配置了插件，请通过移除该键或将其设置为空数组来临时禁用它们：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [],
}
```

#### 检查插件目录

OpenCode 还可以从磁盘加载本地插件。临时将这些插件移走（或重命名文件夹），然后重新启动桌面应用：

- **全局插件**
  - **macOS/Linux**: `~/.config/opencode/plugins/`
  - **Windows**: 按 `WIN+R` 并粘贴 `%USERPROFILE%\.config\opencode\plugins`
- **项目插件**（仅当你使用了项目级配置时）
  - `<your-project>/.opencode/plugins/`

如果应用恢复正常，请逐个重新启用插件，找出导致问题的那个。

---

### 清除缓存

如果禁用插件没有帮助（或插件安装卡住了），请清除缓存以便 OpenCode 重新构建。

1. 完全退出 OpenCode Desktop。
2. 删除缓存目录：

- **macOS**: Finder -> `Cmd+Shift+G` -> 粘贴 `~/.cache/opencode`
- **Linux**: 删除 `~/.cache/opencode`（或运行 `rm -rf ~/.cache/opencode`）
- **Windows**: 按 `WIN+R` 并粘贴 `%USERPROFILE%\.cache\opencode`

3. 重新启动 OpenCode Desktop。

---

### 修复服务器连接问题

OpenCode Desktop 可以启动自己的本地服务器（默认行为），也可以连接到你配置的服务器 URL。

如果你看到**"Connection Failed"**对话框（或应用始终停留在启动画面），请检查自定义服务器 URL。

#### 清除桌面默认服务器 URL

在主页面上，点击服务器名称（带有状态指示点）以打开服务器选择器。在**默认服务器**部分，点击**清除**。

#### 从配置中移除 `server.port` / `server.hostname`

如果你的 `opencode.json(c)` 包含 `server` 部分，请临时移除该部分并重新启动桌面应用。

#### 检查环境变量

如果你在环境中设置了 `OPENCODE_PORT`，桌面应用将尝试使用该端口作为本地服务器端口。

- 取消设置 `OPENCODE_PORT`（或选择一个空闲端口）并重新启动。

---

### Linux: Wayland / X11 问题

在 Linux 上，某些 Wayland 设置可能会导致窗口空白或合成器错误。

- 如果你使用 Wayland 且应用出现空白或崩溃，请尝试使用 `OC_ALLOW_WAYLAND=1` 启动。
- 如果情况变得更糟，请移除该设置并尝试在 X11 会话下启动。

---

### Windows: WebView2 运行时

在 Windows 上，OpenCode Desktop 需要 Microsoft Edge **WebView2 Runtime**。如果应用打开后是空白窗口或无法启动，请安装或更新 WebView2 后重试。

---

### Windows: 常见性能问题

如果你在 Windows 上遇到性能缓慢、文件访问问题或终端问题，请尝试使用 [WSL (Windows Subsystem for Linux)](/docs/windows-wsl)。WSL 提供了一个 Linux 环境，能更好地与 OpenCode 的功能兼容。

---

### 通知不显示

OpenCode Desktop 仅在以下情况下显示系统通知：

- 在操作系统设置中已为 OpenCode 启用通知，且
- 应用窗口未处于焦点状态。

---

### 重置桌面应用存储（最后手段）

如果应用无法启动且你无法从 UI 内部清除设置，请重置桌面应用的保存状态。

1. 退出 OpenCode Desktop。
2. 找到并删除以下文件（它们位于 OpenCode Desktop 应用数据目录中）：

- `opencode.settings.dat`（桌面默认服务器 URL）
- `opencode.global.dat` 和 `opencode.workspace.*.dat`（UI 状态，如最近的服务器/项目）

快速找到该目录：

- **macOS**: Finder -> `Cmd+Shift+G` -> `~/Library/Application Support`（然后搜索上述文件名）
- **Linux**: 在 `~/.local/share` 下搜索上述文件名
- **Windows**: 按 `WIN+R` -> `%APPDATA%`（然后搜索上述文件名）

---

## 获取帮助

如果你遇到 OpenCode 的问题：

1. **在 GitHub 上报告问题**

   报告 Bug 或请求功能的最佳方式是通过我们的 GitHub 仓库：

   [**github.com/anomalyco/opencode/issues**](https://github.com/anomalyco/opencode/issues)

   在创建新 Issue 之前，请先搜索已有的 Issue，看看你的问题是否已被报告。

2. **加入我们的 Discord**

   如需实时帮助和社区讨论，请加入我们的 Discord 服务器：

   [**opencode.ai/discord**](https://opencode.ai/discord)

---

## 常见问题

以下是一些常见问题及其解决方法。

---

### OpenCode 无法启动

1. 检查日志中的错误消息
2. 尝试使用 `--print-logs` 运行以在终端中查看输出
3. 使用 `opencode upgrade` 确保你使用的是最新版本

---

### 身份验证问题

1. 尝试在 TUI 中使用 `/connect` 命令重新进行身份验证
2. 检查你的 API 密钥是否有效
3. 确保你的网络允许连接到提供商的 API

---

### 模型不可用

1. 检查你是否已通过提供商的身份验证
2. 验证配置中的模型名称是否正确
3. 某些模型可能需要特定的访问权限或订阅

如果你遇到 `ProviderModelNotFoundError`，很可能是在某处错误地引用了模型。
模型应按如下方式引用：`<providerId>/<modelId>`

示例：

- `openai/gpt-4.1`
- `openrouter/google/gemini-2.5-flash`
- `opencode/kimi-k2`

要查看你有权访问哪些模型，请运行 `opencode models`

---

### ProviderInitError

如果你遇到 ProviderInitError，很可能是配置无效或已损坏。

要解决此问题：

1. 首先，按照[提供商指南](/docs/providers)验证你的提供商是否已正确设置
2. 如果问题仍然存在，请尝试清除已存储的配置：

   ```bash
   rm -rf ~/.local/share/opencode
   ```

   在 Windows 上，按 `WIN+R` 并删除：`%USERPROFILE%\.local\share\opencode`

3. 在 TUI 中使用 `/connect` 命令重新与提供商进行身份验证。

---

### AI_APICallError 和提供商包问题

如果你遇到 API 调用错误，可能是由于提供商包过期导致的。OpenCode 会根据需要动态安装提供商包（OpenAI、Anthropic、Google 等）并将它们缓存到本地。

要解决提供商包问题：

1. 清除提供商包缓存：

   ```bash
   rm -rf ~/.cache/opencode
   ```

   在 Windows 上，按 `WIN+R` 并删除：`%USERPROFILE%\.cache\opencode`

2. 重新启动 OpenCode 以重新安装最新的提供商包

这将强制 OpenCode 下载最新版本的提供商包，通常可以解决模型参数和 API 变更带来的兼容性问题。

---

### 在 Linux 上复制/粘贴不可用

Linux 用户需要安装以下剪贴板工具之一，复制/粘贴功能才能正常工作：

**对于 X11 系统：**

```bash
apt install -y xclip
# or
apt install -y xsel
```

**对于 Wayland 系统：**

```bash
apt install -y wl-clipboard
```

**对于无头环境：**

```bash
apt install -y xvfb
# and run:
Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &
export DISPLAY=:99.0
```

OpenCode 会检测你是否正在使用 Wayland 并优先使用 `wl-clipboard`，否则将按以下顺序尝试查找剪贴板工具：`xclip` 和 `xsel`。

---

## windows-wsl

- 官方原文：https://opencode.ai/docs/zh-cn/windows-wsl
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-windows-wsl.md`

虽然 OpenCode 可以直接在 Windows 上运行，但我们推荐使用 [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) 以获得最佳体验。WSL 提供了一个 Linux 环境，能够与 OpenCode 的各项功能无缝配合。

:::tip[为什么选择 WSL？]
WSL 提供更出色的文件系统性能、完整的终端支持，以及与 OpenCode 所依赖的开发工具的良好兼容性。

---

## 安装配置

1. **安装 WSL**

   如果尚未安装，请参照 Microsoft 官方指南[安装 WSL](https://learn.microsoft.com/en-us/windows/wsl/install)。

2. **在 WSL 中安装 OpenCode**

   WSL 设置完成后，打开 WSL 终端，使用任一[安装方式](/docs/)安装 OpenCode。

   ```bash
   curl -fsSL https://opencode.ai/install | bash
   ```

3. **从 WSL 中使用 OpenCode**

   导航到你的项目目录（通过 `/mnt/c/`、`/mnt/d/` 等路径访问 Windows 文件），然后运行 OpenCode。

   ```bash
   cd /mnt/c/Users/YourName/project
   opencode
   ```

---

## 桌面应用 + WSL 服务器

如果你希望使用 OpenCode 桌面应用，同时在 WSL 中运行服务器：

1. **在 WSL 中启动服务器**，添加 `--hostname 0.0.0.0` 以允许外部连接：

   ```bash
   opencode serve --hostname 0.0.0.0 --port 4096
   ```

2. **在桌面应用中连接到** `http://localhost:4096`

:::note
如果 `localhost` 在你的环境中无法使用，请改用 WSL 的 IP 地址进行连接（在 WSL 中运行：`hostname -I`），使用 `http://<wsl-ip>:4096`。

:::caution
使用 `--hostname 0.0.0.0` 时，请设置 `OPENCODE_SERVER_PASSWORD` 以保护服务器安全。

```bash
OPENCODE_SERVER_PASSWORD=your-password opencode serve --hostname 0.0.0.0
```

---

## Web 客户端 + WSL

要在 Windows 上获得最佳的 Web 体验：

1. **在 WSL 终端中运行 `opencode web`**，而非在 PowerShell 中运行：

   ```bash
   opencode web --hostname 0.0.0.0
   ```

2. **在 Windows 浏览器中访问** `http://localhost:<port>`（OpenCode 会输出该 URL）

从 WSL 中运行 `opencode web` 可确保正确的文件系统访问和终端集成，同时仍可通过 Windows 浏览器进行访问。

---

## 访问 Windows 文件

WSL 可以通过 `/mnt/` 目录访问你的所有 Windows 文件：

- `C:` 盘 → `/mnt/c/`
- `D:` 盘 → `/mnt/d/`
- 其他盘符以此类推...

示例：

```bash
cd /mnt/c/Users/YourName/Documents/project
opencode
```

:::tip
为了获得更流畅的体验，建议将仓库克隆或复制到 WSL 文件系统中（例如 `~/code/` 目录下），然后在该位置运行 OpenCode。

---

## 使用技巧

- 对于存储在 Windows 驱动器上的项目，在 WSL 中运行 OpenCode 即可无缝访问文件
- 搭配 VS Code 的 [WSL 扩展](https://code.visualstudio.com/docs/remote/wsl) 使用 OpenCode，打造一体化的开发工作流
- OpenCode 的配置和会话数据存储在 WSL 环境中的 `~/.local/share/opencode/`
