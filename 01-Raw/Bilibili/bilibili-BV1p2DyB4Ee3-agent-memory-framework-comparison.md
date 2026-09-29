---
title: Agent记忆框架怎么选？Text to Mem/Mem0/Letta/Rimi/MemU 五大项目工程级横向对比
keywords:
- memory
- agent-state
- RAG
- vector-database
- hindsight
- AI-Agent
state:
  phase: raw
  time_raw: '2026-09-29T23:10:00'
  time_draft: '2026-09-30T01:52:00'
  time_wiki: null
source_url: https://www.bilibili.com/video/BV1p2DyB4Ee3
source_type: video
source_platform: bilibili
author: 唐国梁Tommy
author_id: ''
publish_date: '2026-04-11'
fetch_date: '2026-09-29'
priority: 3
language: zh
duration_seconds: 911
duration_formatted: '15:11'
notes: Whisper(small, WSL GPU, fp16=False) 转写 + ZHIPU glm-4.5-flash 后处理 + 繁转简 + 专名修正（Letta 官方名/Letta/Mem0 等）。系列「Agent记忆框架」上集，工程级横向对比 Text to Mem/Mem0/Letta/Rimi/MemU。下集见 BV1orQJB2Edt。已编译入 02-Draft/AI-Agent记忆系统-十种开源架构的技术路线与选型判据.md（两集合为一篇）。
---

# Agent记忆框架怎么选？Text to Mem/Mem0/Letta/Rimi/MemU 五大项目工程级横向对比

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | Agent记忆框架怎么选？5大Agent Memory项目工程级横向对比 |
| UP主 | 唐国梁Tommy |
| 发布时间 | 2026-04-11 |
| 总时长 | 15:11 |
| BV号 | BV1p2DyB4Ee3 |

## 原文内容

大家好，今天我们开一个新系列，专门聊一个特别重要但很多人一直没搞透的话题：Agent的记忆。

我相信你一定碰到过这种情况：昨天刚和AI聊完半小时的相关背景，今天打开新对话，他又把你当陌生人，一切从头再来。这不是bug，这是今天大多数LLM agent的默认形态——无状态。而要让Agent真正长期为你工作，记忆就是绕不开的核心模块。

本集讲这五个：Text to Mem、Mem0、Letta、Rimi、MemU。他们代表了当前记忆框架的主流范式。这一集的目标是让你听完之后，对Agent的记忆到底该怎么设计这件事，建立一个完整的认知框架。

好，我们开始。我想先从一个可能很多人没听过，但我觉得特别有意思的项目讲起，它叫Text to Mem。

为什么第一个讲它？因为它做的事情非常基础，也非常野心大。它不是在做一个记忆系统，而是在给所有记忆系统定义一套通用的操作语言。

你想想现在这个场景：你对Agent说一句"把我上周提到的那次会议记忆标记成重要的，30天后自动归档"。这句话对人来说很清楚，但对一个记忆系统来说，问题就来了：上周是哪一段时间？那个会议记忆对应数据库里的哪一条？标记成重要，到底是改权重、改标签，还是加提醒？

Text to Mem的解法非常干脆：它在LLM和存储之间插一层IR，也就是中间表示层。你可以把它类比成CPU的指令级架构。

Text-to-Mem把所有记忆操作收敛到12个原子操作，分成3个阶段：
ENC阶段，只有Incode负责记忆的诞生。
RET阶段，2个操作：Retrieve是纯数据取回，Summarize是让LLM再生成一次摘要。
STO阶段，9个操作，覆盖记忆整个生命周期。

我自己最欣赏的一个细节，是他把retrieve和summarize分开了。因为工程上，他们完全不是一回事：retrieve几十毫秒就返回，而summarize背后是一次完整的LLM推理，延迟是上千倍。分成两个操作，执行引擎就可以用完全不同的超时、缓存、降级策略。

Text to Mem把所有操作都收敛成一段JSON，它是一个五元结构：第一个是阶段，第二个是操作名，第三个是目标，第四个是参数，第五个是元数据。

这五个字段合在一起，就像一张记忆操作的标准功能卡。其中最能体现工程成熟度的是元数据里藏的两个安全字段：DryRun和Confirmation。

你想一种极端场景：LLM抽风给你生成一条JSON说"把所有记忆全部删除"。Text to Mem在这里卡了一道硬性规则：你要么先用DryRun模拟一次，要么显式地把Confirmation设成true，二选一，少一个都不让过。

光有安全法还不够，Text to Mem还上了两层验证：外层查的是格式和结构，走JSON schema标准；里层查的是业务逻辑，靠Pydantic做拦截。比如Promote操作的绝对值和相对值必须恰好有一个为空。这种"不信任LLM，但能兜住LLM"的设计哲学，才是Text to Mem真正值得学的地方。

Text to Mem最有意思的设计点是它的Log操作，四种模式：ReadOnly完全冻结、NoDelete禁止删除、Append Only只允许追加、Custom完全可编程。最喜欢的是Revealer机制，本质上是RBAC风格的权限绕过。

当然，Text to Mem目前还有明显短板：存储只有SQLite，参考实现没有HTTP API，向量以JSON文本存在Text列里。但它真正的价值是，它在帮整个行业定义记忆操作语言长什么样。

讲完了地基，我们进入更偏实战的部分。第二个要讲的是目前开源社区里热度最高的AI记忆开源框架之一：Mem0。它是Weaviate孵化的项目，GitHub上的Star数已经是几万级别。

为什么这么多人选Mem0？原因很直接：上下文窗口有限，长对话里早期用户偏好会丢，每次新对话都要重新介绍自己，不同对话之间没有继承关系。

Mem0官方给出的数据是：相比直接用OpenAI API，准确率高26%，响应快91%，Token省90%。

Mem0整体是三层：最上面是Memory API，中间是LLM推理加向量检索的逻辑层，下面是存储层。真正能体现工程成熟度的是中间的五个工厂模式：LLM Factory支持17家LLM提供商，Embedder Factory支持11家Embedding模型，Vector Store Factory支持22种向量存储，Graph Store Factory支持四种图存储，Reanchor Factory支持五种Reanchor。

更妙的是，它用ImportLib做动态加载：你没装Pinecone包也没关系，只要用的不是Pinecone就不会挂。

Mem0在代码里显示定义了三种记忆类型：语义记忆是抽象的事实性知识，情景记忆是具体事件，程序记忆对应Agent执行的完整步骤。程序记忆要求逐字保留，因为它真正的使用场景是Agent崩溃后恢复执行状态。

几个我觉得最值得学的设计：
第一个，UUID幻觉处理。LLM对长UUID自负串处理能力很差，会幻觉。Mem0的做法是把LLM看到的UUID映射成简单整数，LLM只需要决定对第三条记录执行update，然后系统再把整数映射回真实UUID。
第二个，双存储并行。向量存储负责语义相似搜索，图存储负责关系推理。两条路径用ThreadPoolExecutor并行跑，结果合并返回。
第三个，Shown Prompt策略。Mem0有两个记忆抽取Prompt：User Memory Extraction Prompt只看用户消息，Agent Memory Extraction Prompt只看助手消息。这是一个很聪明的职责分离，防止AI助手的自我表达污染用户记忆，同时也允许AI助手自己积累"我是一个什么样的AI"的自我认知。
第四个，多层级作用隔离。用户隔离、agent隔离、运行时隔离，三层隔离直接支持多用户多agent的复杂场景。

Mem0很强，但它有一个很真实的成本瓶颈：每次Add调用完整模式下会调用2-5次LLM。更麻烦的是，随着用户历史记忆的增多，Token数会随记忆规模线性增长。这就意味着Mem0不适合高频实时写入的场景，更适合用户维度、对话力度、中低频写入，比如AI对话助手、客服系统、医疗健康追踪这一类。所以说Mem0真正强的地方不是某一项黑科技，而是工程化的全家桶。

第三个我想重点讲的是Letta。如果说Mem0是把记忆做成了成熟的中间件，那Letta是在做一件更酷的事情：把操作系统的虚拟内存思想完整地搬进Agent架构里。

很多同学应该记得2023年10月那篇论文MemGPT，2024年9月正式更名为Letta。Letta的核心是一个三层记忆架构：Core memory核心内存，直接加载系统Prompt，每次推理LLM都看得到，就像CPU能直接访问的RAM；Archival memory归档内存，容量无限，走向量检索，就像磁盘；Recall memory召回内存，存放所有历史对话消息，就像操作系统的日志系统。

Core memory的每个block是一个三元组：Label是路径命名空间，Description告诉agent这个block是干什么的，Value是实际内容，Limit是字符上限。这个limit默认十万字符，它是一种强制的信息压缩约束，逼迫agent主动做信息蒸馏。当上下文窗口快满了，触发summarizer，默认驱逐30%的消息，被驱逐的消息写进recall memory，仍然可以通过conversation search再被检索出来。被驱逐的消息不是真的消失了，它们只是从in context移到了out of context。这才是真正意义上的虚拟内存无损分层。

Letta有一个在同类项目里完全独树一帜的设计：Git Enabled Block Manager。它把真正的Git引入了agent架构里。双存储Git是真实来源，PostgreSQL是快速读缓存。每一次记忆变更都会产生一次Git Commit，携带Agent ID、时间戳、变更原因。这样的好处非常多：不可篡改内容寻址存储，防止记忆损坏；完整历史，每一次记忆修改都能回溯；并发安全，多个Sleep-time Agent可以用GitWalkTree隔离修改；可审计，每个Commit就是一条审计记录。再配合MEMFS，记忆会被组织成一颗真正的目录树：一个目录放Agent的人格设定，一个放用户偏好和事实知识，一个放学到的技能和经验。每一份记忆都是一个独立的markdown文件。

另一个很妙的设计是Sleep-time Agent：在用户不交互的时候，Agent也在持续自我改进。主Agent只负责推理和恢复低延迟，每五步触发一次Sleep-time Agent，他在后台读最近的对话分析更新memory block。三个好处：主路径低延迟，后台可以用更大token预算做深度反思，充分利用空闲时间。

Letta是目前开源里记忆自治能力最强的系统，但代价也很明显：认知成本高，数据库强依赖，80多个依赖包。

第四个项目来自阿里巴巴的AgentScope团队，叫Rimi。Rimi最核心的理念：文件即记忆。传统做法记忆全存数据库里，你想知道AI记住了你什么，必须通过API去查，整个记忆是个黑盒。Rimi反过来，记忆直接存成Markdown文件，你打开就能看见，可以直接编辑，可以Git版本控制。这把记忆的控制权和透明度还给了用户。

Rimi内部有两套系统：Rimi Lite是文件记忆，用于短期工作记忆；Rimi本体是向量记忆，用于长期语义记忆。两套系统的时间维度是错开的。

第一个技术亮点：Delta FireWater增量监控。当记忆文件累计到几十KB后，每次变更都重新处理整个文件，是对Inviting API的巨大浪费。Rimi先检测文件是不是纯追加模式，如果是，就只处理新增部分，节省92%的API调用。

第二个亮点：Window和Content分离。它把向量嵌入建在Window上，而不是Content上，因为用户查询和Window天然相近，大幅提升召回率。

第三个亮点：AI自主记忆管理。把文件操作工具给AI，让AI自己决定如何组织记忆。

Rimi的性能数据：Qwen3-8B加Rimi后，综合得分超过了没有记忆的Qwen3-4B。好的记忆系统可以让小模型打过大模型。Rimi是目前开源里最对人性化的记忆系统。

最后一个要讲的是，整个上集里泛式最激进的项目叫MemU。它的Slogan："24小时常驻，主动出击的Agent记忆系统"。

前面四个项目的记忆系统有一个共同点：本质上都是被动的。用户说一句话，系统才去Add一条记忆；用户问一个问题，系统才去检索一次。MemU想做的是另一个方向：让记忆系统不再等，自己主动跑。用户没说话的时候，他在看；甚至在用户下一句话还没发出来之前，他已经预测到你大概会问什么，然后把相关上下文提前加载好了。

MemU实现主动性的方式是双agent架构：MemU agent干老本行，听用户说话，调工具，生成回复；MemU Bot只负责记忆这件事，时序盯着每一次交互，后台提取、整理、分类。

代码实现其实很简单：MemU Bot就是用Python的AsyncIO.createTask起了一个异步后台任务，靠共享conversation messages列表通信。

这个设计的精妙之处在于简单到不像创新。

MemU的文件系统是一个概念隐喻，底层是数据库：文件夹对应category，文件对应memory item，符号链接对应交叉引用，挂载点对应resource。

和Rimi的用法完全不一样：Rimi是给人看的透明文本，MemU是Bot自己维护的结构化目录树。一个偏用户主权，一个偏Bot自制。

MemU在V1.4版本引入了一个我很喜欢的机制叫Significance-Aware Memory（显著性感知记忆）。具体做法是：每条Memory Item都带一个Reinforcement Counter（计数器），每当被检索一次，计数就加一；排序时，根据强化次数加权，越常用的记忆越容易被再次召回。这在模拟人类记忆的一个本质特性：你越经常想到的事情，就越容易想起。我愿意把它叫做给记忆加了一层"肌肉记忆"。

MemU在OKM基准上，所有Agent任务的平均准确率是92.09%，这正是Mem0当年用来打OpenAI memory的同一个基准。两个框架站在同一把尺子前面，MemU给出了非常有竞争力的数字。

MemU最适合需要长期陪伴、长期学习的场景：个人AI助手、企业级客服、DevOps Agent、研究型助手。

前面四个项目：Text to Mem在做记忆的语言，Mem0在做记忆的中间件，Letta在做管理记忆的Agent，Rimi做人能看见的记忆。他们的共同点是：记忆始终是一个被使用的对象。MemU把这个关系反过来：记忆自己成为了一个Agent。

如果让我给上集留一句最想留给观众思考的话，就是这一句：从"Agent有记忆"到"记忆本身是一个Agent"。

今天这集就先聊到这里，我们回顾一下这五个项目的位置：Text to Mem是最底层的记忆操作语言（12个操作+5元JSON契约）；Mem0是当下最流行的记忆中间件（三种记忆、五大工厂、双存储并行）；Letta是记忆自治做得最彻底的（三层记忆、Git版本、Sleep-time Agent）；Rimi走的是完全相反的哲学（文件即记忆，把控制权交还给用户）；MemU把记忆本身变成一个24x7主动运行的Bot。

想快速给产品加记忆层，看Mem0；想做真正有状态的Agent，看Letta；想要记忆能主动预测用户，看MemU；想要记忆透明可见，看Rimi；做研究，定义自己的记忆操作语言，看Text to Mem。

下一集我们会聊更前沿的5个项目：MemOS, OpenViking, Hindsight, Second Me, MetaMem。

如果今天这集让你有收获，请一键三连支持一下。下集的五个项目，一个比一个硬核，我们下期见！

## 核心摘录

- **AI 记忆框架的五个主流范式**（本集）：Text to Mem（记忆操作语言）、Mem0（记忆中间件）、Letta（操作系统虚拟内存架构）、Rimi（文件即记忆/透明）、MemU（记忆本身成为 Agent/主动）
- **Text to Mem**：LLM 与存储之间插 IR 层；12 个原子操作收敛成 5 元 JSON 契约；DryRun+Confirmation 双安全闸；两层验证（JSON schema + Pydantic 业务逻辑）；短板=仅 SQLite、无 HTTP API
- **Mem0**（Weaviate 孵化）：最热开源记忆中间件；三层 + 五大工厂（LLM/Embedder/Vector/Graph/Reanchor）+ ImportLib 动态加载；三种记忆类型（语义/情景/程序）；UUID 幻觉处理、双存储并行、Shown Prompt、三层隔离；成本瓶颈=每次 Add 调 2-5 次 LLM + Token 随记忆线性增长
- **Letta**（前身 MemGPT，UC Berkeley）：三层记忆架构（Core 核心/Archival 归档/Recall 召回）；Core block 三元组 + limit 十万字符强制压缩；Git Enabled Block Manager（Git 为真实来源 + PostgreSQL 读缓存）+ MEMFS 目录树；Sleep-time Agent 后台自改进；记忆自治最强但 80+ 依赖包
- **Rimi**（阿里 AgentScope）：文件即记忆；记忆存成 Markdown 可读可编辑可 Git 版本控制；Rimi Lite 短期文件记忆 + 本体长期向量记忆；Delta FireWater 增量监控省 92% API 调用；Window 与 Content 分离嵌入提升召回
- **MemU**：24x7 主动记忆 Agent；双 Agent 架构（MemU 主 agent + MemU Bot 后台记忆）；Significance-Aware Memory 显著性感知（检索次数加权，模拟"肌肉记忆"）；OKM 基准 Agent 任务平均准确率 92.09%

## 个人解读

- 本集是系列上集，下集（BV1orQJB2Edt）讲 MemOS/OpenViking/Hindsight/Second Me/MetaMem 五大更前沿架构
- 五个项目代表记忆设计的五层定位：操作语言（Text to Mem）→ 中间件（Mem0）→ 自治 Agent（Letta）→ 用户主权（Rimi）→ 记忆即 Agent（MemU）
- 给产品快速加记忆层首选 Mem0；要真正有状态的 Agent 看 Letta；要主动预测用户看 MemU
- "从 Agent 有记忆 到 记忆本身是一个 Agent"——记忆主动化的方向与用户关注的 Agent 记忆系统演进一致

## 待验证点

- 各项目的当前版本与 Star 数（视频 2026-04 发布，可能已演进）
- Mem0 / Letta 在 2026 年的实际维护状态与最新特性
- 各项目的对比评测数据（准确率/Token 节省）的真实基准

## 关联问题

- 下集 BV1orQJB2Edt：MemOS/OpenViking/Hindsight/Second Me/MetaMem 五大架构
- Hermes 官方记忆插件 Hindsight 的选型评估（见 00-Records/research/2026-09-29-记忆系统结论核实与精简记录.md）

## 抓取备注

- Whisper(small, GPU, fp16=False) 转写 15:11 音频 → 5498 字符原文
- ZHIPU glm-4.5-flash 后处理（补标点/分段/修专名），比值 1.079 正常
- 繁转简（OpenCC t2s）+ 专名修正（项目名统一为 Letta/Mem0/Rimi/MemU/Text to Mem）
- 部分 Whisper 错听可能仍有残留（如个别术语音译），以原文音频为准