---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Pack.search"
title: "API文档"
---
**wms.stockout.Pack.search** **（装箱单查询)**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**查询系统内非jit类型的装箱单 |
| **1.2 适用版本：** 客户端 V1.4.0.2及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

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
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | Int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String |  | 否 | 最后修改时间, yyyy-MM-dd HH:mm:ss格式<br>当出库单号和物流单号未传的情况下，时间条件必传 |
| 结束时间 | end\_time | String |  | 否 | yyyy-MM-dd HH:mm:ss格式 |
| 单据类型 | src\_order\_type | Byte |  | 否 | 单据类型<br>1：销售出库<br>2：调拨出库<br>4：盘库出库<br>5：生产出库<br>14：采购退货出库<br>21：其它出库<br>不传默认1 |
| 物流单号 | logistics\_no | String |  | 否 | 物流单号 |
| 出库单号 | stockout\_no | String |  | 否 | 出库单号 |
| 仓库编号 | warehouse\_no | String |  | 否 | 仓库编号 |

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
| 单据信息 | data | Map<String, Object> |  | 是 | 单据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | 是 | 单据数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 装箱单唯一键 | rec\_id | Int | 11 | 是 | 装箱单唯一键 |
| 装箱单号 | order\_no | String | 40 | 是 | 装箱单号 |
| 状态 | status | Byte | 4 | 是 | 装箱单状态<br>10：未完成<br>15：延时发货<br>16：已发货<br>20：待结算<br>30：已完成 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 出库单号 | stockout\_no | String | 40 | 是 | 出库单号 |
| 源单据类型 | src\_order\_type | Byte |  | 是 | 源单据类型<br>1：销售出库<br>2：调拨出库<br>4：盘亏出库<br>5：生产出库<br>14：采购退货出库<br>21：其它出库 |
| 物流单号 | logistics\_no | String | 50 | 是 | 物流单号 |
| 物流公司编号 | logistics\_company\_no | String | 20 | 是 | ERP内手动维护的物流公司编号 |
| 重量 | weight | Decimal(19,4) |  | 是 | 称重重量 |
| 预估重量 | calc\_weight | Decimal(19,4) |  | 是 | 预估重量 |
| 货品数量 | goods\_count | Decimal(19,4) |  | 是 | 货品数量 |
| 货品种类数 | goods\_type\_count | Int |  | 是 | 货品种类数 |
| 打包员 | packager\_name | String | 50 | 是 | 打包员 |
| 发货时间 | consign\_time | String |  | 是 | 发货时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 备注 | remark | String | 256 | 是 | 备注 |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 创建时间 | created | String |  | 是 | 创建时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 物流公司id | logistics\_id | Int | 11 | 是 | 物流公司id |
| 仓库id | warehouse\_id | Int | 11 | 是 | 仓库id |
| 打包员id | packager\_id | Int | 11 | 是 | 打包员id |
| 明细信息 | detail\_list | List<Map<String, Object>> |  | 是 | 明细数据 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细唯一id | rec\_id | Int | 11 | 是 | 明细唯一id |
| 装箱单唯一键 | logistics\_order\_id | Int | 11 | 是 | 装箱单唯一键 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 单品id | spec\_id | Int | 11 | 是 | 单品id |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 规格编码 | spec\_code | String | 40 | 是 | 规格编码 |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 残次品 | defect | boolean | 1 | 是 | true：残次品<br>false：正品 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 批次号 | batch\_no | String | 40 | 是 | 批次号 |
| 批次id | batch\_id | Int | 11 | 是 | 批次id |
| 备注 | remark | String | 512 | 是 | 备注 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Pack.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Pack.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Pack.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Pack.search#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2020-06-02 11:26:31"``,`<br>```"start_time"``:``"2020-05-12 11:00:00"`<br>```}`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``'2022-04-21 16:42:51'``;`<br>`$parMap``->end_time =``'2022-05-29 16:42:51'``;`<br>`$pager``=``new``Pager(2, 0, true);`<br>`try``{`<br>```$data``=``$client``->pageCall(``"wms.stockout.Pack.search"``,``$pager``,``$parMap``);`<br>`}``catch``(WdtErpException``$e``)`<br>`{`<br>```echo``$e``->getMessage();`<br>`}`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Pack.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"order_list"``: [`<br>```{`<br>```"calc_weight"``: 0.0065,`<br>```"consign_time"``:``"2022-04-27 16:42:51"``,`<br>```"created"``:``"2022-04-21 15:43:03"``,`<br>```"detail_list"``: [`<br>```{`<br>```"barcode"``:``"qq01"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``:``""``,`<br>```"defect"``:``false``,`<br>```"goods_name"``:``"zxy的应用"``,`<br>```"goods_no"``:``"zxydapp"``,`<br>```"logistics_order_id"``: 3441352,`<br>```"num"``: 1.0,`<br>```"rec_id"``: 377,`<br>```"remark"``:``""``,`<br>```"spec_code"``:``"qq"``,`<br>```"spec_id"``: 4387,`<br>```"spec_name"``:``"qq"``,`<br>```"spec_no"``:``"qq"`<br>```}`<br>```],`<br>```"goods_count"``: 1.0,`<br>```"goods_type_count"``: 1,`<br>```"logistics_company_no"``:``"0914"``,`<br>```"logistics_id"``: 62,`<br>```"logistics_no"``:``"ZS202204210059"``,`<br>```"modified"``:``"2022-04-27 16:42:51"``,`<br>```"order_no"``:``"LG22042174"``,`<br>```"packager_id"``: 0,`<br>```"packager_name"``:``"系统"``,`<br>```"rec_id"``: 3441352,`<br>```"remark"``:``""``,`<br>```"src_order_type"``: 1,`<br>```"status"``: 20,`<br>```"stockout_no"``:``"CK2022042165"``,`<br>```"warehouse_id"``: 314,`<br>```"warehouse_no"``:``"zxy-app"``,`<br>```"weight"``: 1.2198`<br>```}`<br>```],`<br>```"total_count"``: 2`<br>```},`<br>```"status"``: 0`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Pack.search#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"您的查询时间过宽,查询时间不能大于30天"``,`<br>```"status"``: 100`<br>`}` |
