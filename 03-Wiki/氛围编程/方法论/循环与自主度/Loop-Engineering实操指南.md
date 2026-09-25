---
title: Loop Engineering实操指南
source: https://www.bilibili.com/video/BV1zYEz6oEx7
related:
- Prompt Engineering
- Agentic Workflow
- 测试驱动开发
- 对抗验证
- 动态工作流
keywords:
- AI工程
- agentic-loop
- cursor
- cloud-code
- automation
- systems-engineering
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
  time_wiki: '2026-07-01T12:42:24'
sources:
- Bilibili/bilibili-BV1zYEz6oEx7-loop-engineering-practical-guide.md
---
# Loop Engineering实操指南

## 核心概念

- **[[Loop-Engineering]]**：一种取代手动提示编码代理的工程范式。通过设计递归的目标导向系统，让AI自动生成、测试、修复代码直到满足条件。人类不再参与每一步提示，但仍负责设定边界、验收标准和关键审查。

- **[[Loop-Until-Done]]**：最基础的模式，指定可验证的停止条件（如所有测试通过），系统在该闭环内反复纠正。

- **[[Goal指令]]**（Cloud Code）：每一轮操作后用独立的评估者模型检查目标是否达成。目标必须是可观察的最终状态（如“测试通过且Lint检查无误”）。

- **[[记忆持久化]]**：利用 `CLAUDE.md`（或 `AGENTS.md`）记录项目架构、历史陷阱，使AI在每轮循环开始时读取，避免重复错误。

- **[[动态工作流]]**：用纯JavaScript编写编排脚本，实现并发执行能力。典型模式包括 **Fan Out and Synthesize（发散与综合）** 和 **Adversarial Verification（对抗验证）**。

- **[[对抗验证]]**：引入审查Agent（Agent B）对代码生成Agent（Agent A）的输出进行审查，发现遗漏则打回重写，直到审查通过。

- **[[可组合的Agentic Workflow]]**：Anthropic总结的链式处理、路由、并行、编排、评估、优化等模式。Loop Engineering将这些模式组合成可验证、可停止、可回滚的工程系统。

- **[[负反馈]]**：香农信息论中的概念。Loop Engineering中的每次验证和自修正即为系统获取负反馈，将LLM的不确定性限制在可观察、可纠错、可回滚的边界内。

## 关键洞察

1. **本质是系统架构，而非简单循环**：Loop Engineering不是简单外层循环包API，而是对任务进行克制拆解，设计状态机、异常捕获、验证指标和状态流转。
2. **从Prompt Engineering到Loop Engineering是思维转变**：前者雕琢语言“哄骗”模型，后者是系统工程（文科生→理科生）。
3. **底层模型成熟是爆发前提**：Claude 5等模型具备强大的自我纠正能力，使人工介入成为性能瓶颈。
4. **工程师价值转移**：基础编码能力价值快速归零，系统分解与编排能力指数级上升。设计Loop的工程师成为自动化流水线的架构师。

## 实践指南

### 第一层：测试驱动与自我纠正（[[Cursor]]）

- 配置Agent的Run Mode为 `Run Anything` 或 `Auto Review`，赋予Agent执行终端命令、读写代码的能力。
- 提示词示例：“先写测试，再写代码，然后运行测试并更新代码，直到所有测试通过。”
- 自动流程：创建测试文件 → 写实现代码 → 运行 `npm test` → 读取失败日志 → 修改代码 → 重跑测试。
- 保护配置：在Command Palette添加 `npm test`、`npm run build`、`prettier`；开启File Deletion Protection。
- 日常使用 `Auto Review` 或 `Auto Review with Sandbox`，`Run Everything` 仅限Demo。

### 第二层：目标导向与记忆持久化（[[Cloud Code]]）

- 使用 **Goal指令**：写清可观察的最终状态（如“API的每个调用点都已迁移完毕且构建成功，20轮后停止”）。
- 避免不可验证目标（如“代码达到生产就绪”）。
- 利用 `CLAUDE.md` 持久化项目指令。若团队已有 `AGENTS.md`，可通过 `@AGENTS.md` 导入，确保每一轮AI不重复犯已知错误。

### 第三层：动态工作流与并发执行

- **动态工作流**：用JavaScript编写编排脚本，使用 `forEach` 等指令让Cloud自动创建子工作流。
- **Fan Out and Synthesize**：同时生成多个子Agent，分别执行爬财报、分析GitHub提交频率、爬用户评论等任务，最终合并节点汇总。
- **Adversarial Verification**：Agent A生成代码，Agent B持需求文档审查，缺点打回，直至无问题。
- **分层架构**：高级规划模型（如Claude Opus）负责决策，小模型（如Claude Haiku）负责具体修改，平衡效率与成本。

### 注意事项

- 避免将庞大模糊的任务直接丢入循环（如“写个电厂网站，报错就重试”），会造成Token浪费且无法收敛。
- 必须将复杂业务逻辑拆解成模型能力内确定性高的原子操作。
- 每次验证与自修正都是系统在获取负反馈，确保不确定性被控制在可观察、可纠错、可回滚的边界内。

## 总结

Loop Engineering是2026年硅谷前沿的工程范式，通过精心设计的循环系统让编码代理自动迭代，极大提升效率。从底层的测试驱动自纠正，到中层的目标导向与记忆持久化，再到高层的动态工作流与并发执行，工程师的角色从手动提示者转变为自动化流水线的架构师。

**未来演进**：
1. **基础设施爆发**：出现专门针对Agent的编排框架，封装重试、状态回滚、并行控制。
2. **从静态Loop到动态Loop**：系统根据任务复杂度在运行时动态生成最优Loop拓扑（简单bug单线修复，重构自动展成锦标赛模式）。
3. **对本地算力和SLM（小语言模型）**的需求提升，推动更轻量的自纠正体系。
