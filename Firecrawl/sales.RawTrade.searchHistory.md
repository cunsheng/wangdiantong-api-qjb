---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.searchHistory"
title: "API文档"
---
**sales.RawTrade.searchHistory（历史原始单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP已归档的原始订单信息 |
| **1.2 适用版本：** 客户端 V1.4.1.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：** **【权限校验】：店铺权限**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据， **淘系** **相关平台规则** [点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")， **淘系数据获取办法** **[点击这里，拼多多请自行对接平台获取。](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")**<br>本接口中涉及到用户隐私的字段数据仅自有平台及线下平台订单返回，具体字段详见下述“隐私字段列表”<br>通过从后往前翻页的方式可以避免漏单问题。 |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 客户网名 | buyer\_nick |
| 邮箱 | buyer\_email |
| 买家姓名 | buyer\_name |
| 买家支付账号 | pay\_account |
| 收件人姓名 | receiver\_name |
| 收件地址 | receiver\_address |
| 收件人手机 | receiver\_mobile |
| 收件人电话 | receiver\_telno |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 财务系统、SAP、数据分析等系统的对接 |

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
| 分页 | pager | Pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始单号 | tid | String | 40 | n | 原始单号 |
| 开始时间 | start\_time | String | 40 | n | 修改起始时间 |
| 结束时间 | end\_time | String | 40 | n | 修改结束时间 |
| 店铺编号 | shop\_no | String | 20 | n | 店铺编号 |
| 是否使用从库查询 | is\_slave | boolean | 1 | n | 使用:true  不使用:false<br>(仅对开通从库配置客户生效) |
| 优惠明细掩码 | detail\_mask | Int | 1 | n | 默认为0，<br>1：返回优惠明细<br>0：不返回优惠明细 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小（单量较大的卖家，page\_size建议200以下） |
| 页号 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | y | 单据数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据仅自有平台及线下平台返回，其他平台均不返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | y | 订单相关数据 |
| 总数 | total\_count | Int | 11 | n | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一键 | rec\_id | Int | 20 | y | 唯一键 |
| 平台ID | platform\_id | Int | 6 | y | 平台ID（请点击[平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看对应关系） |
| 原始单号 | tid | String | 40 | y | 原始单号 |
| 店铺id | shop\_id | Int | 6 | y | 店铺id |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺平台id | shop\_platform\_id | int |  | y | 店铺平台id（请点击[平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看对应关系） |
| 已收 | received | int |  | y | 已收 |
| 子平台id | sub\_platform\_id | int |  | y | 子平台id（请点击[平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看对应关系） |
| 币种 | currency | string |  | y | 币种 |
| 处理状态 | process\_status | Int | 4 | y | 10:待递交<br>15:部分发货待递交<br>20:已递交<br>30:部分发货<br>40:已发货<br>60:已完成<br>70:已取消 |
| 平台状态 | trade\_status | Int | 4 | y | 10:未确认<br>20:待尾款<br>30:待发货<br>40:部分发货<br>50:已发货<br>60:已签收<br>70:已完成<br>80:已退款<br>90:已关闭 |
| 支付状态 | pay\_status | Int | 4 | y | 0:未付款<br>1:部分付款<br>2:已付款 |
| 支付方式 | pay\_method | Int | 4 | y | 1:在线转账<br>2:现金<br>3:银行转账<br>4:邮局汇款<br>5:预付款<br>6:刷卡 |
| 退款状态 | refund\_status | Int | 4 | y | 0:无退款<br>1:取消退款<br>2:已申请退款<br>3:等待退货<br>4:等待收货<br>5:退款成功<br>6:未付款关闭 |
| 递交失败原因 | bad\_reason | String |  | y | 递交失败原因 |
| 子单数量 | order\_count | BigDecimal(19,4) |  | y | 子单数量 |
| 货品数量 | goods\_count | BigDecimal(19,4) |  | y | 货品数量 |
| 下单时间 | trade\_time | String | 40 | y | 下单时间 |
| 支付时间 | pay\_time | String | 40 | y | 支付时间 |
| 结束时间 | end\_time | String | 40 | y | 结束时间 |
| 买家留言 | buyer\_message | String | 1024 | y | 买家留言 |
| 客服备注 | remark | String | 1024 | y | 客服备注 |
| 拼接名称 | union\_name | String | 100 | y | 脱敏后的买家昵称-网名id |
| 客户网名 | buyer\_nick | String | 100 | y | 客户网名（仅自有平台及线下平台返回，其他平台均不返回） |
| 邮箱 | buyer\_email | String | 100 | y | 邮箱（仅自有平台及线下平台返回，其他平台均不返回） |
| 买家姓名 | buyer\_name | String | 100 | y | 买家姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 买家区域 | buyer\_area | String | 100 | y | 买家区域 |
| 平台支付单号 | pay\_id | String | 40 | y | 平台支付单号 |
| 买家支付账号 | pay\_account | String | 128 | y | 买家支付账号（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人姓名 | receiver\_name | String | 100 | y | 收件人姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人国家 | receiver\_country | Int | 6 | y | 收件人国家 |
| 收件人省份 | receiver\_province | Int | 11 | y | [见城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 市 | receiver\_city | Int | 11 | y | [见城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 区 | receiver\_district | Int | 11 | y | [见城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 收件人地址 | receiver\_address | String | 255 | y | 收件人地址（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人手机 | receiver\_mobile | String | 40 | y | 收件人手机（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人电话 | receiver\_telno | String | 100 | y | 收件人电话（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人省市区 | receiver\_area | String | 128 | y | 收件人省市区 |
| 区域（京东几环） | receiver\_ring | String | 20 | y | 区域（京东几环） |
| 送货时间 | to\_deliver\_time | String | 20 | y | 送货时间 |
| 货款 | goods\_amount | BigDecimal(19,4) |  | y | 货款 |
| 邮费 | post\_amount | BigDecimal(19,4) |  | y | 邮费 |
| 其他收费 | other\_amount | BigDecimal(19,4) |  | y | 其他收费 |
| 优惠 | discount | BigDecimal(19,4) |  | y | 优惠 |
| 应收 | receivable | BigDecimal(19,4) |  | y | 应收 |
| 买家已付金额 | paid | BigDecimal(19,4) |  | y | 买家已付金额 |
| 平台费用 | platform\_cost | BigDecimal(19,4) |  | y | 平台费用 |
| 外部仓库编号 | warehouse\_no | String | 20 | y | 外部仓库编号 |
| 是否自流转 | is\_auto\_wms | bool |  | y | 是否自流转 |
| 最后修改时间 | modified | String | 40 | y | 最后修改时间 |
| 给消费者开票金额 | consumer\_amount | BigDecimal(19,4) |  | y | 给消费者开票金额，数值来源于订单平台，若平台未传递给旺店通对应的值，该字段不返回 |
| 给平台开票金额 | platform\_amount | BigDecimal(19,4) |  | y | 给平台开票金额，数值来源于订单平台，若平台未传递给旺店通对应的值，该字段不返回 |
| 创建时间 | created | String | 40 | y | 创建时间 |
| 发货条件 | delivery\_term | Int | 4 | y | 1：款到发货<br>2：货到付款（包含部分货到付款）<br>3：分期付款 |
| 担保方式 | guarantee\_mode | Int | 4 | y | 1：担保交易<br>2：非担保交易<br>3：非担保在线交易（ecshop） |
| 原始单明细 | trade\_orders | List<Map<String, Object>> |  | y | 原始单明细 |
| 优惠明细 | discount\_list | List<Map<String, Object>> |  | y | 优惠明细, 不存在金额明细时金额明细为空数组 |

**trade\_orders**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 系统原始单明细id | rec\_id | Int | 20 | y | 系统原始单明细id |
| 原始单号 | tid | String | 40 | y | 原始单号 |
| 原始子单号 | oid | String | 40 | y | 原始子单号 |
| 平台id | platform\_id | Int | 6 | y | 平台id |
| 状态 | status | Int | 4 | y | 10:未确认<br>20:待尾款<br>30:待发货<br>40:部分发货<br>50:已发货<br>60:已签收<br>70:已完成<br>80:已退款<br>90:已关闭 |
| 处理状态 | process\_status | Int | 4 | y | 10:待递交<br>15:部分发货待递交<br>20:已递交<br>30:部分发货<br>40:已发货<br>60:已完成<br>70:已取消 |
| 退款状态 | refund\_status | Int | 4 | y | 0:无退款<br>1:取消退款<br>2:已申请退款<br>3:等待退货<br>4:等待收货<br>5:退款成功<br>6:未付款关闭 |
| 平台货品名称 | goods\_name | String | 255 | y | 平台货品名称 |
| 平台货品编号 | goods\_no | String | 40 | y | 平台货品编号 |
| 平台货品id | goods\_id | String | 40 | y | 平台货品id |
| 平台规格编码 | spec\_no | String | 40 | y | 平台规格编码 |
| 平台规格名称 | spec\_name | String | 255 | y | 平台规格名称 |
| 平台规格id | spec\_id | String | 40 | y | 平台规格id |
| 平台规格码 | spec\_code | String | 40 | y | 平台规格码 |
| 数量 | num | Decimal(19,4) |  | y | 数量 |
| 单价 | price | Decimal(19,4) |  | y | 单价 |
| 优惠 | discount | Decimal(19,4) |  | y | 优惠 |
| 调整 | adjust\_amount | Decimal(19,4) |  | y | 调整 |
| 分摊优惠 | share\_discount | Decimal(19,4) |  | y | 分摊优惠 |
| 总价 | total\_amount | Decimal(19,4) |  | y | 总价 |
| 分摊后应收 | share\_amount | Decimal(19,4) |  | y | 分摊后应收 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | y | 退款金额 |
| 备注 | remark | String | 255 | y | 备注 |
| 最后变更时间 | modified | String | 40 | y | 最后变更时间 |
| 创建时间 | created | String | 40 | y | 创建时间 |
| 子单完成时间 | end\_time | String | 40 | y | 子单完成时间 |

**discount\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始子单号 | oid | String | 20 | y | 原始子单号 |
| 优惠名称 | name | String | 50 | y | 优惠名称 |
| 详情 | detail | String | 128 | y | 详情 |
| 金额 | amount | Decimal(19,4) |  | y | 金额 |
| 类型 | type | String | 60 | y | 对应平台上的优惠id |

**5.请求示例**

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.searchHistory#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.searchHistory#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.searchHistory#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.searchHistory#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"tid"``:``"TID-TgKngjNFhj"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->tid =``'TID-TgKngjNFhj'``;`<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>``<br>`try``{`<br>```$data``=``$client``->pageCall(``"sales.RawTrade.search"``,``$pager``,``$parMap``);`<br>`}``catch``(WdtErpException``$e``)`<br>`{`<br>```echo``$e``->getMessage();`<br>`}`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.searchHistory#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"buyer_area"``:``""``,`<br>```"post_amount"``: 0,`<br>```"trade_time"``:``"2021-01-29 18:06:43"``,`<br>```"receiver_ring"``:``""``,`<br>```"bad_reason"``:``""``,`<br>```"buyer_name"``:``""``,`<br>```"discount"``: 0,`<br>```"other_amount"``: 0,`<br>```"pay_account"``:``""``,`<br>```"tid"``:``"1000000026482026"``,`<br>```"to_deliver_time"``:``""``,`<br>```"platform_cost"``: 0,`<br>```"modified"``:``"2021-01-29 18:37:11"``,`<br>```"receiver_country"``: 0,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"buyer_email"``:``""``,`<br>```"receiver_area"``:``"北京市北京市东城区"``,`<br>```"refund_status"``: 2,`<br>```"buyer_message"``:``""``,`<br>```"receiver_province"``: 110000,`<br>```"created"``:``"2021-01-29 18:06:59"``,`<br>```"received"``: 0,`<br>```"trade_orders"``: [{`<br>```"rec_id"``: 7615840,`<br>```"tid"``:``"1000000026482026"``,`<br>```"oid"``:``"QJB16119148202804961"``,`<br>```"platform_id"``: 127,`<br>```"status"``: 80,`<br>```"process_status"``: 20,`<br>```"refund_status"``: 5,`<br>```"goods_name"``:``"品牌桶包"``,`<br>```"goods_no"``:``"PMJHBBYQ"``,`<br>```"goods_id"``:``"1022"``,`<br>```"spec_no"``:``"PMJHBBYQ00101"``,`<br>```"spec_name"``:``"夜空黑"``,`<br>```"spec_id"``:``"1046"``,`<br>```"spec_code"``:``""``,`<br>```"num"``: 2,`<br>```"price"``: 480,`<br>```"discount"``: 0,`<br>```"adjust_amount"``: 0,`<br>```"share_discount"``: 0,`<br>```"total_amount"``: 960,`<br>```"share_amount"``: 960,`<br>```"refund_amount"``: 10,`<br>```"remark"``:``""``,`<br>```"modified"``:``"2021-01-29 18:37:11"``,`<br>```"created"``:``"2021-01-29 18:06:59"``,`<br>```"end_time"``:``""`<br>```}],`<br>```"shop_platform_id"``: 127,`<br>```"pay_time"``:``"2021-01-29 18:06:44"``,`<br>```"shop_id"``: 442,`<br>```"union_name"``:``"aaaa-"``,`<br>```"is_auto_wms"``:``false``,`<br>```"process_status"``: 70,`<br>```"pay_id"``:``""``,`<br>```"receiver_city"``: 110100,`<br>```"remark"``:``""``,`<br>```"sub_platform_id"``: 0,`<br>```"goods_count"``: 2,`<br>```"discount_list"``: [],`<br>```"pay_status"``: 2,`<br>```"receiver_telno"``:``""``,`<br>```"warehouse_no"``:``""``,`<br>```"trade_status"``: 80,`<br>```"receiver_name"``:``"晓五"``,`<br>```"currency"``:``""``,`<br>```"guarantee_mode"``: 1,`<br>```"order_count"``: 1,`<br>```"delivery_term"``: 1,`<br>```"goods_amount"``: 960,`<br>```"receiver_district"``: 110101,`<br>```"end_time"``:``""``,`<br>```"pay_method"``: 1,`<br>```"receivable"``: 960,`<br>```"rec_id"``: 5047556,`<br>```"receiver_mobile"``:``"111111111111"``,`<br>```"buyer_nick"``:``"aaaa"``,`<br>```"platform_id"``: 127,`<br>```"paid"``: 0,`<br>```"receiver_address"``:``"我退酒有UI"`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.searchHistory#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` |
