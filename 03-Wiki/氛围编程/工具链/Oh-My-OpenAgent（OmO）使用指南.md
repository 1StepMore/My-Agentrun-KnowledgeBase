---
title: "Oh-My-OpenAgent（OmO）使用指南"
source: OmO 官方仓库 code-yeongyu/oh-my-openagent（项目一手，E2）
evidence: E2
domain: 氛围编程
keywords: [opencode, vibe-coding, AI编程, AI-Agent, claude-code]
state:
  phase: wiki
  time_raw: "2026-09-23T03:45:00+08:00"
  time_draft: "2026-09-23T03:45:00+08:00"
  time_wiki: "2026-09-23T03:50:00+08:00"
related:
  - "[[_MOC-氛围编程]]"
  - "[[OpenCode与Oh-My-OpenCode高级使用]]"
---

# Oh-My-OpenAgent（OmO）使用指南

> **工具篇章**（你实际在用的 opencode 增强插件）。
> **证据等级 E2**：来源是 **项目自己的官方仓库**（`code-yeongyu/oh-my-openagent`，⭐69k），**不是 Anthropic/OpenAI 等企业官方**——引用时请区分。
> 官方原文存档：`01-Raw/VibeCoding/oh-my-openagent/`（含官方中文 README 全文）
> 更早的二手教程（E4，博客园）：[[OpenCode与Oh-My-OpenCode高级使用]]

## 0. 名字先理清（最容易踩的坑）

同一个项目有三层名字，混用会装错东西：

| 层 | 名字 | 说明 |
|:---|:---|:---|
| 项目名 | **oh-my-openagent（OmO）** | 仓库名（原 `oh-my-opencode`，已改名） |
| **npm 包名 / CLI 二进制** | **仍是 `oh-my-opencode`** | 过渡期双重发布；`oh-my-openagent install` 也可以 |
| 短命令 | `omo-agent-toolkit` | 安装完成后的快捷入口 |
| ⚠️ `omo` bin | 已移除，归 **OmO Native**（包名 `omo-ai`，仅 beta：`bun add -g omo-ai@beta`） | **不要**用 `bunx omo` / `npx omo`——npm 上的 `omo` 是**别人的无关包**，会解析错 |

其他相关名：Codex 侧 marketplace = `sisyphuslabs`，插件 = `omo`（`omo@sisyphuslabs`）；`lazycodex-ai` 是 Codex Light 版安装器。

## 1. 安装（官方推荐"让 agent 自己装"）

官方给人类用户的做法是**把提示词丢给 agent**（原话：*"人类在配置环境的时候，总是容易敲错字母"*）：

```
Install and configure oh-my-openagent by following the instructions here:
https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

或让 agent 直接拉安装指南：

```bash
curl -fsSL https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

**启用**：在 `opencode.json` 的 `plugin` 数组里出现插件入口（兼容层优先 `oh-my-openagent`，旧的 `oh-my-opencode` 仍会加载但**带警告**）。

## 2. 一句话上手：`ultrawork` / `ulw`

> 官方 README 的核心亮点只有一条：**装完，输入 `ultrawork`（或 `ulw`），完事。**
> 其余全部特性"你都不需要知道，它就是能跑"。

底层是 **graph engineering（图工程）**：把任务编排成多 agent 协作图——主 Agent 调度 **架构师咨询 / Librarian（检索）/ Explore（快速 grep）/ 类别工作者**并行工作。

**成本提醒（官方自己的说法）**：`ultrawork` 在仅订阅 ChatGPT($20) / Kimi Code($19) / GLM Coding($10) 这类套餐下也能跑；按 token 计费时社区反馈 Kimi 与 GLM 更省。

## 3. 能力清单（官方概览，按用途分组）

| 组 | 能力 |
|:---|:---|
| **Agents** | 主 Agent（调度器）· Ultrawork Planner（`/ulw-plan`）· 架构师咨询（架构/调试）· Librarian（文档与代码检索）· Explore（快速 grep）· Multimodal Looker |
| **后台 Agents** | 像真实开发团队那样并行跑多个 agent |
| **Team Mode**（选择性启用） | 领导 Agent + 最多 8 个并行成员，tmux 实时可视化 |
| **代码理解** | LSP & AST 工具：重构、重命名、诊断、AST 感知检索 |
| **精确编辑** | 基于哈希的编辑（`hashline_edit: true`）：`LINE#ID` 引用在每次应用修改前**验证内容**，消除陈旧行错误 |
| **上下文** | 自动注入 `AGENTS.md` / `README.md` / 条件规则 |
| **兼容** | Claude Code 兼容层：完整 Hook 系统、命令、技能、Agents、MCP |
| **内置 MCP** | websearch（Exa）· context7（文档）· grep_app（GitHub 检索）· lsp ——**运行时注入，不出现在 `opencode mcp list`** |
| **效率** | Goal · Todo Enforcer · Comment Checker · Think Mode · 会话历史检索 · 会话自动恢复（错误/上下文溢出/API 失败） |
| **诊断** | `bunx oh-my-opencode doctor`：验证插件注册、配置、模型、环境 |

## 4. 配置（`~/.omo/omo.jsonc`）

- **位置**：用户级 `~/.omo/omo.jsonc` + 从当前目录**逐级向上**查找项目 `.omo/omo.jsonc`（到 `$HOME` 为止），**离得近的优先**。旧 `oh-my-*` 配置文件只被迁移引擎导入一次。
- **JSONC**：支持注释与尾逗号。
- **可覆盖**：任意 Agent 的模型、temperature、prompts、权限；内置技能 `playwright`（浏览器自动化）、`git-master`（原子提交）。
- **类别（categories）**：`visual-engineering` / `ultrabrain` / `deep` / `artistry` / `quick` / `unspecified-low` / `unspecified-high` / `writing` + 自定义名。
- **Hooks**：**54+** 内置生命周期 Hook（启用 Team Mode 为 61 个），用 `disabled_hooks` 关。
- **后台并发**：按 provider/model 设并发上限。
- **模型回退**：`fallback_models` 支持普通字符串与 per-fallback 对象混用。

## 5. 卸载（官方四步）

```bash
# 1) 从配置里摘掉插件
jq '.plugin = [.plugin[] | select(. != "oh-my-openagent" and . != "oh-my-opencode")]' \
    ~/.config/opencode/opencode.json > /tmp/oc.json && mv /tmp/oc.json ~/.config/opencode/opencode.json
# 2) 清配置
rm -f ~/.omo/omo.jsonc ~/.omo/omo.json .omo/omo.jsonc .omo/omo.json
# 3) 验证
opencode --version    # 应无插件相关输出
# 4) 若装了 Codex Light 版
npx lazycodex-ai uninstall
```

## 6. 已知注意事项（官方 README 明示）

- **匿名遥测默认开启**（统计 DAU/WAU/MAU）：每机器每 UTC 日最多一次、哈希化标识、不用原始主机名。禁用：`OMO_SEND_ANONYMOUS_TELEMETRY=0` 或 `OMO_DISABLE_POSTHOG=1`。
- **项目正在重构**：目标是把纯 TS 核心 / MCP server / 技能 / 适配器 shim 分层，以复用"多 harness"（OpenCode、Codex、Pi、Claude Code…）。
- README 含赞助商与推荐内容（**属推广信息，非技术结论**），本页只取技术事实。

## 7. ⭐ 官方明说的一条原则：**指令文件 ≠ 强制边界**

> 官方原文：`AGENTS.md` files are instruction context… **but they are not a deterministic permission boundary.**

官方列出**确定性强制**真正来自哪里：

| 强制来源 | 说明 |
|:---|:---|
| **OMO 配置** | `agents.*.permission`、agent 的 `tools`、禁用的工具/agent |
| **内置 agent 限制** | 官方预置角色的工具边界 |
| **OpenCode 自身权限门** | 宿主层的 permission 门（可用时） |
| **守卫 hook** | 如 `team-tool-gating`、`write-existing-file-guard` |

→ 这与我们"**机制强制不靠自觉**"是同一条原则：**写在文档里的规则只是上下文，不是边界**；要拦得住就得落在配置/hook/权限门上。（同类陷阱我们实证过：机制装了≠在工作、门禁空转。）

## 8. 选版判据（官方三版）

| 版本 | 适用 | 命令 |
|:---|:---|:---|
| **Ultimate**（推荐） | 已用 OpenCode / 想要最成熟的路径 | `bunx oh-my-openagent install` |
| **Light** | 已用 Codex CLI | `npx lazycodex-ai install` |
| **OmO Native（beta）** | 不想先装宿主 | `bun add -g omo-ai@beta`（**必须带 `@beta`**，不带会按设计失败） |

Ultimate / Light 是**插件**（装进你已有的宿主）；Native 是**独立**的（自带固定版本引擎）。

## 9. 配置文件位置（官方：统一一份）

一份配置管**所有 omo harness**（OpenCode 插件、Senpi、Codex）。优先级从低到高：

1. **用户层**：`~/.omo/omo.jsonc`（`omo.json` 作后备名）
2. **项目层**：从工作目录逐级向上到 `$HOME` 的 `.omo/omo.jsonc`

⚠️ 旧文件（`oh-my-openagent.jsonc` / `oh-my-opencode.jsonc` / `~/.omo/config.jsonc`）**只有迁移引擎会读**，别以为改了有用。

**其他官方机制**：后台 agent（启动后可继续干活，完成后通知、按需取结果）· Team Mode（实验性，**默认关闭**）· 类别系统（Categories）· 模型解析链（Model Resolution）

## 待补

- [ ] 官方 `docs/guide/installation.md`、`docs/reference/features.md`、`docs/reference/configuration.md` 三个正式文档（README 只是概览）→ 下一步抓
- [ ] `mass ulw`（README 顶部提到）与 `ulw` 的差别
- [ ] 与 opencode 原生 `plugins` / `skills` / `mcp-servers` 的能力边界对照表
