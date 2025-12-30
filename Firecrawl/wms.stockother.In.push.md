---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push"
title: "API文档"
---
****wms.stockother.In.push**（其它入库业务单创建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述：** 其它入库业务单创建 |
| **1.2 适用版本：** 客户端 V1.5.4.3及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：仓库权限** |

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
| 单据数据 | order | Map<String, Object> |  | 是 | 单据数据 |
| 单据明细 | order\_details | List<Map<String, Object>> |  | 是 | 单据明细 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 物流公司编号 | logistics\_code | String | 60 | 否 | ERP系统内自行维护的物流公司的编号 |
| 入库原因 | reason | String | 255 | 否 | 入库原因 |
| 标记名称 | flag\_name | String | 32 | 否 | 标记名称 |
| 物流单号 | logistics\_no | String | 40 | 否 | 物流单号 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 其它入库业务单属性1 | prop1 | String | 255 | 否 | 其他入库业务单属性1 |
| 其它入库业务单属性2 | prop2 | String | 255 | 否 | 其他入库业务单属性2 |
| 其它入库业务单属性3 | prop3 | String | 255 | 否 | 其他入库业务单属性3 |
| 其它入库业务单属性4 | prop4 | String | 255 | 否 | 其他入库业务单属性4 |
| 其它入库业务单属性5 | prop5 | String | 255 | 否 | 其他入库业务单属性5 |
| 其它入库业务单属性6 | prop6 | String | 255 | 否 | 其他入库业务单属性6 |
| 外部单号 | outer\_no | String | 40 | 否 | 传入外部单号则使用外部单号作为系统内业务单号 |
| 是否审核 | is\_check | boolean | 1 | 否 | 审核传入true,不传默认false,<br>传入false则创建的业务单为待审核状态 |

**order\_details**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 数量 | num | Int | 11 | 是 | 数量 |
| 货位 | position\_no | String | 20 | 否 | 货位 |
| 批次 | batch\_no | String | 40 | 否 | 批次，支持传入并创建ERP内不存在的批次信息 |
| 有效期 | expire\_date | String | 40 | 否 | 有效期 |
| 生产日期 | production\_date | String |  | 否 | 生产日期<br>yyyy-MM-dd<br>例： 2024-09-01 |
| 是否残次品 | defect | boolean | 1 | 否 | 默认false |
| 辅助单位 | aux\_unit\_name | String |  | 否 | 基本单位取值：优先取单品，单品无则取货品基本单位，辅助单位需要和基本单位有匹配关系 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 入库价 | price | Decimal(19,4) |  | 否 | 入库价 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | 是 | 结果信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 0：表示操作全部成功<br>20：审核失败 |
| 返回信息 | message | String |  | 是 | status = 0时,返回创建成功的单号;否则返回错误信息 |
| 单号 | outer\_no | String |  | 否 | 单据是在旺店通系统上创建成功，仅下发wms失败时返回业务单号 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"outer_no"``:``"stockother_out02"``,`<br>```"warehouse_no"``:``"1002"``,`<br>```"remark"``:``"API TEST"``,`<br>```"is_check"``:``true`<br>```},`<br>```[`<br>```{`<br>```"spec_no"``:``"PC_2018"``,`<br>```"num"``:``"200.0000"``,`<br>```"defect"``:``false``,`<br>```"batch_no"``:``"11111"``,`<br>```"expire_date"``:``"2020-07- 01 00:00:00"`<br>`}]]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$order =``new``stdClass();`<br>`$order->outer_no =``"stockother_in03"``;`<br>`$order->warehouse_no =``"1002"``;`<br>`$order->defect =``1``;`<br>`$order->remark =``"API TEST"``;`<br>`$order->is_check =``true``;`<br>``<br>`$specList = array();`<br>`$spec =``new``stdClass();`<br>`$spec->spec_no =``"PC_2018"``;`<br>`$spec->remark =``"PD TEST"``;`<br>`$spec->num =``"200.0000"``;`<br>`$spec->defect =``false``;`<br>`$spec->batch_no =``'11111'``;`<br>`$spec->expire_date =``'2020-07-01 00:00:00'``;`<br>`//$spec->position_no = 'xcx';`<br>``<br>`array_push($specList, $spec);`<br>``<br>`// 审核失败的message, 前缀为check_fail`<br>`$data = $client->call(``"wms.stockother.In.push"``, $order, $specList);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"message"``:``"QR202206240004"``,`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2 异常响应示例

1）单据推送成功，系统处理异常

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"outer_no"``:``"XXXXXXXXX"``,`<br>```"message"``:``"check_fail 审核成功, 推送WMS失败： 旺店通WMS返回：Db Error: Unknown column 'is_gift' in 'field list'"``,`<br>```"status"``: 20`<br>```}`<br>`}` |

2）单据推送失败

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.In.push#autoTab2_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``:   100,`<br>```"message"``:``"外部单号重复!"`<br>`}` |
