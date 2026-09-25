---
title: 如何写好一个Skill：核心原则与进阶技巧
keywords:
- Skill
- writing-principles
- advanced-techniques
- progressive-disclosure
- Claude
state:
  phase: draft-archived
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
sources:
- Bilibili/bilibili-BV1aVA5zDEXY-how-to-write-a-skill-part2.md
related: []
promoted_to: '[[如何写好Skill-原则与技巧]]'
---
# 如何写好一个Skill：核心原则与进阶技巧

> 来源：Bilibili视频 | BV1aVA5zDEXY | 发布：2026-04-08 | 时长：10:17

## 概述

本视频是"写好Skill"专题的第二部分。在了解Skills是什么、有哪些类型之后，作者分享了写好Skill的**四条核心原则**和**四个进阶技巧**，以及运营、度量方面的经验。

---

## 四条核心编写原则

### 1. 不要陈述显而易见的事

Claude本身已经非常了解代码库和编程知识，Skill应该聚焦于让它跳出常规思维的信息。

好的Skill不是教Claude它已经知道的事，而是**纠正它的默认偏好**。作者举了一个生动的例子：Front and Design这个Skill，是Anthropic工程师在和客户反复迭代中打磨出来的，专门帮Claude避免千篇一律的Inter字体和紫色渐变这些"AI味"设计。

### 2. 建立Gotchas章节

Gotchas是Skill中**最高价值的内容**。Gotchas就是Claude在使用该Skill时常常犯的错误，把这些坑记录下来，持续迭代更新。

核心思想：Skill不是写完就完了，而是一个**随着使用不断进化的活文档**。

### 3. 利用文件系统与渐进式披露

Skill是"文件夹"，不只是Markdown。你应该：
- 把API文档拆分到`References/API.MD`
- 模板文件放在`Assets`目录
- 还可以包含参考代码和脚本

关键在于告诉Claude这些文件在哪儿，它会在适当的时机自己去读取。这就是**渐进式披露**的精髓：不是一股脑把所有信息塞给模型，而是让它**按需获取**。

### 4. 避免过度约束Claude

给它信息和灵活性，但不要硬编码指令。因为Claude是高度可适配的，如果指令太具体，反而限制了它适应不同场景的能力。

---

## 四个进阶技巧

### 1. 配置与初始化

有些Skill需要用户提供上下文才能运行。比如一个发Slack占位消息的Skill，需要知道发到哪个频道。

推荐的模式是用`config.json`文件存储配置信息。如果未配置，Agent会自动询问用户。如果需要结构化的选项，还可以让Claude使用`AskUserQuestion`工具来展示多选菜单。

### 2. 记忆与数据存储

Skill可以拥有自己的记忆。存储形式可以很简单（追加写入的文本日志或JSON文件），也可以复杂到用SQLite数据库。

举例：`StandupPost`这个Skill会保存`standups.log`文件，每次运行时Claude会读取自己的历史记录，从而知道上次都写了什么、有什么变化。

**注意**：Skill目录下的数据在升级时可能被删除，应该使用`Claude Data Sampler and STIO`这个稳定路径来存储持久化数据。

### 3. Description字段是写给模型的

当Claude Code启动时，会扫描所有可用Skill的描述，来决定这个请求有没有对应的Skill。所以**Description不是摘要，而是触发条件**。写好描述就等于实现了精准触发。

### 4. 存储脚本与生成代码

你能给Claude的最强大工具就是代码。给它现成的脚本和函数库，Claude就可以把精力花在**组合**上——决定下一步做什么，而不是重建样板代码。

Claude还可以按需生成脚本来完成更高级的分析任务，比如回答"周二发生了什么"这样的问题。

---

## 按需Hooks

Skills可以注册临时生效的钩子。比如：
- `Careful`：阻止危险操作
- `Freeze`：限制编辑范围

只在需要时启用，用完即止。核心思想：**不是所有约束都要全局生效**。

---

## 分发策略

两种方式：

1. **小团队**：直接提交到代码仓库的`Claude Skills`目录
2. **大规模团队**：用插件市场，用户自主选择安装

**注意**：每个仓库及Skill都会增加上下文开销，规模大了建议走市场分发。

---

## 运营相关话题

### 市场管理

- Anthropic内部没有集中管控，靠有机发现
- 先在沙盒试用，积累用户后再提交正式市场
- 要注意避免低质量和冗余
- 组合Skills目前没有原生依赖系统，按名称引用即可，模型会自动调用已安装的Skill

### 度量

通过Hooks记录使用日志，分析：
- 哪些Skills最受欢迎
- 哪些触发不足

**核心经验**：完整的生命周期是**创建 → 迭代 → 分发 → 度量 → 优化**，是一个持续循环的闭环。

---

## 总结

Skills是极其强大且灵活的Agent工具，需要大家打开脑洞、不断探索。四点核心建议：

1. **动手开始，从简单做起**，不要追求一步到位。大多数Skills从几行文字和一个Gotcha就开始了
2. **持续迭代**，遇到问题就更新Skills
3. **关注Gotchas**，这是最高价值的内容
4. **善用文件系统**，不要把所有东西塞进一个文件

Anthropic自身的经验也印证了这一点。他们的Skills都是从简单开始，随着Claude遇到新的边界情况而不断完善的，**没有一个Skill是一开始就完美的**。

> 最好的理解方式就是亲自尝试。与其纠结于理论，不如今天就动手写你的第一个Skill，从一个小场景切入，持续迭代，让实践来验证效果。

---

## 相关概念

- Skill设计模式
- Agent
- Prompt Engineering
- Progressive Disclosure
- Gotchas
- Hooks

## 相关资源

- Claude Code
- Anthropic官方Skill开发指南
