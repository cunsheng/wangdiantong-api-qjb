---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Barcode.upload"
title: "API文档"
---
**goods.Barcode.upload（条码** **上传）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 新建或更新条码 |
| **1.2 适用版本：** 客户端 V1.4.6.6及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

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
| 业务请求参数 | barcodeInfoList | List<Map<String,Object>> |  | 是 | 业务请求参数 |

**barcodeInfoList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | merchant\_no | String | 40 | 是 | 单品/组合装商家编码 |
| 条码 | barcode | String | 50 | 否 | 条码 |
| 操作类型 | type | Int |  | 否 | 1：新增<br>2：更新<br>默认1 |
| 数量 | num | Int |  | 否 | 默认1 |
| 原条码 | old\_barcode | String | 50 | 否 | 原条码，仅更新操作有效 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | Map<String,Object> |  | 否 | 返回信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 异常信息 | error\_list | List<Map<String,Object>> |  | 是 | 操作全部成功时列表为空 |

**error\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 商家编码 | merchant\_no | String | 40 | 是 | 商家编码 |
| 异常信息 | message | String |  | 是 | 异常信息 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```[`<br>```{`<br>```"barcode"``:``"TEST001"``,`<br>```"merchant_no"``:``"TEST"``,`<br>```"num"``: 1,`<br>```"type"``: 1`<br>```},`<br>```{`<br>```"barcode"``:``"TEST002"``,`<br>```"merchant_no"``:``"TEST"``,`<br>```"num"``: 1,`<br>```"type"``: 2`<br>```}`<br>```]`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client = new WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$barcode_list = array();`<br>`$barcode1 = new stdClass();`<br>`$barcode1->type = 1;`<br>`$barcode1->merchant_no =``'TEST'``;`<br>`$barcode1->barcode =``'TEST0011'``;`<br>`$barcode1->num = 1;`<br>`//$barcode1->old_barcode = 1;`<br>`$barcode_list[] = $barcode1;`<br>`$data = $client->call(``"goods.Barcode.upload"``, $barcode_list);`<br>``<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"error_list"``: [`<br>```{`<br>```"barcode"``:``"TEST001"``,`<br>```"merchant_no"``:``"TEST"``,`<br>```"message"``:``"条码重复"`<br>```},`<br>```{`<br>```"barcode"``:``"TEST002"``,`<br>```"merchant_no"``:``"TEST"``,`<br>```"message"``:``"条码重复"`<br>```}`<br>```]`<br>```},`<br>```"status"``: 0`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"包含重复数据"``,`<br>```"status"``: 100`<br>`}` | |
