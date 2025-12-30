---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.RawTrade.pushSelf2"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

订单类

销售出库单查询

物流同步状态回传

原始单推送

订单查询

待同步列表查询

重量回传

重量回传2

发票信息查询

发票信息更新

平台账单查询

平台账单推送

取消当前同步

库存同步失败

库存同步成功

获取自有平台货品需要同步信息

历史销售出库单查询

历史订单查询

平台对账单查询

原始单查询

被合并订单查询

收付款单查询

重量回传3

库存同步计算查询

重量回传4

订单客服备注修改

物流单查询

历史原始单查询

JIT退货单查询

原始单推送2

销售出库实际出库明细查询

销售收付单查询

已完成订单推送

已取消出库单查询

订单日志查询

订单标签查询

订单转异常订单

库存同步计算查询（批量）

订单查询（仅返回自有平台、线下平台订单信息）

历史原始单查询（仅返回自有平台、线下平台订单）

历史订单查询（仅返回自有平台、线下平台订单）

原始单查询（仅返回自有平台、线下平台订单）

当前位置： API文档 > 订单类

**sales.RawTrade.pushSelf2（原始** **单推送2）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** ①推送销售订单给ERP ②更新已推送成功的销售订单 |
| **1.2 适用版本：** 客户端V1.5.9.9及以上版本 |
| **1.3注意事项：** **【权限校验】：店铺权限（仅支持自有平台推送）**；上线之前必须在测试环境测试订单推送之后的相关流程!!!<br>单次推送建议单量不超过100单 |

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
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String | 40 | 是 | 店铺编号 |
| 原始单信息 | rawTradeList | List<Map<String, Object>> |  | 是 | 原始单信息信息集合 |
| 原始子单信息 | rawTradeOrderList | List<Map<String, Object>> |  | 是 | 原始子单信息集合 |
| 优惠信息 | discountList | List<Map<String, Object>> |  | 否 | 不需要优惠明细可不传,优惠明细显示在订单管理界面的优惠明细Tab页 |

rawTradeList

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始单号 | tid | String | 40 | 是 | 指商城、官网等平台的订单编号，ERP称之为原始单号，同一个sid下通过本接口新增订单的tid保证唯一。 |
| 处理状态 | process\_status | Int | 4 | 是 | 是否执行自动递交以系统配置为准<br>10: 待递交,<br>20: 已递交，<br>30: 部分发货，<br>40: 已发货，<br>60: 已完成，<br>70: 已取消 |
| 平台状态 | trade\_status | Int | 4 | 是 | 10未确认 20待尾款 30待发货 40部分发货 50已发货 60已签收 70已完成 80已退款 90已关闭(付款前取消)，单据状态变更点击 [文档查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ddfh) |
| 退款状态 | refund\_status | Int | 4 | 是 | 0无退款 1申请退款 2部分退款 3全部退款，单据状态变更点击 [文档查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ddfh) |
| 付款状态 | pay\_status | Int | 4 | 是 | 0未付款1部分付款2已付款 |
| 子订单个数 | order\_count | Int | 6 | 是 | 原始单包含的子订单数，rawTradeOrderList节点下所有子单数之和 |
| 货品总数量 | goods\_count | Decimal(19,4) |  | 是 | 货品总数量，rawTradeOrderList节点下所有“num”数量之和 |
| 支付方式 | pay\_method | Int | 4 | 是 | 1在线转帐 2现金，3银行转账，4邮局汇款 5预付款 6刷卡 7支付宝 8微信支付 |
| 下单时间 | trade\_time | String | 40 | 是 | 下单时间 |
| 支付时间 | pay\_time | String | 40 | 否 | 支付时间 |
| 交易结束时间 | end\_time | String | 40 | 是 | 交易结束时间，若无则传null |
| 买家昵称/客户网名 | buyer\_nick | String | 100 | 是 | 若无则传一个固定值 |
| 买家备注 | buyer\_message | String | 1024 | 否 | 若无则传‘’ |
| 买家邮箱 | buyer\_email | String | 40 | 否 | ‘’ |
| 买家地区 | buyer\_area | String | 255 | 否 | ‘’ |
| 收件人姓名 | receiver\_name | String | 100 | 是 | 收件人姓名 |
| 省市区 | receiver\_area | String | 40 | 是 | 省市区空格分隔，示例【北京 北京市 朝阳区】，省市区推送旺店通地址库， [点击查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb "旺店通地址库") |
| 地址 | receiver\_address | String | 256 | 是 | 收件人详细地址，不包含省市区，示例【xx街道xx小区xx号楼101】 |
| 收件人邮编 | receiver\_zip | String | 20 | 否 | 收件人邮编，若无则传‘’ |
| 收件人手机 | receiver\_mobile | String | 40 | 是 | 该字段必传，收件人手机号，为11位手机号码，示例【13888888888】 |
| 收件人电话 | receiver\_telno | String | 40 | 否 | 收件人固话号，为11位固话号码，示例【02288888888】 |
| 邮费 | post\_amount | Decimal(19,4) |  | 是 | 邮费 |
| 其他费用 | other\_amount | Decimal(19,4) |  | 否 | 其他费用 |
| 优惠金额 | discount | Decimal(19,4) |  | 是 | 优惠金额 |
| 应收金额 | receivable | Decimal(19,4) |  | 是 | 应收金额，售前退款会变化，“详细金额逻辑点击 [查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ddfh)” |
| 平台费用 | platform\_cost | Decimal(19,4) |  | 否 | 0.0000 |
| 发票类别 | invoice\_type | Int | 4 | 否 | 0：不需要<br>1：普通发票<br>2：增值税普通发票<br>3：增值税专用发票 |
| 发票抬头 | invoice\_title | String | 255 | 否 | 发票抬头，若无则传‘’ |
| 发票内容 | invoice\_content | String | 255 | 否 | 发票内容，格式：纳税人识别号:\*\*\*\*\*\*\*;地址:\*\*\*\*\*\*\*;开户银行:\*\*\*\*\*\*\*;银行账号:\*\*\*\*\*\*;联系电话:\*\*\*\*\*,电子邮箱\*\*\*\*\*  若无则传‘"" |
| 物流类别 | logistics\_type | Int | 6 | 否 | -1 |
| 物流编号 | cust\_data | String |  | 否 | 系统物流编号（设置--基本设置--物流） |
| 发货条件 | delivery\_term | Int | 4 | 是 | 1款到发货 2货到付款(包含部分货到付款) 3分期付款 |
| 平台支付订单ID | pay\_id | String | 40 | 否 | ‘’ |
| 客服备注 | remark | String | 1024 | 否 | 客服备注 |
| 客服备注标记 | remark\_flag | Int | 11 | 否 | 标旗（1 红、2 黄、3 绿、4 蓝、5 紫 无则填0） |
| 货到付款金额 | cod\_amount | Decimal(19,4) |  | 否 | 若delivery\_term=2，则为应付金额，否则为0 |
| 是否是自流转 | is\_auto\_wms | Boolean |  | 是 | true自流转，false 非自流转  自动流转模式处理办法详解   单击这里 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仅自流转订单填写该仓库编号, 非自流转订单传入空字符串即可 |
| 买家支付宝帐号 | pay\_account | String | 128 | 否 | ‘’ |
| 买家要求的送货日期 | to\_deliver\_time | String | 20 | 否 | 买家要求的送货日期 |
| 已收 | received | Decimal(19,4) |  | 否 | 已从平台收款的金额 |
| 淘宝新增,物流到货时效，单位小时 | consign\_interval | Int | 6 | 否 | 淘宝新增,物流到货时效，单位小时 |
| 已付 | paid | Decimal(19,4) |  | 否 | 已支付金额 |
| 是否能合并订单 | is\_sealed | byte |  | 否 | 0：默认<br>3：不允许合并 |
| 分销商名称 | fenxiao\_nick | String | 40 | 否 | 分销商名称 |
| 证件类型 | id\_card\_type | Int |  | 否 | 0：无<br>1：身份证<br>2：军官证<br>3：护照 |
| 证件号 | id\_card | String |  | 否 | 证件号 |
| 省份id | receiver\_province\_no | Int |  | 否 | 省份id， [点击查看省市区代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb)（传省份id、市id、区id的情况下可以不传receiver\_area字段） |
| 市id | receiver\_city\_no | Int |  | 否 | 市id， [点击查看省市区代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) （传省份id、市id、区id的情况下可以不传receiver\_area字段） |
| 区id | receiver\_district\_no | Int |  | 否 | 区id， [点击查看省市区代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) （传省份id、市id、区id的情况下可以不传receiver\_area字段） |

**rawTradeOrderList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始订单号 | tid | String | 40 | 是 | 原始订单号 |
| 原始子单号 | oid | String | 40 | 是 | 平台订单货品表主键,子订单唯一标识,同一个sid下通过本接口新增订单的oid（子订单编号）要保证唯一；如果oid重复,ERP生成系统单（递交）时会提示“订单货品数量不一致xxxxxx” |
| 平台的状态 | status | Int | 4 | 是 | 10未确认 20待尾款 30待发货 40部分发货 50已发货 60已签收 70已完成 80已退款 90已关闭，单据状态变更点击 [文档查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ddfh) |
| 退款标记 | refund\_status | Int | 4 | 是 | 0无退款1取消退款,2已申请退款,3等待退货,4等待收货,5退款成功,6未付款关闭，单据状态变更点击 [文档查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ddfh) |
| 平台货品ID | goods\_id | String | 40 | 是 | 平台系统货品（SPU）的唯一标识。SPU和SKU概念介绍，单击这里 |
| 平台规格ID | spec\_id | String | 40 | 是 | 平台系统单品（SKU）的的唯一标识。SPU和SKU概念介绍，单击这里 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 规格编码 | spec\_no | String | 40 | 是 | 规格编码 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 规格名称 | spec\_name | String | 100 | 否 | 规格名称 |
| 子单类型 | order\_type | Int | 4 | 否 | 0正常货品 1虚拟货品 2服务（不传默认为0） |
| 平台类目 | cid | String | 40 | 否 | 平台类目 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 单价 | price | Decimal(19,4) |  | 是 | 单价 |
| 优惠 | discount | Decimal(19,4) |  | 是 | 优惠，平台折扣, 不包含手工调整和分摊优惠 |
| 分摊优惠 | share\_discount | Decimal(19,4) |  | 是 | 分摊优惠,退款不变 |
| 总价格 | total\_amount | Decimal(19,4) |  | 是 | 总价格，“详细金额逻辑点击 [查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ddfh)” |
| 手工调整的优惠金额 | adjust\_amount | Decimal(19,4) |  | 是 | 手工调整的优惠金额，“详细金额逻辑点击 [查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ddfh)” |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 退款金额 |
| 备注 | remark | String | 255 | 是 | 备注 |
| json串 | json | String | 255 | 是 | json串，若无可传“” |
| 赠品方式 | gift\_type | Int |  | 否 | 赠品方式<br>0非赠品<br>1自动赠送<br>2手工赠送<br>4周期购赠送<br>8平台赠送<br>32阶梯满赠 <br>64CRM追加赠送 <br>65 主品 |

**discountList**(平台,tid,oid,sn,type 联合组成唯一)

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始订单号 | tid | String | 40 | 是 | 原始订单号 |
| 原始子单号 | oid | String | 20 | 是 | 原始子单号 |
| 唯一编码 | sn | String | 40 | 否 | 平台上优惠的唯一标识 |
| 优惠名称 | name | String | 50 | 否 | 优惠名称 |
| 优惠详情 | detail | String | 128 | 否 | 优惠详情 |
| 优惠金额 | amount | Decimal(19,4) |  | 否 | 优惠金额 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int | 11 | 是 | 状态码,0表示正常 |
| 错误信息 | message | String | 255 | 是 | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | 是 | 结果相关数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 更新订单数 | chg\_count | Int | 11 | 是 | 返回的为更新订单的数量 |
| 新增订单数 | new\_count | Int | 11 | 是 | 返回的为新增订单的数量 |
| 错误信息 | error\_list | List<Map<String, Object>> |  | 是 | 错误信息为空，表示全部创建成功 |

**error\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单号 | no | String |  | 是 | 单号 |
| 错误信息 | error | String |  | 是 | 错误信息 |

**5.请求示例**

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89 | `[``"test"``, [{`<br>`"is_auto_wms"``:``false``,`<br>`"post_amount"``: 2,`<br>`"other_amount"``: 5.2,`<br>`"discount"``: 1,`<br>`"platform_cost"``: 0,`<br>`"cod_amount"``:``""``,`<br>`"received"``:``""``,`<br>`"tid"``:``"tid-aqyYHjEldp"``,`<br>`"process_status"``: 10,`<br>`"trade_status"``: 30,`<br>`"refund_status"``: 0,`<br>`"pay_status"``: 2,`<br>`"order_count"``: 2,`<br>`"pay_method"``: 2,`<br>`"trade_time"``:``"2020-03-20 18:24:37"``,`<br>`"pay_time"``:``"2020-03-20 18:24:37"``,`<br>`"end_time"``:``"2020-03-20 18:24:37"``,`<br>`"buyer_nick"``:``"test_openapi"``,`<br>`"buyer_message"``:``"test_openapi"``,`<br>`"buyer_email"``:``"test_openapi@gmail.com"``,`<br>`"buyer_area"``:``"test_area"``,`<br>`"receiver_name"``:``"receiver_name"``,`<br>`"receiver_area"``:``"北京 北京市 朝阳区"``,`<br>`"receiver_address"``:``"春天街道春天花园小区1号楼1单元101"``,`<br>`"receiver_zip"``:``"014500"``,`<br>`"receiver_mobile"``:``"15612340987"``,`<br>`"receiver_telno"``:``"02288888888"``,`<br>`"invoice_type"``: 0,`<br>`"invoice_title"``:``""``,`<br>`"invoice_content"``:``""``,`<br>`"logistics_type"``: -1,`<br>`"consign_interval"``: 0,`<br>`"delivery_term"``: 1,`<br>`"to_deliver_time"``:``""``,`<br>`"pay_id"``:``""``,`<br>`"pay_account"``:``""``,`<br>`"remark"``:``""``,`<br>`"remark_flag"``: 0,`<br>`"goods_count"``: 6,`<br>`"receivable"``: 17.6`<br>`}],`<br>`[{`<br>`"tid"``:``"tid-aqyYHjEldp"``,`<br>`"oid"``:``"tid-aqyYHjEldp-0"``,`<br>`"order_type"``: 0,`<br>`"status"``: 30,`<br>`"refund_status"``: 0,`<br>`"goods_id"``:``"openapi_gid-0"``,`<br>`"spec_id"``:``"openapi_sid-0"``,`<br>`"goods_no"``:``"api_gno-0"``,`<br>`"spec_no"``:``"api_sno-0"``,`<br>`"goods_name"``:``"api_gname-0"``,`<br>`"spec_name"``:``"api_sname-0"``,`<br>`"num"``: 3,`<br>`"price"``: 2.5,`<br>`"adjust_amount"``: 2,`<br>`"refund_amount"``:``""``,`<br>`"discount"``: 0.5,`<br>`"share_discount"``: 0.2,`<br>`"total_amount"``: 9,`<br>`"cid"``:``""``,`<br>`"remark"``:``""``,`<br>`"json"``:``""`<br>`}, {`<br>`"tid"``:``"tid-aqyYHjEldp"``,`<br>`"oid"``:``"tid-aqyYHjEldp-1"``,`<br>`"order_type"``: 0,`<br>`"status"``: 30,`<br>`"refund_status"``: 0,`<br>`"goods_id"``:``"openapi_gid-1"``,`<br>`"spec_id"``:``"openapi_sid-1"``,`<br>`"goods_no"``:``"api_gno-1"``,`<br>`"spec_no"``:``"api_sno-1"``,`<br>`"goods_name"``:``"api_gname-1"``,`<br>`"spec_name"``:``"api_sname-1"``,`<br>`"num"``: 3,`<br>`"price"``: 2.5,`<br>`"adjust_amount"``: 2,`<br>`"refund_amount"``:``""``,`<br>`"discount"``: 0.5,`<br>`"share_discount"``: 0.2,`<br>`"total_amount"``: 9,`<br>`"share_amount"``: 8.8,`<br>`"cid"``:``""``,`<br>`"remark"``:``""``,`<br>`"json"``:``""`<br>`}]`<br>`]` | |
| PHP | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118 | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`function``str_rand(``$length``= 10,``$char``=``'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'``) {`<br>```if``(!``is_int``(``$length``) ||``$length``< 0) {`<br>```return``false;`<br>```}`<br>``<br>```$string``=``''``;`<br>```for``(``$i``=``$length``;``$i``> 0;``$i``--) {`<br>```$string``.=``$char``[mt_rand(0,``strlen``(``$char``) - 1)];`<br>```}`<br>``<br>```return``$string``;`<br>`}`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$rawTrade``=``new``stdClass();`<br>`$rawTrade``->is_auto_wms=false;`<br>`// $rawTrade->warehouse_no='pos_inner'; // 非自流转订单不需要设置此字段.`<br>``<br>`$rawTrade``->post_amount=2.0000;`<br>`$rawTrade``->other_amount=5.2000;`<br>`$rawTrade``->discount=1.0000;`<br>`// $rawTrade->receivable='';`<br>`$rawTrade``->platform_cost=0.0000;`<br>`$rawTrade``->cod_amount=``''``;`<br>`$rawTrade``->received=``''``;`<br>`$rawTrade``->goods_amount =``$rawTrade``->receivable -``$rawTrade``->post_amount +``$rawTrade``->discount;`<br>``<br>`$rawTrade``->tid=``'tid-'``.str_rand();`<br>`$rawTrade``->process_status=10;`<br>`$rawTrade``->trade_status=30;`<br>`$rawTrade``->refund_status=0;`<br>`$rawTrade``->pay_status=2;`<br>``<br>`// !!`<br>`$rawTrade``->order_count=2;`<br>`// $rawTrade->goods_count='';`<br>`$rawTrade``->pay_method=2;``//1在线转帐 2现金，3银行转账，4邮局汇款 5预付款 6刷卡`<br>`$rawTrade``->trade_time=``date``(``'Y-m-d H:i:s'``);`<br>`$rawTrade``->pay_time=``date``(``'Y-m-d H:i:s'``);`<br>`$rawTrade``->end_time=``date``(``'Y-m-d H:i:s'``);`<br>``<br>`$rawTrade``->buyer_nick=``'test_openapi'``;`<br>`$rawTrade``->buyer_message=``'test_openapi'``;`<br>`$rawTrade``->buyer_email=``'test_openapi@gmail.com'``;`<br>`$rawTrade``->buyer_area=``'test_area'``;`<br>``<br>`$rawTrade``->receiver_province=``'3'``;`<br>`$rawTrade``->receiver_name=``'receiver_name'``;`<br>`$rawTrade``->receiver_area=``'85 West Lancaster Court Paramus, NJ 07652'``;`<br>`$rawTrade``->receiver_address=``'ABCDEFG'``;`<br>`$rawTrade``->receiver_zip=``'014500'``;`<br>`$rawTrade``->receiver_mobile=``'15612340987'``;`<br>`$rawTrade``->receiver_telno=``''``;`<br>``<br>`$rawTrade``->invoice_type=0;`<br>`$rawTrade``->invoice_title=``''``;`<br>`$rawTrade``->invoice_content=``''``;`<br>``<br>`$rawTrade``->logistics_type=-1;`<br>`$rawTrade``->consign_interval=0;`<br>`$rawTrade``->delivery_term=1;`<br>`$rawTrade``->to_deliver_time=``''``;`<br>`$rawTrade``->pay_id=``''``;`<br>`$rawTrade``->pay_account=``''``;`<br>`$rawTrade``->remark=``''``;`<br>`$rawTrade``->remark_flag=0;`<br>``<br>`$tradeOderList``=``array``();`<br>`for``(``$j``=0;``$j``<``$rawTrade``->order_count;``$j``++)`<br>`{`<br>`$tradeOrder``=``new``stdClass();`<br>``<br>`$tradeOrder``->tid =``$rawTrade``->tid;`<br>`$tradeOrder``->oid =``$tradeOrder``->tid.``'-'``.``$j``;`<br>`$tradeOrder``->order_type = 0;`<br>``<br>`$tradeOrder``->status = 30;`<br>`$tradeOrder``->refund_status = 0;`<br>``<br>`$tradeOrder``->goods_id =``'openapi_gid'``.``'-'``.``$j``;`<br>`$tradeOrder``->spec_id =``'openapi_sid'``.``'-'``.``$j``;`<br>`$tradeOrder``->goods_no =``'api_gno'``.``'-'``.``$j``;`<br>`$tradeOrder``->spec_no =``'api_sno'``.``'-'``.``$j``;`<br>`$tradeOrder``->goods_name =``'api_gname'``.``'-'``.``$j``;`<br>`$tradeOrder``->spec_name =``'api_sname'``.``'-'``.``$j``;`<br>`$tradeOrder``->num = 3.0000;`<br>`$tradeOrder``->price = 2.5000;`<br>`$tradeOrder``->adjust_amount = 2.0000;`<br>`$tradeOrder``->refund_amount =``''``;`<br>`$tradeOrder``->discount = 0.5000;``// 优惠金额`<br>`$tradeOrder``->share_discount = 0.2000;``//分摊优惠金额`<br>`$tradeOrder``->total_amount =``$tradeOrder``->price *``$tradeOrder``->num +``$tradeOrder``->adjust_amount -``$tradeOrder``->discount;`<br>`// 页面的分摊优惠 = total_amount - 分摊优惠金额, 此参数不需要传入`<br>``<br>`$tradeOrder``->cid =``''``;`<br>`$tradeOrder``->remark =``''``;`<br>`$tradeOrder``->json =``''``;`<br>``<br>``<br>`// 处理主单部分数据`<br>`$rawTrade``->goods_count +=``$tradeOrder``->num;`<br>`$rawTrade``->receivable +=``$tradeOrder``->share_amount;`<br>`$tradeOderList``[``$j``] =``$tradeOrder``;`<br>`}`<br>``<br>``<br>`$shopNo``=``"test"``;`<br>`$data``=``$client``->call(``"sales.RawTrade.pushSelf"``,``$shopNo``, [``$rawTrade``],``$tradeOderList``);`<br>``<br>`var_dump(``$data``);`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"chg_count"``: 2,`<br>```"error_list"``: [],`<br>```"new_count"``: 0`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"chg_count"``: 0,`<br>```"error_list"``: [`<br>```{`<br>```"error"``:``"XXXXXXXXX"``,`<br>```"no"``:``"ceshi20230109002"`<br>```}`<br>```],`<br>```"new_count"``: 1`<br>```}`<br>`}` | |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1