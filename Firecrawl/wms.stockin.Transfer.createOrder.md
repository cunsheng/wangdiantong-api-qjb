---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.createOrder"
title: "API文档"
---
**wms.stockin.Transfer.createOrder** **（调拨入库单新建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送调拨入库单据给ERP |
| **1.2 适用版本：** 客户端 V1.5.7.0及以上版本 |
| **1.3注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | Y | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | Y | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式 [点击这里](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E6%B5%8B%E8%AF%95/%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83%E5%8F%82%E6%95%B0%E4%BF%A1) |
| 盐 | salt | String |  | Y | 由旺店通分配appsecret，是由两部分构成, 冒号前面的部分是secret, 冒号后面的部分是salt. 例如一个appsecret是testsecret:testsalt, 那么secret为testsecret, salt为testsalt. |
| 接口名称 | method | String |  | Y | 调用的接口名称 |
| 版本号 | v | String |  | Y | 1.0 |
| 秒级时间戳 | timestamp | int |  | Y | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | Y | 签名 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调拨入库单单据信息 | orderInfo | Map<String, Object> |  | Y | 调拨入库单单据信息 |
| 调拨入库单明细信息 | detailList | List<Map<String, Object>> |  | Y | 调拨入库单明细信息 |
| 是否审核 | is\_check | boolean |  | N | 是否审核（低优先级）V1.4.9.1版本以上非必传 |

**orderInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 源调拨单号 | src\_order\_no | String | 40 | Y | 源调拨单号 |
| 调入仓库编码 | warehouse\_no | String | 40 | Y | 调入仓库编码 |
| 物流编号 | logistics\_code | String | 60 | N | 物流编号（系统物流编号） |
| 备注 | remark | String |  | N | 备注 |
| 创建后的单据状态 | is\_check | Int |  | N | 0：待审核<br>1：已审核<br>2：编辑中<br>默认0 |
| 是否创建批次 | is\_create\_batch | boolean |  | N | true：创建<br>false：不创建<br>默认不创建 |

****detailList****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单品信息 | spec\_no | String | 40 | Y | 单品信息 |
| 调拨数量 | num | Decimal(19,4) |  | Y | 调拨数量 |
| 基本单位 | unit\_name | String | 40 | N | 基本单位，不传默认为调拨单明细对应货品的基本单位 |
| 调入货位 | position\_no | String | 20 | N | 调入货位，不传默认取调拨单中设置的入库货位，如果有多个相同货品随机取一条明细填充信息 |
| 批次号 | batch\_no | String | 40 | N | 批次号，不传默认取调拨单中设置的批次号，如果有多个相同货品随机取一条明细填充信息 |
| 有效期 | expire\_date | String | 40 | N | 有效期，不传默认取调拨单中设置的有效期，如果有多个相同货品随机取一条明细填充信息 |
| 残次品 | defect | Bool |  | N | true：残次品<br>false：正品 |
| 备注 | remark | String | 40 | N | 备注 |
| 是否开启序列号 | is\_enable\_sn | Int |  | N | 0：不开启<br>1：开启<br>默认不开启 |
| 序列号列表 | sn\_list | String |  | N | 序列号列表，多个序列号用","分隔，<br>例如："xxx1,xxx2,xxx3"，开启序列号后序列号数量要与出库数量保持一致 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | Status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 结果信息 | data | Map<String, String> |  | Y | 结果信息 |

****data****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回信息 | message | String |  | Y | 如果创建/修改成功message内容为单号,否则为错误信息 |
| 状态码 | status | Int |  | Y | 0：操作全部成功<br>20：审核失败 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.createOrder#autoTab3_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.createOrder#autoTab3_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.createOrder#autoTab3_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.createOrder#autoTab3_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"src_order_no"``:``"TF202003020004"``,`<br>`"warehouse_no"``:``"jziyy"``,`<br>`"remark"``:``"test"`<br>`},`<br>`[{`<br>`"spec_no"``:``"lz41"``,`<br>`"num"``: 1,`<br>`"unit_name"``:``"lz1"``,`<br>`"remark"``:``"test"``,`<br>`"position_no"``:``"b01"`<br>`}],`<br>`false`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$transferInOrder``=``new``stdClass();`<br>`$transferInOrder``->src_order_no=``'TF202003020004'``;`<br>`$transferInOrder``->warehouse_no=``'jziyy'``;`<br>`//$transferInOrder->logisctics_code='';`<br>`$transferInOrder``->remark=``'test'``;`<br>``<br>`$transferInOrderList``=``array``();`<br>`$transferInOrderDetail1``=``new``stdClass();`<br>`$transferInOrderDetail1``->spec_no=``'lz41'``;`<br>`$transferInOrderDetail1``->num=1;`<br>`$transferInOrderDetail1``->unit_name=``'lz1'``;`<br>`$transferInOrderDetail1``->remark=``'test'``;`<br>`$transferInOrderDetail1``->position_no=``'b01'``;`<br>``<br>`array_push``(``$transferInOrderList``,``$transferInOrderDetail1``);`<br>``<br>`$data``=``$client``->call(``"wms.stockin.Transfer.createOrder"``,``$transferInOrder``,``$transferInOrderList``,true);`<br>`?>` |

**6.响应示例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.createOrder#autoTab3_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"message"``:``"RK202211239"``,`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.createOrder#autoTab4_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"商家编码不存在"`<br>`}` |
