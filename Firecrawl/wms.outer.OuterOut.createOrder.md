---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.createOrder"
title: "API文档"
---
****wms.outer.OuterOut.createOrder**（外仓调整出库单创建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述：** 外仓调整出库单创建 |
| **1.2 适用版本：** 客户端 V1.5.7.0及以上版本 |
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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | Map<String, Object> |  | 是 | 单据数据 |
| 单据明细 | order\_details | List<Map<String, Object>> |  | 是 | 单据明细 |
| 是否审核 | is\_check | boolean |  | 是 | 审核：true<br>不审核：false |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 外部单号 | order\_no | String | 40 | 否 | 传入外部单号则使用外部单号作为系统内业务单号 |
| 源单类型 | src\_order\_type | Int | 4 | 否 | 0:调整出库，2:调拨出库，14:采购退货出库 |
| 源单号 | src\_order\_no | String | 40 | 否 | 源单类型为2和14需传源单号 |
| 出库原因 | reason | String | 64 | 否 | 出库原因 |

**order\_details**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 数量 | num | Int | 11 | 是 | 数量 |
| 辅助单位 | aux\_unit\_name | String | 20 | 否 | 辅助单位 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 是否残次品 | defect | boolean | 1 | 否 | 默认false |
| 批次编号 | batch\_no | String | 50 | 否 | 批次编号若不在会自动创建 |
| 有效期 | expire\_date | String |  | 否 | 有效期 |
| 是否开启序列号 | is\_enable\_sn | Int |  | 否 | 0：不开启<br>1：开启<br>默认不开启 |
| 序列号列表 | sn\_list | String |  | 否 | 序列号列表，多个序列号用","分隔，<br>例如："xxx1,xxx2,xxx3"，开启序列号后序列号数量要与出库数量保持一致 |

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

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.createOrder#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.createOrder#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.createOrder#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.createOrder#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"warehouse_no"``:``"pos"``},[{``"spec_no"``:``"DFAQT101"``,``"num"``:2}],``false``]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$order =``new``stdClass();`<br>`$order->warehouse_no =``'pos'``;`<br>``<br>`$detail =``new``stdClass();`<br>`$detail->spec_no =``'DFAQT101'``;`<br>`$detail->num =``2``;`<br>`$details = array($detail);`<br>``<br>`try``{`<br>```$response = $client->call(``"wms.outer.OuterOut.createOrder"``, $order, $details,``false``);`<br>```echo json_encode($response);`<br>`}``catch``(exception $e)`<br>`{`<br>```echo``"exception info:"``.$e->getMessage();`<br>`}` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.createOrder#autoTab0_0)

|     |     |
| --- | --- |
| 1 | `[{``"warehouse_no"``:``"pos"``},[{``"spec_no"``:``"DFAQT101"``,``"num"``:2}],``false``]` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.createOrder#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"code"``:``"right.required"``,``"message"``:``"无该仓库权限"``}` |
