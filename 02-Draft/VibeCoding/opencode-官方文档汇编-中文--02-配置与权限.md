---
title: opencode 官方文档汇编（中文） · 02-配置与权限
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-zh-config.md
- VibeCoding/opencode/opencode-zh-enterprise.md
- VibeCoding/opencode/opencode-zh-formatters.md
- VibeCoding/opencode/opencode-zh-network.md
- VibeCoding/opencode/opencode-zh-permissions.md
- VibeCoding/opencode/opencode-zh-policies.md
- VibeCoding/opencode/opencode-zh-rules.md
- VibeCoding/opencode/opencode-zh-themes.md
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

> **汇编性质**：opencode 官方文档 官方原文 8 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## config

- 官方原文：https://opencode.ai/docs/zh-cn/config
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-config.md`

您可以使用 JSON 配置文件来配置 OpenCode。

---

## 格式

OpenCode 支持 **JSON** 和 **JSONC**（带注释的 JSON）格式。

```jsonc title="opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "autoupdate": true,
  "server": {
    "port": 4096,
  },
}
```

---

## 位置

您可以将配置放置在不同的位置，它们具有不同的优先级顺序。

:::note
配置文件是**合并在一起**的，而不是替换。

配置文件是合并在一起的，而不是被替换。来自以下配置位置的设置会被合并。后面的配置仅在键冲突时覆盖前面的配置。所有配置中的非冲突设置都会被保留。

例如，如果您的全局配置设置了 `autoupdate: true`，而您的项目配置设置了 `model: "anthropic/claude-sonnet-4-5"`，则最终配置将包含这两个设置。

---

### 优先级顺序

配置源按以下顺序加载（后面的源覆盖前面的源）：

1. **远程配置**（来自 `.well-known/opencode`）- 组织默认值
2. **全局配置**（`~/.config/opencode/opencode.json`）- 用户偏好
3. **自定义配置**（`OPENCODE_CONFIG` 环境变量）- 自定义覆盖
4. **项目配置**（项目中的 `opencode.json`）- 项目特定设置
5. **`.opencode` 目录** - 代理、命令、插件
6. **内联配置**（`OPENCODE_CONFIG_CONTENT` 环境变量）- 运行时覆盖

这意味着项目配置可以覆盖全局默认值，全局配置可以覆盖远程组织默认值。

:::note
`.opencode` 和 `~/.config/opencode` 目录的子目录使用**复数名称**：`agents/`、`commands/`、`modes/`、`plugins/`、`skills/`、`tools/` 和 `themes/`。为了向后兼容，也支持单数名称（例如 `agent/`）。

---

### 远程

组织可以通过 `.well-known/opencode` 端点提供默认配置。当您使用支持该功能的提供商进行身份验证时，会自动获取此配置。

远程配置最先加载，作为基础层。所有其他配置源（全局、项目）都可以覆盖这些默认值。

例如，如果您的组织提供了默认禁用的 MCP 服务器：

```json title="Remote config from .well-known/opencode"
{
  "mcp": {
    "jira": {
      "type": "remote",
      "url": "https://jira.example.com/mcp",
      "enabled": false
    }
  }
}
```

您可以在本地配置中启用特定服务器：

```json title="opencode.json"
{
  "mcp": {
    "jira": {
      "type": "remote",
      "url": "https://jira.example.com/mcp",
      "enabled": true
    }
  }
}
```

---

### 全局

将全局 OpenCode 配置放在 `~/.config/opencode/opencode.json` 中。使用全局配置来设置用户级别的偏好，例如主题、提供商或快捷键。

全局配置覆盖远程组织默认值。

---

### 项目级

在项目根目录中添加 `opencode.json`。项目配置在标准配置文件中具有最高优先级——它会覆盖全局配置和远程配置。

:::tip
将项目特定配置放在项目的根目录中。

当 OpenCode 启动时，它会在当前目录中查找配置文件，或向上遍历到最近的 Git 目录。

该配置文件也可以安全地提交到 Git 中，并使用与全局配置相同的 Schema。

---

### 自定义路径

使用 `OPENCODE_CONFIG` 环境变量指定自定义配置文件路径。

```bash
export OPENCODE_CONFIG=/path/to/my/custom-config.json
opencode run "Hello world"
```

自定义配置在优先级顺序中位于全局配置和项目配置之间加载。

---

### 自定义目录

使用 `OPENCODE_CONFIG_DIR` 环境变量指定自定义配置目录。该目录会像标准 `.opencode` 目录一样被搜索代理、命令、模式和插件，并且应遵循相同的结构。

```bash
export OPENCODE_CONFIG_DIR=/path/to/my/config-directory
opencode run "Hello world"
```

自定义目录在全局配置和 `.opencode` 目录之后加载，因此**可以覆盖**它们的设置。

---

## Schema

配置文件具有在 [**`opencode.ai/config.json`**](https://opencode.ai/config.json) 中定义的 Schema。

您的编辑器应该能够基于该 Schema 进行验证和自动补全。

---

### TUI

您可以通过 `tui` 选项配置 TUI 相关设置。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "tui": {
    "scroll_speed": 3,
    "scroll_acceleration": {
      "enabled": true
    },
    "diff_style": "auto"
  }
}
```

可用选项：

- `scroll_acceleration.enabled` - 启用 macOS 风格的滚动加速。**优先于 `scroll_speed`。**
- `scroll_speed` - 自定义滚动速度倍率（默认值：`3`，最小值：`1`）。如果 `scroll_acceleration.enabled` 为 `true`，则忽略此选项。
- `diff_style` - 控制差异渲染方式。`"auto"` 根据终端宽度自适应，`"stacked"` 始终显示单列。

[在此了解更多关于 TUI 的信息](/docs/tui)。

---

### 服务器

您可以通过 `server` 选项为 `opencode serve` 和 `opencode web` 命令配置服务器设置。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "server": {
    "port": 4096,
    "hostname": "0.0.0.0",
    "mdns": true,
    "mdnsDomain": "myproject.local",
    "cors": ["http://localhost:5173"]
  }
}
```

可用选项：

- `port` - 监听端口。
- `hostname` - 监听主机名。当 `mdns` 启用且未设置主机名时，默认为 `0.0.0.0`。
- `mdns` - 启用 mDNS 服务发现。这允许网络上的其他设备发现您的 OpenCode 服务器。
- `mdnsDomain` - mDNS 服务的自定义域名。默认为 `opencode.local`。适用于在同一网络上运行多个实例的场景。
- `cors` - 从基于浏览器的客户端使用 HTTP 服务器时允许 CORS 的额外来源。值必须是完整的来源（协议 + 主机 + 可选端口），例如 `https://app.example.com`。

[在此了解更多关于服务器的信息](/docs/server)。

---

### 工具

您可以通过 `tools` 选项管理 LLM 可以使用的工具。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "tools": {
    "write": false,
    "bash": false
  }
}
```

[在此了解更多关于工具的信息](/docs/tools)。

---

### 模型

您可以通过 `provider`、`model` 和 `small_model` 选项在 OpenCode 配置中设置要使用的提供商和模型。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {},
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5"
}
```

`small_model` 选项为标题生成等轻量级任务配置单独的模型。默认情况下，如果您的提供商有更便宜的模型可用，OpenCode 会尝试使用该模型，否则会回退到您的主模型。

提供商选项可以包括 `timeout` 和 `setCacheKey`：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "options": {
        "timeout": 600000,
        "setCacheKey": true
      }
    }
  }
}
```

- `timeout` - 请求超时时间，单位为毫秒（默认值：300000）。设置为 `false` 可禁用超时。
- `setCacheKey` - 确保始终为指定提供商设置缓存键。

您还可以配置[本地模型](/docs/models#local)。[了解更多](/docs/models)。

---

#### 提供商特定选项

一些提供商支持除通用 `timeout` 和 `apiKey` 设置之外的额外配置选项。

##### Amazon Bedrock

Amazon Bedrock 支持 AWS 特定配置：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "amazon-bedrock": {
      "options": {
        "region": "us-east-1",
        "profile": "my-aws-profile",
        "endpoint": "https://bedrock-runtime.us-east-1.vpce-xxxxx.amazonaws.com"
      }
    }
  }
}
```

- `region` - Bedrock 的 AWS 区域（默认为 `AWS_REGION` 环境变量或 `us-east-1`）
- `profile` - 来自 `~/.aws/credentials` 的 AWS 命名配置文件（默认为 `AWS_PROFILE` 环境变量）
- `endpoint` - VPC 端点的自定义端点 URL。这是通用 `baseURL` 选项使用 AWS 特定术语的别名。如果两者都指定，`endpoint` 优先。

:::note
Bearer Token（`AWS_BEARER_TOKEN_BEDROCK` 或 `/connect`）优先于基于配置文件的身份验证。详情请参见[身份验证优先级](/docs/providers#authentication-precedence)。

[了解更多关于 Amazon Bedrock 配置的信息](/docs/providers#amazon-bedrock)。

---

### 主题

您可以通过 OpenCode 配置中的 `theme` 选项设置要使用的主题。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "theme": ""
}
```

[在此了解更多](/docs/themes)。

---

### 代理

您可以通过 `agent` 选项为特定任务配置专用代理。

```jsonc title="opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for best practices and potential issues",
      "model": "anthropic/claude-sonnet-4-5",
      "prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",
      "tools": {
        // Disable file modification tools for review-only agent
        "write": false,
        "edit": false,
      },
    },
  },
}
```

您还可以使用 `~/.config/opencode/agents/` 或 `.opencode/agents/` 中的 Markdown 文件定义代理。[在此了解更多](/docs/agents)。

---

### 默认代理

您可以使用 `default_agent` 选项设置默认代理。当未明确指定代理时，将使用该默认代理。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "plan"
}
```

默认代理必须是主代理（不能是子代理）。可以是内置代理（如 `"build"` 或 `"plan"`），也可以是您定义的[自定义代理](/docs/agents)。如果指定的代理不存在或是子代理，OpenCode 将回退到 `"build"` 并发出警告。

此设置适用于所有界面：TUI、CLI（`opencode run`）、桌面应用和 GitHub Action。

---

### 分享

您可以通过 `share` 选项配置[分享](/docs/share)功能。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "manual"
}
```

该选项接受：

- `"manual"` - 允许通过命令手动分享（默认）
- `"auto"` - 自动分享新会话
- `"disabled"` - 完全禁用分享

默认情况下，分享设置为手动模式，您需要使用 `/share` 命令显式分享会话。

---

### 命令

您可以通过 `command` 选项为重复任务配置自定义命令。

```jsonc title="opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "command": {
    "test": {
      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",
      "description": "Run tests with coverage",
      "agent": "build",
      "model": "anthropic/claude-haiku-4-5",
    },
    "component": {
      "template": "Create a new React component named $ARGUMENTS with TypeScript support.\nInclude proper typing and basic structure.",
      "description": "Create a new component",
    },
  },
}
```

您还可以使用 `~/.config/opencode/commands/` 或 `.opencode/commands/` 中的 Markdown 文件定义命令。[在此了解更多](/docs/commands)。

---

### 快捷键

您可以通过 `keybinds` 选项自定义快捷键。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "keybinds": {}
}
```

[在此了解更多](/docs/keybinds)。

---

### 自动更新

OpenCode 启动时会自动下载新版本。您可以使用 `autoupdate` 选项禁用此功能。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "autoupdate": false
}
```

如果您不想自动更新但希望在新版本可用时收到通知，可将 `autoupdate` 设置为 `"notify"`。
请注意，此功能仅在未通过 Homebrew 等包管理器安装时有效。

---

### 格式化程序

您可以通过 `formatter` 选项配置代码格式化程序。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "formatter": {
    "prettier": {
      "disabled": true
    },
    "custom-prettier": {
      "command": ["npx", "prettier", "--write", "$FILE"],
      "environment": {
        "NODE_ENV": "development"
      },
      "extensions": [".js", ".ts", ".jsx", ".tsx"]
    }
  }
}
```

[在此了解更多关于格式化程序的信息](/docs/formatters)。

---

### 权限

默认情况下，OpenCode **允许所有操作**，无需明确批准。您可以使用 `permission` 选项更改此行为。

例如，要让 `edit` 和 `bash` 工具需要用户确认：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "ask",
    "bash": "ask"
  }
}
```

[在此了解更多关于权限的信息](/docs/permissions)。

---

### 压缩

您可以通过 `compaction` 选项控制上下文压缩行为。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "compaction": {
    "auto": true,
    "prune": false,
    "reserved": 10000
  }
}
```

- `auto` - 当上下文已满时自动压缩会话（默认值：`true`）。
- `prune` - 删除旧的工具输出以节省 Token（默认值：`false`）。
- `reserved` - 压缩时的 Token 缓冲区。保留足够的窗口以避免压缩过程中溢出。

---

### 文件监视器

您可以通过 `watcher` 选项配置文件监视器的忽略模式。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "watcher": {
    "ignore": ["node_modules/**", "dist/**", ".git/**"]
  }
}
```

模式遵循 glob 语法。使用此选项可以从文件监视中排除频繁变动的目录。

---

### MCP 服务器

您可以通过 `mcp` 选项配置要使用的 MCP 服务器。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {}
}
```

[在此了解更多](/docs/mcp-servers)。

---

### 插件

[插件](/docs/plugins)通过自定义工具、钩子和集成来扩展 OpenCode。

将插件文件放置在 `.opencode/plugins/` 或 `~/.config/opencode/plugins/` 中。您还可以通过 `plugin` 选项从 npm 加载插件。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-helicone-session", "@my-org/custom-plugin"]
}
```

[在此了解更多](/docs/plugins)。

---

### 指令

您可以通过 `instructions` 选项为所使用的模型配置指令。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]
}
```

该选项接受指令文件路径和 glob 模式的数组。[在此了解更多关于规则的信息](/docs/rules)。

---

### 禁用提供商

您可以通过 `disabled_providers` 选项禁用自动加载的提供商。当您希望阻止某些提供商被加载（即使其凭据可用）时，此选项非常有用。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "disabled_providers": ["openai", "gemini"]
}
```

:::note
`disabled_providers` 优先于 `enabled_providers`。

`disabled_providers` 选项接受提供商 ID 的数组。当某个提供商被禁用时：

- 即使设置了环境变量，也不会被加载。
- 即使通过 `/connect` 命令配置了 API 密钥，也不会被加载。
- 该提供商的模型不会出现在模型选择列表中。

---

### 启用提供商

您可以通过 `enabled_providers` 选项指定允许使用的提供商白名单。设置后，仅启用指定的提供商，所有其他提供商将被忽略。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "enabled_providers": ["anthropic", "openai"]
}
```

当您希望限制 OpenCode 仅使用特定提供商，而不是逐一禁用其他提供商时，此选项非常有用。

:::note
`disabled_providers` 优先于 `enabled_providers`。

如果某个提供商同时出现在 `enabled_providers` 和 `disabled_providers` 中，为了向后兼容，`disabled_providers` 优先。

---

### 实验性功能

`experimental` 键包含正在积极开发中的选项。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "experimental": {}
}
```

:::caution
实验性选项不稳定。它们可能会在不另行通知的情况下被更改或移除。

---

## 变量

您可以在配置文件中使用变量替换来引用环境变量和文件内容。

---

### 环境变量

使用 `{env:VARIABLE_NAME}` 来替换环境变量：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "model": "{env:OPENCODE_MODEL}",
  "provider": {
    "anthropic": {
      "models": {},
      "options": {
        "apiKey": "{env:ANTHROPIC_API_KEY}"
      }
    }
  }
}
```

如果环境变量未设置，它将被替换为空字符串。

---

### 文件

使用 `{file:path/to/file}` 来替换文件内容：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["./custom-instructions.md"],
  "provider": {
    "openai": {
      "options": {
        "apiKey": "{file:~/.secrets/openai-key}"
      }
    }
  }
}
```

文件路径可以是：

- 相对于配置文件所在目录的路径
- 以 `/` 或 `~` 开头的绝对路径

这些功能适用于：

- 将 API 密钥等敏感数据保存在单独的文件中。
- 引入大型指令文件而不会使配置变得杂乱。
- 在多个配置文件之间共享通用配置片段。

---

## enterprise

- 官方原文：https://opencode.ai/docs/zh-cn/enterprise
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-enterprise.md`

export const email = `mailto:${config.email}`

OpenCode 企业版面向希望确保代码和数据始终留在自有基础设施内的组织。它通过集中式配置与您的 SSO 和内部 AI 网关集成来实现这一目标。

:::note
OpenCode 不会存储您的任何代码或上下文数据。

开始使用 OpenCode 企业版：

1. 在团队内部进行试用。
2. **<a href={email}>联系我们</a>**，讨论定价和实施方案。

---

## 试用

OpenCode 是开源的，不会存储您的任何代码或上下文数据，因此您的开发人员可以直接[开始使用](/docs/)并进行试用。

---

### 数据处理

**OpenCode 不会存储您的代码或上下文数据。** 所有处理均在本地完成，或通过直接 API 调用发送至您的 AI 提供商。

这意味着，只要您使用的是信任的提供商或内部 AI 网关，就可以安全地使用 OpenCode。

唯一需要注意的是可选的 `/share` 功能。

---

#### 分享对话

如果用户启用了 `/share` 功能，对话及其关联数据将被发送到我们用于在 opencode.ai 上托管共享页面的服务。

数据目前通过我们 CDN 的边缘网络提供服务，并缓存在靠近用户的边缘节点上。

我们建议您在试用期间禁用此功能。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "disabled"
}
```

[了解更多关于分享的信息](/docs/share)。

---

### 代码所有权

**您拥有 OpenCode 生成的所有代码。** 不存在任何许可限制或所有权声明。

---

## 定价

OpenCode 企业版采用按席位定价模型。如果您拥有自己的 LLM 网关，我们不会对使用的 Token 收取费用。有关定价和实施方案的更多详情，请 **<a href={email}>联系我们</a>** 。

---

## 部署

完成试用并准备好在组织中使用 OpenCode 后，您可以 **<a href={email}>联系我们</a>** ，讨论定价和实施方案。

---

### 集中式配置

我们可以为您的整个组织设置 OpenCode 的统一集中式配置。

该集中式配置可与您的 SSO 提供商集成，确保所有用户仅访问您的内部 AI 网关。

---

### SSO 集成

通过集中式配置，OpenCode 可以与您组织的 SSO 提供商集成进行身份验证。

这使得 OpenCode 能够通过您现有的身份管理系统获取内部 AI 网关的凭据。

---

### 内部 AI 网关

通过集中式配置，OpenCode 还可以被配置为仅使用您的内部 AI 网关。

您还可以禁用所有其他 AI 提供商，确保所有请求都经过组织批准的基础设施。

---

### 自托管

虽然我们建议禁用共享页面以确保您的数据始终不会离开组织，但我们也可以帮助您在自己的基础设施上自行托管这些页面。

此功能目前已列入我们的路线图。如果您感兴趣，请 **<a href={email}>告诉我们</a>** 。

---

## 常见问题

<details>
<summary>什么是 OpenCode 企业版？</summary>

OpenCode 企业版面向希望确保代码和数据始终留在自有基础设施内的组织。它通过集中式配置与您的 SSO 和内部 AI 网关集成来实现这一目标。

</details>

<details>
<summary>如何开始使用 OpenCode 企业版？</summary>

只需在团队内部开始试用即可。OpenCode 默认不存储您的代码或上下文数据，因此可以轻松上手。

然后 **<a href={email}>联系我们</a>** ，讨论定价和实施方案。

</details>

<details>
<summary>企业版定价如何运作？</summary>

我们提供按席位的企业版定价。如果您拥有自己的 LLM 网关，我们不会对使用的 Token 收取费用。如需了解更多详情，请 **<a href={email}>联系我们</a>** ，获取根据您组织需求定制的报价。

</details>

<details>
<summary>我的数据在 OpenCode 企业版中是否安全？</summary>

是的。OpenCode 不会存储您的代码或上下文数据。所有处理均在本地完成，或通过直接 API 调用发送至您的 AI 提供商。通过集中式配置和 SSO 集成，您的数据将安全地保留在组织的基础设施内。

</details>

<details>
<summary>我们可以使用自己的私有 NPM 注册表吗？</summary>

OpenCode 通过 Bun 原生的 `.npmrc` 文件支持来支持私有 npm 注册表。如果您的组织使用私有注册表（例如 JFrog Artifactory、Nexus 或类似产品），请确保开发人员在运行 OpenCode 之前已完成身份验证。

要设置私有注册表的身份验证：

```bash
npm login --registry=https://your-company.jfrog.io/api/npm/npm-virtual/
```

这会创建包含身份验证信息的 `~/.npmrc` 文件。OpenCode 会自动识别并使用它。

:::caution
在运行 OpenCode 之前，您必须先登录私有注册表。

或者，您也可以手动配置 `.npmrc` 文件：

```bash title="~/.npmrc"
registry=https://your-company.jfrog.io/api/npm/npm-virtual/
//your-company.jfrog.io/api/npm/npm-virtual/:_authToken=${NPM_AUTH_TOKEN}
```

开发人员必须在运行 OpenCode 之前登录私有注册表，以确保能够从您的企业注册表安装软件包。

</details>

---

## formatters

- 官方原文：https://opencode.ai/docs/zh-cn/formatters
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-formatters.md`

OpenCode 会在文件写入或编辑后，自动使用特定语言的格式化工具对其进行格式化。这确保了生成的代码遵循你项目的代码风格。

---

## 内置格式化工具

OpenCode 内置了多种适用于主流语言和框架的格式化工具。下表列出了各格式化工具、支持的文件扩展名以及所需的命令或配置选项。

| 格式化工具           | 扩展名                                                                                                | 要求                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| air                  | .R                                                                                                    | `air` 命令可用                                                                          |
| biome                | .js, .jsx, .ts, .tsx, .html, .css, .md, .json, .yaml 及[更多](https://biomejs.dev/)                   | `biome.json(c)` 配置文件                                                                |
| cargofmt             | .rs                                                                                                   | `cargo fmt` 命令可用                                                                    |
| clang-format         | .c, .cpp, .h, .hpp, .ino 及[更多](https://clang.llvm.org/docs/ClangFormat.html)                       | `.clang-format` 配置文件                                                                |
| cljfmt               | .clj, .cljs, .cljc, .edn                                                                              | `cljfmt` 命令可用                                                                       |
| dart                 | .dart                                                                                                 | `dart` 命令可用                                                                         |
| dfmt                 | .d                                                                                                    | `dfmt` 命令可用                                                                         |
| gleam                | .gleam                                                                                                | `gleam` 命令可用                                                                        |
| gofmt                | .go                                                                                                   | `gofmt` 命令可用                                                                        |
| htmlbeautifier       | .erb, .html.erb                                                                                       | `htmlbeautifier` 命令可用                                                               |
| ktlint               | .kt, .kts                                                                                             | `ktlint` 命令可用                                                                       |
| mix                  | .ex, .exs, .eex, .heex, .leex, .neex, .sface                                                          | `mix` 命令可用                                                                          |
| nixfmt               | .nix                                                                                                  | `nixfmt` 命令可用                                                                       |
| ocamlformat          | .ml, .mli                                                                                             | `ocamlformat` 命令可用且存在 `.ocamlformat` 配置文件                                    |
| ormolu               | .hs                                                                                                   | `ormolu` 命令可用                                                                       |
| oxfmt (Experimental) | .js, .jsx, .ts, .tsx                                                                                  | `package.json` 中有 `oxfmt` 依赖，且设置了[实验性环境变量标志](/docs/cli/#experimental) |
| pint                 | .php                                                                                                  | `composer.json` 中有 `laravel/pint` 依赖                                                |
| prettier             | .js, .jsx, .ts, .tsx, .html, .css, .md, .json, .yaml 及[更多](https://prettier.io/docs/en/index.html) | `package.json` 中有 `prettier` 依赖                                                     |
| rubocop              | .rb, .rake, .gemspec, .ru                                                                             | `rubocop` 命令可用                                                                      |
| ruff                 | .py, .pyi                                                                                             | `ruff` 命令可用且有相应配置                                                             |
| rustfmt              | .rs                                                                                                   | `rustfmt` 命令可用                                                                      |
| shfmt                | .sh, .bash                                                                                            | `shfmt` 命令可用                                                                        |
| standardrb           | .rb, .rake, .gemspec, .ru                                                                             | `standardrb` 命令可用                                                                   |
| terraform            | .tf, .tfvars                                                                                          | `terraform` 命令可用                                                                    |
| uv                   | .py, .pyi                                                                                             | `uv` 命令可用                                                                           |
| zig                  | .zig, .zon                                                                                            | `zig` 命令可用                                                                          |

因此，如果你的项目 `package.json` 中包含 `prettier`，OpenCode 会自动使用它进行格式化。

---

## 工作原理

当 OpenCode 写入或编辑文件时，它会：

1. 根据所有已启用的格式化工具检查文件扩展名。
2. 对文件运行相应的格式化命令。
3. 自动应用格式化更改。

整个过程在后台完成，无需任何手动操作即可保持代码风格的一致性。

---

## 配置

你可以通过 OpenCode 配置中的 `formatter` 部分自定义格式化工具。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "formatter": {}
}
```

每个格式化工具的配置支持以下属性：

| 属性          | 类型     | 描述                           |
| ------------- | -------- | ------------------------------ |
| `disabled`    | boolean  | 设为 `true` 可禁用该格式化工具 |
| `command`     | string[] | 执行格式化的命令               |
| `environment` | object   | 运行格式化工具时设置的环境变量 |
| `extensions`  | string[] | 该格式化工具处理的文件扩展名   |

下面来看一些示例。

---

### 禁用格式化工具

要全局禁用**所有**格式化工具，将 `formatter` 设为 `false`：

```json title="opencode.json" {3}
{
  "$schema": "https://opencode.ai/config.json",
  "formatter": false
}
```

要禁用**特定**格式化工具，将 `disabled` 设为 `true`：

```json title="opencode.json" {5}
{
  "$schema": "https://opencode.ai/config.json",
  "formatter": {
    "prettier": {
      "disabled": true
    }
  }
}
```

---

### 自定义格式化工具

你可以通过指定命令、环境变量和文件扩展名来覆盖内置格式化工具或添加新的格式化工具：

```json title="opencode.json" {4-14}
{
  "$schema": "https://opencode.ai/config.json",
  "formatter": {
    "prettier": {
      "command": ["npx", "prettier", "--write", "$FILE"],
      "environment": {
        "NODE_ENV": "development"
      },
      "extensions": [".js", ".ts", ".jsx", ".tsx"]
    },
    "custom-markdown-formatter": {
      "command": ["deno", "fmt", "$FILE"],
      "extensions": [".md"]
    }
  }
}
```

命令中的 **`$FILE` 占位符**会被替换为待格式化文件的路径。

---

## HTTPS proxy (recommended)

- 官方原文：https://opencode.ai/docs/zh-cn/network
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-network.md`

OpenCode 支持标准代理环境变量和自定义证书，适用于企业网络环境。

---

## 代理

OpenCode 遵循标准代理环境变量。

```bash
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for local server (required)
export NO_PROXY=localhost,127.0.0.1
```

:::caution
TUI 与本地 HTTP 服务器进行通信。你必须为此连接绕过代理，以防止路由循环。

你可以使用 [CLI 标志](/docs/cli#run)来配置服务器的端口和主机名。

---

### 身份验证

如果你的代理需要基本身份验证，请在 URL 中包含凭据。

```bash
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

:::caution
避免将密码硬编码在代码中。请使用环境变量或安全的凭据存储方式。

对于需要高级身份验证（如 NTLM 或 Kerberos）的代理，建议使用支持相应身份验证方式的 LLM 网关。

---

## 自定义证书

如果你的企业使用自定义 CA 进行 HTTPS 连接，请配置 OpenCode 以信任这些证书。

```bash
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

此配置同时适用于代理连接和直接 API 访问。

---

## permissions

- 官方原文：https://opencode.ai/docs/zh-cn/permissions
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-permissions.md`

OpenCode 使用 `permission` 配置来决定某个操作是否应自动运行、提示你审批，还是被阻止。

从 `v1.1.1` 开始，旧版 `tools` 布尔配置已被弃用，并已合并到 `permission` 中。旧版 `tools` 配置仍然支持，以保持向后兼容。

---

## 操作

每条权限规则解析为以下之一：

- `"allow"` — 无需审批直接运行
- `"ask"` — 提示审批
- `"deny"` — 阻止该操作

---

## 配置

你可以全局设置权限（使用 `*`），并覆盖特定工具的权限。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "*": "ask",
    "bash": "allow",
    "edit": "deny"
  }
}
```

你还可以一次性设置所有权限：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": "allow"
}
```

---

## 细粒度规则（对象语法）

对于大多数权限，你可以使用对象来根据工具输入应用不同的操作。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": {
      "*": "ask",
      "git *": "allow",
      "npm *": "allow",
      "rm *": "deny",
      "grep *": "allow"
    },
    "edit": {
      "*": "deny",
      "packages/web/src/content/docs/*.mdx": "allow"
    }
  }
}
```

规则通过模式匹配进行评估，**最后匹配的规则优先**。常见做法是将通配的 `"*"` 规则放在最前面，更具体的规则放在后面。

### 通配符

权限模式使用简单的通配符匹配：

- `*` 匹配零个或多个任意字符
- `?` 精确匹配一个字符
- 所有其他字符按字面值匹配

### 主目录展开

你可以在模式开头使用 `~` 或 `$HOME` 来引用你的主目录。这对于 [`external_directory`](#外部目录) 规则特别有用。

- `~/projects/*` -> `/Users/username/projects/*`
- `$HOME/projects/*` -> `/Users/username/projects/*`
- `~` -> `/Users/username`

### 外部目录

使用 `external_directory` 允许工具调用访问 OpenCode 启动时工作目录之外的路径。这适用于任何接受路径作为输入的工具（例如 `read`、`edit`、`glob`、`grep` 以及许多 `bash` 命令）。

主目录展开（如 `~/...`）仅影响模式的书写方式。它不会将外部路径纳入当前工作空间，因此工作目录之外的路径仍然必须通过 `external_directory` 来允许。

例如，以下配置允许访问 `~/projects/personal/` 下的所有内容：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "external_directory": {
      "~/projects/personal/**": "allow"
    }
  }
}
```

此处允许的任何目录都会继承与当前工作空间相同的默认值。由于 [`read` 默认为 `allow`](#默认值)，`external_directory` 下的条目也允许读取，除非另行覆盖。当需要在这些路径中限制某个工具时，请添加显式规则，例如在保留读取的同时阻止编辑：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "external_directory": {
      "~/projects/personal/**": "allow"
    },
    "edit": {
      "~/projects/personal/**": "deny"
    }
  }
}
```

请将列表限定在受信任的路径上，并根据需要为其他工具（例如 `bash`）叠加额外的允许或拒绝规则。

---

## 可用权限

OpenCode 的权限以工具名称为键，外加几个安全防护项：

- `read` — 读取文件（匹配文件路径）
- `edit` — 所有文件修改（涵盖 `edit`、`write`、`patch`）
- `glob` — 文件通配（匹配通配模式）
- `grep` — 内容搜索（匹配正则表达式模式）
- `bash` — 运行 shell 命令（匹配解析后的命令，如 `git status --porcelain`）
- `task` — 启动子代理（匹配子代理类型）
- `skill` — 加载技能（匹配技能名称）
- `lsp` — 运行 LSP 查询（当前不支持细粒度配置）
- `webfetch` — 获取 URL（匹配 URL）
- `websearch` — 网页搜索（匹配查询内容）
- `external_directory` — 当工具访问项目工作目录之外的路径时触发
- `doom_loop` — 当同一工具调用以相同输入重复 3 次时触发

---

## 默认值

如果你未指定任何配置，OpenCode 将使用宽松的默认值：

- 大多数权限默认为 `"allow"`。
- `doom_loop` 和 `external_directory` 默认为 `"ask"`。
- `read` 为 `"allow"`，但 `.env` 文件默认被拒绝：

```json title="opencode.json"
{
  "permission": {
    "read": {
      "*": "allow",
      "*.env": "deny",
      "*.env.*": "deny",
      "*.env.example": "allow"
    }
  }
}
```

---

## "Ask"的作用

当 OpenCode 提示审批时，界面提供三种选择：

- `once` — 仅批准本次请求
- `always` — 批准与建议模式匹配的后续请求（在当前 OpenCode 会话的剩余时间内有效）
- `reject` — 拒绝请求

`always` 所批准的模式集合由工具提供（例如，bash 审批通常会将安全的命令前缀如 `git status*` 加入白名单）。

---

## 代理

你可以为每个代理单独覆盖权限。代理权限会与全局配置合并，且代理规则优先。[了解更多](/docs/agents#permissions)关于代理权限的内容。

:::note
有关更详细的模式匹配示例，请参阅上方的[细粒度规则（对象语法）](#细粒度规则对象语法)部分。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": {
      "*": "ask",
      "git *": "allow",
      "git commit *": "deny",
      "git push *": "deny",
      "grep *": "allow"
    }
  },
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "*": "ask",
          "git *": "allow",
          "git commit *": "ask",
          "git push *": "deny",
          "grep *": "allow"
        }
      }
    }
  }
}
```

你还可以在 Markdown 中配置代理权限：

```markdown title="~/.config/opencode/agents/review.md"
---
description: Code review without edits
mode: subagent
permission:
  edit: deny
  bash: ask
  webfetch: deny
---

Only analyze code and suggest changes.
```

:::tip
对带参数的命令使用模式匹配。`"grep *"` 允许执行 `grep pattern file.txt`，而单独的 `"grep"` 则会阻止它。像 `git status` 这样的命令适用于默认行为，但在传递参数时需要显式权限（如 `"git status *"`）。

---

## Policies

- 官方原文：https://opencode.ai/docs/zh-cn/policies
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-policies.md`

# Policies

Control which configured resources OpenCode may use. 

此内容尚不支持你的语言。 

Policies control whether OpenCode may perform an action on a named resource. This feature is experimental and is configured with the experimental.policies array in opencode.json.

Policies are separate from permissions. Permissions control what tools can do during a session, while policies control whether OpenCode may use a resource such as an LLM provider.
 

## Configuration

Each policy statement has three fields:
 

- effect - Either "allow" or "deny".

- action - The operation being controlled.

- resource - The resource ID or wildcard pattern the statement applies to.
 

For example, deny use of the openai provider:
 opencode.json 

{ "$schema": "https://opencode.ai/config.json", "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "openai" } ] }}
A provider denied by policy is not available for model selection or model use, even if it has credentials or is otherwise configured correctly.
 

## Available Policies

OpenCode currently supports one policy action:

 Action Resource Description provider.use Provider ID, such as openai Allow or deny use of an LLM provider. 

More policy actions may be added in the future.
 

## Matching

The resource field supports wildcard matching. Use * to match zero or more characters and ? to match one character.
 opencode.json 

{ "$schema": "https://opencode.ai/config.json", "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "company-*" } ] }}
This denies providers such as company-us and company-eu.
 

## Rule Order

When multiple statements match, the last matching statement wins. Put broad rules first, then more specific exceptions after them.

For example, allow only Anthropic:
 opencode.json 

{ "$schema": "https://opencode.ai/config.json", "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "*" }, { "effect": "allow", "action": "provider.use", "resource": "anthropic" } ] }}
If no policy matches a provider, provider use is allowed by default.

Policies may be set in both your global config and project config. If policies from both locations match the same provider, your global policy takes priority over the project policy. This prevents a repository from re-enabling a provider that you deny globally.
 

## Provider Lists

Use policies instead of the older disabled_providers and enabled_providers settings when controlling provider access.

To replace disabled_providers:
 opencode.json 

{ "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "openai" }, { "effect": "deny", "action": "provider.use", "resource": "google" } ] }}
To replace enabled_providers, deny all providers first and allow the selected providers after it:
 opencode.json { "experimental" : { "policies" : [ { "effect" : "deny" , "action" : "provider.use" , "resource" : "*" }, { "effect" : "allow" , "action" : "provider.use" , "resource" : "anthropic" }, { "effect" : "allow" , "action" : "provider.use" , "resource" : "openai" } ] } }

---

## SST v3 Monorepo Project

- 官方原文：https://opencode.ai/docs/zh-cn/rules
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-rules.md`

您可以通过创建 `AGENTS.md` 文件来为 opencode 提供自定义指令。这类似于 Cursor 的规则功能。该文件包含的指令会被纳入 LLM 的上下文中，以便针对您的特定项目自定义其行为。

---

## 初始化

要创建新的 `AGENTS.md` 文件，您可以在 opencode 中运行 `/init` 命令。

:::tip
您应该将项目的 `AGENTS.md` 文件提交到 Git。

该命令会扫描您的项目及其所有内容，了解项目的用途，并据此生成一个 `AGENTS.md` 文件。这有助于 opencode 更好地导航您的项目。

如果您已有 `AGENTS.md` 文件，该命令会尝试在其基础上进行补充。

---

## 示例

您也可以手动创建此文件。以下是一些可以放入 `AGENTS.md` 文件中的内容示例。

```markdown title="AGENTS.md"
# SST v3 Monorepo Project

This is an SST v3 monorepo with TypeScript. The project uses bun workspaces for package management.

## Project Structure

- `packages/` - Contains all workspace packages (functions, core, web, etc.)
- `infra/` - Infrastructure definitions split by service (storage.ts, api.ts, web.ts)
- `sst.config.ts` - Main SST configuration with dynamic imports

## Code Standards

- Use TypeScript with strict mode enabled
- Shared code goes in `packages/core/` with proper exports configuration
- Functions go in `packages/functions/`
- Infrastructure should be split into logical files in `infra/`

## Monorepo Conventions

- Import shared modules using workspace names: `@my-app/core/example`
```

我们在这里添加了项目特定的指令，这些指令会在您的团队中共享。

---

## 类型

opencode 还支持从多个位置读取 `AGENTS.md` 文件，不同的位置有不同的用途。

### 项目级

在项目根目录放置一个 `AGENTS.md` 文件，用于定义项目特定的规则。这些规则仅在您在该目录或其子目录中工作时生效。

### 全局级

您还可以在 `~/.config/opencode/AGENTS.md` 文件中设置全局规则。这些规则会应用于所有 opencode 会话。

由于该文件不会被提交到 Git 或与团队共享，我们建议用它来指定 LLM 应遵循的个人规则。

### Claude Code 兼容性

对于从 Claude Code 迁移过来的用户，OpenCode 支持 Claude Code 的文件约定作为回退方案：

- **项目规则**：项目目录中的 `CLAUDE.md`（在没有 `AGENTS.md` 的情况下使用）
- **全局规则**：`~/.claude/CLAUDE.md`（在没有 `~/.config/opencode/AGENTS.md` 的情况下使用）
- **技能**：`~/.claude/skills/` — 详情请参阅[代理技能](/docs/skills/)

要禁用 Claude Code 兼容性，请设置以下环境变量之一：

```bash
export OPENCODE_DISABLE_CLAUDE_CODE=1        # Disable all .claude support
export OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1 # Disable only ~/.claude/CLAUDE.md
export OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1 # Disable only .claude/skills
```

---

## 优先级

当 opencode 启动时，它会按以下顺序查找规则文件：

1. **本地文件**，从当前目录向上遍历（`AGENTS.md`、`CLAUDE.md`）
2. **全局文件**，位于 `~/.config/opencode/AGENTS.md`
3. **Claude Code 文件**，位于 `~/.claude/CLAUDE.md`（除非已禁用）

在每个类别中，第一个匹配的文件优先。例如，如果您同时拥有 `AGENTS.md` 和 `CLAUDE.md`，则只会使用 `AGENTS.md`。同样，`~/.config/opencode/AGENTS.md` 优先于 `~/.claude/CLAUDE.md`。

---

## 自定义指令

您可以在 `opencode.json` 或全局配置文件 `~/.config/opencode/opencode.json` 中指定自定义指令文件。这允许您和团队复用现有规则，而无需将它们复制到 AGENTS.md 中。

示例：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]
}
```

您还可以使用远程 URL 从网络加载指令。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["https://raw.githubusercontent.com/my-org/shared-rules/main/style.md"]
}
```

远程指令的获取超时时间为 5 秒。

所有指令文件都会与您的 `AGENTS.md` 文件合并。

---

## 引用外部文件

虽然 opencode 不会自动解析 `AGENTS.md` 中的文件引用，但您可以通过以下两种方式实现类似的功能：

### 使用 opencode.json

推荐的方式是使用 `opencode.json` 中的 `instructions` 字段：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["docs/development-standards.md", "test/testing-guidelines.md", "packages/*/AGENTS.md"]
}
```

### 在 AGENTS.md 中手动指定

您可以在 `AGENTS.md` 中提供明确的指令，教 opencode 读取外部文件。以下是一个实际示例：

```markdown title="AGENTS.md"
# TypeScript Project Rules

## External File Loading

CRITICAL: When you encounter a file reference (e.g., @rules/general.md), use your Read tool to load it on a need-to-know basis. They're relevant to the SPECIFIC task at hand.

Instructions:

- Do NOT preemptively load all references - use lazy loading based on actual need
- When loaded, treat content as mandatory instructions that override defaults
- Follow references recursively when needed

## Development Guidelines

For TypeScript code style and best practices: @docs/typescript-guidelines.md
For React component architecture and hooks patterns: @docs/react-patterns.md
For REST API design and error handling: @docs/api-standards.md
For testing strategies and coverage requirements: @test/testing-guidelines.md

## General Guidelines

Read the following file immediately as it's relevant to all workflows: @rules/general-guidelines.md.
```

这种方式允许您：

- 创建模块化、可复用的规则文件
- 通过符号链接或 Git 子模块在项目之间共享规则
- 保持 AGENTS.md 简洁，同时引用详细的指南
- 确保 opencode 仅在特定任务需要时才加载文件

:::tip
对于 monorepo 或具有共享标准的项目，使用 `opencode.json` 配合 glob 模式（如 `packages/*/AGENTS.md`）比手动指定指令更易于维护。

---

## themes

- 官方原文：https://opencode.ai/docs/zh-cn/themes
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-themes.md`

通过 OpenCode，您可以从多个内置主题中进行选择，使用能自动适配终端主题的主题，或者定义您自己的自定义主题。

默认情况下，OpenCode 使用我们自己的 `opencode` 主题。

---

## 终端要求

为了使主题能够正确显示完整的调色板，您的终端必须支持**真彩色**（24 位色）。大多数现代终端默认支持此功能，但您可能需要手动启用：

- **检查支持情况**：运行 `echo $COLORTERM` — 输出应为 `truecolor` 或 `24bit`
- **启用真彩色**：在您的 shell 配置文件中设置环境变量 `COLORTERM=truecolor`
- **终端兼容性**：确保您的终端模拟器支持 24 位色（大多数现代终端如 iTerm2、Alacritty、Kitty、Windows Terminal 以及较新版本的 GNOME Terminal 均已支持）

如果没有真彩色支持，主题可能会出现色彩精度下降的情况，或者回退到最接近的 256 色近似值。

---

## 内置主题

OpenCode 自带多个内置主题。

| 名称                   | 描述                                                                |
| ---------------------- | ------------------------------------------------------------------- |
| `system`               | 自动适配终端的背景颜色                                              |
| `tokyonight`           | 基于 [Tokyonight](https://github.com/folke/tokyonight.nvim) 主题    |
| `everforest`           | 基于 [Everforest](https://github.com/sainnhe/everforest) 主题       |
| `ayu`                  | 基于 [Ayu](https://github.com/ayu-theme) 暗色主题                   |
| `catppuccin`           | 基于 [Catppuccin](https://github.com/catppuccin) 主题               |
| `catppuccin-macchiato` | 基于 [Catppuccin](https://github.com/catppuccin) 主题               |
| `gruvbox`              | 基于 [Gruvbox](https://github.com/morhetz/gruvbox) 主题             |
| `kanagawa`             | 基于 [Kanagawa](https://github.com/rebelot/kanagawa.nvim) 主题      |
| `nord`                 | 基于 [Nord](https://github.com/nordtheme/nord) 主题                 |
| `matrix`               | 黑客风格的黑底绿字主题                                              |
| `one-dark`             | 基于 [Atom One](https://github.com/Th3Whit3Wolf/one-nvim) Dark 主题 |

我们还在不断添加更多主题。

---

## 系统主题

`system` 主题旨在自动适配您终端的配色方案。与使用固定颜色的传统主题不同，_system_ 主题具有以下特点：

- **生成灰度色阶**：根据终端的背景颜色创建自定义灰度色阶，确保最佳对比度。
- **使用 ANSI 颜色**：利用标准 ANSI 颜色（0-15）进行语法高亮和 UI 元素渲染，遵循终端的调色板设置。
- **保留终端默认值**：将文本和背景颜色设为 `none`，以保持终端的原生外观。

系统主题适合以下用户：

- 希望 OpenCode 与终端的外观保持一致
- 使用了自定义终端配色方案
- 偏好所有终端应用程序拥有统一的视觉风格

---

## 使用主题

您可以通过 `/theme` 命令调出主题选择界面来选择主题，也可以在 `tui.json` 文件中直接指定。

```json title="tui.json" {3}
{
  "$schema": "https://opencode.ai/tui.json",
  "theme": "tokyonight"
}
```

---

## 自定义主题

OpenCode 支持灵活的基于 JSON 的主题系统，让用户可以轻松创建和自定义主题。

---

### 层级优先级

主题按以下顺序从多个目录加载，后面的目录会覆盖前面的目录：

1. **内置主题** — 嵌入在二进制文件中
2. **用户配置目录** — 定义在 `~/.config/opencode/themes/*.json` 或 `$XDG_CONFIG_HOME/opencode/themes/*.json`
3. **项目根目录** — 定义在 `<project-root>/.opencode/themes/*.json`
4. **当前工作目录** — 定义在 `./.opencode/themes/*.json`

如果多个目录包含同名主题，将使用优先级较高的目录中的主题。

---

### 创建主题

要创建自定义主题，请在上述任一主题目录中创建一个 JSON 文件。

创建用户级主题：

```bash no-frame
mkdir -p ~/.config/opencode/themes
vim ~/.config/opencode/themes/my-theme.json
```

创建项目级主题：

```bash no-frame
mkdir -p .opencode/themes
vim .opencode/themes/my-theme.json
```

---

### JSON 格式

主题使用灵活的 JSON 格式，支持以下特性：

- **十六进制颜色**：`"#ffffff"`
- **ANSI 颜色**：`3`（0-255）
- **颜色引用**：`"primary"` 或自定义定义的颜色名
- **深色/浅色变体**：`{"dark": "#000", "light": "#fff"}`
- **无颜色**：`"none"` — 使用终端的默认颜色或透明背景

---

### 颜色定义

`defs` 部分是可选的，它允许您定义可在主题中重复引用的可复用颜色。

---

### 终端默认值

特殊值 `"none"` 可用于任何颜色属性，以继承终端的默认颜色。这在创建需要与终端配色方案无缝融合的主题时特别有用：

- `"text": "none"` — 使用终端的默认前景色
- `"background": "none"` — 使用终端的默认背景色

---

### 示例

以下是一个自定义主题的完整示例：

```json title="my-theme.json"
{
  "$schema": "https://opencode.ai/theme.json",
  "defs": {
    "nord0": "#2E3440",
    "nord1": "#3B4252",
    "nord2": "#434C5E",
    "nord3": "#4C566A",
    "nord4": "#D8DEE9",
    "nord5": "#E5E9F0",
    "nord6": "#ECEFF4",
    "nord7": "#8FBCBB",
    "nord8": "#88C0D0",
    "nord9": "#81A1C1",
    "nord10": "#5E81AC",
    "nord11": "#BF616A",
    "nord12": "#D08770",
    "nord13": "#EBCB8B",
    "nord14": "#A3BE8C",
    "nord15": "#B48EAD"
  },
  "theme": {
    "primary": {
      "dark": "nord8",
      "light": "nord10"
    },
    "secondary": {
      "dark": "nord9",
      "light": "nord9"
    },
    "accent": {
      "dark": "nord7",
      "light": "nord7"
    },
    "error": {
      "dark": "nord11",
      "light": "nord11"
    },
    "warning": {
      "dark": "nord12",
      "light": "nord12"
    },
    "success": {
      "dark": "nord14",
      "light": "nord14"
    },
    "info": {
      "dark": "nord8",
      "light": "nord10"
    },
    "text": {
      "dark": "nord4",
      "light": "nord0"
    },
    "textMuted": {
      "dark": "nord3",
      "light": "nord1"
    },
    "background": {
      "dark": "nord0",
      "light": "nord6"
    },
    "backgroundPanel": {
      "dark": "nord1",
      "light": "nord5"
    },
    "backgroundElement": {
      "dark": "nord1",
      "light": "nord4"
    },
    "border": {
      "dark": "nord2",
      "light": "nord3"
    },
    "borderActive": {
      "dark": "nord3",
      "light": "nord2"
    },
    "borderSubtle": {
      "dark": "nord2",
      "light": "nord3"
    },
    "diffAdded": {
      "dark": "nord14",
      "light": "nord14"
    },
    "diffRemoved": {
      "dark": "nord11",
      "light": "nord11"
    },
    "diffContext": {
      "dark": "nord3",
      "light": "nord3"
    },
    "diffHunkHeader": {
      "dark": "nord3",
      "light": "nord3"
    },
    "diffHighlightAdded": {
      "dark": "nord14",
      "light": "nord14"
    },
    "diffHighlightRemoved": {
      "dark": "nord11",
      "light": "nord11"
    },
    "diffAddedBg": {
      "dark": "#3B4252",
      "light": "#E5E9F0"
    },
    "diffRemovedBg": {
      "dark": "#3B4252",
      "light": "#E5E9F0"
    },
    "diffContextBg": {
      "dark": "nord1",
      "light": "nord5"
    },
    "diffLineNumber": {
      "dark": "nord2",
      "light": "nord4"
    },
    "diffAddedLineNumberBg": {
      "dark": "#3B4252",
      "light": "#E5E9F0"
    },
    "diffRemovedLineNumberBg": {
      "dark": "#3B4252",
      "light": "#E5E9F0"
    },
    "markdownText": {
      "dark": "nord4",
      "light": "nord0"
    },
    "markdownHeading": {
      "dark": "nord8",
      "light": "nord10"
    },
    "markdownLink": {
      "dark": "nord9",
      "light": "nord9"
    },
    "markdownLinkText": {
      "dark": "nord7",
      "light": "nord7"
    },
    "markdownCode": {
      "dark": "nord14",
      "light": "nord14"
    },
    "markdownBlockQuote": {
      "dark": "nord3",
      "light": "nord3"
    },
    "markdownEmph": {
      "dark": "nord12",
      "light": "nord12"
    },
    "markdownStrong": {
      "dark": "nord13",
      "light": "nord13"
    },
    "markdownHorizontalRule": {
      "dark": "nord3",
      "light": "nord3"
    },
    "markdownListItem": {
      "dark": "nord8",
      "light": "nord10"
    },
    "markdownListEnumeration": {
      "dark": "nord7",
      "light": "nord7"
    },
    "markdownImage": {
      "dark": "nord9",
      "light": "nord9"
    },
    "markdownImageText": {
      "dark": "nord7",
      "light": "nord7"
    },
    "markdownCodeBlock": {
      "dark": "nord4",
      "light": "nord0"
    },
    "syntaxComment": {
      "dark": "nord3",
      "light": "nord3"
    },
    "syntaxKeyword": {
      "dark": "nord9",
      "light": "nord9"
    },
    "syntaxFunction": {
      "dark": "nord8",
      "light": "nord8"
    },
    "syntaxVariable": {
      "dark": "nord7",
      "light": "nord7"
    },
    "syntaxString": {
      "dark": "nord14",
      "light": "nord14"
    },
    "syntaxNumber": {
      "dark": "nord15",
      "light": "nord15"
    },
    "syntaxType": {
      "dark": "nord7",
      "light": "nord7"
    },
    "syntaxOperator": {
      "dark": "nord9",
      "light": "nord9"
    },
    "syntaxPunctuation": {
      "dark": "nord4",
      "light": "nord0"
    }
  }
}
```
