---
title: "一个人，如何带一支 AI 团队？Lauren Tan 实演自动修 Bug、代码验收【中英字幕】"
source_url: "https://www.bilibili.com/video/BV13be26zEqG/"
source_type: "video"
source_platform: "bilibili"
author: "对抗熵增2046"
author_id: ""
publish_date: "2026-09-18"
fetch_date: "2026-10-07"
keywords:
  - AI-Agent
  - cursor
  - engineering
  - efficiency
  - 评测
  - vibe-coding
  - Skill
state:
  phase: raw
  time_raw: 2026-10-07T22:49:50
priority: 3
language: "en"
notes: "yt-dlp 下载音频 + Whisper small (WSL GPU, fp16=False, language=en【实测三处采样检测所得，非按标题猜】) 转写单P 28.7 分。**未走 LLM 后处理**：实测 AMD DeepSeek-V4-Flash 会概括丢 23% 内容 → 弃用；改机械修专名（148 处，零幻觉）+ 程序分段。"
duration_seconds: 1720
duration_formatted: "28:41"
---

# 一个人，如何带一支 AI 团队？Lauren Tan 实演自动修 Bug、代码验收【中英字幕】

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | 一个人，如何带一支 AI 团队？Lauren Tan 实演自动修 Bug、代码验收【中英字幕】 |
| 原节目 | **MTS 播客**（主持 × **Lauren Tan**、**Roshan Sadanani**）|
| B站 UP 主 | 对抗熵增2046 |
| 发布时间 | 2026-09-18 |
| 总时长 | 28:41 |
| BV号 | BV13be26zEqG |
| 原声语言 | **英文**（三处采样检测 en=0.9988 / 0.9968 / 0.9970）|
| 说明 | 视频标题是中文 + 【中英字幕】，但**正片为英文原声** —— 教训见抓取备注① |

## 原文内容

> **转写说明**：Whisper small 英文原声转写，**未做 LLM 后处理**（理由见抓取备注②）。
> 已做**机械专名修正**（148 处，零幻觉）：`Grock/GROC/graph bot/Graph.Bud/Grotbot/RockWatt/Crock-Bot` → `Grok Bot`；`Grap/Grot/Graph 4.6` → `Grok 4.6`；`cursor` → `Cursor`；`SpaceX AI` → `SpaceXAI`。
> ⚠️ 说话人未标注（Whisper 不区分说话人）；`grid work`（L165 附近）等个别词存疑，见待验证点。

I talk a lot about this bot that I built called Benny, and I wanted to figure out how would I make it so my agents could just automatically fix bugs for me while I sleep. And so that was an inspiration for some of our earlier experiments, like what if everybody could define one of their own bots, you know, give it an identity, and give it things like its own computer plus routines and automations. So like I have bots right now that are, you know, every time someone gives us feedback on Grok Bot, My bots are automatically going off and fixing them for me, and I just like review their code. Hello everyone, and welcome back.

Today I'm joined by Lauren Tan and Roshan Sadanani from Cursor. And earlier today, Cursor and SpaceX jointly announced Grok 4.6. So excited to talk to you both about the new model and also to do some live demos of Grok Bot. Lauren, Roshan, welcome to MTS.

Thanks so much for having us. Yeah, great time here. So excited. I know you just informed me right before we went live that we're actually going to do a live Grok Bot demo.

So before we just jump into that, can you share with me about what Grok Bot is and how does Grok 4.6 maybe change what it's capable of? Yeah, we're super excited about Grok Bot. Tons of really great reception yesterday. And so it's been sort of a labor of love to bring it live over the last little while.

So hopefully folks have had a chance to try it out. If you haven't yet, you can go sign up and try it out right now. Really just motivated by making it easier to interact with and use agents. This product got a ton of internal PMF when we started building it internally.

Everyone from go-to-market teams to ops teams to engineering teams to product teams just like latched on to it. And just really found fun ways to use agents that I think make a lot of sense for their jobs. That's so cool. How have you guys been using it directly?

you found internal PMF with your team. What was that specific moment? Was there an example that happened? Yeah, I think like so early on, there was this very small team prototyping and building Grok Bot.

Um, and, uh, it started out very organically, like, you know, just, it was just them using Grok Bot for themselves, but they started sharing it with a few people and it started, you know, like I started to use it. I used it to book the Odyssey. I'm at 70 inch. Wow.

Oh my gosh, that is a milestone, a new benchmark. Is it able to get tickets there? But yeah, it really was very exciting to be able to use agents to automate like so many different things that you might not necessarily, so really think you can. And Grok Bot has its own computer, so it's like super powerful.

It runs even if you're not at your computer. So it's been, it's been awesome. Yeah. And a little curious, how does it work internally?

So do internal teammates just test out different things and then ones that are starting to take off? We're like, okay, how do we make this into a commercial product? Yeah, I think that's like roughly how it works. We think that our colleagues are pretty high-taste when it comes to using products and also just like using agent products.

And so for a lot of things we build we sort of ship them internally and get feedback from the other folks of the company who are using them daily. Look for that internal PMF and usually that's been a good sign for kind of releasing something into the broader world. and so Grok Bot kind of followed that exact same process. What was really unique about Grok Bot though, I think is that kind of what I was saying earlier, sort of regardless of role everywhere from like ops to go to market to insert your role here, someone found a use case for Grok Bot.

And a lot of that's because it just talks so seamlessly with all the tools you already use. And then obviously like Lauren was saying, it has its own computer. So it's sort of this persistent agent that sort of felt really novel to interact with. And so I think some of those interactions, which we'll hopefully show you in just a second, are really, really cool.

All right, let's jump in. I feel like I got all of the preview. I'm ready to jump into the demo. Let's take it away.

Yeah, I can start. Maybe we can go back and forth a little bit. So what you're looking at here is Grok Bot. And this is my team of bots that we're looking at.

I have a coordinator agent here who's my chief of staff and knows stuff about my calendar and can actually message my other agents. So can check in on the other agents and how they're going. So here's my coordinate agent messaging Shopee, who helps me buy stuff on the internet and learning about the recent purchases I just made. Like Odyssey tickets?

Totally, yeah, like Odyssey tickets or yeah. My groceries maybe, that was a use case we saw internally that was really fun. But then, you know, these agents also have their own computer and can be signed in to all the tools you use. And so, right before this, I just set up a marketing agent who has access to my LinkedIn.

And so if I hit this button here, we can see that this marketing agent has its own screen, just logged into my LinkedIn, and actually just pulled some of my LinkedIn posts just by browsing on Chrome. So I'll just go ahead and ask him to update LinkedIn for me. We'll see if we can do this. We want to post that we're talking about Grok Bot Live.

Actually, don't forget to tag the right MTS account. Or MTS Live. MTS Live. And what's really cool about these agents is you can just chat with them like you're chatting with a colleague.

And that was a real huge part of the design inspiration here is just making it so that this feels like you have a really intelligent colleague that's hanging out with you in the chat versus having to like wait your turn maybe or wait for or some thinking to happen or whatever else. So yeah, he's gonna start working and trying to post from my LinkedIn. So we'll check in on him on in a second. The other cool thing that we've seen a lot of cool use cases with is putting together sort of presentations or helping automate a lot of the more drudgery that might happen in your job.

So we have a channel internally called Grok Bot Wins. And so I'm gonna ask this agent here, my chief of staff, to put together some feedback from that channel and maybe actually do it in Figma slides so we can maybe show those out. So yeah, let those guys cook for a little bit. Oh, and it looks like our post might be going live.

You can see the computer out there. That was really fast. Oh, that's super fast. That is really cool.

I hope it makes it available to anyone. It looks like it is gonna do that. Oh my gosh. And I hope he found the right MTS live account, but I think he did.

Yeah, that looks right. Okay. Nice. Cool, cool, cool.

Well, yeah, we should have a LinkedIn post coming up really soon there. Okay, and we'll post this clip also on LinkedIn afterwards. That sounds great. We'll do some tagging.

We'll do some tagging. Exactly. Oh my gosh. So you guys announced this all yesterday.

What was the reception like? Maybe Lauren would love to get your opinion here. Yeah, I think the reception has been super positive. You know, people really love the Grok Bot identity, the animation, the logo is really fun.

And not to mention, yeah, like all the use cases where you can use Grok Bot are, I think we've heard a lot of cases where it's like very intuitive, you know, it looks like iMessage. I've seen a couple of people share Grok Bot with their mom and their mom's onboarding onto Grok Bot. So I've been really blown away by how well received Grok Bot is. There's still a lot more to do, right?

Like there's, we have a few bugs here and there that we have to fix. But overall, it's been very positive and very excited that we finally got to launch it. And you announced another announcement today. So pairing those two together, what is now possible?

So Grok 4.6 is really powerful. It's much more intelligent than 4.5 is at the same token cost. So I think for coding tasks and the type of work that I do, because I do a lot of engineering work, I use Grok 4.6 a lot for that. And it's just way more capable.

It's really, really fast. I still use the other models too, like Fable and Sol. But Grok is just so fast. And it's affordable.

It's cheap. So I really like using it. Yeah, I think one thing that we talked about when we launched Grok 4.5 with the SpaceXAI team was sort of this idea that we're gonna train models for more than just code. And I think what we're continuing to see with Grok 4.6 and some of the investments in Grok Bot, like really, there's a lot more that's possible with these really great models.

And so yeah, we're just excited for the models to keep improving, to be part of the discussion on the frontier of models. And yeah, to be able to bring that into the world. Yeah, I'm really excited what you show here because I know that Cursor started off mainly in the agentics coding space. I was sharing earlier that Cursor is actually my gateway into starting to use vibe coding tools in general.

It was the first actual tool I used. I used the Cursor models and then I just kept updating from there and I still to this day use it. And then I realized before I was actually testing out Grok Bot, I was like, oh, you can use this same tool to do research, to do other things. And still, even though people say agents are expanding and growing, It's still mainly coding agents because the actual infrastructure in the UX to use agents for everyday things sucks.

I think Open Claw was maybe the first mainstream, but like you mentioned, I don't think my mom would ever be using Open Claw. And even myself, I set up a whole Open Claw in a telegram. It looks kind of like this in my UI and I have my shopping agent, my all that stuff, and it breaks all the time. And I'm always like, like trying to fix it.

This is awesome. I love the whole UI and structure. How did you, what was like the design process going through creating this, creating Grok Bot? Yeah, I mean, the brief was basically keep it simple to be a little cheeky, and I think that's actually really real.

It's like a lot of AI applications have, you know, a lot of control and power that they give you, but sometimes that power is like balanced with complexity. And so really our design brief here was like, how can we make this really simple first and foremost? And so that's kind of where the messaging interface just became a little bit inspired from, and then of course some of the design touches that we added over time. I don't know Lauren if you'd add anything, kind of having built it all.

I would say I built it all, but I think that the team really strove for a very clean, simple user interface, because if you've used Cursor, you're probably like a developer power user. It's like a lot of knobs and whistles and it's very tailor-focused for coding. And with Grok Bot, we really wanted to take a fresh perspective on what would it look like if your agent was really more like a colleague, right? And so you don't necessarily want to micromanage a colleague and say, what tool calls are you using right now?

But you want to talk to it like a person. You want to see what they're doing on their computer. But yeah, it's like, so we've tried to keep the interface really elegant and simple. Really cool.

I love that I have both of you two on the interview because we have the product side, We have the software engineering side. It's a whole team behind the scenes too. There's a lot of work on this. Wait, there's more people besides just YouTube?

Yeah. On it? No, for sure. And so having you both here, you get a really comprehensive overview of what it actually takes to create Grok Bot and get this product into the mainstream.

I do know the user might be a little bit different from the typical Cursor user. Who are you envisioning are going to be the mainstream adopters of Grok Bot? Yeah. we really see this being useful for everyone.

So kind of like what we were saying when we saw this launch internally, I think there's a lot of work out there that's just rife to be made more efficient. And I think the motivation for why we built this internally is we actually saw a bunch of folks within Cursor who were building their own agents, kind of like constructing the chats together, building Slackbots. Actually, Lauren had a really famous Slackbot that still lives in our Slack instance. And it's sort of like that takes a lot of context to put together.

And so the idea was, well, could we package that up? And these bots were for, for deployed engineering and for like software engineering, for our ops teams, and really just wanting to say like, could we productize that in a really, in a really fun way. So, yeah. Yeah.

So yeah, I talk a lot about this bot that I built called Benny. He's like this little dog. This is Avatar. But the idea I had with Benny was really, you know, like, I'm a fairly lazy person.

And I wanted to figure out how can I, you know, we're getting so many bug reports for Cursor, right? And I wanted to just fix them all. And so I started thinking about how would I make it so my agents could just automatically fix bugs for me while I sleep. And so that was the inspiration for some of our earlier experiments with, you know, building like a more like persistent bot.

And so I think there were some ideas that we took from there. Because I got so many questions, like how did you build any, how can I build my own? I think that inspired some of the thinking behind Grok Bot, like what if everybody could define one of their own like bots, you know, give it an identity and give it things like its own computer plus routines and automations. So like I have like a bot like bots right now that are, you know, every time someone gives us feedback on Grok Bot, my bots are automatically going off and fixing them for me and I just like review their code.

So what's your job now? Has it changed? It's definitely become interesting. It's like I'm almost like a manager for my digital colleagues.

Yeah, so it's pretty interesting. It's actually remarkable how much of Grok Bot was built with Grok Bot, too. Wow. It's been a really cool feedback loop where these agents can self-triage issues.

They can write code, and so they can connect to cloud agents. And I don't know if you have a demo of that, Lauren. That was the one we wanted to show. Yeah, I do.

I love these demos. This is so fun. Is this great? You explain something?

Exactly, you explain something and you're like, wow, I do have a demo pulled up. Let me just show you now how it actually works. We'll continue monitoring right after this message from our sponsors. 11 Labs, AI that communicates at human level across every channel and modality.

11Labs.io slash MTS. Scale your startup on Neon. Millions of developers and startups have already chosen Neon for their backend. Start on the free plan or get up to $100,000 in credits for your startup at neon.com slash MTS.

Special thanks to our sponsor, Kong, the AI connectivity platform. Connect APIs, LLMs, agents and systems with serious security and governance. konghq.com Yeah, so I kind of, I asked my chief of staff already, like if there's any interesting bugs that we saw today. And it's found a few.

You can also see I have X open on the on the my box computer just in case. But yeah, if you know, I can, I can tell it to dispatch. So like I have a have a sand team over here or sorry, a Grok Bot team. So each of them kind of are responsible for a different feature.

And so now my chief of staff is going to like send off those tasks to those agents. And in a minute, we'll see a bunch of messages that they'll send to my team members. And then they'll go off and actually work on those tasks. And then at the end of it, I'll get a pull request that I can review.

I'll get videos. I'll get a screenshot. And yeah, she has another example where this is one of my engineering team agents. And I think this is almost like a feature that's not super obvious.

But if you set up cloud agents on Cursor, your Grok Bot bots can actually kick them off. So like here, we have a cloud agent that's running with its own computer that this agent is managing. And so it's got a bunch of things in flight already. So I have a bunch of PRs to review later.

I think there's something really exciting about the future of software development here too, where it's really talking to and working with a bunch of agents that are doing specific tasks. And then you kind of just step back and become the manager of them. And it sort of feels like that vision is coming true in a really fun way here. That's amazing.

And I see here it's a bunch of cat photos. So all your agents are actual cats? Yeah, I just love cats. So I decided to give them silly profile pictures just to press analyze my Grok Bot a little bit.

I mean, the default Grok Bot avatars are super cute as well. and I added these before we added those, but it's just having a bit of fun, you know? Yeah. Roshan, you hinted towards something that is a trend that of course is happening with the future of agent decoding and Cursor has been at the front and center of seeing all of this happen.

More and more code is getting automated and is done by these agents. And so as a human, you become this puppeteer of agents who are handling all these tasks for you. I know that's a world that you're particularly excited about. Can you share a little bit more?

Why are you excited about that? What does that actually unlock at maybe the human level that people in the mainstream audience might not realize? Yeah, totally. I think that if I had to pick one word, it would be efficiency.

I think there's so many ideas in people's heads, regardless of role again. I have so many product ideas. I want to build into Cursor. And it's the limiting factor.

There's always some bottleneck in that idea to existence pipeline. And so I think the promise of being able to throw fleets of agents at these problems and then have them produce things that are really high quality and sort of aligned with the taste that I would myself put into our product. That's the vision, right? Like that's sort of the dream.

It's like being able to go from thought to existence. So to me, that's the thing to work towards is can we build these things in a way where whether I'm managing a bunch of agents or asking agents to manage other agents or working with Lauren's agents or whatever that looks like, we're able to really shorten, compress, compress, compress that cycle more and more. And I think if you kind of like look at the evolution of Cursor as a company, that's sort of how we've built in a lot of ways, built ourselves towards that future is by, you know, continuously introduce more and more sort of like agent tools and complexity there. So yeah, I think that's the vision and we're excited for it.

And then how has it changed on the software engineering team? What differences from when you started working at Cursor to how it is now? I think it's like the way I see engineers roles evolve in the agent world is, you know, like I mentioned, you're sort of like an engineering manager for your agents. But I think a big part of our responsibility now as engineers is also to keep the code base in a condition where product managers, designers can contribute high-quality code.

And that's something I talk a lot about on Twitter as well, which is investing in refactoring, rewriting, even rewriting your code base so that agents can really thrive, even if they're not very smart agents sometimes. things like encoding your rules and your style guides into actual like lint rules or hard constraints that fail CI. So that again, I think the big unlock is as an engineer, I can empower so many other people to do things that they couldn't do before. And I can do things that I couldn't do before as well because I've done a lot of big refactors and migrations at Cursor.

And I did them like mostly by myself. Wow. Like with one of the person. With all the cat agents.

Yeah, all the cat agents were just going wild. And like, you know, I converted, you know, a bunch of stuff, you know, which would have taken me or a team of engineers months or even years to finish. Wow, that's incredible. And as an outsider's perspective, you might think, OK, now that agents can do all this coding, what's the role of a software engineer?

And if you actually look at what's happening on the ground, There's more demand than ever for more and more of these engineers. And it's probably towards something that you hinted now that you can build software with the thought to execution timeline is getting so condensed. We just now get something like Grok Bot that started off as that's something you guys are building. And then you could use Grok Bot to now build Grok Bot and put it out into commercial production.

Is that also what you're seeing just as a trend happen more and more? Yeah. I mean, I think the time to prototype ideas has gone down a bunch. And so it's really quick to test things.

I think we've been able like the team behind Grok Bot has been able to move incredibly quickly just because of these tools getting better. And obviously the model is getting better is a huge component of that. And so, yeah, I think that like to bring it to the Grok Bot side of things, the motivation there is really around how can we make this product more and more helpful for folks. As far as the trend, I think like this is going to get easier.

I think there's still a really strong role for people to play in all that too, whether it's the taste argument or some other combination like that. But yeah, I think it's just ideas are, you know, abound and it's just going to be exciting to see more and more of them come to reality. Yeah, the sort of analogy or metaphor that I personally like a lot is this idea that, so I like food. Yeah.

I'm a big lover of food. And I kind of think of my agents as sort of like a kitchen, a Michelin kitchen is what I call it. And so like maybe my role has sort of changed in that maybe I'm not, you know, cooking all the food myself anymore. Uh, but I have a team of bots and agents that are, that I've sort of hired, right?

And I've trained through skills or, uh, like refactoring to do good code the way that I would have done it. And so my role is becoming more like, you know, like a head chef, right? Like I, I, I maybe assemble a plate to the food. I, you know, I, I own the quality control.

But if you invest a lot in having early capable team of agents, you can just do so much more. Now think about that with every engineer in your team, can have one of these teams behind them. You can solve a lot more problems, you can build more features, not all of them should be built, but you have much more productivity and velocity. Yeah, I do like what you hinted about the internal culture of you actually build things you tested out and that employees themselves at Cursor have a certain taste for what other engineers with other product people would other consumers I guess in general would want to see exist.

Do you have any hints that you can maybe share? Okay, if you don't, but of what might be coming up or even something that people are working on internally. Yeah, I mean, we definitely want to make Grok Bot better. We launched this as a beta yesterday.

And so tons of feedback coming in of all shapes and sizes. Our goal there is just to make this as helpful, these assistance, these bots as helpful as we can. And so definitely going to continue investing there. Obviously really excited about the models getting better too, and excited to be a part of that conversation and to have fun to your models now.

And so I think we're going to continue to just invest a bunch in that space. And then some more fun stuff to come too. But I think overall, just very bullish on the future and the future of both coding agents, but also general purpose agents. And I think it's going to be a really fun time.

Definitely. Yeah, I personally am really excited to see more performance and reliability as an engineer and that's something I care about a lot. But yeah, you have some really interesting features that we're debating. Actually, one thing that I hacked into Grok Bot when in the early days was support for iMessage.

We can actually text your bots. I don't know if we'll add it for Grok Bot, but I know it's like a common ass. So we're definitely like, you know, thinking about things like this where, again, it's like the mental model is these are colleagues, right? You know, so like how do you, like your, your colleague is accessible, not just through Slack, right?

That you can text them, you can call them. So it's interesting to kind of imagine a world where you have these always on colleagues that you can talk to at any time from anywhere. And they're just off doing grid work for you. Oh my gosh, I can't wait to be able to text them or call them.

I saw this meme where it's like my agents were talking to each other and they're stand up and they're like, sorry, I was off all weekend. I'm like, you're an agent. I don't know exactly what that means. Yeah, maybe we need agent PTO as a taxation frontier.

Yeah, agent PTO. Turn your computer off. Let's do it. One last thing I did want to bring up, because this was really impressive, is you guys, of course, are not just working on Grok Bot, not just working on the application layer, but also on the model layer and Grok 4.6 the benchmarks came out on Cursor bench 3.2 and we're really impressive and I wanted to address them here on air.

While we still have time you had Grok 4.6 extra high scored 70.8% an average cost of 2.81 per task for context fable 5 max scored 70.5% but at 17.32 dollars. This is a huge change. How does this model maybe change how the everyday consumer actually interacts with agents with AI as a whole? Yeah.

Go ahead. So yeah, this is definitely like very top of mind for me because, you know, I think about this a lot because I work at Cursor, I have unlimited tokens and so I can just, you know, you know, go crazy with token maxing. But obviously a lot of our customers and our users are, you know, are more cost-conscious. So personally, what I'm most excited about is this idea that you have a very efficient model that is as good as some of the other big models, but a fraction of the cost.

And I feel like that's a very important topic that a lot of leaders and engineers are having right now, which is the rising cost of using AI. So I think Grok 4.6 is a really interesting choice in that discussion. Every company is going to have their own requirements as opposed to the type of model mix that they use. So I think Grok 4.6 makes a very compelling option if you're considering between some of the bigger models, which are also extremely capable.

but you want something like a little bit more cheaper. Grok is like an excellent choice. Yeah, it's like if you have a budget of 20 bucks to do all of your AI tasks and the cost per task goes down, it's like you can just do more tasks. And so I think the efficiency game is just such a fun one to play because it feels like you just can do more.

Like you can have more bots or write more code. And so yeah, just like this idea, and I think this is happening across the industry, which is very exciting, but just being able to do more things with the tokens or just like it's wildly cool to see. So yeah, I think we are investing a ton in efficiency specifically because we think that's just a really great direction for these models to go in. And obviously intelligence matters a ton too.

So yeah, we're excited about the results. The benchmarks are pretty cool. Yeah, that was really cool to see. And I'm super excited specifically about lowering costs for such a great model.

It provides better capabilities for startups who maybe don't have the same amount of resources, or even just indie hackers who want to experiment. but you can't be paying for all of your token costs out of pocket, this is just getting a little bit crazy. So it's really starting to level out the playing field. And I'm incredibly excited about what that actually means, what that looks like for the future and all of your guys' products.

But Lauren, Erosion, really wanted to thank you guys for coming on MTS today and sharing more about Grok Bot, Grok 4.6 and all of the fun updates. Thanks so much for having us. Yeah, it's really fun. And if you haven't tried Grok Bot, give it a shot.

It's really great. I'll definitely have to give it a shot. Please give it a try. Appreciate you guys for joining.

And we'll be back with MTS. A huge thanks to MTS sponsors. Blitzy, Autonomous Software Development for Enterprise Code Basis. Ship 5X faster, blitzy.com.

AdQuik, make your brand a billboard out of home advertising as easy to scale as digital, adquik.com. Arena, measuring AI performance in the real world, arena.ai. Support for the show comes from VCX, the public ticker for private tech. The US stock market started history's greatest wave of wealth creation.

From factory workers in Detroit to farmers in Omaha, anyone could own a piece of the great American companies. But today, our most innovative companies are staying private longer, which means everyday Americans are missing out. Until now, introducing VCX, a public ticker for private tech. GetVCX.com for more info.

That's GetVCX.com. Carefully consider the investment material before investing, including objectives, risk, charges, and expenses. This and other information can be found in the Innovations Fund, Prospectus.GetVCX.com. This is a paid sponsorship.

## 核心摘录

### 1. 产品：Grok Bot —— "一支 bot 团队"
- Cursor / SpaceXAI 的产品；**每个 bot 有自己的电脑**，可登录你日常用的工具（LinkedIn / Figma / Chrome），**即使你不在电脑前也继续跑**
- 交互形态刻意做成 **iMessage 式聊天**："像跟一个聪明的同事聊天"，而不是等它思考、排队、看工具调用
- 内部 PMF 先行：先在公司内 ship 给同事用（ops / GTM / 工程 / 产品都找到了用法），看到内部 PMF 再对外发

### 2. ⭐ 架构（对"一个人带一支 agent 团队"最直接的部分）
```
coordinator agent（"chief of staff"，知道日历）
        │  能给其他 agent 发消息、check in
        ▼
按 feature 分工的专家 agent（"each responsible for a different feature"）
        │  写代码
        ▼
Cursor cloud agents（Grok Bot 的 bot 可以启动它们）
        ▼
产出：**一个 pull request 给你审** + 视频 + 截图
```
- **闭环**：chief of staff 找到今天的 bug → 派活 → 写码 → 出 PR → **人只做 review**
- **"Grok Bot 相当一部分是 Grok Bot 自己建的"** —— 自我 triage issue、自己写代码

### 3. 角色变化：工程师 → agents 的"经理"
- Lauren 原话："我几乎成了**我这些数字同事的 manager**"
- 一个人（+ 一群"猫头像" agent）做完了本该一个团队**几个月甚至几年**的重构 / 迁移

### 4. ⭐ 她的两条工程论断（最有迁移价值）
1. **投资重构 / 重写** —— 让代码库处于"**agents 能 thrive**"的状态（哪怕 agent 不聪明）
2. **把规则和风格指南编码成真正的硬约束** —— **lint 规则、会 fail CI 的 hard constraints**
   （⇒ 这与"一致性门禁 / 脚本化门禁"是同一个思想，只是换了个说法）

### 5. Michelin kitchen 比喻
> 我不再自己炒所有菜了。我**雇**了一支 bot/agent 厨房团队，**通过 skills 和重构去训练**他们按我的方式做好代码。
> 我的角色变成 **head chef**：装盘 + **控质量**。

### 6. Roshan 的愿景：efficiency
- 一个字：**efficiency**；目标是"**thought to existence**"，把这个循环"compress, compress, compress"
- "**throw fleets of agents at these problems**"；"**asking agents to manage other agents**"

### 7. 模型：Grok 4.6（同日与 Cursor / SpaceX 一起发布）
| 模型 | Cursor Bench 3.2 | 每任务成本 |
|---|---|---|
| **Grok 4.6 Extra High** | **70.8%** | **$2.81** |
| Fable 5 Max | 70.5% | $17.32 |

⇒ 讨论焦点是**"AI 成本上升"**下的性价比：同等能力、约 1/6 成本

### 8. 其他
- Lauren 早期自己 hack 进 **iMessage 支持** —— "你可以给 bot 发短信"
- 自嘲式玩笑："agent PTO"（agents 也要休假）
- 片尾为赞助商口播（11Labs / Neon / Kong / Blitzy / AdQuik / Arena / VCX）

## 个人解读

> 仅为阅读时的联想，非原文观点。

- **这条视频与我们正在做的事高度同构**：他讲的是"一个人 + 一支 agent 团队"的公开样本，
  而我们已经在做的（skills 沉淀、门禁脚本、`/goal` 长任务、载体无关设计）是同一路线的另一条腿。
- **「把规则编码成 lint / fail CI 的硬约束」= 我们昨天刚做的「一致性门禁 + check_tool/run_regression」**。
  别人用一句话说出来的原则，我们已经落成了可执行脚本 —— 这是**可验证的领先点**，值得写进对外材料。
- **「通过 skills 训练 agent」** 与其 Kitchen 比喻，几乎就是我们的 **L0–L4 + 载体无关工具**设计的另一种表述。
- **「edge case：agent 不聪明也要能 thrive」** 提示：门禁要**不依赖 agent 的自觉**（这与我们「别给资产写'记得做'，要给必然触发的动作」判据一致）。
- 他这条线（Grok Bot 团队 + pstack）**可作为一个"对标样本"**：我们的 AutoMedia / 知识库引擎 vs 他的 outer loop。

## 待验证点

| # | 待验证 | 原因 |
|---|---|---|
| 1 | "**20+ GrokBots**"、"**85% 工程师跑 10+ bots**" | 第三方整理（aiidelist）**明确指出这两个数字未被一手材料证实** —— 属流传说法 |
| 2 | "**一个月 ship 1000 个 PR**" | Lauren **自述**；无仓库级审计（无 PR 大小 / 复杂度 / 业务影响数据） |
| 3 | `Open Claw`（"我搭了一整套 Open Claw 在 telegram 里"） | 拼写待核，可能是别的产品名 |
| 4 | 模型名 `Fable 5 Max` / `Sol` | 名称待核（可能也是错听） |
| 5 | `grid work`（"they're just off doing grid work for you"） | 语义存疑，可能为 Grok 相关或属误听 |
| 6 | **Cursor / SpaceXAI / SpaceX 三者关系** | 播客中"Cursor and SpaceX jointly announced"；第三方资料写 Lauren 在 **SpaceXAI**、同时提 **Cursor** —— 口径需核 |
| 7 | `pstack` 的具体内容 | 播客未展开；第三方称其是 Lauren 自建的 harness |

## 关联问题

- 🔗 **同系列前置条目（库里已有）**：`bilibili-BV1AjH66gETc-2500-prs-skill-workflow-michelin-kitchen.md`
  —— 标题即「两个最会写 Skill 工作流的人的对话：每月 2500 个 PR，睡觉时 AI 还在干活！**pstack 作者**怎么做到的？」
  ⇒ **两片讲的是同一件事**（同一人 / pstack / Michelin kitchen 比喻），本片是**同一天发布的对话实录**，可互为上下文。
- ⚠️ 两片的"1000 PRs"（本片）与"2500 PRs"（前片）**数字不一致** —— 两个都是自述口径，**引用时必须标明出处与日期**，不得混用
- `pstack` 与"agent harness / skills 体系"的关系？→ 与我们的 skill 引擎是否同构
- "把规则编码成 fail-CI 硬约束" ↔ 我们的 `check_tool.py` / `check_consistency.py` / `run_regression.py`
- "chief of staff agent 派活给专业 agent" ↔ 我们的 **default 主管 + code/content 特化 profile** 分工
- "Michelin kitchen：用 skills 训练 agent" ↔ **L0–L4 分级 + 载体无关工具**设计

## 抓取备注

**① 🔴 语言判定踩坑（第二次同类，务必先检测）**
视频标题是**中文**且标 **【中英字幕】**，但**正片为英文原声**。
实测三处采样（开头 / 中间 / 后段）检测：`en=0.9988 / 0.9968 / 0.9970`。
若按标题硬编码 `language='Chinese'` → 会产出全篇中英混排乱码。**中文字幕 ≠ 中文原声。**

**② 🔴 LLM 后处理在本片被实测否决（英文场景）**
用 AMD `DeepSeek-V4-Flash`（3 并发、提示词明确写了"逐字保留、不得概括"）跑第 1 块：
```
块01: in=2983 字符 → out=2384 字符  ratio=0.799  （<0.95 = 概括信号）
逐句 diff：丢掉 115 词整段（主播开场"Benny…"）+ 另 4 词，共丢 ≈130/563 词 = 23.1%
新增仅 18 词（多为 Groc→Grok 修正），无编造
```
⇒ **判定：该通道在英文转写上会静默概括**。改用**机械修名（零幻觉）+ 程序分段**：
- 机械修名两轮共 **148 处**（`Grock*` 128 处 + 远距变体 20 处），残留扫描全 0
- 修名前后词数 5555 → 5593（+38，来自 `GrockBot`→`Grok Bot` 拆词），**零内容丢失**
- 分段：按句切分、每 4 句一段 → 98 段
> 值得记：**中文场景需要 LLM 补标点，英文场景反而不要 LLM** —— 英文 Whisper 自带标点，LLM 只会引入概括风险。

**③ 关键词词表补别名（已改，已备份）**
本片主题词 `agents` 出现 41 次，但词表 `AI-Agent` 的别名只有 `AI-Agent / AI Agent / coding-agent / 智能体`，
**裸词 `agent`/`agents` 命中不到** → 只抽出 6 个词条。
已补别名 `agent` / `agents` / `AI agents`（备份：`_keywords.yaml.bak-20261007-agentalias`）。
补后重提：`AI-Agent` 命中 **58** 次，登顶。

**④ 管线与产物**
- 音频：`/mnt/d/Hermes-Workspace/01-Projects/bilibili_audio/BV13be26zEqG_p01.wav`（1720.69s，**已核时长与元数据一致，非 600s 试看片段**）
- Whisper 原始：`.../_raw/BV13be26zEqG.txt`（29,719 B）
- 修正+分段成品：`/tmp/pp_bv13/final2.txt`
