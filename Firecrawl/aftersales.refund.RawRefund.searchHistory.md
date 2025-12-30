---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.RawRefund.searchHistory"
title: "API文档"
---
aftersales.refund.RawRefund.searchHistory（历史原始退款单查询）

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP已归档的原始退款单信息 |
| **1.2 适用版本：** 客户端 V1.4.5.8及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：**<br>**1.5.1 满足一下情况之一时间参数非必填**<br>（1）platform\_id&refund\_no<br>（2）platform\_id&tid<br>（3）logistics\_no<br>**1.5.2【权限校验】：店铺权限**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台数据， **淘系**相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")，拼多多请自行对接平台获取。<br>本接口中涉及到用户隐私的字段数据仅自有平台及线下平台订单返回。具体字段详情见下面表格； |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 网名 | buyer\_nick |
| 支付账号 | pay\_account |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 自研商城、分销系统、全渠道等系统对接 |

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
| 分页 | pager | pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 是 | 开始时间 |
| 结束时间 | end\_time | String | 40 | 是 | 结束时间 |
| 时间条件类型 | time\_type | Int | 4 | 是 | 1：修改时间<br>2：退款时间<br>不传按照修改时间获取数据 |
| 原始退单号 | refund\_no | String | 40 | 否 | 原始退单号 |
| 物流单号 | logistics\_no | String | 40 | 否 | 物流单号 |
| 平台id | platform\_id | Int | 6 | 否 | 平台id，映射表点击 [详情](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看 |
| 店铺编号 | shop\_no | String | 40 | 否 | 店铺编号 |
| 原始单号 | tid | String | 40 | 否 | 原始单号 |
| 原始子单号 | oid | String | 40 | 否 | 原始子单号 |
| 明细掩码 | detail\_mask | Int | 11 | 否 | 0：不返回原始退款单优惠<br>1：返回原始退款单优惠<br>默认0 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小（单量较大的卖家，page\_size建议200以下） |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参** **数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 否 | 状态码:0表示成功,在调用错误时不返回该值 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | 是 | 单据数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 单据数据 |
| 数据总条数 | total\_count | Int | 11 | 是 | 单据数据总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始退款单唯一id | refund\_id | Int | 11 | 是 | 原始退款单唯一id |
| 平台id | platform\_id | Int | 6 | 是 | 平台id，点击 [查看平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 店铺名称 | shop\_name | String | 128 | 是 | 店铺名称 |
| 原始退款单号 | refund\_no | String | 40 | 是 | 原始退款单号 |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 原始子单号 | oid | String | 40 | 是 | 原始子单号 |
| 类型 | type | byte | 4 | 是 | 1：售前退款<br>2：退货<br>3：换货<br>4：退款不退货 |
| 平台状态 | status | byte | 4 | 是 | 1：取消退款<br>2：申请退款<br>3：等待退货<br>4：等待收货<br>5：退款成功<br>7：卖家拒绝退款 |
| 处理状态 | process\_status | byte | 4 | 是 | 0：待递交<br>15：已递交<br>20：递交失败<br>40：已处理 |
| 支付账号 | pay\_account | String | 128 | 是 | 支付账号（仅自有平台及线下平台返回，其他平台均不返回） |
| 支付单号 | pay\_no | String | 60 | 是 | 支付单号 |
| 申请退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 申请退款金额 |
| 实际退款金额 | actual\_refund\_amount | Decimal(19,4) |  | 是 | 实际退款金额 |
| 退款成功时间 | current\_phase\_timeout | String |  | 是 | 退款成功时间 |
| 标题 | title | String | 255 | 是 | 标题 |
| 物流公司名称 | logistics\_name | String | 40 | 是 | 物流公司名称 |
| 物流单号 | logistics\_no | String | 40 | 是 | 物流单号 |
| 网名 | buyer\_nick | String | 100 | 是 | 网名（仅自有平台及线下平台返回，其他平台均不返回） |
| 退款时间 | refund\_time | String |  | 是 | 申请退款时间, yyyy-MM-dd HH:mm:ss格式 |
| 是否售后退款单 | is\_aftersale | boolean |  | 是 | 是否售后退款单 |
| 退款原因 | reason | String | 255 | 是 | 退款原因 |
| 退款原因关键字映射对应id | reason\_id | Int | 11 | 是 | 退款原因关键字映射对应id |
| 备注 | remark | String | 255 | 是 | 备注 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 单价 | price | Decimal(19,4) |  | 是 | 单价 |
| 退款货品总价格 | total\_amount | Decimal(19,4) |  | 是 | 退款货品总价格 |
| 平台货品id | goods\_id | String | 40 | 是 | 平台货品id |
| 平台规格id | spec\_id | String | 40 | 是 | 平台规格id |
| 平台货品编号 | goods\_no | String | 40 | 是 | 平台货品编号 |
| 平台规格编号 | spec\_no | String | 40 | 是 | 平台规格编号 |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间, yyyy-MM-dd HH:mm:ss格式 |
| 创建时间 | created | String |  | 是 | 创建时间, yyyy-MM-dd HH:mm:ss格式 |
| 店铺id | shop\_id | Int | 6 | 是 | 店铺id |
| 子平台id | sub\_platform\_id | Int | 11 | 是 | 子平台id |
| 店铺平台id | shop\_platform\_id | Int | 11 | 是 | 店铺平台id |
| 是否拒收 | is\_reject | Int | 4 | 是 | 是否拒收<br>0：否<br>1：是 |
| 退款版本 | refund\_version | String | 40 | 是 | 退款版本 |
| tag | tag | Int | 11 | 是 | tag |
| 外部退款单 | is\_external | Int | 4 | 是 | 外部退款单，未经ERP处理过的订单 |
| 修改掩码 | modify\_flag | Int | 11 | 是 | 修改掩码<br>1：状态<br>2：金额<br>16：类型 |
| 原始退款单明细 | detail\_list | List<Map<String, Object>> |  | 是 | 原始退款单明细 |
| 原始退款单优惠明细 | discount\_list | List<Map<String, Object>> |  | 是 | 原始退款单优惠明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主单id或明细主键id | refund\_id | Int | 11 | 是 | 主单id或明细主键id |
| 原始子单号 | oid | String | 40 | 是 | 原始子单号 |
| 平台id | platform\_id | Int | 6 | 是 | 平台id |
| 原始退款单号 | refund\_no | String | 40 | 是 | 原始退款单号 |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 平台状态 | status | Int | 4 | 是 | 1：取消退款<br>2：已申请退款<br>3：已同意<br>4：待收货<br>5：退款成功 |
| 平台货品名称 | goods\_name | String | 255 | 是 | 平台货品名称 |
| 平台货品编码 | goods\_no | String | 40 | 是 | 平台货品编码 |
| 平台货品id | goods\_id | String | 40 | 是 | 平台货品id |
| 平台规格名称 | spec\_name | String | 255 | 是 | 平台规格名称 |
| 平台规格编码 | spec\_no | String | 40 | 是 | 平台规格编码 |
| 平台规格id | spec\_id | String | 40 | 是 | 平台规格id |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 总金额 | total\_amount | Decimal(19,4) |  | 是 | 总金额 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 单价 | price | Decimal(19,4) |  | 是 | 单价 |
| 类型 | type | Int |  | 是 | 类型<br>0：该明细取自原始退款单明细<br>1：该明细取自原始退款单主单 |
| 退货时间 | refund\_time | String | 40 | 是 | 退货时间 |
| 最后修改时间 | modified\_date | String | 40 | 是 | 最后修改时间 |
| 创建时间 | created\_date | String | 40 | 是 | 创建时间 |

**discount\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始退款单号 | refund\_no | String | 40 | 是 | 原始退款单号 |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 原始子单号 | oid | Sting | 40 | 是 | 原始子单号 |
| 优惠名称 | name | String | 50 | 是 | 优惠名称 |
| 金额 | amount | Decimal(19,4) |  | 是 | 金额 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
| 1 | `[{``"refund_no"``:``"91294632450951678"``,``"platform_id"``:1}]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->refund_no =``'91294632450951678'``;`<br>`$parMap``->platform_id = 1;`<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>``<br>`try``{`<br>```$data``=``$client``->pageCall(``"aftersales.refund.RawRefund.searchHistory"``,``$pager``,``$parMap``);`<br>`}``catch``(WdtErpException``$e``)`<br>`{`<br>```echo``$e``->getMessage();`<br>`}`<br>`?>` | |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"logistics_name"``:``" "``,`<br>```"refund_version"``:``" "``,`<br>```"reason"``:``" "``,`<br>```"detail_list"``: [{`<br>```"refund_id"``: 210348,`<br>```"oid"``:``"202210270002-0"``,`<br>```"price"``: 0,`<br>```"platform_id"``: 127,`<br>```"refund_no"``:``"202210270002"``,`<br>```"num"``: 5,`<br>```"remark"``:``" "``,`<br>```"total_amount"``: 0,`<br>```"tid"``:``"202210270002"``,`<br>```"status"``: 3,`<br>```"goods_no"``:``""``,`<br>```"spec_no"``:``""``,`<br>```"goods_id"``:``""``,`<br>```"spec_id"``:``""``,`<br>```"refund_time"``:``"2022-04-08 09:18:00"``,`<br>```"modified_date"``:``"2022-10-27 17:47:17"``,`<br>```"created_date"``:``"2022-10-27 17:46:21"``,`<br>```"goods_name"``:``""``,`<br>```"spec_name"``:``""`<br>```}],`<br>```"refund_no"``:``"202210270002"``,`<br>```"num"``: 5,`<br>```"goods_no"``:``""``,`<br>```"remark"``:``" "``,`<br>```"sub_platform_id"``: 0,`<br>```"oid"``:``"202210270002-0"``,`<br>```"pay_account"``:``""``,`<br>```"type"``: 3,`<br>```"title"``:``" "``,`<br>```"spec_no"``:``""``,`<br>```"discount_list"``: [],`<br>```"tid"``:``"202210270002"``,`<br>```"current_phase_timeout"``:``""``,`<br>```"pay_no"``:``""``,`<br>```"price"``: 0,`<br>```"spec_id"``:``""``,`<br>```"refund_amount"``: 0,`<br>```"modified"``:``"2022-10-27 17:47:17"``,`<br>```"tag"``: 0,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"logistics_no"``:``" "``,`<br>```"is_aftersale"``:``true``,`<br>```"created"``:``"2022-10-27 17:46:21"``,`<br>```"is_reject"``: 0,`<br>```"swap_order_id"``:``""``,`<br>```"is_external"``: 0,`<br>```"goods_id"``:``""``,`<br>```"shop_platform_id"``: 127,`<br>```"shop_name"``:``"wdtapi3-test"``,`<br>```"refund_id"``: 210348,`<br>```"reason_id"``: 99,`<br>```"shop_id"``: 711,`<br>```"buyer_nick"``:``""``,`<br>```"actual_refund_amount"``: 0,`<br>```"total_amount"``: 0,`<br>```"refund_time"``:``"2022-04-08 09:18:00"``,`<br>```"process_status"``: 15,`<br>```"platform_id"``: 127,`<br>```"modify_flag"``: 0,`<br>```"status"``: 3`<br>```}]`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` | |
