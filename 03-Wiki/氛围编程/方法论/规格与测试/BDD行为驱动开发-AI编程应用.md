---
title: BDD行为驱动开发-AI编程应用
keywords:
- ai-coding
- methodology
- LLM
- workflow
- prompt-engineering
state:
  phase: wiki
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
  time_wiki: '2026-07-01T12:47:26'
source: Bilibili/bilibili-BV1guRwB4Ejm-bdd-precise-requirements.md
sources:
- Bilibili/bilibili-BV1guRwB4Ejm-bdd-precise-requirements.md
---
# BDD行为驱动开发-AI编程应用
## 核心知识点

### **BDD（行为驱动开发）的定义与公式**
BDD（Behavior Driven Development）是一种用自然语言描述软件预期行为的开发方法，核心公式为 [[Given-When-Then]]：给定上下文（Given），当操作发生（When），应得到结果（Then）。它面向人而非代码，让非技术人员也能精确描述需求，例如「棋盘上吸血鬼剩1血，攻击敌将后应回血2点」。

### **BDD 与 TDD 的对比 （表格）**

| 对比维度 | BDD | TDD |
| --- | --- | --- |
| 语言形式 | 自然语言（人话） | 代码（单元测试） |
| 核心关注 | 行为是否符合需求 | 逻辑是否正确无 Bug |
| 沟通对象 | 产品、测试、开发者、AI | 开发者 |
| 产出时机 | 需求描述阶段 | 编码之前 |
| 在 AI 中的优势 | 消除需求歧义 | 保证修改后不引入 Bug |

### **BDD 在 AI 编程中的新价值**
AI 可以秒级生成大量 [[Given-When-Then]] 用例，低成本的精确沟通使得 AI 产出的功能更严格符合用户预期。{{Video}} 指出，传统写大作文式 PRD 对 AI 充满歧义，而 BDD 用例经确认后几乎没有可自由发挥的空间，转译为代码也非常简单。

### **TDD + BDD 双保险**
单独使用 [[TDD]] 能防 Bug 但无法保证功能符合预期；单独使用 [[BDD]] 能精确描述需求却难防编码 Bug。两者结合构成约束 [[AI 编程]] 的双保险：TDD 确保代码逻辑正确，BDD 确保最终行为正是用户想要的。

## 总结
视频介绍了 BDD（行为驱动开发）及其 Given-When-Then 公式，强调它比 TDD 更擅长用自然语言消除需求歧义。在 AI 时代，BDD 低成本的用例生成让沟通变得极其精确，与 TDD 配合可形成双保险，既防止 AI 写出 Bug，也防止做出不符合要求的功能。
