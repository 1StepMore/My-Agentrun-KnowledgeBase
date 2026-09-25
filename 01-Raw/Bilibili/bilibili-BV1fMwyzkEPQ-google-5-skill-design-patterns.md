---
title: Google总结了5种Skill设计模式，让Agent稳定输出
keywords:
- Skill
- Agent
- prompt-engineering
- workflow
- AI
- skill-design-patterns
- Harness
state:
  phase: raw
  time_raw: '2026-05-14T00:00:00'
  time_draft: '2026-09-19T14:37:03'
  time_wiki: '2026-09-23T00:53:35'
source_url: https://www.bilibili.com/video/BV1fMwyzkEPQ/
source_type: video
source_platform: bilibili
author: 慢学AI
publish_date: '2026-03-19'
fetch_date: '2026-05-14'
priority: 3
language: zh
notes: 使用 Whisper (openai-whisper small, WSL GPU, fp16=False) 转写 + MiniMax 后处理。视频时长7分18秒。
duration_seconds: 438
duration_formatted: '7:18'
author_id: ''
---
# Google总结了5种Skill设计模式，让Agent稳定输出

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | Google总结了5种Skill设计模式，让Agent稳定输出 |
| 作者 | 慢学AI |
| 发布时间 | 2026-03-19 |
| 总时长 | 7分18秒 |
| BV号 | BV1fMwyzkEPQ |

## 原文内容

<think>
用户需要我对这段B站视频字幕文本进行优化，要求：
1. 精准断句，加逗号、句号、顿号等中文标点
2. 合理分段，按话题/章节分组
3. 修正明显的语音识别错误，保留专业术语
4. 保持口语化风格
5. 直接输出纯文本，不加任何标记

让我逐段分析并优化：

原文本主要是关于Google Cloud Tech团队发布的关于Agent Skill设计模式的博客内容。

我需要：
1. 修正明显的语音识别错误，比如：
   - "skill打好了skill.md" -> "Skill写好了，Skill.md也写了"
   - "答片" -> "答案"
   - "entropic,versal" -> 可能是公司名，保留
   - "C进" -> "塞进"
   - "react" -> React（技术术语保留）
   - "fast API" -> FastAPI
   - "CQ查询" -> SQL查询？或者是特定术语，保留
   - "Api" -> API
   - "docksdream" -> docs？或者保留
   - "PASSEN風格審查" -> 可能是特定术语
   - "OWASP" -> OWASP（安全术语）
   - "拍盘来" -> "Pipeline"
   - "漏步軸" -> "漏步骤"
   - "自信的答片" -> "自信地答错"
   - "知識什麼時候加載" -> "知识什么时候加载"
   - "输出结构总是不稳定" -> 这部分已经是正确的
   - "Generator" -> 保留英文
   - "Reviewer" -> 保留英文
   - "Inversion" -> 保留英文
   - "Pipeline" -> 保留英文

现在让我重新整理文本，确保流畅性和准确性，同时保持原有的技术术语和口语化风格。

首先处理开场的常见问题。用户描述了一个典型场景：Skill已经写好，但Agent使用时仍然输出不稳定，经常出现格式混乱、遗漏步骤或自信地给出错误答案的情况。

接着介绍Google Cloud Tech团队发布的关于Agent Skill设计模式的文章。他们指出问题的根源不在于格式本身——因为主流Agent工具已经逐渐统一了Skill.md的格式规范——而是在于内容设计层面，即Skill中逻辑的组织方式。通过研究Entropic、V ersal和Google内部的Skill构建方法，总结出五种关键的设计模式。这些模式分别针对Agent最常见的失控点：知识何时加载、结构输出不稳定、审查标准和流程混杂、信息不足就匆忙行动，以及复杂任务中步骤遗漏。

第一种是Tool Wrapper，用来解决知识注入时机的问题。常见做法是提前把所有技术规范塞进System Prompt，比如React规范、FastAPI规范、团队约定和命名规则。但这样做的缺点是大部分任务实际上不需要这些信息，反而浪费了Context空间。

更好的方式是用Tool Wrapper来管理这些内容，让模型只在相关领域被激活时才加载对应的知识。

另一种模式是Generator，用来解决输出结构不一致的问题。如果没有预设模板，模型每次都会重新决定输出格式，导致结果不稳定。Generator通过固定输出模板和风格指南来解决这个问题，让Skill只负责补充缺失的内容和填充框架。

模板定义"要产出什么"，风格指南定义"怎么写"，这样不同人、不同时间触发的输出都能保持一致。这套方案特别适合API文档、文档标准化报告、Commit Message和Changelog生成等场景。

第三个模式是Reviewer，用来解决审查任务经常返工的问题。很多团队把"检查什么"和"怎么检查"混在一起，Reviewer模式要求明确分离这两部分。Checklist定义要检查的内容，Skill.md定义具体的检查方法，这样规则可以随时更换。比如从代码风格审查切换到安全审查时，只需要替换Checklist，而不需要重写整个Skill。

最后输出统一成Error、Warning、Info三个级别，让使用者清楚知道哪些必须修复、哪些建议修改、哪些只是提醒。

第四个模式是Inversion，这个最有实际感受。很多Agent存在"太爱猜"的问题——拿到模糊需求就急着生成，信息不足就自信地自己补全。Inversion的思路是反转流程，让Agent先向用户提问而不是直接输出。

它分为三个阶段：Discovery阶段确认要解决什么问题，Constraints阶段收集平台、技术栈、限制条件和交付要求，Synthesis阶段等所有信息齐全后才开始生成。比如规划客服机器人时，Agent应该先询问服务对象、接入渠道、订单系统对接、合规要求和人工接管机制等细节，在这些问题明确之前不允许开始写方案。这种模式通过门控指令确保信息完整才允许开工。

第五个是Pipeline，用来处理多步骤任务中容易跳步骤的问题。某些任务本身有强顺序依赖，比如先分析输入、生成中间产物、组装最终结果、最后验证。如果用单一Prompt处理，模型很容易中途偷懒。Pipeline的做法是把Skill.md写成明确的工作流定义，规定每一步做什么以及何时可以进入下一步，同时在关键节点设置门控。

比如文档生成场景，先解析公开API，再生成Docs确认，组装成完整文档，最后做质量检查。这样每步只加载当前需要的references和templates，保持Context干净。

选择哪种模式要看任务性质。如果Skill要产出内容且从模板产出，就用Generator；如果只是运行时加载某套知识，更像Tool Wrapper；如果评估已有输入，就是Reviewer；如果是澄清类任务，先补全信息。

这些模式可以叠加，Generator前面接澄清流程，Pipeline结尾接审查，Tool Wrapper几乎可以加在任何模式上补充知识。关键是不要把所有指令都塞进System Prompt，而要根据实际场景选择合适的结构化模式来判断是知识问题、结构问题、审查问题还是澄清问题。

模式选对了，Agent的稳定性才能真正提升。
</think>

你是不是也遇到这种情况？Skill写好了，Skill.md也写了，但Agent用了Skill输出还是不稳定，一会格式乱，一会漏步骤，一会又自信地答错。

本期我们读Google Cloud Tech团队的博客，5 Agent Skill Design Patterns Every ADK Developer Should Know。他们认为问题很少出在格式上，现在主流的Agent工具已经逐渐统一了Skill.md的格式规范。规范真正的，问题出在内容设计上，也就是Skill里面的逻辑究竟该怎么组织。

他们研究了Entropic、V ersal、Google内部的Skill构建方式，总结出五种设计模式。用对了，Skill的输出才能稳定有质量。这五种模式，对应的正式Agent最常遇到的两类失控点。

第一类，是知识什么时候加载，对应Tool Wrapper。第二类，是输出结构总是不稳定，对应Generator。第三类，是审查标准和审查流程混在一起，对应Reviewer。第四类，是信息不全，却急着开工，对应Inversion。第五类，是复杂任务容易跳步骤，对应Pipeline。

先看第一种，Tool Wrapper。它解决的是知识什么时候应该被交给Agent。很多人会把某个技术栈的全部规范提前塞进System Prompt，比如React规范、FastAPI规范、团队组建约定、命名规则，一次性全塞进去。问题是，大部分任务根本用不到这些东西。你平时在浪费Context，模型还更容易被无关知识干扰。

Tool Wrapper的做法，是把这些内容放进References。Skill只负责判断，现在这个任务是否进入了React领域，或者是否进入了数据库领域。只有判断命中，才加载那一套知识。你可以把它理解成，Skill像一个总闸门，负责在合适的时候把某个专家手册接近上下文。比如让Agent改一个React页面时，再加载References里的React规范。但如果当前任务只是写SQL查询，或者只是改一段产品文案，那份前端规范根本不出现。

所以Tool Wrapper的本质，就是按需注入知识。

第二种，Generator。它解决的是为什么同样让Agent写文档，今天长这样，明天又长成另一种样子。本质原因是模型每次都在现场重新决定这份输出该长什么样。Generator的答案很直接，别让它现场发挥。把输出结构固定在模板里，把表达方式固定在风格指南里。Skill.md负责做的是先补全缺失的量，再把内容填进去。所以模板回答的是What to produce，风格指南回答的是How to write。

比如你要让Agent产出API文档，模板规定必须有接口说明、参数表、返回值、错误码、示例调用。Style Guide规定标题格式数与统一、语气和自断命名。这样你今天写、明天写，不同人触发，出来的结构还是同一套。这就是为什么Generator特别适合API文档、文档标准化报告、Commit Message、Changelog生成。

第三种，Reviewer。它解决的是为什么你的审查任务经常要推倒重来。很多团队把两件事写混了，一件事是检查什么，另一件事是怎么检查。Reviewer模式要求你把这两件事硬拆开。检查什么？放进Checklist。怎么检查？留在Skill.md。这样一来，流程不动，规则可换。

比如你今天做代码风格审查，明天换成OWASP安全审查，后天又换成合规规则，你不需要为每一类审查重写一遍Skill，只需要替换不同的Checklist。最后输出统一成Error、Warning、Info这种层级。这样人一看就知道哪些必须修，哪些建议修，哪些只是提醒。

第四种，Inversion。这是我觉得最容易让人有实感的一种，因为很多Agent最大的问题是太爱猜。它一拿到一个模糊需求就急着开始生成，信息不够它就自己补，而且补得非常自信。Inversion的思路是把流程反过来，流程会变成Agent先发问，用户先回答。它通常会分成三个阶段。

第一阶段Discovery，先确认你到底要解决什么问题。第二阶段Constraints，把平台、技术栈、限制条件、交付要求问完整。第三阶段Synthesis，信息齐了之后才允许开始生成。

比如你让Agent规划一个客服机器人，它应该先问服务对象是谁？接入微信还是网页？要不要对接工单系统？有没有合规要求？有没有人工接管机制？这些没问清之前，禁止直接开始写方案。所以Inversion的关键是用门控指令，明确规定信息没齐，不准开工。

第五种，Pipeline。它解决的是多步骤任务为什么总有人跳步骤。有些任务本身就是一个强顺序流程，比如先分析输入，再生成中间产物，再组装最终结果，最后还要验证。如果你把这件事当成一句Prompt，模型很容易中途偷懒。Pipeline的做法是直接把Skill.md写成工作流定义，第一步做什么，第二步做什么，什么时候能进入下一步，全都写清楚。中间还要放Gate，也就是显式门控。

比如先解析公开API，再生成docs确认，确认之后再组装成完整文档，最后做质量检查。这一类模式特别适合文档生成、复杂代码修改、发布流程、合规流程，这种不能跳过验证的任务。因为它的价值不只是顺序清楚，还在于每一步只加载当前所需的references和templates，能让Context一直保持干净。

这五种模式讲完之后，最后一个问题就是到底该怎么选。这篇文章给了一个很实用的判断路径：

先问这个Skill是否要产出内容？不过要，而且是从模板里产出，那通常就是Generator。如果要产出，但本质只是运行时加载某一套知识，那更像Tool Wrapper。如果这个Skill是在评估已有输入，那通常是Reviewer。如果它在开始之前必须先向用户补全信息，那就是Inversion。如果它还有严格步骤确认点，不能跳过的门，那就是Pipeline。

这些模式之间可以互相叠加。Generator前面可以接Inversion，Pipeline结尾可以接Reviewer，Tool Wrapper几乎可以叠在任何模式上，负责补知识。

最后总结一下，别把越来越复杂的指令一股脑塞进同一个System Prompt。真正可靠的Skill靠的是更合适的结构，你要先判断自己遇到的是知识问题、结构问题、审查问题、澄清问题还是流程问题。模式选对了，Agent才会稳定。

## 核心摘录

（在这里记录你阅读时的重点摘录）

## 个人解读

（在这里写下你的理解和思考）

## 待验证点

（记录文章中需要查证的信息）

---

## 抓取备注

- 抓取时间：2026-05-14
- 抓取工具：yt-dlp + Whisper small GPU + MiniMax-M2.7
