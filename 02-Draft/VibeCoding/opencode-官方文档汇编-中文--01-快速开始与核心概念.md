---
title: opencode 官方文档汇编（中文） · 01-快速开始与核心概念
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-zh-cli.md
- VibeCoding/opencode/opencode-zh-commands.md
- VibeCoding/opencode/opencode-zh-keybinds.md
- VibeCoding/opencode/opencode-zh-models.md
- VibeCoding/opencode/opencode-zh-providers.md
- VibeCoding/opencode/opencode-zh-tui.md
- VibeCoding/opencode/opencode-zh-zen.md
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

> **汇编性质**：opencode 官方文档 官方原文 7 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## Start the backend server for web/mobile access

- 官方原文：https://opencode.ai/docs/zh-cn/cli
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-cli.md`

OpenCode CLI 在不带任何参数运行时，默认启动 [TUI](/docs/tui)。

```bash
opencode
```

但它也接受本页面中记录的命令，使您可以通过编程方式与 OpenCode 进行交互。

```bash
opencode run "Explain how closures work in JavaScript"
```

---

### tui

启动 OpenCode 终端用户界面。

```bash
opencode [project]
```

#### 标志

| 标志                                     | 简写 | 描述                                                      |
| ---------------------------------------- | ---- | --------------------------------------------------------- |
| <nobr><code>{"--continue"}</code></nobr> | `-c` | 继续上一个会话                                            |
| <nobr><code>{"--session"}</code></nobr>  | `-s` | 要继续的会话 ID                                           |
| <nobr><code>{"--fork"}</code></nobr>     |      | 继续时分叉会话（与 `--continue` 或 `--session` 配合使用） |
| <nobr><code>{"--prompt"}</code></nobr>   |      | 要使用的提示词                                            |
| <nobr><code>{"--model"}</code></nobr>    | `-m` | 要使用的模型，格式为 provider/model                       |
| <nobr><code>{"--agent"}</code></nobr>    |      | 要使用的代理                                              |
| <nobr><code>{"--port"}</code></nobr>     |      | 监听端口                                                  |
| <nobr><code>{"--hostname"}</code></nobr> |      | 监听主机名                                                |

---

## 命令

OpenCode CLI 还提供以下命令。

---

### agent

管理 OpenCode 的代理。

```bash
opencode agent [command]
```

---

### attach

将终端连接到已通过 `serve` 或 `web` 命令启动的 OpenCode 后端服务器。

```bash
opencode attach [url]
```

这允许将 TUI 与远程 OpenCode 后端配合使用。例如：

```bash
# Start the backend server for web/mobile access
opencode web --port 4096 --hostname 0.0.0.0

# In another terminal, attach the TUI to the running backend
opencode attach http://10.20.30.40:4096
```

#### 标志

| 标志                                     | 简写 | 描述                                                                |
| ---------------------------------------- | ---- | ------------------------------------------------------------------- |
| <nobr><code>{"--dir"}</code></nobr>      |      | 启动 TUI 的工作目录                                                 |
| <nobr><code>{"--continue"}</code></nobr> | `-c` | 继续上一个会话                                                      |
| <nobr><code>{"--session"}</code></nobr>  | `-s` | 要继续的会话 ID                                                     |
| <nobr><code>{"--fork"}</code></nobr>     |      | 继续时派生会话（与 `--continue` 或 `--session` 一起使用）           |
| <nobr><code>{"--password"}</code></nobr> | `-p` | 基本认证密码（默认使用 `OPENCODE_SERVER_PASSWORD`）                 |
| <nobr><code>{"--username"}</code></nobr> | `-u` | 基本认证用户名（默认使用 `OPENCODE_SERVER_USERNAME` 或 `opencode`） |

---

#### create

使用自定义配置创建新的代理。

```bash
opencode agent create
```

此命令将引导您使用自定义系统提示词和工具配置来创建新的代理。

---

#### list

列出所有可用的代理。

```bash
opencode agent list
```

---

### auth

管理提供商的凭据和登录信息的命令。

```bash
opencode auth [command]
```

---

#### login

OpenCode 基于 [Models.dev](https://models.dev) 的提供商列表运行，因此您可以使用 `opencode auth login` 为任何想要使用的提供商配置 API 密钥。密钥存储在 `~/.local/share/opencode/auth.json` 中。

```bash
opencode auth login
```

OpenCode 启动时会从凭据文件加载提供商信息，同时也会加载环境变量或项目中 `.env` 文件中定义的密钥。

---

#### list

列出凭据文件中存储的所有已认证提供商。

```bash
opencode auth list
```

或使用简写版本。

```bash
opencode auth ls
```

---

#### logout

从凭据文件中清除提供商信息以完成登出。

```bash
opencode auth logout
```

---

### github

管理用于仓库自动化的 GitHub 代理。

```bash
opencode github [command]
```

---

#### install

在您的仓库中安装 GitHub 代理。

```bash
opencode github install
```

此命令会设置必要的 GitHub Actions 工作流并引导您完成配置过程。[了解更多](/docs/github)。

---

#### run

运行 GitHub 代理。通常在 GitHub Actions 中使用。

```bash
opencode github run
```

##### 标志

| 标志                                  | 描述                           |
| ------------------------------------- | ------------------------------ |
| <nobr><code>{"--event"}</code></nobr> | 用于运行代理的 GitHub 模拟事件 |
| <nobr><code>{"--token"}</code></nobr> | GitHub 个人访问令牌            |

---

### mcp

管理 Model Context Protocol 服务器。

```bash
opencode mcp [command]
```

---

#### add

将 MCP 服务器添加到您的配置中。

```bash
opencode mcp add
```

此命令将引导您添加本地或远程 MCP 服务器。

---

#### list

列出所有已配置的 MCP 服务器及其连接状态。

```bash
opencode mcp list
```

或使用简写版本。

```bash
opencode mcp ls
```

---

#### auth

对支持 OAuth 的 MCP 服务器进行认证。

```bash
opencode mcp auth [name]
```

如果您不提供服务器名称，系统将提示您从可用的支持 OAuth 的服务器中进行选择。

您还可以列出支持 OAuth 的服务器及其认证状态。

```bash
opencode mcp auth list
```

或使用简写版本。

```bash
opencode mcp auth ls
```

---

#### logout

移除 MCP 服务器的 OAuth 凭据。

```bash
opencode mcp logout [name]
```

---

#### debug

调试 MCP 服务器的 OAuth 连接问题。

```bash
opencode mcp debug <name>
```

---

### models

列出已配置提供商的所有可用模型。

```bash
opencode models [provider]
```

此命令以 `provider/model` 的格式显示所有已配置提供商中可用的模型。

这对于确定在[配置文件](/docs/config/)中使用的确切模型名称非常有用。

您可以选择传入提供商 ID 来按提供商筛选模型。

```bash
opencode models anthropic
```

#### 标志

| 标志                                    | 描述                                     |
| --------------------------------------- | ---------------------------------------- |
| <nobr><code>{"--refresh"}</code></nobr> | 从 models.dev 刷新模型缓存               |
| <nobr><code>{"--verbose"}</code></nobr> | 使用更详细的模型输出（包含费用等元数据） |

使用 `--refresh` 标志可以更新缓存的模型列表。当提供商新增了模型并且您希望在 OpenCode 中看到它们时，此功能非常有用。

```bash
opencode models --refresh
```

---

### run

以非交互模式运行 OpenCode，直接传入提示词。

```bash
opencode run [message..]
```

这对于脚本编写、自动化或无需启动完整 TUI 即可快速获取答案的场景非常有用。例如：

```bash "opencode run"
opencode run Explain the use of context in Go
```

您还可以连接到正在运行的 `opencode serve` 实例，以避免每次运行时 MCP 服务器的冷启动时间：

```bash
# Start a headless server in one terminal
opencode serve

# In another terminal, run commands that attach to it
opencode run --attach http://localhost:4096 "Explain async/await in JavaScript"
```

#### 标志

| 标志                                     | 简写 | 描述                                                                |
| ---------------------------------------- | ---- | ------------------------------------------------------------------- |
| <nobr><code>{"--command"}</code></nobr>  |      | 要运行的命令，使用 message 作为参数                                 |
| <nobr><code>{"--continue"}</code></nobr> | `-c` | 继续上一个会话                                                      |
| <nobr><code>{"--session"}</code></nobr>  | `-s` | 要继续的会话 ID                                                     |
| <nobr><code>{"--fork"}</code></nobr>     |      | 继续时分叉会话（与 `--continue` 或 `--session` 配合使用）           |
| <nobr><code>{"--share"}</code></nobr>    |      | 分享会话                                                            |
| <nobr><code>{"--model"}</code></nobr>    | `-m` | 要使用的模型，格式为 provider/model                                 |
| <nobr><code>{"--agent"}</code></nobr>    |      | 要使用的代理                                                        |
| <nobr><code>{"--file"}</code></nobr>     | `-f` | 附加到消息的文件                                                    |
| <nobr><code>{"--format"}</code></nobr>   |      | 格式：default（格式化输出）或 json（原始 JSON 事件）                |
| <nobr><code>{"--title"}</code></nobr>    |      | 会话标题（未提供值时使用截断的提示词）                              |
| <nobr><code>{"--attach"}</code></nobr>   |      | 连接到正在运行的 opencode 服务器（例如 http://localhost:4096）      |
| <nobr><code>{"--password"}</code></nobr> | `-p` | 基本认证密码（默认使用 `OPENCODE_SERVER_PASSWORD`）                 |
| <nobr><code>{"--username"}</code></nobr> | `-u` | 基本认证用户名（默认使用 `OPENCODE_SERVER_USERNAME` 或 `opencode`） |
| <nobr><code>{"--dir"}</code></nobr>      |      | 运行目录，或附加时远程服务器上的路径                                |
| <nobr><code>{"--variant"}</code></nobr>  |      | 模型变体（特定于提供商的推理级别）                                  |
| <nobr><code>{"--thinking"}</code></nobr> |      | 显示思考块                                                          |
| <nobr><code>{"--port"}</code></nobr>     |      | 本地服务器端口（默认为随机端口）                                    |

---

### serve

启动无界面的 OpenCode 服务器以提供 API 访问。查看[服务器文档](/docs/server)了解完整的 HTTP 接口。

```bash
opencode serve
```

此命令启动一个 HTTP 服务器，提供对 OpenCode 功能的 API 访问，无需 TUI 界面。设置 `OPENCODE_SERVER_PASSWORD` 可启用 HTTP 基本认证（用户名默认为 `opencode`）。

#### 标志

| 标志                                     | 描述                       |
| ---------------------------------------- | -------------------------- |
| <nobr><code>{"--port"}</code></nobr>     | 监听端口                   |
| <nobr><code>{"--hostname"}</code></nobr> | 监听主机名                 |
| <nobr><code>{"--mdns"}</code></nobr>     | 启用 mDNS 发现             |
| <nobr><code>{"--cors"}</code></nobr>     | 允许 CORS 的额外浏览器来源 |

---

### session

管理 OpenCode 会话。

```bash
opencode session [command]
```

---

#### list

列出所有 OpenCode 会话。

```bash
opencode session list
```

##### 标志

| 标志                                      | 简写 | 描述                                  |
| ----------------------------------------- | ---- | ------------------------------------- |
| <nobr><code>{"--max-count"}</code></nobr> | `-n` | 限制为最近 N 个会话                   |
| <nobr><code>{"--format"}</code></nobr>    |      | 输出格式：table 或 json（默认 table） |

---

### stats

显示 OpenCode 会话的 Token 用量和费用统计信息。

```bash
opencode stats
```

#### 标志

| 标志                                    | 描述                                                   |
| --------------------------------------- | ------------------------------------------------------ |
| <nobr><code>{"--days"}</code></nobr>    | 显示最近 N 天的统计信息（默认为所有时间）              |
| <nobr><code>{"--tools"}</code></nobr>   | 显示的工具数量（默认为全部）                           |
| <nobr><code>{"--models"}</code></nobr>  | 显示模型用量明细（默认隐藏）。传入数字可显示前 N 个    |
| <nobr><code>{"--project"}</code></nobr> | 按项目筛选（默认为所有项目，传入空字符串表示当前项目） |

---

### export

将会话数据导出为 JSON。

```bash
opencode export [sessionID]
```

如果您不提供会话 ID，系统将提示您从可用的会话中进行选择。

---

### import

从 JSON 文件或 OpenCode 分享链接导入会话数据。

```bash
opencode import <file>
```

您可以从本地文件或 OpenCode 分享链接导入。

```bash
opencode import session.json
opencode import https://opncd.ai/s/abc123
```

---

### web

启动带有 Web 界面的无界面 OpenCode 服务器。

```bash
opencode web
```

此命令启动一个 HTTP 服务器并打开浏览器，通过 Web 界面访问 OpenCode。设置 `OPENCODE_SERVER_PASSWORD` 可启用 HTTP 基本认证（用户名默认为 `opencode`）。

#### 标志

| 标志                                     | 描述                       |
| ---------------------------------------- | -------------------------- |
| <nobr><code>{"--port"}</code></nobr>     | 监听端口                   |
| <nobr><code>{"--hostname"}</code></nobr> | 监听主机名                 |
| <nobr><code>{"--mdns"}</code></nobr>     | 启用 mDNS 发现             |
| <nobr><code>{"--cors"}</code></nobr>     | 允许 CORS 的额外浏览器来源 |

---

### acp

启动 ACP（Agent Client Protocol）服务器。

```bash
opencode acp
```

此命令启动一个通过 stdin/stdout 使用 nd-JSON 进行通信的 ACP 服务器。

#### 标志

| 标志                                     | 描述       |
| ---------------------------------------- | ---------- |
| <nobr><code>{"--cwd"}</code></nobr>      | 工作目录   |
| <nobr><code>{"--port"}</code></nobr>     | 监听端口   |
| <nobr><code>{"--hostname"}</code></nobr> | 监听主机名 |

---

### uninstall

卸载 OpenCode 并删除所有相关文件。

```bash
opencode uninstall
```

#### 标志

| 标志                                        | 简写 | 描述                           |
| ------------------------------------------- | ---- | ------------------------------ |
| <nobr><code>{"--keep-config"}</code></nobr> | `-c` | 保留配置文件                   |
| <nobr><code>{"--keep-data"}</code></nobr>   | `-d` | 保留会话数据和快照             |
| <nobr><code>{"--dry-run"}</code></nobr>     |      | 显示将被删除的内容但不实际删除 |
| <nobr><code>{"--force"}</code></nobr>       | `-f` | 跳过确认提示                   |

---

### upgrade

将 OpenCode 更新到最新版本或指定版本。

```bash
opencode upgrade [target]
```

更新到最新版本。

```bash
opencode upgrade
```

更新到指定版本。

```bash
opencode upgrade v0.1.48
```

#### 标志

| 标志                                   | 简写 | 描述                                       |
| -------------------------------------- | ---- | ------------------------------------------ |
| <nobr><code>{"--method"}</code></nobr> | `-m` | 使用的安装方式：curl、npm、pnpm、bun、brew |

---

## 全局标志

OpenCode CLI 接受以下全局标志。

| 标志                                       | 简写 | 描述                                 |
| ------------------------------------------ | ---- | ------------------------------------ |
| <nobr><code>{"--help"}</code></nobr>       | `-h` | 显示帮助信息                         |
| <nobr><code>{"--version"}</code></nobr>    | `-v` | 打印版本号                           |
| <nobr><code>{"--print-logs"}</code></nobr> |      | 将日志输出到 stderr                  |
| <nobr><code>{"--log-level"}</code></nobr>  |      | 日志级别（DEBUG、INFO、WARN、ERROR） |

---

## 环境变量

OpenCode 可以通过环境变量进行配置。

| 变量                                  | 类型    | 描述                                    |
| ------------------------------------- | ------- | --------------------------------------- |
| `OPENCODE_AUTO_SHARE`                 | boolean | 自动分享会话                            |
| `OPENCODE_GIT_BASH_PATH`              | string  | Windows 上 Git Bash 可执行文件的路径    |
| `OPENCODE_CONFIG`                     | string  | 配置文件路径                            |
| `OPENCODE_TUI_CONFIG`                 | string  | TUI 配置文件路径                        |
| `OPENCODE_CONFIG_DIR`                 | string  | 配置目录路径                            |
| `OPENCODE_CONFIG_CONTENT`             | string  | 内联 JSON 配置内容                      |
| `OPENCODE_DISABLE_AUTOUPDATE`         | boolean | 禁用自动更新检查                        |
| `OPENCODE_DISABLE_PRUNE`              | boolean | 禁用旧数据清理                          |
| `OPENCODE_DISABLE_TERMINAL_TITLE`     | boolean | 禁用自动终端标题更新                    |
| `OPENCODE_PERMISSION`                 | string  | 内联 JSON 权限配置                      |
| `OPENCODE_DISABLE_DEFAULT_PLUGINS`    | boolean | 禁用默认插件                            |
| `OPENCODE_DISABLE_LSP_DOWNLOAD`       | boolean | 禁用 LSP 服务器自动下载                 |
| `OPENCODE_ENABLE_EXPERIMENTAL_MODELS` | boolean | 启用实验性模型                          |
| `OPENCODE_DISABLE_AUTOCOMPACT`        | boolean | 禁用自动上下文压缩                      |
| `OPENCODE_DISABLE_CLAUDE_CODE`        | boolean | 禁用读取 `.claude`（提示词 + 技能）     |
| `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT` | boolean | 禁用读取 `~/.claude/CLAUDE.md`          |
| `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS` | boolean | 禁用加载 `.claude/skills`               |
| `OPENCODE_DISABLE_MODELS_FETCH`       | boolean | 禁用从远程源获取模型                    |
| `OPENCODE_FAKE_VCS`                   | string  | 用于测试目的的模拟 VCS 提供商           |
| `OPENCODE_CLIENT`                     | string  | 客户端标识符（默认为 `cli`）            |
| `OPENCODE_ENABLE_EXA`                 | boolean | 启用 Exa 网络搜索工具                   |
| `OPENCODE_SERVER_PASSWORD`            | string  | 为 `serve`/`web` 启用基本认证           |
| `OPENCODE_SERVER_USERNAME`            | string  | 覆盖基本认证用户名（默认为 `opencode`） |
| `OPENCODE_MODELS_URL`                 | string  | 自定义模型配置获取 URL                  |

---

### 实验性功能

这些环境变量用于启用可能会更改或移除的实验性功能。

| 变量                                            | 类型    | 描述                            |
| ----------------------------------------------- | ------- | ------------------------------- |
| `OPENCODE_EXPERIMENTAL`                         | boolean | 启用受总开关控制的实验性功能    |
| `OPENCODE_EXPERIMENTAL_ICON_DISCOVERY`          | boolean | 启用图标发现                    |
| `OPENCODE_EXPERIMENTAL_DISABLE_COPY_ON_SELECT`  | boolean | 禁用 TUI 中的选中即复制         |
| `OPENCODE_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS` | number  | bash 命令的默认超时时间（毫秒） |
| `OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX`        | number  | LLM 响应的最大输出 Token 数     |
| `OPENCODE_EXPERIMENTAL_FILEWATCHER`             | boolean | 启用整个目录的文件监听器        |
| `OPENCODE_EXPERIMENTAL_OXFMT`                   | boolean | 启用 oxfmt 格式化器             |
| `OPENCODE_EXPERIMENTAL_LSP_TOOL`                | boolean | 启用实验性 LSP 工具             |
| `OPENCODE_EXPERIMENTAL_DISABLE_FILEWATCHER`     | boolean | 禁用文件监听器                  |
| `OPENCODE_EXPERIMENTAL_EXA`                     | boolean | 启用实验性 Exa 功能             |
| `OPENCODE_EXPERIMENTAL_LSP_TY`                  | boolean | 为 python 文件启用 TY LSP       |
| `OPENCODE_EXPERIMENTAL_PLAN_MODE`               | boolean | 启用计划模式                    |
| `OPENCODE_EXPERIMENTAL_BACKGROUND_SUBAGENTS`    | boolean | 启用后台子代理任务              |
| `OPENCODE_EXPERIMENTAL_EVENT_SYSTEM`            | boolean | 启用实验性事件系统              |
| `OPENCODE_EXPERIMENTAL_NATIVE_LLM`              | boolean | 启用原生 LLM 请求路径           |
| `OPENCODE_EXPERIMENTAL_PARALLEL`                | boolean | 启用并行 Web 搜索执行           |
| `OPENCODE_EXPERIMENTAL_SCOUT`                   | boolean | 启用 Scout 子代理               |
| `OPENCODE_EXPERIMENTAL_WORKSPACES`              | boolean | 启用工作区支持                  |

---

## commands

- 官方原文：https://opencode.ai/docs/zh-cn/commands
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-commands.md`

自定义命令允许你指定一个提示词，当在 TUI 中执行该命令时会运行这个提示词。

```bash frame="none"
/my-command
```

自定义命令是 `/init`、`/undo`、`/redo`、`/share`、`/help` 等内置命令之外的补充。[了解更多](/docs/tui#commands)。

---

## 创建命令文件

在 `commands/` 目录中创建 markdown 文件来定义自定义命令。

创建 `.opencode/commands/test.md`：

```md title=".opencode/commands/test.md"
---
description: Run tests with coverage
agent: build
model: anthropic/claude-3-5-sonnet-20241022
---

Run the full test suite with coverage report and show any failures.
Focus on the failing tests and suggest fixes.
```

frontmatter 定义命令属性，内容则成为模板。

通过输入 `/` 后跟命令名称来使用该命令。

```bash frame="none"
"/test"
```

---

## 配置

你可以通过 OpenCode 配置或在 `commands/` 目录中创建 markdown 文件来添加自定义命令。

---

### JSON

在 OpenCode [配置](/docs/config)中使用 `command` 选项：

```json title="opencode.jsonc" {4-12}
{
  "$schema": "https://opencode.ai/config.json",
  "command": {
    // This becomes the name of the command
    "test": {
      // This is the prompt that will be sent to the LLM
      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",
      // This is shown as the description in the TUI
      "description": "Run tests with coverage",
      "agent": "build",
      "model": "anthropic/claude-3-5-sonnet-20241022"
    }
  }
}
```

现在你可以在 TUI 中运行这个命令：

```bash frame="none"
/test
```

---

### Markdown

你还可以使用 markdown 文件定义命令。将它们放在：

- 全局：`~/.config/opencode/commands/`
- 项目级：`.opencode/commands/`

```markdown title="~/.config/opencode/commands/test.md"
---
description: Run tests with coverage
agent: build
model: anthropic/claude-3-5-sonnet-20241022
---

Run the full test suite with coverage report and show any failures.
Focus on the failing tests and suggest fixes.
```

markdown 文件名即为命令名。例如，`test.md` 允许你运行：

```bash frame="none"
/test
```

---

## 提示词配置

自定义命令的提示词支持多种特殊占位符和语法。

---

### 参数

使用 `$ARGUMENTS` 占位符向命令传递参数。

```md title=".opencode/commands/component.md"
---
description: Create a new component
---

Create a new React component named $ARGUMENTS with TypeScript support.
Include proper typing and basic structure.
```

带参数运行命令：

```bash frame="none"
/component Button
```

`$ARGUMENTS` 将被替换为 `Button`。

你还可以使用位置参数访问各个参数：

- `$1` - 第一个参数
- `$2` - 第二个参数
- `$3` - 第三个参数
- 以此类推...

例如：

```md title=".opencode/commands/create-file.md"
---
description: Create a new file with content
---

Create a file named $1 in the directory $2
with the following content: $3
```

运行命令：

```bash frame="none"
/create-file config.json src "{ \"key\": \"value\" }"
```

替换结果为：

- `$1` 替换为 `config.json`
- `$2` 替换为 `src`
- `$3` 替换为 `{ "key": "value" }`

---

### Shell 输出

使用 _!`command`_ 将 [bash 命令](/docs/tui#bash-commands)输出注入到提示词中。

例如，创建一个分析测试覆盖率的自定义命令：

```md title=".opencode/commands/analyze-coverage.md"
---
description: Analyze test coverage
---

Here are the current test results:
!`npm test`

Based on these results, suggest improvements to increase coverage.
```

或者查看最近的更改：

```md title=".opencode/commands/review-changes.md"
---
description: Review recent changes
---

Recent git commits:
!`git log --oneline -10`

Review these changes and suggest any improvements.
```

命令在项目的根目录中运行，其输出会成为提示词的一部分。

---

### 文件引用

使用 `@` 后跟文件名在命令中引用文件。

```md title=".opencode/commands/review-component.md"
---
description: Review component
---

Review the component in @src/components/Button.tsx.
Check for performance issues and suggest improvements.
```

文件内容会自动包含在提示词中。

---

## 选项

让我们详细了解各配置选项。

---

### Template

`template` 选项定义执行命令时发送给 LLM 的提示词。

```json title="opencode.json"
{
  "command": {
    "test": {
      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes."
    }
  }
}
```

这是一个**必需的**配置选项。

---

### Description

使用 `description` 选项提供命令功能的简要描述。

```json title="opencode.json"
{
  "command": {
    "test": {
      "description": "Run tests with coverage"
    }
  }
}
```

当你输入命令时，这将在 TUI 中显示为描述。

---

### Agent

使用 `agent` 配置可选地指定由哪个[代理](/docs/agents)执行此命令。
如果这是一个[子代理](/docs/agents/#subagents)，该命令默认会触发子代理调用。
要禁用此行为，请将 `subtask` 设置为 `false`。

```json title="opencode.json"
{
  "command": {
    "review": {
      "agent": "plan"
    }
  }
}
```

这是一个**可选的**配置选项。如果未指定，默认使用你当前的代理。

---

### Subtask

使用 `subtask` 布尔值强制命令触发[子代理](/docs/agents/#subagents)调用。
如果你希望命令不污染主要上下文，这会很有用，它会**强制**代理作为子代理运行，
即使[代理](/docs/agents)配置中的 `mode` 设置为 `primary`。

```json title="opencode.json"
{
  "command": {
    "analyze": {
      "subtask": true
    }
  }
}
```

这是一个**可选的**配置选项。

---

### Model

使用 `model` 配置覆盖此命令的默认模型。

```json title="opencode.json"
{
  "command": {
    "analyze": {
      "model": "anthropic/claude-3-5-sonnet-20241022"
    }
  }
}
```

这是一个**可选的**配置选项。

---

## 内置命令

opencode 包含多个内置命令，如 `/init`、`/undo`、`/redo`、`/share`、`/help`；[了解更多](/docs/tui#commands)。

:::note
自定义命令可以覆盖内置命令。

如果你定义了同名的自定义命令，它将覆盖内置命令。

---

## keybinds

- 官方原文：https://opencode.ai/docs/zh-cn/keybinds
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-keybinds.md`

OpenCode 提供了一系列快捷键，您可以通过 `tui.json` 进行自定义。

```json title="tui.json"
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    "leader": "ctrl+x",
    "app_exit": "ctrl+c,ctrl+d,<leader>q",
    "editor_open": "<leader>e",
    "theme_list": "<leader>t",
    "sidebar_toggle": "<leader>b",
    "scrollbar_toggle": "none",
    "username_toggle": "none",
    "status_view": "<leader>s",
    "tool_details": "none",
    "session_export": "<leader>x",
    "session_new": "<leader>n",
    "session_list": "<leader>l",
    "session_timeline": "<leader>g",
    "session_fork": "none",
    "session_rename": "none",
    "session_share": "none",
    "session_unshare": "none",
    "session_interrupt": "escape",
    "session_compact": "<leader>c",
    "session_child_first": "<leader>down",
    "session_child_cycle": "<leader>right",
    "session_child_cycle_reverse": "<leader>left",
    "session_parent": "<leader>up",
    "messages_page_up": "pageup,ctrl+alt+b",
    "messages_page_down": "pagedown,ctrl+alt+f",
    "messages_line_up": "ctrl+alt+y",
    "messages_line_down": "ctrl+alt+e",
    "messages_half_page_up": "ctrl+alt+u",
    "messages_half_page_down": "ctrl+alt+d",
    "messages_first": "ctrl+g,home",
    "messages_last": "ctrl+alt+g,end",
    "messages_next": "none",
    "messages_previous": "none",
    "messages_copy": "<leader>y",
    "messages_undo": "<leader>u",
    "messages_redo": "<leader>r",
    "messages_last_user": "none",
    "messages_toggle_conceal": "<leader>h",
    "model_list": "<leader>m",
    "model_cycle_recent": "f2",
    "model_cycle_recent_reverse": "shift+f2",
    "model_cycle_favorite": "none",
    "model_cycle_favorite_reverse": "none",
    "variant_cycle": "ctrl+t",
    "variant_list": "none",
    "command_list": "ctrl+p",
    "agent_list": "<leader>a",
    "agent_cycle": "tab",
    "agent_cycle_reverse": "shift+tab",
    "input_clear": "ctrl+c",
    "input_paste": "ctrl+v",
    "input_submit": "return",
    "input_newline": "shift+return,ctrl+return,alt+return,ctrl+j",
    "input_move_left": "left,ctrl+b",
    "input_move_right": "right,ctrl+f",
    "input_move_up": "up",
    "input_move_down": "down",
    "input_select_left": "shift+left",
    "input_select_right": "shift+right",
    "input_select_up": "shift+up",
    "input_select_down": "shift+down",
    "input_line_home": "ctrl+a",
    "input_line_end": "ctrl+e",
    "input_select_line_home": "ctrl+shift+a",
    "input_select_line_end": "ctrl+shift+e",
    "input_visual_line_home": "alt+a",
    "input_visual_line_end": "alt+e",
    "input_select_visual_line_home": "alt+shift+a",
    "input_select_visual_line_end": "alt+shift+e",
    "input_buffer_home": "home",
    "input_buffer_end": "end",
    "input_select_buffer_home": "shift+home",
    "input_select_buffer_end": "shift+end",
    "input_delete_line": "ctrl+shift+d",
    "input_delete_to_line_end": "ctrl+k",
    "input_delete_to_line_start": "ctrl+u",
    "input_backspace": "backspace,shift+backspace",
    "input_delete": "ctrl+d,delete,shift+delete",
    "input_undo": "ctrl+-,super+z",
    "input_redo": "ctrl+.,super+shift+z",
    "input_word_forward": "alt+f,alt+right,ctrl+right",
    "input_word_backward": "alt+b,alt+left,ctrl+left",
    "input_select_word_forward": "alt+shift+f,alt+shift+right",
    "input_select_word_backward": "alt+shift+b,alt+shift+left",
    "input_delete_word_forward": "alt+d,alt+delete,ctrl+delete",
    "input_delete_word_backward": "ctrl+w,ctrl+backspace,alt+backspace",
    "history_previous": "up",
    "history_next": "down",
    "terminal_suspend": "ctrl+z",
    "terminal_title_toggle": "none",
    "tips_toggle": "<leader>h",
    "display_thinking": "none"
  }
}
```

---

## 前导键

OpenCode 的大多数快捷键使用 `leader`（前导键）。这可以避免与终端中的其他快捷键冲突。

默认情况下，`ctrl+x` 是前导键，大多数操作需要您先按下前导键，然后再按对应的快捷键。例如，要新建一个会话，请先按 `ctrl+x`，然后按 `n`。

您不一定需要使用前导键来设置快捷键，但我们建议您这样做。

---

## 禁用快捷键

您可以通过将键值添加到 `tui.json` 并设置为 "none" 来禁用某个快捷键。

```json title="tui.json"
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    "session_compact": "none"
  }
}
```

---

## 桌面版提示词输入快捷键

OpenCode 桌面应用的提示词输入框支持常见的 Readline/Emacs 风格文本编辑快捷键。这些快捷键为内置功能，目前无法通过 `opencode.json` 进行配置。

| 快捷键   | 操作                              |
| -------- | --------------------------------- |
| `ctrl+a` | 移动到当前行的开头                |
| `ctrl+e` | 移动到当前行的末尾                |
| `ctrl+b` | 光标向后移动一个字符              |
| `ctrl+f` | 光标向前移动一个字符              |
| `alt+b`  | 光标向后移动一个单词              |
| `alt+f`  | 光标向前移动一个单词              |
| `ctrl+d` | 删除光标所在位置的字符            |
| `ctrl+k` | 删除从光标到行尾的内容            |
| `ctrl+u` | 删除从光标到行首的内容            |
| `ctrl+w` | 删除前一个单词                    |
| `alt+d`  | 删除后一个单词                    |
| `ctrl+t` | 交换光标前后的字符                |
| `ctrl+g` | 取消弹出窗口 / 中止正在运行的响应 |

---

## Shift+Enter

某些终端默认不会发送带修饰键的 Enter 键。您可能需要配置终端将 `Shift+Enter` 作为转义序列发送。

### Windows Terminal

打开您的 `settings.json` 文件，路径为：

```
%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
```

将以下内容添加到根级 `actions` 数组中：

```json
"actions": [
  {
    "command": {
      "action": "sendInput",
      "input": "\u001b[13;2u"
    },
    "id": "User.sendInput.ShiftEnterCustom"
  }
]
```

将以下内容添加到根级 `keybindings` 数组中：

```json
"keybindings": [
  {
    "keys": "shift+enter",
    "id": "User.sendInput.ShiftEnterCustom"
  }
]
```

保存文件并重启 Windows Terminal，或打开一个新标签页。

---

## models

- 官方原文：https://opencode.ai/docs/zh-cn/models
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-models.md`

OpenCode 使用 [AI SDK](https://ai-sdk.dev/) 和 [Models.dev](https://models.dev) 支持 **75+ LLM 提供商**，并支持运行本地模型。

---

## 提供商

大多数热门提供商已默认预加载。如果你通过 `/connect` 命令添加了提供商的凭据，它们将在你启动 OpenCode 时自动可用。

了解更多关于[提供商](/docs/providers)的信息。

---

## 选择模型

配置好提供商后，你可以通过输入以下命令来选择想要使用的模型：

```bash frame="none"
/models
```

---

## 推荐模型

市面上有非常多的模型，每周都有新模型发布。

:::tip
建议使用我们推荐的模型。

然而，真正擅长代码生成和工具调用的模型只有少数几个。

以下是与 OpenCode 配合良好的几个模型，排名不分先后（此列表并非详尽无遗，也不一定是最新的）：

- GPT 5.2
- GPT 5.1 Codex
- Claude Opus 4.5
- Claude Sonnet 4.5
- Minimax M2.1
- Gemini 3 Pro

---

## 设置默认模型

要将某个模型设为默认模型，可以在 OpenCode 配置中设置 `model` 字段。

```json title="opencode.json" {3}
{
  "$schema": "https://opencode.ai/config.json",
  "model": "lmstudio/google/gemma-3n-e4b"
}
```

这里完整的 ID 格式为 `provider_id/model_id`。例如，如果你使用 [OpenCode Zen](/docs/zen)，则 GPT 5.1 Codex 对应的值为 `opencode/gpt-5.1-codex`。

如果你配置了[自定义提供商](/docs/providers#custom)，`provider_id` 是配置中 `provider` 部分的键名，`model_id` 是 `provider.models` 中的键名。

---

## 配置模型

你可以通过配置文件全局配置模型的选项。

```jsonc title="opencode.jsonc" {7-12,19-24}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "openai": {
      "models": {
        "gpt-5": {
          "options": {
            "reasoningEffort": "high",
            "textVerbosity": "low",
            "reasoningSummary": "auto",
            "include": ["reasoning.encrypted_content"],
          },
        },
      },
    },
    "anthropic": {
      "models": {
        "claude-sonnet-4-5-20250929": {
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 16000,
            },
          },
        },
      },
    },
  },
}
```

这里我们为两个内置模型配置了全局设置：通过 `openai` 提供商访问的 `gpt-5`，以及通过 `anthropic` 提供商访问的 `claude-sonnet-4-20250514`。
内置的提供商和模型名称可以在 [Models.dev](https://models.dev) 上查阅。

你还可以为使用中的任何代理配置这些选项。代理配置会覆盖此处的全局选项。[了解更多](/docs/agents/#additional)。

你也可以定义扩展内置变体的自定义变体。变体允许你为同一个模型配置不同的设置，而无需创建重复的条目：

```jsonc title="opencode.jsonc" {6-21}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "opencode": {
      "models": {
        "gpt-5": {
          "variants": {
            "high": {
              "reasoningEffort": "high",
              "textVerbosity": "low",
              "reasoningSummary": "auto",
            },
            "low": {
              "reasoningEffort": "low",
              "textVerbosity": "low",
              "reasoningSummary": "auto",
            },
          },
        },
      },
    },
  },
}
```

---

## 变体

许多模型支持具有不同配置的多种变体。OpenCode 为热门提供商内置了默认变体。

### 内置变体

OpenCode 为许多提供商提供了默认变体：

**Anthropic**：

- `high` - 高思考预算（默认）
- `max` - 最大思考预算

**OpenAI**：

因模型而异，但大致如下：

- `none` - 无推理
- `minimal` - 极少推理
- `low` - 低推理
- `medium` - 中等推理
- `high` - 高推理
- `xhigh` - 超高推理

**Google**：

- `low` - 较低推理/Token 预算
- `high` - 较高推理/Token 预算

:::tip
此列表并不全面，许多其他提供商也有内置的默认变体。

### 自定义变体

你可以覆盖现有变体或添加自己的变体：

```jsonc title="opencode.jsonc" {7-18}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "openai": {
      "models": {
        "gpt-5": {
          "variants": {
            "thinking": {
              "reasoningEffort": "high",
              "textVerbosity": "low",
            },
            "fast": {
              "disabled": true,
            },
          },
        },
      },
    },
  },
}
```

### 切换变体

使用快捷键 `variant_cycle` 可以快速在变体之间切换。[了解更多](/docs/keybinds)。

---

## 加载模型

OpenCode 启动时，会按以下优先顺序加载模型：

1. `--model` 或 `-m` 命令行标志。格式与配置文件中相同：`provider_id/model_id`。

2. OpenCode 配置中的 model 字段。

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "model": "anthropic/claude-sonnet-4-20250514"
   }
   ```

   格式为 `provider/model`。

3. 上次使用的模型。

4. 按内部优先级排列的第一个可用模型。

---

## providers

- 官方原文：https://opencode.ai/docs/zh-cn/providers
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-providers.md`

export const console = config.console

OpenCode 使用 [AI SDK](https://ai-sdk.dev/) 和 [Models.dev](https://models.dev)，支持 **75+ LLM 提供商**，同时也支持运行本地模型。

要添加提供商，你需要：

1. 使用 `/connect` 命令添加提供商的 API 密钥。
2. 在 OpenCode 配置中设置该提供商。

---

### 凭据

使用 `/connect` 命令添加提供商的 API 密钥后，凭据会存储在
`~/.local/share/opencode/auth.json` 中。

---

### 配置

你可以通过 OpenCode 配置中的 `provider` 部分来自定义提供商。

---

#### 自定义 Base URL

你可以通过设置 `baseURL` 选项来自定义任何提供商的 Base URL。这在使用代理服务或自定义端点时非常有用。

```json title="opencode.json" {6}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "https://api.anthropic.com/v1"
      }
    }
  }
}
```

---

## OpenCode Zen

OpenCode Zen 是由 OpenCode 团队提供的模型列表，这些模型已经过测试和验证，能够与 OpenCode 良好配合使用。[了解更多](/docs/zen)。

:::tip
如果你是新用户，我们建议从 OpenCode Zen 开始。

1. 在 TUI 中执行 `/connect` 命令，选择 opencode，然后前往 [opencode.ai/auth](https://opencode.ai/auth)。

   ```txt
   /connect
   ```

2. 登录后添加账单信息，然后复制你的 API 密钥。

3. 粘贴你的 API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 在 TUI 中执行 `/models` 查看我们推荐的模型列表。

   ```txt
   /models
   ```

它的使用方式与 OpenCode 中的其他提供商完全相同，且完全可选。

---

## 目录

下面我们来详细了解一些提供商。如果你想将某个提供商添加到列表中，欢迎提交 PR。

:::note
没有看到你想要的提供商？欢迎提交 PR。

---

### 302.AI

1. 前往 [302.AI 控制台](https://302.ai/)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **302.AI**。

   ```txt
   /connect
   ```

3. 输入你的 302.AI API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

---

### Amazon Bedrock

要在 OpenCode 中使用 Amazon Bedrock：

1. 前往 Amazon Bedrock 控制台中的**模型目录**，申请访问你想要使用的模型。

   :::tip
   你需要先在 Amazon Bedrock 中获得对目标模型的访问权限。

2. 使用以下方法之一**配置身份验证**：

   ***

   #### 环境变量（快速上手）

   运行 opencode 时设置以下环境变量之一：

   ```bash
   # Option 1: Using AWS access keys
   AWS_ACCESS_KEY_ID=XXX AWS_SECRET_ACCESS_KEY=YYY opencode

   # Option 2: Using named AWS profile
   AWS_PROFILE=my-profile opencode

   # Option 3: Using Bedrock bearer token
   AWS_BEARER_TOKEN_BEDROCK=XXX opencode
   ```

   或者将它们添加到你的 bash 配置文件中：

   ```bash title="~/.bash_profile"
   export AWS_PROFILE=my-dev-profile
   export AWS_REGION=us-east-1
   ```

   ***

   #### 配置文件（推荐）

   如需项目级别或持久化的配置，请使用 `opencode.json`：

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "amazon-bedrock": {
         "options": {
           "region": "us-east-1",
           "profile": "my-aws-profile"
         }
       }
     }
   }
   ```

   **可用选项：**
   - `region` - AWS 区域（例如 `us-east-1`、`eu-west-1`）
   - `profile` - `~/.aws/credentials` 中的 AWS 命名配置文件
   - `endpoint` - VPC 端点的自定义端点 URL（通用 `baseURL` 选项的别名）

   :::tip
   配置文件中的选项优先级高于环境变量。

   ***

   #### 进阶：VPC 端点

   如果你使用 Bedrock 的 VPC 端点：

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "amazon-bedrock": {
         "options": {
           "region": "us-east-1",
           "profile": "production",
           "endpoint": "https://bedrock-runtime.us-east-1.vpce-xxxxx.amazonaws.com"
         }
       }
     }
   }
   ```

   :::note
   `endpoint` 选项是通用 `baseURL` 选项的别名，使用了 AWS 特有的术语。如果同时指定了 `endpoint` 和 `baseURL`，则 `endpoint` 优先。

   ***

   #### 认证方式
   - **`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`**：在 AWS 控制台中创建 IAM 用户并生成访问密钥
   - **`AWS_PROFILE`**：使用 `~/.aws/credentials` 中的命名配置文件。需要先通过 `aws configure --profile my-profile` 或 `aws sso login` 进行配置
   - **`AWS_BEARER_TOKEN_BEDROCK`**：从 Amazon Bedrock 控制台生成长期 API 密钥
   - **`AWS_WEB_IDENTITY_TOKEN_FILE` / `AWS_ROLE_ARN`**：适用于 EKS IRSA（服务账户的 IAM 角色）或其他支持 OIDC 联合的 Kubernetes 环境。使用服务账户注解时，Kubernetes 会自动注入这些环境变量。

   ***

   #### 认证优先级

   Amazon Bedrock 使用以下认证优先级：
   1. **Bearer Token** - `AWS_BEARER_TOKEN_BEDROCK` 环境变量或通过 `/connect` 命令获取的 Token
   2. **AWS 凭证链** - 配置文件、访问密钥、共享凭证、IAM 角色、Web Identity Token（EKS IRSA）、实例元数据

   :::note
   当设置了 Bearer Token（通过 `/connect` 或 `AWS_BEARER_TOKEN_BEDROCK`）时，它的优先级高于所有 AWS 凭证方式，包括已配置的配置文件。

3. 执行 `/models` 命令选择你想要的模型。

   ```txt
   /models
   ```

:::note
对于自定义推理配置文件，请在 key 中使用模型名称和提供商名称，并将 `id` 属性设置为 ARN。这可以确保正确的缓存行为：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "amazon-bedrock": {
      // ...
      "models": {
        "anthropic-claude-sonnet-4.5": {
          "id": "arn:aws:bedrock:us-east-1:xxx:application-inference-profile/yyy"
        }
      }
    }
  }
}
```

---

### Anthropic

1. 注册完成后，执行 `/connect` 命令并选择 Anthropic。

   ```txt
   /connect
   ```

2. 你可以选择 **Claude Pro/Max** 选项，浏览器会自动打开并要求你进行身份验证。

   ```txt
   ┌ Select auth method
   │
   │ Claude Pro/Max
   │ Create an API Key
   │ Manually enter API Key
   └
   ```

3. 现在使用 `/models` 命令即可看到所有 Anthropic 模型。

   ```txt
   /models
   ```

:::info
在 OpenCode 中使用 Claude Pro/Max 订阅不是 [Anthropic](https://anthropic.com) 官方支持的用法。

##### 使用 API 密钥

如果你没有 Pro/Max 订阅，也可以选择 **Create an API Key**。浏览器会自动打开并要求你登录 Anthropic，然后会提供一个代码供你粘贴到终端中。

如果你已经有 API 密钥，可以选择 **Manually enter API Key** 并将其粘贴到终端中。

---

### Atomic Chat

你可以通过 [Atomic Chat](https://atomic.chat) 配置 opencode 以使用本地模型。Atomic Chat 是一款桌面应用程序，它在 OpenAI 兼容的 API 服务器后面运行本地 LLM（默认端点 `http://127.0.0.1:1337/v1`）。

```json title="opencode.json" "atomic-chat" {5, 6, 8, 10-14}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "atomic-chat": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Atomic Chat (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1337/v1"
      },
      "models": {
        "<your-model-id>": {
          "name": "<your-model-name>"
        }
      }
    }
  }
}
```

在此示例中：

- `atomic-chat` 是自定义的提供商 ID。可以是任何你想要的字符串。
- `npm` 指定此提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来连接任何 OpenAI 兼容的 API。
- `name` 是提供商在界面中显示的名称。
- `options.baseURL` 是本地服务器的端点。根据你的 Atomic Chat 设置修改主机和端口。
- `models` 是模型 ID 到其显示名称的映射。每个 ID 必须与 `GET /v1/models` 返回的 `id` 匹配——运行 `curl http://127.0.0.1:1337/v1/models` 可列出 Atomic Chat 当前已加载的 ID。

:::tip
如果工具调用工作不佳，请选择一个对 tool calling 支持较好的已加载模型（例如 Qwen-Coder 或 DeepSeek-Coder 的变体）。

---

### Azure OpenAI

:::note
如果遇到 "I'm sorry, but I cannot assist with that request" 错误，请尝试将 Azure 资源中的内容过滤器从 **DefaultV2** 更改为 **Default**。

1. 前往 [Azure 门户](https://portal.azure.com/)并创建 **Azure OpenAI** 资源。你需要：
   - **资源名称**：这会成为你的 API 端点的一部分（`https://RESOURCE_NAME.openai.azure.com/`）
   - **API 密钥**：资源中的 `KEY 1` 或 `KEY 2`

2. 前往 [Azure AI Foundry](https://ai.azure.com/) 并部署一个模型。

   :::note
   部署名称必须与模型名称一致，OpenCode 才能正常工作。

3. 执行 `/connect` 命令并搜索 **Azure**。

   ```txt
   /connect
   ```

4. 输入你的 API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

5. 将资源名称设置为环境变量：

   ```bash
   AZURE_RESOURCE_NAME=XXX opencode
   ```

   或者添加到你的 bash 配置文件中：

   ```bash title="~/.bash_profile"
   export AZURE_RESOURCE_NAME=XXX
   ```

6. 执行 `/models` 命令选择你已部署的模型。

   ```txt
   /models
   ```

---

### Azure Cognitive Services

1. 前往 [Azure 门户](https://portal.azure.com/)并创建 **Azure OpenAI** 资源。你需要：
   - **资源名称**：这会成为你的 API 端点的一部分（`https://AZURE_COGNITIVE_SERVICES_RESOURCE_NAME.cognitiveservices.azure.com/`）
   - **API 密钥**：资源中的 `KEY 1` 或 `KEY 2`

2. 前往 [Azure AI Foundry](https://ai.azure.com/) 并部署一个模型。

   :::note
   部署名称必须与模型名称一致，OpenCode 才能正常工作。

3. 执行 `/connect` 命令并搜索 **Azure Cognitive Services**。

   ```txt
   /connect
   ```

4. 输入你的 API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

5. 将资源名称设置为环境变量：

   ```bash
   AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX opencode
   ```

   或者添加到你的 bash 配置文件中：

   ```bash title="~/.bash_profile"
   export AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX
   ```

6. 执行 `/models` 命令选择你已部署的模型。

   ```txt
   /models
   ```

---

### Baseten

1. 前往 [Baseten](https://app.baseten.co/)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **Baseten**。

   ```txt
   /connect
   ```

3. 输入你的 Baseten API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

---

### Cerebras

1. 前往 [Cerebras 控制台](https://inference.cerebras.ai/)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **Cerebras**。

   ```txt
   /connect
   ```

3. 输入你的 Cerebras API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Qwen 3 Coder 480B_。

   ```txt
   /models
   ```

---

### Cloudflare AI Gateway

Cloudflare AI Gateway 允许你通过统一端点访问来自 OpenAI、Anthropic、Workers AI 等提供商的模型。通过 [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/)，你无需为每个提供商单独准备 API 密钥。

1. 前往 [Cloudflare 仪表盘](https://dash.cloudflare.com/)，导航到 **AI** > **AI Gateway**，创建一个新的网关。

2. 将你的 Account ID 和 Gateway ID 设置为环境变量。

   ```bash title="~/.bash_profile"
   export CLOUDFLARE_ACCOUNT_ID=your-32-character-account-id
   export CLOUDFLARE_GATEWAY_ID=your-gateway-id
   ```

3. 执行 `/connect` 命令并搜索 **Cloudflare AI Gateway**。

   ```txt
   /connect
   ```

4. 输入你的 Cloudflare API Token。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

   或者将其设置为环境变量。

   ```bash title="~/.bash_profile"
   export CLOUDFLARE_API_TOKEN=your-api-token
   ```

5. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

   你也可以通过 OpenCode 配置添加模型。

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "cloudflare-ai-gateway": {
         "models": {
           "openai/gpt-4o": {},
           "anthropic/claude-sonnet-4": {}
         }
       }
     }
   }
   ```

---

### Cortecs

1. 前往 [Cortecs 控制台](https://cortecs.ai/)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **Cortecs**。

   ```txt
   /connect
   ```

3. 输入你的 Cortecs API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_。

   ```txt
   /models
   ```

---

### DeepSeek

1. 前往 [DeepSeek 控制台](https://platform.deepseek.com/)，创建账户并点击 **Create new API key**。

2. 执行 `/connect` 命令并搜索 **DeepSeek**。

   ```txt
   /connect
   ```

3. 输入你的 DeepSeek API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择 DeepSeek 模型，例如 _DeepSeek V4 Pro_。

   ```txt
   /models
   ```

---

### Deep Infra

1. 前往 [Deep Infra 仪表盘](https://deepinfra.com/dash)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **Deep Infra**。

   ```txt
   /connect
   ```

3. 输入你的 Deep Infra API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

---

### FrogBot

1. 前往 [FrogBot 仪表盘](https://app.frogbot.ai/signup)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **FrogBot**。

   ```txt
   /connect
   ```

3. 输入你的 FrogBot API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

---

### Fireworks AI

1. 前往 [Fireworks AI 控制台](https://app.fireworks.ai/)，创建账户并点击 **Create API Key**。

2. 执行 `/connect` 命令并搜索 **Fireworks AI**。

   ```txt
   /connect
   ```

3. 输入你的 Fireworks AI API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_。

   ```txt
   /models
   ```

---

### GitLab Duo

GitLab Duo 通过 GitLab 的 Anthropic 代理提供具有原生工具调用能力的 AI 驱动的代理聊天。

1. 执行 `/connect` 命令并选择 GitLab。

   ```txt
   /connect
   ```

2. 选择你的身份验证方式：

   ```txt
   ┌ Select auth method
   │
   │ OAuth (Recommended)
   │ Personal Access Token
   └
   ```

   #### 使用 OAuth（推荐）

   选择 **OAuth**，浏览器会自动打开进行授权。

   #### 使用个人访问令牌
   1. 前往 [GitLab 用户设置 > Access Tokens](https://gitlab.com/-/user_settings/personal_access_tokens)
   2. 点击 **Add new token**
   3. 名称填写 `OpenCode`，范围选择 `api`
   4. 复制令牌（以 `glpat-` 开头）
   5. 在终端中输入该令牌

3. 执行 `/models` 命令查看可用模型。

   ```txt
   /models
   ```

   提供三个基于 Claude 的模型：
   - **duo-chat-haiku-4-5**（默认）- 快速响应，适合简单任务
   - **duo-chat-sonnet-4-5** - 性能均衡，适合大多数工作流
   - **duo-chat-opus-4-5** - 最强大，适合复杂分析

:::note
你也可以通过指定 `GITLAB_TOKEN` 环境变量来避免将令牌存储在 OpenCode 的认证存储中。

##### 自托管 GitLab

:::note[合规说明]
OpenCode 会使用一个小模型来执行部分 AI 任务，例如生成会话标题。默认情况下使用由 Zen 托管的 gpt-5-nano。如果你需要让 OpenCode 仅使用你自己的 GitLab 托管实例，请在 `opencode.json` 文件中添加以下内容。同时建议禁用会话共享。

```json
{
  "$schema": "https://opencode.ai/config.json",
  "small_model": "gitlab/duo-chat-haiku-4-5",
  "share": "disabled"
}
```

对于自托管 GitLab 实例：

```bash
export GITLAB_INSTANCE_URL=https://gitlab.company.com
export GITLAB_TOKEN=glpat-...
```

如果你的实例运行了自定义 AI Gateway：

```bash
GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com
```

或者添加到你的 bash 配置文件中：

```bash title="~/.bash_profile"
export GITLAB_INSTANCE_URL=https://gitlab.company.com
export GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com
export GITLAB_TOKEN=glpat-...
```

:::note
你的 GitLab 管理员必须启用以下功能：

1. 为用户、群组或实例启用 [Duo Agent Platform](https://docs.gitlab.com/user/duo_agent_platform/turn_on_off/)
2. 功能标志（通过 Rails 控制台）：
   - `agent_platform_claude_code`
   - `third_party_agents_enabled`

##### 自托管实例的 OAuth

要在自托管实例上使用 OAuth，你需要创建一个新应用（设置 → 应用），回调 URL 设置为 `http://127.0.0.1:8080/callback`，并选择以下范围：

- api（代表你访问 API）
- read_user（读取你的个人信息）
- read_repository（允许对仓库进行只读访问）

然后将应用 ID 导出为环境变量：

```bash
export GITLAB_OAUTH_CLIENT_ID=your_application_id_here
```

更多文档请参阅 [opencode-gitlab-auth](https://www.npmjs.com/package/opencode-gitlab-auth) 主页。

##### 配置

通过 `opencode.json` 进行自定义配置：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "gitlab": {
      "options": {
        "instanceUrl": "https://gitlab.com"
      }
    }
  }
}
```

##### GitLab API 工具（可选，但强烈推荐）

要访问 GitLab 工具（合并请求、Issue、流水线、CI/CD 等）：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-gitlab-plugin"]
}
```

该插件提供全面的 GitLab 仓库管理功能，包括 MR 审查、Issue 跟踪、流水线监控等。

---

### GitHub Copilot

要在 OpenCode 中使用你的 GitHub Copilot 订阅：

:::note
部分模型可能需要 [Pro+ 订阅](https://github.com/features/copilot/plans)才能使用。

1. 执行 `/connect` 命令并搜索 GitHub Copilot。

   ```txt
   /connect
   ```

2. 前往 [github.com/login/device](https://github.com/login/device) 并输入验证码。

   ```txt
   ┌ Login with GitHub Copilot
   │
   │ https://github.com/login/device
   │
   │ Enter code: 8F43-6FCF
   │
   └ Waiting for authorization...
   ```

3. 现在执行 `/models` 命令选择你想要的模型。

   ```txt
   /models
   ```

---

### Google Vertex AI

要在 OpenCode 中使用 Google Vertex AI：

1. 前往 Google Cloud Console 中的**模型花园**，查看你所在区域可用的模型。

   :::note
   你需要一个启用了 Vertex AI API 的 Google Cloud 项目。

2. 设置所需的环境变量：
   - `GOOGLE_CLOUD_PROJECT`：你的 Google Cloud 项目 ID
   - `VERTEX_LOCATION`（可选）：Vertex AI 的区域（默认为 `global`）
   - 身份验证（选择其一）：
     - `GOOGLE_APPLICATION_CREDENTIALS`：服务账户 JSON 密钥文件的路径
     - 使用 gcloud CLI 进行身份验证：`gcloud auth application-default login`

   在运行 opencode 时设置：

   ```bash
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json GOOGLE_CLOUD_PROJECT=your-project-id opencode
   ```

   或者添加到你的 bash 配置文件中：

   ```bash title="~/.bash_profile"
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
   export GOOGLE_CLOUD_PROJECT=your-project-id
   export VERTEX_LOCATION=global
   ```

:::tip
`global` 区域可以提高可用性并减少错误，且不会产生额外费用。如果有数据驻留需求，请使用区域端点（例如 `us-central1`）。[了解更多](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#regional_and_global_endpoints)

3. 执行 `/models` 命令选择你想要的模型。

   ```txt
   /models
   ```

---

### Groq

1. 前往 [Groq 控制台](https://console.groq.com/)，点击 **Create API Key** 并复制密钥。

2. 执行 `/connect` 命令并搜索 Groq。

   ```txt
   /connect
   ```

3. 输入该提供商的 API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择你想要的模型。

   ```txt
   /models
   ```

---

### Hugging Face

[Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) 提供对由 17+ 提供商支持的开放模型的访问。

1. 前往 [Hugging Face 设置](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained)，创建一个具有调用 Inference Providers 权限的令牌。

2. 执行 `/connect` 命令并搜索 **Hugging Face**。

   ```txt
   /connect
   ```

3. 输入你的 Hugging Face 令牌。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Kimi-K2-Instruct_ 或 _GLM-4.6_。

   ```txt
   /models
   ```

---

### Helicone

[Helicone](https://helicone.ai) 是一个 LLM 可观测性平台，为你的 AI 应用提供日志记录、监控和分析功能。Helicone AI Gateway 会根据模型自动将请求路由到对应的提供商。

1. 前往 [Helicone](https://helicone.ai)，创建账户并在仪表盘中生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **Helicone**。

   ```txt
   /connect
   ```

3. 输入你的 Helicone API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

如需了解更多提供商以及缓存、速率限制等高级功能，请查阅 [Helicone 文档](https://docs.helicone.ai)。

#### 可选配置

如果 Helicone 的某些功能或模型未通过 OpenCode 自动配置，你随时可以手动配置。

[Helicone 模型目录](https://helicone.ai/models)中可以找到你需要添加的模型 ID。

```jsonc title="~/.config/opencode/opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "helicone": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Helicone",
      "options": {
        "baseURL": "https://ai-gateway.helicone.ai",
      },
      "models": {
        "gpt-4o": {
          // Model ID (from Helicone's model directory page)
          "name": "GPT-4o", // Your own custom name for the model
        },
        "claude-sonnet-4-20250514": {
          "name": "Claude Sonnet 4",
        },
      },
    },
  },
}
```

#### 自定义请求头

Helicone 支持用于缓存、用户跟踪和会话管理等功能的自定义请求头。使用 `options.headers` 将它们添加到提供商配置中：

```jsonc title="~/.config/opencode/opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "helicone": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Helicone",
      "options": {
        "baseURL": "https://ai-gateway.helicone.ai",
        "headers": {
          "Helicone-Cache-Enabled": "true",
          "Helicone-User-Id": "opencode",
        },
      },
    },
  },
}
```

##### 会话跟踪

Helicone 的 [Sessions](https://docs.helicone.ai/features/sessions) 功能允许你将相关的 LLM 请求归为一组。使用 [opencode-helicone-session](https://github.com/H2Shami/opencode-helicone-session) 插件可以自动将每个 OpenCode 对话记录为 Helicone 中的一个会话。

```bash
npm install -g opencode-helicone-session
```

将其添加到配置中。

```json title="opencode.json"
{
  "plugin": ["opencode-helicone-session"]
}
```

该插件会在你的请求中注入 `Helicone-Session-Id` 和 `Helicone-Session-Name` 请求头。在 Helicone 的 Sessions 页面中，你可以看到每个 OpenCode 对话都作为独立的会话列出。

##### 常用 Helicone 请求头

| 请求头                     | 描述                                                   |
| -------------------------- | ------------------------------------------------------ |
| `Helicone-Cache-Enabled`   | 启用响应缓存（`true`/`false`）                         |
| `Helicone-User-Id`         | 按用户跟踪指标                                         |
| `Helicone-Property-[Name]` | 添加自定义属性（例如 `Helicone-Property-Environment`） |
| `Helicone-Prompt-Id`       | 将请求与提示词版本关联                                 |

有关所有可用请求头，请参阅 [Helicone Header Directory](https://docs.helicone.ai/helicone-headers/header-directory)。

---

### llama.cpp

你可以通过 [llama.cpp](https://github.com/ggml-org/llama.cpp) 的 llama-server 工具配置 OpenCode 使用本地模型。

```json title="opencode.json" "llama.cpp" {5, 6, 8, 10-15}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "llama.cpp": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "llama-server (local)",
      "options": {
        "baseURL": "http://127.0.0.1:8080/v1"
      },
      "models": {
        "qwen3-coder:a3b": {
          "name": "Qwen3-Coder: a3b-30b (local)",
          "limit": {
            "context": 128000,
            "output": 65536
          }
        }
      }
    }
  }
}
```

在这个示例中：

- `llama.cpp` 是自定义的提供商 ID，可以是任意字符串。
- `npm` 指定该提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来兼容任何 OpenAI 兼容的 API。
- `name` 是该提供商在 UI 中显示的名称。
- `options.baseURL` 是本地服务器的端点地址。
- `models` 是模型 ID 到其配置的映射。模型名称会显示在模型选择列表中。

---

### IO.NET

IO.NET 提供 17 个针对不同用例优化的模型：

1. 前往 [IO.NET 控制台](https://ai.io.net/)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **IO.NET**。

   ```txt
   /connect
   ```

3. 输入你的 IO.NET API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

---

### LM Studio

你可以通过 LM Studio 配置 OpenCode 使用本地模型。

```json title="opencode.json" "lmstudio" {5, 6, 8, 10-14}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1"
      },
      "models": {
        "google/gemma-3n-e4b": {
          "name": "Gemma 3n-e4b (local)"
        }
      }
    }
  }
}
```

在这个示例中：

- `lmstudio` 是自定义的提供商 ID，可以是任意字符串。
- `npm` 指定该提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来兼容任何 OpenAI 兼容的 API。
- `name` 是该提供商在 UI 中显示的名称。
- `options.baseURL` 是本地服务器的端点地址。
- `models` 是模型 ID 到其配置的映射。模型名称会显示在模型选择列表中。

---

### Moonshot AI

要使用 Moonshot AI 的 Kimi K2：

1. 前往 [Moonshot AI 控制台](https://platform.moonshot.ai/console)，创建账户并点击 **Create API key**。

2. 执行 `/connect` 命令并搜索 **Moonshot AI**。

   ```txt
   /connect
   ```

3. 输入你的 Moonshot API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择 _Kimi K2_。

   ```txt
   /models
   ```

---

### MiniMax

1. 前往 [MiniMax API 控制台](https://platform.minimax.io/login)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **MiniMax**。

   ```txt
   /connect
   ```

3. 输入你的 MiniMax API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _M2.1_。

   ```txt
   /models
   ```

---

### Nebius Token Factory

1. 前往 [Nebius Token Factory 控制台](https://tokenfactory.nebius.com/)，创建账户并点击 **Add Key**。

2. 执行 `/connect` 命令并搜索 **Nebius Token Factory**。

   ```txt
   /connect
   ```

3. 输入你的 Nebius Token Factory API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_。

   ```txt
   /models
   ```

---

### Ollama

你可以通过 Ollama 配置 OpenCode 使用本地模型。

:::tip
Ollama 可以自动为 OpenCode 进行配置。详见 [Ollama 集成文档](https://docs.ollama.com/integrations/opencode)。

```json title="opencode.json" "ollama" {5, 6, 8, 10-14}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "llama2": {
          "name": "Llama 2"
        }
      }
    }
  }
}
```

在这个示例中：

- `ollama` 是自定义的提供商 ID，可以是任意字符串。
- `npm` 指定该提供商使用的包。这里使用 `@ai-sdk/openai-compatible` 来兼容任何 OpenAI 兼容的 API。
- `name` 是该提供商在 UI 中显示的名称。
- `options.baseURL` 是本地服务器的端点地址。
- `models` 是模型 ID 到其配置的映射。模型名称会显示在模型选择列表中。

:::tip
如果工具调用不工作，请尝试增大 Ollama 中的 `num_ctx` 值。建议从 16k - 32k 左右开始。

---

### Ollama Cloud

要在 OpenCode 中使用 Ollama Cloud：

1. 前往 [https://ollama.com/](https://ollama.com/) 登录或创建账户。

2. 导航到 **Settings** > **Keys**，点击 **Add API Key** 生成新的 API 密钥。

3. 复制 API 密钥以便在 OpenCode 中使用。

4. 执行 `/connect` 命令并搜索 **Ollama Cloud**。

   ```txt
   /connect
   ```

5. 输入你的 Ollama Cloud API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

6. **重要**：在 OpenCode 中使用云端模型之前，必须先将模型信息拉取到本地：

   ```bash
   ollama pull gpt-oss:20b-cloud
   ```

7. 执行 `/models` 命令选择你的 Ollama Cloud 模型。

   ```txt
   /models
   ```

---

### OpenAI

我们建议注册 [ChatGPT Plus 或 Pro](https://chatgpt.com/pricing)。

1. 注册完成后，执行 `/connect` 命令并选择 OpenAI。

   ```txt
   /connect
   ```

2. 你可以选择 **ChatGPT Plus/Pro** 选项，浏览器会自动打开并要求你进行身份验证。

   ```txt
   ┌ Select auth method
   │
   │ ChatGPT Plus/Pro
   │ Manually enter API Key
   └
   ```

3. 现在使用 `/models` 命令即可看到所有 OpenAI 模型。

   ```txt
   /models
   ```

##### 使用 API 密钥

如果你已经有 API 密钥，可以选择 **Manually enter API Key** 并将其粘贴到终端中。

---

### OpenCode Zen

OpenCode Zen 是由 OpenCode 团队提供的经过测试和验证的模型列表。[了解更多](/docs/zen)。

1. 登录 **<a href={console}>OpenCode Zen</a>** 并点击 **Create API Key**。

2. 执行 `/connect` 命令并搜索 **OpenCode Zen**。

   ```txt
   /connect
   ```

3. 输入你的 OpenCode API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Qwen 3 Coder 480B_。

   ```txt
   /models
   ```

---

### OpenRouter

1. 前往 [OpenRouter 仪表盘](https://openrouter.ai/settings/keys)，点击 **Create API Key** 并复制密钥。

2. 执行 `/connect` 命令并搜索 OpenRouter。

   ```txt
   /connect
   ```

3. 输入该提供商的 API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 默认已预加载了许多 OpenRouter 模型，执行 `/models` 命令选择你想要的模型。

   ```txt
   /models
   ```

   你也可以通过 OpenCode 配置添加更多模型。

   ```json title="opencode.json" {6}
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "openrouter": {
         "models": {
           "somecoolnewmodel": {}
         }
       }
     }
   }
   ```

5. 你还可以通过 OpenCode 配置自定义模型。以下是指定提供商的示例：

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "openrouter": {
         "models": {
           "moonshotai/kimi-k2": {
             "options": {
               "provider": {
                 "order": ["baseten"],
                 "allow_fallbacks": false
               }
             }
           }
         }
       }
     }
   }
   ```

---

### SAP AI Core

SAP AI Core 通过统一平台提供对来自 OpenAI、Anthropic、Google、Amazon、Meta、Mistral 和 AI21 的 40+ 模型的访问。

1. 前往 [SAP BTP Cockpit](https://account.hana.ondemand.com/)，导航到你的 SAP AI Core 服务实例，并创建服务密钥。

   :::tip
   服务密钥是一个包含 `clientid`、`clientsecret`、`url` 和 `serviceurls.AI_API_URL` 的 JSON 对象。你可以在 BTP Cockpit 的 **Services** > **Instances and Subscriptions** 下找到你的 AI Core 实例。

2. 执行 `/connect` 命令并搜索 **SAP AI Core**。

   ```txt
   /connect
   ```

3. 输入你的服务密钥 JSON。

   ```txt
   ┌ Service key
   │
   │
   └ enter
   ```

   或者设置 `AICORE_SERVICE_KEY` 环境变量：

   ```bash
   AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}' opencode
   ```

   或者添加到你的 bash 配置文件中：

   ```bash title="~/.bash_profile"
   export AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}'
   ```

4. 可选：设置部署 ID 和资源组：

   ```bash
   AICORE_DEPLOYMENT_ID=your-deployment-id AICORE_RESOURCE_GROUP=your-resource-group opencode
   ```

   :::note
   这些设置是可选的，应根据你的 SAP AI Core 配置进行设置。

5. 执行 `/models` 命令从 40+ 个可用模型中进行选择。

   ```txt
   /models
   ```

---

### STACKIT

STACKIT AI Model Serving 提供完全托管的主权托管环境，专注于 Llama、Mistral 和 Qwen 等大语言模型，在欧洲基础设施上实现最大程度的数据主权。

1. 前往 [STACKIT Portal](https://portal.stackit.cloud)，导航到 **AI Model Serving**，为你的项目创建认证令牌。

   :::tip
   你需要先拥有 STACKIT 客户账户、用户账户和项目，才能创建认证令牌。

2. 执行 `/connect` 命令并搜索 **STACKIT**。

   ```txt
   /connect
   ```

3. 输入你的 STACKIT AI Model Serving 认证令牌。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Qwen3-VL 235B_ 或 _Llama 3.3 70B_。

   ```txt
   /models
   ```

---

### OVHcloud AI Endpoints

1. 前往 [OVHcloud 管理面板](https://ovh.com/manager)。导航到 `Public Cloud` 部分，`AI & Machine Learning` > `AI Endpoints`，在 `API Keys` 标签页中点击 **Create a new API key**。

2. 执行 `/connect` 命令并搜索 **OVHcloud AI Endpoints**。

   ```txt
   /connect
   ```

3. 输入你的 OVHcloud AI Endpoints API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _gpt-oss-120b_。

   ```txt
   /models
   ```

---

### Scaleway

要在 OpenCode 中使用 [Scaleway Generative APIs](https://www.scaleway.com/en/docs/generative-apis/)：

1. 前往 [Scaleway Console IAM 设置](https://console.scaleway.com/iam/api-keys)生成新的 API 密钥。

2. 执行 `/connect` 命令并搜索 **Scaleway**。

   ```txt
   /connect
   ```

3. 输入你的 Scaleway API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _devstral-2-123b-instruct-2512_ 或 _gpt-oss-120b_。

   ```txt
   /models
   ```

---

### Together AI

1. 前往 [Together AI 控制台](https://api.together.ai)，创建账户并点击 **Add Key**。

2. 执行 `/connect` 命令并搜索 **Together AI**。

   ```txt
   /connect
   ```

3. 输入你的 Together AI API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Kimi K2 Instruct_。

   ```txt
   /models
   ```

---

### Venice AI

1. 前往 [Venice AI 控制台](https://venice.ai)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **Venice AI**。

   ```txt
   /connect
   ```

3. 输入你的 Venice AI API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Llama 3.3 70B_。

   ```txt
   /models
   ```

---

### Vercel AI Gateway

Vercel AI Gateway 允许你通过统一端点访问来自 OpenAI、Anthropic、Google、xAI 等提供商的模型。模型按原价提供，不额外加价。

1. 前往 [Vercel 仪表盘](https://vercel.com/)，导航到 **AI Gateway** 标签页，点击 **API keys** 创建新的 API 密钥。

2. 执行 `/connect` 命令并搜索 **Vercel AI Gateway**。

   ```txt
   /connect
   ```

3. 输入你的 Vercel AI Gateway API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型。

   ```txt
   /models
   ```

你也可以通过 OpenCode 配置自定义模型。以下是指定提供商路由顺序的示例。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "vercel": {
      "models": {
        "anthropic/claude-sonnet-4": {
          "options": {
            "order": ["anthropic", "vertex"]
          }
        }
      }
    }
  }
}
```

一些常用的路由选项：

| 选项                | 描述                             |
| ------------------- | -------------------------------- |
| `order`             | 提供商尝试顺序                   |
| `only`              | 限制为特定提供商                 |
| `zeroDataRetention` | 仅使用具有零数据留存策略的提供商 |

---

### xAI

1. 前往 [xAI 控制台](https://console.x.ai/)，创建账户并生成 API 密钥。

2. 执行 `/connect` 命令并搜索 **xAI**。

   ```txt
   /connect
   ```

3. 输入你的 xAI API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _Grok Beta_。

   ```txt
   /models
   ```

---

### Z.AI

1. 前往 [Z.AI API 控制台](https://z.ai/manage-apikey/apikey-list)，创建账户并点击 **Create a new API key**。

2. 执行 `/connect` 命令并搜索 **Z.AI**。

   ```txt
   /connect
   ```

   如果你订阅了 **GLM Coding Plan**，请选择 **Z.AI Coding Plan**。

3. 输入你的 Z.AI API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 执行 `/models` 命令选择模型，例如 _GLM-4.7_。

   ```txt
   /models
   ```

---

### ZenMux

1. 前往 [ZenMux 仪表盘](https://zenmux.ai/settings/keys)，点击 **Create API Key** 并复制密钥。

2. 执行 `/connect` 命令并搜索 ZenMux。

   ```txt
   /connect
   ```

3. 输入该提供商的 API 密钥。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. 默认已预加载了许多 ZenMux 模型，执行 `/models` 命令选择你想要的模型。

   ```txt
   /models
   ```

   你也可以通过 OpenCode 配置添加更多模型。

   ```json title="opencode.json" {6}
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "zenmux": {
         "models": {
           "somecoolnewmodel": {}
         }
       }
     }
   }
   ```

---

## 自定义提供商

要添加 `/connect` 命令中未列出的任何 **OpenAI 兼容**提供商：

:::tip
你可以在 OpenCode 中使用任何 OpenAI 兼容的提供商。大多数现代 AI 提供商都提供 OpenAI 兼容的 API。

1. 执行 `/connect` 命令，向下滚动到 **Other**。

   ```bash
   $ /connect

   ┌  Add credential
   │
   ◆  Select provider
   │  ...
   │  ● Other
   └
   ```

2. 输入该提供商的唯一 ID。

   ```bash
   $ /connect

   ┌  Add credential
   │
   ◇  Enter provider id
   │  myprovider
   └
   ```

   :::note
   请选择一个容易记住的 ID，你将在配置文件中使用它。

3. 输入该提供商的 API 密钥。

   ```bash
   $ /connect

   ┌  Add credential
   │
   ▲  This only stores a credential for myprovider - you will need to configure it in opencode.json, check the docs for examples.
   │
   ◇  Enter your API key
   │  sk-...
   └
   ```

4. 在项目目录中创建或更新 `opencode.json` 文件：

   ```json title="opencode.json" ""myprovider"" {5-15}
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "myprovider": {
         "npm": "@ai-sdk/openai-compatible",
         "name": "My AI ProviderDisplay Name",
         "options": {
           "baseURL": "https://api.myprovider.com/v1"
         },
         "models": {
           "my-model-name": {
             "name": "My Model Display Name"
           }
         }
       }
     }
   }
   ```

   以下是配置选项说明：
   - **npm**：要使用的 AI SDK 包，对于 OpenAI 兼容的提供商使用 `@ai-sdk/openai-compatible`（适用于 `/v1/chat/completions`）。如果你的提供商/模型走 `/v1/responses`，请使用 `@ai-sdk/openai`。
   - **name**：在 UI 中显示的名称。
   - **models**：可用模型。
   - **options.baseURL**：API 端点 URL。
   - **options.apiKey**：可选，如果不使用 auth 认证，可直接设置 API 密钥。
   - **options.headers**：可选，设置自定义请求头。

   更多高级选项请参见下面的示例。

5. 执行 `/models` 命令，你自定义的提供商和模型将出现在选择列表中。

---

##### 示例

以下是设置 `apiKey`、`headers` 和模型 `limit` 选项的示例。

```json title="opencode.json" {9,11,17-20}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "myprovider": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "My AI ProviderDisplay Name",
      "options": {
        "baseURL": "https://api.myprovider.com/v1",
        "apiKey": "{env:ANTHROPIC_API_KEY}",
        "headers": {
          "Authorization": "Bearer custom-token"
        }
      },
      "models": {
        "my-model-name": {
          "name": "My Model Display Name",
          "limit": {
            "context": 200000,
            "output": 65536
          }
        }
      }
    }
  }
}
```

配置详情：

- **apiKey**：使用 `env` 变量语法设置，[了解更多](/docs/config#env-vars)。
- **headers**：随每个请求发送的自定义请求头。
- **limit.context**：模型接受的最大输入 Token 数。
- **limit.output**：模型可生成的最大 Token 数。

`limit` 字段让 OpenCode 了解你还剩余多少上下文空间。标准提供商会自动从 models.dev 拉取这些信息。

---

## 故障排除

如果你在配置提供商时遇到问题，请检查以下几点：

1. **检查认证设置**：运行 `opencode auth list` 查看该提供商的凭据是否已添加到配置中。

   这不适用于 Amazon Bedrock 等依赖环境变量进行认证的提供商。

2. 对于自定义提供商，请检查 OpenCode 配置并确认：
   - `/connect` 命令中使用的提供商 ID 与 OpenCode 配置中的 ID 一致。
   - 使用了正确的 npm 包。例如，Cerebras 应使用 `@ai-sdk/cerebras`。对于其他所有 OpenAI 兼容的提供商，使用 `@ai-sdk/openai-compatible`（`/v1/chat/completions`）；如果模型走 `/v1/responses`，请使用 `@ai-sdk/openai`。同一 provider 混用时，可在模型下设置 `provider.npm` 覆盖默认值。
   - `options.baseURL` 字段中的 API 端点地址正确。

---

## tui

- 官方原文：https://opencode.ai/docs/zh-cn/tui
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-tui.md`

OpenCode 提供了一个交互式终端界面（TUI），用于配合 LLM 处理您的项目。

运行 OpenCode 即可启动当前目录的 TUI。

```bash
opencode
```

或者您可以为指定的工作目录启动它。

```bash
opencode /path/to/project
```

进入 TUI 后，您可以输入消息进行提示。

```text
Give me a quick summary of the codebase.
```

---

## 文件引用

您可以使用 `@` 在消息中引用文件。这会在当前工作目录中进行模糊文件搜索。

:::tip
您还可以使用 `@` 来引用消息中的文件。

```text "@packages/functions/src/api/index.ts"
How is auth handled in @packages/functions/src/api/index.ts?
```

文件的内容会自动添加到对话中。

---

## Bash 命令

以 `!` 开头的消息会作为 shell 命令执行。

```bash frame="none"
!ls -la
```

命令的输出会作为工具结果添加到对话中。

---

## 命令

使用 OpenCode TUI 时，您可以输入 `/` 后跟命令名称来快速执行操作。例如：

```bash frame="none"
/help
```

大多数命令还支持以 `ctrl+x` 作为前导键的快捷键，其中 `ctrl+x` 是默认前导键。[了解更多](/docs/keybinds)。

以下是所有可用的斜杠命令：

---

### connect

将提供商添加到 OpenCode。允许您从可用的提供商中选择并添加其 API 密钥。

```bash frame="none"
/connect
```

---

### compact

压缩当前会话。_别名_：`/summarize`

```bash frame="none"
/compact
```

**快捷键：** `ctrl+x c`

---

### details

切换工具执行详情的显示。

```bash frame="none"
/details
```

**快捷键：** `ctrl+x d`

---

### editor

打开外部编辑器来编写消息。使用 `EDITOR` 环境变量中设置的编辑器。[了解更多](#editor-setup)。

```bash frame="none"
/editor
```

**快捷键：** `ctrl+x e`

---

### exit

退出 OpenCode。_别名_：`/quit`、`/q`

```bash frame="none"
/exit
```

**快捷键：** `ctrl+x q`

---

### export

将当前对话导出为 Markdown 并在默认编辑器中打开。使用 `EDITOR` 环境变量中设置的编辑器。[了解更多](#editor-setup)。

```bash frame="none"
/export
```

**快捷键：** `ctrl+x x`

---

### help

显示帮助对话框。

```bash frame="none"
/help
```

**快捷键：** `ctrl+x h`

---

### init

创建或更新 `AGENTS.md` 文件。[了解更多](/docs/rules)。

```bash frame="none"
/init
```

**快捷键：** `ctrl+x i`

---

### models

列出可用模型。

```bash frame="none"
/models
```

**快捷键：** `ctrl+x m`

---

### new

开始新的会话。_别名_：`/clear`

```bash frame="none"
/new
```

**快捷键：** `ctrl+x n`

---

### redo

重做之前撤销的消息。仅在使用 `/undo` 后可用。

:::tip
所有文件更改也会被恢复。

在内部，这使用 Git 来管理文件更改。因此您的项目**需要是一个 Git 仓库**。

```bash frame="none"
/redo
```

**快捷键：** `ctrl+x r`

---

### sessions

列出会话并在会话之间切换。_别名_：`/resume`、`/continue`

```bash frame="none"
/sessions
```

**快捷键：** `ctrl+x l`

---

### share

分享当前会话。[了解更多](/docs/share)。

```bash frame="none"
/share
```

**快捷键：** `ctrl+x s`

---

### themes

列出可用主题。

```bash frame="none"
/themes
```

**快捷键：** `ctrl+x t`

---

### thinking

切换对话中思考/推理块的可见性。启用后，您可以看到支持扩展思考的模型的推理过程。

:::note
此命令仅控制思考块是否**显示** — 它不会启用或禁用模型的推理能力。要切换实际的推理能力，请使用 `ctrl+t` 循环切换模型变体。

```bash frame="none"
/thinking
```

---

### undo

撤销对话中的最后一条消息。移除最近的用户消息、所有后续响应以及所有文件更改。

:::tip
所做的任何文件更改也会被还原。

在内部，这使用 Git 来管理文件更改。因此您的项目**需要是一个 Git 仓库**。

```bash frame="none"
/undo
```

**快捷键：** `ctrl+x u`

---

### unshare

取消分享当前会话。[了解更多](/docs/share#un-sharing)。

```bash frame="none"
/unshare
```

---

## 编辑器设置

`/editor` 和 `/export` 命令都使用 `EDITOR` 环境变量中指定的编辑器。

    ```bash
    # Example for nano or vim
    export EDITOR=nano
    export EDITOR=vim

    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.
    # include --wait
    export EDITOR="code --wait"
    ```

    要使其永久生效，请将其添加到您的 shell 配置文件中；
    `~/.bashrc`、`~/.zshrc` 等。

    ```bash
    set EDITOR=notepad

    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.
    # include --wait
    set EDITOR=code --wait
    ```

    要使其永久生效，请使用**系统属性** > **环境变量**。

    ```powershell
    $env:EDITOR = "notepad"

    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.
    # include --wait
    $env:EDITOR = "code --wait"
    ```

    要使其永久生效，请将其添加到您的 PowerShell 配置文件中。

常用的编辑器选项包括：

- `code` - Visual Studio Code
- `cursor` - Cursor
- `windsurf` - Windsurf
- `nvim` - Neovim 编辑器
- `vim` - Vim 编辑器
- `nano` - Nano 编辑器
- `notepad` - Notepad（Windows 记事本）
- `subl` - Sublime Text

:::note
某些编辑器（如 VS Code）需要以 `--wait` 标志启动。

某些编辑器需要命令行参数才能以阻塞模式运行。`--wait` 标志使编辑器进程阻塞直到关闭。

---

## 配置

您可以通过 `tui.json`（或 `tui.jsonc`）自定义 TUI 行为。

```json title="tui.json"
{
  "$schema": "https://opencode.ai/tui.json",
  "theme": "opencode",
  "leader_timeout": 2000,
  "keybinds": {
    "leader": "ctrl+x",
    "command_list": "ctrl+p"
  },
  "scroll_speed": 3,
  "scroll_acceleration": {
    "enabled": false
  },
  "diff_style": "auto",
  "mouse": true,
  "attention": {
    "enabled": true,
    "notifications": true,
    "sound": true,
    "volume": 0.4,
    "sound_pack": "opencode.default",
    "sounds": {
      "error": "./sounds/error.mp3"
    }
  }
}
```

这与 `opencode.json` 是分开的；`opencode.json` 用于配置服务器和运行时行为。

`keybinds` 会与内置默认值合并，因此你只需要配置想要修改的快捷键。

### 选项

- `theme` - 设置 UI 主题。[了解更多](/docs/themes)。
- `keybinds` - 自定义键盘快捷键。[了解更多](/docs/keybinds)。
- `leader_timeout` - 控制按下 leader key 后 OpenCode 等待后续按键的时间。默认为 `2000`。
- `scroll_acceleration.enabled` - 启用 macOS 风格的滚动加速，让滚动更平滑自然。启用后，快速滚动时速度会增加，慢速移动时仍保持精确。**此设置优先于 `scroll_speed`，启用时会覆盖它。**
- `scroll_speed` - 控制使用滚动命令时 TUI 的滚动速度（最小值：`0.001`，支持小数）。默认为 `3`。**注意：如果 `scroll_acceleration.enabled` 设置为 `true`，则此设置会被忽略。**
- `diff_style` - 控制 diff 的显示方式。`"auto"` 会根据终端宽度自适应，`"stacked"` 始终显示单列布局。
- `mouse` - 在 TUI 中启用或禁用鼠标捕获（默认：`true`）。禁用后，终端原生的鼠标选择和滚动行为会保留下来。
- `attention` - 配置 TUI 桌面通知和声音。默认禁用。

使用 `OPENCODE_TUI_CONFIG` 可以加载自定义的 TUI 配置文件路径。

### Attention

当 OpenCode 需要你处理问题、批准权限请求、查看会话错误，或想告知会话已完成时，TUI 可以通过声音和桌面通知提醒你。设置 `attention.enabled` 后会启用这些提醒；内置事件触发时会播放声音。桌面通知只会在终端窗口未聚焦时发送，并且不会用于 subagent 事件。

- `enabled` - 开启 Attention 的所有通知和声音。默认为 `false`。
- `notifications` - 启用 Attention 后，允许 TUI 通过终端发送桌面通知。默认为 `true`。
- `sound` - 启用 Attention 后，允许播放提示音。默认为 `true`。
- `volume` - 默认提示音音量，范围从 `0` 到 `1`。默认为 `0.4`。
- `sound_pack` - 要使用的 sound pack ID。默认为 `opencode.default`。
- `sounds` - 为 `default`、`question`、`permission`、`error`、`done` 或 `subagent_done` 指定自定义声音文件。路径可以是绝对路径、`file://` URL，或相对于 `tui.json` 的路径。

---

## 自定义

您可以使用命令面板（`ctrl+x h` 或 `/help`）自定义 TUI 视图的各个方面。这些设置在重启后仍会保留。

---

#### 用户名显示

切换您的用户名是否显示在聊天消息中。通过以下方式访问：

- 命令面板：搜索 "username" 或 "hide username"
- 该设置会自动保存，并在各个 TUI 会话中保持记忆

---

## zen

- 官方原文：https://opencode.ai/docs/zh-cn/zen
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-zen.md`

export const console = config.console
export const email = `mailto:${config.email}`

OpenCode Zen 是由 OpenCode 团队提供的一组经过测试和验证的模型。

Zen 的工作方式与 OpenCode 中的任何其他提供商相同。你登录 OpenCode Zen 并获取 API 密钥。它是**完全可选的**，即使不用它，你也可以照常使用 OpenCode。

---

## 背景

现在市面上有大量模型，但其中只有少数模型适合作为编码代理使用。此外，大多数提供商的配置方式差异很大，因此你获得的性能和质量也会非常不同。

:::tip
我们测试了一组与 OpenCode 配合良好的精选模型和提供商。

所以，如果你通过 OpenRouter 之类的服务使用模型，你无法确定自己拿到的是否是目标模型的最佳版本。

为了解决这个问题，我们做了几件事：

1. 我们测试了一组选定的模型，并与它们的团队讨论了如何以最佳方式运行这些模型。
2. 然后我们与几家提供商合作，确保这些模型被正确提供。
3. 最后，我们对模型和提供商的组合进行了基准测试，并整理出了一份我们认为值得推荐的列表。

OpenCode Zen 是一个 AI 网关，让你可以访问这些模型。

---

## 工作原理

OpenCode Zen 的工作方式与 OpenCode 中的任何其他提供商相同。

1. 登录 **<a href={console}>OpenCode Zen</a>**，添加你的账单信息，然后复制你的 API 密钥。
2. 在 TUI 中运行 `/connect` 命令，选择 OpenCode Zen，然后粘贴你的 API 密钥。
3. 在 TUI 中运行 `/models`，查看我们推荐的模型列表。

你按请求付费，也可以向账户充值。

---

## 端点

你也可以通过以下 API 端点访问我们的模型。

| 模型                            | 模型 ID                         | 端点                                                      | AI SDK 包                   |
| ------------------------------- | ------------------------------- | --------------------------------------------------------- | --------------------------- |
| GPT 6 Astra                     | gpt-6-astra                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.6 Sol                     | gpt-5.6-sol                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.6 Terra                   | gpt-5.6-terra                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.6 Luna                    | gpt-5.6-luna                    | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.5                         | gpt-5.5                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.5 Pro                     | gpt-5.5-pro                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4                         | gpt-5.4                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4 Pro                     | gpt-5.4-pro                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4 Mini                    | gpt-5.4-mini                    | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4 Nano                    | gpt-5.4-nano                    | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.3 Codex                   | gpt-5.3-codex                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.3 Codex Spark             | gpt-5.3-codex-spark             | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.2                         | gpt-5.2                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.2 Codex                   | gpt-5.2-codex                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1                         | gpt-5.1                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1 Codex                   | gpt-5.1-codex                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1 Codex Max               | gpt-5.1-codex-max               | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1 Codex Mini              | gpt-5.1-codex-mini              | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5                           | gpt-5                           | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5 Codex                     | gpt-5-codex                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5 Nano                      | gpt-5-nano                      | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Claude Fable 5.1                | claude-fable-5-1                | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Fable 5                  | claude-fable-5                  | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 5                   | claude-opus-5                   | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.8                 | claude-opus-4-8                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.7                 | claude-opus-4-7                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.6                 | claude-opus-4-6                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.5                 | claude-opus-4-5                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Sonnet 5                 | claude-sonnet-5                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Sonnet 4.6               | claude-sonnet-4-6               | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Sonnet 4.5               | claude-sonnet-4-5               | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Haiku 4.5                | claude-haiku-4-5                | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Gemini 3.8 Flash                | gemini-3.8-flash                | `https://opencode.ai/zen/v1/models/gemini-3.8-flash`      | `@ai-sdk/google`            |
| Gemini 3.7 Flash                | gemini-3.7-flash                | `https://opencode.ai/zen/v1/models/gemini-3.7-flash`      | `@ai-sdk/google`            |
| Gemini 3.6 Flash                | gemini-3.6-flash                | `https://opencode.ai/zen/v1/models/gemini-3.6-flash`      | `@ai-sdk/google`            |
| Gemini 3.5 Flash                | gemini-3.5-flash                | `https://opencode.ai/zen/v1/models/gemini-3.5-flash`      | `@ai-sdk/google`            |
| Gemini 3.5 Flash Lite           | gemini-3.5-flash-lite           | `https://opencode.ai/zen/v1/models/gemini-3.5-flash-lite` | `@ai-sdk/google`            |
| Gemini 3.1 Pro                  | gemini-3.1-pro                  | `https://opencode.ai/zen/v1/models/gemini-3.1-pro`        | `@ai-sdk/google`            |
| Gemini 3 Flash                  | gemini-3-flash                  | `https://opencode.ai/zen/v1/models/gemini-3-flash`        | `@ai-sdk/google`            |
| Grok 4.7                        | grok-4.7                        | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Grok 4.6                        | grok-4.6                        | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Grok 4.5                        | grok-4.5                        | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Grok Build 0.1                  | grok-build-0.1                  | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Muse Spark 1.3                  | muse-spark-1.3                  | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Muse Spark 1.2                  | muse-spark-1.2                  | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Qwen3.8 Flash                   | qwen3.8-flash                   | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.7 Max                     | qwen3.7-max                     | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.7 Plus                    | qwen3.7-plus                    | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.6 Plus                    | qwen3.6-plus                    | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.5 Plus                    | qwen3.5-plus                    | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| DeepSeek V4.1 Flash             | deepseek-v4.1-flash             | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Pro                 | deepseek-v4-pro                 | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Flash               | deepseek-v4-flash               | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Flash Vision Exp    | deepseek-v4-flash-vision-exp    | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiniMax M3                      | minimax-m3                      | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiniMax M2.7                    | minimax-m2.7                    | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiniMax M2.5                    | minimax-m2.5                    | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.3 Flash                   | glm-5.3-flash                   | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.3                         | glm-5.3                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.2                         | glm-5.2                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.1                         | glm-5.1                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5                           | glm-5                           | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K2.5                       | kimi-k2.5                       | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K2.6                       | kimi-k2.6                       | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K2.7 Code                  | kimi-k2.7-code                  | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K3                         | kimi-k3                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Jev 1.13                        | jev-1.13                        | `https://opencode.ai/zen/v1/systemone`                    | -                           |
| Jev 1.13 Free                   | jev-1.13-free                   | `https://opencode.ai/zen/v1/systemone`                    | -                           |
| Big Pickle                      | big-pickle                      | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiMo-V2.6-Flash Free            | mimo-v2.6-flash-free            | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiMo-V2.5 Free                  | mimo-v2.5-free                  | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Ling 3.0 Flash Fin Free         | ling-3.0-flash-fin-free         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Nemotron 3 Ultra Free           | nemotron-3-ultra-free           | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Nemotron 3.5 Lightning Free     | nemotron-3.5-lightning-free     | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Muse Spark 1.3 Contributor Free | muse-spark-1.3-contributor-free | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |

在你的 OpenCode 配置中，[模型 ID](/docs/config/#models) 使用 `opencode/<model-id>` 格式。例如，对于 GPT 5.5，你需要在配置中使用 `opencode/gpt-5.5`。

---

### 模型

你可以从以下地址获取可用模型及其元数据的完整列表：

```
https://opencode.ai/zen/v1/models
```

---

### Jev

Jev 是 TypeSafe AI 推出的一款 System One 模型，适用于快速、结构化的决策。它不会生成文本，而是根据带类型的问题评估 `state`，并返回可供代码直接使用的值和概率。它支持是/否问题（`noul`）、多项选择问题（`choice`）以及基于评分标准的问题（`score`）。

将你的 OpenCode Zen API 密钥用于 `https://opencode.ai/zen/v1/systemone` 端点。以下示例会检查支持请求是否紧急：

```bash
curl https://opencode.ai/zen/v1/systemone \
  -H "Authorization: Bearer $OPENCODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "jev-1.13",
    "state": "My payments have failed for three days and I am losing sales. Please help now.",
    "questions": {
      "is_urgent": {
        "type": "noul",
        "instructions": "Does this request require urgent attention?"
      }
    }
  }'
```

你可以在一个请求中提出多个问题。Jev 会并行评估这些问题，并将每个答案返回到对应的问题 ID 下：

```bash
curl https://opencode.ai/zen/v1/systemone \
  -H "Authorization: Bearer $OPENCODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "jev-1.13",
    "state": "My order arrived late and the item is damaged. I want a refund.",
    "questions": {
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this request?",
        "criteria": {
          "returns": "Refunds, exchanges, or damaged items",
          "shipping": "Delivery delays or lost packages",
          "billing": "Charges, invoices, or payment problems"
        }
      },
      "frustration": {
        "type": "score",
        "instructions": "How frustrated is the customer?",
        "criteria": ["Calm", "Frustrated", "Very angry"]
      }
    }
  }'
```

使用 `jev-1.13-free` 代替 `jev-1.13`，即可使用限时免费模型。有关问题类型和响应字段的详细信息，请参阅 [TypeSafe AI 文档](https://docs.typesafe.ai/)。

---

## 定价

我们支持按量付费模式。以下是**每 1M tokens** 的价格。

| 模型                              | 输入   | 输出    | 缓存读取 | 缓存写入 |
| --------------------------------- | ------ | ------- | -------- | -------- |
| Big Pickle                        | Free   | Free    | Free     | -        |
| MiMo-V2.6-Flash Free              | Free   | Free    | Free     | -        |
| MiMo-V2.5 Free                    | Free   | Free    | Free     | -        |
| Ling 3.0 Flash Fin Free           | Free   | Free    | Free     | -        |
| Nemotron 3 Ultra Free             | Free   | Free    | Free     | -        |
| Nemotron 3.5 Lightning Free       | Free   | Free    | Free     | -        |
| Muse Spark 1.3 Contributor Free   | Free   | Free    | Free     | -        |
| Jev 1.13 Free                     | 免费   | 免费    | -        | -        |
| Jev 1.13                          | $0.042 | 免费    | -        | -        |
| MiniMax M3                        | $0.30  | $1.20   | $0.06    | -        |
| MiniMax M2.7                      | $0.30  | $1.20   | $0.06    | -        |
| MiniMax M2.5                      | $0.30  | $1.20   | $0.06    | -        |
| GLM 5.3 Flash                     | $0.15  | $0.50   | $0.03    | -        |
| GLM 5.3                           | $1.40  | $4.40   | $0.26    | -        |
| GLM 5.2                           | $1.40  | $4.40   | $0.26    | -        |
| GLM 5.1                           | $1.40  | $4.40   | $0.26    | -        |
| GLM 5                             | $1.00  | $3.20   | $0.20    | -        |
| Kimi K2.7 Code                    | $0.95  | $4.00   | $0.19    | -        |
| Kimi K3                           | $3.00  | $15.00  | $0.30    | -        |
| Kimi K2.6                         | $0.95  | $4.00   | $0.16    | -        |
| Kimi K2.5                         | $0.60  | $3.00   | $0.10    | -        |
| Qwen3.8 Flash                     | $0.15  | $0.47   | $0.016   | $0.20    |
| Qwen3.7 Max                       | $2.50  | $7.50   | $0.50    | $3.125   |
| Qwen3.7 Plus                      | $0.40  | $1.60   | $0.04    | $0.50    |
| Qwen3.6 Plus                      | $0.50  | $3.00   | $0.05    | $0.625   |
| Qwen3.5 Plus                      | $0.20  | $1.20   | $0.02    | $0.25    |
| DeepSeek V4.1 Flash               | $0.30  | $1.20   | $0.006   | -        |
| DeepSeek V4 Pro                   | $1.74  | $3.48   | $0.145   | -        |
| DeepSeek V4 Flash                 | $0.14  | $0.28   | $0.028   | -        |
| DeepSeek V4 Flash Vision Exp      | $0.14  | $0.28   | $0.028   | -        |
| Claude Fable 5.1                  | $10.00 | $50.00  | $0.25    | $12.50   |
| Claude Fable 5                    | $10.00 | $50.00  | $1.00    | $12.50   |
| Claude Opus 5                     | $5.00  | $25.00  | $0.50    | $6.25    |
| Claude Opus 4.8                   | $5.00  | $25.00  | $0.50    | $6.25    |
| Claude Opus 4.7                   | $5.00  | $25.00  | $0.50    | $6.25    |
| Claude Opus 4.6                   | $5.00  | $25.00  | $0.50    | $6.25    |
| Claude Opus 4.5                   | $5.00  | $25.00  | $0.50    | $6.25    |
| Claude Sonnet 5                   | $2.00  | $10.00  | $0.20    | $2.50    |
| Claude Sonnet 4.6                 | $3.00  | $15.00  | $0.30    | $3.75    |
| Claude Sonnet 4.5 (≤ 200K tokens) | $3.00  | $15.00  | $0.30    | $3.75    |
| Claude Sonnet 4.5 (> 200K tokens) | $6.00  | $22.50  | $0.60    | $7.50    |
| Claude Haiku 4.5                  | $1.00  | $5.00   | $0.10    | $1.25    |
| Gemini 3.8 Flash                  | $1.50  | $7.50   | $0.15    | -        |
| Gemini 3.7 Flash                  | $1.50  | $7.50   | $0.15    | -        |
| Gemini 3.6 Flash                  | $1.50  | $7.50   | $0.15    | -        |
| Gemini 3.5 Flash                  | $1.50  | $9.00   | $0.15    | -        |
| Gemini 3.5 Flash Lite             | $0.30  | $2.50   | $0.03    | -        |
| Gemini 3.1 Pro (≤ 200K tokens)    | $2.00  | $12.00  | $0.20    | -        |
| Gemini 3.1 Pro (> 200K tokens)    | $4.00  | $18.00  | $0.40    | -        |
| Gemini 3 Flash                    | $0.50  | $3.00   | $0.05    | -        |
| Grok 4.7 (≤ 200K tokens)          | $2.00  | $6.00   | $0.50    | -        |
| Grok 4.7 (> 200K tokens)          | $4.00  | $12.00  | $1.00    | -        |
| Grok 4.6 (≤ 200K tokens)          | $2.00  | $6.00   | $0.50    | -        |
| Grok 4.6 (> 200K tokens)          | $4.00  | $12.00  | $1.00    | -        |
| Grok 4.5 (≤ 200K tokens)          | $2.00  | $6.00   | $0.30    | -        |
| Grok 4.5 (> 200K tokens)          | $4.00  | $12.00  | $0.60    | -        |
| Grok Build 0.1                    | $1.00  | $2.00   | $0.20    | -        |
| Muse Spark 1.3                    | $1.25  | $4.25   | $0.15    | -        |
| Muse Spark 1.2                    | $1.25  | $4.25   | $0.15    | -        |
| GPT 6 Astra (≤ 272K tokens)       | $10.00 | $50.00  | $1.00    | $12.50   |
| GPT 6 Astra (> 272K tokens)       | $20.00 | $75.00  | $2.00    | $25.00   |
| GPT 5.6 Sol (≤ 272K tokens)       | $4.00  | $20.00  | $0.40    | $5.00    |
| GPT 5.6 Sol (> 272K tokens)       | $8.00  | $30.00  | $0.80    | $10.00   |
| GPT 5.6 Terra (≤ 272K tokens)     | $2.00  | $12.00  | $0.20    | $2.50    |
| GPT 5.6 Terra (> 272K tokens)     | $4.00  | $18.00  | $0.40    | $5.00    |
| GPT 5.6 Luna (≤ 272K tokens)      | $0.20  | $1.20   | $0.02    | $0.25    |
| GPT 5.6 Luna (> 272K tokens)      | $0.40  | $1.80   | $0.04    | $0.50    |
| GPT 5.5 (≤ 272K tokens)           | $5.00  | $30.00  | $0.50    | -        |
| GPT 5.5 (> 272K tokens)           | $10.00 | $45.00  | $1.00    | -        |
| GPT 5.5 Pro                       | $30.00 | $180.00 | $30.00   | -        |
| GPT 5.4 (≤ 272K tokens)           | $2.50  | $15.00  | $0.25    | -        |
| GPT 5.4 (> 272K tokens)           | $5.00  | $22.50  | $0.50    | -        |
| GPT 5.4 Pro                       | $30.00 | $180.00 | $30.00   | -        |
| GPT 5.4 Mini                      | $0.75  | $4.50   | $0.075   | -        |
| GPT 5.4 Nano                      | $0.20  | $1.25   | $0.02    | -        |
| GPT 5.3 Codex Spark               | $1.75  | $14.00  | $0.175   | -        |
| GPT 5.3 Codex                     | $1.75  | $14.00  | $0.175   | -        |
| GPT 5.2                           | $1.75  | $14.00  | $0.175   | -        |
| GPT 5.2 Codex                     | $1.75  | $14.00  | $0.175   | -        |
| GPT 5.1                           | $1.07  | $8.50   | $0.107   | -        |
| GPT 5.1 Codex                     | $1.07  | $8.50   | $0.107   | -        |
| GPT 5.1 Codex Max                 | $1.25  | $10.00  | $0.125   | -        |
| GPT 5.1 Codex Mini                | $0.25  | $2.00   | $0.025   | -        |
| GPT 5                             | $1.07  | $8.50   | $0.107   | -        |
| GPT 5 Codex                       | $1.07  | $8.50   | $0.107   | -        |
| GPT 5 Nano                        | $0.05  | $0.40   | $0.005   | -        |

**DeepSeek V4 Flash Vision Exp:** 图片会根据尺寸转换为 token，并与文本 token 一起按输入 token 计费。 [了解更多](https://api-docs.deepseek.com/quick_start/pricing/)。

你可能会在使用记录中看到 Haiku、Nano 或 Flash 等[低成本模型](/docs/config/#models)。OpenCode 使用这些模型生成会话标题。

:::note
信用卡手续费按成本转嫁（每笔交易 4.4% + $0.30）；除此之外我们不会额外收费。

免费模型：

- MiMo-V2.6-Flash Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
- MiMo-V2.5 Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
- Ling 3.0 Flash Fin Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
- Nemotron 3 Ultra Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
- Nemotron 3.5 Lightning Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
- Big Pickle 是一个隐身模型，目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
- Muse Spark 1.3 Contributor Free 目前在 OpenCode 上限时免费提供。团队正在利用这段时间收集反馈并改进模型。
- Jev 1.13 Free 目前在 OpenCode 上限时提供。

如果你有任何问题，请<a href={email}>联系我们</a>。

---

### 自动充值

如果你的余额低于 $5，Zen 将自动充值 $20。

你可以更改自动充值金额，也可以完全禁用自动充值。

---

### 月度限额

你还可以为整个工作区以及团队中的每位成员设置月度使用限额。

例如，假设你将月度使用限额设置为 $20，那么 Zen 在一个月内的使用金额不会超过 $20。但如果你启用了自动充值，当余额低于 $5 时，Zen 最终向你收取的金额可能会超过 $20。

---

### 已弃用模型

| 模型               | 弃用日期          |
| ------------------ | ----------------- |
| GPT 5.2 Codex      | July 23, 2026     |
| GPT 5.1 Codex      | July 23, 2026     |
| GPT 5.1 Codex Max  | July 23, 2026     |
| GPT 5.1 Codex Mini | July 23, 2026     |
| GPT 5 Codex        | July 23, 2026     |
| Claude Opus 4.1    | August 5, 2026    |
| Claude Sonnet 4    | June 15, 2026     |
| Claude Haiku 3.5   | February 16, 2026 |
| Gemini 3 Pro       | March 9, 2026     |
| MiniMax M2.5       | August 5, 2026    |
| MiniMax M2.1       | March 15, 2026    |
| GLM 5              | May 14, 2026      |
| GLM 4.7            | March 15, 2026    |
| GLM 4.6            | March 15, 2026    |
| Kimi K2.5          | August 5, 2026    |
| Kimi K2 Thinking   | March 6, 2026     |
| Kimi K2            | March 6, 2026     |
| Qwen3 Coder 480B   | February 6, 2026  |

---

## 隐私

我们所有模型都托管在 US。我们的提供商遵循零保留政策，不会将你的数据用于模型训练，但以下情况除外：

- Big Pickle：在免费期间，收集的数据可能会被用于改进模型。
- MiMo-V2.6-Flash Free：在免费期间，收集的数据可能会被用于改进模型。
- MiMo-V2.5 Free：在免费期间，收集的数据可能会被用于改进模型。
- Ling 3.0 Flash Fin Free：在免费期间，收集的数据可能会被用于改进模型。
- Nemotron 3 Ultra Free（NVIDIA 免费端点）：仅供试用 — 请勿提交个人或机密数据。出于安全目的以及为改进 NVIDIA 产品和服务，系统会记录你的使用情况。出于改进目的而记录的会话数据不会与你的身份或任何持久标识符相关联。有关我们数据处理实践的更多信息，请参阅我们的[隐私政策](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)。与此端点进行交互，即表示你同意我们收集、记录和使用此类信息，并同意 [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)。
- Nemotron 3.5 Lightning Free（NVIDIA 免费端点）：仅供试用 — 请勿提交个人或机密数据。出于安全目的以及为改进 NVIDIA 产品和服务，系统会记录你的使用情况。出于改进目的而记录的会话数据不会与你的身份或任何持久标识符相关联。有关我们数据处理实践的更多信息，请参阅我们的[隐私政策](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)。与此端点进行交互，即表示你同意我们收集、记录和使用此类信息，并同意 [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)。
- OpenAI APIs：请求会根据 [OpenAI's Data Policies](https://platform.openai.com/docs/guides/your-data) 保留 30 天。
- Anthropic APIs：请求会根据 [Anthropic's Data Policies](https://docs.anthropic.com/en/docs/claude-code/data-usage) 保留 30 天。
- Muse Spark 1.3 Contributor Free：以允许使用你的提示词和补全内容训练未来的 Meta 模型为条件，享受大幅折扣的 token 价格。[了解更多](https://dev.meta.ai/docs/pricing-rate-limits#contributor-tier)。

---

## 团队

Zen 也非常适合团队使用。你可以邀请队友、分配角色、管理团队使用的模型，等等。

:::note
作为测试版的一部分，工作区目前对团队免费开放。

作为测试版的一部分，团队目前可以免费管理工作区。我们很快会分享更多定价细节。

---

### 角色

你可以邀请队友加入工作区并分配角色：

- **Admin**：管理模型、成员、API 密钥和账单
- **Member**：仅管理自己的 API 密钥

Admin 还可以为每位成员设置月度支出限额，以便控制成本。

---

### 模型访问

Admin 可以为工作区启用或禁用特定模型。向已禁用模型发出的请求会返回错误。

这在你想禁用会收集数据的模型时很有用。

---

### 自带密钥

你可以使用自己的 OpenAI 或 Anthropic API 密钥，同时仍然访问 Zen 中的其他模型。

当你使用自己的密钥时，tokens 由提供商直接计费，而不是由 Zen 计费。

例如，你的组织可能已经拥有 OpenAI 或 Anthropic 的密钥，并且你想使用它，而不是使用 Zen 提供的密钥。

---

## 目标

我们创建 OpenCode Zen，是为了：

1. 为编码代理**基准测试**最佳模型和提供商。
2. 提供**最高质量**的选项，而不是降低性能或路由到更便宜的提供商。
3. 通过按成本销售来传递任何**降价**；因此唯一的加价只是为了覆盖我们的处理费用。
4. 保持**无锁定**，允许你将它与任何其他编码代理一起使用。同时也始终允许你在 OpenCode 中使用任何其他提供商。
