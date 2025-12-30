---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Base.search"
title: "API文档"
---
**wms.stockin.Base.search** **（入库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP入库单单据信息 |
| **1.2 适用版本：** 客户端 V1.5.6.8及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** 起止时间跨度不超过1天 |
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
| 开始时间 | start\_time | String | 40 | Y | 修改时间，时间格式 YYYY-MM-DD HH:MM:SS |
| 结束时间 | end\_time | String | 40 | Y | 修改时间，时间格式 YYYY-MM-DD HH:MM:SS |
| 单据类型 | order\_type | Byte |  | N | 2：调拨<br>4：盘点<br>5：生产原料<br>6：生产成品<br>8：正残转换<br>10：采购单<br>13：jit退货入库<br>20：其它入库<br>23：外仓调整入库<br>33：初始化入库 |
| 状态 | status | Byte |  | N | 10：已取消<br>20：编辑中<br>30：待审核<br>37：待质检<br>40：质检确认<br>80：已完成 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 源单号 | src\_order\_no | String | 40 | N | 源单号 |
| 入库单号 | stockin\_no | String | 40 | N | 入库单号 |

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
| 单据数据 | data | Map<String, Object> |  | Y | 入库单相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | Y | 入库单相关数据 |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 审核时间 | check\_time | String |  | Y | 审核时间，YYYY-MM-DD HH:MM:SS格式 |
| 创建时间 | created | String |  | Y | 创建时间，YYYY-MM-DD HH:MM:SS格式 |
| 标记id | flag\_id | Int | 11 | Y | 标记id |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 货品种类数量 | goods\_type\_count | Short |  | Y | 货品种类数量 |
| 物流id | logistics\_id | Int | 11 | Y | 物流id |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间，YYYY-MM-DD HH:MM:SS格式 |
| 便签数量 | note\_count | Short | 6 | Y | 便签数量 |
| 经办人 | operator\_id | Int | 11 | Y | 经办人 |
| 备注 | remark | String | 255 | Y | 备注 |
| 源单id | src\_order\_id | Int |  | Y | 源单id |
| 源单号 | src\_order\_no | String | 40 | Y | 源单号 |
| 源单类型 | src\_order\_type | Byte | 4 | Y | 源单类型<br>2：调拨<br>4：盘点<br>5：生产原料<br>6：生产成品<br>8：正残转换<br>10：采购单<br>20：其它入库<br>23：外仓调整入库<br>33：初始化入库 |
| 状态 | status | Byte | 4 | Y | 状态<br>10：已取消<br>20：编辑中<br>30：待审核<br>37：待质检<br>40：质检确认<br>80：已完成 |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单id |
| 入库单号 | stockin\_no | String | 40 | Y | 入库单号 |
| 仓库id | warehouse\_id | Int |  | Y | 仓库id |
| 仓库编号 | warehouse\_no | String |  | Y | 仓库编号 |
| 仓库名称 | warehouse\_name | String |  | Y | 仓库名称 |
| 物流类型 | logistics\_type | Short |  | Y | 物流类型， [点击查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) 代码表 |
| 操作员名称 | operator\_name | String |  | Y | 操作员名称 |
| 入库明细 | detail\_list | List<Map<String, Object>> |  | Y | 入库明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务单明细id | src\_order\_detail\_id | Int | 11 | Y | 业务单明细id |
| 调整数量 | adjust\_num | Decimal(19,4) |  | Y | 调整数量 |
| 基本单位 | base\_unit\_id | Short | 6 | Y | 基本单位 |
| 批次id | batch\_id | Int | 11 | Y | 批次id |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 创建时间 | created | String |  | Y | 创建时间 |
| 预期数量 | expect\_num | Decimal(19,4) |  | Y | 预期数量 |
| 有效期 | expire\_date | String |  | Y | 有效期 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品单位名称 | goods\_unit\_name | String | 20 | Y | 优先取单品单位，为空则取货品单位 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间 |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | Y | 辅助数量 |
| 源单明细id | org\_stockin\_detail\_id | Int | 11 | Y | 源单明细id |
| 货位id | position\_id | Int | 11 | Y | 货位id |
| 货位 | position\_no | String |  | Y | 货位 |
| 生产日期 | production\_date | String |  | Y | 生产日期 |
| 明细rec\_id | rec\_id | Int | 11 | Y | 明细rec\_id |
| 备注 | remark | String |  | Y | 备注 |
| 规格编码 | spec\_code | String |  | Y | 规格编码 |
| 商家编码 | spec\_no | String |  | Y | 商家编码 |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 规格名称 | spec\_name | String |  | Y | 规格名称 |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单id |
| 单位id | unit\_id | Short | 6 | Y | 单位id |
| 单位系数 | unit\_ratio | Decimal(19,4) |  | Y | 单位系数 |
| 有效期天数 | validity\_days | Short | 6 | Y | 有效期天数 |
| 批次号 | batch\_no | String |  | Y | 批次号 |
| 批次备注 | batch\_remark | String |  | Y | 批次备注 |
| 辅助单位 | aux\_unit\_name | String | 20 | Y | 辅助单位 |
| 是否残次品 | defect | Int |  | Y | 是否残次品<br>0：正品<br>1：残次品 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2023-01-11 18:18:21"``,`<br>```"start_time"``:``"2023-01-11 17:18:21"`<br>```}`<br>`]` | |
| php 请求示例 | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2023-01-11 17:18:21'``;`<br>`$params``->end_time =``'2023-01-11 18:18:21'``;`<br>`$data``=``$client``->pageCall(``"wms.stockin.Base.search"``,``$pager``,``$params``);`<br>``<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order_list"``: [{`<br>```"flag_id"``: 0,`<br>```"stockin_id"``: 90763,`<br>```"logistics_no"``:``""``,`<br>```"src_order_id"``: 9100,`<br>```"operator_id"``: 585,`<br>```"created"``:``"2023-06-08 09:59:50"``,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 214244,`<br>```"stockin_id"``: 90763,`<br>```"num"``: 1,`<br>```"num2"``: 0.1111,`<br>```"unit_id"``: 58,`<br>```"unit_ratio"``: 9,`<br>```"unit"``: 34,`<br>```"expect_num"``: 1,`<br>```"validity_days"``: 0,`<br>```"remark"``:``""``,`<br>```"adjust_num"``: 0,`<br>```"brand_no"``:``"111"``,`<br>```"brand_name"``:``"小苹果"``,`<br>```"goods_name"``:``"美国原装进口rumbatime手表女正品腕表女石英表防水宝石时尚"``,`<br>```"goods_no"``:``"daba1"``,`<br>```"spec_id"``: 152515,`<br>```"spec_name"``:``"默认规格"``,`<br>```"spec_code"``:``"红宝石"``,`<br>```"batch_id"``: 0,`<br>```"batch_no"``:``""``,`<br>```"batch_remark"``:``""``,`<br>```"position_id"``: -2,`<br>```"position_no"``:``"采购未上架"``,`<br>```"spec_no"``:``"daba1"``,`<br>```"org_stockin_detail_id"``: 0,`<br>```"src_order_detail_id"``: 0,`<br>```"modified"``:``"2023-06-08 09:59:58"``,`<br>```"created"``:``"2023-06-08 09:59:50"``,`<br>```"production_date"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"aux_unit_name"``:``"南9"``,`<br>```"goods_unit_name"``:``"南"`<br>```}],`<br>```"src_order_type"``: 10,`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"goods_count"``: 1,`<br>```"src_order_no"``:``"CG23060803"``,`<br>```"logistics_id"``: 0,`<br>```"operator_name"``:``"aaa"``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"stockin_no"``:``"RK2023060822"``,`<br>```"modified"``:``"2023-06-08 09:59:58"``,`<br>```"logistics_type"``: -1,`<br>```"note_count"``: 0,`<br>```"status"``: 80,`<br>```"warehouse_id"``: 624,`<br>```"check_time"``:``"2023-06-08 09:59:58"`<br>```}]`<br>```}`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"您的查询时间过宽,查询时间不能大于1天"``,`<br>```"status"``: 100`<br>`}` | |
