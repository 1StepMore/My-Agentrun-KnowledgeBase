---
title: Lark Document Transformation Strategy
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
- Xpertai/XpertAI工作流教程-MD版/ai/plugin/feishu-document-example/transformer.md
---
# Lark Document Transformation Strategy

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Lark Document Transformation Strategy

## Code Review

```ts theme={null}
import { Injectable } from '@nestjs/common'
import { Document } from '@langchain/core/documents'
import {
  DocumentTransformerStrategy,
  IDocumentTransformerStrategy,
  IntegrationPermission,
  TDocumentTransformerConfig,
} from '@xpert-ai/plugin-sdk'
import { IconType, IKnowledgeDocument } from '@metad/contracts'
import { iconImage, LarkDocumentMetadata, LarkDocumentName, LarkName } from './types.js'
import { LarkClient } from './lark.client.js'

@Injectable()
@DocumentTransformerStrategy(LarkDocumentName)
export class LarkDocTransformerStrategy implements IDocumentTransformerStrategy<TDocumentTransformerConfig> {

  readonly permissions = [
    {
      type: 'integration',
      service: LarkName,
      description: 'Access to Lark system integrations'
    } as IntegrationPermission,
  ]

  readonly meta = {
    name: LarkDocumentName,
    label: {
      en_US: 'Lark Document',
      zh_Hans: '飞书文档'
    },
    description: {
      en_US: 'Load content from Lark documents',
      zh_Hans: '加载飞书文档内容'
    },
    icon: {
      type: 'image' as IconType,
      value: iconImage,
      color: '#14b8a6'
    },
    helpUrl: 'https://open.feishu.cn/document/server-docs/docs/docs-overview',
    configSchema: {
      type: 'object',
      properties: {},
      required: []
    }
  }

  validateConfig(config: any): Promise<void> {
    throw new Error('Method not implemented.')
  }

  async transformDocuments(
    files: Partial<IKnowledgeDocument<LarkDocumentMetadata>>[],
    config: TDocumentTransformerConfig
  ): Promise<Partial<IKnowledgeDocument<LarkDocumentMetadata>>[]> {
    const integration = config?.permissions?.integration
    if (!integration) {
      throw new Error('Integration system is required')
    }

    console.log('LarkDocTransformerStrategy transformDocuments', files, config)

    const client = new LarkClient(integration)
    
    const results: Partial<IKnowledgeDocument<LarkDocumentMetadata>>[] = []
    for await (const file of files) {
      const content = await client.getDocumentContent(file.metadata.token)
      results.push({
        id: file.id,
        chunks: [
          new Document({
            id: file.id,
            pageContent: content,
            metadata: {
              chunkId: file.id,
              source: LarkName,
              sourceId: file.id
            }
          })
        ],
        metadata: {
          assets: []
        } as LarkDocumentMetadata
      })
    }
    return results
  }
}
```

***

## Logic Breakdown

### 1. Decorators and Dependency Injection

```ts theme={null}
@Injectable()
@DocumentTransformerStrategy(LarkDocumentName)
```

* `@Injectable()`: NestJS dependency injection decorator, marks this as an injectable service.
* `@DocumentTransformerStrategy(LarkDocumentName)`: Registers the class as a **document transformation strategy** with the unique name `LarkDocumentName`.
  👉 This allows the system to automatically recognize and use this strategy.

***

### 2. Permission Definition

```ts theme={null}
readonly permissions = [
  {
    type: 'integration',
    service: LarkName,
    description: 'Access to Lark system integrations'
  } as IntegrationPermission,
]
```

* The plugin requires **Lark integration permission** to call the API and fetch documents.
* `IntegrationPermission` declares the dependent service, here it's `LarkName` (Lark).

***

### 3. Metadata (meta)

```ts theme={null}
readonly meta = {
  name: LarkDocumentName,
  label: {
    en_US: 'Lark Document',
    zh_Hans: '飞书文档'
  },
  description: {
    en_US: 'Load content from Lark documents',
    zh_Hans: '加载飞书文档内容'
  },
  icon: {
    type: 'image' as IconType,
    value: iconImage,
    color: '#14b8a6'
  },
  helpUrl: 'https://open.feishu.cn/document/server-docs/docs/docs-overview',
  configSchema: { ... }
}
```

* **Plugin UI display info**: name, icon, description, help documentation link.
* `configSchema`: Defines configuration options (empty here, meaning no extra parameters required).

***

### 4. Configuration Validation

```ts theme={null}
validateConfig(config: any): Promise<void> {
  throw new Error('Method not implemented.')
}
```

* Placeholder method for future configuration validation.
* For example: check if document ID or token is provided.

***

### 5. Core Document Transformation Logic

```ts theme={null}
async transformDocuments(
  files: Partial<IKnowledgeDocument<LarkDocumentMetadata>>[],
  config: TDocumentTransformerConfig
): Promise<Partial<IKnowledgeDocument<LarkDocumentMetadata>>[]> {
  const integration = config?.permissions?.integration
  if (!integration) {
    throw new Error('Integration system is required')
  }

  const client = new LarkClient(integration)
  
  const results: Partial<IKnowledgeDocument<LarkDocumentMetadata>>[] = []
  for await (const file of files) {
    const content = await client.getDocumentContent(file.metadata.token)
    results.push({
      id: file.id,
      chunks: [
        new Document({
          id: file.id,
          pageContent: content,
          metadata: {
            chunkId: file.id,
            source: LarkName,
            sourceId: file.id
          }
        })
      ],
      metadata: {
        assets: []
      } as LarkDocumentMetadata
    })
  }
  return results
}
```

Line-by-line explanation:

1. **Get Integration Info**

   ```ts theme={null}
   const integration = config?.permissions?.integration
   if (!integration) throw new Error('Integration system is required')
   ```

   * Retrieves Lark integration credentials from config.
   * Throws error if credentials are missing.

2. **Initialize Client**

   ```ts theme={null}
   const client = new LarkClient(integration)
   ```

   * Constructs `LarkClient` with credentials to access Lark API.

3. **Process Files in a Loop**

   ```ts theme={null}
   for await (const file of files) {
     const content = await client.getDocumentContent(file.metadata.token)
   }
   ```

   * Iterates over the list of documents to process.
   * Calls `client.getDocumentContent` to fetch document content by `token`.

4. **Build Transformed Document**

   ```ts theme={null}
   results.push({
     id: file.id,
     chunks: [
       new Document({
         id: file.id,
         pageContent: content,
         metadata: {
           chunkId: file.id,
           source: LarkName,
           sourceId: file.id
         }
       })
     ],
     metadata: {
       assets: []
     } as LarkDocumentMetadata
   })
   ```

   * Each Lark document is converted to an `IKnowledgeDocument`.
   * Main content is placed in the `chunks` array.
   * `metadata` stores extra info (currently only `assets`).

***

## Overall Execution Flow

1. **Input**: A batch of Lark document metadata (file ID / token).
2. **Permission Validation**: Ensure Lark integration config is present.
3. **API Call**: Use `LarkClient` to fetch the content of each document.
4. **Transform to Knowledge Base Format**:

   * Wrap as `IKnowledgeDocument`
   * Content is chunked into `Document` (for later vectorization)
5. **Output**: Returns an array of documents usable by Xpert AI Knowledge Base.

***

## Core Value

* **Decoupling**: The strategy class does not call the API directly, but relies on `LarkClient`.
* **Generality**: All documents are ultimately converted to `IKnowledgeDocument`, seamlessly integrating with the platform's knowledge base.
* **Extensibility**: In the future, you can add to `transformDocuments`:

  * Text cleaning (remove empty lines/formatting)
  * Content chunking
  * Metadata enhancement (author, tags, update time)
