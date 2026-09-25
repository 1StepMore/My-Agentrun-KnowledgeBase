---
title: 【AI】WebSearch工具横评
keywords:
- AI-Agent
- WebSearch
- tool-review
- API
- Tavily
- Exa
- Perplexity
state:
  phase: draft-archived
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
sources:
- Bilibili/bilibili-BV1hSN3zjE8F-websearch-tools-benchmark.md
related: []
promoted_to: '[[WebSearch工具横评]]'
---
# 【AI】WebSearch工具横评

## 核心知识点

### **1. WebSearch工具的五种分类与现状**
目前市场上的WebSearch工具可分为五类：搜索引擎官方API（已大多下线）、[[SERP API]]爬取搜索引擎结果页、自建搜索引擎的[[API]]（如EXA、Tavily）、本地爬虫技术（如DuckDuckGo MCP）、以及AI模型内置搜索（如[[Perplexity]]）。其中自建API成为主流，因其与AI集成丝滑且功能可控。

### **2. 自建搜索API关键维度对比**
选择自建搜索API时需重点评估免费额度、价格、是否提供[[REST]]和[[MCP]]接口、[[深度搜索]]能力、[[WebFetch]]支持、[[限流]]策略及注册门槛。下表对比了主流的四个工具：

| 工具 | 免费额度 | 价格(美元/千次) | 深度提取 | WebFetch | 免费限流 | 注册门槛 |
|------|----------|----------------|----------|----------|----------|----------|
| EXA | 匿名无限 | $8 (付费) | 支持(可选) | 支持(可选) | ~1 QPS，可能封IP | 无需注册 |
| Tavily | 1000次/月 | $5 | 支持(Answer参数) | 支持 | 1 QPS，可重试 | 低 |
| Brevo | 1000次/月 | 约€5 | 有限 | 有限 | 未明确 | 需[[信用卡]] |
| LinkUp | 1000次/月 | €5 | 支持 | 有限 | 约1 QPS | 中等 |

### **3. 限流与注册条件对白嫖党的核心影响**
对于免费用户，[[限流]]直接影响使用体验。例如[[EXA]]虽完全免费，但触发限流后IP会被封禁6小时以上，甚至连坐同网络用户；而[[Tavily]]同样限制1 QPS，但允许重试，不封IP。此外，Brevo要求绑定[[信用卡]]，增加了多账号注册的难度，对羊毛党不友好。

### **4. 深度提取与WebFetch的价值**
[[深度搜索]]能够将搜索结果页面内的详细内容提取并转化为Markdown，大幅提升信息量；[[WebFetch]]功能则能绕过本地网络限制直接获取外网内容（如OpenAI文档）。EXA和Tavily均支持这些功能，而传统SERP API大多缺乏，因此更适合Agent场景。

### **5. 工具选择建议**
综合评测，[[EXA]]适合低频率、简单验证的场景（白嫖无成本）；[[Tavily]]在功能和限流宽容度上更平衡，适合正式项目与Agent集成；[[Brevo]]因需信用卡不推荐；[[LinkUp]]适合欧洲用户。若需极致稳定或全免费，可考虑本地爬虫方案（如DuckDuckGo MCP）。

## 总结
本视频评测了WebSearch工具的五种类型，重点对比了EXA、Tavily等自建API的免费额度、限流、深度提取等关键属性。EXA提供匿名免费但限流风险较高，Tavily功能全面且限流友好，是当前更推荐的选择。用户应根据实际使用频率和功能需求挑选合适的工具，白嫖首选EXA，正式开发建议Tavily。
