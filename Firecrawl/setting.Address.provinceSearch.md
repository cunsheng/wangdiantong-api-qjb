---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Address.provinceSearch"
title: "API文档"
---
**setting.Address.provinceSearch（地址查询-省** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：接口描述: 查询省份信息 |
| **1.2 适用版本：** 客户端 V1.5.2.0及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4注意事项：** |

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
| 开始时间 | start\_time | String | 40 | N | 最后修改时间 |
| 结束时间 | end\_time | String | 40 | N | 最后修改时间 |

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
| 国家id | country\_id | Int | 11 | Y | 国家id |
| 省id | province\_id | int |  | Y | 省id |
| 名称 | name | String |  | Y | 名称 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间，yyyy-MM-dd HH:mm:ss格式 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2024-02-01"``,`<br>```"start_time"``:``"2024-01-01"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params =``new``stdClass();`<br>`$params->start_time =``'2022-06-05 11:42:56'``;`<br>`$params->end_time =``'2022-07-19 11:42:56'``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$data = $client->pageCall(``"setting.Address.provinceSearch"``, $pager, $params);` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"detail_list"``: [`<br>```{`<br>```"country_id"``: 0,`<br>```"modified"``:``"2022-03-08 10:16:01"``,`<br>```"name"``:``"北京"``,`<br>```"province_id"``: 110000`<br>```},`<br>```{`<br>```"country_id"``: 0,`<br>```"modified"``:``"2022-03-08 10:16:01"``,`<br>```"name"``:``"天津"``,`<br>```"province_id"``: 120000`<br>```}`<br>```],`<br>```"total_count"``: 35`<br>```},`<br>```"status"``: 0`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"此方法仅支持分页查询"``,`<br>```"status"``: 100`<br>`}` | |
