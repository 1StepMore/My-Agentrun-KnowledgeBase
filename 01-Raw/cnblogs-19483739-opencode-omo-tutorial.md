---
title: OpenCode + Oh My OpenCode 高级使用教程：掌握 ulw、ralph-loop 与高效玩法
keywords:
- OpenCode
- Oh-My-OpenCode
- prompt-engineering
- multi-agent-system
- workflow
- ulw
- long-running-agent
- Multi-Agent
state:
  phase: raw
  time_raw: '2026-06-13T00:00:00'
  time_draft: '2026-09-19T14:37:03'
  time_wiki: '2026-09-23T00:53:35'
source_url: https://www.cnblogs.com/gyc567/p/19483739
source_type: article
source_platform: cnblogs
author: gyc567
author_id: gyc567
publish_date: '2026-04-06'
fetch_date: '2026-06-13'
priority: 2
language: zh
notes: OpenCode + Oh My OpenCode 高级用法，含 ulw 超工作模式、ralph-loop 自动迭代、多代理团队配置。作者是前 IBM
  架构师，内容实操导向。
---
# OpenCode + Oh My OpenCode 高级使用教程：掌握 ulw、ralph-loop 与高效玩法

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

# [OpenCode + Oh My OpenCode 高级使用教程：掌握 ulw、ralph-loop 与高效玩法](https://www.cnblogs.com/gyc567/p/19483739)

**Author:** gyc567 (Eric, ex-IBM architect)
**Focus:** Advanced prompt engineering for OpenCode + Oh My OpenCode (OMO) multi-agent team, assuming basic setup is complete.

## Overview & Prerequisites
- **OpenCode:** Terminal AI coding assistant (supports Claude, Gemini, GPT, GLM, etc.)
- **Oh My OpenCode (OMO):** Plugin upgrading single models into multi-agent teams (`oracle` architect, `librarian` codebase expert, `frontend`, `backend`, etc.)
- **Prerequisite:** Installation and basic configuration completed.

## 1. Basic Commands Refresher

| Command | Effect |
|---|---|
| `/edit <file>` | Precision editing |
| `/run <command>` | Execute terminal commands |
| `/test` | Run test suite |
| `/undo` | Undo last change |
| `/clear` | Clear context |
| `/diff` | View recent changes |

---

## 2. Core Advanced Prompt Mechanics

### 2.1 `ulw` (UltraWork Mode) — The All-Purpose Powerhouse

**Core Mechanism:** Automatically activates multi-agent parallelism (oracle planning → librarian analysis → specialist implementation), deep toolchains (LSP static analysis, AST parsing, MCP multi-file context), intelligent task splitting, and auto-validation.

> **Why it's strong:**  
> *"普通提示是单模型线性思考，容易遗漏边缘 case 或与现有代码冲突。ulw 开启多代理并行，librarian 会持续引用项目历史，oracle 会提前识别风险，整体质量和速度提升 **3-5 倍**。"*

**Usage Examples:**
- **General Feature:**
  ```
  ulw 请实现用户认证系统：注册、登录、JWT、刷新令牌、权限控制，集成到现有 Express 项目。
  ```
- **Role-Based Priority:**
  ```
  ulw UI 部分优先交给视觉/交互专家，优先级最高；后端逻辑交给 backend 代理；整体架构先让 oracle 评审。
  ```
- **Deep Codebase Refactor:**
  ```
  ulw 先全面分析整个代码库的现有模式和痛点，再重构所有 API 路由为 RESTful 标准，消除重复代码。
  ```
- **New Project Scaffold:**
  ```
  ulw 创建一个完整的 SaaS 模板：Next.js 14 App Router + Prisma + PostgreSQL + NextAuth + Tailwind + Shadcn/ui，支持多租户和订阅支付（Stripe）。
  ```
- **Toolchain Integration:**
  ```
  ulw 先运行 npm test 收集失败案例，再针对性修复所有单元测试和集成测试，确保覆盖率 >90%。
  ```

**Usage Guidelines:**
- ✅ **Use `ulw` for:** Medium-to-large tasks (new features, refactoring, cross-module work)
- ❌ **Skip `ulw` for:** Small tasks (modifying a single component)
- ⚠️ **Token Cost:** Increases 2-4x. Reserve expensive models (e.g., Sonnet) for critical agents.

---

### 2.2 `ralph-loop` (Autonomous Infinite Iteration Loop) — The Ultimate Perfection Loop

**Core Mechanism:** AI repeatedly executes → self-checks → fixes → re-executes until a condition is met. Ideal for "death-grip" quality scenarios.

**Syntax:**
```
/ralph-loop "任务描述（建议先加 ulw 增强）" --max-iterations N --completion-promise "停止条件"
```

**Parameter Breakdown:**
- `--max-iterations`: Safety valve (recommended: 10-30)
- `--completion-promise`: **Critical!** Must be a precisely detectable phrase in the AI output

**Practical Examples:**

| Scenario | Full Command |
|---|---|
| **Bug Fixing** | `ulw /ralph-loop "修复所有已知的生产 bug（参考 ISSUE 列表），所有测试必须通过" --max-iterations 20 --completion-promise "所有测试通过且无新错误"` |
| **Performance** | `ulw /ralph-loop "优化首页加载时间到 <1.5s（Lighthouse 分数 >95）" --max-iterations 25 --completion-promise "Lighthouse 性能分 >95"` |
| **Large Migration** | `ulw /ralph-loop "将整个项目从 Redux 迁移到 Zustand，所有功能保持一致" --max-iterations 30 --completion-promise "所有 e2e 测试通过且无状态丢失"` |
| **Algorithm Challenge** | `ulw /ralph-loop "实现一个 O(n log n) 的顶部 K 频繁元素算法" --max-iterations 15 --completion-promise "所有测试用例通过"` |

**Advanced Play:**
- **Nested loop:** `ulw` for planning → `ralph-loop` for execution
- **Intervention:** `Ctrl+C` to halt, adjust prompt, then restart
- **Real-time checking:** Let the loop auto-run `/run npm run build` between iterations

**Risk Control:**
- Test with small iterations first (`--max-iterations 5`)
- Keep `completion-promise` precise to avoid infinite loops
- Monitor token consumption closely

---

### 2.3 Other Advanced Prompt Techniques

- **Role Directives:**
  ```
  @oracle 请先设计整体微服务架构图和数据库 schema
  @librarian 请搜索项目中所有与支付相关的代码，总结现有逻辑和潜在风险
  @frontend 请实现一个现代的响应式侧边栏，支持折叠和动态路由
  ```

- **Background Parallel Tasks** (non-blocking):
  ```
  ulw background: 持续监控代码库变化，自动生成更新后的架构文档
  ulw background: 分析所有第三方依赖，列出过时/有安全漏洞的包并建议升级路径
  ```

- **Chain Tasks (Staged Execution):**
  ```
  ulw 第一阶段：只规划和输出详细实现计划（不修改代码）
  ulw 第二阶段：根据计划逐步实现，每步完成后等待我确认
  ```

- **Forced Thinking Chain:**
  ```
  请严格遵守：1. 先全面分析现有代码 2. 输出详细计划 3. 分步执行 4. 每步完成后运行测试验证
  ```

- **Multi-Model Optimization** (`oh-my-opencode.json` config):
  - `oracle` → Claude-3.5-Sonnet (strong reasoning)
  - `librarian` → Gemini-1.5-Pro (ultra-long context)
  - `code generation` → GPT-4o or o1 (speed)

---

## 3. Efficient Use Cases & Scenarios

- **Daily Code Review:**
  ```
  ulw 审查昨天的所有 git commit，指出潜在 bug、性能问题、风格不一致，并自动修复低风险项
  ```
- **Auto Documentation Sync:**
  ```
  ulw 每次代码变更后，自动更新 README、API 文档、架构图（用 mermaid）
  ```
- **Exploratory R&D:**
  ```
  ulw 并行探索三种技术方案：A. 使用 tRPC  B. 使用 GraphQL  C. 使用 REST + Zod，请分别实现最小可运行原型并对比优劣
  ```
- **Bulk Component Generation:**
  ```
  ulw 参考设计稿，生成 5 个可复用的 Dashboard 组件：数据卡片、趋势图、数据表、筛选器、导出按钮。含 TypeScript 类型、Storybook stories、单元测试。
  ```

---

## 4. Real-World Engineering Practices

### 4.1 Large-Scale Refactoring

```
ulw /ralph-loop "重构项目目录结构为领域驱动设计（DDD）
- 按 domain 组织：order、payment、user、notification
- 每个 domain 含：controller、service、repository、dto
- 保留所有现有功能，全部测试通过"
```

### 4.2 Integration Testing Matrix

```
ulw 为支付模块编写全面的集成测试矩阵：信用卡、支付宝、微信支付、国际卡、退款、超时、网络异常；确保覆盖率 >95%
```

### 4.3 Legacy Migration

```
ulw 设计从 jQuery + PHP 到 React + Node.js 的渐进式迁移计划，保持站点一直可用；分五阶段：包裹、替换、迁移、优化、清理
```

---

## 5. Tips

- **Training Data:** OpenCode 团队发布的高级 prompt 技巧教程
- **Contribution:** GitHub repo: `gyc567/openocode-playbook`
- **License:** MIT

## 核心摘录

- `ulw` = UltraWork Mode，开启多代理并行，效果提升 3-5 倍，但 token 消耗增加 2-4 倍
- `ralph-loop` = 自动迭代循环，用 `--completion-promise` 控制停止条件，建议先小迭代测试
- 多代理角色：`@oracle` 架构师、`@librarian` 代码库专家、`@frontend`/`@backend` 专岗
- 链式任务：`ulw 第一阶段` → 确认 → `ulw 第二阶段` 逐步推进
- 嵌套玩法：`ulw` 规划 + `ralph-loop` 执行

## 个人解读

（待消化）

## 待验证

- OpenCode 是否已原生支持 OMO 插件？需确认 opencode 版本兼容性
- ulw 在 code profile 中是否可复用相似模式？
- `ralph-loop` 的 `--completion-promise` 在中文输出中是否可靠匹配？
