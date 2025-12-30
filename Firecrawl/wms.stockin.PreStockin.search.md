---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.search"
title: "API文档"
---
**wms.stockin.PreStockin.search** **（预入库单据查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP预入库单单据信息 |
| **1.2 适用版本：** 客户端 V1.5.6.6及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** |
| **1.5 注意事项：** **【权限校验】：仓库权限**,此接口仅支持奇门自定场景访问 |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**自研商城、分销系统、全渠道等系统对接 |

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
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 入库单号 | stockin\_no | String | 20 | N | 入库单号 |
| 寄回物流单号 | logistics\_no | String | 40 | N | 寄回物流单号 |
| 修改起始时间 | mt\_from | datetime | 40 | N | 修改起始时间 |
| 修改结束时间 | mt\_to | datetime | 40 | N | 修改结束时间 |
| 创建起始时间 | ct\_from | datetime | 40 | N | 创建起始时间 |
| 创建结束时间 | ct\_to | datetime | 40 | N | 创建结束时间 |
| 退货人姓名 | sender\_name | String | 20 | N | 退货人姓名 |
| 客户网名 | buyer\_nick | String | 100 | N | 客户网名 |
| 退货人手机 | sender\_mobile | String | 40 | N | 退货人手机 |
| 商家编码 | spec\_no | String | 40 | N | 商家编码 |
| 货品编号 | goods\_no | String | 40 | N | 货品编号 |
| 货品名称 | goods\_name | String | 40 | N | 货品名称 |
| 条码 | barcode | String | 40 | N | 条码 |
| 货品简称 | short\_name | String | 40 | N | 货品简称 |
| 备注 | remark | String | 40 | N | 备注 |
| 入库单状态 | status | int | 4 | N | 10:已取消;20编辑中;30:待审核;80:已完成 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | int | 4 | N | 分页大小 |
| 页号 | page\_no | int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | data | Map<String, Object> |  | N | 单据数据 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 状态 | status | int | 1 | N | 0表示调用成功,在调用错误时候不返回该值。 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 单据数据 |
| 数据总条数 | total\_count | int |  | Y | 单据数据总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单id |
| 入库单号 | stockin\_no | String | 20 | Y | 入库单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 源单号类型 | src\_order\_type | int | 4 | Y | 源单号类型（预入库单类型为固定值"22"） |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 物流名称 | logistics\_name | String | 40 | Y | 物流名称 |
| 状态 | status | int | 4 | Y | 状态 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 货品种类数 | goods\_type\_count | int | 6 | Y | 货品种类数 |
| 便签数量 | note\_count | int | 6 | Y | 便签数量 |
| 标记名称 | flag\_name | String | 32 | Y | 标记名称 |
| 入库人姓名 | operator\_name | String | 40 | Y | 入库人姓名 |
| 审核员姓名 | checker\_name | String | 40 | Y | 审核员姓名 |
| 备注 | remark | String | 255 | Y | 备注 |
| 审核时间 | check\_time | datetime |  | Y | 审核时间 |
| 创建时间 | created | timestamp |  | Y | 创建时间 |
| 预入库单自定义属性1 | prop1 | String | 255 | Y | 预入库单自定义属性1 |
| 预入库单自定义属性2 | prop2 | String | 255 | Y | 预入库单自定义属性2 |
| 物流id | logistics\_id | Int | 6 | Y | 物流id |
| 源单id | src\_order\_id | Int | 11 | Y | 源单id |
| 修改时间 | modified\_date | String | 40 | Y | 修改时间 |
| 创建时间 | created\_date | String | 40 | Y | 创建时间 |
| 仓库id | warehouse\_id | Int | 6 | Y | 仓库id |
| 源预入库单号 | prop3 | String | 255 | Y | 预入库单拆分前的预入库单号 |
| wms业务单号 | wms\_code | String |  | Y | wms业务单号 |
| 详情列表 | detail\_list | List<Map<String, Object>> |  | Y | 详情列表 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单id |
| 明细id | rec\_id | Int | 11 | Y | 明细id |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 入库数量 | num | Decimal(19,4) |  | Y | 入库数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | Y | 辅助数量 |
| 预期数量 | expect\_num | Decimal(19,4) |  | Y | 预期数量 |
| 有效期 | expire\_date | String | 40 | Y | 有效期 |
| 生产日期 | production\_date | String | 40 | Y | 生产日期 |
| 批次号 | batch\_no | String | 20 | Y | 批次号 |
| 备注 | remark | String | 255 | Y | 备注 |
| 重量 | weight | Decimal(19,4) |  | Y | 重量 |
| 总重量 | goods\_weight | Decimal(19,4) |  | Y | 总重量 |
| 是否残次品 | defect | bool | 1 | Y | 是否残次品 |
| 单位换算系数 | unit\_ratio | Decimal(19,4) |  | Y | 单位换算系数 |
| 保质期 | validity\_days | int | 6 | Y | 保质期(天数) |
| 需要质检的数量 | need\_inspect\_num | Decimal(19,4) |  | Y | 需要质检的数量 |
| 基本单位名称 | unit\_name | String | 20 | Y | 基本单位名称 |
| 辅助单位名称 | aux\_unit\_name | String | 20 | Y | 辅助单位名称 |
| 货位编号 | position\_no | String | 20 | Y | 货位编号 |
| 货品id | goods\_id | Int | 11 | Y | 货品id |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 修改时间 | modified\_date | String | 40 | Y | 修改时间 |
| 创建时间 | created\_date | String | 40 | Y | 创建时间 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.search#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.search#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.search#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.search#autoTab5_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"mt_from"``:``"2020-01-01 00:00:00"``,`<br>```"mt_to"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->mt_from =``"2020-01-01 00:00:00"``;`<br>`$parMap``->mt_to   =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"wms.stockin.PreStockin.search "``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.search#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"logistics_name"``:``"小火柴其他物流"``,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 206498,`<br>```"stockin_id"``: 86705,`<br>```"goods_id"``: 106369,`<br>```"spec_id"``: 276760,`<br>```"goods_name"``:``"隔离衣"``,`<br>```"goods_no"``:``"XT001"``,`<br>```"spec_name"``:``"XL"``,`<br>```"spec_no"``:``"XT001"``,`<br>```"expire_date"``:``""``,`<br>```"num"``:``"1.0000"``,`<br>```"num2"``:``"0.0100"``,`<br>```"production_date"``:``""``,`<br>```"batch_no"``:``""``,`<br>```"expect_num"``:``"0.0000"``,`<br>```"remark"``:``""``,`<br>```"weight"``:``"0.0000"``,`<br>```"goods_weight"``:``"0.0000"``,`<br>```"defect"``:``false``,`<br>```"modified_date"``:``"2022-09-14 19:43:49"``,`<br>```"created_date"``:``"2022-09-14 19:43:49"``,`<br>```"unit_ratio"``:``"100.0000"``,`<br>```"validity_days"``: 730,`<br>```"need_inspect_num"``:``"0.0000"``,`<br>```"unit_name"``:``"件"``,`<br>```"position_no"``:``"A01"``,`<br>```"aux_unit_name"``:``"箱(100件)"`<br>```}],`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"goods_count"``:``"1.0000"``,`<br>```"flag_name"``:``"无"``,`<br>```"src_order_no"``:``""``,`<br>```"logistics_id"``: 491,`<br>```"warehouse_no"``:``"234234234"``,`<br>```"modified"``: 1663155836000,`<br>```"note_count"``: 0,`<br>```"checker_name"``:``"系统"``,`<br>```"stockin_id"``: 86705,`<br>```"src_order_id"``: 0,`<br>```"logistics_no"``:``""``,`<br>```"created"``: 1663155829000,`<br>```"src_order_type"``: 22,`<br>```"version_id"``: 0,`<br>```"modified_date"``:``"2022-09-14 19:43:56"``,`<br>```"prop2"``:``""``,`<br>```"prop1"``:``""``,`<br>```"operator_name"``:``"nff"``,`<br>```"stockin_no"``:``"RK20220914224"``,`<br>```"created_date"``:``"2022-09-14 19:43:49"``,`<br>```"status"``: 10,`<br>```"warehouse_id"``: 330`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.search#autoTab6_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"参数中必须包含起止时间"`<br>`}` |
