---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryHisWithDetail"
title: "API文档"
---
****wms.stockin.Refund.queryHisWithDetail** **（历史退货入库单查询）****

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的历史退货入库单单据信息 |
| **1.2 适用版本：** 客户端 V1.4.5.3及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：** **【权限校验】：仓库权限，店铺权限** <br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台数据， **淘系**相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")，拼多多请自行对接平台获取。<br>本接口中涉及到用户隐私的字段数据仅自有平台及线下平台订单返回。具体字段详情见下面表格； |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 客户网名 | nick\_name |
| 客户姓名 | customer\_name |

**2.调用场** **景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

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
| 查询参数 | params | Map<String, Object> |  | y | 查询参数 |
| 分页 | pager | pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | n | 仓库编号 |
| 入库单号 | stockin\_no | String | 20 | n | 入库单号 |
| 退换单号 | refund\_no | String | 40 | n | 退换单号 |
| 店铺编号 | shop\_nos | String | 255 | n | 多个编号间使用英文逗号分隔 |
| 入库单状态 | status | String | 255 | n | 英文逗号拼接的状态值:<br>10=已取消；20=编辑中；30=待审核/待处理；80=已完成 |
| 时间条件类型 | time\_type | Int | 1 | n | 查询的时间条件类型, 0:修改时间; 1:入库时间 不传默认为0 |
| 开始时间 | start\_time | String | 40 | y | 起始时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | y | 结束时间, yyyy-MM-dd HH:mm:ss格式 |
| 是否使用从库查询 | is\_slave | boolean | 1 | n | 使用：true  不使用：false<br>（仅对开通从库配置客户生效） |
| 是否返回sn信息 | need\_sn | boolean | 1 | n | 返回：true<br>不返回：false |

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
| 退货入库单信息 | data | Map<String, Object> |  | n | 退货入库信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据仅自有平台及线下平台返回，其他平台均不返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | y | 入库单相关数据 |
| 总数 | total\_count | Int | 11 | n | 查询条件总数单据 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单号 | order\_no | String | 40 | y | 入库单号 |
| 入库单状态 | status | Int | 4 | y | 入库单状态<br>10:已取消；20:编辑中；30:待处理/待审核；80:已完成 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | y | 仓库名称 |
| 制单时间 | created\_time | String | 40 | y | 入库单创建时间（毫秒级时间戳，例如：1631861379000） |
| 备注 | remark | String | 255 | y | 备注 |
| 分销商昵称 | fenxiao\_nick | String | 40 | y | 分销商昵称 |
| 入库人 | operator\_name | String | 40 | y | 入库人 |
| 入库人id | operator\_id | Int |  | y | 入库人id |
| 物流方式 | logistics\_type | Int | 6 | y | 物流方式，点击查看 [物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) |
| 物流公司 | logistics\_name | String | 40 | y | 物流公司名称 |
| 物流单号 | logistics\_no | String | 40 | y | 物流单号 |
| 物流id | logistics\_id | Int | 6 | y | 物流公司唯一键 |
| 审核时间 | check\_time | String | 40 | y | 审核时间（毫秒级时间戳，例如：1631861379000） |
| 退换单号 | refund\_no | String | 40 | y | 退换单号 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量 |
| 退换单实际退款金额 | actual\_refund\_amount | Decimal(19,4) |  | y | 退换单实际退款金额 |
| 客户编码 | customer\_no | String | 40 | y | 客户编码 |
| 退货人姓名 | customer\_name | String | 100 | y | 退货人姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 客户网名 | nick\_name | String | 100 | y | 客户网名（仅自有平台及线下平台返回，其他平台均不返回） |
| 店铺名称 | shop\_name | String | 128 | y | 店铺名称 |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺备注 | shop\_remark | String | 255 | y | 店铺备注 |
| 标记名称 | flag\_name | String | 32 | y | 标记名称 |
| 系统订单编号 | trade\_no\_list | String | 255 | y | 系统订单编号，若为多个以“，”分割，超长会被截取 |
| 原始单号 | tid\_list | String | 255 | y | 原始单号，若为多个以“，”分割，超长会被截取 |
| 退换单id | src\_order\_id | Int | 11 | y | 退换单主键 |
| 入库单id | stockin\_id | Int | 11 | y | 入库单id |
| 店铺平台id | shop\_platform\_id | Int | 6 | y | 店铺平台id，点击 [文档](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看平台id对照表 |
| 子平台id | sub\_platform\_id | Int | 6 | y | 子平台id |
| 店铺id | shop\_id | Int | 6 | y | 店铺唯一键 |
| 仓库id | warehouse\_id | Int | 40 | y | 仓库唯一键 |
| 入库单总成本 | total\_price | Decimal(19,4) |  | y | 入库单总成本<br>子单明细total\_cost的总和 |
| 货品入库总数量 | total\_goods\_stockin\_num | Decimal(19,4) |  | y | 货品入库总数量 |
| 退换单状态 | process\_status | Int | 4 | y | 10:已取消;20:待审核;30:已审核;80:已结算;85:待过账;86:已过账;87:成本确认;90:已完成 |
| 修改时间 | modified | String | 40 | y | 退货入库单修改时间, 样例: 2020-04-23 14:55:08 |
| 审核人 | check\_operator\_name | String | 40 | y | 审核人 |
| 审核人id | check\_operator\_id | Int |  | y | 审核人id |
| 退换说明 | reason | String | 40 | y | 退换说明 |
| 退换说明id | reason\_id | Int |  | y | 退换说明id |
| 入库总金额 | refund\_amount | Decimal(19,4) |  | y | 入库单明细退款金额之和 |
| 调整数量 | adjust\_num | Decimal(19,4) |  | y | 调整数量 |
| 创建时间 | created | String |  | y | 创建时间 |
| 标记id | flag\_id | Int | 6 | y | 标记id |
| 货品类型数量 | goods\_type\_count | Int | 6 | y | 货品类型数量 |
| 退换单编号 | src\_order\_no | String | 40 | y | 退换单编号 |
| 便签条数 | note\_count | Int | 6 | y | 便签条数 |
| 业务单类型 | src\_order\_type | Int | 4 | y | 业务单类型，固定12 |
| 入库单明细 | details\_list | List<Map<String, Object>> |  | y | 入库单明细 |

****details\_list****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单明细id(主键) | rec\_id | Int | 11 | 是 | 入库单明细ID（主键） |
| 入库单id | stockin\_id | Int | 11 | 是 | 入库单ID |
| 退换单明细id | refund\_detail\_id | String | 100 | 是 | 退换单明细id,id之间用逗号分隔 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 总成本 | total\_cost | Decimal(19,4) |  | 是 | 总成本=明细数量\*成本（以系统配置决定是实际成本/计划成本） |
| 明细备注 | remark | String | 255 | 是 | 明细备注 |
| 调整后数量 | right\_num | Decimal(19,4) |  | 是 | 调整后数量 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品编码 | goods\_no | String | 40 | 是 | 货品编码 |
| 货品id | goods\_id | Int |  | 是 | 货品唯一键 |
| 商品id | spec\_id | Int |  | 是 | 单品唯一键 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 是否残次品 | defect | boolean | 1 | 是 | 默认为非残次品 |
| 单品自定义属性2 | prop2 | String | 100 | 是 | 单品自定义属性2（来源货品档案） |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 品牌编号 | brand\_no | String | 32 | 是 | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 辅助单位 | goods\_unit | String | 20 | 是 | 辅助单位（入库单对应的辅助单位） |
| 物流名称 | logistics\_name | String | 40 | 是 | 物流名称 |
| 物流单号 | logistics\_no | String | 40 | 是 | 物流单号 |
| 仓库id | warehouse\_id | Int | 40 | 是 | 仓库唯一键 |
| 退换单id | src\_order\_id | Int | 6 | 是 | 退换单主键 |
| 物流id | logistics\_id | Int | 6 | 是 | 物流公司唯一键 |
| 单位 | base\_unit\_name | String | 20 | 是 | 基本单位 |
| 批次号 | batch\_no | String | 40 | 是 | 批次号 |
| 有效期 | expire\_date | String | 40 | 是 | 有效期，样例: 2020-04-20 00:00:00 |
| 生产日期 | production\_date | String | 40 | 是 | 生产日期 |
| 货位 | position\_no | String | 20 | 是 | 货位 |
| 预期数量 | expect\_num | Decimal(19,4) |  | 是 | 预期数量 |
| 入库数量 | stockin\_num | Decimal(19,4) |  | 是 | 入库数量 |
| 入库单明细成本价 | checked\_cost\_price | Decimal(19,4) |  | 是 | 入库单明细成本价 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 退换管理明细货品价格\*入库数量 |
| sn序列号信息 | sn\_list | String | 255 | 是 | 当need\_sn=true时返回英文逗号分隔的sn |
| 入库单位id | unit\_id | Int | 6 | 是 | 入库单位id |
| 基本单位id | base\_unit\_id | Int | 6 | 是 | 基本单位id |
| 库存明细id | org\_stockin\_detail\_id | Int | 11 | 是 | 库存明细id |
| 批次id | batch\_id | Int | 11 | 是 | 批次id |
| 货位id | position\_id | Int | 11 | 是 | 货位id |
| 有效期天数 | validity\_days | Int | 6 | 是 | 有效期天数 |
| 辅助数量 | num2 | Decimal(19,4) |  | 是 | 辅助数量 |
| 调整数量 | adjust\_num | Decimal(19,4) |  | 是 | 调整数量 |
| 单位换算关系 | unit\_ratio | Decimal(19,4) |  | 是 | 单位换算关系 |
| 最后修改时间 | modified | String | 40 | 是 | 最后修改时间 |
| 创建时间 | created | String | 40 | 是 | 创建时间 |
| 业务单类型 | src\_order\_type | Int | 4 | 是 | 业务单类型，固定12 |
| 退换单明细 | refund\_order\_detail\_list | List<Map<String, Object>> |  | 是 | 退换单明细 |

**refund\_order\_detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单明细id | refund\_order\_id | Int | 11 | 是 | 退换单明细id |
| 入库单明细id | stockin\_order\_detail\_id | Int | 11 | 是 | 入库单明细id |
| 价格 | price | Decimal(19,4) |  | 是 | 价格（退换单明细价格字段） |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | ```<br>[{<br>"start_time": "2019-09-01 00:00:00",<br>"end_time": "2019-10-01 23:59:59"<br>}]<br>``` |
| PHP | ```<br><?php<br>header("Content-Type: text/html; charset=UTF-8");<br>date_default_timezone_set("Asia/Shanghai");<br>require_once('wdtsdk.php');<br> <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");<br> <br>$paraMap = new stdClass();<br>$paraMap->start_time = "2019-09-01 00:00:00";<br>$paraMap->end_time = "2019-10-01 23:59:59";<br> <br> <br>$pager = new Pager(1, 0, true);<br>$response = $client->pageCall("wms.stockin.Refund.queryHisWithDetail",$pager, $paraMap);<br> <br>?><br>``` |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>	"status": 0,<br>	"data": {<br>		"total_count": 1,<br>		"order": [{<br>			"logistics_name": "奇门中通001",<br>			"details_list": [{<br>				"stockin_id": 89138,<br>				"num": 1,<br>				"total_cost": 10,<br>				"remark": "批次:20230113",<br>				"right_num": 1,<br>				"rec_id": 211045,<br>				"goods_name": "lym测试货品B-批次",<br>				"goods_no": "lymhpB",<br>				"spec_no": "lymhpB03",<br>				"defect": false,<br>				"prop2": "",<br>				"spec_name": "批次03较晚",<br>				"spec_code": "",<br>				"batch_no": "20230113",<br>				"brand_no": "BRAND",<br>				"brand_name": "无",<br>				"unit_id": 0,<br>				"base_unit_id": 0,<br>				"expire_date": "",<br>				"position_no": "",<br>				"logistics_id": 98,<br>				"logistics_no": "202302060002",<br>				"src_order_id": 1129912,<br>				"warehouse_id": 783,<br>				"goods_id": 166908,<br>				"spec_id": 355229,<br>				"expect_num": 0,<br>				"checked_cost_price": 10,<br>				"org_stockin_detail_id": 0,<br>				"batch_id": 17591,<br>				"position_id": 0,<br>				"validity_days": 0,<br>				"num2": 1,<br>				"adjust_num": 0,<br>				"unit_ratio": 1,<br>				"modified": "2023-02-06 16:27:39",<br>				"created": "2023-02-06 16:27:39",<br>				"src_order_type": 12,<br>				"sn_list": "",<br>				"refund_order_detail_list": [{<br>					"refund_order_id": 1135829,<br>					"stockin_order_detail_id": 211045,<br>					"spec_no": "lymhpB03",<br>					"price": 0<br>				}],<br>				"goods_unit": "无",<br>				"base_unit_name": "无",<br>				"logistics_name": "奇门中通001",<br>				"refund_amount": "0.0000",<br>				"refund_detail_id": "1135829",<br>				"production_date": "",<br>				"stockin_num": "1.0000"<br>			}],<br>			"fenxiao_nick": "",<br>			"reason": "无",<br>			"operator_id": 0,<br>			"refund_no": "TK2302060008",<br>			"adjust_num": 0,<br>			"shop_remark": "",<br>			"modified": "2023-02-06 16:27:39",<br>			"shop_no": "DP-lym",<br>			"check_operator_name": "系统",<br>			"seq_no": 1,<br>			"created_time": 1675672059000,<br>			"stockin_id": 89138,<br>			"customer_no": "KH202112140012",<br>			"src_order_id": 1129912,<br>			"created": "2023-02-06 16:27:39",<br>			"trade_no_list": "JY20230206000050",<br>			"shop_name": "LYM店铺",<br>			"shop_platform_id": 0,<br>			"shop_id": "285",<br>			"warehouse_name": "wmslt旺店通联调仓库",<br>			"actual_refund_amount": "0.0000",<br>			"nick_name": "liz",<br>			"process_status": 90,<br>			"status": 80,<br>			"check_time": 1675672059000,<br>			"order_no": "RK2023020664",<br>			"flag_id": 0,<br>			"tid_list": "AT202302060006",<br>			"goods_type_count": 1,<br>			"remark": "LYM店铺",<br>			"sub_platform_id": 0,<br>			"goods_count": 1,<br>			"flag_name": "",<br>			"logistics_id": 98,<br>			"src_order_no": "TK2302060008",<br>			"warehouse_no": "wms_lt_erp30",<br>			"check_operator_id": 0,<br>			"refund_amount": 0,<br>			"logistics_type": 5,<br>			"note_count": 0,<br>			"total_price": 10,<br>			"logistics_no": "202302060002",<br>			"src_order_type": 12,<br>			"reason_id": 0,<br>			"operator_name": "系统",<br>			"total_goods_stockin_num": "1.0000",<br>			"customer_name": "",<br>			"warehouse_id": 783<br>		}]<br>	}<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "仓库不存在"<br>}<br>``` |
