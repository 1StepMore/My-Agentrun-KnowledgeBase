---
title: 🤖 Chat Bot
source: XpertAI 官方文档
related: []
keywords:
- XpertAI
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:25'
  time_draft: '2026-07-01T12:42:25'
  time_wiki: '2026-07-01T12:42:25'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/toolset/chatbi-toolset/bot.md
---
# 🤖 Chat Bot

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 🤖 Chat Bot

When starting a conversation, the ChatBI bot will present common questions related to the currently available data models, helping users quickly begin the dialogue. Users can directly click on the questions they are interested in or manually input custom questions to initiate a conversation.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-welcome.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=0c90e3fd62b18e2f1d692ecdf2551879" alt="Lark chatbot welcome" width="2420" height="1754" data-path="public/img/chatbi/lark-chatbot-welcome.png" />

## Basic Questions

Users can freely ask questions related to data models, such as inquiring about specific metrics, dimensions, or what kinds of charts ChatBI can create.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-measures.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=0d3781adc7ce063835a628f5f670601a" alt="Lark chatbot measures" width="2420" height="1754" data-path="public/img/chatbi/lark-chatbot-measures.png" />

Whether asking data-related questions or clicking on examples for a quick conversation, ChatBI will refer to the knowledge base to find relevant information related to your query based on the data model and then call the large model to provide an answer. Based on the answer given by the large model, ChatBI will retrieve the actual data from the data source and return it to the user in various forms, such as charts, metrics, or tables.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-kpi.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=f3629f29bd5b7e6547d294a291b5057f" alt="Lark chatbot kpi" width="2368" height="1796" data-path="public/img/chatbi/lark-chatbot-kpi.png" />

If the data result is returned in the form of a chart, the bot currently supports three types of charts: bar charts, line charts, and pie charts.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-chart.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=a465adeaab6e4e17bdb159141dec95c8" alt="Lark chatbot chart" width="2368" height="1796" data-path="public/img/chatbi/lark-chatbot-chart.png" />

Data can also be returned in the form of data tables within the message.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-table.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=dc147956bd5f884296393dbbd994e9ea" alt="Lark chatbot table" width="2368" height="1796" data-path="public/img/chatbi/lark-chatbot-table.png" />

## Calculated Metrics Questions

For metrics that don't have a direct corresponding measure, ChatBI will automatically create a calculated formula metric and use this calculated metric to answer the question, providing relevant data results.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-indicator.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=447698757409518f4d2cae7dd22244ad" alt="Lark chatbot calculated indicator" width="2370" height="1774" data-path="public/img/chatbi/lark-chatbot-indicator.png" />

<Tip>
  The accuracy of calculated metrics also depends on the richness of the knowledge in the knowledge base. Please import the relevant knowledge base before using ChatBI.
</Tip>

## Multi-turn Conversations

The technology behind ChatBI belongs to multi-turn conversational agents. Each time a question is answered, the context of the current conversation is included in the large language model's request, allowing for a more intelligent understanding of the user's question context.

Users can click the "End Conversation" button below the bot message or manually input "End Conversation" to conclude the current conversation. Asking again will start a new conversation context.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-end.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=3dd20bc516e7cdb94bfb132cdc561fcf" alt="Lark chatbot end conversation" width="2306" height="1652" data-path="public/img/chatbi/lark-chatbot-end.png" />

<Tip>
  To avoid unnecessary content or reduce token usage, please end the conversation promptly.
</Tip>

## Group Chat Conversations

In addition to one-on-one conversations, ChatBI supports multi-turn conversations among multiple users within a group. When chatting with the ChatBI bot in a group, users need to @ the bot and input their questions. Different users will have different conversation contexts, but if one user clicks on an example button in another user's message, the conversation will continue within the original context.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-group-kpi.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=a56babe7eb8b65edcdedcbb2221821a6" alt="Lark chatbot in group" width="2304" height="1696" data-path="public/img/chatbi/lark-chatbot-group-kpi.png" />

<Tip>
  @ your boss in the group and @ ChatBI with a question, and let ChatBI intelligently analyze the data for your boss!
</Tip>

## Sharing and Forwarding

Users can forward ChatBI's answer messages to others or to a group, making it easier for colleagues to collaborate more efficiently.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-share.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=39412e06c961bae0be224ee2d7dcb212" alt="Lark chatbot share" width="2304" height="1696" data-path="public/img/chatbi/lark-chatbot-share.png" />

Share the message within the group.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-shared-message.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=4c04bb149b3524d3c2025d1f4307d0e3" alt="Lark chatbot shared message" width="2442" height="1696" data-path="public/img/chatbi/lark-chatbot-shared-message.png" />

## Technical Analysis

To quickly understand how ChatBI retrieves data, users can open the "Query Statement" button to view the specific query statement. For technical personnel, this allows them to judge whether the answer provided by ChatBI is accurate and make improvements accordingly.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-query.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=a4a53c68df754a7ab317a711ae7dbef2" alt="Lark chatbot query" width="2304" height="1696" data-path="public/img/chatbi/lark-chatbot-query.png" />

In the calculated metrics, you can also view the calculation formulas, making it clearer to understand whether the answers provided by ChatBI are accurate and allowing you to upgrade the knowledge base.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/lark-chatbot-formula.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=a40751b1be89cad1188678b4f9077d98" alt="Lark chatbot formula" width="2304" height="1696" data-path="public/img/chatbi/lark-chatbot-formula.png" />
