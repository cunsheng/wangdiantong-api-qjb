---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.searchHistory"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

售后类

退货入库单查询

原始退款单推送

创建退货预入库

退换单查询

预入库单据查询

退货预入库单取消

历史退换单查询

原始退款单查询

原始退款单推送2

退货入库单推送

快速退货

历史退货入库单查询

历史原始退款单查询

退货物流包裹查询

当前位置： API文档 > 售后类

**aftersales.refund.Refund.searchHistory**（历史退换单查询）

**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：查询已经归档的退换单信息 |
| **1.2 适用版本：** 客户端 V1.2.5.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** 请求时间最大跨度为30天。 |
| **1.5注意事项：** **【权限校验】：店铺权限**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台货品数据，相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")，拼多多请自行对接平台获取。<br>本接口中涉及到用户隐私的字段数据仅自有平台及线下平台订单返回。具体字段详情见下面表格； |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 买家昵称 | buyer\_nick |
| 收件人姓名 | receiver\_name |
| 收件人固话 | receiver\_telno |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 自研商城、分销系统、全渠道等系统对接 |

**3.请求参数说明**

3.1 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | http://47.92.239.46/openapi |
| 正式环境 | http://wdt.wangdian.cn/openapi |

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
| 开始时间 | start\_time | String | 40 | 否 | 起始时间, 针对最后变更时间检索。如果退换单号为空则时间条件必填 |
| 结束时间 | end\_time | String | 40 | 否 | 结束时间 |
| 店铺编号 | shop\_no | String | 20 | 否 | 店铺编号 |
| 退换单号 | refund\_no | String | 40 | 否 | 退换单号 |
| 类型 | type | Int | 4 | 否 | 1：售前退款；2：退货；3：换货；4：退款不退货 |
| 退换单状态 | status | String | 4 | 否 | 用逗号分隔开数字的字符串。10：已取消；90：已完成 |

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

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据仅自有平台及线下平台返回，其他平台均不返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 单据数据 |
| 数据总条数 | total\_count | Int |  | 是 | 单据数据总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 标记id | flag\_id | Int | 11 | 是 | 标记id |
| 退换原因 | reason | String | 255 | 是 | 退换原因 |
| 原始单列表 | tid\_list | String | 255 | 是 | 长度超过255之后会截取 |
| 操作员id | operator\_id | Int | 11 | 是 | 操作员id |
| 退换单号 | refund\_no | String | 40 | 是 | 退换单号 |
| 退货人手机号 | return\_mobile | String | 100 | 是 | 退货人手机号 |
| 拦截原因 | bad\_reason | Int | 11 | 是 | 拦截原因 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 退货人电话 | return\_telno | String | 100 | 是 | 退货人电话 |
| 类型 | type | Int | 4 | 是 | 1：售前退款；2：退货；3：换货；4：退款不退货 6：保价退款 |
| 入库状态 | stockin\_status | Int | 4 | 是 | 0:无需入库;1:待入库;2:部分入库;3:全部入库;4:终止入库 |
| 标记名称 | flag\_name | String | 32 | 是 | 标记名称 |
| 业务员id | salesman\_id | Int | 11 | 是 | 业务员id |
| 退回货品数量 | return\_goods\_count | Decimal(19,4) |  | 是 | 退回货品数量 |
| 支付状态 | pay\_status | Int | 4 | 是 | 支付状态 |
| 固话 | receiver\_telno | String | 100 | 是 | 固话（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人姓名 | receiver\_name | String | 100 | 是 | 收件人姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 修改时间 | modified | String | 40 | 是 | 修改时间 |
| 退货人姓名 | return\_name | String | 100 | 是 | 退货人姓名 |
| 退回仓库id | return\_warehouse\_id | Int | 6 | 是 | 退回仓库id |
| 店铺编号 | shop\_no | String | 40 | 是 | 店铺编号 |
| 建单方式 | from\_type | Int | 4 | 是 | 0:API抓单;1:手工建单;2:Excel导入;3:分销商推送 |
| 建单时间 | created | String | 40 | 是 | 建单时间 |
| 系统订单号 | trade\_no\_list | String | 255 | 是 | 超过255长度将会被截取 |
| 退回物流单号 | return\_logistics\_no | String | 40 | 是 | 退回物流单号 |
| 退货金额 | return\_goods\_amount | Decimal(19,4) |  | 是 | 退货金额 |
| 平台退款金额 | guarantee\_refund\_amount | Decimal(19,4) |  | 是 | 平台退款金额 |
| 退货物流名称 | return\_logistics\_name | String | 40 | 是 | 退货物流名称 |
| 退换单主键 | refund\_id | Int | 11 | 是 | 退换单主键 |
| 结算时间 | settle\_time | String |  | 是 | 结算时间 |
| 原因id | reason\_id | Int | 11 | 是 | 原因id |
| 店铺id | shop\_id | Int | 11 | 是 | 店铺id |
| 买家昵称 | buyer\_nick | String | 100 | 是 | 买家昵称（仅自有平台及线下平台返回，其他平台均不返回） |
| 实际退款 | actual\_refund\_amount | Decimal(19,4) |  | 是 | 实际退款 |
| 驳回原因 | revert\_reason | Int | 11 | 是 | 驳回原因 |
| 退回仓库编号 | return\_warehouse\_no | String | 40 | 是 | 退回仓库编号 |
| 线下退款金额 | direct\_refund\_amount | Decimal(19,4) |  | 是 | 线下退款金额 |
| 入库单号 | stockin\_no | String | 40 | 是 | 入库单号 |
| 收款金额 | receive\_amount | Decimal(19,4) |  | 是 | 收款金额 |
| 业务员名称 | salesman | String | 40 | 是 | 业务员名称 |
| 退换单状态 | status | Int | 4 | 是 | 10：已取消；90：已完成 |
| 退换信息 | return\_mask | Int | 40 | 是 | 退换信息 |
| 退换单明细 | detail\_list | List<Map<String, Object>> |  | 是 | 退换单明细 |
| 换货信息 | swap\_order | <Map<String, Object> |  | 是 | 仅换货类型的单据返回 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细唯一键 | rec\_id | Int | 11 | 是 | 明细唯一键 |
| 退换单id | refund\_id | Int | 11 | 是 | 退换单id |
| 平台id | platform\_id | Int | 6 | 是 | 平台id， [点击链接查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) |
| 原始子单号 | oid | String | 40 | 是 | 原始子单号 |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 系统子单id | trade\_order\_id | Int | 11 | 是 | 系统子单id |
| 订单id | trade\_id | Int | 11 | 是 | 订单id |
| 系统订单号 | trade\_no | String | 40 | 是 | 系统订单号 |
| 担保退款 | is\_guarantee | bool | 1 | 是 | 是否担保退款<br>是：true；否：false |
| 数量 | num | Decimal(19,4) |  | 是 | 实际发出数量 |
| 价格 | price | Decimal(19,4) |  | 是 | 价格, 系统订单明细分摊后价格 |
| 原价 | original\_price | Decimal(19,4) |  | 是 | 原价, 系统订单明细标价 |
| 退款数量 | refund\_num | Decimal(19,4) |  | 是 | 退款数量 |
| 退款总额 | total\_amount | Decimal(19,4) |  | 是 | 退款总额, 系统订单明细的分摊后金额 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 已经退款的总金额 |
| 单品id | spec\_id | Int | 11 | 是 | 单品id |
| 是否残次品 | defect | boolean | 1 | 是 | 是否残次品<br>是：true；否：false |
| 退回数量 | returned\_num | Decimal(19,4) |  | 是 | 退回数量 |
| 退货入库数量 | stockin\_num | Decimal(19,4) |  | 是 | 退货入库数量 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 创建时间 | created | String | 40 | 是 | 创建时间 |
| 最后修改时间 | modified | String | 40 | 是 | 最后修改时间 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 规格编码 | spec\_code | String | 40 | 是 | 规格编码 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |

**swap\_order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单id | refund\_id | Int | 11 | 是 | 退换单id |
| 换出订单原始单号 | tid | String | 40 | 是 | 换出订单原始单号 |
| 店铺id | shop\_id | Int | 11 | 是 | 店铺id |
| 仓库id | warehouse\_id | Int | 11 | 是 | 仓库id |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 店铺名称 | shop\_name | String | 40 | 是 | 店铺名称 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 换货详情 | swap\_order\_detail\_list | List<Map<String, Object>> |  | 是 | 换出订单明细 |

**swap\_order\_detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单id | refund\_id | Int | 11 | 是 | 退换单id |
| 原始子单号 | oid | String | 40 | 是 | 原始子单号 |
| 货品类型 | target\_type | Int | 4 | 是 | 货品类型 |
| 换出货品id | target\_id | Int | 11 | 是 | 换出货品id |
| 是否残次品 | defect | boolean | 1 | 是 | 是否残次品 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 商家编码 | merchant\_no | String | 40 | 是 | 商家编码,换出货品为组合装则此编码为组合装的商家编码 |
| 零售价 | price | Decimal(19,4) |  | 是 | 零售价 |
| 总价 | total\_amount | Decimal(19,4) |  | 是 | 总价 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 备注 | remark | String | 255 | 是 | 备注 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.searchHistory#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.searchHistory#autoTab0_1)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2018-10-25 10:32:12"``,``"end_time"``:``"2018-10-29 10:32:12"``,``"type"``:3}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>`$pars``=``array`<br>`(`<br>```'start_time'``=>``'2018-10-25 10:32:12'``,`<br>```'end_time'``=>``'2018-10-29 10:32:12'`<br>`);`<br>`$pager``=``new``Pager(50, 0, true);`<br>`$data``=``$client``->pageCall(``"aftersales.refund.Refund.searchHistory"``,``$pager``,``$pars``);``//分页方法`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.searchHistory#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54 | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"total_count"``: 1,`<br>`"order"``: [`<br>`{`<br>`"flag_id"``: 0,`<br>`"reason"``:``"无"``,`<br>`"tid_list"``:``"AT201810260027"``,`<br>`"operator_id"``: 21,`<br>`"detail_list"``: [`<br>`],`<br>`"refund_no"``:``"TK1810260005"``,`<br>`"return_mobile "``:``""``,`<br>`"bad_reason"``: 0,`<br>`"remark"``:``""``,`<br>`"return_telno"``:``"~fSQFZ/yni5sB7AbC9Kt5oA==~1~"``,`<br>`"type"``: 3,`<br>`"stockin_status"``: 0,`<br>`"flag_name"``:``"无"``,`<br>`"salesman_id"``: 21,`<br>`"return_goods_count"``: 2.0000,`<br>`"pay_status"``: 0,`<br>`" receiver_telno"``:``"16619955153"``,`<br>`"receiver_name"``:``"王召红"``,`<br>`"modified"``:``"2018-10-26 14:52:15"``,`<br>`"return_name"``:``"~fSQFZ/yni5sB7AbC9Kt5oA==~1~"``,`<br>`"return_warehouse_id"``: 12,`<br>`"shop_no"``:``"001"``,`<br>`"from_type "``: 1,`<br>`"created"``:``"2018-10-26 14:49:02"``,`<br>`"trade_no_list"``:``"JY201810260048"``,`<br>`"return_logistics_no"``:``""``,`<br>`"return_goods_amount"``: 13.0000,`<br>`"guarantee_refund_amount"``: 0.0000,`<br>`"return_logistics_name"``:``"销 售退货专用物流"``,`<br>`"refund_id"``: 20,`<br>`"settle_time"``:``""``,`<br>`"reason_id"``: 0,`<br>`"shop_id"``: 10,`<br>`"buyer_nick"``:``"~GY2AcukFtGPJiW2+UvWl/y2Ri5KB5++K/7HI+nixOf0=~1~"``,`<br>`"actual_refund_amount"``: 12.9800,`<br>`"revert_reason "``: 0,`<br>`"return_warehouse_no"``:``"001"``,`<br>`"direct_refund_amount"``: 13.0000,`<br>`"stockin_no"``:``""``,`<br>`"receive_amount"``: 0.0200,`<br>`"salesman"``:``"W"``,`<br>`"return_mask"``: 0,`<br>`"status"``: 10`<br>`}`<br>`]`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.searchHistory#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

4.响应参数

4.1 公共响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1