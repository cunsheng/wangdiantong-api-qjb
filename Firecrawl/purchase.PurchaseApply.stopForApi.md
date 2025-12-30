---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.stopForApi"
title: "API文档"
---
**purchase.PurchaseApply.stopForApi（采购申请单停止引用）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述：** 停止引用部分引用状态的采购申请单 |
| **1.2 适用版本：** 客户端 V1.4.8.1及以上版本 |
| **1.3注意事项：** |

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
| 秒级时间戳 | timestamp | int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购申请单号 | applyList | List<String> |  | y | 采购申请单号 |

4.响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误数量 | total | Int |  | 是 | 错误数量 |
| 结果信息 | data | List<Map<String, Object>> |  | 是 | 错误采购申请单信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购申请单号 | order\_no | String |  |  | 采购申请单号 |
| 错误信息 | error | String |  |  | 错误信息 |
| 错误码 | error\_code | Int |  |  | 错误码 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```[`<br>```"POA2309130001"``,``"POA2309040001"`<br>```]`<br>`]` | |
| PHP |  |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: []`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"total"``: 2,`<br>```"data"``: [`<br>```{`<br>```"order_id"``: 764,`<br>```"order_no"``:``"POA2309040001"``,`<br>```"error"``:``"采购申请单状态不是部分引用"``,`<br>```"error_code"``: 0`<br>```},`<br>```{`<br>```"order_id"``: 767,`<br>```"order_no"``:``"POA2309130001"``,`<br>```"error"``:``"采购申请单状态不是部分引用"``,`<br>```"error_code"``: 0`<br>```}`<br>```]`<br>`}` | |
