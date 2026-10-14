---
title: "两个最会写 Skill 工作流的人的对话：每月 2500 个 PR，睡觉时 AI 还在干活！pstack 作者怎么做到的？"
source_url: "https://www.bilibili.com/video/BV1AjH66gETc/"
source_type: "video"
source_platform: "bilibili"
author: "山人自有GoodIdea"
author_id: ""
publish_date: "2026-10-04"
fetch_date: "2026-10-07"
keywords:
  - Skill
  - workflow
  - agentic-loop
  - Harness
  - vibe-coding
  - cursor
  - mcp
state:
  phase: raw
  time_raw: 2026-10-07T03:45:32
priority: 3
language: "en"
notes: "英文原声访谈（B站搬运）。yt-dlp 下载音频（3935.53s，与元数据一致）× Whisper small（WSL GPU, fp16=False, language=en；⚠️首轮误用 language=Chinese 致全篇乱码，已重转）× AMD DeepSeek-V4-Flash 后处理（15 块，比值~1.00）。"
duration_seconds: 3935
duration_formatted: "65:36"
---

# 两个最会写 Skill 工作流的人的对话：每月 2500 个 PR，睡觉时 AI 还在干活！pstack 作者怎么做到的？

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | 两个最会写 Skill 工作流的人的对话：每月 2500 个 PR，睡觉时 AI 还在干活！pstack 作者怎么做到的？ |
| 作者 | 山人自有GoodIdea |
| 发布时间 | 2026-10-04 |
| 总时长 | 65:36 |
| BV号 | BV1AjH66gETc |
| 语言 | **英语原声**（B站搬运，标题为中文） |

## 原文内容

> Whisper small (language=en) 转写 + AMD DeepSeek-V4-Flash 后处理（分段 + 修专名）。
> ⚠️ 英文原文，未翻译。

So, hello folks. I've got another treat for you today. Last time on this kind of podcasty thing, I suppose, we had Uncle Bob, and we talked about software quality, we talked about agents, we talked about lots of cool stuff. Now, we have an incredible guest, someone who I'm delighted to welcome on, who's been exploding on Twitter recently about software factories, about increasing the quality of your work, about increasing your velocity, and climbing the trust ladder with agents so that you can ship more and more and more. And it is Potato. Welcome. Thank you so much for joining. Thanks for having me. Yeah, very excited to be here.

Yeah, I'm a huge fan of yours. People have been talking about this like it's like the meeting of the skill minds. The skill Mount Olympus or something because both of us have very popular skill libraries. As I was saying before we started, I've not used a ton of yours. And like I want to get all of the juice out of your brain so that I can go and use it. Yes, I think where I want to start with this is you gave a talk pretty recently like about 10 days ago and posted it on X which went absolutely nuts about how I shipped 2,500 PRs last month in production. Got about three million views or something on X and I watched it and I loved it and I recommended it. And I kind of want to run this as almost like a Q&A of that talk, basically, of giving you... Because I just had tons of questions about it and I wanted to dive into it.

And I think where I want to start is you talk about a trust ladder with agents, where you, as you trust agents more, you can get them to do better and better things and or scale them up to use more and more agents. So what is your story of how you climbed the trust ladder and how did that work when like you've got SpaceX and start climbing more and more? So I think the journey sort of began even before I joined Cursor, which is now SpaceX AI. So the story is after Meta, so I used to work at Meta on the React team, I took a month off because I was feeling kind of burned out. And of course, what do you do when you're burnt out? You go and start a new side project. And so I started a side project. I was, of course, using AI to write code. But then I started to realize spending so many hours just micromanaging one agent.

And at the time, this was back in February, maybe early February or January. People are really obsessed with this idea of orchestration. This was before things like Cursor, like the agents window had become popular. So people were still in two-way land in their terminal, and they were all talking about, oh, here I built a custom orchestrator, right? And so of course, I was a bit nerd sniped by that. And as I was building my toy project, I got nerd sniped by, oh, how do I make my AI coding setup more efficient? And so I kind of started the journey there where I just took a step back and realized I was spending all this time micromanaging a single agent. I was creating skills, and I was finding it quite difficult to measure the output or the results, the impact of the skill as well. So I was kind of flying blind, but I was iterating really fast.

And so that project eventually sort of became the basis of PSAC, even though I didn't know it at the time. And a lot of some tricks I had learned, like building that early set of skills. Actually, it's still open source if anybody wants to take a look, it's on my GitHub, like Potato slash Noodle and OODLE. And in there, you will see some skills and a brain directory. And so I was really interested in this idea of, how do I extract my own ability, if that makes sense, and give it to the agent. Because I realized that all I was trying to do was trying to teach the agent to write code more like me. You do workflows more like me. So the skills were like an entry point to doing that. And then after I joined Cursor, I was starting to work on the agents window and it had a lot of performance issues. It was pretty laggy.

And so since I had experience working on React, I was asked like, hey, do you want to come and help out with the agent's window? And so the beginning of the Corsair journey was very manual. I was deep in looking at flame graphs and heap snapshots and trying to see why exactly is the app so slow. But then coming back to the same realization, I was sort of the bottleneck. I was doing everything manually. I was sort of the meat proxy in a way, or I was the meat proxy between my agent and Chrome Dev Tools. And I was like really annoyed by that.

And what month of the year is that, let's say? Where are we in the timeline? So I joined cursor in March. So this was like early, early April, probably. Early April is when I joined and I didn't have any skills. Or I had, I sort of abandoned my personal skills because I didn't think they'd be relevant anymore. But then working on the agents window and now working on GROC bot, I sort of realized that a lot of the lessons I had learned from those skills, time building the initial set of skills were very relevant, especially around things like verification, you know, being very rigorous in your work. Because I think agents from my experience, even the frontier ones tend to, tend to take shortcuts. They tend to do the easy thing. So a lot of the skills that I built have been around, how do I make the easy thing, the right thing? You know, how do I make that the best thing? The idea of sort of distilling your expertise and turning what you do every day into processes, that's something that feels super familiar to me. That's exactly what I've been doing with the skills.

And I suppose there's something in that which is a lot of people think domain expertise is getting less useful now as people start to rely more on AI. What do you think about that just as a sort of vibe check before we start to talk about that? I feel like domain expertise is more important than ever. I think I wrote this on my ex at some point, but at times I sometimes think of AI as this, especially as the models get smarter and smarter and more capable, and the frontier models are just getting so good. Like I love opus 5.5, by the way. As the models get really, really, really good, it almost becomes like the bottleneck is no longer the agent, right? It becomes your ability to express your intent and your goals in a clear way that the agent can understand and actually carry out.

And that's why I think, you know, people with a lot of domain expertise are extremely, have a huge advantage in my opinion, especially if you're a little bit like, you know, techno curious, you know, so I think of people like, you know, like a doctor or a lawyer or someone who has a deep expertise in a particular non-engineering domain. And if they're actually just a little bit tech savvy and they can figure out how to use agents, they can actually build really, really great products. If they have a clear enough vision in their head and they can articulate it in a way that the agent can build it, I think that that is really the bottleneck these days is like the transfer of your intent and your vision to the agent.

Yeah, I've been obsessed with language basically since agents dropped. I just obsessed with thinking constantly about the composition of words, how I can make things sharper, what might be hidden in the phrases that I'm using. And finding what I love is when you find a word that the agent then hooks onto and then goes, okay, I'm going to reinforce that word. Yes, I'm going to reuse that in my thinking traces. You know, I found that with TDD was an early example of that. A lot of chat about TDD recently of like, you know, people say, should you use TDD with agents? It doesn't matter. What you're doing is you're getting the agent to think about TDD, getting it to write tests, getting it to prioritize things in a different way than it did before. And that's why sort of grilling, I think works effectively.

Yes, grilling is a yeah, it draws those words out of you right or at least it helps the agent understand your thinking so that it can propose those words to you and you can pick up and say yes exactly that. I've actually copied some of the tips that you've shared as well but you know one of my favorite ones that you've shared recently or not or like maybe in the past couple weeks is about reducing or eliminating tautological tests like one of my pet peeves of agents is like all of the useless tests that they write. And so, you know, that was one thing where, you know, the word tautology, right, is, is, is, I guess, you know, not many people necessarily know that, if, especially if English isn't your first language. But there's a lot of meaning to that word. And it's like, it's almost like compressed, right? Like you compress a lot of intent and meaning into words. And so I totally agree with you. Like, I think language, I've always been interested in in language actually, like programming languages, natural human languages and how they came to be. And it's so interesting that now with agents, it's sort of like this meeting of natural language with programming language, but it's all it's all language out of the hood. It's all communication.

Totally. I did a drama degree, right? So, you know, I've been thinking about language and Shakespeare and stuff for a long time. And so this all feels very familiar. So, okay, sort of before we get into like, because I think the thing I want from you is like software factory stuff, right? Software factory is the big buzzword. Software factory is the thing that I'm thinking about too. I'm sort of releasing a course in that direction too. And it's this sort of scaling yourself up to unrealistic numbers of PRs basically, or PR numbers that sound ridiculous to people who don't understand how this works. So where I want to get to is sort of from people who are doing kind kind of like one to five agents today up to, you know, hundreds of agents running at once and how that sort of functions. And so I'd love to hear about your metaphor of the Michelin kitchen instead of the software factory. Because I think that says a bit about the way you think about this stuff.

Yes. Yeah, I've never really liked the term software factory. Not because, you know, it's not accurate, but I think a lot of people when you think factory, right, They don't necessarily create that with quality or craft, things which are very important to me and a lot of people and technologists who work, building products, we care about the user experience, we care about the things we're building. So while I do think software factory is an apt term, it also, I guess maybe conjures up negative, maybe sometimes negative connotations. So Michelin Kitchen is the thing that I've sort of landed on where it's much more, I feel like it's much more aspirational and I like the metaphor a lot because you know I like food, I'm called potato of course and I like cooking and I see a lot of parallels right like with food right when you're cooking a meal for yourself for example it's both utilitarian like you're trying to just feed yourself right and survive but it can actually be transformed into art right and that's what what a Michelin starred chef or even just a chef or a cook can do with food is take something very ordinary and turn it into a delicious meal that takes you back to your childhood days or something like that.

And so it almost mirrors that trust letter that I talk about where you can sort of imagine your own journey as a home cook. As a home cook, you are doing all of the cooking yourself. You cut all the vegetables. You do all the prep work. do all the cleanup. You know, you are the one man or one woman show really. And it's an interesting thought experiment like, okay, if you were to cook a meal, and then you add people, right? You're your partner and trying to your brother or your sister.

And now suddenly you have your whole family in the kitchen. I think most people would get very stressed by that, right? The thought of so many people are just mucking around in my kitchen. They have no idea where all the utensils are. I have a max capacity of one person in the kitchen. Yeah, exactly. Yeah, absolutely.

So I feel like that's really apt, because when you ask yourself that question of, how do I go from being a solo cook, right? To having an army or even not even an army, but a few sous chefs that are helping me in the kitchen. How do I think about dividing the work in a way that makes sense? You know, I'm not dividing work just for the sake of it, but in a way that actually makes the sum better than the total of its parts. And so the Michelin kitchen metaphor to me works really well in that regard because as a chef, if you become a chef, you're in a position where you're not necessarily cooking all the food yourself anymore, but you are thinking, you're almost like the tech lead for the kitchen where chefs have to think about, not just cooking, but they have to basically organize the whole kitchen and they're like the CEO of the kitchen. They have to think about when do you order ingredients? How do you store them? How do you prepare them? When do they have to be prepared? You know, it's a whole job, right? That's not just cooking.

And I think that again, it mirrors so much of how engineers write code today, where you are not writing the code yourself anymore. You have agents, right? But you as a human are still responsible for the final outcome, right? Your name still is associated with the work that you do, your reputation, and you know, so how you set up your kitchen, right? And how you set up your skills, your environment, your code base, I think are ultimately the new ingredients that go into building product.

Yeah, I think what I love about your approach is the amount of focus that you put into the environment that the agent operates in, right? Because I think a lot of people they think, right, the agent is good, I'm probably not gonna be able to make it better. Let's just trust what these magic model people have put into the harness and the model combination. There's nothing I can really do, like I can't mess about with core codes internals or something or whatever you're using. But what I love about your approach, and it's something I advocate for too, is that you can change the environment the agent operates in, right? You can make changes in the code base and also give it tools for verification as well and allow it to verify its own work. So the thing I loved about watching that talk is the amount of focus you put in verification and like that is the lever that you can start to generate trust. Can you talk about that and what that concretely looks like?

Let's start like looking at practical ways that people can improve their own processes, their own kitchens. Yeah, I've said this a lot actually that, you know, even if you don't use PSAC or, you know, your skills, I think that the single most important skill that should be in your toolkit is verification. Because without verification, and for those watching who don't know what that means, it's this idea that you can give, you can sort of give your agent hands and eyes. Eyes in a way that's the analogy I like, where the agent is able to run the code and actually interact with it like a normal human user would and also do things like debug it, take traces and snapshots. And funnily enough, that was actually the first skill I built when I joined Cursor that gave me a lot of, that was the thing that actually started to let me send the trust ladder a little bit in a way that some of the other skills I had looked at or built had not really led me through.

Because no matter how good, you know, some of the other skills were like the how skill, the why skill, the unslop skill were, I was still relying on me as the proxy between my agent and the output so that, you know, if the agent can actually see the result of its work, there's no way it can actually iterate. Right. And so this is where people start to talk about loops, this idea of a loop. And really, I think the term loop, you know, seems kind of almost abstract, like people that what is a loop, what is an agent loop? But really, to me, like, the most important part of the loop that allows it to be a loop is the verification part, because the agent is able to verify its own work. And, you know, that takes you out of the equation, where now I can actually do something like, so one of the very first use cases I had for verification was, you know, like the performance work that I was doing on Cursor's agent window. And I wanted to get to a point where I could do something called hill climbing, which is a term that I think the labs talk about a lot, which is this idea that, you know, you have some kind of rubric or a way to judge or score something. And now because you have a loop, you can have an agent continually try to make improvements to that. I think Carpathy, Andre Carpathy also famously released something called auto research that has a lot of these ideas. But yeah, verification I would say is probably the most important skill in PSAC and many other you know, tool sets. And I think it's the most important thing to focus on. So a lot of the, a lot of, I spent a lot of time actually, you know, tuning the verification, the creative verification skill, and also internally, we have so many verification skills now that every app that Cursor has or SpaceX AI has, has a verification skill that is auto-maintained as well, and it's become critical infrastructure for our team because everybody uses it.

And you went pretty far with that too, right? Like you had a, in your talk, I saw that you actually built a custom CLI for that too. So what does that CLI do? Like how does it execute things? And why did you, I mean, that's proof of how deep you're going, right? Of how much you're pushing that. Yeah, so this is actually a tip I learned early on where, I guess, you know, back in January or late last year, the thing that people were very concerned about was context window, right? That was the big topic at the time was, how do I manage the context window? Because compaction summarization wasn't really that good yet. And people had this, there was almost this meme in the community that once your agent summarized or compacted once, it would become sort of stupid for the rest of your session. So there was a lot of thinking around being very efficient with your context usage. And so that was actually the inspiration for some of the CLI work inside of the verification skills. I guess now it's less so about context because agents are much better or harnesses have gotten a lot better with summarization. I still think there's some benefits to having a clean context window. So the CLI is really just more of a way for me to take the deterministic parts of what the skill does and encode that into a script or a CLI to reduce, to kind of take away the judgment that would otherwise unnecessarily be used because with judgment. So I also think of, you know, agents and skills and sort of like, is like a gradient. You have some parts of the work that are are entirely judgment based, right? Something that requires thought, putting together multiple pieces of context, thinking. And then you have the more deterministic parts, like I don't know if you wanted to refactor some code from one pattern to another, that's very mechanical, right? You don't need an agent to think about it and come up with it in a novel way each time. And so that was really the inspiration for the CLI. And you'll see this in a lot of the other skills that I built.

It's like I try to extract out the deterministic parts and turn that into code and just leave only the parts that actually require judgment through the agent. So in a way, I think of the skill as kind of like your wrapper. It's a wrapper with some light instructions around how to use these custom tools that are inside of the skill.

Oh yeah, I don't think the skill is really that interesting in its own right, really. It's not like a novel piece of software. It's just something that interacts with Playwright and the Chrome DevTools protocol and calls a bunch of APIs. It's just a bunch of glue.

No, it's fascinating, because it's a way of hiding information from the skill. It's a way of conserving the skill, keeping the skill quite small, I imagine, and then you're able to delegate more of the complicated deterministic stuff into a script within the skill. So it's almost you're compressing information and making the agent do more consistent things more consistently. That's fascinating.

Yeah, and it also helps, I guess, if you care about context window, it does help because now the agent doesn't need to reinvent things. Because one thing I had noticed early on when we didn't have a CLI was that, well, the agent would try to verify its work, but it would basically rebuild the world each time, and then every agent did it differently. And I was starting to notice that's very inefficient. I was wasting. It was actually not just about context usage, but also speed. Like, it's now an agent had to actually go off and write the scripts or the CLI and test it, and it doesn't work. And the last agent did it and it worked, but it discarded it. So it was just very obvious at that point, like I should just turn this into a CLI and put that inside of the skill so that every agent that uses it now benefits from that same piece.

But I also think like, that's a good push for people to think about is how much of your skills and rules could actually be deterministic. That's like another core thing or one of my core principles that I like to think about is how do I make very efficient use of determinism and non-determinism and let agents shine at the non-deterministic parts, right? Because that's what they're trained to do. And the other parts which are much more mechanical or straightforward can be just pure determinism. And you'll see this as well for things like doing migrations, which is another big thing that I've talked about is going from one technology to another, especially one that is better for our agents. And a lot of how you can do that migration is I think through things like scripts and CLIs, like the deterministic parts like code mods, like crawling the AST, the abstract syntax tree, and transforming code literally mechanically, right? Like a script does it for you instead of the agent.

Totally makes sense. I mean, I think what, there's another thing there, which is you're taking stuff away from the agent and you're kind of putting it in the environment too, a little bit, which is let's say you have a thing that you notice the agent always gets wrong. You want to make that just impossible within the environment. And that sort of comes down to code quality as well. I mean, I talk about a lot like having a good code base means, right? What is a good code base? And there's a definition I like, which is a good code base is a code base that's easy to make changes in, right? Easy to change stuff without things screwing up. And that means that you have a lot of guardrails, that you have a lot of the agent or the human is constrained to very narrow paths. And that's again, something you talk about in your talk. And you talk about this not only on the kind of, sort of automated checks side of things, so linting and time checking, blah, blah, blah, but also in the way you design abstractions. And you guys even, I think, built a framework for your agent to work into. I think what I'd love to hear is you obviously think of that as very important, right?

And that's how important is that compared to other things you could be doing, like building features or shipping work?

Yeah, I think that's—I almost feel like the new job of the engineer is really to spend time on the environment. I almost actually wrote a tweet about this yesterday, but I didn't. But I think that, you know, if you haven't really spent time building trust in your agents and building skills and tools, you can get stuck in this mode where you're very low on that trust ladder. You don't have a lot of trust in your agent's work. And so the only way to cope when you're in that situation is just to lock in and micromanage your agents. And that's very time consuming. And when you're stuck in that mode, you don't really have the luxury to think about higher level things.

So like, making yourself more productive in the same way that—I guess the analogy would be like, if you've never taken the time to learn your tools as a developer when you're writing code yourself. And you know, you've never heard of VS Code, you've never heard of Vim, you only knew about Notepad, and you hadn't even heard about Git. That's sort of the analogy. It's like you haven't spent the time sharpening your own knives. And so of course, if you have a dull knife, then everything can take a long time. And you're just going to be—especially if deadlines are looming—then you don't have the—now you're stuck in this rut where you don't have sharp knives, you don't have good tools, but you're under all this pressure to ship. And so all you can do is just focus on that.

But I do think that if you can find yourself the time to actually spend time thinking about your setup—it's again going back to the cooking analogy. It's like, you know, if for example, if cutting the garlic is super slow, right, there are garlic mashers, right, you can buy it and you put it in the thing and you squeeze it out, right, it's super fast. Machines and tools are invented for a reason, right. And so if you're operating a Michelin kitchen and your cooks have no tools, then of course everything is going to be extremely inefficient. Every cook is going to make something up of their own. So I think the tools and the determinism to me are taking that part away. And just like you said about constraints as well, the constraints are to me as well.

Actually, a slight tangent on that is I think we should talk about TypeScript because we actually both share a background in TypeScript where you obviously have done a lot of work with TypeScript and Total TypeScript and you're a leader in that space, and I had adopted TypeScript pretty early and I had given a talk or two at TypeScript Conf many years ago. And so one of the talks that I did actually was about type systems and constraining the types. Like one of my most favorite things about TypeScript is actually type narrowing. All right, this idea that you go from a very broad type, all right, that could be anything. And then you through type guards and you know type narrowing and you know runtime checks, you can actually narrow the space and say like, oh, this isn't just a string. This is a very special type of string constant, right? I determined that through the type system.

And in a way, it's like, there's a lot of parallels, I think, to that with constraints in your codebase, where is it you're constraining the space, right? If you think about category theory as well, you know, you're constraining the number of possible types, right, that can exist. And you're saying there's only one type, right? And for us, that framework that I'm building called Dune, it's not an open source framework. The way I describe it to people, it's kind of like our internal Next.js for our Electron apps. But it comes with a lot of really, really restrictive lint rules.

And the codebase is designed in a way that there's really only one way to do something. So we make use of a lot of conventional patterns. So features all go into a specific directory. Well, every feature has its own directory. As an example, there's a thing that discovers features through a registry and crawling the codebase and stuff like that. But this conventional pattern and the lint rules make for an environment where it's actually very hard to write bad code. And that frees up the, it both frees up your own mental capacity, as well as the agent, sort of doesn't have to think about that anymore. Or it's just like, oh, there's only, I should just, if I wanna add a new feature, it just goes into the new feature directory. And all the code goes in there, and I'm not gonna append to a God file.

That was really actually the inspiration for those feature directories is the very first couple of versions of GROCKBOT, were composed of eight God files, which were at least 10,000 lines long, if not longer. And so I had to break it up into smaller pieces. But I was just observing. Actually, that's another important part, is observing how agents fail. And then every time you see a mistake, every time you see something that could be done better, you step back and think, how do I turn this into a lint rule? How do I make it so that the codebase makes is impossible, right? And it comes back to me for my, you know, my background learning TypeScript and types, type systems is how do I constrain the space so that, you know, I know precisely what I'm working with. And I think, yeah, there's a lot of parallels there. Totally makes sense.

And then, I mean, it's funny that you mentioned TypeScript and code files in the same sentence, because type famously has a 25,000 line type. Yeah, I realize the irony of that. Well, I don't know if they've rewritten that and go. I don't know if they've already have one. OK, so the environment is important. You should watch your agent like a hawk to make sure that any mistakes it makes, you turn them into things in the environment. And the benefit of the environment is you're not overloading your agent, right, in terms of rules, in terms of things it has to remember. It's just in the environment. And so it stumbles into the rules. Exactly. bounces off them and hits them at the right moment.

So okay, we still haven't talked about the 2500 PRs. Where do those come from? Like, how do you, you've built your trust ladder, you've worked on your environment, and you understand, okay, I now want to scale up. So what are the mechanics of that scaling? Are you initiating 2500, like, chats per month? That can't be right. So there must be, Are there any kind of automated triggers that trigger stuff in your repo? Like how do you get the software factory kind of triggering work by itself? Right. I'll definitely say that the prerequisite to something like a very high volume of pull requests is the environment, the stuff we just talked about, where I definitely would not have been able to do this if I had not spent the time, you know, thinking about the kitchen and the knives and the tools for my agents.

And so in a way, I think of this as I've spent a time building one kitchen and one restaurant. And now I'm in a position where I don't actually have to be there anymore, because the environment, you know, the same analogy, right? It works really well. Yeah, exactly. Yeah, exactly. It's at your Gordon Ramsay and you've taught your executive chef all the tricks of coming up with a great menu and the kitchen is set up really well. Everything is just perfect. And you're now in a position where you can open your second, your third restaurant. And I guess I sort of see each project that I work on, each big chat, is sort of like a restaurant. And I have multiple of them operating at the same time. And I'm sort of like, helicoptering between them, sometimes some more than others, depending on how in the loop I am.

But yeah, definitely I think there are external triggers and context that those projects don't have. For a long time, I was the proxy for that. So the best example I have is like, you have a project that's working on a feature or you're trying to fix a bug, and you're getting bug reports, but the bug reports are going to things like Slack or Linear or X, right? And these are external systems that aren't connected to your inner loop.

So I like to talk about this outer loop and the inner loop. I don't know if I'm using the definition correctly, but to me, my inner loop is basically my engineers, my agent engineers working on the code, building towards an intent or snapshot of my intent, right? And the thing about that is that the snapshot can go stale, right? New information comes to light that I then have to be the proxy of and transfer that context to my agent. So if you don't have these triggers pulling information back into the inner loop, then you sort of have to play that role where you're off in Slack or X or whatever, and you're gathering context, right? You're getting context about bug reports, about feature requests, about something someone said about our backend infrastructure having some limitation. All that information, you have to ferry that across to your agent.

So that's where I think tools like Grogbot are really good, because they help you automate the outer loop as well. And when you connect those two loops, it's very, very powerful, because now all of a sudden, your agents have the ability to get context for themselves. If, for example, either through just as a simple example, maybe you have the Slack MCP, or you have your own harness that you've built a Slack subscription into for a particular Slack channel. Now, all of a sudden, you can tell your agents, OK, subscribe to the Slack channel. Every time there's a bug report about something, go off and triage that thing. Go reproduce the issue using the verification skills that we've already spent time building, and all of those other skills that we've set up so that I have a lot of trust. They have a lot of trust that these agents can actually go off and understand the bug, verify that the bug actually still exists on main, and it wasn't something about maybe the user's setup or their data, or maybe they didn't install a dependency or something like that.

Like basically, I think creating those two loops and connecting them is really a very important part of the job these days, especially if you are thinking about how to scale yourself. So a big theme here is really just always thinking about like, where am I the bottleneck in this process? Why do my agents need me to answer this question? I always like to think about that. And so I try to think about how do I actually get the agent to answer its own question, but not by hallucinating, not by guessing, but actually real data.

And a lot of people talk about this idea of a company brain or a context graph. I feel like those terms are unnecessarily complex or even abstract. To me, it's just about how do I take information that my agent needs, that I would otherwise have to go and pass it myself, and just teach it how to do it. And that removes me from the equation. And so how I arrive at 2000 or however many PRs is the fact that I have all these loops set up. And so it allows me to open chain restaurants. I can really parallelize myself. So yeah, I'm not sitting there creating 2005 and chats, of course. It's really like these projects are. Articursor has a new feature called Projects, which are these like coordinator agents. And so the coordinator agents are really good at sort of delegating and not doing work of their own, but they manage and supervise like almost a list of tasks and respond to agents to go and do them.

And so I'm just constantly feeding context or teaching the agents how to get their own context and then they're going off and doing the work for me. And really the big, the last thing I'll say to this is like the big unlock for me for getting to 2000 PRs is starting from the question and working backwards of how do I get to the point where my agent can merge its own code? Because the obvious thing people ask me when I tell them, oh, I shipped 2500 full requests last month, they'll be like, how did you review that? All right, that's just a lot of PRs to review. Your team must hate you.

Do you mind if we go there in a second? Because I have a good question about that. Yeah, yeah, yeah. I want to like this analogy is great. I want to like deepen it a bit, which is before, if you're like manually initiating all those chats, it's like you're bringing the orders to your chefs manually, right? Whereas if you've got an agent, sort of like doing the expo, then you're able to sort of run it yourself.

What does that concretely look like then? You've got these sort of grok bots that are subscribing to channels, pulling in Slack messages, and you, it sounds like have a couple of coordinator agents or like chief of staff agents that monitor that or something. When you look at your computer to manage your agents, what does it look like?

Yeah, so this is, I guess, somewhat confusing, but we're working on simplifying and unifying. But so there's Grapbot, or you can use other tools, of course, as well. But I largely think of these tools as like your outer loop. These are tools like Grapbot that have connectors, right? These are connectors. I guess a lot of people call them personal agents, but they're connectors to things like your email, your calendar, Slack, plaid, I don't know, like all these different services. And they are a great source of pulling context in to your work.

So the same way that a human, like if I were, if I was a manager and I was leading a team of engineers, you know, like when I used to work at Netflix, one of the biggest things that managers would talk about was this idea of context, not control, which funnily enough, you know, has so much, has so much carry over to the agents world of, you know, you, you know, you of course can drive to an outcome you want by control, right, like by micromanaging. But what you want is to provide context instead, right? Like teach the agent, teach your engineers how to be self-sufficient, and then you don't have to micromanage them. And so I see a lot of parallels there.

But yeah, GROCBOT, so concretely, I have some GROCBOTs that look at my Slack channels, look at my X or my emails or linear, and they're just constantly, they have routines that subscribe, so they're constantly watching. And I'll tell them things like, you know, I'll watch for issues with bugs in the GraphBot desktop app, as an example. And whenever you find that, send it to my cursor project. So one of the really cool things about GraphBot is it connects to cursor. So cursor has, like I just mentioned, this new feature called projects. And a project is really a, again, like you get a coordinator agent that's in the cloud. It has its own computer. And all it really does is like it's a manager of agents. It's like your executive chef, right? Your chief of staff. It doesn't do the work itself. It delegates and orchestrates and manages the work of other sub agents to, you know, that report to your chief, your chief of staff. And it basically is responsible for driving the work forward and managing things and passing context to them.

So if you get a sudden burst of issues, let's say you get 30 issues at once in one payload or something or very quickly, the coordinator agent can figure it out and delegate. Yeah, exactly. It gets like, you know, 30 or so payloads and spawns a subagent or a single coordinate agent.

It can actually do a bunch of different topologies of agents and it will sort of figure out the best way to, you know, efficiently distribute the tasks to your team of agents. So I use Cursor projects a lot. And I also use Graph Bot a lot. And Cursor projects are my inner loop and Graph Bot is my outer loop. Graph Bot takes all the external context, gives it to the projects because it can actually just send messages to those projects. You don't even have to open Cursor. You can just tell your Graph Bot, OK, create a project for these series of tasks because they're all related.

Maybe as an example, you've had a big burst of issues that are all about performance. Your app is slow. And they're all connected. Maybe some of them even have a similar fix. And you can certainly go off and just spawn one agent per task. But then you've lost that thread between them. And you may duplicate work, or you may not really think about the higher level problem. Sometimes when you solve bugs, it helps to have multiple bug reports that are slightly different, because it helps you really zoom out and see. Actually, the problem, when I looked at this one report, I thought the bug was here. But actually, when I see the other multitude of bugs, it's actually up here.

Yeah, got you. So that's why you have so many agents in that loop then, right? Because it's not just you have a bug report comes in, you spawn a single agent to look at that bug report. That single agent will be duplicating work with other agents, right? Because if there are multiple bug reports coming in through the same thing, that can be duplicated work. Yeah, fascinating. That's really fascinating. Okay, and so just this endless series of triggers coming from real users, reporting real reports, builds up this sort of an accelerates the factory, sort of adds more orders in.

Other than bug reports, are there any other sources that you use for accelerating, for pushing these PRs? Well, funnily enough, some of it comes from reading the code too. So I guess I have sort of, well, so to clarify that the 2,500 PRs, they're not obviously 2,500 features, right? They are, a lot of the work actually is spent on gardening, like another term that I really love. Where, so I guess this is more important when you have a big team of engineers, human engineers that you work with, where, and also this goes back a little bit to what I was talking about with the environment, you know, setting up a really good environment doesn't just help you and your agents but everybody on your team, right? Think of a new hire who doesn't have a lot of context on all of your engineering practices joining your team, and if you have a really good environment, they can be productive from day one, right? They can, they don't have to like, you know, make open a bunch of low quality PRs, they can start, you know, they can start just turning out really good code. And yeah, I think I sort of lost my train of thought.

I've got a follow up, which is what are the mechanics of like triggering? Like, when do you trigger an agent to go and look at the code, right? Because some people might say, or let's just do that every hour or something, or like on a cron job or what's- Oh yeah, yeah, yeah. I saw some of your recent tweets as well about like, you know, the some of the tweets you've been doing, which are great for Santa Apres routines. I have some routines like that as well. So one of them is like looking through just another simple example is, you know, React has a lot of foot guns. So as I'm sure you're aware, and so I have an agent that's just constantly looking for bad patterns. And the interesting thing about that one is that I don't actually tell it to fix the issue first. I tell it to append it to a document. And then every couple of days I look at it and I say, actually, these are all the same thing. And so that gives me, you almost want a buffer, a queue.

Sometimes it's actually more effective than just spawning off a lot of sub-agents to fix every single thing. Because when you are in pure execution mode and just trying to execute on the orders that are coming in very fast, you sometimes miss the big picture. So sometimes having a buffer forces you to think about the big picture, because you have these artifacts and things that you can look at as a human. And use your own human judgment to, or I guess you can use an agent to do that as well. But you give the agent and yourself a way to identify patterns that you might otherwise miss if you're just only solving each bug at a time.

And that's also really the benefit of having something like a chief of staff agent is it can see the forest in addition to actually doing the execution. Fascinating. My brain is exploding a bit there with the sort of chief of staff at the software factory. I might have to change some of the course that I'm filming next week, that's a no.

All right, let's talk about review, right? Cause this is the reply that you get. Is did you read, did you taste all 2,500 of those dishes as they swept past you? And I assume the answer is a variety, is a version of no. Yeah, I think you don't want to be in a position where you're not tasting your food ever again. But you also, for scale, you cannot be tasting every single dish that comes out of your kitchen, especially if you have multiple restaurants. So it becomes more about sampling and thinking about the processes.

In the same way that, if I guess maybe this is where the factory analogy is a bit more apt, is as a quality supervisor on a factory, you can't look at every single item. You sample, right? You go in there every day and you look at the quality of the pull requests, you look at the code that the agents are writing, and you scrutinize it very rigorously and you think about all the inefficiencies, the bad patterns that the agents are doing, and then you think about how to course correct the environment, not that single agent. Because if maybe if it was a one-off incident, it's fine, you know, that maybe there's nothing to fix there. But if you actually notice that multiple agents are having the same issue, right? They're taking the same shortcut. They're propagating the same work around everywhere. That's a sign that you should go off and think about how to amend your kitchen or your factory. Right? Like thinking about your skills, your constraints, your lints, your type systems and adjusting it so that that problem doesn't happen again.

And when you do that enough times, then you get to a place where the code basis, again, the environment is so constrained. And so it guides you so well that you can just step away. That's the dream. And I'll definitely say it's very hard to get to this point. I don't wanna sell this as something that you can just do easily by using PSAC. Like it takes a lot of time and effort to think about your code and where you see your agents failing and thinking very thoughtfully, intentionally, and setting up guardrails and constraints so that they do the right thing by default.

And you're not, like, to go back to the software factory analogy, this isn't a dark factory, right? This, the lights are on, right? It kind of is, actually. Is it? Yeah, well, it's dark in the sense that, so it's dark in the sense that, well, I think if my agents are merging their own pull requests, it's sort of become dark, where I go to sleep, my agents now work 24-7. I have the equivalent of like more than 10 chiefs of staff, each working on a different area. Like for example, I have one that's working on performance of the GropBot desktop app. I have one that's working on fixing bugs that uses report. I have one that's exploring, rewriting it in a different language just for fun. You know, like what if, what if, you know, just reimagining what it would be if it was like a native app. It's just a toy.

But the idea is like, yeah, when you spend the time setting up your environment, I've gotten to a point where I review the pull request after it's landed. I tell my agents full autopilot is something that you can do in PSAC. And that will trigger off this very intense rigorous verification loop where it will spawn a bunch of verifier agents for every pull request. And it will fuzz, fuzzing meaning that it will actually run the application. It's going to click around and try to use it like a real human. Look for regression, look for bugs in your implementation. And it will try to find issues with the thing. And then it will fix it itself. It'll do that again and eventually get the PR to a state where it can land. So it does, it does, it is quite token intensive. You can tune this, of course. So you know, instead of like 10 verifier agents, you might do like one, right? Or, you know, just tell the agent to verify it's on work. But yeah, the key thing is the verification part is really the key piece that gives me a lot of confidence that I guess verification plus the environment, it's these the combination of these two things that allow me to step and say agents go off and merge your thing, I'll review it in the morning by looking at my commit history. And if I see problems, I go in course correct, right? And I'll go in revert or modify, add new lit rules and whatever. So it does take time to get to that point. But once you get it, oh, it feels so magical. I tell people like, I'm sleeping so much better now because, you know, it took, the very first day I turned on that sort of dark factory was very scary. Cause I was like, ooh, what if I cause a set of right? What if I break something overnight? And it took a lot of, it took a lot of bravery, I think to do that, but somehow I did it. And now I'm in a place where my agents are merging their own code while I say, it sounds like it's dark in that sense. Yes, it's dark sometimes, right? You do sometimes. That's true. Because I think of a dark factor is like almost like if you take the original definition of Kapathi's vibe coding, right, which is the code almost doesn't exist, you forget that code might be a thing. I think your approach is totally different from that, which is that code and the environment is essential. And if the code and the environment are bad, then you will get bad outputs, garbage in garbage out. So I think this is a different thing. It's It's like, you know, I don't know, maybe there's a dimmer switch or something, right? Like, you know, some parts are dark, some parts were light. This is why that maybe the kitchen is a better analogy. It's better, yeah. The restaurant, because you know, even as a restaurateur, you still might go to your restaurants every now and then to take a peek in, taste the food, right? Yeah, I think that's- The idea of sampling instead of blocking, I think is really important. Yeah, yeah, yeah. I think what would you say to people who are in, I guess you're obviously in a pretty security conscious environment where you're working, very security conscious. Maybe there are folks working in like medical applications or law or finance or something. I think of that like some PRs are kind of like two-way doors which is you can merge it and then revert it, right? It's changing the way back through. But there are some PRs that are one-way doors, right? that will cause data loss of some kind that will do something that can't be easily walked back. How do you deal with situations where most of your PRs, let's say, are one-way doors? Like, is this something you just wouldn't recommend or like, what do you think? Yeah, I think that's a really good question. I think that it all comes back to me to the quality of the verification that you're able to get out of your agents. And I think for domains where the work is verifiable, this is easier, right? And the one-way door has become two-way doors in a sense.

But I guess I don't know if you're working on something that is extremely, is very hard to verify programmatically, then I think, yeah, you're definitely in a position where it's very hard to get to that point. So I do think like, yeah, verifiability of the domain is an important aspect to be able to do this. And software engineering is just one of those things where it's quite verifiable in a lot of cases, maybe not totally. Other domains like mathematics, I think are another example of, not all of it, of course, but some aspects of mathematics can be verifiable if you write a proof, for example. And so, yeah, I think it's a great question that I don't really have the answer to. And I think that this is something the industry and us as engineers will have to figure out.

My sort of hope and prediction for the future is that we'll see more and more interesting, new agent-oriented programming languages. And one of the most fascinating ones that I've seen so far is this one called Bend, B-E-N-D, Bend. And that language is one where it kind of marries programming with proofs. There used to be a time where you actually had to write your proofs in a different language. And proofs, by the way, for those who aren't familiar, is this idea that you can formally verify that some code is correct mathematically, especially if you've written your code in a very functional programming way. But for the longest time, you had to do that in a separate language like Lean or TLA+, or I'm blanking on some of the other examples. But languages like that, where you would construct the mathematical proof and then use a solver, essentially, to check that you've covered all the cases, you don't have a race condition or whatever.

So yeah, I think trying to sum up the question, I think, yeah, if you are in a position where you can figure out how your agents can truly verify the work in a way that gives you confidence, you can actually, you know, have the PRs merge. Because if it compiles, right, if the proofs show you that it's correct, then why wouldn't you just merge it? But of course, yeah, not all domains are verifiable. Yeah, it's a tough one.

Okay, I think we've got to think about wrapping up because we are nearly on the hour. Have you got something after this? I mean, I've got something. I'll give my son dinner, but I can go a bit longer after you. Okay. Let's go five minutes longer then.

I think I just want to have one more question, which is I think I want to ask how you see P-Stack and how you see skills in general? Like in terms of, we talked about this before we went on air, which is like people think of it as like my skills versus your skills. And how do you combine frameworks together? How do you use P-Stack with my stuff? Like what should you take from each one? And because I think I see skills as sort of just derived from process basically, like they're just processes turned into words. And I would love to know how you recommend people take P-Stack and take my stuff as well and turn it into their own processes.

I think you shared a tip actually, today that I thought was actually very relevant, which is this idea that you go off and look at your previous transcripts, right, and you sort of mine for information of your own, look through your own, your own prompts, right, to the agents where you correct them, where you have to constantly intervene and take that higher level learning and turn that into a reusable skill, right? So that agents stop repeating that mistake. I think that P-Stack and your skills are very complementary. I totally agree with you that their skills really much just process. I mean, it's just at the end of the day, it's just English or language, it's just markdown. And I think you can definitely weave them, combine them in a way that makes sense to you. But I do think that everyone should have their own set of knives.

I keep going back to the cooking analogy, but it's so apt because every chef, when they go to a different job, when they go to a different restaurant, they bring their knives with them. The tools go with them. And so trust to me is really about trust in your own tools. And when you spend the time sharpening them and understanding them really, really well, you can do great things.

And everybody's skills and tool set is going to look different. Someone might find a lot of success combining your grill, me with docs, or Wayfinder skill with some of the execution skills in P-Stack as an example. Some people might use more of your skills. Some people might use more of my skills. I think at the end of the day, it really just comes back to, how much do you trust me and Matt? If you trust us both, of course, use our skills. But I also encourage you to look at your own transcripts. Tell the agent to look through some of the patterns that you've used, the times you've had to intervene, suggest turning them into lit rules or new skills.

The past chance I often say is like a treasure trove of context because it's like the process materialized. It's the real process, not an abstract idea in your head. It's the actual thing. And you can actually see how it happened in practice and extract so much information from that. And there's so much show that I actually turned a half a skill in piece called Recall, which is exactly that, where this was a pattern where I was working on a similar problem. So specifically, I was working on virtualization for the cursor application. And there were a lot of bugs. And so every time I started a new chat, I was like, oh, there's so much good context from the last one, though. I want to bring it over to the new chat. How do I do that? And that's where the transcript came about. And then recall was just a way for me to collapse and compress that workflow into a skill so that I didn't have to just say, I didn't have to write a long essay every time. Go look at all these chats, right? And then blah, blah, blah.

So I largely think of skills, especially as agents get more capable as really encoding workflows. Skills from last year were really more about almost like implementation details. Here are the exact script commands you should use. I think with the latest models, you can just delete those parts and just really focus on the workflow, right? and tell it it's more like the skill becomes more like a series of steps, a series of your process. And I think over time we'll see that skills get smaller and smaller, you know, more compact. And yeah, they're very, very compatible. Or you can, you know, if you want, why not read our skills, right? And come and combine them in your of your own, right? Combine wayfinder with potato mode and make your own custom mode, right? And the thing I love about skills are that they're so malleable. You can do anything you want in just language. Absolutely. There's nothing magical in them, right? They're just words. Yes, exactly. If there is any magic in them, it's just the words chosen and the phrases used and the thinking that's been done to turn those, like, take abstract process and turn them into language. And once that thinking has been done, then it's just there. available. It's on the surface and you just nick it.

Um, Lauren, thank you so much. It's been glorious. Yeah, this has been super fun. I really, really enjoyed talking to you. Hopefully we can do it again. I'd love to do it again. Yeah, I'd love to do it again. Absolutely. Um, yeah, we'll check in in uh one, two, three, yeah, one day. Let's do it. Part two. Well, thanks so much. I'm going to close the stream here. Laura and I will chat a little bit and stay here, but thank you guys so much Thanks for watching. Glory to you.

## 核心摘录

> **原节目**：并非 B站原创，是英文播客搬运。**主持人 = Matt Pocock**（Total TypeScript 作者；
> 播客中提到"你有 Total TypeScript、是 TypeScript 领域的 leader"），**嘉宾 = Lauren Tan**（pstack 作者；
> Meta React 团队 → Cursor → SpaceXAI）。**两位都是知名 skill 库作者** → 标题"两个最会写 Skill 工作流的人"。

### 1. ⭐ 核心命题：信任阶梯（trust ladder）+ 两个杠杆

**从"手动微管理一个 agent"爬到"agent 自己 merge 代码"，靠的是两个杠杆：**

| 杠杆 | 含义 |
|:--|:--|
| **环境（environment）** | 你改不了模型/harness，但**你能改 agent 运行的环境**：代码库、约束、工具、skills |
| **验证（verification）** | 让 agent **能自己看见自己工作的结果** —— 她称之为"给 agent 手和眼睛" |

> 原话：「即使你不用 pstack，我也认为**你的工具箱里最重要的一个 skill 是 verification**。」
> 「**loop 里最重要的部分，就是那个让 loop 成立的 verification**。」（没有验证，agent 无法自迭代，你就永远是中间人）

### 2. ⭐ Michelin Kitchen（米其林厨房）—— 为什么不用"软件工厂"

- 她不喜欢 factory 这个词（暗示**没有品质与手艺**）；厨房"更有抱负"（aspirational）
- **信任阶梯 = 厨师成长路径**：家常厨师（全都自己干，切菜备料打扫都是你）
  → 有帮厨（sous chef）→ **主厨**（不再自己炒所有菜，而是像厨房的 tech lead / CEO：
  什么时候订食材、怎么存、怎么备、什么时候备）
- **"工程师的新工作，就是花时间在环境上"**
  - 类比：没磨过刀、没用过 VS Code/Vim/Git，只用 Notepad —— 刀钝，什么都慢，deadline 压着，就被卡死在"微管理"的坑里出不来
  - **"每个厨师换餐厅都带着自己的刀。信任，其实是对你自己工具的信任。"**
- 到 2500 PRs 的前提**就是这个环境**：「我在一个厨房/一家餐厅上花了时间，现在我不必在那儿了」→ 可以开第二、第三家（每个项目 = 一家餐厅）

### 3. ⭐⭐ 环境怎么建（最可操作的部分）

**(a) 观察 agent 怎么失败 → 每次错误都退一步问："怎么把它变成一条 lint 规则，让代码库使它不可能发生？"**
> 原话：「这是另一个重要的部分 —— **观察 agent 如何失败**。每次你看到一个错误、看到有更好的做法，
> 就退一步想：**我怎么把它变成一条 lint 规则？**」

**(b) 约束空间（她拿 TypeScript 的 type narrowing 作类比）**
- 内部框架 **Dune**（"我们 Electron 应用的内部 Next.js"）+ **非常严格的 lint 规则** + **约定式模式**
  - 例：**每个 feature 一个目录**（通过 registry 扫描发现），代码不许往 God file 里追加
  - 来由：**Grok Bot 最早是 8 个 God file，每个 10000+ 行** → 逼出来的
- **好处：不 overload agent** —— 规则不塞进它脑子，而是让它**在环境里撞到**

**(c) 把确定性抽出来做成 CLI** ⭐
> 「我把 skill 里**确定性的部分抽出来变成代码/CLI**，只把**真正需要判断的部分留给 agent**。」
> 「skill 本身没什么意思 —— 它就是个 wrapper，包着几条轻量指令，说明怎么用里面的自定义工具。」
- 收益：**一致性**（不然每个 agent 都重建一遍世界、各做各的）+ 省 context + 快
- 应用例：**迁移（migration）用 code mod / 爬 AST 机械变换**，不是让 agent 想

**(d) ⭐ outer loop × inner loop**
```
inner loop  = 我的 agent 工程师在代码上朝我的 intent 推进
outer loop  = Slack / X / Linear / 邮件 / 日历 —— 外部信号（bug 报告、需求、反馈）
```
- **难点**：inner loop 里的 intent 快照会**过期**，新信息要人来搬运 → **你就是瓶颈**
- **解法**：连接两个 loop —— 让 agent **自己去拿 context**（Slack MCP / 自己 harness 里的订阅）
- **Cursor Projects = 云端 coordinator agent**（有自己的电脑）：**只管理不干活**，
  像 **executive chef / chief of staff**，把任务分给下属 sub-agent，驱动推进
  - **Cursor Projects = inner loop；Grok Bot = outer loop**（Grok Bot 能把外部 context 发进 Projects）

### 4. ⭐ 2500 PRs 的机制

- **不是**开了 2500 个 chat；是**这些 loop + 从终点倒推**：
  > 「最大的 unlock 是**从问题倒推：怎么让我的 agent 能 merge 它自己的代码**。」
- **PR 里很多不是 feature，是 "gardening"（园艺/维护）**
- **buffer / queue 机制**（重要）：
  > 有个 agent 一直找 React 坏 pattern —— 但**我不让它直接修，而是先 append 到一个文档**。
  > 每隔几天回看：「**这些其实是一回事**」→ 强制自己看大图景。
  > 纯执行模式下会漏掉大局；**有个 buffer 才有 artifact 让你用人的判断抓 pattern**。
- **review = sampling（抽样），不是逐道尝菜**
  > 「不能每道菜都尝，尤其是你有多家餐厅。**变成抽样 + 思考流程**。
  > 每天进去看 PR 质量、严格审视、找低效和坏 pattern。」
- ⭐ **course-correct 的是环境，不是那一个 agent**：
  > 「如果是一次性事件，没事。**但如果多个 agent 在犯同一个错、抄同一条捷径 —— 那是该改你的厨房了**：
  > 改 skills、约束、lint、类型系统，让这个问题不再发生。」
- **Full Autopilot（pstack 功能）**：为每个 PR **spawn 一批 verifier agent**，**fuzz**（真的跑应用、
  像人一样点、找回归），自己修，直到能 land
- **她 review 的是已经 land 的 PR**（早上看 commit history；有问题就 revert / 改 / 加 lint）

### 5. 边界与诚实的部分

- **"dark factory"之辩**：她说她的确实"有点暗"（agent 在她睡着时 7×24 干、自己 merge），
  但**与 Karpathy 最初的 vibe coding 完全不同** —— 那里"代码几乎不存在"，而**她这里代码与环境是命根子**（garbage in garbage out）
  → 「也许不是开关，是**调光器**：有些地方暗，有些地方亮」
- **单向门 vs 双向门**（最诚实的回答）：
  - 大多数 PR 是**双向门**（merge 了能 revert）
  - **但涉及数据丢失等的单向门**，结论是：**取决于这个领域能不能被验证**
  - 「如果领域极难程序化验证，那你确实很难到这个位置。**我没有答案**，这是行业要一起解的。」
- **对未来的预测**：会出现**面向 agent 的编程语言**；她提到 **Bend**（把编程与证明结合起来）；
  证明语言原本是 Lean / TLA+ 那一类

### 6. ⭐ 关于 skills 本身（收尾，观点很集中）

- **"skills 说到底就是 process 变成语言"** —— 就是 markdown、就是英文，**没有任何魔法**
  （"如果要说有魔法，就是**选词、用句、以及把抽象流程变成语言所花的那份思考**"）
- ⭐ **从自己的 transcript 里挖 skills（主持人给的 tip，她强烈认同）**：
  > 「回去看你以前的 transcript，**去挖你自己** —— 看你**纠正 agent 的地方、你不得不介入的地方**，
  > 把那个更高层的教训变成可复用的 skill，让 agent 不再重复犯错。」
  > 「也可以直接让 agent 去看你常出现的 pattern、你介入的时刻，**建议把它们变成 lint 规则或新 skill**。」
  > 「**transcript 是一座 context 的宝库 —— 它是被物化的流程**，是真实发生过的，不是脑中的抽象。」
  - 她因此做了 skill **`Recall`**（起因：做 Cursor 虚拟化时 bug 太多，每次开新 chat 都想要上一个的 context）
- **skills 会越来越小**：
  > 「去年的 skills 更像 implementation details（**这里是你该用的确切命令**）。
  > 用最新的模型，**那些部分可以直接删掉，只留下 workflow** —— skill 变成一系列步骤、你的流程。」
- **"每个人都该有自己的刀"**：她的 pstack 与主持人的 skills **高度互补**，可以自由混搭
  （例：把主持人的 `grill me` / `Wayfinder` 和 pstack 的 execution skills 混着用）

## 个人解读

> 仅为阅读时的联想，非原文观点。

- **这条的含金量在"环境工程"这一块**：它把"怎么让 agent 可靠"从"换更好的模型"翻转成
  **"改 agent 运行的环境"**（代码库约束 + CLI 化 + 验证基础设施）。这个翻转对我们直接可用。
- ⭐ **与我们已经在做的高度同构，而且我们有些地方走得更前**：
  | 她的做法 | 我们的对应 | 状态 |
  |:--|:--|:--|
  | 把确定性抽出来做成 CLI | 门禁脚本 / `derive.py` / `check_*.py` | ✅ 已在做 |
  | **每次 agent 犯错 → 变成 lint 规则** | **`check_tool`/`check_consistency`/`run_regression` + 回归用例固化** | ✅ 同构（只是她叫 lint，我们叫门禁） |
  | skills 只是 process 的语言化 | skills 体系 | ✅ 同构 |
  | **从 transcript 挖 skill** | **`understand-the-master` 的 L3 判据捕获回路** | ✅ 同构（我们已有机制） |
  | verification = 第一技能 | 验证闭环 / e2e-test-suite | ✅ 在 core |
  | outer/inner loop + coordinator | **default 主管 + code/content 特化 profile** | 🟡 **结构相似但没显式做成 coordinator 派活的机制** |
  | buffer/queue 抓 pattern | — | ❌ **我们没有**（我们倾向于发现问题立刻修） |
- ⭐ **最值得抄的一条：「buffer before fix」**：她发现坏 pattern 时**先攒进文档、隔几天回看找共性**，
  而不是立刻逐个修。**我们目前的模式是"发现即修"**（如今天七个问题逐个闭环），
  **代价是可能错过"这些其实是同一个问题"的大图景** —— 而这一整轮正好印证了这个风险：
  同样的根因（"知道≠会做，缺必然触发点"）我今天撞了**两次**（实体层过期 / KB 不吃）。
  ⇒ **"攒着回看找共性"这个动作，值得进我们的流程。**
- **另一个可引用的判断**：「工程师的新工作是花时间在环境上」——
  这句话可以支撑"为什么我们花时间做门禁/脚本/skills 而不是急着出货"。

## 待验证点

| # | 待验证 | 说明 |
|:--|:--|:--|
| 1 | 嘉宾的称呼 **"Potato"** | 转写如此（且她自称"我当然是叫 potato"，还提到 "potato mode"）；同一人在 BV13be26zEqG 里是 **Lauren Tan**。**是昵称？还是 handle 误听？待核** |
| 2 | 主持人身份 | 转写里主持人被称"**Lauren**"（结尾"，Lauren, thank you"）—— 与嘉宾同名 **矛盾**，疑为 Whisper 把两人名字都听成 Lauren，或称呼错位。**主持人依内容推断是 Matt Pocock**（Total TypeScript），**待核** |
| 3 | "**2,500 PRs / 月**" | **自述**，无审计（她自己也说"很多是 gardening，不是 2500 个 feature"）。与 BV13be26zEqG 里的"1,000 PRs"口径不同，**引用必须标出处与日期** |
| 4 | 内部框架 **Dune** | 只听写，未见其他来源 |
| 5 | **Bend** 语言 | 听写为 B-E-N-D；拼写与是否确有此名待核 |
| 6 | 主持人的 skills 名（`grill me` / `Wayfinder` / `how` / `why` / `unslop`） | 均为听写，拼写待核 |
| 7 | 她自建 skill **`Recall`**（/`Recalc`） | 听写；用途清楚（从历史 chat 压缩流程成 skill），名字拼写待核 |
| 8 | **"Netflix"**（"I used to work at Netflix"） | 与 Lauren Tan 履历（Meta React → Cursor）是否一致待核 |
| 9 | GitHub 仓库名（听写 "**Potato slash Noodle and OODLE**"） | 明显错听，待核 |

## 关联问题

- 🔗 **与库里既有条目的关系**：
  - `bilibili-BV13be26zEqG-ai-agent-team-grokbot-pstack-code-review.md`（**同一人 Lauren Tan**，同日对话实录）
  - `03-Wiki/氛围编程/方法论/流程与治理/七阶段AI开发流程-用CodingAgent交付成品的方法论.md`
    （**提炼自 Matt Pocock《AI Coding for Real Engineers》** —— 即本片主持人）
  - `01-Raw/Bilibili/bilibili-BV1S6EY6fEUc-loop-engineering-next-paradigm.md` / `BV1zYEz6oEx7-loop-engineering-practical-guide.md`（loop 主题）
  - `01-Raw/Bilibili/bilibili-BV1jRD6BvEAS-harness-engineering-multimodal-view.md` / `BV1tfoNBqEtN-beyond-vibe-coding-harness-sdd-team.md`（harness / SDD）
- ⭐ **对 code profile 的直接价值**（这条是全库对 code 最相关的一条）：
  - "改环境而不是改 agent" ↔ code 的 `llm-quality-gates` / `code-conventions-audit`
  - "确定性抽成 CLI" ↔ code 的脚本化门禁
  - "outer/inner loop + coordinator 派活" ↔ code 的 kanban-orchestrator（**可升级为显式 coordinator**）
  - "buffer before fix" ↔ **code 的 fix-retro / issue-triage 缺这一环**
- **可迁移判据**：**验证能力决定你能放权到哪一步**（verifiability of the domain）
  ↔ 我们的「L0–L4 分级：每步标能不能自动验证」

## 抓取备注

**① 语言坑（本片是首例，后被复核确认）**
标题为中文、B站搬运，但**正片是英文原声**（3935.53s / 65:36）。
首轮误用 `language=Chinese` → **全篇中英日西混排乱码，白跑**；改 `language=en` 重转。
⇒ 见 skill `bilibili-subtitle` 的 Step 1.5（后经 BV13be26zEqG 复核第三次踩到，已在 skill 中固化）。

**② LLM 后处理：本片走了（15 块，比值 ~1.00），但该路径后来被否决**
本片用 AMD DeepSeek-V4-Flash 后处理 15 块，长度比值正常。
**但 2026-10-07 在 BV13be26zEqG 上实测该通道会静默概括（块比值 0.799，丢 23%）** →
**英文场景已改为"只机械修名、不走 LLM"**（见 skill `bilibili-subtitle`）。
⇒ **本片的转写里仍留有大量明显错听未被修正**（Potato / PSAC / GROC / Corsair / Carpathy / lit rules …），
**阅读时需注意；正式引用前建议按新流程重跑一遍机械修名。**

**③ 本次（2026-10-07 晚）补写说明**
本条目首次入库时（2026-10-07 凌晨）**只写了转写，五个内容段全空**（壳子）。
经用户指出"KB→code 消费断链"时发现，本次补全。
**未重跑转写/修名**（避免覆盖已验证的 58840 字正文）；错听清单见 ②。
