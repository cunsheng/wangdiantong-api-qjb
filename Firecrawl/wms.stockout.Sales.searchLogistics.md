---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchLogistics"
title: "API文档"
---
**wms.stockout.Sales.searchLogistics（物** **流单查询)**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取包含多物流的出库物流单信息 |
| **1.2 适用版本：** 客户端 V1.5.8.2及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：**start\_time与end\_time时间跨度不超过1天 |
| **1.5注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

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
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String |  | 是 | 最后变更时间, 开始时间,样例: 2022-01-25 16:40:06 |
| 结束时间 | end\_time | String |  | 是 | 结束时间 |
| 状态 | status | Int |  | 是 | 10:待发货;15:延时发货;20:待结算;30:已结算 |
| 仓库编号 | warehouse\_no | String |  | 否 | 仓库编号 |
| 单据类型 | order\_type | String |  | 否 | 1:销售订单;2:调拨单;5:生产原料;21:其它出库;24:调整出库<br>（目前仅支持查询销售订单类型的物流单数据） |
| 订单编号 | trade\_no | String |  | 否 | 订单编号 |
| 原始单号 | src\_tids | String |  | 否 | 多个原始单号使用英文逗号分隔 |
| 店铺编号 | shop\_no | String |  | 否 | 店铺编号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

**返回值为一个Map<String, Object>**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 货品数据 | data | Map<String, Object> |  | 是 | 货品分类相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据 | order\_list | List<Map<String, Object>> |  | 是 | 物流单数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单号 | stockout\_no | string |  | 是 | 出库单号 |
| 出库单ID | stockout\_id | int |  | 是 | 出库单主键ID |
| 最后修改时间 | modified | string |  | 是 | 最后修改时间 |
| 发货时间 | consign\_time | string |  | 是 | 发货时间 |
| 物流公司名称 | logistics\_name | String |  | 是 | 在ERP内手工维护的物流公司名称 |
| 物流单号 | logistics\_no | String |  | 是 | 物流单号 |
| 高度 | height | Decimal(19,4) |  | 是 | 高度 |
| 宽度 | width | Decimal(19,4) |  | 是 | 宽度 |
| 长度 | length | Decimal(19,4) |  | 是 | 长度 |
| 称重结果 | weight | Decimal(19,4) |  | 是 | 称重结果 |
| 备注 | remark | String |  | 是 | 备注 |
| 状态 | status | Int |  | 是 | 10:待发货;15:延时发货;20:待结算;30:已结算 |
| 货品数量 | goods\_count | Decimal(19,4) |  | 是 | 货品数量 |
| 唯一键 | rec\_id | Int |  | 是 | 唯一键 |
| 物流公司id | logistics\_id | Int |  | 是 | 物流公司id |
| 估算邮资 | postage | Decimal(19,4) |  | 是 | 估算邮资 |
| 仓库名称 | warehouse\_name | String |  | 是 | 仓库名称 |
| 仓库编号 | warehouse\_no | String |  | 是 | 仓库编号 |
| 仓库id | warehouse\_id | Int |  | 是 | 仓库id |
| 导入重量 | import\_weight | Decimal(19,4) |  | 是 | 导入重量 |
| 导入邮资 | import\_postage | Decimal(19,4) |  | 是 | 导入邮资 |
| 重量差 | weight\_diff | Decimal(19,4) |  | 是 | 重量差 |
| 邮资差 | postage\_diff | Decimal(19,4) |  | 是 | 邮资差 |
| 估算重量 | calc\_weight | Decimal(19,4) |  | 是 | 估算重量 |
| 店铺编号 | shop\_no | String |  | 是 | 店铺编号 |
| 店铺名称 | shop\_name | String |  | 是 | 店铺名称 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchLogistics#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchLogistics#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchLogistics#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchLogistics#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"status"``: 30,`<br>```"order_type"``: 21,`<br>```"start_time"``:``"2020-02-03 17:15:17"``,`<br>```"end_time"``:``"2020-02-03 17:55:17"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-02-03 17:15:17"``;`<br>`$parMap``->end_time =``"2020-02-03 17:55:17"``;`<br>`$parMap``->status = 30;`<br>`$parMap``->order_type = 21;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.Sales.searchLogistics"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchLogistics#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order_list"``: [`<br>```{`<br>```"logistics_name"``:``"自由物流"``,`<br>```"consign_time"``:``"2025-05-26 14:30:00"``,`<br>```"remark"``:``""``,`<br>```"goods_count"``: 2,`<br>```"stockout_id"``: 700849,`<br>```"logistics_id"``: 185,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"import_weight"``: 0,`<br>```"modified"``:``"2025-05-26 14:30:00"``,`<br>```"calc_weight"``: 10,`<br>```"import_postage"``: 0,`<br>```"height"``: 0,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"logistics_no"``:``"ZS202505260002"``,`<br>```"stockout_no"``:``"CK202505265"``,`<br>```"length"``: 0,`<br>```"weight"``: 10,`<br>```"rec_id"``: 12673311,`<br>```"shop_name"``:``"wdtapi3-test"``,`<br>```"postage"``: 0,`<br>```"src_tids"``:``"20250407001"``,`<br>```"shop_id"``: 290,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"width"``: 0,`<br>```"trade_no"``:``"JY202504070099"``,`<br>```"weight_diff"``: 0,`<br>```"postage_diff"``: 0,`<br>```"warehouse_id"``: 311,`<br>```"status"``: 20`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchLogistics#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"参数中必须包含状态"`<br>`}` |
