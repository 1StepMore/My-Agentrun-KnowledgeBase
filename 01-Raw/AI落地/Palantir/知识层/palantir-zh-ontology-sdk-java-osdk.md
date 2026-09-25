---
title: Palantir 官方文档 · ontology-sdk · Java Ontology SDK (OSDK)
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/java-osdk/
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

# Java Ontology SDK (OSDK)

本页面基于一个示例餐馆对象及其相关操作和查询，提供Java OSDK的通用文档。您可以在平台中使用开发者控制台[根据您的特定Ontology生成文档](/docs/foundry/ontology-sdk/create-a-new-osdk/)。

| 属性 | API 名称 | 类型 |
|---|---|---|
| `Restaurant Id` (主键) | `restaurantId` | 字符串 |
| `Restaurant Name` (标题) | `restaurantName` | 字符串 |
| `Address` | `address` | 字符串 |
| `E Mail` | `eMail` | 字符串 |
| `Number Of Reviews` | `numberOfReviews` | Integer |
| `Phone Number` | `phoneNumber` | 字符串 |
| `Review Summary` | `reviewSummary` | 字符串 |
| `Date Of Opening` | `dateOfOpening` | LocalDate |

## 加载单个`Restaurant`

参数：

* primaryKey `string`: 您想获取的`Restaurant`的主键
  示例查询：

```java
// 从ontology中获取Restaurant对象，如果不存在则抛出异常
Restaurant result = client.ontology().objects().Restaurant().fetch("primaryKey").orElseThrow();
```

## 加载`Restaurants`流

加载可收集的对象流。这会根据用户流式传输的对象数量自动加载对象页面。

请注意，此端点利用了用于对象类型的底层对象同步技术。如果`Restaurant`由对象存储V2支持，则没有请求限制。如果`Restaurant`由对象存储V1（Phonograph）支持，则限制为10,000个结果；如果请求超过10,000个`Restaurants`，将抛出`ObjectsExceededLimit`出错。

示例查询：

```java
Stream<Restaurant> result = client.ontology().objects().Restaurant().fetchStream()
// 从本体中获取餐厅对象的流
```

## 加载所有 `Restaurants`

将所有 `Restaurant` Object 加载到一个列表中。

请注意，此端点利用了用于对象类型的基础对象同步技术。如果 `Restaurant` 由 Object Storage v2 支持，则没有请求限制。如果 `Restaurant` 由 Object Storage v1 (Phonograph) 支持，则限制为10,000个结果；如果请求超过10,000个 `Restaurants`，将会抛出一个 `ObjectsExceededLimit` 出错。

示例查询：

```java
List<Restaurant> result = client.ontology().objects().Restaurant().fetchStream().toList()
// 从本体中获取餐馆对象，转换为流并收集到列表中
```

示例 API 响应：

## 加载有序结果

通过为特定属性指定排序方向来加载有序的`Restaurants`列表。通过API调用时，排序标准通过`fields`数组指定。通过SDK调用时，可以将多个`orderBy`调用链接在一起。字符串的排序顺序是区分大小写的，这意味着数字会排在大写字母之前，大写字母会排在小写字母之前。例如，Cat 会排在 bat 之前。

参数：

* ordering `{ObjectType}Ordering`：您想要排序的属性。在Java SDK中，这通过`{ObjectType}Ordering`接口为您提供。
* 属性名称和方向 `ASC`| `DESC`：您要排序的方向，可以是升序或降序。在Java SDK中，这通过`{ObjectType}Ordering`接口上的`{PROPERTY_NAME}_ASC`和`{PROPERTY_NAME}_DESC`限定符提供。

查询示例：

```java
Stream<Aircraft> result = client.ontology()
    .objects()
    .Restaurant()  // 获取 Restaurant 对象流
    .orderBy(RestaurantOrdering.RESTAURANT_NAME_ASC)  // 按照餐厅名称升序排序
    .fetchStream();  // 获取排序后的流
```

## 筛选

您可以执行的筛选类型取决于给定对象类型的属性类型。这些筛选还可以通过布尔表达式组合在一起，以构建更复杂的筛选。

请注意，此端点利用用于对象类型的底层对象同步技术。如果`Restaurant`由Object Storage v2支持，则没有请求限制。如果`Restaurant`由Object Storage v1 (Phonograph)支持，则有10,000个结果的限制；如果请求的`Restaurants`超过10,000，将抛出`ObjectsExceededLimit`出错。

参数：

* where `筛选` (非必填): 筛选特定属性。可能的操作取决于属性的类型。这通过`{ObjectType}筛选`表示，并为每个属性调用方法。
* orderBy `OrderBy` (非必填): 基于特定属性对结果排序。如果使用SDK，您可以将`.where`调用与`orderBy`调用链接以实现相同的结果。这通过`{ObjectType}OrderBy`表示，并为每个属性调用方法。

示例查询：

```java
List<Restaurant> result = client.ontology()
    .objects()
    .Restaurant()
    .where(RestaurantFilter.restaurantName().isNull(false)) // 过滤掉restaurantName为空的餐馆
    .fetchStream() // 从数据库中获取流数据
    .toList(); // 将流数据转换为列表
```

### 搜索筛选的类型 (`RestaurantFilter`)

#### 起始

仅适用于字符串属性。搜索`Restaurants`，其中`restaurantName`以给定的字符串开头（不区分大小写）。

参数：

* 字段 `method`：要使用的属性名称（例如，restaurantName）。
* 值 `string`：用于与`Restaurant Name`进行前缀匹配的值。例如，“foo”将匹配“foobar”而不匹配“barfoo”。

示例查询：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Restaurant()
    .where(RestaurantFilter.restaurantName().startsWith("foo")); // 过滤名称以 "foo" 开头的餐馆对象
```

#### 包含任意术语

仅适用于字符串属性。返回`Restaurants`，其中`restaurantName`包含提供的值中以空格分隔的任意顺序的单词（不区分大小写）。

参数：

* 字段 `method`: 要使用的属性名称（例如，restaurantName）。
* 值 `string`: 用空格分隔的匹配单词集。例如，“foo bar”将匹配“bar baz”但不匹配“baz qux”。

示例查询：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    .where(RestaurantFilter.restaurantName().containsAnyTerm("foo bar"));
    // 这里的代码从本体（ontology）中查询对象（objects），
    // 并使用过滤器（where）条件匹配餐厅名称中包含“foo”或“bar”任一术语的记录。
```

#### 包含所有词元

仅适用于字符串属性。返回`restaurantName`包含提供值中所有以空格分隔的词（不区分大小写，顺序不限）的`Restaurants`。

参数：

* 字段 `method`: 使用的属性名称（例如，`restaurantName`）。
* 值 `string`: 用空格分隔的要匹配的词集。例如，“foo bar”将匹配“hello foo baz bar”，但不匹配“foo qux”。

示例查询：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    // 过滤餐厅名称包含所有术语 "foo bar"
    .where(RestaurantFilter.restaurantName().containsAllTerms("foo bar"));
```

#### 包含所有术语按顺序

仅适用于字符串属性。返回`restaurantName`包含所有提供的术语（不区分大小写）的`Restaurants`，但它们确实必须彼此相邻。

参数：

* 字段 `method`: 要使用的属性名称（例如，`restaurantName`）。
* 值 `string`: 用空格分隔的词组集合以进行匹配。例如，“foo bar”将匹配“hello foo bar baz”但不匹配“bar foo qux”。

示例查询：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    .where(RestaurantFilter.restaurantName().containsAllTermsInOrder("foo bar"));
// 创建一个名为result的RestaurantObjectSet对象
// 使用client的ontology()方法获取本体对象
// 调用objects()方法获取所有对象
// 使用Aircraft()方法筛选出与Aircraft相关的对象
// 使用where()方法定义过滤条件
// 通过RestaurantFilter.restaurantName()方法过滤餐馆名称
// containsAllTermsInOrder("foo bar")确保餐馆名称包含"foo bar"且顺序一致
```

#### 范围比较

仅适用于数值、字符串和日期时间属性。返回`Restaurants`，其中`Restaurant.restaurantName`小于某个值。

参数：

* 字段 `method`：要使用的属性名称（例如 `restaurantName`）。
* 值 `string`：用于比较`Restaurant Name`的值

比较类型：

* 小于 `lt`
* 大于 `gt`
* 小于或等于 `lte`
* 大于或等于 `gte`

示例查询：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft() // 假设此处为调用某种对象类型为Aircraft的集合
    .where(RestaurantFilter.restaurantName().lt("Restaurant Name")); // 过滤条件：餐馆名称小于"Restaurant Name"
```

#### 等于

仅适用于布尔、日期时间、数字和字符串属性。搜索`Restaurants`中`restaurantName`等于给定值的项。

参数:

* 字段 `method`: 要使用的属性名称（例如`restaurantName`）。
* 值 `string`: 用于与`Restaurant Name`进行相等性检查的值。

示例查询:

```java
// 创建一个RestaurantObjectSet类型的变量result，用于存储查询结果
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    // 使用where方法进行过滤，筛选出餐馆名称等于"Restaurant Name"的对象
    .where(RestaurantFilter.restaurantName().eq("Restaurant Name"));
```

#### 空值检查

仅适用于数组、布尔值、日期时间、数值和字符串属性。基于`restaurantName`是否存在的值来搜索`Restaurants`。

参数：

* field `method`: 要使用的属性名称（例如 `restaurantName`）。
* value `boolean`: `Restaurant Name`是否存在。请注意，对于TypeScript SDK，您需要使用非筛选来检查字段是否为非空。

示例查询：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    .where(RestaurantFilter.restaurantName().isNull(true));
// 该代码段从客户端的本体中获取对象集合，选择与Aircraft相关的对象。
// 然后通过过滤条件选择restaurantName为空的对象。
```

#### `Not` 筛选

返回查询不满足条件的`餐馆`。这可以进一步与其他布尔筛选操作组合。

参数:

* value `筛选`: 要反转的搜索查询。

示例查询:

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    .where(
        RestaurantFilter.$not(
            RestaurantFilter.restaurantName().isNull(true)
        )
    );
// 这个代码片段用于从一个本体（ontology）中获取对象集合（例如，Aircraft类型的对象）。
// 使用了过滤器（filter）来排除restaurantName属性为空的对象。
```

#### `And` 筛选

返回满足所有查询条件的 `Restaurants`。这可以进一步与其他布尔筛选操作组合。

参数：

* 值 `筛选[]`：要合并在一起的查询条件集。

示例查询：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    .where(
        RestaurantFilter.$and(
            // 检查餐厅名称是否不为空
            RestaurantFilter.restaurantName().isNull(false),
            // 检查餐厅名称是否等于指定的主键
            RestaurantFilter.restaurantName().eq("<primarykey>")
        )
    );
```

#### `Or` 筛选

返回满足任意指定查询的`Restaurants`。这可以进一步与其他布尔筛选操作结合。

参数：

* 值 `Filter[]`: 要`or`在一起的查询集合。

查询示例：

```java
RestaurantObjectSet result = client.ontology()
    .objects()
    .Aircraft()
    .where(
        RestaurantFilter.$or(
            RestaurantFilter.restaurantName().isNull(false), // 检查餐厅名称是否不为空
            RestaurantFilter.restaurantName().eq("<primarykey>") // 检查餐厅名称是否等于指定的主键
        )
    );
```

## 聚合

聚合允许您计算数据集上的汇总统计信息。它们对于从大型数据集中理解模式和洞察非常有用，而无需手动分析每个单独的数据点。您可以组合多个聚合操作以创建更复杂的查询，从而提供对数据的更深入的洞察。

请注意，此端点利用用于对象类型的底层对象同步技术。如果`Restaurant`由Object Storage v2支持，则没有请求限制。如果`Restaurant`由Object Storage v1 (Phonograph)支持，则结果限制为10,000个；如果请求超过10,000个`Restaurants`，将抛出`ObjectsExceededLimit`出错。

对`Restaurants`执行聚合。

参数：

* aggregation `Aggregation[]`（非必填）：要执行的一组聚合函数。使用SDK时，聚合计算可以通过进一步的搜索使用 `.where` 链接在一起。
* groupBy `GroupBy[]`（非必填）：创建聚合结果的分组集
* where `Filter`（非必填）：对特定属性进行筛选。可能的操作取决于属性的类型。

示例查询：

```java
AggregationResponse numRestaurants = client.ontology()
        .objects()
        .Restaurants()
        .where(RestaurantFilter.restaurantName().isNull(false)) // 过滤条件：餐馆名称不为空
        .groupBy(GroupBy.exact(Restaurant.Property.restaurantName())) // 按餐馆名称进行分组
        .count() // 统计每个分组的数量
        .compute(); // 执行聚合计算
```

### 聚合类型 (`Aggregation`)

#### 近似不重复值

计算`restaurantName`的不重复值的近似数量。

参数：

* 字段 `Property`：要使用的属性名称（例如 `restaurantName`）。
* 名称 `字符串`（非必填）：计算计数的别名。默认情况下，这是 `distinctCount`。

示例查询：

```java
Double distinctRestaurants = client.ontology()
        .objects()
        .Restaurant()
        .approximateDistinct(Restaurant.Property.restaurantName())
        .compute();

// 计算餐厅名称的近似唯一值数量
// 这与上面的代码等效，但使用 metricName 作为度量名称，而不是默认的 "distinctCount"

AggregationResponse distinctRestaurants = client.ontology()
        .objects()
        .Restaurant()
        .aggregate(
            Map.of(
                "metricName",
                Aggregation.approximateDistinct(Restaurant.Property.restaurantName())
            )
        )
        .compute();
```

#### 计数

计算`餐厅`的总计数。

参数：

* name `字符串` (非必填): 计算总数的别名。默认情况下，这是`count`。

示例查询：

```java
Double distinctRestaurants = client.ontology()
        .objects()
        .Restaurant()
        .count()
        .compute(); // 计算不同餐馆的数量
```

#### 数值聚合

仅适用于数值属性。计算`Restaurants`数值属性的最大值、最小值、总和或平均值。

参数：

* 字段 `NumericProperty`：要使用的属性名称（例如`numberOfReviews`）。
* 名称 `字符串`（非必填）：计算值的别名。

聚合类型：

* 平均值：`avg()`
* 最大值：`max()`
* 最小值：`min()`
* 总和：`sum()`

示例查询：

```java
Double avgReviewScore = client.ontology()
        .objects()
        .Restaurant()
        .avg(Restaurant.Property.numberOfReviews())
        .compute();

// 这段代码等价于上面的代码，但使用 "avgReview" 作为指标名称，而不是默认的 "avg"

AggregationResponse distinctRestaurants = client.ontology()
        .objects()
        .Restaurant()
        .aggregate(
            Map.of(
                "avgReview",
                Aggregation.avg(Restaurant.Property.numberOfReviews())
            )
        )
        .compute();
```

### 分组类型 (`GroupBy`)

#### 精确分组

通过`restaurantName`的确切值对`Restaurants`进行分组。

参数：

* 字段 `Property`: 要使用的属性名称（例如 `restaurantName`）。
* 最大分组数 `integer`（非必填）：要创建的`restaurantName`的最大分组数。

示例查询：

```java
AggregationResponse groupedRestaurants = client.ontology()
       .objects()
       .Restaurant()
       .groupBy(GroupBy.exact(Restaurant.Property.restaurantName())) // 按餐厅名称精确分组
       .count() // 统计每个分组的数量
       .compute();
```

#### 数值分桶

通过将`numberOfReviews`按指定宽度分桶对`Restaurants`进行分组。

参数：

* 字段 `NumericProperty`: 要使用的属性名称（例如`numberOfReviews`）。
* 固定宽度 `integer` （非必填）: 要将选择的属性分成的每个桶的宽度。

示例查询：

```java
AggregationResponse groupedRestaurants = client.ontology()
       .objects()
       .Restaurant()
       // 按照 numberOfReviews 属性以固定宽度为10进行分组
       .groupBy(GroupBy.fixedWidth(Restaurant.Property.numberOfReviews(), 10))
       // 统计每个组的数量
       .count()
       // 执行计算
       .compute();
```

#### 范围分组

以指定的`numberOfReviews`范围对`Restaurants`进行分组。

参数:

* 字段 `NumericProperty | DateProperty | TimestampProperty`: 要使用的属性名称（例如`numberOfReviews`）。
* 范围 `AggregationRange[]` (非必填): 一组范围，这些范围具有包含的起始值和排除的结束值。

查询示例:

```java
AggregationResponse groupedRestaurants = client.ontology()
    .objects()
    .Restaurant()
    .groupBy(
        GroupBy.range(
            Restaurant.Property.numberOfReviews(),
            List.of(
                AggregationRange.of(0, 3), // 将评论数量在0到3之间的餐馆分组
                AggregationRange.of(3, 5)  // 将评论数量在3到5之间的餐馆分组
            )
        )
    )
    .count() // 计算每个分组中餐馆的数量
    .compute(); // 执行聚合计算
```

```json
{
    "excludedItems": 0,  // 排除的项目数为0
    "data": [
        {
            "group": {
                "numberOfReviews": {
                    "startValue": 0,  // 评价数量的起始值为0
                    "endValue": 3     // 评价数量的结束值为3
                }
            },
            "metrics": [
                {
                    "name": "count",  // 指标名称为"count"
                    "value": 50       // 对应的指标值为50
                }
            ]
        },
        {
            "group": {
                "numberOfReviews": {
                    "startValue": 3,  // 评价数量的起始值为3
                    "endValue": 5     // 评价数量的结束值为5
                }
            },
            "metrics": [
                {
                    "name": "count",  // 指标名称为"count"
                    "value": 30       // 对应的指标值为30
                }
            ]
        }
    ]
}
```

此JSON数据结构用于表示不同评价数量区间内的项目统计信息。`excludedItems`字段表示被排除的项目数量。在`data`数组中，每个对象包含一个`group`，描述了评价数量的区间，以及一个`metrics`数组，记录了该区间内的统计指标及其值。

#### 日期时间分组

以特定的日期/时间时长桶来分组`Restaurants`，通过`dateOfOpening`。

参数：

* 字段 `DateProperty | TimestampProperty`：要使用的属性名称（例如 `dateOfOpening`）。
* 值 `integer`（非必填）：用于分组的时长单位数量。

时长类型：

* 秒 `bySeconds()`
* 分钟 `byMinutes()`
* 小时 `byHours()`
* 天 `byDays()`
* 周 `byWeeks()`
* 月 `byMonths()`
* 季度 `byQuarters()`
* 年 `byYears()`

示例查询：

```java
AggregationResponse groupedRestaurants = client.ontology()
       .objects()
       .Restaurant()
       // 按照餐馆的开业日期进行分组，每10天为一个组
       .groupBy(GroupBy.byDays(Restaurant.Property.dateOfOpening(), 10))
       // 统计每个组中的餐馆数量
       .count()
       // 计算分组结果
       .compute();
```

```json
{
    excludedItems: 0, // 排除的项目数为0
    data: [{
        group: {
            "dateOfOpening": {
                startValue: "2024-09-25" // 开始日期为2024年9月25日
            }
        },
        metrics: [
            {
                name: "count", // 度量名称为"count"
                value: 100 // 度量值为100
            }
        ]
    }]
}
```

## Ontology上的操作

Ontology中的操作类型指的是可以在数据模型中的对象上执行的预定义操作。这些操作可以创建、修改和删除Ontology中的对象。操作类型是基于Ontology生成的，可以在Java OSDK中用于对代码中的对象执行特定任务。

### 向`Restaurant`添加评论的参数 (`AddRestaurantReview`)

| 属性                 | API 名称          | 类型      |
|----------------------|-------------------|-----------|
| `Restaurant Id`      | `restaurantId`    | 字符串    |
| `Review Rating`      | `reviewRating`    | Integer   |
| `Review Summary`     | `reviewSummary`   | 字符串    |

#### 应用操作

要应用操作，请填写输入参数值。这将执行一个操作并返回响应是否有效。

参数：

* 参数 `Object`：参数ID到用于这些输入参数的值的映射。
  * `restaurantId` `string`
  * `reviewRating` `integer`
  * `reviewSummary` `string`
* 选项 `integer`（非必填）：用于分组的持续时间单位数量。

示例查询：

```java
AddReviewActionResponse response = client.ontology()
    .actions()
    .addReview()
    .apply(
        AddReviewActionRequest.builder()
            .restaurantId(restaurantId)  // 设置餐厅ID
            .reviewRating(5)  // 设置评论评分
            .reviewSummary("It was great!")  // 设置评论摘要
            .build(),
        ReturnEditsMode.ALL  // 设置返回模式
    );

response.getValidationResult().accept(new ActionValidationVisitor<Object>() {
    @Override
    public Object valid(ActionValidationResponse response) {
        System.out.println("Review added successfully " + response);  // 评论添加成功
        return null;
    }

    @Override
    public Object invalid(ActionValidationResponse response) {
        System.out.println("Review validation failed! " + response);  // 评论验证失败
        return null;
    }
});
```

```json
{
    "validation": {
        "result": "VALID",  // 验证结果为有效
        "submissionCriteria": [],  // 提交标准（此处为空）
        "parameters": {
            "restaurantId": {
                "result": "VALID",  // 餐厅ID验证结果为有效
                "evaluatedConstraints": [],  // 评估的约束（此处为空）
                "required": true  // 餐厅ID是必填项
            },
            "reviewRating": {
                "result": "VALID",  // 评分验证结果为有效
                "evaluatedConstraints": [],  // 评估的约束（此处为空）
                "required": true  // 评分是必填项
            },
            "reviewSummary": {
                "result": "VALID",  // 评价摘要验证结果为有效
                "evaluatedConstraints": [],  // 评估的约束（此处为空）
                "required": true  // 评价摘要是必填项
            }
        }
    },
    "edits": {
        "type": "edits",  // 编辑类型
        "edits": [
            {
                "type": "modifyObject",  // 修改对象
                "primaryKey": "restaurantId1",  // 主键为restaurantId1
                "objectType": "Restaurant"  // 对象类型为餐厅
            }
        ],
        "addedObjectCount": 0,  // 添加的对象数量为0
        "modifiedObjectsCount": 1,  // 修改的对象数量为1
        "deletedObjectsCount": 0,  // 删除的对象数量为0
        "addedLinksCount": 0,  // 添加的链接数量为0
        "deletedLinksCount": 0  // 删除的链接数量为0
    }
}
```

#### 应用批量操作

要应用一批操作，请填写输入参数值。这将执行一系列操作，并返回响应是否有效或无效。请注意，这不返回验证，仅返回编辑。

参数：

* parameters `Object`: 参数ID与这些输入参数所使用的值的映射。
  * `restaurantId` `字符串`
  * `reviewRating` `integer`
  * `reviewSummary` `字符串`
* value `ReturnEditsMode.(ALL|NONE)` （非必填）: 应用操作后，编辑是否在响应中返回。

示例查询：

```java
AddReviewBatchActionResponse response = client.ontology()
    .actions()
    .addReview()
    .applyBatch(
        List.of(
            AddReviewActionRequest.builder()
                .restaurantId("restaurantId1") // 设置餐厅ID为restaurantId1
                .reviewRating(5) // 设置评价为5星
                .reviewSummary("It was great!") // 设置评价摘要
                .build(),
            AddReviewActionRequest.builder()
                .restaurantId("restaurantId2") // 设置餐厅ID为restaurantId2
                .reviewRating(4) // 设置评价为4星
                .reviewSummary("Good food but service can improve.") // 设置评价摘要
                .build()
        ),
        ReturnEditsMode.ALL // 设置返回编辑模式为ALL
    );


responseAction.getActionEdits().get().accept(new ActionEditsVisitor<Void>() {
        @Override
        public Void objectEdits(ObjectEdits response) {
            System.out.println("Edited Objects " + response); // 输出已编辑的对象信息
            return null;
        }

        @Override
        public Void largeScaleObjectEdits(ObjectTypeEdits response) {
            System.out.println("Edited ObjectTypes: " + response); // 输出已编辑的对象类型信息
            return null;
        }
    });
```

示例响应：

```json
{
    "edits": {
        "type": "edits",
        "edits": [
            {
                "type": "modifyObject",
                "primaryKey": "restaurantId1",
                "objectType": "Restaurant"
            },
            {
                "type": "modifyObject",
                "primaryKey": "restaurantId2",
                "objectType": "Restaurant"
            }
        ],
        "addedObjectCount": 0, // 添加的对象数量为0
        "modifiedObjectsCount": 2, // 修改的对象数量为2
        "deletedObjectsCount": 0, // 删除的对象数量为0
        "addedLinksCount": 0, // 添加的链接数量为0
        "deletedLinksCount": 0 // 删除的链接数量为0
    }
}
```

该代码段表示了一次编辑操作，其中对两个餐厅对象进行了修改，分别通过其主键 `restaurantId1` 和 `restaurantId2` 确定。这次编辑操作没有添加或删除任何对象或链接。

## 函数

在Palantir平台中，[函数](/docs/foundry/functions/overview/)（有时称为“对象上的函数”或FoO）是一个强大的功能，旨在增强数据建模和操作。函数提供了一种在存储于Ontology中的数据上定义和执行自定义逻辑的方法，允许用户创建更复杂的数据变换、验证和分析。

在Java SDK中，用户可以通过生成的查询执行Foundry函数。

通过将您的函数添加到应用程序中，您可以生成调用FoO以执行逻辑并获得结果的查询。

在这个例子中，我们有一个函数`findSimilarRestaurants`，它接受一个ID并返回一个包含所有相似`Restaurants`的ObjectSet。

### 执行函数以查找相似`Restaurants`(`findSimilarRestaurants`)的参数

| 属性           | API 名称        | 类型    |
|---------------|--------------|--------|
| `Restaurant Id` | `restaurantId` | 字符串 |

返回：`RestaurantObjectSet`

#### 应用函数

要应用一个函数，您必须访问并执行一个查询。这可以通过访问`.queries()`并通过`.execute(...).getReturnValue()`执行逻辑函数来完成。

查询示例：

```java
RestaurantObjectSet response = client
    .ontology() // 获取ontology对象
    .queries() // 访问查询功能
    .findSimilarRestaurants() // 查找相似餐馆的方法
    .execute("restaurantId") // 执行查询，传入餐馆ID
    .getReturnValue(); // 获取返回值
```
