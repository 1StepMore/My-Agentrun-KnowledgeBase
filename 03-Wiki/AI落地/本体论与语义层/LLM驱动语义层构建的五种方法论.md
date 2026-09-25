---
title: LLM驱动语义层构建的五种方法论
source_url: https://www.bilibili.com/video/BV1UbL46wEwm/
source_type: video
source_platform: bilibili
author: 零点未来
author_id: ''
publish_date: '2026-06-28'
fetch_date: '2026-06-28'
notes: Whisper small 转写 + DeepSeek V4 Flash (opencode CLI) 后处理。视频时长约12:45。Palantir
  Ontology 三部曲之二。
priority: 4
language: zh
duration_seconds: 766
duration_formatted: '12:45'
keywords:
- semantic-layer
- LLM
- knowledge-graph
- ontology-construction
- RAG
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
  time_wiki: '2026-07-01T12:42:24'
sources:
- Bilibili/bilibili-BV1UbL46wEwm-llm-driven-ontology-building-12min.md
source: 历史文件，来源见 sources
evidence: E1
---
# 12分钟学习LLM驱动Ontology构建

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | 12分钟学习LLM驱动Ontology构建 |
| 作者 | 零点未来 |
| 时长 | 12:45 |

## 原文内容

> DeepSeek V4 Flash 后处理，已修正专有名词和断句。

### 为什么需要 Ontology

没有 Ontology 的世界：你问 AI"供应商 A 的评分是多少"，AI 今天回答 85，明天回答 92，后天回答 78。AI 不是在骗你，而是根本不知道供应商、评分、日期这三件事有什么关系。

Ontology 就是一张**知识地图**：不只是告诉 AI 有哪些数据，还告诉他这些数据之间有什么关系、遵守什么规则。有了地图，AI 才能从随机猜测变成有据可查。

### LLM 构建 Ontology 的四道坎

1. **类型未知**：开始前不知道领域里有多少种实体类型
2. **幻觉输出**：LLM 可能创造出原始数据中没有的概念
3. **粒度控制**：关系太宽泛没用，太细没人维护
4. **评估困难**：Ontology 没有标准答案，没有对错之分

### 五种流派

#### 1. 拆解派
把大任务拆成小任务：提取实体 → 提取关系 → 去重 → 归一 → 验证 → 存图。每步用最合适的工具。
- **关键设计**：双重验证闭环——结构验证 + 逻辑验证，通不过的只留日志不污染知识库
- **案例**：法国电力 EDF 管理核电站技术文档；Wingtonic 构建知识图谱
- **评价**：工程量最大，但上生产系统最可靠

#### 2. 聚类派
先不定义有什么东西，让数据自己说话。提取名词 → BERT 向量化 → AP 密度聚类（不用 K-Means，因为不知道有几类）→ LLM 命名。
- **代表性论文**：LLM for Ontology（2025）
- **评价**：数据驱动、幻觉风险低；但聚类质量直接影响结果，开放域场景粒度可能过细
- **适合**：探索全新领域，不知道有什么类型时

#### 3. 两步走派
先让 LLM 提取概念清单，再整理成层次结构，最后序列化标准格式。
- **代表性论文**：Onto1KG
- **评价**：中间产物可审查可调整，适合快速出 Demo
- **比喻**：先列提纲，再组织章节

#### 4. 框架派
基于已有框架（如 WikiData，几亿实体），定义好可以有什么类型和关系，让 LLM 在框框内提取，不能乱发明。
- **评价**：减少幻觉，输出天然符合共识。适合医疗、法律、电力等有标准规范的行业

#### 5. 直给派
端到端 Prompt：设计一个 prompt 让 LLM 直接从文本输出 Ontology。
- **评价**：最快（半小时出结果），但幻觉风险最高、输出不稳定、prompt 极度敏感
- **适合**：快速验证想法，不适合生产

### 选择框架

| 场景 | 选哪个 |
|------|--------|
| 快速 POC 验证 | 直给派 |
| 探索全新领域 | 聚类派 |
| 有行业标准 | 框架派 |
| 生产系统不能出错 | 拆解派 + 双重验证 |

### 实战教训

- **大部分错误发生在第一步（实体提取）**：类型标错、关系错误、别名混在一起，一路传导越滚越多。宁可在第一步多花功夫
- **Prompt 措辞极度敏感**：同一个 LLM，换了几个词生成的结构完全不同。用结构化模板代替自然语言能大幅减少波动
- **数据不是越多越好**：Wingtonic 用了不到 1000 Token 就建立了有效的知识图谱。关键是数据质量和约束合理性

### 作者的工具：OntoPrompt

基于直给派 + 约束规则构建的 Ontology 构建小工具：
- 概览、本体管理、提示词管理、模型管理、设置
- 支持供应链/财务/营销等不同业务域的 prompt 模板
- 支持 Word、Markdown、CSV 等多种文件类型
- 可视化知识图谱展示（层级/圆型布局）
- 支持添加/编辑实体、查看属性/关联实体/逻辑规则

## 抓取备注

- 零点未来 Palantir Ontology 三部曲之二
- 核心价值：五种构建流派的方法论，从实践层面分类
- 验证闭环设计是拆解派的关键工程决策
