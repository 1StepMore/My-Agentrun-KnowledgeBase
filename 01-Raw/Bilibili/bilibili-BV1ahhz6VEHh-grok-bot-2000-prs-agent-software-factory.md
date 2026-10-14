---
title: "【中字】超干货！Cursor 团队大神 Poteto 分享怎么用 Grok Bot 一个月处理 2000 个好 PR"
source_url: "https://www.bilibili.com/video/BV1ahhz6VEHh/"
source_type: "video"
source_platform: "bilibili"
author: "AI嘉豪老吴从零开始版（原讲者：Lauren Tan / @poteto，SpaceXAI）"
author_id: ""
publish_date: "2026-09-21"
fetch_date: "2026-10-08"
keywords:
  - AI-Agent
  - verification
  - pull-request
  - trust
  - cloud-agent
  - Skill
  - cursor
  - architecture
state:
  phase: raw
  time_raw: 2026-10-08T23:32:36
priority: 3
language: "en"
notes: "bilibili-api/yt-dlp 下载音频 + 检测语言（三处采样 en=0.998，**非中文原声**）+ Whisper small (WSL GPU, fp16=False) 转写单P 38:02 音频 + **英文走机械修名（不经 LLM）**。标题带【中字】= 英文原声信号，已按判据先检测再转写。"
duration_seconds: 2282
duration_formatted: "38:02"
---

# 【中字】超干货！Cursor 团队大神 Poteto 分享怎么用 Grok Bot 一个月处理 2000 个好 PR

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。
> ⚠️ **原始音频为英文**（标题的【中字】= 中文字幕，非中文原声）。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | 【中字】超干货！Cursor 团队大神 Poteto 分享怎么用 Grok Bot 一个月处理 2000 个好 PR |
| B站 UP | AI嘉豪老吴从零开始版（搬运/翻译）|
| 原讲者 | **Lauren Tan（@poteto）** —— SpaceXAI 首席工程师（前 Meta 6 年 / Netflix；React Core 团队成员，React Compiler；**pstack 作者**）|
| 场景 | 疑似 2026-09 的公开分享（讲者自述「上个月我发了 2000 个 PR 到生产」）|
| 解析 | 转写 449 段 / 28,697 字符 ｜ Whisper small GPU 151s |
| 发布时间 | 2026-09-21 |
| 总时长 | 38:02 |
| BV号 | BV1ahhz6VEHh |
| 观看/点赞 | 1,153 / 22（抓取时）|

**涉及的专名（已机械核对，均有出处）**：Grok Bot（xAI/SpaceXAI + Cursor 的常驻 AI 队友，2026-08-11 公测）· Grok 4.6 ·
Cursor（含 Cursor agent window / Cursor Origin）· **Dune**（Grok Bot 内部的 agent-friendly 客户端框架）·
**pstack**（讲者自研插件，含大量 playbooks/skills）· Cloud Agents · SpaceX AI（官方写作 SpaceXAI）·
React / React Compiler · Datadog · Sentry · PlanetScale · Chrome / Electron / DevTools · Slack · Lean / TLA+（形式化验证）

## 原文内容

> Whisper small 转写（英文原声，**未走 LLM 后处理**——按判据：英文必须机械修名，LLM 会静默概括）；
> 已做机械修名（16 条规则 / 21 处，词数 5275→5293，差值为专名拆分，非内容增减）。

Hi, my name is Lauren. You might know me as poteto on X, and I work on Grok Bot at SpaceX AI. So last month, I did something pretty crazy. I shipped 2,000 pull requests to production.

A lot of how I'm able to do this is through trust, and I think a lot about trust in terms of how I can trust my agents to produce high quality work even when I'm not there. And my argument and thesis for this talk today is that if you set up your environment for your agents really, really well, you can end up with something that looks more like a personal or even team software factory, where you're producing very high quality code at much greater rates than before. But I'm not a fan of the term software factory. I like the analogy of the Michelin Kitchen better, where, you know, as technologists, we're not really producing, we're not mass producing a product on an assembly line.

But the work that we do looks very creative. It's very, you know, it's the act of building a product and it's art in some sense. So even though with agents we're not cooking the individual components that go into the product anymore, we're still responsible for the final outcome and thinking about our kitchen setup. Because depending on how you set up your line cooks, your sous chefs, the kind of equipment they have, the kind of training they have, dishwashers and the ratio I guess of line cooks to dishwashers.

All of these ingredients go into making the final product and I think this analogy is really apt. So I wanted to talk a little bit about a story before we begin where six months ago when I first joined Cursor before we were a part of SpaceX AI, I obviously had you know, no agent skills to use. I just joined the company. It was a fresh code base and a fresh product that I was working on.

So at the time, Cursor was building the replacement for the Cursor IDE, which is the new agents window. And before I joined, the Cursor agent window had quite a lot of performance issues. and my manager at the time asked if I was able to help them. And since I had spent some time on the React team before I joined Cursor, it seemed like a good fit.

But when I first started, I quickly realized how manual this process was. Obviously, I have done performance work before, but at the rate at which pull requests were being landed, It was just, it felt almost an insurmountable wall of pull requests that just kept coming in. And I had no idea whether or not the performance of the app would be regressing. Right.

So a lot of my early time on the cursor team was spent looking at Chrome DevTools and the performance and doing performance traces and taking heap snapshots. And it was extremely, extremely manual. It was so manual, it got to the point where I just got really frustrated and started to think about, you know, wait, we have agents, what am I doing? And so I started thinking about verification skills, where, you know, what if my agent could actually run the application itself and take the traces for me, understand the traces and find the hotspots and basically he'll climb to better performance in our application automatically.

And throughout the last six months of being at cursor in SpaceX AI, you can really see that my product already has skyrocketed. And I never set out to ship 2000 full requests a month. There was not a goal of mine at all. But I realized that all of the skills, all of the tools, and code-based changes I were making, laddered up to this idea of trust.

You know, I didn't know it at the time, but I had this thought in the back of my head, which was, you know, I am the bottleneck, and I need to be able to take all the knowledge that I have as an engineer and impart them into my team of agents so that I didn't need to be the blocker for everything. You can clearly see that it's paid off. So I think it really comes down to trust. But how exactly do you build that trust?

And where do you start if you're wherever you are in your journey of using agents? So when I started, obviously I was in this category, you know, the one to one to five range, where you still feel like you have to babysit every chat and conversation and you're just constantly course correcting, you know, you're intervening, you're correcting your agent so that it does the right thing. And if you're not there, basically nothing happens and the agents do the wrong thing. Now I would actually argue that this part, this phase of using agents is actually the hardest to get out of because it's not always very clear how exactly you get out of it.

And again, it just comes down to trust. The reason you're unable to go from one or one to five agents to something more like a hundred is because you don't have trust in your agent's work yet. So if you don't have trust and you try to spawn 100 sub-agents or cloud agents, you're gonna quickly find that you're just gonna get a ton of slot pull requests and a bunch of regressions and a bunch of bugs shipped and no one's gonna be very happy with that. So that begs the question, how do you trust your agent's work?

So for me, it came, it really started when I, like I said, I joined the cursor team and I was starting to work on performance where I realized the need for verification. So when I say verification, there are sort of levels to that. Because on the, I guess, the lower end of the scale for verification, you have things like the verification skills that I talk about, where you teach your agent how to run your application, and use things like the Chrome DevTools protocol or whatever other protocol that you have for debugging and teach them how to, you know, debug the application, take performance traces, take heat snapshots and so on. And then on the opposite end of spectrum, or de-spectrum, which is much, much harder and still very much an open question, is like more formal verification where maybe you rely on formal methods or languages like Lean or TLA+, to do verification so that you can check that your business level or business logic invariance are always true, and that you can formally verify that your application is always in a correct state.

But I would say that even if you don't have the ability to run formal methods, and very few people really do, that with verification skills, you can get very far. So when I joined Cursor and started to work on the Cursor agent window, the first skill that I built was a skill called Control Glass, which is a verification skill that teaches the agent how to run the application and take traces like I mentioned, and it does that through the Chrome DevTool protocol. Something interesting about that skill is, and I kind of iterated my way to this, or it didn't start out this way, but the control or verification skill really has two components to it. The first part is obviously a CLI.

So you want your agents to be able to reproducibly be able to run the application and collect traces and collect evidence, empirical evidence that code is working, that your performance bar is being met, rather than have your agents create scripts every time that can differ between agent sessions, you can actually create a CLI that's within the skill directory, and then your agents will just use that every time. And then, of course, you need to actually invest in it and make it good so that it can handle all sorts of different use cases and be able to run the application correctly. Another thing that's also really important is this idea of a feature map. So a feature map really is something that I kind of coined, I guess where we started using these control skills within cursor, then we quickly realized that a Slack report would come in and a user would post a very big screenshot, right?

Like a very small slice of the UI and just like three question marks. And the agents using our control skills are just no idea. Like it could run the application, but it would just be guessing at what exactly the user meant. And so I had this idea to create something called feature map which is I guess kind of inspired by like a site map.

It essentially is a form of materialized memory. You know like how exactly does your application work? What features does it have? How does a user reach it?

You know in terms of keyboard shortcuts or what DOM elements to to click on things like that and what all the different features do. And these, this feature map is stored into skill itself in the code base as part of the skill directory. And we have an automation that maintains this feature map as well. But when we combine the CLI and the feature map, we quickly realized that this combination was very, very powerful because now agents can not only, you know, reproducibly control the application and pick traces, but it could also understand requests that came in from internal users as well as external users.

And so we very quickly realized that the control verification skills were so useful that they've become more or less a critical infrastructure for our team and we constantly maintain it. But the ability for an agent to verify its own work is extremely powerful and we have spent a lot of time on this skill and it's very, very powerful for building that trust. In addition to verification, of course, you want, because verification is really about correctness. Correctness to me is really about does the thing, does the feature or code do the thing that you want it to do.

Does the checkout button, does it actually check out the card? Verification is really important for that because you can get empirical evidence that this feature actually works. But it doesn't tell you much about the performance or the code quality of that feature. And that's where you start thinking about skills that teach agents to work like real software engineers.

So I've built a plugin called pstack. I'm not going to talk about the plugin too much today, but a lot of the inspiration for that plugin, which is a collection of skills that I've created, are inspired by the kind of workflows that I personally have used as my in my time doing software engineering for all sorts of different types of tasks. So debugging, feature development, prototyping, there's a whole bunch of different playbooks and skills that ship in pstack that teach your agents how to write code the way that you want them to. And this is where the more experienced engineers on your team can really contribute to set up a team repository of skills that just make your agents a lot smarter.

And when you combine those skills with verification skills, then you're able to get the point where your agents are able to not just verify that the work that they're doing is correct, but that is also high quality. And again, because of verification, you can collect real performance metrics, you can get real numbers and statistics and telemetry on the performance of the application. So I think that's a really important part to invest in. Another thing I think is really important is refactoring and rewriting your architecture to be more agent-friendly.

And I almost want to say that this is one of the most important things you can do as a software engineering team because if you really truly believe that agents are going to be writing all the code in the future, then we need to design our code bases so that they do the right thing by default. And you'll find that there's this, I almost want to say like a scale or or continuum between these different pieces of building trust in your agents, where I have like five of these points here, where the code base is really like the best form of memory because agents love to extend existing patterns that they see. And I think this is just the nature of how LLMs work, where they're more likely to use whatever it is in their context window to make changes. And of course, the files that the agents read and opens are part of its context window.

And therefore, the code base is a really important part of that because agents aren't gonna just refactor your code in every single PR. They're gonna just look at what's already there and just extend. Next level, I think, is about static analysis, where you have linters, you have compiler diagnostics, you have continuous integration. And these are guidelines and constraints that you can enforce in your code base so that whenever you correct your agent, you find that they just keep making the same mistake.

You can add those as lint rules, or even better, you can refactor your code base so that the mistake that the agent is making becomes categorically impossible. And then a step above that, right, where, and this is where we're starting to get more into less of like a hard constraint and enforcement and more into the realm of guidance. You have things like rules, you have bug bot, you have skills, which, you know, your agents will obviously sometimes and mostly use when they're doing their work, but there is also a chance that it might, for various reasons, you know, forget to read a rule or maybe the user that is piloting the agent ignores them. So these aren't quite as enforceable, but also an important part of setting up your environment so that you can really trust what your agents are doing.

And then finally you have a style guide which is really only enforceable by humans in a code review. I guess you could put these in your rules and bug-bot and skills as well. But if you don't then you have this big glaring hole in your review process where now humans have to you know look at every single line that's being changed and remember to comment and with the rate of pull requests that are coming in, it just becomes impossible. So I definitely wouldn't recommend relying only on the style guide.

I think the style guide or looking at human reviews is a good place to start in terms of what's missing. But you should really invest the time to think about the other four parts, your code base, making things categorically impossible through better data structures or algorithms, static analysis, and then of course you layer that with rules and bugbots and skills. On the codebase front, and in the Grok Bot codebase, we actually have invested into setting something up that we call Dune, which is our agent-friendly framework. So the inspiration for Dune really came about from a lot of performance issues we were seeing in the cursor agent window.

And so a lot of lessons came out of that inspiration. But the key principle that we landed on is really that agents love taking shortcuts. So what if we design the framework such that the shortcut, you know, the easy path is the right path for agents and also one that would be a code base that is, you know, maybe pretty annoying for humans to work in because it's so locked down in terms of what you can do and what you can't do. but it actually creates the perfect environment for agents, especially ones that have very minimal context because you know not every contributor to your code base is going to be an engineer anymore.

You can have designers, you can have product managers, you can have CEOs you know going into the code base and shipping features. So we want to really think a lot about how we invest and set up our code bases so that even agents that are piloted by busy people with not a lot of context can do a good job by default. And like I mentioned before, your code base is really a form of memory for agents because they love to extend the existing patterns that they see. And the reverse is actually also true.

You can invest the time to set up your code base in a way that things are bad patterns are categorically impossible or you have like lit rules that prevent them. But the reverse is also true in the sense that if you have existing anti-patterns, you will actually find that these will spread kind of like a virus where you have like one small workaround or a comment that explains a workaround and you'll quickly find that agents just love to copy that and then in a matter of a few days or a few weeks you'll find that the workaround has spread everywhere and it's now becomes it has become like a de facto pattern for all agents and that's a really really bad place to be in and that goes back to what I was saying about why it's It's really important, you know, whenever you're correcting your agents, that you invest the time into thinking about code-based changes and static analysis and of course, layering them with rules, good rules, and bug-bot and skills because of that reason. And another analogy that I like in addition to the Michelin kitchen is this idea that, know your code base is kind of like a garden where you have workarounds you know that seem seemingly that seem kind of innocent at first then because of the nature of agents you just copy that pattern over and over again and you quickly end up with a very you know vibe-coded code base that is you know a pain in the butt to maintain and has a lot of performance issues so in my opinion the perfect agent code base is one that's so locked down that you know it's again it's like really annoying for humans to do the right coding but it's so conventional it's so standardized that you know even innocent looking patterns are just forbidden and the best example of this I have is actually something that seems very very innocent when you look at it but when you think about it is actually really bad. And that pattern is agents leaving comments in the code.

Now, when I first saw agents starting to do this, I initially wasn't, well, I did think that a lot of them were slot, but I also thought that it actually doesn't, it's not a bad thing, right? I guess if agents are leaving comments in the code, because as humans, we left comments the code whenever we saw, you know, edge cases or we needed to actually make a workaround or, you know, leave a note to ourselves or a colleague on a particular tricky part of the code base. But what I quickly realized when we saw this happening in the cursor code base was that agents were just using the comments around the code as justification for why it wasn't going to solve the actual problem and instead paper over it with a band-aid or a short-term solution. So in Dune, which is again the framework that powers Grok Bot, we made the choice to actually ban comments for that reason, so that agents would not just copy that pattern and and propagate it everywhere in the code base.

So my pitch here is that every team really needs something that, you know, a role that I'm calling a gardener. In the same way that, you know, with a real garden, you need someone who is thinking a lot about the, you know, things that can kind of creep in and grow in ways that you don't want. like you know you have weeds, you have you know just other types of organic growth. I don't really know gardening that well.

But you have things that you know unwanted pests and stuff like that that kind of creep in and pure code based. And so you want to nip them in the bud as soon as possible before they start propagating everywhere. A lot of the principles behind dune are really centered around these three things. First of all, we want to delete tech depth that we already have for reasons I just mentioned.

We want to keep or enforce a single paved path for most blessed patterns. There should be one conventional way to do some things so that agents don't really need to guess. And there should be enough guidance in the code base, in CI, in Lint rules, so that the agents are guided to follow that path. And then finally, whenever you see tech depth or bad patterns, your instinct should be, I need to write a Lint rule against it.

You don't always have to clean up immediately, because if you write a Lint rule, you can at least stop the bleeding, and which doesn't solve the problem entirely, but it at least prevents it from growing. So I definitely recommend really thinking a lot about how you can guard against antipatterns so that they don't spread like a virus. And then also spend time to actually get your agents to clean them up so that your code base is just constantly kept in a state where you would be happy if an agent were to copy it. That's the kind of mindset that I would recommend having.

And then I won't actually go through all the details of doing itself, but I'll just kind of gloss through some interesting parts. So again, as a reminder, Dune is the architecture, the client framework that we built to power Grok Bot. We've invested a lot into, you know, all the things I was saying, where we have conventions. have a lot of conventions about where a code should live and where and how a code should be imported between them.

So in Dune applications, you know, there's different concepts where, like for example, features are all co-located in a single folder. You have an entry point that's, you know, in the React part of the code that determines, you can kind of think of it like a route. You have transcript cards that show up in the Grok Bot application. You have a host that runs on the Grok Bot Berkel machine and then of course you have your client which powers the overall doing application.

And we have a lot of strict boundaries between these things where just as an example things that run on the main process or the main thread in Electron aren't allowed to be run on the renderer thread and we keep that separation very intentionally because of lessons we learned from cursor's agent window where we would sometimes see code accidentally get imported into the renderer thread and you know slow code and since on the render thread you want your UI to be very smooth and performant, you need to make sure that you don't have any long tasks or you know things that take longer than 16 milliseconds or if you want like 60 frames per second or 8 milliseconds if you want 120 frames per second and so So your renderer has to be constantly in a state where it is, it can really kind of chunk up the work and not do them all at once. And so we have code within Dune that enforces this, these boundaries through the import and dependency graph. But yeah, just an example of a pattern that we saw lead to really bad performance that we categorically eliminated through the architecture of Dune. And then all of these other pieces aren't that interesting, but again, the core theme here, it's not about Dune, but the idea that an agent-friendly framework of your own is actually very, very powerful, and you can encode all of the learnings that you and your best engineers on your team have tribal knowledge of.

And I think the lesson here is that how do you take that away from what used to be in the style guide process of reviewing code and engineers reviewing other engineers' work and leaving comments to extract almost like extracting that knowledge and encoding that into the framework into the codebase itself so that the codebase access the memory. It's the thing, like you're coming back to this idea that the codebase is just the thing that it's the materialized snapshot of the state in which you want your agents to extend and you want that codebase to be so pristine, so great that the next agent that comes along it's just very likely to continue that pattern and keep it really really good. And if you spend enough time on this process, like I mentioned, you can really set up a Michelin kitchen or a software factory where because you've spent so much time on, you know, all of these pieces that allow you to trust your agents, whether it's in the code base, whether it's lint rules, whether it is diagnostics or rules or bugbots or skills, these layers come together and provide you a lot of trust. Because now, just imagine from when you're working in rock-bot code base.

It's super locked down, it's almost impossible to write bad code so you know you can even an agent with very little context you know even an agent with not a lot of reasoning can come in and actually write code that's good and going back to my example about the Michelin Factory I think there's a lot here right where you know we're setting up our agents our bots with skills and tools you know we're training them we're setting up our kitchen in a way that makes sense, right, for the agents and bots to do the right thing by default. You know, whenever we see, for example, in the kitchen example, if we notice that one of our cooks or dishwashers is constantly tripping over something, of course we need to fix that, right? We need to problem solve and ensure that others don't trip as well because, you know, in the kitchen is a very dangerous place and you don't want to hurt yourself. the same mindset I think that we should have with our code bases, how do we set it up so that even agents without a lot of knowledge can do a good job.

And I think with Grok Bot, Grok Bot and Cursor play an interesting role together, where Grok Bot is really great at providing what I call the outer loop because you can connect Grok Bot to lots of different, you know, different connectors like Slack, to Datadog, Century, PlanetScale, whatever services that you use, and you can aggregate all of that information together and use that to make really good decisions for itself. Some people call this like a company brain. I personally don't think you need anything that sophisticated here because agents are really good at using tools. And so if you connect these tools to Grok Bot and you start having your Grok Bot's auto kickoff things like Cloud Agents, you can actually find that it's really not...

You don't really have to invest in a lot of infrastructure to build a software factory. In fact, I'm gonna cross out this term, because I don't like this term. I think you can set up this personal Michelin kitchen for yourself through Grok Bot, things like Grok Bot routines, which let you subscribe to Slack threads, to Sentry Alerts that let you kick off things automatically. And when you combine all of these things that I've been mentioning, your code base, your rules, your skills, they all compound and Grok Bot will be able to you know automatically respond to events that come from the outer loop and then kick off Cloud Agents and you can also set up cursor automations and use our SDK to set up additional bots as well that reuse a lot of these pieces of agent that you've set up and allow them to do much more complicated tasks.

So if you've done all this, then I think you can get to a point where, I have some screenshots here of some of our automations and our agents in that work on cursor, where we are automatically reproducing bug reports. we're automatically opening pull requests. We are essentially adding a lot of value to the entire team because all of these things compound. So if we kind of zoom out again and go back to this graph, I think that to kind of close off the talk, If you spend a lot of time thinking about all of the pieces that you need to be able to ascend the trust graph, you start getting to a place where you can really trust your agents more and parallelize your work and also empower your entire team to build on top of these pieces of infrastructure for your agents and empower everyone, you know, every engineer on your team, every builder, to be extremely productive and be able to write high quality code.

So the last thing I want to leave you with is actually this piece. Sorry, not that piece, but this piece. I think if there's only one thing you take away from my talk, it should be this slide here, which is, you know, these are the activities that will help you build up towards a high trust environment. Whenever you find yourself correcting and interviewing your agent, you really want to think about it from these five pieces.

And where is the most effective step in this sequence in order to make your agent much more trustworthy? And of course, I definitely recommend thinking about it in this order, where you either invest the time to make that pattern categorically impossible through your code base and architecture and data structures, or you start looking at things like static analysis, and then you layer that on with rules and bugbots and skills. If you do all of that, and you also spend some time thinking about your code quality in terms of skills, you get to a place where you trust the environment so much that your agents can just be free. And personally, I have spent a lot of time for this for Grok Bot's code base, for example, and this is really the secret.

Well, it's not really a secret. a lot of hard work, but I hope you found this talk useful and please reach out to me on X. My handle is poteto, potato with an E, and I hope that you'll have a lot of fun and success pulling your own Michelin kitchen. Thanks for watching!

## 核心摘录

（原始素材阶段，不做解读；要点抽取留给 `02-Draft/`）

线索关键词：**trust / environment / skills / verification / Michelin Kitchen 隐喻 / software factory（她不喜此词）/
2000 PRs / Grok Bot 常驻队友 / Cloud Agents / 一键 kickoff（routine）**

## 个人解读

（raw 阶段留空——解读属 Draft/Wiki，不在素材层）

## 待验证点

- **`Berkel`**：转写为「a host that runs on the Grok Bot **Berkel** machine」——疑为 `backend`，**保留原拼写待核**（不猜）
- **`Control Glass`**：讲者自称「我建的第一个 skill 叫 Control Glass」，形似内部 skill 名，**未找到外部出处**，保留
- 讲者公司口径：转写为 "SpaceX AI"（她说出来的形式），**官方写作 `SpaceXAI`**（x.ai）。正文保留口语形式，此处存官方写法
- 分享场合（会议名/日期）未在音频中明示，**未编造**

## 关联问题

- Grok Bot 与 Cursor / Claude Code 等 agent 产品的分工与边界（待补外部资料）
- 「skills + rules + 环境」这一套与本地 Hermes skills 体系的对照（可作跨源比较）
- **与已入库 `bilibili-BV1AjH66gETc-*`（同为 Lauren Tan / pstack 作者访谈）可交叉印证**

## 抓取备注

1. **语言判定**：三处采样（开头/中间/后段）**en=0.998 / 0.998 / 0.998** ⇒ 英文原声（**检测所得，非按标题猜**）。
   标题【中字】正是「英文原声」的强信号 —— skill 里三次踩坑的判据再次生效。
2. **转写**：Whisper `small` / cuda / `fp16=False` / `condition_on_previous_text=False` ⇒ **151 秒（2.5 分钟）**跑完 38:02 音频，输出 **28,697 字符 / 449 段**（`DONE len=28697 segs=449 lang=en elapsed=151s`）。
   - ⚠️ 修正记录：初版备注误写为「4.6 分钟 / len=12889」——那是目录里**遗留的旧 `whisper_boot.log`**（往期其它视频的），已按实测更正。
3. **后处理**：英文**不走 LLM**，只做机械修名（`Grok Bot` 的 10 种错拼 → 统一；`pstack`；`Slack threads`；
   `agents`（原误听为 Asians，必改）；`Dune`）。**未做繁转简**（英文无此问题）。
4. ✅ **词表缺口已补（2026-10-08 当晚，用户拍板）**：原缺的 4 个主题词已进 `_keywords.yaml`（`auto_added`）：
   `pull-request`（含别名 **PR / PRs / 拉取请求 / 合并请求**——用户特别指出「PR」这个别名）·
   `verification`（验证/校验）· `trust`（信任）· `cloud-agent`（云端 Agent）。
   本条目 keywords 相应更新为这 4 个新规范词 + `AI-Agent/Skill/cursor/architecture`。
   **补后实测**：`PR`→本条第 1 ｜ `2000 PR`→第 1 ｜ `信任`→第 1 ｜ `cloud agent`→第 1 ｜
   `verification`→第 1（88 分）｜ `pull request`→命中 ｜ `验证`→命中（名次偏中，因 Raw 层只索引前 600 字，属已知设计）
   ⚠️ 施工中一次自纠：`pull-request` 起初误配 `related: [软件开发]`，把结果稀释到查不到本条 —— **已拆掉**（教训：`related` 只加"具体→抽象且不泛化"的，泛化即稀释精度）。
5. 中间产物：`01-Projects/bilibili_audio/_raw/`（Whisper 原始）+ `_pp/`（修名版 + 分段版）；wav 已按收尾规矩删除
   （本批 418.7MB → 0.88MB；**已按 skill 规矩做全目录扫描**，无往期遗漏）。
6. **检索实测（入库后验证，不是假设）**：
   - `kb_search.py "Grok Bot" --raw` → **本条目排第 1**（score 216）✅
   - `kb_search.py "Poteto" --raw` → **本条目排第 1**（score 144）✅
   - ⚠️ **须带 `--raw`**：默认检索层是 `wiki+draft`，Raw 层不在默认范围
   - ⚠️ **Raw 条目的可检索面 = 标题 + 关键词 + 前 600 字 + 小标题**（`kb_search.py` 对 raw 层
     `body` 置空，只留 `snip[:600]` —— 这与《检索规范》里"Raw 正文只留 600 字摘要"的**已知设计取舍**一致，
     不是缺陷）。⇒ 正文中段内容（如 "Michelin kitchen"）**默认查不到**，这是该设计的结果
   - ⇒ **所以关键词与标题的覆盖度对本条目至关重要** —— 见第 4 条的词表缺口
7. **同源交叉**：库内已有 **`bilibili-BV13be26zEqG-ai-agent-team-grokbot-pstack-code-review.md`** ——
   **同一位讲者（Lauren Tan / @poteto）、同一主题（Grok Bot + pstack + code review）**。
   两条互为印证，建议在 `02-Draft` 阶段合并编译。
