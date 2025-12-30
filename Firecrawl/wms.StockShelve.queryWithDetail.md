---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockShelve.queryWithDetail"
title: "API文档"
---
**wms.StockShelve.queryWithDetail** **（补货单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP库存变化信息 |
| **1.2 适用版本：** 客户端 V1.4.4.9及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** |

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
| 开始时间 | start\_time | String | 40 | N | 开始时间(最后更新时间) |
| 结束时间 | end\_time | String | 40 | N | 结束时间(最后更新时间) |
| 商家编码 | spec\_no | String | 40 | N | 商家编码 |
| 补货单号 | order\_no | String | 40 | N | 补货单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 类型 | type | Int | 4 |  | 0通用，1下架，2上架，3预补 |

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
| 单据数据 | data | Map<String, Object> |  | N | 单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String,   Object>> |  | Y | 库存信息列表 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 补货单号 | order\_no | String | 40 | Y | 补货单号 |
| 源货区 | to\_zone\_no | String | 20 | Y | 源货区 |
| 仓库 | warehouse\_no | String | 40 | Y | 仓库 |
| 目标货区 | from\_zone\_no | String | 20 | Y | 目标货区 |
| 状态 | status | Int | 4 | Y | 0已取消 10待审核 20已审核 30已完成 |
| 类型 | type | Int | 4 | Y | 0通用，1下架，2上架，3预补 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 修改时间 | modified | String | 255 | Y | 修改时间 |
| 操作员 | operator\_name | String | 50 | Y | 操作员 |
| 补货单明细 | detail\_list | List<Map<String, Object>> |  | Y | 补货单明细 |

****detailList****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 补货单ID | order\_id | Int | 11 | Y | 补货单ID |
| 单品ID | spec\_id | Int | 11 | Y | 单品ID |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 补货车框位 | cart\_seat | Int | 11 | Y | 补货车框位 |
| 有效期 | expire\_date | String | 40 | Y | 有效期 |
| 下架数量 | down\_num | Decimal(19,4) |  | Y | 下架数量 |
| 上架数量 | up\_num | Decimal(19,4) |  | Y | 上架数量 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 源货位 | from\_position\_no | String | 50 | Y | 源货位 |
| 目标货位 | to\_position\_no | String | 50 | Y | 目标货位 |
| 是否残品 | defect | bool | 1 | Y | 是否残品 |
| 简称 | short\_name | String | 255 | Y | 简称 |
| 单品名称 | spec\_name | String | 100 | Y | 单品名称 |
| 条码 | barcode | String | 50 | Y | 条码 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockShelve.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockShelve.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockShelve.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockShelve.queryWithDetail#autoTab5_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_date"``:``"2020-01-01 00:00:00"``,`<br>`"end_date"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>`$parMap``->warehouse_no =``"lz"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"wms.StockShelve.queryWithDetail"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockShelve.queryWithDetail#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"order_no"``:``"BH202009070003"``,`<br>```"operator_name"``:``"罗昭伦"``,`<br>```"to_zone_no"``:``"J"``,`<br>```"warehouse_no"``:``"lzl"``,`<br>```"from_zone_no"``:``"B"``,`<br>```"created"``: 1599458476000,`<br>```"detail_list"``: [{`<br>```"order_id"``: 1316,`<br>```"spec_id"``: 183958,`<br>```"cart_seat"``: 0,`<br>```"expire_date"``:``""``,`<br>```"down_num"``: 1,`<br>```"up_num"``: 0,`<br>```"from_position_no"``:``"B01-01-01"``,`<br>```"to_position_no"``:``"J01-01-01"``,`<br>```"defect"``:``false``,`<br>```"goods_name"``:``"C语言程序设计，面向过程语言，学会了也没对象,学会了也没对象,学会了也没对象"``,`<br>```"short_name"``:``"C语言程序设计"``,`<br>```"goods_no"``:``"book1"``,`<br>```"spec_code"``:``"book1_ggm"``,`<br>```"spec_name"``:``"book1_ggm这是规格名称的位置"``,`<br>```"spec_no"``:``"book1"``,`<br>```"barcode"``:``"book1"`<br>```}],`<br>```"modified"``: 1599458476000,`<br>```"type"``: 3,`<br>```"status"``: 30`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockShelve.queryWithDetail#autoTab6_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``:100,`<br>```"message"``:``"请指定仓库"`<br>`}` |
