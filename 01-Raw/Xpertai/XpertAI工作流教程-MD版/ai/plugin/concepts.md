---
title: Core Concepts of the Plugin System
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
# Core Concepts of the Plugin System

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Core Concepts of the Plugin System

In the Xpert AI plugin system, all plugins follow a unified interface specification and lifecycle management. Through a set of core concepts, developers can easily extend the host system's capabilities without modifying the core code.

***

### 2.1 XpertPlugin

`XpertPlugin` is the main entry interface for plugins, defining plugin metadata (`meta`), configuration (`config`), lifecycle methods, and module registration logic.

```ts theme={null}
export interface XpertPlugin<TConfig extends object = any> 
  extends PluginLifecycle, PluginHealth {
  meta: PluginMeta;                       // Plugin metadata
  config?: PluginConfigSpec<TConfig>;     // Plugin configuration
  register(ctx: PluginContext<TConfig>): DynamicModule; // Register plugin module
}
```

* **meta**: Basic plugin metadata, including `name`, `version`, `category`, `icon`, `description`, etc.
* **config**: Defines the plugin's configuration schema (based on `zod`), supporting default values and UI form rendering.
* **register**: Returns a `DynamicModule` to mount the plugin to the main application (optionally as global).

***

### 2.2 Plugin Lifecycle

The plugin system provides a complete set of lifecycle hooks for each plugin, allowing developers to execute initialization or cleanup logic at different stages.

```ts theme={null}
export interface PluginLifecycle {
  onInit?(ctx: PluginContext): Promise<void> | void;   // Called after module registration
  onStart?(ctx: PluginContext): Promise<void> | void;  // Called after app startup (services available)
  onStop?(ctx: PluginContext): Promise<void> | void;   // Called during graceful shutdown
}
```

* **onInit**: Suitable for resource initialization (e.g., loading configs, registering resource pools).
* **onStart**: Suitable for starting background tasks or service listeners.
* **onStop**: Suitable for cleaning up resources, closing connections, releasing caches.

***

### 2.3 Plugin Health Check

Plugins can implement the `checkHealth` method to report their running status, enabling unified health monitoring by the host system.

```ts theme={null}
export interface PluginHealth {
  checkHealth?(ctx: PluginContext): Promise<{ status: 'up' | 'down'; details?: any }> 
}
```

* **status**: Running status (`up` or `down`)
* **details**: Optional dependency check details, such as API connectivity or database status

***

### 2.4 Plugin Context

`PluginContext` provides plugins with runtime access to the host system, including application context, logging service, and configuration.

```ts theme={null}
export interface PluginContext<TConfig extends object = any> {
  app: INestApplicationContext;   // Nest runtime context
  logger: PluginLogger;           // SDK-provided logging wrapper
  config: TConfig;                // Final validated and merged config
  resolve<TInput, TResult>(token: any): TResult; // Dependency injection resolver
}
```

* **app**: NestJS's `INestApplicationContext`, allowing access to the DI container.
* **logger**: Unified logging interface, supporting `debug`, `log`, `warn`, `error`.
* **config**: Final config object after zod validation and merging defaults.
* **resolve**: Retrieve other providers from the NestJS container.

***

### 2.5 Plugin Configuration Specification

Each plugin can define a configuration specification to constrain and validate config parameters, usually implemented via a `zod` schema:

```ts theme={null}
export interface PluginConfigSpec<T extends object = any> {
  schema?: ZodSchema<T>;       // Config validation schema
  defaults?: Partial<T>;       // Default config
}
```

* Supports **type safety** (zod type inference)
* Supports **default values** and **secure input** (e.g., API key secrets)
* The host system automatically renders the config UI based on the schema

***

### 2.6 XpertServerPlugin Decorator

`@XpertServerPlugin` is an enhanced [Nestjs Module](https://docs.nestjs.com/modules) class decorator, used to register plugins as NestJS modules and attach plugin metadata.

```ts theme={null}
@XpertServerPlugin({
  imports: [ /* submodules */ ],
  providers: [ /* services, strategies */ ],
  controllers: [ /* controllers */ ],
  entities: [ /* database entities */ ],
})
export class FirecrawlPlugin { ... }
```

* Essentially extends NestJS's `@Module` decorator
* Supports registering submodules, services, controllers, entities, etc.
* The plugin thus becomes a complete NestJS dynamic module

***

### 2.7 Enhancement Points

Enhancement points are the key mechanism for plugins to extend the host system. The host system defines a series of strategy interfaces, and plugins can implement these interfaces and use decorators to be automatically discovered and registered.

#### IntegrationStrategy

Used to connect external systems or API services, such as Firecrawl, OpenAI, etc.

```ts theme={null}
export interface IntegrationStrategy<T = unknown> {
  meta: TIntegrationProvider;  
  execute(integration: IIntegration<T>, payload: TIntegrationStrategyParams): Promise<any>;
}
```

* **meta**: Metadata for the integration provider (name, description, icon, etc.)
* **execute**: Executes the integration logic (e.g., calling external APIs)

Decorator:

```ts theme={null}
@IntegrationStrategyKey('Firecrawl')
@Injectable()
export class FirecrawlIntegrationStrategy implements IntegrationStrategy<FirecrawlOptions> { ... }
```

#### DocumentSourceStrategy

Used to connect new data sources, such as web crawlers, file parsers, databases. Plugins only need to implement the corresponding interface to make the data source available to agents/BI.

***

### 2.8 Strategy Registry

All strategy classes (Integration, DocumentSource, etc.) are registered to the **strategy registry** via **decorators + NestJS dependency injection**.

For example, IntegrationStrategy:

```ts theme={null}
@Injectable()
export class IntegrationStrategyRegistry 
  extends BaseStrategyRegistry<IntegrationStrategy> {
  constructor(discoveryService: DiscoveryService, reflector: Reflector) {
    super(INTEGRATION_STRATEGY, discoveryService, reflector);
  }
}
```

* `IntegrationStrategyRegistry` automatically discovers classes decorated with `@IntegrationStrategyKey`
* Plugins do not need to manually register strategies; implementing the interface and using the decorator is enough for system recognition

***

📌 Summary:

* `XpertPlugin` defines plugin **metadata, configuration, and lifecycle**
* `XpertServerPlugin` registers plugins as **NestJS modules**
* **Enhancement points (Strategy)** are the core for plugins to extend host system functionality
* All plugins form extensible and maintainable modules via **lifecycle + strategy interfaces + config schema**


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
