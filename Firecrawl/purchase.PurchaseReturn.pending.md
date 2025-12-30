---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.pending"
title: "API文档"
---
****purchase.PurchaseReturn.pending**（采购退货单停止等待）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述：** 采购退货单停止等待 |
| **1.2 适用版本：** 客户端 V1.2.5.6及以上版本 |
| **1.5注意事项：**一次请求退货单数量不可大于500 |

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
| 采购退货单号 | purchaseReturnNos | List<String> |  | 是 | 采购退货单号 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | 是 | 采购退货单相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误信息 | error\_info | List<Map<String, Object>> |  | 是 | 错误信息，如果没有错误信息返回空List |
| 状态 | status | Int | 11 | 是 | 0表示正常 |

**error\_info**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购退货单号 | order\_no | String |  | 是 | 采购退货单号 |
| 错误信息 | message | String |  | 是 | 错误信息 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.pending#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.pending#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.pending#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.pending#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[[``"xxx"``,``"CR202006290001"``,``"CR202006230007"``,``"CR202006190001"``]]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$purchaseNos = array();`<br>`array_push($purchaseNos,``'xxx'``,``'CR202006290001'``,``'CR202006230007'``,``'CR202006190001'``);`<br>``<br>`$data = $client->call(``"purchase.PurchaseReturn.pending"``, $purchaseNos);` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.pending#autoTab0_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:0,``"data"``:{``"error_info"``:[],``"status"``:0}}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.pending#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``:0,`<br>```"data"``:{`<br>```"error_info"``:[`<br>```{`<br>```"order_no"``:``"xxxxxxx"``,`<br>```"message"``:``"采购退货单号不存在"`<br>```},`<br>```{`<br>```"order_no"``:``"lskdjlkjklj"``,`<br>```"message"``:``"采购退货单号不存在"`<br>```}],`<br>```"status"``:0`<br>```}`<br>`}` |
