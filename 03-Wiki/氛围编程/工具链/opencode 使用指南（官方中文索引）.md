---
title: "opencode 使用指南（官方中文索引）"
source: opencode 官方文档（含官方中文版，E1）
evidence: E1
domain: 氛围编程
keywords: [opencode, vibe-coding, AI编程, claude-code, AI-Agent]
state:
  phase: wiki
  time_raw: "2026-09-23T02:40:00+08:00"
  time_draft: "2026-09-23T02:40:00+08:00"
  time_wiki: "2026-09-23T03:55:00+08:00"
related:
  - "[[_MOC-氛围编程]]"
  - "[[Oh-My-OpenAgent（OmO）使用指南]]"
---

# opencode 使用指南（官方中文索引）

> **工具篇章**：你的主力工具。官方文档**有中文版**（36 页），本页是官方中文汇编的**使用索引**——按"我要干什么"找，不按文档目录找。
> 证据 **E1**（opencode 官方文档）。全文存档：`01-Raw/VibeCoding/opencode/`（zh 36 + en 37）

## 按目的找

| 我要… | 去这（官方中文汇编） |
|:---|:---|
| 装起来 / 跑通第一件事 | [[opencode-官方文档汇编-中文--01-快速开始与核心概念]] |
| 配模型 / 换 provider / 配快捷键 / 主题 | [[opencode-官方文档汇编-中文--02-配置与权限]] |
| 管权限（让它敢动手 / 又别乱动） | [[opencode-官方文档汇编-中文--02-配置与权限]] · 权限与沙箱 |
| 写插件 / 写 skills / 接 MCP / 自定义工具 | [[opencode-官方文档汇编-中文--03-扩展能力-插件-技能-MCP-工具]] |
| 接 GitHub / GitLab / IDE / 用 SDK 当库 | [[opencode-官方文档汇编-中文--04-集成-GitHub-GitLab-IDE-SDK-Server]] |
| **在 WSL 里跑 / 出问题排查** | [[opencode-官方文档汇编-中文--05-运维与排错]] |

## 核心概念速览（来自官方目录）

| 概念 | 一句话 |
|:---|:---|
| **TUI** | 终端界面主入口：会话、工具调用可视化、快捷键（`keybinds`） |
| **CLI** | 命令行子命令：`opencode run` 等（非交互/脚本化） |
| **commands** | 自定义命令，把常用提示词固化成可复用入口 |
| **rules（规则）** | 项目级持久指令（等价于 Claude Code 的 `CLAUDE.md` 思路） |
| **permissions / policies** | 权限与策略：决定 agent 能不能改文件、跑命令、联网 |
| **agents** | 子智能体：按角色分工，隔离上下文 |
| **plugins** | 扩展点：注入工具、hook、生命周期逻辑（**OmO 就走这一层**） |
| **skills** | 可发现的能力模块 |
| **mcp-servers** | 接外部工具的标准协议 |
| **custom-tools** | 自定义工具 |
| **sdk / server / share / acp** | 把 opencode 当库/服务用；`acp` 是与编辑器互通的协议 |
| **zen** | 官方托管的模型接入（无需自备 key） |
| **enterprise** | 企业部署相关 |

## 与 OmO 的关系

opencode 是**宿主**（harness），OmO 是**插件**：OmO 通过 opencode 的 plugin 层注入多 agent 编排、内置 MCP（websearch/context7/grep_app/lsp）、54+ hooks 等。所以"opencode 装了不动"和"opencode + OmO"是两种体验 —— 见 [[Oh-My-OpenAgent（OmO）使用指南]]。

**边界提醒**：OmO 的 `ultrawork` 会显著提高 token 消耗（并行 agent），适合中等以上任务；单文件小改动用原生 opencode 更省。

## 实操配方（官方中文文档取证的要点）

### 1. 权限：`permission` 三档 + 两条易踩的坑

```jsonc
// opencode.json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "*": "ask",              // 默认问
    "bash": { "*": "ask", "git *": "allow", "npm *": "allow", "rm *": "deny" },
    "edit": { "*": "deny", "docs/**/*.md": "allow" }
  }
}
```
- 三档：`"allow"` 直接跑 / `"ask"` 弹窗 / `"deny"` 阻止；整体也可一次给 `"permission": "allow"`。
- ⚠️ **坑一：最后匹配的规则优先** → 通配 `"*"` 必须写在**最前面**，具体规则放后面（写反了等于通配覆盖全部）。
- ⚠️ **坑二：`external_directory` 才是"出工作目录"的开关** —— `~` / `$HOME` 展开只影响**写法**，**不会**把目录纳入工作区；访问 cwd 之外的路径必须显式用 `external_directory` 允许（`read`/`edit`/`glob`/`grep` 及多数 bash 命令都受此约束）。
- 版本提示：`v1.1.1` 起旧的 `tools` 布尔配置已弃用、并入 `permission`（仍向后兼容）。

### 2. 配置优先级：**合并**，不是替换

按加载顺序（后者覆盖前者的**冲突键**，非冲突项全部保留）：

`远程配置(.well-known/opencode)` → **全局 `~/.config/opencode/opencode.json`** → `OPENCODE_CONFIG` 环境变量 → **项目 `opencode.json`** → `.opencode` 目录（agents/commands/plugins）→ `OPENCODE_CONFIG_CONTENT`

→ 实用含义：**个人偏好放全局、项目特定放项目内**，两者叠加而不是二选一。

### 3. 内置 agent 谱系（官方）

| agent | 模式 | 能力 |
|:---|:---|:---|
| **build** | primary（默认） | 全工具，日常开发主力 |
| **plan** | primary | **受限**：文件编辑与 bash 默认全 `ask` → 只看不改 |
| **general** | subagent | 通用多步任务，可改文件 |
| **explore** | subagent | **快速只读**：按模式找文件/搜关键字/回答代码库问题 |
| **scout** | subagent | **只读**：外部文档与依赖研究（可把依赖仓库克隆到托管缓存看源码） |

### 4. WSL（官方推荐做法，你就在这个环境）

- 官方**推荐 WSL**：文件系统性能更好、完整终端支持、与依赖的开发工具兼容性好。
- 安装：`curl -fsSL https://opencode.ai/install | bash`
- 访问 Windows 文件：`cd /mnt/c/Users/...` 或 `/mnt/d/...` 后运行 `opencode`
- **桌面应用 + WSL 服务端**：在 WSL 内启动服务时加 `--hostname 0.0.0.0` 允许外部连接

### 5. OpenCode Go（可选订阅）

官方说明：**每月 10 美元**，提供对一批**经官方测试与基准跑分**的开源编程模型的稳定访问（含 API key）；**完全可选**，不是使用 opencode 的前提。主要面向国际用户、提供稳定全球访问。

## 待补

- [ ] `rules` 与 Claude Code `CLAUDE.md` 的对照（迁移视角）
- [ ] 与本机 Hermes 工具的协作方式（谁调度谁）
