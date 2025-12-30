---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdOutDetail"
title: "API文档"
---
**wms.StockPd.queryStockPdOutDetail** **（盘点出库单查询 ）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP盘点出库单信息 |
| **1.2 适用版本：** 客户端 V1.3.9.6及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

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
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无出库单号或源单号，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int | 4 | N | 查询时间限制类型。<br>1:最后修改时间<br>2:发货时间<br>默认1 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 出库单号 | stockout\_no | String | 40 | N | 出库单号 |
| 盘点单号 | src\_order\_no | String | 40 | N | 盘点单号 |
| 出库单状态 | status | String | 40 | N | 出库单状态:  <br>50待审核<br>90延时发货<br>110已完成 |

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
| 单据数据 | data | Map<String, Object> |  | Y | 单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 盘点出库单相关数据 |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单ID | stockout\_id | Int | 11 | Y | 出库单ID |
| 出库单号 | order\_no | String | 40 | Y | 出库单号 |
| 源单号 | src\_order\_no | String | 40 | Y | 源单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 出库时间 | consign\_time | String | 40 | Y | 出库时间 |
| 出库类型 | order\_type | Int | 4 | Y | 出库类型<br>4盘亏出库 |
| 出库单状态 | status | Int | 4 | Y | 出库单状态<br>50待审核<br>90延时发货<br>110已完成 |
| 出库数量 | goods\_count | Decimal(19,4) |  | Y | 出库数量 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 收件人姓名 | receiver\_name | varchar | 40 | Y | 收件人姓名 |
| 国家ID | receiver\_country | Int | 6 | Y | 国家ID |
| 省ID | receiver\_province | Int | 11 | Y | 省ID |
| 城市ID | receiver\_city | Int | 11 | Y | 城市ID |
| 地区ID | receiver\_district | Int | 11 | Y | 地区ID |
| 收件地址 | receiver\_address | Sring | 256 | Y | 收件地址 |
| 收件人手机号 | receiver\_mobile | Sring | 40 | Y | 收件手机号 |
| 收件固话号 | receiver\_telno | Sring | 40 | Y | 收件人固话号 |
| 邮编 | receiver\_zip | Sring | 20 | Y | 邮编 |
| 出库单备注 | remark | Sring | 255 | Y | 出库单备注 |
| 制单人 | operator\_name | Sring | 40 | Y | 制单人 |
| 总成本 | goods\_total\_cost | Decimal(19,4) |  | Y | 总成本 |
| 盘点单备注 | pd\_order\_remark | String |  | Y | 盘点单备注 |
| 出库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 出库单明细 |

**d** **etail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单详情ID | rec\_id | Int | 11 | Y | 出库单详情ID |
| 出库单ID | stockout\_id | Int | 11 | Y | 出库单ID |
| 数量 | goods\_count | Decimal(19,4) |  | Y | 数量 |
| 出库单详情备注 | remark | String | 64 | Y | 出库单详情备注 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 是否残次品 | defect | boolean | 1 | Y | true:  残次品<br>false:  正品 |
| 成本价 | cost\_price | Decimal(19,4) |  | Y | 成本价(存货成本) |
| 总重量 | weight | Decimal(19,4) |  | Y | 总重量（货品档案预估重量\*数量） |
| 货品类型 | goods\_type | Int | 4 | Y | 货品类型<br>0：其它<br>1：销售货品<br>2：原材料<br>3：包装物<br>4：周转材料<br>5：虚拟商品<br>6：固定资产<br>8：分装箱 |
| 单位 | unit\_name | String | 20 | Y | 单位 |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 货位编号 | position\_no | String | 20 | Y | 货位编号 |
| 有效期 | expire\_date | String | 40 | Y | 有效期 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdOutDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdOutDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdOutDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdOutDetail#autoTab5_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"wms.StockPd.queryStockPdOutDetail"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdOutDetail#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"order_no"``:``"CKDH202201203"``,`<br>```"consign_time"``: 1642661817000,`<br>```"receiver_province"``: 0,`<br>```"logistics_no"``:``""``,`<br>```"receiver_city"``: 0,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 637286,`<br>```"stockout_id"``: 473480,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"goods_count"``: 5,`<br>```"remark"``:``""``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"brand_name"``:``"无"``,`<br>```"goods_name"``:``"旺店通"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_name"``:``"旺店通"``,`<br>```"spec_code"``:``""``,`<br>```"defect"``:``false``,`<br>```"cost_price"``: 0.0011,`<br>```"weight"``: 0,`<br>```"goods_type"``: 1,`<br>```"unit_name"``:``""``,`<br>```"batch_no"``:``""`<br>```}],`<br>```"receiver_district"``: 0,`<br>```"remark"``:``"盘亏出库"``,`<br>```"goods_count"``: 5,`<br>```"stockout_id"``: 473480,`<br>```"receiver_mobile"``:``""``,`<br>```"src_order_no"``:``"PD2022012003"``,`<br>```"operator_name"``:``"AAAA"``,`<br>```"pd_order_remark"``:``""``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"receiver_telno"``:``""``,`<br>```"receiver_zip"``:``""``,`<br>```"goods_total_cost"``:``"0.00550000"``,`<br>```"receiver_name"``:``""``,`<br>```"receiver_address"``:``""``,`<br>```"receiver_country"``: 0,`<br>```"order_type"``: 4,`<br>```"status"``: 110`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdOutDetail#autoTab6_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
