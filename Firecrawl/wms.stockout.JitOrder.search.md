---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.JitOrder.search"
title: "API文档"
---
**wms.stockout.JitOrder.search（JIT出库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的JIT出库单单据信息 |
| **1.2 适用版本：** 客户端 V1.5.3.3及以上版本 |
| **1.3 增量获取：**按照制单时间进行获取 |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

**2.调用场** **景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段 |
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
| 查询参数 | params | Map<String, Object> |  | y | 查询参数 |
| 分页 | pager | pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | y | 起始时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | y | 结束时间, yyyy-MM-dd HH:mm:ss格式 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小 |
| 页号 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 返回0为正常 |
| 错误信息 | message | String |  | n | 无错误信息不返回 |
| 出库单信息 | data | Map<String, Object> |  | n | 出库单信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据仅自有平台及线下平台返回，其他平台均不返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | y | JIT出库单相关数据 |
| 总数 | total\_count | Int | 11 | n | 查询条件总数单据 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 标记名称 | flag\_name | String | 32 | y | 标记名称 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量 |
| 货品种类数 | goods\_type\_count | Int | 11 | y | 货品种类数 |
| 物流公司名称 | logistics\_company\_name | String | 40 | y | 系统内手动维护的物流公司名称 |
| 物流单号 | logistics\_no | String | 40 | y | 物流单号 |
| 物流公司id | logistics\_id | int |  | y | 系统内手动维护的物流公司对应的id |
| 制单员 | operator\_name | String | 50 | y | 制单员 |
| po编号列表 | po\_no\_list | String | 255 | y | po编号列表 |
| 收货仓名称 | receive\_warehouse\_name | String | 64 | y | 收货仓名称 |
| 收货仓编号 | receive\_warehouse\_no | String | 40 | y | 收货仓编号 |
| 备注 | remark | String | 255 | y | 备注 |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺id | shop\_id | short |  | y | 店铺id |
| 店铺名称 | shop\_name | String | 128 | y | 店铺名称 |
| 平台拣货单号 | src\_tids | String | 255 | y | 平台拣货单号 |
| 状态 | status | Byte |  | y | 状态 |
| 出库单号 | stockout\_no | String | 40 | y | 出库单号 |
| 出库单id | stockout\_id | Int | 11 | y | 出库单id |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | y | 仓库名称 |
| 仓库id | warehouse\_id | int |  | y | 仓库id |
| 邮费 | weigh\_post\_cost | String | 40 | y | 邮费 |
| 发货时间 | consign\_time | String |  | y | 发货时间，<br>格式: yyyy-MM-dd HH:mm:ss |
| 最后修改时间 | modified | String |  | y | 最后修改时间格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String |  | y | 创建时间，<br>格式: yyyy-MM-dd HH:mm:ss |
| 销售总金额 | amount | Decimal(19,4) |  | y | 销售总金额（供货价\*数量） |
| 明细列表 | detail\_list | List<Map<String, Object>> |  | y | 明细列表 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 批次号 | batch\_no | String | 40 | 是 | 批次号 |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 是否残次品 | defect | boolean |  | 是 | 是否残次品 |
| 有效期 | expire\_date | String |  | 是 | 有效期 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品编码 | goods\_no | String | 40 | 是 | 货品编码 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 规格编码 | spec\_code | String | 40 | 是 | 规格编码 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 总体积 | volume | Decimal(19,4) |  | 是 | 总体积，货品长宽高\*数量 |
| 总重量 | weight | Decimal(19,4) |  | 是 | 总重量，货品重量\*数量 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 品牌编号 | brand\_no | String | 32 | 是 | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 审核时成本 | checked\_cost\_price | Decimal(19,4) |  | 是 | 审核时成本（**货品出库时的瞬时成本**） |
| 含税供货价 | tax\_price | Decimal(19,4) |  | 是 | 含税供货价 |
| 供货价 | price | Decimal(19,4) |  | 是 | 供货价 |
| 出库单id | stockout\_id | int |  | 是 | 出库单id |
| 货品id | goods\_id | int |  | 是 | 货品id |
| 单品id | spec\_id | int |  | 是 | 单品id |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String |  | 是 | 创建时间，<br>格式: yyyy-MM-dd HH:mm:ss |
| 明细id | rec\_id | int |  | 是 | 明细id |
| po单号 | po\_no | String |  | 是 | po单号 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2022-08-30 11:10:04"``,`<br>```"start_time"``:``"2022-08-25 11:10:04"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>`$parMap =``new``stdClass();`<br>`$parMap->start_time =``'2022-08-25 11:10:04'``;`<br>`$parMap->end_time =``'2022-08-30 11:10:04'``;`<br>`$pager =``new``Pager(``2``,``0``,``true``);`<br>`try``{`<br>```$data = $client->pageCall(``"wms.stockout.JitOrder.search"``, $pager, $parMap);`<br>`}``catch``(WdtErpException $e)`<br>`{`<br>```echo $e->getMessage();`<br>`}`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 4,`<br>```"order_list"``: [{`<br>```"flag_id"``: 0,`<br>```"consign_time"``:``"2022-10-18 11:19:34"``,`<br>```"operator_id"``: 23,`<br>```"detail_list"``: [{`<br>```"stockout_id"``: 1630052,`<br>```"spec_id"``: 158800,`<br>```"goods_name"``:``"阿拉蕾 新品黄色"``,`<br>```"goods_no"``:``"all"``,`<br>```"num"``: 2,`<br>```"spec_name"``:``"黄色"``,`<br>```"spec_code"``:``""``,`<br>```"defect"``:``false``,`<br>```"barcode"``:``"all1"``,`<br>```"remark"``:``""``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"brand_id"``: 2138,`<br>```"price"``: 0,`<br>```"tax_price"``: 0,`<br>```"checked_cost_price"``: 8.95,`<br>```"spec_no"``:``"all1"``,`<br>```"brand_name"``:``"商品"``,`<br>```"brand_no"``:``"BD202103300001"``,`<br>```"volume"``:``"0"``,`<br>```"weight"``:``"4"`<br>```}],`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"receive_warehouse_id"``: 30,`<br>```"goods_count"``: 2,`<br>```"stockout_id"``: 1630052,`<br>```"flag_name"``:``"无"``,`<br>```"logistics_id"``: 972,`<br>```"warehouse_no"``:``"zxy03"``,`<br>```"logistics_company_name"``:``"唯品专配22"``,`<br>```"shop_no"``:``"vip_yqf"``,`<br>```"receive_warehouse_name"``:``"VIP_BJ"``,`<br>```"receive_warehouse_no"``:``"VIP_BJ"``,`<br>```"amount"``:``"0.00000000"``,`<br>```"logistics_no"``:``"111111112"``,`<br>```"created"``:``"2022-10-18 11:19:04"``,`<br>```"stockout_no"``:``"CH202210183"``,`<br>```"shop_name"``:``"唯品测试_勿用勿用!!!"``,`<br>```"src_tids"``:``"PICK-20220901003"``,`<br>```"shop_id"``: 281,`<br>```"operator_name"``:``"aaaaa"``,`<br>```"weigh_post_cost"``: 0,`<br>```"warehouse_name"``:``"zxy的测试仓3"``,`<br>```"po_no_list"``:``"34565466576713333"``,`<br>```"warehouse_id"``: 395,`<br>```"status"``: 110`<br>```}]`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"时间参数必填"``,`<br>```"status"``: 100`<br>`}` | |
