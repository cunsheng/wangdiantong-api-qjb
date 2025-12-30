---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Base.search"
title: "API文档"
---
**wms.stockout.Base.search** **（出库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP非销售类型出库单单据信息 |
| **1.2 适用版本：** 客户端 V1.5.6.8及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** 起止时间跨度不超过60分钟 |
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
| 单据类型 | order\_type | Byte |  | N | 2：调拨出库<br>4：盘点出库<br>5：生产出库<br>8：正残转换出库<br>9：jit出库<br>14：采购退货<br>21：其它出库<br>24：外仓调整出库<br>34：初始化出库 |
| 状态 | status | Byte |  | N | 5：已取消<br>10：待放回<br>48：未确认<br>50：待审核<br>51：缺货<br>53：wms已接单<br>54：获取面单<br>58：档口锁定<br>60：待分配<br>61：排队中<br>63：待补货<br>65：待处理<br>70：待发货<br>73：爆款锁定<br>75：待拣货<br>77：拣货中<br>79：已拣货<br>90：延时发货<br>110：已完成 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 源单号 | src\_order\_no | String | 40 | N | 源单号 |
| 出库单号 | stockout\_no | String | 40 | N | 出库单号，传入单号可不传时间 |

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
| 单据数据 | data | Map<String, Object> |  | Y | 出库单相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | Y | 出库单相关数据 |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 预估邮费 | calc\_post\_cost | Decimal(19,4) |  | Y | 预估邮费 |
| 预估重量 | calc\_weight | Decimal(19,4) |  | Y | 预估重量 |
| 审核时总成本 | checked\_goods\_total\_cost | Decimal(19,4) |  | Y | 审核时总成本 |
| 发货状态 | consign\_status | Int | 11 | Y | 发货状态<br>1：已验货<br>2：已称重<br>16：已拣货<br>32：电子面单回传<br>64：已分拣<br>128：配送清单打印<br>4096：订单回告 |
| 发货时间 | consign\_time | String |  | Y | 发货时间 |
| 创建时间 | created | String |  | Y | 创建时间 |
| 其他出库自定义子类别 | custom\_type | Int | 6 | Y | 其他出库自定义子类别 |
| 错误信息 | error\_info | String | 255 | Y | 错误信息 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 货品种类数量 | goods\_type\_count | Int |  | Y | 货品种类数量 |
| 物流公司编号 | logistics\_company\_no | String |  | Y | 物流公司编号 |
| 物流id | logistics\_id | Int | 11 | Y | 物流id |
| 物流公司名称 | logistics\_name | String |  | Y | 物流公司名称 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 物流类型 | logistics\_type | Short |  | Y | 物流类型， [点击查看物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) |
| 最后修改时间 | modified | String |  | Y | 最后修改时间 |
| 操作员id | operator\_id | Int | 11 | Y | 操作员id |
| 操作员 | operator\_name | String | 50 | Y | 操作员 |
| 收件人城市 | receiver\_city | Int | 11 | Y | 收件人城市， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 收件人国家 | receiver\_country | Int | 6 | Y | 收件人国家， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 收件人区 | receiver\_district | Int | 11 | Y | 收件人区， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 收件人省 | receiver\_province | Int | 11 | Y | 收件人省， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 收件人邮编 | receiver\_zip | String | 20 | Y | 收件人邮编 |
| 备注 | remark | String | 1024 | Y | 备注 |
| 源单id | src\_order\_id | Int | 11 | Y | 源单id |
| 源单单号 | src\_order\_no | String | 40 | Y | 源单单号 |
| 单据类型 | src\_order\_type | Byte |  | Y | 单据类型<br>2：调拨出库<br>4：盘点出库<br>5：生产出库<br>8：正残转换出库<br>14：采购退货<br>21：其它出库<br>24：外仓调整出库 |
| 出库单状态 | status | Byte |  | Y | 出库单状态<br>5：已取消<br>10：待放回<br>48：未确认<br>50：待审核<br>51：缺货<br>53：wms已接单<br>54：获取面单<br>58：档口锁定<br>60：待分配<br>61：排队中<br>63：待补货<br>65：待处理<br>70：待发货<br>73：爆款锁定<br>75：待拣货<br>77：拣货中<br>79：已拣货<br>90：延时发货<br>110：已完成 |
| 出库单id | stockout\_id | Int |  | Y | 出库单id |
| 出库单号 | stockout\_no | String | 40 | Y | 出库单号 |
| 仓库id | warehouse\_id | Short |  | Y | 仓库id |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库类型 | warehouse\_type | Byte |  | Y | 仓库类型<br>1：普通仓<br>2：自流转<br>3：奇门<br>4：京东沧海<br>6：抖音云仓<br>125：代发<br>126：分销 |
| 称重邮资 | weigh\_post\_cost | Decimal(19,4) |  | Y | 称重邮资 |
| 重量 | weight | Decimal(19,4) |  | Y | 重量 |
| 出库明细 | detail\_list | List<Map<String, Object>> |  | Y | 出库明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 批次id | batch\_id | Int | 11 | Y | 批次id |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 批次备注 | batch\_remark | String | 128 | Y | 批次备注 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 审核时成本 | checked\_cost\_price | Decimal(19,4) |  | Y | 审核时成本 |
| 货品id | goods\_id | Int | 11 | Y | 货品id |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品类型 | goods\_type | Byte | 4 | Y | 货品类型<br>0：其他<br>1：销售货品<br>2：原料<br>3：包材<br>4：周转材料<br>5：虚拟产品<br>6：固定资产<br>8：入库装箱<br>9：周期送货品 |
| 是否包装 | is\_package | boolean |  | Y | 是否包装 |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 货位id | position\_id | Int | 11 | Y | 货位id |
| 货位编号 | position\_no | String | 20 | Y | 货位编号 |
| 明细rec\_id | rec\_id | Int | 11 | Y | 明细rec\_id |
| 明细备注 | remark | String | 255 | Y | 明细备注 |
| 扫描类型 | scan\_type | Byte | 4 | Y | 0：未验货<br>5：图片验货 |
| 规格编码 | spec\_code | String | 40 | Y | 规格编码 |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 出库单id | stockout\_id | Int | 11 | Y | 出库单id |
| 单位名称 | unit | String | 20 | Y | 优先取单品单位，为空则取货品单位 |
| 单位id | unit\_id | Short |  | Y | 单位id |
| 有效期 | expire\_date | String |  | Y | 有效期 |
| 重量 | weight | Decimal(19,4) |  | Y | 重量 |
| 源单明细id | src\_order\_detail\_id | Int | 11 | Y | 源单明细id |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 修改时间 | modified | String | 40 | Y | 修改时间 |
| 单位换算系数 | unit\_ratio | Decimal(19,4) |  | Y | 单位换算系数 |
| 辅助单位 | aux\_unit\_name | String | 20 | Y | 辅助单位 |
| 辅助单位id | aux\_unit\_id | Int |  | Y | 辅助单位id |
| 是否残次品 | defect | Int |  | Y | 是否残次品<br>0：正品<br>1：残次品 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2023-01-11 18:18:21"``,`<br>```"start_time"``:``"2023-01-11 17:18:21"`<br>```}`<br>`]` | |
| php 请求示例 | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2023-01-11 17:18:21'``;`<br>`$params``->end_time =``'2023-01-19 18:18:21'``;`<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.Base.search"``,``$pager``,``$params``);`<br>``<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order_list"``: [{`<br>```"logistics_name"``:``""``,`<br>```"consign_time"``:``"2023-04-24 10:08:11"``,`<br>```"warehouse_type"``: 1,`<br>```"error_info"``:``""``,`<br>```"custom_type"``: 0,`<br>```"receiver_city"``: 0,`<br>```"operator_id"``: 585,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 2852889,`<br>```"stockout_id"``: 1637150,`<br>```"spec_id"``: 1,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"num"``: 1,`<br>```"brand_no"``:``"ffl"``,`<br>```"brand_name"``:``"发发拉"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_name"``:``"暂无"``,`<br>```"spec_code"``:``"LL "``,`<br>```"checked_cost_price"``: 5,`<br>```"weight"``: 0.2,`<br>```"remark"``:``""``,`<br>```"unit_id"``: 31,`<br>```"unit_ratio"``: 33,`<br>```"aux_unit_id"``: 577,`<br>```"batch_no"``:``""``,`<br>```"batch_remark"``:``""``,`<br>```"goods_type"``: 1,`<br>```"position_id"``: -8,`<br>```"position_no"``:``"销退质检"``,`<br>```"goods_id"``: 1,`<br>```"batch_id"``: 0,`<br>```"is_package"``:``false``,`<br>```"scan_type"``: 0,`<br>```"src_order_detail_id"``: 0,`<br>```"unit"``:``"口"``,`<br>```"aux_unit_name"``:``"锅"``,`<br>```"expire_date"``:``""``,`<br>```"created"``:``"2023-04-24 10:08:11"``,`<br>```"modified"``:``"2023-04-24 10:08:11"`<br>```}],`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"goods_count"``: 1,`<br>```"calc_post_cost"``: 0,`<br>```"stockout_id"``: 1637150,`<br>```"src_order_no"``:``"ZC202304240001"``,`<br>```"logistics_id"``: 0,`<br>```"receiver_zip"``:``""``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"checked_goods_total_cost"``: 5,`<br>```"modified"``:``"2023-04-24 10:08:11"``,`<br>```"receiver_country"``: 0,`<br>```"calc_weight"``: 0,`<br>```"logistics_type"``: -1,`<br>```"receiver_province"``: 0,`<br>```"logistics_no"``:``""``,`<br>```"src_order_id"``: 260,`<br>```"created"``:``"2023-04-24 10:08:11"``,`<br>```"stockout_no"``:``"CH2023042427"``,`<br>```"src_order_type"``: 8,`<br>```"receiver_district"``: 0,`<br>```"weight"``: 0,`<br>```"logistics_company_no"``:``""``,`<br>```"operator_name"``:``"aaa"``,`<br>```"weigh_post_cost"``: 0,`<br>```"warehouse_id"``: 624,`<br>```"status"``: 110,`<br>```"consign_status"``: 0`<br>```}]`<br>```}`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"您的查询时间过宽,查询时间不能大于60分钟"``,`<br>```"status"``: 100`<br>`}` | |
