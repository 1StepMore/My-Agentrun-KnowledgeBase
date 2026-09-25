---
title: Enhanced Features
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:53:35'
  time_wiki: '2026-09-23T00:50:32'
source_url: AI生成
source_type: article
source_platform: xpertai
author: XpertAI
fetch_date: '2026-05-08'
priority: 3
language: zh
notes: XpertAI官方文档
author_id: ''
publish_date: ''
---
# Enhanced Features

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Enhanced Features

Enhanced features can improve the interactive experience for Digital Expert users. For example, adding file upload functionality, adding an introduction or welcome message to LLM applications, allowing application users to have a richer interactive experience.

Click the "Features" button in the upper right corner of the application to add more features to the application.

## Enhanced Features Details

### 1. Welcome Message

"Welcome Message" is used to display custom text on the Digital Expert welcome page, which can serve as a welcome message or AI self-introduction, helping users quickly understand the assistant's capabilities and purposes.

#### 🎯 Main Functions

* Bring users closer and create a sense of familiarity
* Guide users to ask questions and lower the barrier to use
* Provide application context to improve conversation efficiency

#### ⚙️ Configuration Method

* Customize welcome message content (supports line breaks and emojis)
* Can set 1-10 suggested opening questions
  * Suggested questions are displayed as buttons, clickable for quick questions

#### 💡 Usage Suggestions

* Keep welcome messages concise and friendly, for example:
  > "Hello, I'm your data analysis assistant and can help you analyze sales, inventory, or budget situations."
* Suggested questions can be set around common needs, such as:
  * "View this month's sales data"
  * "Analyze customer churn reasons"
  * "Generate financial report summary"

***

### 2. Suggested Questions

"Suggested Questions" intelligently generates 5 related follow-up questions after each round of conversation, guiding users to continue asking questions and keeping the conversation active.

#### 🎯 Main Functions

* Maintain user interest and enhance interactive experience
* Inspire ideas and lower the barrier of "having nothing to ask"
* Provide creative topics and enhance conversation interest

#### ⚙️ Configuration Method

* Edit prompt templates to guide the large model to generate appropriate questions
* Supports freely setting tone, such as: professional, relaxed, humorous, etc.
* Scene descriptions or instructions can be added to templates

#### 💡 Usage Suggestions

* Set prompts based on application goals and user preferences, for example:

  > "Based on the user's previous question, generate 5 humorous and imaginative questions to encourage continued exploration."

* Example output questions (humorous style):

  * If AI had dreams, what would its career ideal be?
  * Why is the "F" key always cooler than the "J" key?
  * If cats ruled human society, what would the first law be?
  * What would be the biggest bug in time travel?
  * What would happen if there was no Monday tomorrow?

***

### 3. Conversation Summary

When the number of conversation messages exceeds the set maximum tolerance (e.g., 100 messages), Xpert will use the "Conversation Summary" feature to extract important information from historical conversations and convert it into concise summaries, reducing system memory burden and improving the focus and efficiency of subsequent conversations.

#### 🧠 Working Mechanism

* **Maximum Tolerance**: Sets the upper limit of new conversation messages allowed before starting to generate a new summary. For example, if shown as 22, this means that even if the conversation exceeds 16 rounds, the system will continue recording until reaching 22 rounds before triggering a new summary generation. This parameter helps avoid frequent summary generation, thereby reducing computational overhead.
* **Number of Messages to Summarize**: The number of messages to be summarized, for example, 16 in the figure means summarizing the first 16 messages out of 22 messages in the session.
* **Retention Count**: The number of messages retained after summarization, for example, 4 in the figure means retaining 4 messages, and the remaining messages will be deleted (appearing as summaries in system prompts).
* **Prompt**: Used to guide the system on how to summarize historical messages in conversations. If not provided, the system uses default prompts.

> Example configuration:
> Maximum tolerance: 100
> Summary trigger count: 40
> 👉 Retention count = 100 - 40 = 60 messages

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/feature-conversation-summary.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=78988cf44ce1664135754aa08712ff6a" alt="Config conversation summary" width="1512" height="854" data-path="public/img/ai/feature-conversation-summary.png" />

#### 📋 Application Scenarios

* Long-term interaction between users and agents
* Multi-round complex task follow-up
* Conversation flows requiring periodic knowledge summaries or task reviews

***

### 4. Long-term Memory

See [Long-term Memory](../long-term-memory.md) documentation.

***

### 5. Memory Reply

Memory Reply functionality allows manually editing and storing specific Q\&A-style memories for agents. When users ask questions, the system can prioritize matching these "memory" contents, directly generating high-quality, stable, and controllable replies, skipping the LLM's free generation process.
This mechanism effectively improves Q\&A consistency and reliability, especially suitable for customized, rule-defined, or hallucination-sensitive scenarios.

#### 🧠 Working Mechanism

* **Q\&A Memory Creation**: Developers can manually write several Q\&A pairs (question + standard answer) for agents as [Long-term Memory](../long-term-memory.md) content.
* **Similarity Matching**: When users ask questions, the system uses Embedding vectors to calculate the similarity between user input and all memory questions.
* **Score Threshold Judgment**: Only when the similarity score ≥ set threshold will the system recall and directly return the first answer from the corresponding memory.
* **Embedding Model**: Uses the Embedding model configured for long-term memory. If not set, uses the system's global default model.

#### ⚙️ Configuration Parameter Description

| Parameter       | Description                                                                        |
| --------------- | ---------------------------------------------------------------------------------- |
| Score Threshold | Controls the similarity score boundary for whether memory is recalled (e.g., 0.85) |
| Embedding Model | Uses the Embedding model configured for long-term memory                           |

#### 📌 Application Scenarios

* ✅ Standardized replies for specific domains<br />
  Suitable for knowledge base scenarios in enterprises, government, education, finance, etc., where precise control over answers is needed for some questions, such as:
  * "What is the company's customer service phone number?"
  * "Can I delete my account?"
  * "Does this system support overseas users?"

These questions should typically have clear results or avoid generating hallucination content.

* ✅ Rapid Prototype (POC/DEMO) Construction

In POC or DEMO stages, manually entering Q\&A memories can quickly tune product performance and meet customer expectations.

* ✅ Parallel use with RAG as stable fallback

The Memory Reply mechanism is equivalent to a lightweight, controllable retrieval enhancement system (RETRIEVAL ONLY), effectively avoiding hallucinations or irrelevant answers in the large model generation process.

#### ✨ Feature Advantages

* 🎯 Improves answer stability and determinism
* 💡 Avoids hallucination issues from large model free generation
* 🧩 Supports parallel use with knowledge base, search, and other modules

***

### 6. Conversation Title

Conversation Title functionality automatically extracts a concise, summary title based on conversation content after the user initiates a session for the first time, serving as the session title for that round of conversation. This feature enhances the browsability and organization of multi-round conversations, especially suitable for scenarios with many agent chat records.

| Configuration Item | Description                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| Enable/Disable     | Enabled by default, system will automatically generate titles for each new session                              |
| Title Prompt       | Supports configuring prompts to guide the large model to generate summary titles in specified styles or formats |

The system will automatically trigger title generation logic after the user sends the first message or when the system identifies that the conversation has initially formed.

#### 🧩 Examples

| Conversation Content                                                                                            | Auto-generated Title                             |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| "I want to understand our sales department's performance last month, can you break it down by region?"          | Sales Department Last Month Performance Analysis |
| "Can you help me write an introduction copy for the AI assistant feature? Make it a bit more relaxed in style." | AI Assistant Feature Copy Writing Request        |
| "Please explain the principles and application scenarios of the Memory Reply mechanism."                        | Memory Reply Mechanism Explanation               |

#### 🛠️ Configuration Suggestions

* For structured conversation scenarios (such as BI Q\&A, ticket systems), it is recommended to customize prompts to generate titles based on user intent or entity fields.
* Prompts should guide generation of **concise, specific, no redundant words** titles, for example:

  ```
  Summarize a one-sentence title to mark the theme of this user's question, avoiding redundant words.
  ```

***

### 7. File Upload

File Upload functionality allows users to upload specified types of files during conversations, inserting images or complete text into the current conversation to help AI better understand and respond to contextual questions.

#### ✅ Feature Description

* **Upload Location:**
  In the dialog box, users can upload files by clicking the 📎 icon (or "Upload a file" button).

* **After Upload Effect:**
  File content (such as document text, images, etc.) will be injected into the context as user messages for model reference, improving conversation understanding accuracy.

#### ⚙️ Configuration Items

* 1. Maximum Upload Count

- Value range: 1 \~ any value
- Meaning: Limits the number of files users can upload at once
- Example configuration: Maximum upload 10 files

* 2. File Size Limits (by type)

| File Type | Maximum Single File Size |
| --------- | ------------------------ |
| Document  | 15MB                     |
| Image     | 10MB                     |
| Audio     | 50MB                     |
| Video     | 100MB                    |

* 3. Supported File Types

Supports uploading the following types of files for easy understanding and parsing by large models:

* **Documents:** `TXT`, `MD`, `MDX`, `MARKDOWN`, `PDF`, `HTML`, `XLSX`, `XLS`, `DOC`, `DOCX`, `CSV`, `EML`, `MSG`, `PPTX`, `PPT`, `XML`, `EPUB`
* **Images:** `JPG`, `JPEG`, `PNG`, `GIF`, `WEBP`, `SVG`
* **Audio (if enabled):** `MP3`, `M4A`, `WAV`, `AMR`, `MPGA`
* **Video (if enabled):** `MP4`, `MOV`, `MPEG`, `WEBM`

> Supported file types can be configured through interface checkboxes. Non-checked types will be prohibited from uploading.

***

### 8. Text to Speech

Text to Speech (TTS) functionality supports users converting answer content to speech and playing it by clicking the read-aloud button after AI generates answers. This feature improves the accessibility and multimodal interaction capabilities of AI conversation systems, especially suitable for mobile scenarios, visually impaired users, information-intensive conversation scenarios with high reading pressure, etc.

#### ⚙️ Feature Description

| Configuration Item            | Description                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------ |
| TTS Model Selection           | Can configure different TTS models (such as Azure TTS, Google TTS, Edge-tts, local TTS, etc.)    |
| Model Parameter Configuration | Supports configuring parameters such as voice (Voice)                                            |
| Playback Trigger Method       | User clicks read-aloud button to trigger playback, supports play/stop operations                 |
| Multi-language Support        | As long as the model supports it, can automatically adapt to text reading in different languages |

***

### 9. Speech to Text

Speech to Text (STT) functionality allows users to use voice input instead of text input in dialog boxes. When this feature is enabled, users can click the microphone button to start recording, and the browser will capture the user's voice content and convert it to text after completion, sending it as question content to AI.

| Configuration Item                 | Description                                                                                                            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Enable Method                      | User clicks the microphone button in the conversation input box to start voice input                                   |
| Browser Permissions                | Requires user authorization for microphone use (usually prompts authorization on first use)                            |
| STT Model Support                  | Can integrate local browser recognition (such as Web Speech API) or external STT services (such as Whisper, Azure STT) |
| Recognition Language Configuration | Can preset recognition language (such as Chinese, English, etc.) to improve transcription accuracy                     |

#### 🔒 Privacy and Security Notes

* All voice content is only used for recognition purposes and is not stored or analyzed (unless user explicitly authorizes)
* Browser will prompt for microphone permission, users can close it at any time

***

## 📚 FAQ

### ❓1. Feature not working after enabling?

Possible causes and troubleshooting suggestions are as follows:

| Cause                                          | Troubleshooting and Solution                                                                                                                                                            |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature not saved                              | After enabling the feature, configuration has not been automatically saved.                                                                                                             |
| Incomplete configuration items                 | Some enhanced features (such as Memory Reply, TTS, etc.) require model or parameter configuration. If not configured, they will not take effect. Please check if anything is missing.   |
| Network exception or service dependency issues | Some enhanced features depend on external services (such as TTS/STT models, file storage services). It is recommended to check network connection or check console logs for API errors. |
| Suggested Questions                            | Only takes effect after publishing                                                                                                                                                      |

### ❓2. How to troubleshoot file upload failures?

File upload failures commonly occur in the following situations:

| Problem Type                                  | Troubleshooting Suggestions                                                                                                                                                                         |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upload size exceeded                          | Please confirm that uploaded files do not exceed system size limits (usually 20MB or administrator-configured limits).                                                                              |
| File type restricted                          | Currently only supports uploading common document types (such as .pdf, .docx, .xlsx, .csv, .txt, etc.). Please check if file extensions are supported.                                              |
| Network or server exception                   | Check browser console or network panel for upload failure prompts or API error messages.                                                                                                            |
| Browser does not support multi-file selection | Please ensure you use the latest versions of Chrome, Edge, Safari, and other modern browsers, avoiding browsers with poor compatibility.                                                            |
| File not bound to context after upload        | After successful upload, ensure files are bound to conversation context by the system, otherwise they will not participate in AI generation process. Try reselecting files and confirm file status. |

### ❓3. How to clear long-term memory content?

Long-term memory is used to save long-term conversation knowledge between users and Digital Experts, suitable for advanced scenarios such as customized replies and context understanding. To clear long-term memory, follow these steps:

#### ✅ Clear all long-term memory for a Digital Expert:

1. Enter the long-term memory management interface for that Digital Expert
2. Click the \[Clear Memory] button, system will prompt for confirmation
3. After confirmation, all memory entries for that agent will be deleted and cannot be recovered

#### ✅ Delete partial memory entries:

1. In the same "Memory Management" feature interface
2. For entries to delete, click \[Delete]
3. Can also use keyword search and then delete matching content

⚠️ Note:

* Clearing long-term memory will not affect short-term conversation history
* Memory cannot be recovered after clearing, please operate with caution
* After clearing, the system will rely on the base model to generate answers again, which may lack customized content


## 核心摘录

（在这里记录你阅读时的重点摘录）

## 个人解读

（在这里写下你的理解和思考）

## 待验证点

（记录文章中需要查证的信息）

## 关联问题

- 这个概念和其他知识有什么联系？
- 这个观点和我的已有认知是否冲突？

---

## 抓取备注

- 抓取时间：2026-05-08
- 抓取工具：手动导入
- 质量评分：
