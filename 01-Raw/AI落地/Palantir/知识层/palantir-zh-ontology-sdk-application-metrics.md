---
title: Palantir 官方文档 · ontology-sdk · 应用指标
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/application-metrics/
lang: zh
keywords:
- Palantir
- Foundry
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:24:14+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

# 应用指标

:::callout{theme="neutral"}
应用指标功能处于[测试阶段](https://www.palantir.com/docs/foundry/platform-overview/development-life-cycle/#beta)，可能无法在您的注册中使用。
:::

应用指标使用一组图表提供关于您的应用随时间表现的见解。这些图表包括随时间变化的请求数量、请求的成功率以及与您调用的API端点相关的延迟。

从Developer Console左侧菜单导航到**指标**页面，以查看您的Ontology SDK使用情况的指标。

![Developer Console中的应用指标页面。](../../foundry-docs/ontology-sdk/media/metrics.png)

指标目前提供约24小时的延迟和最长30天的历史视图。

您必须在应用中使用一个[支持的OAuth流程](/docs/foundry/ontology-sdk/permissions/#permission-types)以收集指标。使用在此OAuth流程之外生成的API词元进行的API调用将不会在您的应用指标中收集。例如，如果您在TypeScript或Python中使用`UserTokenAuth`进行连接，则通过该客户端进行的调用将不会显示在指标应用中。然而，如果您使用`PublicClientAuth`或`ConfidentialClientAuth`进行连接，则您的调用将会出现在Developer Console中。

## 配置时间段

您可以使用顶部导航栏中的时间范围选择器配置显示指标的时间段。可用的预设选项包括一天、两天、七天、14天和30天。您也可以选择**自定义**下拉菜单以选择过去30天内的任何时间段。

在查看时间段为五天或更短的指标时，数据点以每小时为单位显示。在时间段超过五天时，数据点以每天为单位显示。

## API延迟

**延迟**卡片允许您查看由Ontology SDK进行的API调用的50th、75th、95th和99th百分位数的延迟。

要查看特定端点在给定时间段内的延迟更改，您可以选择端点以及您希望查看数据的百分位数：

![应用指标延迟卡片](../../foundry-docs/ontology-sdk/media/metrics-latency-chart.png)
