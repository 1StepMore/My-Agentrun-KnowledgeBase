---
title: "MOC · 氛围编程（Vibe Coding）知识地图"
source: 本库自建索引（入口页）
evidence: E1
domain: 氛围编程
keywords: [vibe-coding, AI编程, claude-code, opencode, context-engineering]
state:
  phase: wiki
  time_raw: 2026-09-23T00:00:00+08:00
  time_draft: 2026-09-23T00:00:00+08:00
  time_wiki: 2026-09-23T00:00:00+08:00
related:
  - "[[_MOC-AI落地]]"
---

# 🗺️ 氛围编程知识地图（MOC）

> **这是入口页。** 任何关于「氛围编程 / AI 编码」的问题，先从这里定位，再进具体条目。
> 架构说明见 `00-Inbox/reports/知识库架构-氛围编程与AI落地-20260923.md`
> 证据等级：**E1 官方一手** / E3 社区高质量 / E4 社区经验（仅作线索）

---

## 🚪 三个入口（我想干什么是关键）

| 我想… | 从这进 |
|:---|:---|
| **搞懂一个词** | [[术语表-氛围编程]]（19 个机制术语，带官方英文原句）|
| **系统学一遍** | §5 学习路径（按顺序读） |
| **做个选择/踩坑前** | §3 方法论 + §4 工具链 |

---

## 1. 认知基座（这行是什么）

| 条目 | 说明 | 状态 |
|:---|:---|:---|
| 什么是氛围编程（术语、谱系、与 AI 编码的关系） | 名词澄清：vibe coding / AI 编码 / agentic coding 的边界 | ⏳ 待写（素材已到位：[[Anthropic-工程博客-官方一手--工程实践与最佳实践]]）|
| 能力边界与失败模式 | 什么活能干、什么活会炸 | ◐ 已有素材：[[告别循环修复-AI编码的防腐化工程闭环]] |

## 2. 权威一手（官方怎么说的）

| 来源 | 汇编产物 | 规模 | 证据 |
|:---|:---|---:|:---|
| **Claude Code 官方文档** | [[Claude-Code-官方文档汇编-Getting-started]] · [[Claude-Code-官方文档汇编-Build-with-Claude-Code]] · [[Claude-Code-官方文档汇编-Configuration]] · [[Claude-Code-官方文档汇编-Administration]] · [[Claude-Code-官方文档汇编-Agent-SDK]] · [[Claude-Code-官方文档汇编-Reference]] · [[Claude-Code-官方文档汇编-What-s-New]] | 208 页 | E1 |
| **opencode 官方文档** | [[opencode-官方文档汇编-中文--01-快速开始与核心概念]] · [[opencode-官方文档汇编-中文--03-扩展能力-插件-技能-MCP-工具]] · [[opencode-官方文档汇编-中文--04-集成-GitHub-GitLab-IDE-SDK-Server]] · [[opencode-官方文档汇编-中文--02-配置与权限]] · [[opencode-官方文档汇编-中文--05-运维与排错]] | 36 中文 + 37 英文 | E1 |
| **Anthropic 官方工程博客** | [[Anthropic-工程博客-官方一手--工程实践与最佳实践]] | 24 篇 | E1 |
| **Anthropic 开发者文档**（agent/skills/tool-use/MCP/评测） | [[Anthropic-开发者文档汇编-Agent-与工具]] · [[Anthropic-开发者文档汇编-Claude-构建指南]] · [[Anthropic-开发者文档汇编-托管-Agent]] · [[Anthropic-开发者文档汇编-CLI-SDK-库]] · [[Anthropic-开发者文档汇编-测试与评测]] | 144 页（en） | E1 |
| **OpenAI 官方**（Agents SDK + Cookbook） | [[OpenAI-官方文档汇编-01-Agents-SDK-官方文档]] · [[OpenAI-官方文档汇编-02-Cookbook-官方文章]] · [[OpenAI-Codex-官方文档-GitHub-仓库--官方文档]] | 20 篇（302 KB） | E1 |
| ⚠️ 年份提醒 | Cookbook 部分文章为 **GPT-3 时代（2023）**（如 `techniques_to_improve_reliability`）——**E1 也需看年份**，只能作史料，不得当现行最佳实践 |
| ⚠️ 说明 | 官网对本站 IP 403 → **改走官方 GitHub 仓库**（openai-agents-python / openai-cookbook）；仓库里纯网页类文档（如 codex CLI 手册）是跳转桩，仍缺 | — | — |

## 3. 方法论（怎么做才对）

### 3.1 循环与自主度　`方法论/循环与自主度/`
**⭐ [[智能体与工作流模式（方法论·官方一手提炼）]]** ← 官方：workflow≠agent / 五种工作流模式 / "只在可证明改善时才加复杂度"
**⭐ [[多智能体与编排（方法论·官方提炼）]]** ← 官方一手教训：50 个子代理 / 子代理=智能过滤器 / 错误会累积→断点恢复
[[Loop-Engineering]] · [[循环工程-Loop-Engineering]] · [[Loop-Engineering实操指南]] · [[Agentic-Loops-重塑开发生态]] · [[goal-programming-autonomous-ai-collaboration]] · [[龙虾之父说-loops-能干嘛]]

### 3.2 规格驱动 / 测试驱动　`方法论/规格与测试/`
**⭐ [[评测的基础设施噪声（方法论·官方提炼）]]** ← 官方实测：环境能摆动 benchmark 数个点（比榜首差距还大）／**紧约束奖励高效、松约束奖励利用资源＝测的不是同一件事**
**⭐ [[评测方法论（方法论·官方一手提炼）]]** ← 官方：反应式循环的根因 / 三类评分者 / 能力评测≠回归评测
[[SDD规范驱动开发-vs-Vibe-Coding]] · [[BDD行为驱动开发-AI编程应用]] · [[TDD-ATDD-BDD-测试驱动开发方法论]]

### 3.3 上下文与 Harness（被低估的一层）　`方法论/上下文与Harness/`
**⭐ [[托管式Agent架构-解耦大脑与手（方法论·官方提炼）]]** ← 官方**现行**做法：别养宠物／**会话 ≠ 上下文窗口**／meta-harness
**⭐ [[上下文工程（方法论·官方一手提炼）]]** ← 官方一手提炼：context rot / attention budget / 五个杠杆 / 实操清单
**⭐ [[工具规模与检索的上下文治理（方法论·官方提炼）]]** ← 官方：工具定义税（58 工具≈55K tokens）/ Tool Search / 程序化调用 / 检索失败率 5.7%→1.9% ｜**含本机 204 skill ≈11K tokens 实测**
**⭐ [[Harness与长任务（方法论·官方一手提炼）]]** ← 官方一手提炼：长任务失败的根因 / 让主观质量可评分 / Ralph loop 原理
[[harness-工程-多模态视角]] · [[Harness工程-被忽视的视角]] · [[从ToolCall到Harness-Claw-Agent一切]] · [[上下文工程-用磁盘文件替代上下文状态管理]]

### 3.4 Skill 设计与 Agent 稳定输出　`方法论/Skill设计与Agent稳定输出/`
**⭐ [[Skill与工具设计（方法论·官方一手提炼）]]** ← 官方机制：skill 的 description 为什么必须自带触发条件
[[5-Agent-Skill-Design-Patterns-ADK]] · [[Skill最佳实践-五种设计模式]] · [[如何写好一个Skill（一）]] · [[如何写好Skill-原则与技巧]] · [[从0到会写Skill-10分钟科普]] · [[hermes-agent-15-技巧-5-心法]]

### 3.5 流程与治理　`方法论/流程与治理/`
**⭐ [[事故复盘与可观测性（方法论·官方提炼）]]** ← 官方复盘：**"我们的评测没捕捉到用户报的现象"**（＝本库"假门禁"同病）／隐私与可调试性的张力／要在真实生产上跑评测
**⭐ [[CLI编码智能体最佳实践（官方提炼）]]** ← Claude Code 官方：给它能跑的检查 / 四阶段工作流 / **六个失败模式+修法**
**⭐ [[护栏与人在环（方法论·官方提炼）]]** ← OpenAI 官方：护栏四层 / 阻断 vs 并行 / tripwire 要"有咬合" / HITL 状态放服务端
[[七阶段AI开发流程-用CodingAgent交付成品的方法论]] · [[ai-assisted-coding-workflow-general-methodology]] · [[告别循环修复-AI编码的防腐化工程闭环]] · [[巨型代码库的AI编码治理-spec驱动与skill约束]]

### 3.6 安全与隔离　`方法论/安全与隔离/`
**⭐ [[沙箱隔离与遏制（方法论·官方提炼）]]** ← 官方：先环境层后模型层 / 三条遏制模式 / **隔离强度要匹配用户的监管能力** / egress 风险

> ⚠️ **时效提醒**：官方 2024-12 的 `building-effective-agents` 已被官方自己标注"工具生态已变化"，**现行做法见 [[托管式Agent架构-解耦大脑与手（方法论·官方提炼）]]**。引用旧文时务必说明年份。

## 4. 工具链（我实际在用的）

| 工具 | 官方文档 | 中文 | 备注 |
|:---|:---|:---|:---|
| **opencode**（主力） | ✅ [[opencode 使用指南（官方中文索引）]] | ✅ 36 页官方中文 | 汇编见「扩展能力」篇；OmO 是其插件层 |
| **Claude Code** | 官方 208 页全量入库 | ❌ 官方无中文 | 概念最强，读 §2 汇编 |
| **Codex**（OpenAI） | ⏳ 待抓 | — | 走 GitHub 官方仓库 |
| **OmO 插件**（Oh-My-OpenAgent） | ✅ [[Oh-My-OpenAgent（OmO）使用指南]] | 官方中文 README 已入库 | E2（项目一手，⭐69k） |
| **Hermes Agent** | ✅ `工具链/Hermes Agent/` | ✅ | [[hermes-agent-15-技巧-5-心法]] · [[b站视频-本地-ai-知识库]] |
| **Xpertai**（agent 平台） | ✅ `工具链/Xpertai/`（官方文档 150 篇） | — | 官方文档区已入库 |

## 5. 学习路径（按顺序）

1. **第 0 步 · 概念**：§2 的 [[Anthropic-工程博客-官方一手--工程实践与最佳实践]]（先读 claude-code-best-practices 与 building-effective-agents 两篇）
2. **第 1 步 · 上下文**：§3.3 上下文/Harness 四篇——**这是氛围编程真正的分水岭**
3. **第 2 步 · 循环**：§3.1 挑 2 篇（Loop-Engineering + 实操指南）
4. **第 3 步 · 规格与验证**：§3.2 + §3.5（防腐化闭环）
5. **第 4 步 · 工具**：§4 的 opencode 官方中文汇编（用你自己的工具练）
6. **第 5 步 · 沉淀**：§3.4 Skill 设计（把重复劳动变成 skill）

## 6. 目录结构（已归位，2026-09-23）

```
03-Wiki/氛围编程/
├── _MOC-氛围编程.md            ← 你在这里
├── 术语表-氛围编程.md
├── 认知基座/                    什么是氛围编程（术语、谱系、官方口径）
├── 方法论/                      循环与自主度 · 规格与测试 · 上下文与Harness · Skill设计 · 流程与治理 · 安全与隔离
├── 工具链/                      opencode · OmO · Xpertai · Hermes Agent
└── 案例与社区/                  媒体与视频生产
```
> 旧 Wiki 的 29 篇平铺文件已按上表归位，**文件名未变 → 所有 wikilink 保持有效**（实测校验通过）。

## 7. 待补（缺口，不藏）

- [ ] 术语表（≥20 词，含官方出处）
- [ ] 认知基座两篇（素材已在 Raw，待写）
- [ ] OpenAI 官方（Codex / Cookbook）→ GitHub 路径
- [ ] Anthropic 开发者文档汇编（Raw 366 页已就位）
- [ ] Claude Code 中文（官方无中文 → 考虑做「官方概念中文对照」）
- [ ] 社区最佳实践层（E3/E4，需标日期）
