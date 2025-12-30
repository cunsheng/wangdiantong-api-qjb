---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.queryWithDetail"
title: "API文档"
---
**wms.stockout.PurchaseReturn.queryWithDetail** **（采购退货出库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP采购退货出库单信息 |
| **1.2 适用版本：** 客户端 V1.5.5.2及以上版本 |
| **1.3 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.4 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** 财务系统、SAP、线下ERP、数据分析等系统的对接 |

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
| 分页大小 | page\_size | int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | N | 开始时间，若无出库单号或采购退货单号，则为必填。 |
| 结束时间 | end\_time | String | 40 | N | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int | 40 | N | 时间类型<br>1：出库时间<br>2：创建时间<br>3：最后修改时间<br>默认1 |
| 仓库编号 | warehouse\_no | String | 40 | N | 限普通仓库 |
| 出库单号 | stockout\_no | String | 40 | N | 出库单号 |
| 采购退货单号 | src\_order\_no | String | 40 | N | 采购退货单号 |
| 出库单状态 | status | String | 40 | N | 由逗号分隔的整数数组<br>出库单状态:  <br>5已取消 <br>48 未确认 <br>50 待审核<br>77 拣货中,PDA拣货后<br>110已完成 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 出库单信息 | data | Map<String, Object> |  | N | 出库信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 出库单相关数据 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单id | stockout\_id | Int | 11 | Y | 出库单id |
| 出库单号 | order\_no | String | 40 | Y | 出库单号 |
| 采购退货单号 | src\_order\_no | String | 40 | Y | 采购退货单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 发货时间 | consign\_time | String | 40 | Y | 发货时间（单据未出库该字段不返回） |
| 状态 | status | Byte |  | Y | 出库单状态<br>5: 已取消<br>48: 未确认<br>50: 待审核<br>65: 待处理<br>77: 拣货中<br>110: 已完成 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 邮费 | post\_fee | Decimal(19,4) |  | Y | 邮费 |
| 收件人姓名 | receiver\_name | String | 40 | Y | 收货人姓名 |
| 省份id | receiver\_province | String | 40 | Y | 省份，返回值可参考[城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 城市id | receiver\_city | String | 40 | Y | 城市，返回值可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地区id | receiver\_district | String | 40 | Y | 地区，返回值可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 收件人地址 | receiver\_address | String | 256 | Y | 收件人地址 |
| 收件人电话 | receiver\_telno | String | 40 | Y | 收件人电话 |
| 备注 | remark | String | 255 | Y | 备注 |
| 重量 | weight | Decimal(19,4) |  | Y | 重量 |
| 供应商编号 | provider\_no | String | 20 | Y | 供应商编号 |
| 供应商名称 | provider\_name | String | 64 | Y | 供应商名称 |
| 最后一次引用的采购单号 | last\_load\_purchase\_no | String | 20 | Y | 最后一次引用的采购单号 |
| 货品种类数 | goods\_type\_count | Int | 6 | Y | 货品种类数 |
| 制单时间 | create\_time | String |  | Y | 制单时间 |
| 制单人 | operator\_name | String |  | Y | 制单人姓名（接口创建或者是制单人为系统的返回空字符串） |
| 总成本价 | goods\_total\_cost | Decimal(19,4) |  | Y | 总成本价 |
| 总货款 | goods\_total\_amount | Decimal(19,4) |  | Y | 总货款（出库金额） |
| 瞬时成本总额 | checked\_goods\_total\_cost | Decimal(19,4) |  | Y | 瞬时成本总额 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间，<br>格式: yyyy-MM-dd HH:mm:ss |
| 采购退货单自定义属性1 | prop1 | String |  | Y | 采购退货单自定义属性1 |
| 采购退货单自定义属性2 | prop2 | String |  | Y | 采购退货单自定义属性2 |
| 出库单明细 | details\_list | List<Map<String, Object>> |  | Y | 出库单明细 |

**details\_list**

| 名称 | 字段 | 字段类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单明细id | rec\_id | Int | 11 | Y | 出库单明细ID（主键） |
| 出库单id | stockout\_id | Int | 11 | Y | 出库单ID |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 货品总额 | total\_amount | Decimal(19,4) |  | Y | 货品总额（税前折后单价\*数量） |
| 税前折后单价 | sell\_price | Decimal(19,4) |  | Y | 税前折后单价 |
| 备注 | remark | String | 255 | Y | 备注 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 成本价 | cost\_price | Decimal(19,4) |  | Y | 成本价 |
| 预估重量 | weight | Decimal(19,4) |  | Y | 预估重量 |
| 货品类型 | goods\_type | Int | 11 | Y | 货品类型 |
| 单位 | goods\_unit | String | 20 | Y | 单位 |
| 批次 | batch\_no | String | 40 | Y | 批次号 |
| 有效期 | expire\_date | String | 40 | Y | 如果没有则返回空字符串 |
| 残次品 | defect | boolean | 1 | Y | true：残次品<br>false：正品 |
| 货位 | position\_no | String | 20 | Y | 货位 |
| 总瞬时实际成本 | total\_checked\_cost\_price | Decimal(19,4) |  | Y | 总瞬时实际成本 |
| 自定义属性1 | prop1 | String | 255 | Y | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | Y | 自定义属性2 |
| 货位明细 | position\_details\_list | List<Map<String, Object>> |  | Y | 货位明细 |

**position\_details\_list**

| 名称 | 字段 | 字段类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货位明细主键 | rec\_id | Int | 11 | Y | 货位明细主键 |
| 出库单明细主键 | stockout\_detail\_id | Int | 11 | Y | 出库单明细主键 |
| 货位id | position\_id | Int | 11 | Y | 货位id |
| 货位 | position\_no | String | 20 | Y | 货位 |
| 有效期 | expire\_date | String |  | Y | 有效期 |
| 批次 | batch\_no | String | 40 | Y | 批次 |
| 当前货位出库总货品数量 | position\_goods\_count | Decimal(19,4) |  | Y | 当前货位出库货品总数量 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.queryWithDetail#autoTab5_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"start_time"``:``"2019-12-11 00:00:00"``,`<br>```"end_time"``:``"2019-12-31 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2019-12-11 00:00:00'``;`<br>`$params``->end_time =``'2019-12-31 00:00:00'``;`<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.PurchaseReturn.queryWithDetail"``,``$pager``,``$params``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.queryWithDetail#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"order_no"``:``"CH2023020752"``,`<br>```"details_list"``: [{`<br>```"rec_id"``: 2849136,`<br>```"stockout_id"``: 1635205,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"defect"``:``false``,`<br>```"goods_count"``: 1,`<br>```"total_amount"``: 1.11,`<br>```"sell_price"``: 1.11,`<br>```"remark"``:``""``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"brand_name"``:``"无"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_name"``:``"暂无"``,`<br>```"spec_code"``:``"LL "``,`<br>```"cost_price"``: 9.9424,`<br>```"weight"``: 0.2,`<br>```"goods_type"``: 1,`<br>```"goods_unit"``:``"箱"``,`<br>```"batch_no"``:``"PC202301050002"``,`<br>```"expire_date"``:``""``,`<br>```"position_no"``:``""``,`<br>```"total_checked_cost_price"``: 9.9424,`<br>```"position_details_list"``: [{`<br>```"rec_id"``: 126237,`<br>```"stockout_detail_id"``: 2849136,`<br>```"position_id"``: 85441,`<br>```"position_no"``:``"102"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"position_goods_count"``: 1`<br>```}],`<br>```"prop1"``:``""``,`<br>```"prop2"``:``""`<br>```}],`<br>```"consign_time"``: 1675751007000,`<br>```"post_fee"``: 0,`<br>```"receiver_city"``:``"0"``,`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"goods_count"``: 1,`<br>```"stockout_id"``: 1635205,`<br>```"src_order_no"``:``"CT2302070001"``,`<br>```"warehouse_no"``:``"234234234"``,`<br>```"receiver_telno"``:``"12345678901"``,`<br>```"checked_goods_total_cost"``: 9.9424,`<br>```"receiver_name"``:``"小K"``,`<br>```"modified"``:``"2023-02-07 14:23:27"``,`<br>```"provider_name"``:``"秋天001"``,`<br>```"provider_no"``:``"20170808002"``,`<br>```"seq_no"``: 1,`<br>```"create_time"``: 1675751003000,`<br>```"receiver_province"``:``"0"``,`<br>```"logistics_no"``:``""``,`<br>```"receiver_district"``:``"0"``,`<br>```"weight"``: 0,`<br>```"goods_total_amount"``: 1.11,`<br>```"operator_name"``:``"nff"``,`<br>```"goods_total_cost"``:``"9.94240000"``,`<br>```"last_load_purchase_no"``:``""``,`<br>```"receiver_address"``:``"北京海淀区花园路2号"``,`<br>```"status"``: 110`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.PurchaseReturn.queryWithDetail#autoTab6_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"参数中必须包含起止时间"`<br>`}` |
