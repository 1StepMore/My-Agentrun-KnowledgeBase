---
title: AI时代演示文稿的方法论-AI辅助PPT制作的四个技能层级
source: Bilibili 视频转写（1 篇）；本页为我们的提炼
keywords:
- ppt-replacement
- prompt-engineering
- productivity-tools
- generative-ai
state:
  phase: draft
  time_raw: 2026-09-13 22:00:00
  time_draft: 2026-09-13 23:11:21
sources:
- Bilibili/bilibili-BV1iRcSzDEnL-ai-ppt-presentation-skills.md
related: []
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---

# 用 AI 做演示：真正稀缺的不是"生成"，而是"基于反馈的迭代"

## 一句话核心观点
AI 演示的真正瓶颈不是生成初稿，而是**基于多方反馈的多轮迭代**；要同时做到"分析锐利 + 视觉精致"，靠的是可迁移的流程与精准 prompt，而不是某一款工具。

## 核心框架

### 一、两条能力轴（选工具前先定位）
- 文本型模型（ChatGPT / Gemini / Claude）：论点锐利，但做不出漂亮幻灯片
- AI 演示工具（Gamma、Beautiful AI 等）：视觉华丽，但内容泛泛
- 目标：右上角象限——analytically sharp 与 visually polished 兼得，用工作流把两端接起来

### 二、时间分配真相
- 初稿生成：约 1 分钟（最不重要的部分）
- 迭代 + 落实 stakeholder feedback：约占 **80%** 时间

### 三、可迁移流程
生成初稿 → 内容清理 → 按角色反馈逐条修改 → 交付（翻译 / 品牌精修）

## 关键细节与可复用做法

### 初稿阶段（以"向 Google CEO 提案与 Apple 合作"的 deck 为例）
- 提纲"工具优化版"：用 `---` 分隔每一页（工具推荐格式）
- 选择 **preserve exact text**：保留自己写好的强标题，正文之后再用 agent 精简
- **标题检验法**：只顺序读所有标题、不看正文，若仍能理解完整 story 线，说明标题合格
- 主题配图：公司场景优先用**图片占位符**，以便后续替换成内部素材
- "附加指令"字段留空——因为它会与工具底层的 system prompt 冲突

### 内容清理
- 用 agent + prompt 批量精简所有页正文；每次改动可选 **keep 或 revert**
- 不满意可追问"更简洁但不丢意图（without losing intent and message）"
- 删除与正文不互补的配图（AI 图常出现"没有头"之类的废图）

### 基于 stakeholder feedback 的六类修改（核心可迁移模式）
1. **结构重排**：按论证依赖调整顺序。风险缓解页应紧跟 executive summary——过不了监管（regulatory hurdles），后面全部无意义
2. **补数据**：让 agent 联网搜最新数据，以表格插入新页；再从页内唤起 agent 把数据可视化
3. **核实来源**：选中文字再打开 agent，文字会自动作为 context；联网核实官方口径（"月度活跃用户"改为官方公布的**周活跃用户**），并补脚注来源
4. **文字转视觉**：把文字页转成 waterfall chart——Android + iPhone ≈ **32.5 亿**台内置 Gemini 的智能手机
5. **视觉层级**：让 agent 用颜色/大小/强调使关键列视觉主导，匹配论证层级（前两列是背景 context，第三列"竞品被淘汰"是 punchline），再手动调字号
6. **合并精简**：只输入"合并 11、12 页"会挤成一团；加约束"**最多三个 talking points**"才可用，再追加"删图、优化间距"

> 该 agent 是为**速度**而非**推理**设计的：指令越精确，输出越好。

### 修复图表错误
- 文字转图表时 agent **经常出错**
- 修正：双击进入图表 → 右键删除多余行（如误加的 MacBook 1.1 billion）→ 总数从 4.53 恢复为正确的 **3.25 billion**

### 翻译与多工具工作流
- 翻译前先**复制一份副本**再翻，否则会用译文覆盖原英文版
- 机翻质量约 **70–75%**，够内部 pre-read 使用
- 精修：把英文原版与译文都导出 PDF，上传到文本模型，让它扮演**双语专家译者**，给出更自然连贯的修改建议

## 对读者的可迁移启示
- **换工具依然成立**：无论用哪款大纲/演示工具，"快速出稿 → 精准指令迭代 → 人工兜底修正"都适用
- **把工具当"快但不聪明"的执行者**：指令要带约束（数量上限、保留意图、指定删除元素）
- **保留 [[Human in the loop]]**：AI 生成的图表、翻译、配图都需人工校验，工具远未完美
- **异步分享**：利用滑动/文档式排版（scroll format），把 talking points 做成"准演示"链接作为会前 pre-read
- **品牌统一**：导出为 PowerPoint 后，可用带本地品牌规范（skills）的工具做视觉精修
- **不会被替代的能力**：[[critical-thinking]]、获取高质量反馈、把反馈编织成连贯叙事——只会更重要

相关概念：[[AI-presentation-tools]]、[[prompt-engineering]]、[[stakeholder-feedback]]、[[multi-tool-workflow]]、[[visual-hierarchy]]、[[agent-iteration]]
