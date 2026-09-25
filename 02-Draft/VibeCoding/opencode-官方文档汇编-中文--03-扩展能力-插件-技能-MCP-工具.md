---
title: opencode 官方文档汇编（中文） · 03-扩展能力（插件·技能·MCP·工具）
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-zh-agents.md
- VibeCoding/opencode/opencode-zh-custom-tools.md
- VibeCoding/opencode/opencode-zh-lsp.md
- VibeCoding/opencode/opencode-zh-mcp-servers.md
- VibeCoding/opencode/opencode-zh-plugins.md
- VibeCoding/opencode/opencode-zh-skills.md
- VibeCoding/opencode/opencode-zh-tools.md
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

## agents

- 官方原文：https://opencode.ai/docs/zh-cn/agents
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-agents.md`

代理是专门的 AI 助手，可以针对特定任务和工作流程进行配置。它们允许您创建具有自定义提示词、模型和工具访问权限的专用工具。

:::tip
使用 Plan 代理来分析代码和审查建议，而不会进行任何代码更改。

您可以在会话期间切换代理，或使用 `@` 提及来调用它们。

---

## 类型

OpenCode 中有两种类型的代理：主代理和子代理。

---

### 主代理

主代理是您直接交互的主要助手。您可以使用 **Tab** 键或配置的 `switch_agent` 快捷键来循环切换它们。这些代理处理您的主要对话。工具访问通过权限进行配置——例如，Build 启用了所有工具，而 Plan 则受到限制。

:::tip
您可以在会话期间使用 **Tab** 键在主代理之间切换。

OpenCode 内置了两个主代理：**Build** 和 **Plan**。我们将在下面介绍它们。

---

### 子代理

子代理是主代理可以调用来执行特定任务的专业助手。您也可以通过在消息中 **@ 提及**它们来手动调用。

OpenCode 内置了三个子代理：**General**、**Explore** 和 **Scout**。我们将在下面介绍它们。

---

## 内置代理

OpenCode 内置了两个主代理和三个子代理。

---

### 使用 Build

_模式_：`primary`

Build 是启用了所有工具的**默认**主代理。这是用于需要完全访问文件操作和系统命令的开发工作的标准代理。

---

### 使用 Plan

_模式_：`primary`

一个专为规划和分析设计的受限代理。我们使用权限系统来为您提供更多控制权，并防止意外更改。
默认情况下，以下所有项均设置为 `ask`：

- `file edits`：所有写入、补丁和编辑
- `bash`：所有 bash 命令

当您希望 LLM 分析代码、建议更改或创建计划，而不对代码库进行任何实际修改时，此代理非常有用。

---

### 使用 General

_模式_：`subagent`

一个用于研究复杂问题和执行多步骤任务的通用代理。拥有完整的工具访问权限（todo 除外），因此可以在需要时修改文件。可用于并行运行多个工作单元。

---

### 使用 Explore

_模式_：`subagent`

一个用于探索代码库的快速只读代理。无法修改文件。当您需要按模式快速查找文件、搜索代码中的关键字或回答有关代码库的问题时，请使用此代理。

---

### 使用 Scout

_模式_：`subagent`

一个用于外部文档和依赖研究的只读代理。当您需要将某个依赖仓库克隆到 OpenCode 的托管缓存中、检查库的源代码，或在不修改工作区的情况下将本地代码与 upstream 实现进行交叉对照时，请使用此代理。

---

### 使用 Compaction

_模式_：`primary`

隐藏的系统代理，将长上下文压缩为较小的摘要。它会在需要时自动运行，且无法在 UI 中选择。

---

### 使用 Title

_模式_：`primary`

隐藏的系统代理，用于生成简短的会话标题。它会自动运行，且无法在 UI 中选择。

---

### 使用 Summary

_模式_：`primary`

隐藏的系统代理，用于创建会话摘要。它会自动运行，且无法在 UI 中选择。

---

## 用法

1. 对于主代理，在会话期间使用 **Tab** 键循环切换。您也可以使用配置的 `switch_agent` 快捷键。

2. 子代理可以通过以下方式调用：
   - 由主代理根据其描述**自动**调用以执行专门任务。
   - 通过在消息中 **@ 提及**子代理来手动调用。例如：

     ```txt frame="none"
     @general help me search for this function
     ```

3. **会话间导航**：当子代理创建自己的子会话时，您可以使用以下方式在父会话和所有子会话之间导航：
   - **\<Leader>+Right**（或配置的 `session_child_cycle` 快捷键）向前循环：父会话 → 子会话1 → 子会话2 → ... → 父会话
   - **\<Leader>+Left**（或配置的 `session_child_cycle_reverse` 快捷键）向后循环：父会话 ← 子会话1 ← 子会话2 ← ... ← 父会话

   这使您可以在主对话和专门的子代理工作之间无缝切换。

---

## 配置

您可以自定义内置代理或通过配置创建自己的代理。代理可以通过两种方式进行配置：

---

### JSON

在 `opencode.json` 配置文件中配置代理：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "mode": "primary",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:./prompts/build.txt}",
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    },
    "plan": {
      "mode": "primary",
      "model": "anthropic/claude-haiku-4-20250514",
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    },
    "code-reviewer": {
      "description": "Reviews code for best practices and potential issues",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```

---

### Markdown

您还可以使用 Markdown 文件定义代理。将它们放在：

- 全局：`~/.config/opencode/agents/`
- 项目级：`.opencode/agents/`

```markdown title="~/.config/opencode/agents/review.md"
---
description: Reviews code for quality and best practices
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
---

You are in code review mode. Focus on:

- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
- Security considerations

Provide constructive feedback without making direct changes.
```

Markdown 文件名即为代理名称。例如，`review.md` 会创建一个名为 `review` 的代理。

---

## 选项

让我们详细了解这些配置选项。

---

### 描述

使用 `description` 选项提供代理的功能及使用场景的简要描述。

```json title="opencode.json"
{
  "agent": {
    "review": {
      "description": "Reviews code for best practices and potential issues"
    }
  }
}
```

这是一个**必需的**配置选项。

---

### 温度

使用 `temperature` 配置控制 LLM 响应的随机性和创造力。

较低的值使响应更加集中和确定，而较高的值则增加创造力和多样性。

```json title="opencode.json"
{
  "agent": {
    "plan": {
      "temperature": 0.1
    },
    "creative": {
      "temperature": 0.8
    }
  }
}
```

温度值通常范围为 0.0 到 1.0：

- **0.0-0.2**：非常集中和确定性的响应，适合代码分析和规划
- **0.3-0.5**：平衡的响应，兼顾一定创造力，适合一般开发任务
- **0.6-1.0**：更有创造力和多样性的响应，适合头脑风暴和探索

```json title="opencode.json"
{
  "agent": {
    "analyze": {
      "temperature": 0.1,
      "prompt": "{file:./prompts/analysis.txt}"
    },
    "build": {
      "temperature": 0.3
    },
    "brainstorm": {
      "temperature": 0.7,
      "prompt": "{file:./prompts/creative.txt}"
    }
  }
}
```

如果未指定温度，OpenCode 将使用模型特定的默认值；大多数模型通常为 0，Qwen 模型为 0.55。

---

### 最大步数

控制代理在被强制以纯文本响应之前可以执行的最大代理迭代次数。这允许希望控制成本的用户对代理操作设置限制。

如果未设置此选项，代理将持续迭代，直到模型选择停止或用户中断会话。

```json title="opencode.json"
{
  "agent": {
    "quick-thinker": {
      "description": "Fast reasoning with limited iterations",
      "prompt": "You are a quick thinker. Solve problems with minimal steps.",
      "steps": 5
    }
  }
}
```

当达到限制时，代理会收到一个特殊的系统提示词，指示其回复工作摘要和建议的剩余任务。

:::caution
旧版 `maxSteps` 字段已弃用。请改用 `steps`。

---

### 禁用

设置为 `true` 以禁用代理。

```json title="opencode.json"
{
  "agent": {
    "review": {
      "disable": true
    }
  }
}
```

---

### 提示词

使用 `prompt` 配置为代理指定自定义系统提示词文件。提示词文件应包含针对代理用途的具体指令。

```json title="opencode.json"
{
  "agent": {
    "review": {
      "prompt": "{file:./prompts/code-review.txt}"
    }
  }
}
```

此路径相对于配置文件所在位置。因此它同时适用于全局 OpenCode 配置和项目级配置。

---

### 模型

使用 `model` 配置为代理覆盖模型。适用于针对不同任务使用不同的优化模型。例如，用更快的模型进行规划，用更强大的模型进行实现。

:::tip
如果您不指定模型，主代理将使用[全局配置的模型](/docs/config#models)，而子代理将使用调用它的主代理所使用的模型。

```json title="opencode.json"
{
  "agent": {
    "plan": {
      "model": "anthropic/claude-haiku-4-20250514"
    }
  }
}
```

OpenCode 配置中的模型 ID 使用 `provider/model-id` 格式。例如，如果您使用 [OpenCode Zen](/docs/zen)，则可以使用 `opencode/gpt-5.1-codex` 来表示 GPT 5.1 Codex。

---

### 工具

使用 `tools` 配置控制代理中可用的工具。您可以通过将特定工具设置为 `true` 或 `false` 来启用或禁用它们。

```json title="opencode.json" {3-6,9-12}
{
  "$schema": "https://opencode.ai/config.json",
  "tools": {
    "write": true,
    "bash": true
  },
  "agent": {
    "plan": {
      "tools": {
        "write": false,
        "bash": false
      }
    }
  }
}
```

:::note
代理级配置会覆盖全局配置。

您还可以使用通配符同时控制多个工具。例如，要禁用 MCP 服务器中的所有工具：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "readonly": {
      "tools": {
        "mymcp_*": false,
        "write": false,
        "edit": false
      }
    }
  }
}
```

[了解更多关于工具的信息](/docs/tools)。

---

### 权限

您可以配置权限来管理代理可以执行的操作。目前，`edit`、`bash` 和 `webfetch` 工具的权限可以配置为：

- `"ask"` — 运行工具前提示审批
- `"allow"` — 允许所有操作，无需审批
- `"deny"` — 禁用该工具

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny"
  }
}
```

您可以按代理覆盖这些权限。

```json title="opencode.json" {3-5,8-10}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny"
  },
  "agent": {
    "build": {
      "permission": {
        "edit": "ask"
      }
    }
  }
}
```

您还可以在 Markdown 代理中设置权限。

```markdown title="~/.config/opencode/agents/review.md"
---
description: Code review without edits
mode: subagent
permission:
  edit: deny
  bash:
    "*": ask
    "git diff": allow
    "git log*": allow
    "grep *": allow
  webfetch: deny
---

Only analyze code and suggest changes.
```

您可以为特定的 bash 命令设置权限。

```json title="opencode.json" {7}
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "git push": "ask",
          "grep *": "allow"
        }
      }
    }
  }
}
```

这可以使用 glob 模式。

```json title="opencode.json" {7}
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "git *": "ask"
        }
      }
    }
  }
}
```

您还可以使用 `*` 通配符来管理所有命令的权限。
由于最后匹配的规则优先，请将 `*` 通配符放在前面，将具体规则放在后面。

```json title="opencode.json" {8}
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "*": "ask",
          "git status *": "allow"
        }
      }
    }
  }
}
```

[了解更多关于权限的信息](/docs/permissions)。

---

### 模式

使用 `mode` 配置控制代理的模式。`mode` 选项用于确定代理的使用方式。

```json title="opencode.json"
{
  "agent": {
    "review": {
      "mode": "subagent"
    }
  }
}
```

`mode` 选项可以设置为 `primary`、`subagent` 或 `all`。如果未指定 `mode`，则默认为 `all`。

---

### 隐藏

使用 `hidden: true` 将子代理从 `@` 自动补全菜单中隐藏。适用于只应由其他代理通过 Task 工具以编程方式调用的内部子代理。

```json title="opencode.json"
{
  "agent": {
    "internal-helper": {
      "mode": "subagent",
      "hidden": true
    }
  }
}
```

这仅影响自动补全菜单中的用户可见性。如果权限允许，模型仍然可以通过 Task 工具调用隐藏的代理。

:::note
仅适用于 `mode: subagent` 的代理。

---

### 任务权限

使用 `permission.task` 控制代理可以通过 Task 工具调用哪些子代理。使用 glob 模式进行灵活匹配。

```json title="opencode.json"
{
  "agent": {
    "orchestrator": {
      "mode": "primary",
      "permission": {
        "task": {
          "*": "deny",
          "orchestrator-*": "allow",
          "code-reviewer": "ask"
        }
      }
    }
  }
}
```

当设置为 `deny` 时，子代理将从 Task 工具描述中完全移除，因此模型不会尝试调用它。

:::tip
规则按顺序评估，**最后匹配的规则优先**。在上面的示例中，`orchestrator-planner` 同时匹配 `*`（deny）和 `orchestrator-*`（allow），但由于 `orchestrator-*` 在 `*` 之后，所以结果为 `allow`。

:::tip
用户始终可以通过 `@` 自动补全菜单直接调用任何子代理，即使代理的任务权限会拒绝它。

---

### 颜色

使用 `color` 选项自定义代理在 UI 中的视觉外观。这会影响代理在界面中的显示方式。

使用有效的十六进制颜色（例如 `#FF5733`）或主题颜色：`primary`、`secondary`、`accent`、`success`、`warning`、`error`、`info`。

```json title="opencode.json"
{
  "agent": {
    "creative": {
      "color": "#ff6b6b"
    },
    "code-reviewer": {
      "color": "accent"
    }
  }
}
```

---

### Top P

使用 `top_p` 选项控制响应多样性。这是控制随机性的温度替代方案。

```json title="opencode.json"
{
  "agent": {
    "brainstorm": {
      "top_p": 0.9
    }
  }
}
```

值范围从 0.0 到 1.0。较低的值更加集中，较高的值更加多样化。

---

### 其他选项

您在代理配置中指定的任何其他选项都将作为模型选项**直接传递**给提供商。这允许您使用提供商特定的功能和参数。

例如，使用 OpenAI 的推理模型时，您可以控制推理力度：

```json title="opencode.json" {6,7}
{
  "agent": {
    "deep-thinker": {
      "description": "Agent that uses high reasoning effort for complex problems",
      "model": "openai/gpt-5",
      "reasoningEffort": "high",
      "textVerbosity": "low"
    }
  }
}
```

这些附加选项是模型和提供商特定的。请查阅您的提供商文档以获取可用参数。

:::tip
运行 `opencode models` 查看可用模型列表。

---

## 创建代理

您可以使用以下命令创建新代理：

```bash
opencode agent create
```

此交互式命令将：

1. 询问代理的保存位置——全局或项目级。
2. 描述代理应该做什么。
3. 生成合适的系统提示词和标识符。
4. 让您选择代理可以访问哪些工具。
5. 最后，创建一个包含代理配置的 Markdown 文件。

---

## 使用场景

以下是不同代理的一些常见使用场景。

- **Build 代理**：启用所有工具的完整开发工作
- **Plan 代理**：分析和规划，不进行任何更改
- **Review 代理**：具有只读访问权限和文档工具的代码审查
- **Debug 代理**：专注于问题排查，启用 bash 和读取工具
- **Docs 代理**：文档编写，具有文件操作但不使用系统命令

---

## 示例

以下是一些您可能会觉得有用的示例代理。

:::tip
您有想要分享的代理吗？[提交 PR](https://github.com/anomalyco/opencode)。

---

### 文档代理

```markdown title="~/.config/opencode/agents/docs-writer.md"
---
description: Writes and maintains project documentation
mode: subagent
tools:
  bash: false
---

You are a technical writer. Create clear, comprehensive documentation.

Focus on:

- Clear explanations
- Proper structure
- Code examples
- User-friendly language
```

---

### 安全审计代理

```markdown title="~/.config/opencode/agents/security-auditor.md"
---
description: Performs security audits and identifies vulnerabilities
mode: subagent
tools:
  write: false
  edit: false
---

You are a security expert. Focus on identifying potential security issues.

Look for:

- Input validation vulnerabilities
- Authentication and authorization flaws
- Data exposure risks
- Dependency vulnerabilities
- Configuration security issues
```

---

## custom-tools

- 官方原文：https://opencode.ai/docs/zh-cn/custom-tools
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-custom-tools.md`

自定义工具是你创建的函数，LLM 可以在对话过程中调用它们。它们与 opencode 的[内置工具](/docs/tools)（如 `read`、`write` 和 `bash`）协同工作。

---

## 创建工具

工具以 **TypeScript** 或 **JavaScript** 文件的形式定义。不过，工具定义可以调用**任何语言**编写的脚本——TypeScript 或 JavaScript 仅用于工具定义本身。

---

### 位置

工具可以在以下位置定义：

- 本地定义：将工具文件放在项目的 `.opencode/tools/` 目录中。
- 全局定义：将工具文件放在 `~/.config/opencode/tools/` 中。

---

### 结构

创建工具最简单的方式是使用 `tool()` 辅助函数，它提供类型安全和参数校验。

```ts title=".opencode/tools/database.ts" {1}

export default tool({
  description: "Query the project database",
  args: {
    query: tool.schema.string().describe("SQL query to execute"),
  },
  async execute(args) {
    // Your database logic here
    return `Executed query: ${args.query}`
  },
})
```

**文件名**即为**工具名称**。上面的示例创建了一个名为 `database` 的工具。

---

#### 单文件多工具

你也可以从单个文件中导出多个工具。每个导出都会成为**一个独立的工具**，命名格式为 **`<filename>_<exportname>`**：

```ts title=".opencode/tools/math.ts"

export const add = tool({
  description: "Add two numbers",
  args: {
    a: tool.schema.number().describe("First number"),
    b: tool.schema.number().describe("Second number"),
  },
  async execute(args) {
    return args.a + args.b
  },
})

export const multiply = tool({
  description: "Multiply two numbers",
  args: {
    a: tool.schema.number().describe("First number"),
    b: tool.schema.number().describe("Second number"),
  },
  async execute(args) {
    return args.a * args.b
  },
})
```

这会创建两个工具：`math_add` 和 `math_multiply`。

---

#### 与内置工具的名称冲突

自定义工具通过工具名称进行索引。如果自定义工具使用了与内置工具相同的名称，则优先使用自定义工具。

例如，这个文件取代了内置的bash工具：

```ts title=".opencode/tools/bash.ts"

export default tool({
  description: "Restricted bash wrapper",
  args: {
    command: tool.schema.string(),
  },
  async execute(args) {
    return `blocked: ${args.command}`
  },
})
```

:::note
除非你有意替换内置工具，否则最好用独特的名字。如果你想禁用内置工具但不想覆盖它，使用 [权限](/docs/permissions).

---

### 参数

你可以使用 `tool.schema`（即 [Zod](https://zod.dev)）来定义参数类型。

```ts "tool.schema"
args: {
  query: tool.schema.string().describe("SQL query to execute")
}
```

你也可以直接导入 [Zod](https://zod.dev) 并返回一个普通对象：

```ts {6}

export default {
  description: "Tool description",
  args: {
    param: z.string().describe("Parameter description"),
  },
  async execute(args, context) {
    // Tool implementation
    return "result"
  },
}
```

---

### 上下文

工具会接收当前会话的上下文信息：

```ts title=".opencode/tools/project.ts" {8}

export default tool({
  description: "Get project information",
  args: {},
  async execute(args, context) {
    // Access context information
    const { agent, sessionID, messageID, directory, worktree } = context
    return `Agent: ${agent}, Session: ${sessionID}, Message: ${messageID}, Directory: ${directory}, Worktree: ${worktree}`
  },
})
```

使用 `context.directory` 获取会话的工作目录。
使用 `context.worktree` 获取 git worktree 根目录。

---

## 示例

### 用 Python 编写工具

你可以使用任何语言编写工具。以下示例展示了如何用 Python 实现两数相加。

首先，创建一个 Python 脚本作为工具：

```python title=".opencode/tools/add.py"
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
```

然后创建调用该脚本的工具定义：

```ts title=".opencode/tools/python-add.ts" {10}

export default tool({
  description: "Add two numbers using Python",
  args: {
    a: tool.schema.number().describe("First number"),
    b: tool.schema.number().describe("Second number"),
  },
  async execute(args, context) {
    const script = path.join(context.worktree, ".opencode/tools/add.py")
    const result = await Bun.$`python3 ${script} ${args.a} ${args.b}`.text()
    return result.trim()
  },
})
```

这里我们使用 [`Bun.$`](https://bun.com/docs/runtime/shell) 工具函数来运行 Python 脚本。

---

## lsp

- 官方原文：https://opencode.ai/docs/zh-cn/lsp
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-lsp.md`

OpenCode 可以与语言服务器协议（LSP）服务器集成，将诊断信息作为 agent 的反馈。

---

## 内置支持

OpenCode 内置了多种适用于主流语言的 LSP 服务器：

| LSP 服务器         | 扩展名                                                              | 要求                                                  |
| ------------------ | ------------------------------------------------------------------- | ----------------------------------------------------- |
| astro              | .astro                                                              | 为 Astro 项目自动安装                                 |
| bash               | .sh, .bash, .zsh, .ksh                                              | 自动安装 bash-language-server                         |
| clangd             | .c, .cpp, .cc, .cxx, .c++, .h, .hpp, .hh, .hxx, .h++                | 为 C/C++ 项目自动安装                                 |
| csharp             | .cs                                                                 | 需要已安装 `.NET SDK`                                 |
| clojure-lsp        | .clj, .cljs, .cljc, .edn                                            | 需要 `clojure-lsp` 命令可用                           |
| dart               | .dart                                                               | 需要 `dart` 命令可用                                  |
| deno               | .ts, .tsx, .js, .jsx, .mjs                                          | 需要 `deno` 命令可用（自动检测 deno.json/deno.jsonc） |
| elixir-ls          | .ex, .exs                                                           | 需要 `elixir` 命令可用                                |
| eslint             | .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts, .vue                  | 项目中需要 `eslint` 依赖                              |
| fsharp             | .fs, .fsi, .fsx, .fsscript                                          | 需要已安装 `.NET SDK`                                 |
| gleam              | .gleam                                                              | 需要 `gleam` 命令可用                                 |
| gopls              | .go                                                                 | 需要 `go` 命令可用                                    |
| hls                | .hs, .lhs                                                           | 需要 `haskell-language-server-wrapper` 命令可用       |
| jdtls              | .java                                                               | 需要已安装 `Java SDK (version 21+)`                   |
| julials            | .jl                                                                 | 需要安装 `julia` and `LanguageServer.jl`              |
| kotlin-ls          | .kt, .kts                                                           | 为 Kotlin 项目自动安装                                |
| lua-ls             | .lua                                                                | 为 Lua 项目自动安装                                   |
| nixd               | .nix                                                                | 需要 `nixd` 命令可用                                  |
| ocaml-lsp          | .ml, .mli                                                           | 需要 `ocamllsp` 命令可用                              |
| oxlint             | .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts, .vue, .astro, .svelte | 项目中需要 `oxlint` 依赖                              |
| php intelephense   | .php                                                                | 为 PHP 项目自动安装                                   |
| prisma             | .prisma                                                             | 需要 `prisma` 命令可用                                |
| pyright            | .py, .pyi                                                           | 需要已安装 `pyright` 依赖                             |
| ruby-lsp (rubocop) | .rb, .rake, .gemspec, .ru                                           | 需要 `ruby` 和 `gem` 命令可用                         |
| rust               | .rs                                                                 | 需要 `rust-analyzer` 命令可用                         |
| sourcekit-lsp      | .swift, .objc, .objcpp                                              | 需要已安装 `swift`（macOS 上为 `xcode`）              |
| svelte             | .svelte                                                             | 为 Svelte 项目自动安装                                |
| terraform          | .tf, .tfvars                                                        | 从 GitHub releases 自动安装                           |
| tinymist           | .typ, .typc                                                         | 从 GitHub releases 自动安装                           |
| typescript         | .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts                        | 项目中需要 `typescript` 依赖                          |
| vue                | .vue                                                                | 为 Vue 项目自动安装                                   |
| yaml-ls            | .yaml, .yml                                                         | 自动安装 Red Hat yaml-language-server                 |
| zls                | .zig, .zon                                                          | 需要 `zig` 命令可用                                   |

LSP 默认关闭。启用后，当检测到上述文件扩展名且满足相应要求时，服务器会启动。

:::note
你可以将 `OPENCODE_DISABLE_LSP_DOWNLOAD` 环境变量设置为 `true` 来禁用 LSP 服务器的自动下载。

---

## 工作原理

启用 LSP 且 opencode 打开文件时，它会：

1. 将文件扩展名与所有已启用的 LSP 服务器进行匹配。
2. 如果对应的 LSP 服务器尚未运行，则自动启动它。

---

## 最佳实践

LSP 可以通过语言服务器诊断帮助 agent 发现并修复问题。这对某些项目很有用，但并不总是带来净收益。

语言服务器可能与项目不同步、占用较多内存、随版本或项目表现不同，并拖慢 agent 工作流。在许多项目中，更好的做法是让 agent 直接运行 lint、typecheck 或其他诊断类 CLI 工具，这样错误会进入 agent 循环，同时避免这些权衡。将这些命令记录在 `AGENTS.md` 或 skills 等指令文件中，让 agent 知道该运行什么。当你的项目能从额外的语言服务器反馈中受益时再启用 LSP。

---

## 配置

你可以通过 opencode 配置文件中的 `lsp` 部分来启用并自定义 LSP 服务器。

要启用所有内置 LSP 服务器，请将 `lsp` 设置为 `true`。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": true
}
```

使用对象可以在保持内置服务器启用的同时配置覆盖项或自定义服务器。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {}
}
```

每个 LSP 服务器支持以下配置项：

| 属性             | 类型     | 描述                              |
| ---------------- | -------- | --------------------------------- |
| `disabled`       | boolean  | 设置为 `true` 可禁用该 LSP 服务器 |
| `command`        | string[] | 启动 LSP 服务器的命令             |
| `extensions`     | string[] | 该 LSP 服务器需要处理的文件扩展名 |
| `env`            | object   | 启动服务器时设置的环境变量        |
| `initialization` | object   | 发送给 LSP 服务器的初始化选项     |

下面来看一些示例。

---

### 环境变量

使用 `env` 属性在启动 LSP 服务器时设置环境变量：

```json title="opencode.json" {5-7}
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {
    "rust": {
      "env": {
        "RUST_LOG": "debug"
      }
    }
  }
}
```

---

### 初始化选项

使用 `initialization` 属性向 LSP 服务器传递初始化选项。这些是在 LSP `initialize` 请求期间发送的服务器特定设置：

```json title="opencode.json" {5-9}
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {
    "typescript": {
      "initialization": {
        "preferences": {
          "importModuleSpecifierPreference": "relative"
        }
      }
    }
  }
}
```

:::note
初始化选项因 LSP 服务器而异。请查阅你所使用的 LSP 服务器的文档以了解可用选项。

---

### 禁用 LSP 服务器

如果省略 `lsp`，所有 LSP 服务器都会被禁用。如果另一个配置启用了 LSP，可将 `lsp` 设置为 `false` 来禁用所有 LSP 服务器：

```json title="opencode.json" {3}
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": false
}
```

要禁用**特定的** LSP 服务器，将 `disabled` 设置为 `true`：

```json title="opencode.json" {5}
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {
    "typescript": {
      "disabled": true
    }
  }
}
```

---

### 自定义 LSP 服务器

你可以通过指定命令和文件扩展名来添加自定义 LSP 服务器：

```json title="opencode.json" {4-7}
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": {
    "custom-lsp": {
      "command": ["custom-lsp-server", "--stdio"],
      "extensions": [".custom"]
    }
  }
}
```

---

## 补充信息

### PHP Intelephense

PHP Intelephense 通过许可证密钥提供高级功能。你可以将许可证密钥单独放在以下路径的文本文件中：

- macOS/Linux：`$HOME/intelephense/license.txt`
- Windows：`%USERPROFILE%/intelephense/license.txt`

该文件应仅包含许可证密钥，不要添加其他任何内容。

---

## 查看所有支持 OAuth 的服务器的认证状态

- 官方原文：https://opencode.ai/docs/zh-cn/mcp-servers
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-mcp-servers.md`

你可以通过 _Model Context Protocol_（MCP）为 OpenCode 添加外部工具。OpenCode 同时支持本地和远程服务器。

添加后，MCP 工具会自动与内置工具一起提供给 LLM 使用。

---

#### 注意事项

使用 MCP 服务器时，它会占用上下文空间。如果你启用了大量工具，上下文消耗会迅速增加。因此，我们建议谨慎选择要使用的 MCP 服务器。

:::tip
MCP 服务器会占用你的上下文空间，所以请谨慎选择启用哪些服务器。

某些 MCP 服务器（例如 GitHub MCP 服务器）往往会消耗大量 Token，很容易超出上下文限制。

---

## 启用

你可以在 [OpenCode 配置](https://opencode.ai/docs/config/)的 `mcp` 字段下定义 MCP 服务器。为每个 MCP 指定一个唯一的名称，在提示词中可以通过该名称来引用对应的 MCP。

```jsonc title="opencode.jsonc" {6}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "name-of-mcp-server": {
      // ...
      "enabled": true,
    },
    "name-of-other-mcp-server": {
      // ...
    },
  },
}
```

你也可以将 `enabled` 设置为 `false` 来禁用某个服务器。当你想临时禁用某个服务器而不将其从配置中移除时，这个选项非常有用。

---

### 覆盖远程默认值

组织可以通过其 `.well-known/opencode` 端点提供默认的 MCP 服务器。这些服务器可能默认处于禁用状态，允许用户按需启用。

要启用组织远程配置中的某个服务器，请在本地配置中添加该服务器并设置 `enabled: true`：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "jira": {
      "type": "remote",
      "url": "https://jira.example.com/mcp",
      "enabled": true
    }
  }
}
```

本地配置值会覆盖远程默认值。详情请参阅[配置优先级](/docs/config#precedence-order)。

---

## 本地

通过在 MCP 对象中将 `type` 设置为 `"local"` 来添加本地 MCP 服务器。

```jsonc title="opencode.jsonc" {15}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-local-mcp-server": {
      "type": "local",
      // Or ["bun", "x", "my-mcp-command"]
      "command": ["npx", "-y", "my-mcp-command"],
      "enabled": true,
      "environment": {
        "MY_ENV_VAR": "my_env_var_value",
      },
    },
  },
}
```

`command` 用于指定本地 MCP 服务器的启动命令。你还可以传入一组环境变量。

例如，以下是添加测试用的 [`@modelcontextprotocol/server-everything`](https://www.npmjs.com/package/@modelcontextprotocol/server-everything) MCP 服务器的方法。

```jsonc title="opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "mcp_everything": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-everything"],
    },
  },
}
```

要使用它，可以在提示词中添加 `use the mcp_everything tool`。

```txt "mcp_everything"
use the mcp_everything tool to add the number 3 and 4
```

---

#### 选项

以下是配置本地 MCP 服务器的所有选项。

| 选项          | 类型   | 必填 | 描述                                                              |
| ------------- | ------ | ---- | ----------------------------------------------------------------- |
| `type`        | 字符串 | 是   | MCP 服务器连接类型，必须为 `"local"`。                            |
| `command`     | 数组   | 是   | 运行 MCP 服务器的命令及参数。                                     |
| `environment` | 对象   |      | 运行服务器时设置的环境变量。                                      |
| `enabled`     | 布尔值 |      | 启动时启用或禁用该 MCP 服务器。                                   |
| `timeout`     | 数字   |      | 从 MCP 服务器获取工具的超时时间（毫秒）。默认为 5000（即 5 秒）。 |

---

## 远程

通过将 `type` 设置为 `"remote"` 来添加远程 MCP 服务器。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-remote-mcp": {
      "type": "remote",
      "url": "https://my-mcp-server.com",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer MY_API_KEY"
      }
    }
  }
}
```

`url` 是远程 MCP 服务器的地址，通过 `headers` 选项可以传入一组请求头。

---

#### 选项

| 选项      | 类型   | 必填 | 描述                                                              |
| --------- | ------ | ---- | ----------------------------------------------------------------- |
| `type`    | 字符串 | 是   | MCP 服务器连接类型，必须为 `"remote"`。                           |
| `url`     | 字符串 | 是   | 远程 MCP 服务器的 URL。                                           |
| `enabled` | 布尔值 |      | 启动时启用或禁用该 MCP 服务器。                                   |
| `headers` | 对象   |      | 随请求发送的请求头。                                              |
| `oauth`   | 对象   |      | OAuth 身份验证配置。详见下方 [OAuth](#oauth) 部分。               |
| `timeout` | 数字   |      | 从 MCP 服务器获取工具的超时时间（毫秒）。默认为 5000（即 5 秒）。 |

---

## OAuth

OpenCode 会自动处理远程 MCP 服务器的 OAuth 身份验证。当服务器需要身份验证时，OpenCode 将：

1. 检测 401 响应并启动 OAuth 流程
2. 在服务器支持的情况下使用**动态客户端注册（RFC 7591）**
3. 安全地存储 Token 以供后续请求使用

---

### 自动认证

对于大多数支持 OAuth 的 MCP 服务器，无需特殊配置。只需配置远程服务器即可：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-oauth-server": {
      "type": "remote",
      "url": "https://mcp.example.com/mcp"
    }
  }
}
```

如果服务器需要身份验证，OpenCode 会在你首次使用时提示你进行认证。你也可以使用 `opencode mcp auth <server-name>` [手动触发认证流程](#authenticating)。

---

### 预注册

如果你已经从 MCP 服务器提供商处获得了客户端凭据，可以直接配置：

```json title="opencode.json" {7-11}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-oauth-server": {
      "type": "remote",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "{env:MY_MCP_CLIENT_ID}",
        "clientSecret": "{env:MY_MCP_CLIENT_SECRET}",
        "scope": "tools:read tools:execute"
      }
    }
  }
}
```

---

### 身份验证

你可以手动触发身份验证或管理凭据。

对特定 MCP 服务器进行身份验证：

```bash
opencode mcp auth my-oauth-server
```

列出所有 MCP 服务器及其认证状态：

```bash
opencode mcp list
```

删除已存储的凭据：

```bash
opencode mcp logout my-oauth-server
```

`mcp auth` 命令会打开浏览器进行授权。授权完成后，OpenCode 会将 Token 安全地存储在 `~/.local/share/opencode/mcp-auth.json` 中。

---

#### 禁用 OAuth

如果你想为某个服务器禁用自动 OAuth（例如，该服务器使用 API 密钥而非 OAuth），可以将 `oauth` 设置为 `false`：

```json title="opencode.json" {7}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-api-key-server": {
      "type": "remote",
      "url": "https://mcp.example.com/mcp",
      "oauth": false,
      "headers": {
        "Authorization": "Bearer {env:MY_API_KEY}"
      }
    }
  }
}
```

---

#### OAuth 选项

| 选项           | 类型            | 描述                                                   |
| -------------- | --------------- | ------------------------------------------------------ |
| `oauth`        | 对象 \| `false` | OAuth 配置对象，或设为 `false` 以禁用 OAuth 自动检测。 |
| `clientId`     | 字符串          | OAuth 客户端 ID。如果未提供，将尝试动态客户端注册。    |
| `clientSecret` | 字符串          | OAuth 客户端密钥（如果授权服务器要求提供）。           |
| `scope`        | 字符串          | 授权时请求的 OAuth 作用域。                            |

#### 调试

如果远程 MCP 服务器身份验证失败，你可以通过以下方式诊断问题：

```bash
# 查看所有支持 OAuth 的服务器的认证状态
opencode mcp auth list

# 调试特定服务器的连接和 OAuth 流程
opencode mcp debug my-oauth-server
```

`mcp debug` 命令会显示当前认证状态、测试 HTTP 连接，并尝试执行 OAuth 发现流程。

---

## 管理

你的 MCP 在 OpenCode 中作为工具使用，与内置工具并列。因此，你可以像管理其他工具一样，通过 OpenCode 配置来管理它们。

---

### 全局

你可以全局启用或禁用 MCP 工具。

```json title="opencode.json" {14}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-mcp-foo": {
      "type": "local",
      "command": ["bun", "x", "my-mcp-command-foo"]
    },
    "my-mcp-bar": {
      "type": "local",
      "command": ["bun", "x", "my-mcp-command-bar"]
    }
  },
  "tools": {
    "my-mcp-foo": false
  }
}
```

也可以使用 glob 模式来禁用所有匹配的 MCP。

```json title="opencode.json" {14}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-mcp-foo": {
      "type": "local",
      "command": ["bun", "x", "my-mcp-command-foo"]
    },
    "my-mcp-bar": {
      "type": "local",
      "command": ["bun", "x", "my-mcp-command-bar"]
    }
  },
  "tools": {
    "my-mcp*": false
  }
}
```

这里使用 glob 模式 `my-mcp*` 来禁用所有 MCP。

---

### 按代理配置

如果你有大量 MCP 服务器，可以选择全局禁用它们，然后仅在特定代理中启用。具体做法：

1. 全局禁用该工具。
2. 在[代理配置](/docs/agents#tools)中，将 MCP 服务器作为工具启用。

```json title="opencode.json" {11, 14-18}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-mcp": {
      "type": "local",
      "command": ["bun", "x", "my-mcp-command"],
      "enabled": true
    }
  },
  "tools": {
    "my-mcp*": false
  },
  "agent": {
    "my-agent": {
      "tools": {
        "my-mcp*": true
      }
    }
  }
}
```

---

#### Glob 模式

glob 模式使用简单的正则通配符规则：

- `*` 匹配零个或多个任意字符（例如，`"my-mcp*"` 匹配 `my-mcp_search`、`my-mcp_list` 等）
- `?` 匹配恰好一个字符
- 其他字符按字面值匹配

:::note
MCP 服务器工具在注册时以服务器名称作为前缀，因此要禁用某个服务器的所有工具，只需使用：

```
"mymcpservername_*": false
```

---

## 示例

以下是一些常见 MCP 服务器的配置示例。如果你想记录其他服务器的用法，欢迎提交 PR。

---

### Sentry

添加 [Sentry MCP 服务器](https://mcp.sentry.dev) 以与你的 Sentry 项目和问题进行交互。

```json title="opencode.json" {4-8}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "sentry": {
      "type": "remote",
      "url": "https://mcp.sentry.dev/mcp",
      "oauth": {}
    }
  }
}
```

添加配置后，使用 Sentry 进行身份验证：

```bash
opencode mcp auth sentry
```

这会打开浏览器窗口完成 OAuth 流程，将 OpenCode 连接到你的 Sentry 账户。

认证完成后，你可以在提示词中使用 Sentry 工具来查询问题、项目和错误数据。

```txt "use sentry"
Show me the latest unresolved issues in my project. use sentry
```

---

### Context7

添加 [Context7 MCP 服务器](https://github.com/upstash/context7) 以搜索文档。

```json title="opencode.json" {4-7}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp"
    }
  }
}
```

如果你注册了免费账户，可以使用 API 密钥来获得更高的速率限制。

```json title="opencode.json" {7-9}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"
      }
    }
  }
}
```

这里假设你已经设置了 `CONTEXT7_API_KEY` 环境变量。

在提示词中添加 `use context7` 即可使用 Context7 MCP 服务器。

```txt "use context7"
Configure a Cloudflare Worker script to cache JSON API responses for five minutes. use context7
```

你也可以在 [AGENTS.md](/docs/rules/) 中添加类似的规则。

```md title="AGENTS.md"
When you need to search docs, use `context7` tools.
```

---

### Grep by Vercel

添加 [Grep by Vercel](https://grep.app) MCP 服务器以搜索 GitHub 上的代码片段。

```json title="opencode.json" {4-7}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "gh_grep": {
      "type": "remote",
      "url": "https://mcp.grep.app"
    }
  }
}
```

由于我们将 MCP 服务器命名为 `gh_grep`，你可以在提示词中添加 `use the gh_grep tool` 来让代理使用它。

```txt "use the gh_grep tool"
What's the right way to set a custom domain in an SST Astro component? use the gh_grep tool
```

你也可以在 [AGENTS.md](/docs/rules/) 中添加类似的规则。

```md title="AGENTS.md"
If you are unsure how to do something, use `gh_grep` to search code examples from GitHub.
```

---

## plugins

- 官方原文：https://opencode.ai/docs/zh-cn/plugins
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-plugins.md`

插件允许你通过挂钩各种事件和自定义行为来扩展 OpenCode。你可以创建插件来添加新功能、集成外部服务，或修改 OpenCode 的默认行为。

如需了解示例，请查看社区创建的[插件](/docs/ecosystem#plugins)。

---

## 使用插件

有两种方式加载插件。

---

### 从本地文件加载

将 JavaScript 或 TypeScript 文件放置在插件目录中。

- `.opencode/plugins/` - 项目级插件
- `~/.config/opencode/plugins/` - 全局插件

这些目录中的文件会在启动时自动加载。

---

### 从 npm 加载

在配置文件中指定 npm 包。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-helicone-session", "opencode-wakatime", "@my-org/custom-plugin"]
}
```

支持常规和带作用域的 npm 包。

浏览[生态系统](/docs/ecosystem#plugins)中的可用插件。

---

### 插件的安装方式

**npm 插件**在启动时使用 Bun 自动安装。包及其依赖项会缓存在 `~/.cache/opencode/node_modules/` 中。

**本地插件**直接从插件目录加载。如果需要使用外部包，你必须在配置目录中创建 `package.json`（参见[依赖项](#dependencies)），或者将插件发布到 npm 并[将其添加到配置中](/docs/config#plugins)。

---

### 加载顺序

插件从所有来源加载，所有钩子按顺序执行。加载顺序为：

1. 全局配置 (`~/.config/opencode/opencode.json`)
2. 项目配置 (`opencode.json`)
3. 全局插件目录 (`~/.config/opencode/plugins/`)
4. 项目插件目录 (`.opencode/plugins/`)

名称和版本相同的重复 npm 包只会加载一次。但本地插件和名称相似的 npm 插件会分别独立加载。

---

## 创建插件

插件是一个 **JavaScript/TypeScript 模块**，它导出一个或多个插件函数。每个函数接收一个上下文对象，并返回一个钩子对象。

---

### 依赖项

本地插件和自定义工具可以使用外部 npm 包。在配置目录中添加一个 `package.json`，列出所需的依赖项。

```json title=".opencode/package.json"
{
  "dependencies": {
    "shescape": "^2.1.0"
  }
}
```

OpenCode 会在启动时运行 `bun install` 来安装这些依赖项。之后你的插件和工具就可以导入它们了。

```ts title=".opencode/plugins/my-plugin.ts"

export const MyPlugin = async (ctx) => {
  return {
    "tool.execute.before": async (input, output) => {
      if (input.tool === "bash") {
        output.args.command = escape(output.args.command)
      }
    },
  }
}
```

---

### 基本结构

```js title=".opencode/plugins/example.js"
export const MyPlugin = async ({ project, client, $, directory, worktree }) => {
  console.log("Plugin initialized!")

  return {
    // Hook implementations go here
  }
}
```

插件函数接收以下参数：

- `project`：当前项目信息。
- `directory`：当前工作目录。
- `worktree`：git 工作树路径。
- `client`：用于与 AI 交互的 OpenCode SDK 客户端。
- `$`：Bun 的 [Shell API](https://bun.com/docs/runtime/shell)，用于执行命令。

---

### TypeScript 支持

对于 TypeScript 插件，你可以从插件包中导入类型：

```ts title="my-plugin.ts" {1}

export const MyPlugin: Plugin = async ({ project, client, $, directory, worktree }) => {
  return {
    // Type-safe hook implementations
  }
}
```

---

### 事件

插件可以订阅事件，如下方示例部分所示。以下是所有可用事件的列表。

#### 命令事件

- `command.executed`

#### 文件事件

- `file.edited`
- `file.watcher.updated`

#### 安装事件

- `installation.updated`

#### LSP 事件

- `lsp.client.diagnostics`
- `lsp.updated`

#### 消息事件

- `message.part.removed`
- `message.part.updated`
- `message.removed`
- `message.updated`

#### 权限事件

- `permission.asked`
- `permission.replied`

#### 服务器事件

- `server.connected`

#### 会话事件

- `session.created`
- `session.compacted`
- `session.deleted`
- `session.diff`
- `session.error`
- `session.idle`
- `session.status`
- `session.updated`

#### 待办事项事件

- `todo.updated`

#### Shell 事件

- `shell.env`

#### 工具事件

- `tool.execute.after`
- `tool.execute.before`

#### TUI 事件

- `tui.prompt.append`
- `tui.command.execute`
- `tui.toast.show`

---

## 示例

以下是一些可用于扩展 OpenCode 的插件示例。

---

### 发送通知

在特定事件发生时发送通知：

```js title=".opencode/plugins/notification.js"
export const NotificationPlugin = async ({ project, client, $, directory, worktree }) => {
  return {
    event: async ({ event }) => {
      // Send notification on session completion
      if (event.type === "session.idle") {
        await $`osascript -e 'display notification "Session completed!" with title "opencode"'`
      }
    },
  }
}
```

这里使用 `osascript` 在 macOS 上运行 AppleScript 来发送通知。

:::note
如果你使用 OpenCode 桌面应用，它可以在响应就绪或会话出错时自动发送系统通知。

---

### .env 保护

阻止 OpenCode 读取 `.env` 文件：

```javascript title=".opencode/plugins/env-protection.js"
export const EnvProtection = async ({ project, client, $, directory, worktree }) => {
  return {
    "tool.execute.before": async (input, output) => {
      if (input.tool === "read" && output.args.filePath.includes(".env")) {
        throw new Error("Do not read .env files")
      }
    },
  }
}
```

---

### 注入环境变量

将环境变量注入所有 Shell 执行（AI 工具和用户终端）：

```javascript title=".opencode/plugins/inject-env.js"
export const InjectEnvPlugin = async () => {
  return {
    "shell.env": async (input, output) => {
      output.env.MY_API_KEY = "secret"
      output.env.PROJECT_ROOT = input.cwd
    },
  }
}
```

---

### 自定义工具

插件还可以为 OpenCode 添加自定义工具：

```ts title=".opencode/plugins/custom-tools.ts"

export const CustomToolsPlugin: Plugin = async (ctx) => {
  return {
    tool: {
      mytool: tool({
        description: "This is a custom tool",
        args: {
          foo: tool.schema.string(),
        },
        async execute(args, context) {
          const { directory, worktree } = context
          return `Hello ${args.foo} from ${directory} (worktree: ${worktree})`
        },
      }),
    },
  }
}
```

`tool` 辅助函数用于创建 OpenCode 可调用的自定义工具。它接受一个 Zod schema 函数，并返回一个工具定义，包含：

- `description`：工具的功能描述
- `args`：工具参数的 Zod schema
- `execute`：工具被调用时执行的函数

你的自定义工具将与内置工具一起在 OpenCode 中可用。

:::note
如果插件工具与内置工具使用相同的名称，则优先使用插件工具。

---

### 日志记录

使用 `client.app.log()` 代替 `console.log` 进行结构化日志记录：

```ts title=".opencode/plugins/my-plugin.ts"
export const MyPlugin = async ({ client }) => {
  await client.app.log({
    body: {
      service: "my-plugin",
      level: "info",
      message: "Plugin initialized",
      extra: { foo: "bar" },
    },
  })
}
```

日志级别：`debug`、`info`、`warn`、`error`。详情请参阅 [SDK 文档](https://opencode.ai/docs/sdk)。

---

### 压缩钩子

自定义会话压缩时包含的上下文：

```ts title=".opencode/plugins/compaction.ts"

export const CompactionPlugin: Plugin = async (ctx) => {
  return {
    "experimental.session.compacting": async (input, output) => {
      // Inject additional context into the compaction prompt
      output.context.push(`
## Custom Context

Include any state that should persist across compaction:
- Current task status
- Important decisions made
- Files being actively worked on
`)
    },
  }
}
```

`experimental.session.compacting` 钩子在 LLM 生成续接摘要之前触发。使用它来注入默认压缩提示词可能遗漏的领域特定上下文。

你还可以通过设置 `output.prompt` 来完全替换压缩提示词：

```ts title=".opencode/plugins/custom-compaction.ts"

export const CustomCompactionPlugin: Plugin = async (ctx) => {
  return {
    "experimental.session.compacting": async (input, output) => {
      // Replace the entire compaction prompt
      output.prompt = `
You are generating a continuation prompt for a multi-agent swarm session.

Summarize:
1. The current task and its status
2. Which files are being modified and by whom
3. Any blockers or dependencies between agents
4. The next steps to complete the work

Format as a structured prompt that a new agent can use to resume work.
`
    },
  }
}
```

当设置了 `output.prompt` 时，它会完全替换默认的压缩提示词。在这种情况下，`output.context` 数组将被忽略。

---

## skills

- 官方原文：https://opencode.ai/docs/zh-cn/skills
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-skills.md`

代理技能让 OpenCode 能够从你的仓库或主目录中发现可复用的指令。
技能通过原生的 `skill` 工具按需加载——代理可以查看可用技能，并在需要时加载完整内容。

---

## 放置文件

为每个技能名称创建一个文件夹，并在其中放入 `SKILL.md`。
OpenCode 会搜索以下位置：

- 项目配置：`.opencode/skills/<name>/SKILL.md`
- 全局配置：`~/.config/opencode/skills/<name>/SKILL.md`
- 项目 Claude 兼容：`.claude/skills/<name>/SKILL.md`
- 全局 Claude 兼容：`~/.claude/skills/<name>/SKILL.md`
- 项目代理兼容：`.agents/skills/<name>/SKILL.md`
- 全局代理兼容：`~/.agents/skills/<name>/SKILL.md`

---

## 了解发现机制

对于项目本地路径，OpenCode 会从当前工作目录向上遍历，直到到达 git 工作树根目录。
在此过程中，它会加载 `.opencode/` 中所有匹配的 `skills/*/SKILL.md`，以及匹配的 `.claude/skills/*/SKILL.md` 或 `.agents/skills/*/SKILL.md`。

全局定义也会从 `~/.config/opencode/skills/*/SKILL.md`、`~/.claude/skills/*/SKILL.md` 和 `~/.agents/skills/*/SKILL.md` 中加载。

---

## 编写 frontmatter

每个 `SKILL.md` 必须以 YAML frontmatter 开头。
仅识别以下字段：

- `name`（必填）
- `description`（必填）
- `license`（可选）
- `compatibility`（可选）
- `metadata`（可选，字符串到字符串的映射）

未知的 frontmatter 字段会被忽略。

---

## 验证名称

`name` 必须满足：

- 长度为 1–64 个字符
- 仅包含小写字母和数字，可用单个连字符分隔
- 不以 `-` 开头或结尾
- 不包含连续的 `--`
- 与包含 `SKILL.md` 的目录名称一致

等效的正则表达式：

```text
^[a-z0-9]+(-[a-z0-9]+)*$
```

---

## 遵循长度规则

`description` 必须为 1-1024 个字符。
请保持描述足够具体，以便代理能够正确选择。

---

## 使用示例

创建 `.opencode/skills/git-release/SKILL.md`，内容如下：

```markdown
---
name: git-release
description: Create consistent releases and changelogs
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: github
---

## What I do

- Draft release notes from merged PRs
- Propose a version bump
- Provide a copy-pasteable `gh release create` command

## When to use me

Use this when you are preparing a tagged release.
Ask clarifying questions if the target versioning scheme is unclear.
```

---

## 识别工具描述

OpenCode 会在 `skill` 工具描述中列出可用技能。
每个条目包含技能名称和描述：

```xml
<available_skills>
  <skill>
    <name>git-release</name>
    <description>Create consistent releases and changelogs</description>
  </skill>
</available_skills>
```

代理通过调用工具来加载技能：

```
skill({ name: "git-release" })
```

---

## 配置权限

在 `opencode.json` 中使用基于模式的权限来控制代理可以访问哪些技能：

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "pr-review": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

| 权限    | 行为                     |
| ------- | ------------------------ |
| `allow` | 技能立即加载             |
| `deny`  | 对代理隐藏技能，拒绝访问 |
| `ask`   | 加载前提示用户确认       |

模式支持通配符：`internal-*` 可匹配 `internal-docs`、`internal-tools` 等。

---

## 按代理覆盖权限

为特定代理授予与全局默认值不同的权限。

**自定义代理**（在代理 frontmatter 中）：

```yaml
---
permission:
  skill:
    "documents-*": "allow"
---
```

**内置代理**（在 `opencode.json` 中）：

```json
{
  "agent": {
    "plan": {
      "permission": {
        "skill": {
          "internal-*": "allow"
        }
      }
    }
  }
}
```

---

## 禁用技能工具

为不需要使用技能的代理完全禁用技能功能：

**自定义代理**：

```yaml
---
tools:
  skill: false
---
```

**内置代理**：

```json
{
  "agent": {
    "plan": {
      "tools": {
        "skill": false
      }
    }
  }
}
```

禁用后，`<available_skills>` 部分将被完全省略。

---

## 排查加载问题

如果某个技能没有显示：

1. 确认 `SKILL.md` 文件名全部为大写字母
2. 检查 frontmatter 是否包含 `name` 和 `description`
3. 确保技能名称在所有位置中唯一
4. 检查权限设置——设为 `deny` 的技能会对代理隐藏

---

## tools

- 官方原文：https://opencode.ai/docs/zh-cn/tools
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-tools.md`

工具允许 LLM 在您的代码库中执行操作。OpenCode 自带一组内置工具，您也可以通过[自定义工具](/docs/custom-tools)或 [MCP 服务器](/docs/mcp-servers)来扩展它。

默认情况下，所有工具都是**启用**的，且无需权限即可运行。您可以通过[权限](/docs/permissions)来控制工具的行为。

---

## 配置

使用 `permission` 字段来控制工具行为。您可以对每个工具设置允许、拒绝或需要审批。

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny",
    "bash": "ask",
    "webfetch": "allow"
  }
}
```

您还可以使用通配符同时控制多个工具。例如，要求某个 MCP 服务器的所有工具都需要审批：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "mymcp_*": "ask"
  }
}
```

[了解更多](/docs/permissions)关于配置权限的内容。

---

## 内置工具

以下是 OpenCode 中所有可用的内置工具。

---

### bash

在项目环境中执行 shell 命令。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": "allow"
  }
}
```

该工具允许 LLM 运行终端命令，例如 `npm install`、`git status` 或其他任何 shell 命令。

---

### edit

通过精确的字符串替换来修改现有文件。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "allow"
  }
}
```

该工具通过替换精确匹配的文本来对文件进行编辑。这是 LLM 修改代码的主要方式。

---

### write

创建新文件或覆盖现有文件。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "allow"
  }
}
```

使用此工具允许 LLM 创建新文件。如果文件已存在，则会覆盖现有文件。

:::note
`write` 工具由 `edit` 权限控制，该权限涵盖所有文件修改操作（`edit`、`write`、`patch`）。

---

### read

读取代码库中的文件内容。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "read": "allow"
  }
}
```

该工具读取文件并返回其内容。它支持对大文件读取指定行范围。

---

### grep

使用正则表达式搜索文件内容。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "grep": "allow"
  }
}
```

在代码库中快速搜索内容。支持完整的正则表达式语法和文件模式过滤。

---

### glob

通过模式匹配查找文件。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "glob": "allow"
  }
}
```

使用 `**/*.js` 或 `src/**/*.ts` 等 glob 模式搜索文件。返回按修改时间排序的匹配文件路径。

---

### lsp（实验性）

与已配置的 LSP 服务器交互，获取代码智能功能，如定义跳转、引用查找、悬停信息和调用层次结构。

:::note
该工具仅在设置 `OPENCODE_EXPERIMENTAL_LSP_TOOL=true`（或 `OPENCODE_EXPERIMENTAL=true`）时可用。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "lsp": "allow"
  }
}
```

支持的操作包括 `goToDefinition`、`findReferences`、`hover`、`documentSymbol`、`workspaceSymbol`、`goToImplementation`、`prepareCallHierarchy`、`incomingCalls` 和 `outgoingCalls`。

要配置项目可用的 LSP 服务器，请参阅 [LSP 服务器](/docs/lsp)。

---

### patch

对文件应用补丁。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "allow"
  }
}
```

该工具将补丁文件应用到您的代码库中。适用于应用来自各种来源的 diff 和补丁。

:::note
`patch` 工具由 `edit` 权限控制，该权限涵盖所有文件修改操作（`edit`、`write`、`patch`）。

---

### skill

加载一个[技能](/docs/skills)（即 `SKILL.md` 文件）并在对话中返回其内容。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "skill": "allow"
  }
}
```

---

### todowrite

在编码会话中管理待办事项列表。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "todowrite": "allow"
  }
}
```

创建和更新任务列表以跟踪复杂操作的进度。LLM 使用此工具来组织多步骤任务。

:::note
该工具默认对子代理禁用，但您可以手动启用。[了解更多](/docs/agents/#permissions)

---

### webfetch

获取网页内容。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "webfetch": "allow"
  }
}
```

允许 LLM 获取并读取网页内容。适用于查阅文档或研究在线资源。

---

### websearch

在网络上搜索信息。

:::note
该工具仅在使用 OpenCode 提供商时，或当 `OPENCODE_ENABLE_EXA` 环境变量设置为任意真值（例如 `true` 或 `1`）时可用。

在启动 OpenCode 时启用：

```bash
OPENCODE_ENABLE_EXA=1 opencode
```

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "websearch": "allow"
  }
}
```

使用 Exa AI 进行网络搜索以查找相关信息。适用于研究主题、了解时事动态或获取超出训练数据截止日期的信息。

无需 API 密钥——该工具无需身份验证即可直接连接到 Exa AI 的托管 MCP 服务。

:::tip
当您需要查找信息（发现）时使用 `websearch`，当您需要从特定 URL 获取内容（检索）时使用 `webfetch`。

---

### question

在执行过程中向用户提问。

```json title="opencode.json" {4}
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "question": "allow"
  }
}
```

该工具允许 LLM 在执行任务期间向用户提问。适用于以下场景：

- 收集用户偏好或需求
- 澄清模糊的指令
- 获取实现方案的决策
- 提供方向选择的选项

每个问题包含标题、问题正文和选项列表。用户可以从提供的选项中选择，也可以输入自定义答案。当有多个问题时，用户可以在提交所有答案之前在各问题之间切换浏览。

---

## 自定义工具

自定义工具允许您定义 LLM 可以调用的自定义函数。这些函数在您的配置文件中定义，可以执行任意代码。

[了解更多](/docs/custom-tools)关于创建自定义工具的内容。

---

## MCP 服务器

MCP（Model Context Protocol）服务器允许您集成外部工具和服务，包括数据库访问、API 集成和第三方服务。

[了解更多](/docs/mcp-servers)关于配置 MCP 服务器的内容。

---

## 内部机制

在内部，`grep` 和 `glob` 等工具底层使用 [ripgrep](https://github.com/BurntSushi/ripgrep)。默认情况下，ripgrep 遵循 `.gitignore` 中的模式，这意味着 `.gitignore` 中列出的文件和目录将被排除在搜索和列表结果之外。

---

### 忽略模式

要包含通常会被忽略的文件，请在项目根目录下创建一个 `.ignore` 文件。该文件可以显式允许某些路径。

```text title=".ignore"
!node_modules/
!dist/
!build/
```

例如，这个 `.ignore` 文件允许 ripgrep 在 `node_modules/`、`dist/` 和 `build/` 目录中进行搜索，即使它们已在 `.gitignore` 中列出。
