# 知识库关键词系统与管道整改方案

> 设计确认时间：2026-07-01
> 版本：v2
> 状态：**✅ 已执行 2026-09-19**（见文末「执行记录」）

---

## 一、核心管道规则（已生效）

| 规则 | 内容 | 来源 |
|------|------|------|
| **入库默认层** | 01-Raw。不是 Draft，不是 Wiki | 用户明确 |
| **顺序不可跳** | Raw → Draft → Wiki，任何时候不能跳过中间层 | 用户明确 |
| **Draft→Wiki 门槛** | 只能用户本人说"放到03-Wiki"，agent 不得代劳 | 用户明确 |
| **歧义处理** | "入库" "wiki raw" "变成wiki" → 默认 01-Raw | 用户明确 |
| **文件命名** | 禁止 BV 编号/juejin ID 等不明文件名，全部用主题描述 | ✅ 已执行 |
| **全域禁令** | 03-Wiki 禁止直接写入 | ✅ 已补入 skill |

---

## 二、关键词系统

### 2.1 受控关键词表 `_keywords.yaml`

**位置：** `/mnt/d/Hermes-KnowledgeBase/_keywords.yaml`

**格式：**

```yaml
# 规范名（用作检索主键）
hermes-agent:
  aliases:            # 别名列表，用户/内容中可能出现的变体
    - Hermes Agent
    - Hermes-Agent
    - HermesAgent
    - hermes agent 部署
  category: tool      # 可选分类，方便按域检索
  status: verified    # verified | auto_added | merged | deprecated

semantic-layer:
  aliases:
    - 语义层
    - Ontology
    - 企业语义层建模
    - 本体
  category: concept
  status: verified

context-engineering:
  aliases:
    - 上下文工程
    - Context Engineering
    - 上下文管理
    - Context Management
  category: methodology
  status: auto_added
```

**关键词状态列表：**

| 状态 | 含义 | 搜索行为 |
|------|------|---------|
| `verified` | 已确认的规范词 | 正常检索 |
| `auto_added` | LLM 自动添加，待确认 | 正常检索，在报告中标记 |
| `merged` | 已合并到其他词 | 别名重定向到目标词 |
| `deprecated` | 概念过时 | 不推荐新用，存量文件保留 |

**规则：**
- 同义词合并不合并不等义词（`LLM` = `大语言模型`，`Hermes Agent` ≠ `Agent`）
- 新词由 LLM 自动添加，标记 `status: auto_added`
- 定期的 `auto_added` 词报告供用户 review，不阻塞日常管线

### 2.2 关键词在 frontmatter 中的格式

每篇文章的 frontmatter 统一使用 `keywords` 字段（替代旧的 `tags` 和 `related_concepts`），新增 `state` 字段，**删除旧 `status` 字段**。其余字段（`source_url`、`source_type`、`source_platform`、`author`、`publish_date`、`fetch_date`、`notes`、`priority`、`language`、`title`）全部保留不变。

```yaml
---
title: 企业语义层建模：从数据仓库到数字孪生
keywords:
  - hermes-agent          # 按优先级排序
  - llm-wiki
  - 部署教程
state:
  phase: draft            # raw | draft | wiki  （对应所在层级，不因后续操作而变）
  time_raw: 2026-07-01T10:17:00
  time_draft: 2026-07-01T10:35:00
  time_wiki: null         # 未 promote 时为空
source_url: "https://www.bilibili.com/video/BV1xxx/"
source_type: "video"
source_platform: "bilibili"
author: "作者名"
publish_date: "2026-06-28"
fetch_date: "2026-07-01"
priority: 3
language: "zh"
---
```

### 2.3 状态流转图

```
入库 → 01-Raw:     state.phase = raw   , time_raw 写入     ← 可搜索
ingest → 01-Raw:   time_draft 追加                      ← 可搜索（phase 不变）
        02-Draft:  state.phase = draft, time_raw+draft   ← 可搜索
promote → 02-Draft: time_wiki 追加                      ← 可搜索（phase 不变）
         03-Wiki:  state.phase = wiki , time_raw+draft+wiki ← 可搜索
```

**关键变化：** `phase` 只反映文件所在的层级，**永不改变**。文件是否被处理过由时间戳字段（`time_draft`、`time_wiki`）记录。

**搜索时的过滤逻辑：**

| 搜哪层 | 取 phase | 备注 |
|--------|----------|------|
| 03-Wiki | `wiki` | |
| 02-Draft | `draft` | |
| 01-Raw | `raw` | 是否被 ingest 过 → 看 `time_draft` 是否存在 |

### 2.4 关键词提取规则

| 阶段 | 提取方式 | 质量 | 质量控制 |
|------|---------|------|---------|
| Raw 入库 | LLM 从原文粗提取 | ~70-80% | 自动写入 `auto_added` 标记 |
| Ingest→Draft | LLM 从 `_keywords.yaml` 重新匹配精选 | ~90%+ | 新词自动追加(带标记) |
| 用户日常使用 | 你发现不合理的关键词直接指正 | — | 我即时修正 |

### 2.5 现有文章关键词迁移

遍历 KB 全部文件，分三类处理：

| 类别 | 特征 | 数量 | 处理方式 |
|------|------|------|---------|
| A | 已有 `tags` 字段 | ~40 文件 | `tags` 逐条匹配 `_keywords.yaml` → 保规范名/归并同义词/追加新词 → 格式转换 |
| B | 有 frontmatter 但无 tags | ~10 文件 | LLM 根据正文提取关键词 → 匹配词表 → 写入 |
| C | 无 frontmatter | ~5 文件 | LLM 生成完整 frontmatter（title/status/source/keywords） |

**先建 `_keywords.yaml`，再逐文件迁移，不做的事：**
- ❌ 不全部 LLM 重提（A 类 80% 是纯格式转换）
- ❌ 不修改正文内容
- ❌ 不改变文件物理位置

**迁移时的字段变更：**

| 原字段 | 操作 | 新字段 |
|--------|------|--------|
| `tags: [a, b, c]` | → 匹配词表后写入 | 删除旧字段 |
| `related_concepts: [...]` | → 合入 keywords | 删除旧字段 |
| `status: raw/processed/draft/promoted` | → 删除（被 `state.phase` 替代） | 删除旧字段 |
| `notes: "..."` | → 保留，不参与检索 | 保留不变 |
| 其余字段 | → 保留 | 保留不变 |

---

## 三、关键词生命周期

### 3.1 合并（Merge）

**触发时机：**

| 时机 | 怎么做 |
|------|--------|
| LLM 自动发现（draft 精选时检测到新词与现有词相似度 > 90%） | 记录到 `_pending_merges` 缓存区，不自动合并 |
| `kb-organization` 月度审计运行时 | 扫 `_pending_merges` + 全库 aliases 密度聚类，出合并建议清单 |
| 你日常发现说"这两个词不是一回事吗" | 我立即执行 |

**`_pending_merges` 格式：**

位置：`/mnt/d/Hermes-KnowledgeBase/_pending_merges.yaml`

```yaml
pending_merges:
  - source: agent-loop          # 候选合并源
    target: agentic-loop        # 候选合并目标
    confidence: 0.95            # 相似度
    discovered: 2026-07-01T10:00:00
    discovered_by: llm          # llm | user | audit
    note: "同一概念，agent-loop 是旧名"

  - source: ai-workflow
    target: ai-pipeline
    confidence: 0.85
    discovered: 2026-07-01T10:00:00
    discovered_by: llm
    note: "待确认是否为同一概念"
```

**执行方式**（以 `agent-loop` → `agentic-loop` 为例）：

```yaml
# _keywords.yaml 旧词标记合并，别名保留旧名做反向检索
agent-loop:
  aliases: [Agent Loop, agent loop]
  merged_into: agentic-loop   # 重定向标记
  status: merged

agentic-loop:
  aliases: [Agent Loop, agent loop, Agentic Loop, agentic loop]
  status: verified
```

**批量更新文件：**
```
全库 ripgrep frontmatter.keywords 中含 "agent-loop" 的文件
→ 替换为 "agentic-loop"
→ 不修改 state/正文，只改 keywords 字段
→ 生成变更报告（涉及文件数、路径列表）
```

**注意：** 批量更新是事件驱动（合并发生时执行），不是定期任务。

### 3.2 废弃（Deprecate）

**触发时机：**

| 时机 | 怎么做 |
|------|--------|
| 你指出 | 立即标记 `deprecated` |
| 技术/工具生命周期自然结束 | 你提我才做，不主动猜测 |

**执行方式：**

```yaml
old-tool:
  aliases: [OldTool, old_tool]
  status: deprecated
  deprecation_note: "2026-07 OldTool 已更名为 NewTool"
```

**存量文件不动**（历史文章保留旧关键词），新词表屏蔽 `deprecated` 词。

---

## 四、管道 Watchdog

### 4.1 每步骤结构化日志

每次管道操作输出格式：

```
📦 raw 入库  | 01-Raw/Bilibili/BV1xxx.md
  keywords: [语义层, OAG, 数字孪生] (8 raw → 5 deduped)
  state: phase=raw time=2026-07-01T10:17:00
  ✅ success | 4608 bytes written

📝 ingest 到 draft | → 02-Draft/Bilibili/xxx.md
  keywords: [语义层, OAG, 数字孪生, enterprise-architecture]
  state: phase=draft
  ✅ success | 3927 bytes written

⬆️ promote 到 wiki | → 03-Wiki/Bilibili/xxx.md
  state: phase=wiki
  ✅ success | 3927 bytes written
```

### 4.2 失败处理

任一管道步骤失败 → 立即报告：
- ❌ **步骤** + **失败原因** + **建议操作**
- 不静默失败，不跳过错误步骤

---

## 五、检索机制

### 5.1 检索顺序

```
用户说"找XX"

第1步：查 _keywords.yaml aliases 映射到规范名
第2步：按 wiki → draft → raw 顺序搜 frontmatter.keywords
第3步：返回优先级最高的可用版本（只返回一个版本）

    知识在 wiki 中 → 返回 wiki 版本
    知识只在 draft → 返回 draft 版本  
    知识只在 raw   → 返回 raw 版本

第4步（兜底）：全文 search（rg/grep），不限层
```

### 5.2 匹配层级

| 层级 | 触发条件 | 方法 | 速度 |
|------|---------|------|------|
| 别名归一 | 关键词在 `_keywords.yaml` aliases 中 | YAML 查表 | 毫秒 |
| 模糊匹配 | 别名未命中，但拆词后命中 keywords | 分词 + 子串匹配 | ~秒 |
| 全文兜底 | keywords 未命中 | ripgrep 全文搜 | ~秒 |

### 5.3 用户明确指定层

```
你说"raw里找语义层" → 只搜 01-Raw（phase=raw，筛选 `time_draft` 是否为 null 可知是否已处理）
你说"wiki里找"     → 只搜 03-Wiki
你说"draft里找"    → 只搜 02-Draft
```

### 5.4 结果展现格式

```
📄 企业语义层建模：从数据仓库到数字孪生
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 03-Wiki/Bilibili/企业语义层建模-从数据仓库到数字孪生.md
🏷️ 语义层 · OAG · 数字孪生
📋 语义层（Ontology）常被误认为是数据仓库、BI仪表盘...
   核心定位：组织的数字孪生，位于数据层和模型之间的语义层。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

同时发送 MEDIA: 文件（markdown 原文），直接可读。

---

## 六、组件审计（新增 Phase 0）

**目标：** 整改前先盘清所有跟 KB 发生文件 IO 的组件，避免改了 frontmatter 格式后其他组件写错。

### 6.1 组件清单

| # | 组件 | 类型 | KB 交互路径 | 写？ | 读？ | 审计状态 |
|---|------|------|------------|:---:|:---:|:--------:|
| 0 | `_kb-reform-design.md` | 方案文档 | 本文 | - | - | ✅ |
| 1 | `ingest-raw-to-draft` | Skill | 读 01-Raw → 写 02-Draft + 改 01-Raw status | ✅ | ✅ | 待审计 |
| 2 | `bilibili-subtitle` | Skill | B站下载 → Whisper → 写 01-Raw | ✅ | ❌ | 待审计 |
| 3 | `scrapling-ingest` | Skill | 抓网页 → 写 01-Raw | ✅ | ❌ | 待审计 |
| 4 | `whisper-postprocess` | Skill | LLM 后处理转写文本（输出给 ingest 用） | ❌ | ✅ | 待审计 |
| 5 | `ingest-raw-to-draft/scripts/clean_body.py` | 脚本 | 知乎噪声过滤 | ❌ | ✅ | 待审计 |
| 6 | `kb-organization` | Skill | 审计 KB 结构、检查 frontmatter | ❌ | ✅ | 待审计 |
| 7 | 文件重命名操作 | 手动 | 已执行（draft/wiki 31+22 文件重命名） | ✅ | ❌ | ✅ 已执行 |

### 6.2 审计要点

每个读/写 KB 的组件需要回答：

**写入组件（#1, #2, #3）：**
1. 写入时使用什么 frontmatter 字段名？→ 需要改为 `keywords` + `state` schema
2. 写入 `state` 时是否包含完整时间戳？→ 需要加 ISO8601
3. 是否在写入后输出 watchdog 日志？→ 需要加 ✅/❌
4. 是否从 `_keywords.yaml` 匹配关键词再写入？→ 需要加匹配逻辑
5. 是否处理 LLM 失败/超时路径？→ 需要加失败报告

**读取组件（#1, #4, #5, #6）：**
1. 读取时依赖的字段名是否变更？→ `tags` → `keywords`，`status` 原地保留但新增 `state.phase`
2. 读取后逻辑是否需要适配新字段？→ `status: raw` 迁移到 `state.phase: raw`

### 6.3 审计方法

逐组件 `skill_view(name)` 加载 → 读 SKILL.md 中读写 KB 的代码段 → 标注改动量。

审计结果作为 Phase 1 的前置条件：**全部组件审计通过 → 开始 Phase 1。**

---

## 七、执行计划

### Phase 0：组件审计（← 新增，排在最前）

1. 加载 6 个组件的 SKILL.md
2. 按 6.2 审计要点逐项检查
3. 汇总修改清单（每个组件的具体行号/字段/逻辑）
4. 完成审计报告

### Phase 1：构建关键词系统

1. 遍历 03-Wiki 全部文章，提取现有 tags/keywords
2. LLM 归并同义词，生成 `_keywords.yaml` 初版
3. 创建 `keywords` frontmatter + `state` 字段标准 schema
4. 分 A/B/C 三类逐文件迁移现有文章

### Phase 2：修改 Skill

按 Phase 0 审计结果修改各组件（字段名、关键词匹配、state 写入、watchdog 日志）

### Phase 3：集成检索

Hermes 会话中识别检索意图 → 执行 5.1 所述的三层检索逻辑 → 返回 5.4 格式结果。

---

## 八、不变的设计约束

- **不污染 Obsidian**：`_keywords.yaml` 以下划线开头，Obsidian 忽略；keywords 是标准 YAML frontmatter 字段，Obsidian 可读但无副作用
- **最小化人工介入**：LLM 自动提取、自动选词、自动追加。用户只在发现错误时指正
- **正向兼容**：现有文件只改 frontmatter 格式，不改内容正文

---

## 九、执行记录（2026-09-19）

### 执行裁决（与本文档原计划的差异）

| 本文档原计划 | 实际执行 | 原因 |
|---|---|---|
| Phase 0 审计 6 个组件 | ✅ 审计完成，**实际只有 3 个需改** | 其余 3 个（bilibili-subtitle / whisper-postprocess / kb-keywords）已合规；hermes-agent / native-mcp 是误报（模板属 config.yaml 非笔记 fm） |
| Phase 1 建关键词系统 | ⚠️ **发现已建过半**——Draft/Wiki 早已是新 schema，`_keywords.yaml` 已有 134 词 | 设计写"待执行"，但实际做过、只是**从未 commit** |
| Phase 1 分 A/B/C 三类迁移 | ✅ 合并为一次全量迁移（01-Raw 231 + Draft/Wiki 213） | 三类判据已不需要：字段来源统一按 keywords/tags/related_concepts 合并去重 |
| Phase 2 改 6 个组件 | ✅ 改 3 个 + 2 个模板文件 | 同 Phase 0 |
| — | ⚠️ **额外发现**：01-Raw 有 38 个文件仍用 BV/juejin ID 命名 | 违反本文档 §一「禁止 BV 编号」规则，**待处理** |
| — | ⚠️ **额外发现**：2 个文件 frontmatter 收尾 `---` 缺换行 | 预先存在的结构性损伤，已修 |
| — | ⚠️ **额外发现**：词表有 4 类坏别名 | 见下 |

### 词表修正（`_keywords.yaml`）

| 问题 | 修正 |
|---|---|
| 别名过宽：`AI` / `Agent` → AI-Agent | 删除（几乎命中一切） |
| 错映射：`智能体` → Multi-Agent | 移到 AI-Agent |
| 冲突：`react` → ReAct 且 react；`ai视频` → ai-video 且 视频生成 | 各归一处，0 冲突 |
| 缺失规范词 | 新增 5 个（prompt-engineering / vector-database / harness-engineering / video-generation / long-running-agent） |

现 **139 词，0 冲突**。

### 字段裁决（本文档未明确的）

| 字段 | 裁决 | 理由 |
|---|---|---|
| `sources`（Wiki 160/160 都有） | **保留** | 实测内容是 `['Bilibili/BVxxx.md']` —— **是溯源字段**（指向 01-Raw 来源），对应 `_kb-expansion-plan.md` 的溯源补强设计 |
| `source`（Draft/Wiki 常见） | **保留** | 描述性来源文字，本文档 §2.2 Draft 模板已包含 |
| `related`（Draft/Wiki 常见） | **保留**（并加显式警示） | Obsidian 双链；但必须写成引号包的列表项 |
| `created` | **删除** | 被 `state.time_raw` 替代 |

### 终检结果

```
全库 464 md
  ✅ 笔记类合规（keywords + state.phase + 层一致）   444 / 444  = 100%
  ⚪ 根目录设计文档/README（无 fm，正常）              20
  问题                                               0
```

### 本次 commit

| commit | 内容 |
|---|---|
| `180618d` | 基线快照（改造前，含历史未提交工作） |
| `078cd59` | 01-Raw 231 文件归一 + 词表坏别名修正 |
| `cdf3db1` | 组件归一 + Draft/Wiki 旧字段清理 + 结构损伤修复 |

### 遗留（未做）

1. **01-Raw 38 个 BV/juejin ID 命名的文件** → 需读内容改用主题名（**需人工判断，待办**）
2. **`_pending_merges.yaml` 合并机制** → 本文档 §3.1 设计，未落地（属新功能）
3. ~~04-Compendium / 05-Experience 新层~~ → ⛔ **已作废（2026-09-19 用户拍板）**：两份设计冲突且从未实施，不再推进。两份文档已加作废标记
4. 行业知识入 KB → ⏸ **用户明确：暂不入**
