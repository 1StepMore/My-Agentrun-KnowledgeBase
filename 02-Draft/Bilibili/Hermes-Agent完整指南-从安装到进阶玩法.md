---
title: Hermes-Agent完整指南-从安装到进阶玩法
source: 知乎回答（1 篇）；本页为我们的提炼
keywords:
- Hermes-Agent
- setup
- OpenClaw
- multi-platform
- productivity-tools
state:
  phase: draft
  time_raw: '2026-05-07T00:00:00'
  time_draft: '2026-09-23T01:05:00'
sources:
- zhihu-2027128115831260939.md
related:
- '[[hermes-agent-15-技巧-5-心法]]'
- '[[Hermes-Agent接入飞书-企业自建应用与长连接配置]]'
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---

# Hermes Agent 完整指南：从安装到进阶玩法

## 结论

一篇**工具书性质**的速查：环境要求 → 一行命令安装 → 设置与模型 → 验证 → 对话与斜杠命令 → 多平台网关 → 从 OpenClaw 迁移。最有价值的三个命令是 **`hermes doctor`（排错第一反应，能省 90% 排错时间）**、**`/skills`（看 agent 自进化沉淀了什么）**、**`/insights --days 7`（给你出一份 AI 周报）**。

## 一、环境要求

- **Python 3.11+**（`python3 --version` 自查）。
- macOS（Homebrew）：`brew install python@3.11`；Linux / WSL2：`sudo apt install python3.11 python3.11-venv`。

## 二、安装：一行命令

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

> 📌 **官方口径（2026-09 核对 README）**：安装脚本的规范地址是 `https://hermes-agent.nousresearch.com/install.sh`（Windows 原生用 PowerShell 版 `install.ps1`）。原视频/原文给出的 `raw.githubusercontent.com/.../scripts/install.sh` 是旧式写法，属同一脚本的 GitHub 直链——**能用但非官方推荐入口**。

脚本自动完成：检测系统环境 → 安装依赖 → 下载核心代码 → 把 `hermes` 注册进 PATH。

两个必须知道的细节：
1. 装完**当前终端还不认识 `hermes` 命令**，需 `source ~/.zshrc`（macOS）或 `source ~/.bashrc`（Linux），或重开终端；
2. **不要用 `sudo` 跑安装脚本**——用普通用户权限，加 sudo 反而引出权限问题。

## 三、设置向导与模型配置

```bash
hermes setup     # 首次建议跑完整向导：选提供商、填 API Key、配默认工具集与基础偏好
hermes model     # 随时换模型，不改代码
```

- 对话中也能临时切换：`/model openrouter:nous/hermes-3-405b` —— 可以**先用便宜模型跑初稿、再切强模型精修**。
- **国内模型可用**：Kimi / Moonshot / MiniMax，或任何**兼容 OpenAI API 格式**的服务，走自定义端点即可，不必翻墙。

## 四、验证安装：`hermes doctor`

逐项检查 Python 版本、依赖完整性、模型配置有效性、工具链状态；全绿即装好。

> 💡 排错铁律：**遇到问题先跑 `hermes doctor`，不要去搜论坛**——80% 的问题它直接给答案。

## 五、对话与高频斜杠命令

启动 `hermes` 进入交互式终端（多行编辑、斜杠命令自动补全、对话历史、流式输出）。重点两个命令：

| 命令 | 作用 | 为什么重要 |
|:---|:---|:---|
| `/skills` | 查看 agent 自动沉淀的技能 | 自进化能力的可视化窗口；用一个月后会看到技能积累量 |
| `/insights --days 7` | 生成 AI 助手「周报」 | 总结这周学到了什么、哪些技能频繁调用、哪些任务模式在重复 |

后者的意义不只是好玩：**它让 AI 员工第一次有了可考核的绩效数据**。

## 六、多平台网关

```bash
hermes gateway    # 一个进程管所有聊天平台（Telegram / Discord / Slack / 飞书…）
```

关键特性：**跨平台对话连续**——在 Telegram 聊到一半切到 Discord 继续，**上下文不丢**；另支持语音消息转录。对做社群运营的人尤其有用：客户分散在不同渠道，但 Hermes 记住的是同一份上下文。

## 七、从 OpenClaw 迁移

Hermes 是 OpenClaw（龙虾）的正式继任者（同一团队、同一条产品线，架构与能力大幅升级）。

```bash
hermes claw migrate              # 交互式迁移（推荐）
hermes claw migrate --dry-run    # 只看不执行
hermes claw migrate --preset user-data   # 只迁用户数据，不含密钥
```

首次跑 `hermes setup` 时若检测到 `~/.openclaw` 目录会自动提示迁移。迁移内容：人格文件（SOUL.md）、记忆（MEMORY.md / USER.md）、自建技能（进 `~/.hermes/skills/openclaw-imports/`）、命令审批白名单、各平台 API Key（Telegram / OpenRouter / OpenAI / ElevenLabs 等）、TTS 语音资源、工作区指令（AGENTS.md）。

**迁移不删除 OpenClaw 原始数据**，可放心操作。

## 八、商业价值翻译（为什么这几条重要）

1. **模型无关 = 最大的保险**：不绑定任何一家模型，换模型不影响累积的技能与记忆——在模型快速迭代期，这是最重要的护城河。
2. **跨平台上下文不丢 = 解决客服最大痛点**：客户从微信问一半、去 Telegram 再问一遍，AI 不需要重新了解情况。
3. **一键迁移 = 生态在收敛**：新项目提供老项目的迁移工具，通常意味着它有信心成为最终胜出者。
4. **`/insights` = AI 第一次有了「周报」**：管理 AI 从拍脑袋变成有数据可看。

## 关联与核实记录

- `[[hermes-agent-15-技巧-5-心法]]`（使用技巧）、`[[Hermes-Agent接入飞书-企业自建应用与长连接配置]]`（接入配置）可与本篇组成 Hermes 知识三部曲。
- **已核实（2026-09-23，本机 Hermes v0.21.0 + 官方 README）**：`hermes setup` / `hermes model` / `hermes doctor` / `hermes gateway` / `hermes claw migrate` / `hermes skills` / `hermes insights --days N` **全部真实存在**；安装脚本规范地址为 `hermes-agent.nousresearch.com/install.sh`。
- **未核实**：① 原文正文的 star 数自相矛盾（前文 74K+、后文 59K），本次无法联网核验（GitHub API 请求被挡），**引用该数字前必须回原文/官方仓库核对**；② `hermes claw migrate` 的具体参数（`--dry-run`、`--preset user-data`）未逐条验证，以 `hermes claw migrate --help` 实测为准；③ 文中部分数字在清洗过程中丢失，涉及数字的结论都需回原文。
