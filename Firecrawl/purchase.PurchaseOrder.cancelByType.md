---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.cancelByType"
title: "API文档"
---
**purchase.PurchaseOrder.cancelByType** **（采购单取消新）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述：** 根据传入的类型进行采购单取消或停止等待，支持对推送委外仓的采购单进行取消 |
| **1.2 适用版本：** 客户端 V1.4.5.8及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

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

**3.3 业务请求参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务请求参数 | params | Map<String,Object> |  | 是 | 业务请求参数 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购单操作类型 | operate\_type | Int | 3 | 是 | 0：采购单取消<br>1：采购单停止等待<br>2：wms停止等待 |
| 采购单批量列表节点 | purchase\_no\_list | List<String> |  | 是 | 采购单号 |
| 采购单是否允许已审核的单子取消 | allow\_cancel\_checked\_order | Int | 1 | 否 | 0：待审核、已审核单据无法取消<br>1：待审核、已审核单据先进行反审核、反编辑再取消<br>默认0 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 响应正文 | data | Map<String, Object> |  | 是 | 响应正文 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | Int | 6 | 是 | 错误码，0标识成功其他表示失败 |
| 错误描述 | message | String |  | 是 | 错误描述 |
| 错误数量 | error\_count | Int |  | 是 | 错误数量 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"operate_type"``: 1,`<br>```"purchase_no_list"``: [`<br>```"CG2304260001"``,`<br>```"CG2212140008"``,`<br>```"CG2212140007"``,`<br>```"CG2212140006"``,`<br>```"CG2212140005"``,`<br>```"CG2212140004"``,`<br>```"CG2212140003"``,`<br>```"CG2212140002"`<br>```],`<br>```"allow_cancel_checked_order"``: 1`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params =``new``stdClass();`<br>`$params->operate_type =``1``;`<br>`$params->purchase_no_list = array(``"CG2304260001"``,``"CG2212140003"``,``"CG2212140007"``);`<br>`$params->allow_cancel_checked_order =``0``;`<br>``<br>`$data = $client->call(``"purchase.PurchaseOrder.cancelByType"``, $params);`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"code"``: 0,`<br>```"message"``:``""``,`<br>```"error_count"``: 0`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"code"``: 1,`<br>```"message"``:``"[{\"error\":\"采购单编号:CG2212140009,采购单非部分入库状态\"},{\"error\":\"采购单编号:CG2212140008,采购单非部分入库状态\"},{\"error\":\"采购单编号:CG2212140007,采购单非部分入库状态\"},{\"error\":\"采购单编号:CG2212140006,采购单非部分入库状态\"},{\"error\":\"采购单编号:CG2212140005,采购单非部分入库状态\"},{\"error\":\"采购单编号:CG2212140004,采购单非部分入库状态\"},{\"error\":\"采购单编号:CG2212140003,采购单非部分入库状态\"},{\"error\":\"采购单编号:CG2212140002,采购单非部分入库状态\"}]"``,`<br>```"error_count"``: 8`<br>```}`<br>`}` | |
