# Hermes Agent 知识库

> Hermes Agent 相关知识积累仓库，专注于 AI 自动化工作流和本地知识库搭建。
>
> ## 🔴 收什么、不收什么（2026-09-23 修正，用户原则）
>
> **只收：可公开的通用知识** —— 官方一手材料、公开方法论、可跨客户复用的行业常识、工具链。
> **不收（留在项目/私有区，`/mnt/d/Hermes-Workspace/01-Projects/` 与 `00-Records/`）**：
> **客户 / 合作方 / 实体信息**、**我方调研结论与商业判断**、方案报价交付记录、内部治理物（如《引用红线台账》）。
>
> **判据**：先问「**这是"知识"还是"我方私有信息"**」——私有信息一律不进库，哪怕它"换个客户也成立"。
> **实测教训**：曾把项目行业调研（16 篇）与合作方档案搬进本库并推上公开仓（远端为 public），已全部移出并清洗历史。
> 机制：`kb_sensitive_scan.py` 已挂进 pre-commit（提交时提示）；`pre-push` 守卫会阻断向公开仓的推送。

## 目录结构

```
Hermes-KnowledgeBase/
├── _private/         # 私有区（**gitignore，不上公开仓**）：内部过程产物 + 敏感词表真实名单
│   └── 00-Inbox/     #   周报（self-packaging-reports/）· 审计/流转报告（reports/）· 安全复盘（security/）
├── 01-Raw/           # 原始素材（抓取内容，未经整理）
│   ├── Bilibili/     # B站视频字幕 raw
│   ├── Xpertai/      # XpertAI 官方文档树（GBK 旧目录名已废弃）
│   ├── _meta/        # 非素材（模板/索引），不参与流转检查
│   └── *.md          # 网页文章 raw
├── 02-Draft/         # 清洗整理后，待审核的稿子
│   └── _archive/     # 已上 Wiki（promoted_to）或已退役（superseded_by）的草稿
├── 03-Wiki/          # 定稿知识
│   ├── Xpertai/03-官方文档/  # 产品官方文档直达区（旁路通道，附区域说明页）
│   └── Bilibili/*.md        # 自建知识
├── _design/          # 设计文档（_kb-*.md）
├── _backup/          # 旧版本/备份（词表 .bak 等）
├── _sensitive_terms.example.yaml  # 敏感词表**模板**（真实名单在 _private/，勿放仓内）
└── README.md / _keywords.yaml / _pending_merges.yaml
```

## 机制：三层门禁（2026-09-23 立）

> **原则：规范写在文档里 = 必然漂移。** 每条要长期守住的规矩，必须有「可执行检查」+「触发时机」。

| 层 | 时机 | 实现 |
|:---|:---|:---|
| 写入时 | 每写完一个文件 | 流程内跑 `kb_coverage_check.py --staged`（skill 强制步骤） |
| **提交时** | `git commit` | `.git/hooks/pre-commit`（已装，双向验证通过） |
| 周期 | 每周 | cron 全库体检 + 推送（待启用） |

检查项（C1–C7）与详细规矩见 `ingest-raw-to-draft` skill 的「机制优先原则」节；脚本在 `~/.hermes/skills/knowledge-base/ingest-raw-to-draft/scripts/kb_coverage_check.py`。**门禁上线必须双向验证**（造违规样本确认被拦 + 造合规样本确认放行）。

## 两条流转通道

| 通道 | 适用 | 记录要求 |
|:---|:---|:---|
| **编译通道** Raw → Draft → Wiki | 需要通化/重写的内容（视频、文章） | Draft 写 `sources`（可多条，多对一合并）；每条 Raw 回写 `time_draft` |
| **旁路通道** Raw → Wiki 直达 | 产品官方文档（如 Xpertai 文档树） | Wiki 写 `sources`；Raw 回写 `time_wiki` |

**字段职责**：`source:` = 描述性来源（人读）；`sources:` = 路径列表，相对 `01-Raw/`（机器读，供门禁与检索）。**禁止**把 URL / 裸 ID / 描述性文本塞进 `sources`。

## 覆盖度门禁（改完必跑）

```bash
python3 ~/.hermes/skills/knowledge-base/ingest-raw-to-draft/scripts/kb_coverage_check.py
```

- 阻塞项：C1 有 Raw 未流转｜C2 Draft 无来源且无溯源注｜C3 悬空来源引用
- 警告项：C4 未解析 wikilink（Obsidian 允许的「未来笔记」）
- `exit 0` 才算过。**改动流程见 `ingest-raw-to-draft` skill 的「溯源字段规范」与「迁移安全」两节。**

## 自动化工作流

### B站视频 ingestion
```
B站视频链接 → bilibili-subtitle skill → yt-dlp 下载音频 → Whisper GPU 转写 → 智谱 glm-4.5-flash 分块后处理（关推理）+ 二轮定向修正 → 01-Raw → ingest-raw-to-draft → 02-Draft
```

### 网页文章 ingestion
```
文章链接 → scrapling-ingest / Firecrawl → 01-Raw → ingest-raw-to-draft → 02-Draft
```

### 书籍文档本地化
```
源文件（DOCX/PDF/PPTX/MD）
    ↓ OPP v0.2.0（标准化 + manifest.json + 骨架保存）
Intermediate/*.md + *_manifest.json + *.skeleton.zip
    ↓ OL v0.2.0（翻译 + YAML frontmatter + XLIFF header notes）
Output/*_translated.md
```

**工具仓库**：
- [Omni Pre-Processor (OPP)](https://github.com/1StepMore/Omni_Pre_Processor) — v0.2.0：manifest.json 清单 + DOCX/PPTX 骨架 ZIP 保留
- [Omni Localizer (OL)](https://github.com/1StepMore/Omni_Localizer) — v0.2.0：YAML frontmatter 元数据头 + XLIFF `<note from="OL">` CAT 工具兼容

**本地化项目**：`/mnt/d/Hermes-Workspace/01-Projects/book-localization/`

## 相关 Skills

- `bilibili-subtitle` — B站视频全自动 ingestion pipeline
- `whisper-postprocess` — Whisper 无标点 → 带标点文本
- `scrapling-ingest` — 反爬网页抓取
- `ingest-raw-to-draft` — raw → 结构化 wiki draft

详见: `~/.hermes/skills/knowledge-base/`

## 贡献指南

1. 抓取的内容先入 `01-Raw/`
2. 整理后入 `02-Draft/`，等待审核
3. 审核通过后移入 `03-Wiki/`

---

## 🔎 检索（所有 profile 共用）

```bash
python3 _tools/kb_search.py "关键词"        # 默认 Wiki + Draft
python3 _tools/kb_search.py "词" --raw      # 含素材层
python3 _tools/kb_search.py "词" --json     # 机器读
python3 _tools/kb_search.py --selftest      # 自检
```
规范见 `_tools/检索规范.md`（触发规则 / 打分 / 效率与鲁棒性 / 维护）。
索引 `_index/` 为派生文件（不进 git），写入后由 `kb_finalize.py` 自动打脏标记、下次查询自动重建。
