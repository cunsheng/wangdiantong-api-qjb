---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.createOrder"
title: "API文档"
---
****purchase.PurchaseReturn.createOrder**（采购退货单新建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述：** 推送采购退货单据给ERP |
| **1.2 适用版本：** 客户端V1.6.0.10及以上版本 |

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
| 采购退货单单据信息 | orderInfo | Map<String, Object> |  | 是 | 采购退货单单据信息 |
| 采购退货单明细信息 | detailList | List<Map<String,Object>> |  | 是 | 采购退货单明细信息 |
| 是否审核 | is\_check | boolean |  | 是 | 是否审核 |

**orderInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 外部单号 | outer\_no | String | 20 | 是 | 外部单号（创建成功后作为系统退货单号） |
| 仓库编码 | warehouse\_no | String | 40 | 是 | 仓库编码 |
| 供应商编号 | provider\_no | String | 20 | 是 | 供应商编号 |
| 物流公司编号 | logistics\_no | String |  | 否 | ERP内维护的采购业务类型的物流公司编号 |
| 邮费 | post\_fee | Decimal(19,4) |  | 否 | 邮费 |
| 其他费用 | other\_fee | Decimal(19,4) |  | 否 | 其他费用 |
| 联系人 | contact | String | 40 | 否 | 联系人（若未传该参数，使用供应商默认的联系人） |
| 联系电话 | telno | String | 32 | 否 | 联系电话（若未传该参数，使用供应商默认的电话） |
| 收件地址 | receive\_address | String | 255 | 否 | 收件地址<br>（当省份、城市、区域、地址字段皆为空时，默认使用供应商的省市区及地址信息） |
| 省 | receive\_province | String |  | 否 | 省编码，可以查看 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb)，<br>（当省份、城市、区域、地址字段皆为空时，默认使用供应商的省市区及地址信息） |
| 市 | receive\_city | String |  | 否 | 市编码，可以查看 [城市代码](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) [表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb)<br>（当省份、城市、区域、地址字段皆为空时，默认使用供应商的省市区及地址信息） |
| 区 | receive\_district | String |  | 否 | 区编码，可以查看 [城市代码](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) [表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb)<br>（当省份、城市、区域、地址字段皆为空时，默认使用供应商的省市区及地址信息） |
| 自定义属性1 | prop1 | String | 255 | 否 | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | 否 | 自定义属性2 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 引用的采购单号 | ref\_purchase\_nos | String\[\] |  | 否 | 引用的采购单号，采购单状态要大于已审核 |
| 审核失败是否取消单据 | check\_fail\_cancel | Int |  | 否 | 0：不取消<br>1：审核失败后取消<br>默认0 |

**detailList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 退货数量 | num | Decimal(19,4) |  | 是 | 退货数量 |
| 折扣 | discount | Decimal(19,4) |  | 否 | 折扣字段，默认值为1，1代表原价，无折扣；假设需要折扣为一折时，可将字段值传为0.1，同理，折扣为5折时，传值0.5；折扣为八折时，传值0.8，以此类推 |
| 税率 | tax\_rate | Decimal(19,4) |  | 否 | 税率，不传默认值0 |
| 单价 | price | Decimal(19,4) |  | 否 | 单价，不传为默认值0 |
| 基本单位 | unit\_name | String | 40 | 否 | 退货单位（辅助单位） |
| 是否残次品 | defect | boolean | 1 | 否 | 是否残次品<br>true:残次品<br>false:正品 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 批次号 | batch\_no | String | 40 | 否 | 批次号 |
| 有效期 | expire\_date | String | 40 | 否 | 有效期：样例:2020-04-20 00:00:00 |
| 税后金额 | tax\_price | Decimal(19,4) |  | 否 | 税后金额 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | 是 | 结果信息 |
| **data** |  |  |  |  |  |
| 返回信息 | message | String |  | 是 | 如果创建/修改成功message内容为OK,否则为错误信息 |
| 状态码 | status | Int |  | 是 | 0：操作全部成功<br>20：审核失败 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.createOrder#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.createOrder#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.createOrder#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.createOrder#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"outer_no"``:``"20230112002CGTK"``,`<br>```"ref_purchase_nos"``: [``"RH23011110"``,``"RH22122901"``],`<br>```"provider_no"``:``"LJTest"`<br>```},`<br>```[{`<br>```"defect"``:``true``,`<br>```"price"``: 10,`<br>```"num"``: 3,`<br>```"spec_no"``:``"xiaowanzi"`<br>```}],``true`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$paraMap =``new``stdClass();`<br>`$paraMap->provider_no =``"1001"``;`<br>`$paraMap->warehouse_no =``"1001"``;`<br>``<br>`$detail =``new``stdClass();`<br>`$detail->spec_no =``"daba1"``;`<br>`$detail->num =``"1"``;`<br>``<br>`$response = $client->call(``"purchase.PurchaseReturn.createOrder"``, $paraMap, [$detail],``false``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.createOrder#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"message"``:``"RH8723238"``,`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.createOrder#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"仓库不存在"`<br>`}` |
