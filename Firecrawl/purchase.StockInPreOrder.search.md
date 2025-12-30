---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.StockInPreOrder.search"
title: "API文档"
---
**purchase.StockInPreOrder.search（预约入库单查询** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：分页查询 |
| **1.2 适用版本：** 客户端 V1.6.0.10及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为7天 |
| **1.5注意事项：** |

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
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | Int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数， 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | N | 最后修改时间      不传入单号的情况下必须传入时间条件, 时间范围最大7天 |
| 结束时间 | end\_time | String | 40 | N | 最后修改时间      不传入单号的情况下必须传入时间条件, 时间范围最大7天 |
| 预约单单号 | pre\_order\_no | String |  | N | 预约单单号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | <Map<String, Object>> |  | 是 | 返回信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总条数 | total\_count | Int |  | 是 | 总条数 |
| 数据节点 | order\_list | List<Map<String, Object>> |  | 是 | 数据节点 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 预约单id | pre\_order\_id | int |  | Y | 预约单id |
| 预约单号 | pre\_order\_no | String |  | Y | 预约单号 |
| 业务单号 | busi\_order\_no | String |  | Y | 业务单号 |
| 业务单类型 | busi\_order\_type | Byte |  | Y | 1:采购单 2:调拨单 3:其他入库业务单 4:生产单 |
| 车牌号 | car\_number | String |  | Y | 车牌号 |
| 审核时间 | check\_time | String |  | Y | 审核时间 |
| 创建时间 | created | String |  | Y | 创建时间 |
| 派送人员 | deliver\_name | String |  | Y | 派送人员 |
| 预计派送时间 | deliver\_time | String |  | Y | 预计派送时间 |
| 标记名称 | flag\_time | String |  | Y | 标记名称 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间 |
| 供应商名称 | provider\_name | String |  | Y | 供应商名称 |
| 状态 | status | Byte |  | Y | 10:已取消 20:待审核 30:已审核 40:已驳回 50:已完成 |
| 联系电话 | telno | String |  | Y | 联系电话 |
| 仓库名称 | warehouse\_name | String |  | Y | 仓库名称 |
| 仓库编号 | warehouse\_no | String |  | Y | 仓库编号 |
| 仓库id | warehouse\_id | String |  | Y | 仓库id |
| 预约单明细 | detail\_List | List<Map<String,Object>> |  | Y | 预约单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 预约单明细唯一键 | rec\_id | int |  | Y | 预约单明细唯一键 |
| 辅助数量 | aux\_num | Decimal(19,4) |  | Y | 辅助数量 |
| 条码 | barcode | String |  | Y | 条码 |
| 基本单位 | base\_unit\_name | String |  | Y | 基本单位 |
| 批次号 | batch\_no | String |  | Y | 批次号 |
| 品牌名称 | brand\_name | String |  | Y | 品牌名称 |
| 分类名称 | class\_name | String |  | Y | 分类名称 |
| 有效期 | expire\_date | String |  | Y | 有效期 |
| 货品名称 | goods\_name | String |  | Y | 货品名称 |
| 货品编号 | goods\_no | String |  | Y | 货品编号 |
| 数量 | num | Decimal(19.4) |  | Y | 数量 |
| 供应商货品编号 | provider\_goods\_no | String |  | Y | 供应商货品编号 |
| 规格名称 | spec\_name | String |  | Y | 规格名称 |
| 商家编码 | spec\_no | String |  | Y | 商家编码 |
| 辅助单位名称 | unit\_name | String |  | Y | 辅助单位名称 |
| 预约未到货量 | lack\_num | Decimal(19,4) |  | Y | 预约未到货量 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2024-04-27"``,`<br>```"start_time"``:``"2024-04-20"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params =``new``stdClass();`<br>`$params->start_time =``'2022-07-15 11:42:56'``;`<br>`$params->end_time =``'2022-07-19 11:42:56'``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$data = $client->pageCall(``"purchase.StockInPreOrder.search"``, $pager, $parMap);` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"order_list"``: [`<br>```{`<br>```"busi_order_no"``:``"QR3306"``,`<br>```"busi_order_type"``: 3,`<br>```"car_number"``:``""``,`<br>```"check_time"``:``"2024-04-28 09:52:46"``,`<br>```"created"``:``"2024-04-15 20:23:43"``,`<br>```"deliver_name"``:``""``,`<br>```"deliver_time"``:``"2024-04-18 00:00:00"``,`<br>```"detail_list"``: [`<br>```{`<br>```"aux_num"``: 1.0,`<br>```"barcode"``:``"all1"``,`<br>```"base_unit_id"``: 3,`<br>```"base_unit_name"``:``"m箱"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``: null,`<br>```"brand_id"``: 5,`<br>```"brand_name"``:``"1"``,`<br>```"class_id"``: 0,`<br>```"class_name"``:``"无"``,`<br>```"expire_date"``: null,`<br>```"goods_name"``:``"原味酸奶"``,`<br>```"goods_no"``:``"sn1"``,`<br>```"num"``: 1.0,`<br>```"pre_order_id"``: 5,`<br>```"provider_goods_no"``: null,`<br>```"rec_id"``: 11,`<br>```"spec_name"``:``"阿拉蕾11号"``,`<br>```"spec_no"``:``"all1"``,`<br>```"unit_id"``: 50,`<br>```"unit_name"``:``"g43"`<br>```},`<br>```{`<br>```"aux_num"``: 3.0,`<br>```"barcode"``:``"all1"``,`<br>```"base_unit_id"``: 3,`<br>```"base_unit_name"``:``"m箱"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``: null,`<br>```"brand_id"``: 5,`<br>```"brand_name"``:``"1"``,`<br>```"class_id"``: 0,`<br>```"class_name"``:``"无"``,`<br>```"expire_date"``: null,`<br>```"goods_name"``:``"原味酸奶"``,`<br>```"goods_no"``:``"sn1"``,`<br>```"num"``: 3.0,`<br>```"pre_order_id"``: 5,`<br>```"provider_goods_no"``: null,`<br>```"rec_id"``: 13,`<br>```"spec_name"``:``"阿拉蕾11号"``,`<br>```"spec_no"``:``"all1"``,`<br>```"unit_id"``: 50,`<br>```"unit_name"``:``"g43"`<br>```},`<br>```{`<br>```"aux_num"``: 2.0,`<br>```"barcode"``:``"all2"``,`<br>```"base_unit_id"``: 3,`<br>```"base_unit_name"``:``"m箱"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``: null,`<br>```"brand_id"``: null,`<br>```"brand_name"``:``"无"``,`<br>```"class_id"``: null,`<br>```"class_name"``:``"无"``,`<br>```"expire_date"``: null,`<br>```"goods_name"``: null,`<br>```"goods_no"``: null,`<br>```"num"``: 2.0,`<br>```"pre_order_id"``: 5,`<br>```"provider_goods_no"``: null,`<br>```"rec_id"``: 12,`<br>```"spec_name"``:``"阿拉蕾12号"``,`<br>```"spec_no"``:``"all2"``,`<br>```"unit_id"``: 50,`<br>```"unit_name"``:``"g43"`<br>```},`<br>```{`<br>```"aux_num"``: 1.0,`<br>```"barcode"``:``"BC23091905"``,`<br>```"base_unit_id"``: 0,`<br>```"base_unit_name"``:``"无"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``: null,`<br>```"brand_id"``: null,`<br>```"brand_name"``:``"无"``,`<br>```"class_id"``: null,`<br>```"class_name"``:``"无"``,`<br>```"expire_date"``: null,`<br>```"goods_name"``: null,`<br>```"goods_no"``: null,`<br>```"num"``: 1.0,`<br>```"pre_order_id"``: 5,`<br>```"provider_goods_no"``: null,`<br>```"rec_id"``: 8,`<br>```"spec_name"``:``"蓝白条"``,`<br>```"spec_no"``:``"daj-sn2BW"``,`<br>```"unit_id"``: 0,`<br>```"unit_name"``:``"无"`<br>```},`<br>```{`<br>```"aux_num"``: 1.0,`<br>```"barcode"``:``""``,`<br>```"base_unit_id"``: 0,`<br>```"base_unit_name"``:``"无"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``: null,`<br>```"brand_id"``: null,`<br>```"brand_name"``:``"无"``,`<br>```"class_id"``: null,`<br>```"class_name"``:``"无"``,`<br>```"expire_date"``: null,`<br>```"goods_name"``: null,`<br>```"goods_no"``: null,`<br>```"num"``: 1.0,`<br>```"pre_order_id"``: 5,`<br>```"provider_goods_no"``: null,`<br>```"rec_id"``: 9,`<br>```"spec_name"``:``""``,`<br>```"spec_no"``:``"62901"``,`<br>```"unit_id"``: 0,`<br>```"unit_name"``:``"无"`<br>```},`<br>```{`<br>```"aux_num"``: 2.0,`<br>```"barcode"``:``""``,`<br>```"base_unit_id"``: 0,`<br>```"base_unit_name"``:``"无"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``: null,`<br>```"brand_id"``: null,`<br>```"brand_name"``:``"无"``,`<br>```"class_id"``: null,`<br>```"class_name"``:``"无"``,`<br>```"expire_date"``: null,`<br>```"goods_name"``: null,`<br>```"goods_no"``: null,`<br>```"num"``: 2.0,`<br>```"pre_order_id"``: 5,`<br>```"provider_goods_no"``: null,`<br>```"rec_id"``: 10,`<br>```"spec_name"``:``"默认规格"``,`<br>```"spec_no"``:``"62903"``,`<br>```"unit_id"``: 0,`<br>```"unit_name"``:``"无"`<br>```}`<br>```],`<br>```"flag_id"``: 0,`<br>```"flag_name"``:``"无"``,`<br>```"modified"``:``"2024-04-28 09:52:45"``,`<br>```"pre_order_id"``: 5,`<br>```"pre_order_no"``:``"YD202404150009"``,`<br>```"provider_id"``: 0,`<br>```"status"``: 30,`<br>```"telno"``:``""`<br>```}`<br>```],`<br>```"total_count"``: 30`<br>```},`<br>```"status"``: 0`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"未知错误1"``,`<br>```"status"``: 5`<br>`}` | |
