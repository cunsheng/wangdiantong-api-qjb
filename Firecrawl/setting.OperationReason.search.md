---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.OperationReason.search"
title: "API文档"
---
**setting.OperationReason.search（退换原因查询** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：查询退换原因 |
| **1.2 适用版本：** 客户端 V1.4.9.3及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：**<br>- 不传起止时间则默认返回全部数据, 起止时间最大间隔30天<br>  <br>- 建议在第一次全量获取数据, 后续按照最后变更时间获取变更数据<br>  <br>- 通过其他接口获取到订单标签mask后, 与当前接口返回的所有数据进行make\_set操作即可获取完整的标签<br>  <br>  - 例如 mask= 37, 完整的订单标签数据中前7个分别为a, b, c, d, e, f, g 则mask对应的订单标签为a,c,g<br>    <br>  - mask 转换为2进制为 100101 , 反转后为101001. 结合前7个标签的顺序可得出订单标签为a,c,g |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式 [点击这里](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E6%B5%8B%E8%AF%95/%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83%E5%8F%82%E6%95%B0%E4%BF%A1) |
| 盐 | salt | String |  | 是 | 由旺店通分配appsecret，是由两部分构成, 冒号前面的部分是secret, 冒号后面的部分是salt. 例如一个appsecret是testsecret:testsalt, 那么secret为testsecret, salt为testsalt. |
| 接口名称 | method | String |  | 是 | 调用的接口名称 |
| 版本号 | v | String |  | 是 | 1.0 |
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | Int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数， 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | N | 最后修改时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | N | 最后修改时间, yyyy-MM-dd HH:mm:ss格式 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | <Map<String, Object>> |  | 是 | 返回信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | detail\_list | List<Map<String, Object>> |  | 是 | 数据节点 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换原因id | reason\_id | Int |  | Y | 退换原因id |
| 分类id | class\_id | Int |  | Y | 分类id |
| 是否内置 | is\_builtin | Int |  | Y | 是否内置 |
| 是否已停用 | is\_disabled | String |  | Y | 是否已停用 |
| 优先级 | priority | Int | 11 | Y | 优先级 |
| 名称 | title | String | 64 | Y | 名称 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间，yyyy-MM-dd HH:mm:ss格式 |
| 创建时间 | created | String |  | Y | 创建时间，yyyy-MM-dd HH:mm:ss格式 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.OperationReason.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.OperationReason.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.OperationReason.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.OperationReason.search#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2023-10-03 00:00:00"``,`<br>```"start_time"``:``"2023-10-01 00:00:00"`<br>```}`<br>`]` |

|     |     |
| --- | --- |
|  | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params =``new``stdClass();`<br>`$params->start_time =``'2022-06-05 11:42:56'``;`<br>`$params->end_time =``'2022-07-19 11:42:56'``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$data = $client->pageCall(``"setting.OperationReason.search"``, $pager, $params);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"detail_list"``: [`<br>```{`<br>```"class_id"``: 4,`<br>```"created"``:``"2018-07-17 14:31:25"``,`<br>```"is_builtin"``:``false``,`<br>```"is_disabled"``:``true``,`<br>```"modified"``:``"2020-06-22 16:19:40"``,`<br>```"priority"``: 4,`<br>```"reason_id"``: 4,`<br>```"title"``:``"破损"`<br>```},`<br>```{`<br>```"class_id"``: 4,`<br>```"created"``:``"2018-07-17 14:31:25"``,`<br>```"is_builtin"``:``false``,`<br>```"is_disabled"``:``false``,`<br>```"modified"``:``"2022-01-25 15:57:59"``,`<br>```"priority"``: 6,`<br>```"reason_id"``: 5,`<br>```"title"``:``"买错了"`<br>```}`<br>```],`<br>```"total_count"``: 502`<br>```},`<br>```"status"``: 0`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"未知错误"``,`<br>```"status"``: 100`<br>`}` | |
