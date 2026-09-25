---
title: 循环工程 Loop Engineering
keywords:
- ai-coding
- agentic-loop
- AI-Agent
- automation
state:
  phase: draft-archived
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
source: https://www.bilibili.com/video/BV1S6EY6fEUc
sources:
- Bilibili/bilibili-BV1S6EY6fEUc-loop-engineering-next-paradigm.md
related: []
promoted_to: '[[循环工程-Loop-Engineering]]'
---
# 循环工程 (Loop Engineering)

## 核心概念

- **[[循环工程]]**：设计一个系统，让系统自己代替你 Prompt Coding Agent。你定义目标，AI 自己迭代直到完成。
- **[[Coding Agent]]**：原来人工编写 Prompt，现在由循环系统自动调度 Agent 完成任务。
- **[[Harness]]**：单个 Agent 的运行环境，循环工程在其之上。
- **[[状态]]**：循环的第六个组件，通过 Markdown 文件或看板记录进度和成果，弥补模型遗忘。

## 关键洞察

- **角色转变**：从“手动 Prompt 的司机”变为“设计自动化系统的人”。
- **循环的六要素**：
  1. **自动化触发**：定时任务，无需手动（如每日扫 CI 失败和 Issue）。
  2. **并行 Agent**：多个 Agent 各自在独立分支工作，互不干扰。
  3. **技能文件**：显式记录项目规范、构建步骤等，让 Agent 不用每次都猜。
  4. **插件与连接器**：允许 Agent 读 Jira、Slack、API，实现自动开 PR、更新工单。
  5. **分离审查**：一个 Agent 写代码，另一个审查代码，避免自我审查松懈。
  6. **状态记录**：持久化哪步完成、哪步失败，使循环可以接续昨日进度。
- **工具成熟**：过去需 Bash 脚本搭建，现在 Codex 和 Cloud Code 已内置组件，直接设计循环即可。
- **完整示例**：每日自动任务读取 CI 失败与 Issue → 生成清单 → 每个问题派 Agent 写修复 → 另一 Agent 审查 → 成功则开 PR、更新工单、通知频道 → 失败入人工列表。全部通过状态文件连接。
- **三大恶化问题**：
  - **验证**：循环快速犯错时缺少监督，“做完了”不是证明。
  - **理解债务**：自动产出代码增多，你的理解减少。
  - **认知投降**：人停止思考，被动接受结果，失去判断力。

## 实践指南

- 把项目规矩写成“技能文件”，让 Agent 每次遵循，减少猜测。
- 利用独立分支机制，让多个 Agent 并行工作而不冲突。
- 必须维护状态文件或看板，作为循环的持久记忆。
- 始终设置独立的验证 Agent（如代码审查），提升输出质量。
- 提醒自己：循环工程比 Prompt 工程更难，保持对系统的理解和掌控，像工程师一样造循环，而非单纯按按钮。

## 总结

循环工程是 AI 编程的下一个范式，从手动 Prompt 升级为自动化系统设计。它降低了操作门槛，却放大了验证、理解债务和认知投降的风险。要持续握着方向盘，以工程师身份主动设计循环，而非被动接受其输出。
