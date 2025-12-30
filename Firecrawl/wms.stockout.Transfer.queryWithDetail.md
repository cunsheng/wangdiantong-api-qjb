---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Transfer.queryWithDetail"
title: "API文档"
---
**wms.stockout.Transfer.queryWithDetail** **（调拨出库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP调拨出库单信息 |
| **1.2 适用版本：** 客户端 V1.6.0.10及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**线下ERP、财务系统、数据分析等系统对接 |

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
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 按照发货时间返回，若无出库单号或调拨单号，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 按照发货时间返回，上同开始时间 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 调拨单号 | src\_order\_no | String | 40 | N | 调拨单号 |
| 出库单号 | stockout\_no | String | 40 | N | 出库单号 |
| 是否按照货位分组 | position | Int |  | N | 0:  否<br>不传也为否 |
| 出库单状态 | status | String | 40 | N | 由逗号隔开的整数字符串<br>出库单状态:  <br>5已取消 <br>48 未确认 <br>50 待审核<br>77 拣货中<br>110已完成 |

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
| 单据信息 | data | Map<String,Object> |  | N | 单据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 单据数据 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单id | stockout\_id | Int | 11 | Y | 出库单id |
| 出库单编号 | order\_no | String | 40 | Y | 出库单编号 |
| 调拨单号 | src\_order\_no | String | 40 | Y | 调拨单号 |
| 出库仓编号 | warehouse\_no | String | 40 | Y | 出库仓编号 |
| 出库时间 | consign\_time | String | 40 | Y | 出库时间 |
| 源单据类别 | order\_type | Int | 4 | Y | 源单据类别 <br>2调拨出库 |
| 出库单状态 | status | Int |  | Y | 出库单状态:  <br>5已取消 <br>48 未确认 <br>50 待审核<br>77 拣货中<br>110已完成 |
| 出库数量 | goods\_count | Decimal(19,4) |  | Y | 出库数量 |
| 邮费 | post\_fee | Decimal(19,4) |  | Y | 邮费 |
| 物流单编号 | logistics\_no | String | 40 | Y | 物流单编号 |
| 包装成本 | package\_fee | Decimal(19,4) |  | Y | 包装成本 |
| 收件人姓名 | receiver\_name | varchar | 40 | Y | 收件人姓名 |
| 国家id | receiver\_country | Int | 6 | Y | 国家id |
| 省id | receiver\_province | Int | 11 | Y | 省id |
| 城市id | receiver\_city | Int | 11 | Y | 城市id |
| 地区id | receiver\_district | Int | 11 | Y | 地区id |
| 收件地址 | receiver\_address | String | 256 | Y | 收件地址 |
| 收件人手机号 | receiver\_mobile | String | 40 | Y | 收件人手机号 |
| 收件人固话号 | receiver\_telno | String | 40 | Y | 收件人固话号 |
| 邮编 | receiver\_zip | String | 20 | Y | 邮编 |
| 出库单备注 | remark | String | 255 | Y | 出库单备注 |
| 重量 | weight | Decimal(19,4) |  | Y | 重量 |
| 调拨单创建时间 | st\_created | String | 40 | Y | 调拨单创建时间 |
| 调出仓库编号 | from\_warehouse\_no | String | 40 | Y | 调出仓库编号 |
| 调入仓库编号 | to\_warehouse\_no | String | 40 | Y | 调入仓库编号 |
| 制单人 | operator\_name | String | 40 | Y | 制单人 |
| 总成本 | goods\_total\_cost | Decimal(19,4) |  | Y | 总成本 |
| 调拨单id | transfer\_id | Int | 11 | Y | 调拨单id |
| 出库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 出库单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单详情id | rec\_id | Int | 11 | Y | 出库单详情id |
| 出库单id | stockout\_id | Int | 11 | Y | 出库单id |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 出库单详情备注 | remark | Sting | 255 | Y | 出库单详情备注 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编码 | goods\_no | String | 40 | Y | 货品编码 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 成本价 | cost\_price | Decimal(19,4) |  | Y | 成本价（存货成本） |
| 总成本 | total\_amount | Decimal(19,4) |  | Y | 总成本 |
| 总重量 | weight | Decimal(19,4) |  | Y | 总重量 |
| 货品类型 | goods\_type | Int | 4 | Y | 1销售商品 <br>2原材料 <br>3包装 <br>4周转材料<br>5虚拟商品<br>6固定资产 <br>0其它 |
| 调拨单详情备注 | std\_remark | String | 255 | Y | 调拨单详情备注 |
| 货品单位 | goods\_unit | String | 20 | Y | 货品单位 |
| 货品规格单位 | unit\_name | String | 20 | Y | 货品规格单位 |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 有效期 | expire\_date | String | 40 | Y | 有效期 |
| 是否残次品 | defect | boolean | 1 | Y | true:  残次品<br>false:  正品 |
| 货位编号 | position\_no | String | 20 | Y | 货位编号 |
| 调拨单明细id | src\_order\_detail\_id | Int | 11 | Y | 调拨单明细id |
| 货位明细 | position\_details\_list | List<Map<String, Object>> |  | Y | 货位明细 |

**position\_details\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货位明细id | rec\_id | Int | 11 | Y | 货位明细id |
| 出库单明细id | stockout\_detail\_id | Int | 11 | Y | 出库单明细id |
| 货位id | position\_id | Int | 11 | Y | 货位id |
| 货位号 | position\_no | String | 20 | Y | 货位号 |
| 有效期 | expire\_date | String |  | Y | 有效期 |
| 批次号 | batch\_no | Sting | 40 | Y | 批次号 |
| 当前货位出库总货品数量 | position\_goods\_count | Decimal(19,4) |  | Y | 当前货位出库总货品数量 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Transfer.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Transfer.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Transfer.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Transfer.queryWithDetail#autoTab5_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"start_time"``:``"2019-12-11 00:00:00"``,`<br>```"end_time"``:``"2019-12-31 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2019-12-11 00:00:00'``;`<br>`$params``->end_time =``'2019-12-31 00:00:00'``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.Transfer.queryWithDetail"``,``$pager``,``$params``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Transfer.queryWithDetail#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"order_no"``:``"CH2023012822"``,`<br>```"consign_time"``: 1674897720000,`<br>```"post_fee"``: 0,`<br>```"receiver_city"``: 0,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 2847800,`<br>```"stockout_id"``: 1634770,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"goods_count"``: 1,`<br>```"total_amount"``: 10,`<br>```"remark"``:``""``,`<br>```"brand_no"``:``"ffl"``,`<br>```"brand_name"``:``"发发拉"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_name"``:``"暂无"``,`<br>```"spec_code"``:``"LL "``,`<br>```"defect"``:``false``,`<br>```"cost_price"``: 10,`<br>```"weight"``: 0.2,`<br>```"goods_type"``: 1,`<br>```"std_remark"``:``""``,`<br>```"unit_name"``:``"口"``,`<br>```"goods_unit"``:``"箱"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"position_no"``:``"bhq002"``,`<br>```"position_details_list"``: [{`<br>```"rec_id"``: 125750,`<br>```"stockout_detail_id"``: 2847800,`<br>```"position_id"``: 69789,`<br>```"position_no"``:``"bhq002"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``"2022-08-27 00:00:00"``,`<br>```"position_goods_count"``: 1`<br>```}]`<br>```}],`<br>```"remark"``:``""``,`<br>```"goods_count"``: 1,`<br>```"stockout_id"``: 1634770,`<br>```"src_order_no"``:``"TF2301280049"``,`<br>```"from_warehouse_no"``:``"234234234"``,`<br>```"st_created"``:``"2023-01-28 17:22:00"``,`<br>```"warehouse_no"``:``"234234234"``,`<br>```"receiver_telno"``:``""``,`<br>```"receiver_zip"``:``""``,`<br>```"receiver_name"``:``""``,`<br>```"receiver_country"``: 0,`<br>```"order_type"``: 2,`<br>```"to_warehouse_no"``:``"333444"``,`<br>```"receiver_province"``: 0,`<br>```"logistics_no"``:``""``,`<br>```"receiver_district"``: 0,`<br>```"weight"``: 0,`<br>```"goods_total_amount"``: 10,`<br>```"receiver_mobile"``:``""``,`<br>```"operator_name"``:``"nff"``,`<br>```"goods_total_cost"``:``"10.00000000"``,`<br>```"receiver_address"``:``""``,`<br>```"status"``: 110,`<br>```"package_fee"``: 0`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Transfer.queryWithDetail#autoTab6_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"仓库不存在"`<br>`}` |
