---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterOut.queryWithDetail"
title: "API文档"
---
**wms.outer.OuterOut.queryWithDetail（** **外仓调整出库单查询 ）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP外仓调整出库信息 |
| **1.2 适用版本：** 客户端 V1.6.0.10及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限**<br>传入参数如果没有出库单号，就必须传入时间，和时间类型作为参数 |

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
| 出库单号 | outer\_out\_no | String | 40 | Y | 出库单号 |
| 仓库编号 | warehouse\_no | String | 40 | N | 出库仓库编号 |
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无出库单编号，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int | 4 | N | 时间判断的类型，1为建单时间，2为修改时间，默认为建单时间 |
| 物流单号 | logistics\_no | String | 40 | N | 物流单号 |
| 出库类型 | order\_type | Int | 4 | N | 出库类型<br>0，调整出库<br>2，调拨出库<br>4，盘点出库<br>14，采购退货出库 |
| 状态 | status | String | 4 | N | 用逗号分隔开数字的字符串，状态码<br>10，已取消<br>20，编辑中<br>30，待审核<br>40，待结算<br>50，已完成 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小不能超过2000 |
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
| 调整出库单 | order | List<Map<String, Object>> |  | Y | 调整出库单数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**Order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调整出库单id | rec\_id | Int | 11 | Y | 调整出库单id |
| 出库单号 | outer\_out\_no | String | 40 | Y | 出库单号 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 出库的仓库名称 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 物流公司 | logistics\_name | String | 20 | Y | 物流公司名称 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 货品种类数 | goods\_type\_count | Int | 6 | Y | 货品种类数 |
| 出库单状态 | status | Int | 4 | Y | 10，已取消<br>20，编辑中<br>30，待审核<br>40，待结算<br>50，已完成 |
| 出库原因 | reason | String | 255 | Y | 出库原因 |
| 建单人 | creator\_name | String | 40 | Y | 建单人 |
| 出库单源单据类型 | src\_order\_type | Int | 4 | Y | 0，调整出库<br>2，调拨出库<br>4，盘点出库<br>14，采购退货出库 |
| 出库单源单号 | src\_order\_no | String |  | Y | 出库单源单号 |
| 备注 | remark | String | 255 | Y | 备注 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 出库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 出库单明细信息 |

**d** **etail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调整出库单明细id | rec\_id | Int | 11 | Y | 调整出库单明细id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品编码 | goods\_no | String | 40 | Y | 货品编码 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 条码 | barcode | String | 50 | Y | 条码 |
| 出库数量 | num | Decimal(19,4) |  | Y | 出库数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | Y | 辅助数量 |
| 是否残次品 | defect | bool | 1 | Y | true：残次品<br>false：正品 |
| 备注 | remark | String | 255 | Y | 备注 |
| 换算系数 | unit\_ratio | Decimal(19,4) |  | Y | 换算系数 |
| 辅助单位 | aux\_unit\_name | String | 20 | Y | 辅助单位 |
| 单位 | base\_unit\_name | String | 20 | Y | 单位 |
| 批次号 | batch\_no | String | 50 | Y | 批次号 |
| 有效期 | expire\_date | String |  | Y | 有效期，格式：yyyy-MM-dd HH:mm:ss |
| 货品类别 | goods\_type | Byte | 4 | Y | 0: 其他<br>1: 销售货品<br>2: 原料<br>3: 包材<br>4: 周转材料<br>5: 虚拟产品<br>6: 固定字长<br>8: 入库装箱<br>9: 周期送货品 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[{`<br>`"outer_out_no"``:``"WO202008180002"``,`<br>`"warehouse_no"``:``"lh003"``,`<br>```"logistics_no"``:``"lich0313"``,`<br>```"time_type"``: 2,`<br>```"status"``:``"10,12"``,`<br>```"start_time"``:``"2020-06-15 10:05:36"``,`<br>```"end_time"``:``"2020-06-17 11:05:36"`<br>`}]` | |
| php 请求示例 | |     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>``<br>`$par``=``array`<br>`(`<br>`'outer_out_no'``=>``'WO202008180002'``,`<br>`'warehouse_no'``=>``'lh003'``,`<br>```'logistics_no'``=>``'lich0313'``,`<br>```'time_type'``=> 2,`<br>```'status'``=>``'10,20,30'``,`<br>```'start_time'``=>``'2020-06-15 10:05:36'``,`<br>```'end_time'``=>``'2020-06-17 11:05:36'`<br>`);`<br>`$pager``=``new``Pager(50, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.outer.OuterOut.queryWithDetail"``,``$pager``,``$par``);``//分页方法`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>``<br>`?>` | |
| JAVA | |     |     |
| --- | --- |
| 1 | `<br>` | |
| C# | |     |     |
| --- | --- |
| 1 | `<br>` | |

**6.响应示例**

**6.1正常响应示例**

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"logistics_name"``:``"无"``,`<br>```"reason"``:``"无"``,`<br>```"logistics_no"``:``""``,`<br>```"created"``:``"2023-08-15 14:02:14"``,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 4974,`<br>```"goods_name"``:``"外仓批次货品"``,`<br>```"goods_no"``:``"wcpc"``,`<br>```"spec_no"``:``"wcpc3"``,`<br>```"spec_code"``:``"wcpc3"``,`<br>```"spec_name"``:``"wcpc3"``,`<br>```"barcode"``:``"wcpc3"``,`<br>```"num"``: 1,`<br>```"defect"``:``false``,`<br>```"unit_ratio"``: 1,`<br>```"num2"``: 0,`<br>```"remark"``:``""``,`<br>```"batch_no"``:``"PC2305240001"``,`<br>```"aux_unit_name"``:``"无"``,`<br>```"base_unit_name"``:``"无"``,`<br>```"expire_date"``:``"2023-05-18 00:00:00"`<br>```}],`<br>```"goods_type_count"``: 1,`<br>```"src_order_type"``: 4,`<br>```"remark"``:``"WP202308150005 盘亏出库"``,`<br>```"goods_count"``: 1,`<br>```"rec_id"``: 723,`<br>```"outer_out_no"``:``"WO202308150004"``,`<br>```"src_order_no"``:``""``,`<br>```"warehouse_name"``:``"wmslt旺店通联调仓库"``,`<br>```"warehouse_no"``:``"wms_lt_erp30"``,`<br>```"modified"``:``"2023-08-15 14:02:14"``,`<br>```"creator_name"``:``"朱鑫尧"``,`<br>```"status"``: 40`<br>```}]`<br>```}`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` | |
