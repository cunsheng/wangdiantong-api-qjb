---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdInDetail"
title: "API文档"
---
**wms.StockPd.queryStockPdInDetail** **（盘点入库单查询 ）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP盘点入库单信息 |
| **1.2 适用版本：** 客户端 V1.4.3.2及以上版本 |
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
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无入库单号或源单号，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int | 4 | N | 查询时间限制类型。<br>1:最后修改时间<br>2:审核时间<br>默认1 |
| 入库单状态 | status | String | 255 | N | 英文逗号拼接的状态值: <br>10=已取消<br>20=编辑中<br>30=待审核<br>37=待质检<br>40=质检确认<br>60=待结算<br>70=暂估结算<br>80=已完成 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 入库单号 | stockin\_no | String | 20 | N | 入库单号 |
| 盘点单号 | src\_order\_no | String | 40 | N | 盘点单号 |

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
| 单据数据 | data | Map<String, Object> |  | Y | 入库单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 入库单相关数据 |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单ID | stockin\_id | Int | 11 | Y | 入库单ID |
| 入库单号 | order\_no | String | 20 | Y | 入库单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称 |
| 入库时间 | stockin\_time | String | 40 | Y | 入库时间 |
| 创建时间 | created\_time | String | 40 | Y | 创建时间 |
| 入库单备注 | remark | Sring | 255 | Y | 入库单备注 |
| 入库单状态 | status | int | 4 | Y | 状态值:<br>10=已取消<br>20=编辑中<br>30=待审核<br>37=待质检<br>40=质检确认<br>60=待结算<br>70=暂估结算<br>80=已完成 |
| 货品总数 | goods\_count | Decimal(19,4) |  | Y | 货品总数 |
| 审核时间 | check\_time | String | 40 | Y | 审核时间 |
| 源单号 | src\_order\_no | Sring | 40 | Y | 源单号 |
| 操作人 | operator\_name | Sring | 40 | Y | 操作人 |
| 总成本价 | total\_price | Decimal(19,4) |  | Y | 总成本价 |
| 盘点单备注 | pd\_order\_remark | String |  | Y | 盘点单备注 |
| 入库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 入库单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单ID | stockin\_id | Int | 11 | Y | 入库单ID |
| 数量 | goods\_count | Decimal(19,4) |  | Y | 数量 |
| 成本价 | total\_cost | Decimal(19,4) |  | Y | 成本价(存货成本\*数量) |
| 备注 | remark | String | 255 | Y | 备注 |
| 调整后数量 | right\_num | Decimal(19,4) |  | Y | 调整后数量 |
| 单位 | goods\_unit | String | 20 | Y | 单位 |
| 是否残次品 | defect | bool | 1 | Y | true：残次品<br>false：正品 |
| 批次号 | batch\_no | String | 40 | Y | 批次号，如果没有则返回空字符串 |
| 明细id | rec\_id | Int | 11 | Y | 明细id(主键) |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 自定义属性2 | prop2 | String | 255 | Y | 自定义属性2（货品档案单品自定义属性2） |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 货位编号 | position\_no | String | 20 | Y | 货位编号 |
| 有效期 | expire\_date | String | 40 | Y | 有效期，如果没有则返回空字符串 |
| 生产日期 | production\_date | String | 40 | Y | 生产日期，如果没有则返回空字符串 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdInDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdInDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdInDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdInDetail#autoTab5_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"wms.StockPd.queryStockPdInDetail"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdInDetail#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"order_no"``:``"RK2022122859"``,`<br>```"created_time"``: 1672208586000,`<br>```"stockin_id"``: 88464,`<br>```"total_price"``: 0,`<br>```"detail_list"``: [{`<br>```"stockin_id"``: 88464,`<br>```"goods_count"``: 20,`<br>```"total_cost"``: 0,`<br>```"defect"``:``false``,`<br>```"remark"``:``""``,`<br>```"right_num"``: 20,`<br>```"batch_no"``:``""``,`<br>```"rec_id"``: 209899,`<br>```"goods_name"``:``"xiaowanzi"``,`<br>```"goods_no"``:``"xiaowanzi"``,`<br>```"spec_no"``:``"xiaowanzi"``,`<br>```"prop2"``:``""``,`<br>```"spec_name"``:``""``,`<br>```"spec_code"``:``"xiaowanzi"``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"brand_name"``:``"无"``,`<br>```"position_no"``:``"其它未上架"``,`<br>```"goods_unit"``:``"无"``,`<br>```"expire_date"``:``"2024-04-27"``,`<br>```"production_date"``:``"2023-04-29"`<br>```}],`<br>```"remark"``:``"盘盈入库"``,`<br>```"goods_count"``: 20,`<br>```"src_order_no"``:``"PD2022122816"``,`<br>```"operator_name"``:``"aaa"``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"pd_order_remark"``:``""``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"stockin_time"``: 1672208586000,`<br>```"status"``: 80,`<br>```"check_time"``: 1672208586000`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdInDetail#autoTab6_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
