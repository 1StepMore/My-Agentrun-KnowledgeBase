---
title: Plugin Permission Design Guide
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
# Plugin Permission Design Guide

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugin Permission Design Guide

<Tip>
  Design a configuration in `meta` that allows the plugin to request large model invocation permissions from the core system (e.g., request an OpenAI Client instance). For example, declare the large model permission request in `meta`, design properties in `configSchema` for users to configure the model provider and model name, and when the core system detects the permission request, it will instantiate the large model Client according to the user's config and inject it into the `understandImages` method via `config`.
</Tip>

👌 Got it! You want to **declare the required large model permission request in the plugin Strategy's meta**, so the core system can parse it and automatically inject a `client` into `config` based on user configuration (model provider + model name + other parameters). This way, the plugin doesn't need to create its own OpenAI / Anthropic / other VLM client.

I'll help you redesign the `OpenAIGPT4VStrategy` meta and configSchema so it can **request the Client from the core system**.

***

## New Strategy

```ts theme={null}
import { Injectable } from '@nestjs/common';
import { Document } from 'langchain/document';
import {
  ImageUnderstandingStrategy,
  IImageUnderstandingStrategy,
  TImageUnderstandingFile,
  TImageUnderstandingResult
} from './strategy.interface';

@Injectable()
@ImageUnderstandingStrategy('openai-gpt4v')
export class OpenAIGPT4VStrategy implements IImageUnderstandingStrategy<any> {
  readonly meta = {
    name: 'openai-gpt4v',
    label: { en: 'OpenAI GPT-4 Vision', zh: 'OpenAI GPT-4 图像理解' },

    /**
     * Permission declaration: tells the core system this plugin needs an "llm" permission,
     * provider is openai, capability is vision.
     * The core system will instantiate the corresponding Client based on config.provider + config.model,
     * and inject it into config.client.
     */
    permissions: [
      {
        type: 'llm',
        provider: 'openai',
        capability: 'vision',
      },
    ],

    /**
     * Config schema: users need to fill in provider and model.
     * The core system will instantiate the Client based on provider + model + user's API Key,
     * and inject it.
     */
    configSchema: {
      type: 'object',
      properties: {
        provider: { 
          type: 'string', 
          enum: ['openai'], 
          description: 'Model provider' 
        },
        model: { 
          type: 'string', 
          default: 'gpt-4-vision-preview', 
          description: 'Model name' 
        },
        prompt: { 
          type: 'string', 
          default: 'Describe this image in detail.', 
          description: 'Prompt (customize the understanding task)' 
        }
      },
      required: ['provider', 'model']
    },

    icon: {
      svg: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><circle cx="10" cy="10" r="8" stroke="black" fill="none"/><text x="6" y="14">VLM</text></svg>',
      color: '#10a37f'
    }
  };

  async validateConfig(config: any): Promise<void> {
    if (!config.client) {
      throw new Error('Missing injected LLM client in config. Core system must inject client.');
    }
  }

  async understandImages(
    files: TImageUnderstandingFile[],
    config: any
  ): Promise<TImageUnderstandingResult[]> {
    const client = config.client; // ✅ Injected by core system
    const results: TImageUnderstandingResult[] = [];

    for (const file of files) {
      const description = await this.runGPT4V(client, file.path, config);

      const doc = new Document({
        pageContent: description,
        metadata: {
          chunkId: `img-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
          parentChunkId: file.parentChunkId,
          imagePath: file.path,
          source: file.filename,
          type: 'vlm',
          engine: config.model
        }
      });

      results.push({
        docs: [doc],
        metadata: { engine: config.model, file: file.filename }
      });
    }

    return results;
  }

  private async runGPT4V(client: any, imagePath: string, config: any): Promise<string> {
    // client is already an openai client, instantiated by the core system
    const response = await client.chat.completions.create({
      model: config.model,
      messages: [
        {
          role: 'user',
          content: [
            { type: 'text', text: config.prompt || 'Describe this image in detail.' },
            { type: 'image_url', image_url: { url: imagePath } }
          ]
        }
      ],
      max_tokens: 500
    });

    return response.choices[0]?.message?.content || '';
  }
}
```

***

## 🔑 How the Core System Handles This

* Parse the plugin's `meta.permissions` and find it needs:

  ```json theme={null}
  { "type": "llm", "provider": "openai", "capability": "vision" }
  ```
* Instantiate `OpenAI({ apiKey: userApiKey })` according to user `config.provider = "openai"`, `config.model = "gpt-4-vision-preview"`
* Inject the client into `config.client`
* Call `strategy.understandImages(files, config)`

***

## 📌 Usage Example

```ts theme={null}
const strategy = this.imageUnderstandingRegistry.get('openai-gpt4v');
const result = await strategy.understandImages(
  [
    { 
      path: 'https://example.com/chart.png', 
      filename: 'chart.png', 
      extname: 'png', 
      parentChunkId: 'uuid-123' 
    }
  ],
  { 
    provider: 'openai',
    model: 'gpt-4-vision-preview',
    prompt: 'Please describe this image in detail in Chinese.',
    client: openaiClient // ✅ Injected by core system
  }
);

console.log(result[0].docs[0].pageContent);
```

***

This way, the plugin itself does not depend on any `openai` wrapper logic—**it only declares permissions + requires provider/model**, and the core system can inject the appropriate client.

Would you like me to write an **abstract permission declaration interface (e.g., ILLMPermissionRequest)** so OCR/VLM/Embedding plugins can declare dependencies in a unified way?


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
