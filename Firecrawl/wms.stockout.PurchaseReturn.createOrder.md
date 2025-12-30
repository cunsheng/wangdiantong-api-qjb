---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.createOrder"
title: "API文档"
---
****wms.stockout.PurchaseReturn.createOrder**（采购退货出库单新建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述：** 推送采购退货出库单据给ERP |
| **1.2 适用版本：** 客户端V1.4.0.4及以上版本 |

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
| 采购退货出库单据信息 | orderInfo | Map<String, Object> |  | 是 | 采购退货出库单据信息 |
| 采购退货出库单明细信息 | detailList | List<Map<String,Object>> |  | 是 | 采购退货出库单明细信息 |

**orderInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购退货单号 | return\_no | String | 40 | 是 | 采购退货单号 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 物流编码 | logistics\_code | String | 60 | 否 | 系统物流编码 |
| 创建模式 | create\_mode | Int |  | 否 | 默认：编辑中/未确认<br>1：已提交/待审核<br>2：已审核 |
| 备注 | remark | String | 255 | 否 | 备注 |

**detailList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单品信息 | spec\_no | String | 40 | 是 | 单品信息 |
| 出库数量 | num | Decimal(19,4) |  | 是 | 出库数量 |
| 采购单位 | unit\_name | String | 40 | 否 | 采购单位 |
| 货位编号 | position\_no | String | 50 | 否 | 货位编号 |
| 批次号 | batch\_no | String | 50 | 否 | 批次号 |
| 有效期 | expire\_date | String | 50 | 否 | 有效期 |
| 是否残次品 | defect | boolean | 1 | 否 | 是否残次品<br>true:残次品<br>false:正品 |
| 备注 | remark | String | 255 | 否 | 备注 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | 是 | 结果信息 |
| **data** |  |  |  |  |  |
| 返回信息 | message | String |  | 是 | 如果创建成功message内容为单号,否则为错误信息 |
| 状态码 | status | Int |  | 是 | 0表示成功推送 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.createOrder#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.createOrder#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.createOrder#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.createOrder#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"return_no"``:``"1001"``,`<br>```"warehouse_no"``:``"1001"``,`<br>```"create_mode"``: 0`<br>```},`<br>```[{`<br>```"spec_no"``:``"daba1"``,`<br>```"num"``:``"1"`<br>```}]`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$paraMap =``new``stdClass();`<br>`$paraMap->return_no =``"CR202204140001"``;`<br>`$paraMap->warehouse_no =``"1001"``;`<br>`$paraMap->logistics_code =``"123"``;`<br>`$paraMap->create_mode=``0``;`<br>``<br>`$detail =``new``stdClass();`<br>`$detail->spec_no =``"daba1"``;`<br>`$detail->num =``"1"``;`<br>``<br>`$response = $client->call(``"wms.stockout.PurchaseReturn.createOrder"``, $paraMap, [$detail]);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.createOrder#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"message"``:``"CH20220414136"``,`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.createOrder#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"仓库编号为 wdtapi3-test11 的仓库不存在!"`<br>`}` |
