---
title: Environment Variable Explanation
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
# Environment Variable Explanation

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment Variable Explanation

System parameters can be controlled through environment variables. For the community Docker deployment, use `docker/env.example` as the reference; if you are already inside the `docker/` directory, run `cp env.example .env` and then adjust the values as needed.

Some parameter explanations are as follows:

| Environment Variable | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| API\_BASE\_URL       | API service address (needs modification)                                    |
| CLIENT\_BASE\_URL    | Web client base URL (recommended to update together for server deployments) |
| WEB\_PORT            | Port of website                                                             |
| DB\_NAME             | Database name                                                               |
| DB\_USER             | Database username                                                           |
| DB\_PASS             | Database password                                                           |
| DB\_PORT             | Database port                                                               |
| DB\_HOST             | Database address                                                            |
| REDIS\_PASSWORD      | Cache service password                                                      |
| NODE\_ENV            | Operating environment: `development` or `production`                        |
| LOG\_LEVEL           | Log level                                                                   |
| DEFAULT\_LATITUDE    | Default latitude                                                            |
| DEFAULT\_LONGITUDE   | Default longitude                                                           |
| DEFAULT\_CURRENCY    | Default currency                                                            |
| DEMO                 | Demo system                                                                 |

## Organization Bootstrap and Templates

The following variables are mainly used when a new organization is created. They control the default workspace bootstrap flow, analytics seed data, and external xpert templates:

| Environment Variable                | Purpose                                                                                | How to configure                                                                                                 |
| ----------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| ORG\_DEFAULT\_XPERT\_TEMPLATE\_KEYS | Automatically import specific templates into each new organization's default workspace | Provide template IDs separated by commas; leave empty to disable automatic import                                |
| ORG\_ANALYTICS\_BOOTSTRAP\_MODE     | Controls analytics bootstrap mode for new organizations                                | Supported values are `semantic-only` and `full-demo`; unset or invalid values fall back to `semantic-only`       |
| XPERT\_TEMPLATE\_DIR                | External xpert template directory                                                      | Point this to a persistent directory; on first startup the API seeds any missing baseline template files into it |

Example:

```ini theme={null}
ORG_DEFAULT_XPERT_TEMPLATE_KEYS=af7133cb-32b3-47ff-90c1-b144c4d4887e,af7133cb-32b3-47ff-90c1-b144c4d48872
ORG_ANALYTICS_BOOTSTRAP_MODE=semantic-only
XPERT_TEMPLATE_DIR=/var/lib/xpert/data/xpert-template
```

Notes:

* `ORG_DEFAULT_XPERT_TEMPLATE_KEYS` uses template IDs, not display names. The two example IDs above correspond to `ChatBI with Sales Analysis Expert` and `Text2SQL-ChatDB`.
* `ORG_ANALYTICS_BOOTSTRAP_MODE=semantic-only` initializes only the semantic-model prerequisites; `full-demo` also imports demo indicators and demo stories.
* If `XPERT_TEMPLATE_DIR` is not set, the service falls back to the default data directory. In Docker this is typically `/var/lib/xpert/data/xpert-template`.
* These settings affect newly created organizations only. Existing organizations are not backfilled automatically.

## Permissions and Handoff Routing

| Environment Variable           | Purpose                                                                                         | How to configure                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| ALLOW\_SUPER\_ADMIN\_ROLE      | Controls whether `SUPER_ADMIN` can bypass tenant-level and organization-level permission guards | Defaults to `true`; only set it to `false` if you want to disable this bypass                  |
| HANDOFF\_ROUTING\_CONFIG\_PATH | Points to the handoff routing YAML file                                                         | You can use an absolute or relative path; relative paths are resolved from the API server root |

Example:

```ini theme={null}
ALLOW_SUPER_ADMIN_ROLE=true
HANDOFF_ROUTING_CONFIG_PATH=/var/lib/xpert/data/config/handoff-routing.yaml
```

The routing file structure can follow the sample in `docker/handoff-routing.example.yaml` from the Xpert source repository. A minimal example looks like this:

```yaml theme={null}
version: 1
defaultQueue: handoff
defaultLane: main
routes:
  - match:
      typePrefix: channel.lark.
    target:
      queue: integration
      lane: normal
```

Notes:

* `ALLOW_SUPER_ADMIN_ROLE` does not create or remove roles. It only controls whether `SUPER_ADMIN` automatically passes certain tenant and organization permission checks.
* If `HANDOFF_ROUTING_CONFIG_PATH` is not set, the service logs a warning and falls back to built-in defaults.
* The handoff routing file is loaded during module initialization, so API restart is required after editing the YAML file.

## Plugins and Default Skill Repositories

| Environment Variable             | Purpose                                                                         | How to configure                                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PLUGINS                          | Adds extra global plugin packages at deployment time                            | Separate plugin package names with commas or semicolons; the list is appended to the built-in global plugins rather than replacing them                                     |
| AI\_DEFAULT\_SKILL\_REPOSITORIES | Automatically registers default skill repositories when a new tenant is created | Pass a JSON string; the recommended shape is `{ "repositories": [...] }`; each entry must include at least `name` and `provider`, with optional `options` and `credentials` |

Example:

```ini theme={null}
PLUGINS=@xpert-ai/plugin-openrouter,@xpert-ai/plugin-gemini
AI_DEFAULT_SKILL_REPOSITORIES={"repositories":[{"name":"anthropics/skills","provider":"github","options":{"url":"https://github.com/anthropics/skills","branch":"main"}},{"name":"acme/internal-skills","provider":"github","options":{"url":"https://github.com/acme/internal-skills","path":"skills","branch":"main"},"credentials":{"token":"<github-token>"}}]}
```

Notes:

* `PLUGINS` is read during service startup, so API restart is required after changes.
* `AI_DEFAULT_SKILL_REPOSITORIES` also accepts a raw JSON array, but the wrapped `repositories` format from `docker/env.example` is recommended for future extensibility.
* The `provider` field in `AI_DEFAULT_SKILL_REPOSITORIES` must match a supported skill repository provider, such as `github` or `clawhub`.
* Invalid JSON is ignored and a warning is logged.
* These default repositories are only auto-registered for newly created tenants. Existing tenants need manual registration and sync through the skill repository APIs.

## Email related configuration

To customize the SMTP mail server configuration, you need to configure the following environment variables:

| Environment variable | Description              |
| -------------------- | ------------------------ |
| MAIL\_FROM\_ADDRESS  | Sender's email address   |
| MAIL\_HOST           | Mail service host        |
| MAIL\_PORT           | Mail service port number |
| MAIL\_USERNAME       | Mail account             |
| MAIL\_PASSWORD       | Mail password            |

## File Storage

Custom File Storage Providers

| Environment Variable        | Description                                |
| --------------------------- | ------------------------------------------ |
| FILE\_PROVIDER              | File storage provider (LOCAL \| S3 \| OSS) |
| ALIYUN\_ACCESS\_KEY\_ID     | Alibaba Cloud Access Key ID                |
| ALIYUN\_ACCESS\_KEY\_SECRET | Alibaba Cloud Access Key Secret            |
| ALIYUN\_REGION              | Alibaba Cloud Region                       |
| ALIYUN\_OSS\_ENDPOINT       | Alibaba Cloud OSS Endpoint                 |
| ALIYUN\_OSS\_BUCKET         | Alibaba Cloud OSS Bucket                   |
| AWS\_ACCESS\_KEY\_ID        | Amazon Cloud Access Key ID                 |
| AWS\_SECRET\_ACCESS\_KEY    | Amazon Cloud Secret Access Key             |
| AWS\_REGION                 | Amazon Cloud Region                        |
| AWS\_S3\_BUCKET             | Amazon Cloud S3 Bucket                     |


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
