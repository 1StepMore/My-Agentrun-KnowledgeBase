---
title: 龙虾之父说的 loops 到底能干嘛？
source: Bilibili/bilibili-BV18oJV6gEeY-openclaw-loops-explained.md
related: []
keywords:
- agentic-loop
- AI-Agent
- Claude
- ai-coding
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
  time_wiki: '2026-07-01T12:42:24'
sources:
- Bilibili/bilibili-BV18oJV6gEeY-openclaw-loops-explained.md
---
# 龙虾之父说的 loops 到底能干嘛？

## 核心知识点

### **Loops 工作流自动化**
Loops 是一种自动化工作流，通过 [[Agent]] 链式处理 [[Issue]]，从任务板的日志队列开始，自动完成筛选、实现、验证和提交 [[Pull Request]]，极大减少人工介入。

### **Agent 自动处理流程**
每个 Agent 负责特定环节：首先自动 [[Triage]] 新 issue，然后另一个 Agent 实现功能并使用自动化测试或 [[Computer Use]] 验证，最后 PR 交给人审查。将开发者从每个步骤的瓶颈中解放出来。

### **自动化配置（CodexApp）**
在 [[CodexApp]] 的 Automations 界面中，用户可以用自然语言创建规则。例如监听 "ready for agent" 标签，自动抓取 issue 并启动实现流程，实现一键触发。

### **Plan 递进模式**
支持从高层计划逐层细化：一个 Agent 编写 [[Spec]] 文档，另一个 Agent 根据 Spec 实现代码。通过 "plan from plan" 让 Agent 处理规划和实现两层工作，即“两层懒人因子”。

### **Computer Use 功能**
Agent 利用 [[Computer Use]] 操作图形界面，特别适合 UI 变更。这使 Agent 能够在实际应用中点击和验证，确保前端改动符合预期，提升自动化可靠性。

### **开源 Spec 模板**
可以下载开源项目（如 [[Warp]] 终端）的 Spec 文档作为参考，快速构建自己的 [[Skills]]，指导 Agent 生成符合团队标准的规划与实现规范。

## 总结
Loops 通过多级 Agent 自动化串联，将 issue 从创建到 PR 的大部分环节自动化，显著减少人为干预。用户可利用 CodexApp 灵活配置规则，并借助 Computer Use 与计划递进模式实现端到端的智能开发工作流。
