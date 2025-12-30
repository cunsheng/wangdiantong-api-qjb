---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.queryHistorySelfOrderWithDetail"
title: "API文档"
---
**sales.TradeQuery.queryHistorySelfOrderWithDetail（历史订单查询--仅返回自有平台、线下平台订单）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP自有平台及线下的历史销售订单信息 |
| **1.2 适用版本：** 客户端 V1.5.8.8及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为60分钟。 |
| **1.5注意事项：** **权限校验：【店铺权限】**<br>仅返回自有平台、线下平台订单信息 |

**2.调用场景**

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
| 分页 | pager | Pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 时间类型 | time\_type | Int | 4 | n | 时间类型<br>1：修改时间<br>2：支付时间<br>3：下单时间<br>默认1 |
| 开始时间 | start\_time | String | 40 | y | 修改起始时间，若无订单号，则为必填。 |
| 结束时间 | end\_time | String | 40 | y | 修改结束时间，上同开始时间 |
| 仓库编号 | warehouse\_no | String | 40 | n | 仓库编号 |
| 订单状态 | status | String | 255 | n | 若多个状态则以“，”隔开。<br>订单状态:  <br>4 线下退款<br>5已取消<br>6 待转预订单(待审核)<br>7 待转已完成<br>10未付款<br>12待尾款<br>15等未付<br>16延时审核<br>19预订单前处理<br>20 审核前处理<br>21自流转待发货<br>23 异常预订单<br>24 换货预订单<br>25 待处理预订单<br>27待分配预订单 <br>30待客审<br>35待财审<br>55已审核<br>95已发货<br>96 成本确认（待录入计划成本，订单结算时有货品无计划成本）<br>101 已过账<br>110已完成 |
| 订单编号 | trade\_no | String | 40 | n | 订单编号 |
| 店铺编号 | shop\_no | String | 20 | n | 店铺编号 |
| 物流单号 | logistics\_no | String | 40 | n | 物流单号 |
| 原始单号 | src\_tid | String | 40 | n | 原始单号, 多个原始单号之间使用英文逗号分隔 |
| 是否使用从库查询 | is\_slave | boolean | 1 | n | 使用：true  不使用：false<br>(仅对开通从库配置客户生效) |
| 是否需要查询分摊邮费 | cal\_share\_post\_amount | boolean | 1 | n | 需要：true  不需要：false |

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

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | y | 订单相关数据 |
| 总数 | total\_count | Int | 11 | n | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单唯一键 | trade\_id | long |  |  | 订单唯一键 |
| 订单号 | trade\_no | String | 40 |  | 订单号 |
| 平台ID | platform\_id | Int | 4 |  | 平台ID（请点击[平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看对应关系） |
| 仓库类型 | warehouse\_type | Int | 4 |  | 仓库类型:<br>1、普通仓库,大于1为委外仓库(如京东仓储,物流宝等) |
| 原始单号 | src\_tids | String | 255 |  | 原始单号，如果有多个，以","分隔，且以增序排列,不重复,过长将被裁剪 |
| 平台支付帐号 | pay\_account | String | 128 |  | 平台支付帐号 |
| 订单状态 | trade\_status | int | 255 |  | 订单状态：<br>4 线下退款<br>5已取消<br>6 待转预订单(待审核)<br>7 待转已完成<br>10未付款<br>12待尾款<br>15等未付<br>16延时审核<br>19预订单前处理<br>20 审核前处理<br>21自流转待发货<br>23 异常预订单<br>24 换货预订单<br>25 待处理预订单<br>27待分配预订单 <br>30待客审<br>35待财审<br>55已审核<br>95已发货<br>96 成本确认（待录入计划成本，订单结算时有货品无计划成本）<br>101 已过账<br>110已完成 |
| 订单类型 | trade\_type | Int | 4 |  | 订单类型:<br>1、网店销售<br>2、线下订单<br>3、售后换货<br>4、批发业务<br>7、现款销售<br>8、分销<br>101、自定义类型一<br>102、自定义类型二<br>103、自定义类型三<br>104、自定义类型四<br>105、自定义类型五<br>106、自定义类型六 |
| 发货条件 | delivery\_term | Int | 4 |  | 发货条件:<br>1、款到发货 <br>2、货到付款(包含部分货到付款)<br>3、分期付款 |
| 冻结原因 | freeze\_reason | String | 6 |  | 冻结原因 |
| 退款状态 | refund\_status | Int | 4 |  | 退款状态:<br>0、无退款<br>1、申请退款<br>2、部分退款<br>3、全部退款 |
| 分销类别 | fenxiao\_type | Int | 4 |  | 分销类别:<br>0、非分销订单<br>1、代销<br>2、经销 |
| 分销商昵称 | fenxiao\_nick | String | 40 |  | 分销商昵称 |
| 下单时间 | trade\_time | String | 40 |  | 下单时间（毫秒级时间戳，例如：1631861379000） |
| 付款时间 | pay\_time | String | 40 |  | 付款时间，例如：2020-01-19 17:48:12 |
| 发货时间 | consign\_time | String | 40 |  | 发货时间（毫秒级时间戳，例如：1631861379000） |
| 客户网名 | buyer\_nick | String | 100 |  | 客户网名 |
| 收货人/收件人 | receiver\_name | String | 100 |  | 收货人/收件人 |
| 省份id | receiver\_province | Int | 11 |  | 省份id，可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 城市id | receiver\_city | Int | 11 |  | 城市id，可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地区id | receiver\_district | Int | 11 |  | 地区id，可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地址 | receiver\_address | String | 256 |  | 收件人地址 |
| 手机 | receiver\_mobile | String | 40 |  | 手机 |
| 固话 | receiver\_telno | String | 40 |  | 固话 |
| 邮编 | receiver\_zip | String | 20 |  | 邮编 |
| 省市县 | receiver\_area | String | 128 |  | 省市县 |
| 京东几环 | receiver\_ring | String | 20 |  | 京东几环 |
| 大头笔 | receiver\_dtb | String | 128 |  | 大头笔 |
| 送货时间 | to\_deliver\_time | String | 20 |  | 送货时间,例如：2020-10-19 00:00:00 |
| 异常订单原因 | bad\_reason | Int | 11 |  | 异常订单原因（位运算）:<br>2、修改地址<br>4、修改发票<br>8、更换仓库<br>16、修改备注<br>32、更换货品<br>128、拦截赠品<br>256、拦截换货<br>512、买家留言变化<br>1024、拦截平台已发货 |
| 物流单号 | logistics\_no | String | 40 |  | 物流单号 |
| 买家留言 | buyer\_message | String | 1024 |  | 买家留言 |
| 客服备注 | cs\_remark | String | 1024 |  | 客服备注 |
| 标旗 | remark\_flag | Int | 4 |  | 标旗（1 红、2 黄、3 绿、4 蓝、5 紫、6 橙、7 浅蓝、8 浅粉、9 深绿、10 桃红） |
| 打印备注 | print\_remark | String | 1024 |  | 打印备注 |
| 货品种类数 | goods\_type\_count | Decimal(19,4) |  |  | 货品种类数 |
| 货品总量 | goods\_count | Decimal(19,4) |  |  | 货品总量 |
| 货品总额 | goods\_amount | Decimal(19,4) |  |  | 货品总额 |
| 邮资 | post\_amount | Decimal(19,4) |  |  | 邮资（买家支付邮费） |
| 其它费用 | other\_amount | Decimal(19,4) |  |  | 其它费用 |
| 优惠 | discount | Decimal(19,4) |  |  | 优惠 |
| 应收金额 | receivable | Decimal(19,4) |  |  | 应收金额 |
| COD金额 | cod\_amount | Decimal(19,4) |  |  | 货到付款金额/COD金额 |
| 买家COD费用 | ext\_cod\_fee | Decimal(19,4) |  |  | 买家COD费用 |
| 预估货品成本 | goods\_cost | Decimal(19,4) |  |  | 预估货品成本 |
| 预估邮资成本 | post\_cost | Decimal(19,4) |  |  | 预估邮资成本 |
| 预估称重 | weight | Decimal(19,4) |  |  | 预估称重kg |
| 预估毛利 | profit | Decimal(19,4) |  |  | 预估毛利 |
| 税额 | tax | Decimal(19,4) |  |  | 税额 |
| 税率 | tax\_rate | Decimal(19,4) |  |  | 税率 |
| 佣金 | commission | Decimal(19,4) |  |  | 佣金 |
| 发票类别 | invoice\_type | Int | 4 |  | 发票类别:<br>0、不需要<br>1、普通发票<br>2、普通增值税发票<br>3、专用增值税发票 |
| 发票抬头 | invoice\_title | String | 1024 |  | 发票抬头 |
| 发票内容 | invoice\_content | String | 1024 |  | 发票内容 |
| 业务员 | salesman\_name | String | 40 |  | 业务员 |
| 审核人 | checker\_name | String | 40 |  | 审核人 |
| 财审人 | fchecker\_name | String | 40 |  | 财审人 |
| 签出人 | checkouter\_name | String | 40 |  | 签出人 |
| 出库单号 | stockout\_no | String | 40 |  | 出库单号（系统产生的出库单号） |
| 标记名称 | flag\_name | String | 32 |  | 标记名称 |
| 订单来源 | trade\_from | Int | 4 |  | 订单来源:<br>1、API抓单<br>2、手工建单<br>3、导入<br>4、复制订单<br>5、接口推送<br>6、补发订单<br>7、PDA选货开单 |
| 货品商家编码 | single\_spec\_no | String | 40 |  | 单一货品商家编码,多种货品为空,组合装时为组合装编码 |
| 原始货品数量 | raw\_goods\_count | Decimal(19,4) |  |  | 原始货品数量 |
| 原始货品种类数 | raw\_goods\_type\_count | Int | 6 |  | 原始货品种类数 |
| 币种 | currency | String | 20 |  | 币种 |
| 发票ID | invoice\_id | Int | 11 |  | 发票ID(自增生成)，0代表没有发票或已取消/已冲红 |
| 版本号 | version\_id | Int | 6 |  | 版本号 |
| 修改时间 | modified | String | 40 |  | 修改时间，例如：2021-01-29 01:49:40 |
| 递交时间 | created | String | 40 |  | 递交时间（毫秒级时间戳，例如：1631861379000） |
| 证件类别 | id\_card\_type | Int | 4 |  | 证件类别 |
| 店铺编号 | shop\_no | String | 20 |  | 店铺编号 |
| 店铺名称 | shop\_name | String | 128 |  | 店铺名称 |
| 店铺备注 | shop\_remark | String | 255 |  | 店铺备注 |
| 仓库编号 | warehouse\_no | String | 40 |  | 仓库编号 |
| 客户姓名 | customer\_name | String | 40 |  | 客户姓名 |
| 客户编码 | customer\_no | String | 40 |  | 客户编码 |
| 物流公司名称 | logistics\_name | String | 40 |  | 物流公司名称 |
| 物流公司编号 | logistics\_code | String | 60 |  | 物流公司编号 |
| 物流类型 | logistics\_type\_name | String |  |  | 物流类型 |
| 计划发货时间 | delay\_to\_time | String | 40 |  | 计划发货时间 |
| 订单标签 | trade\_label | String | 40 |  | 订单标签 |
| 店铺id | shop\_id | Int | 11 |  | 店铺id |
| 店铺平台id | shop\_platform\_id | Int | 11 |  | 店铺平台id |
| 子平台id | sub\_platform\_id | Int | 11 |  | 子平台id |
| 订单明细 | detail\_list | List<Map<String, Object>> |  |  | 订单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单唯一键 | trade\_id | long |  | y | 订单唯一键 |
| 订单明细唯一键 | rec\_id | long |  | y | 订单明细唯一键 |
| 平台ID | platform\_id | Int | 4 | y | 平台ID |
| 原始子单号 | src\_oid | String | 40 | y | 原始子单号 |
| 原始单号 | src\_tid | String | 40 | y | 原始单号 |
| 赠品方式 | gift\_type | Int | 4 | y | 赠品方式 0、非赠品<br>1、自动赠送 2、手工赠送 4、周期购赠送 8、平台赠送 |
| 退款状态 | refund\_status | Int | 4 | y | 退款状态:<br>0、无退款<br>1、已取消<br>2、已申请退款<br>3、待退款，平台已退款,系统未退款,但订单已审核,不能直接改成,除非驳回<br>4、等待取消,平台上取消退款,系统已退款,但订单已审核,不能直接改成,除非驳回<br>5、退款成功<br>6、未付款关闭，未付款的取消了 |
| 退款模式 | guarantee\_mode | Int | 4 | y | 平台状态:<br>10、未确认<br>20、待尾款<br>30、待发货<br>40、部分发货<br>50、已发货<br>60、已签收<br>70、已完成<br>80、已退款<br>90、已关闭 |
| 子单平台状态 | platform\_status | Int | 4 | y | 如果没有对应的原始单明细,则返回0.<br>平台状态:<br>10、未确认<br>20、待尾款<br>30、待发货<br>40、部分发货<br>50、已发货<br>60、已签收<br>70、已完成<br>80、已退款<br>90、已关闭 |
| 发货条件 | delivery\_term | Int | 4 | y | 发货条件:1、款到发货 2、货到付款(包含部分货到付款)<br>3、分期付款 |
| 货品数量 | num | Decimal(19,4) |  | y | 货品数量 |
| 标价 | price | Decimal(19,4) |  | y | 标价，手工新建时使用货品属性中的“零售价” |
| 售后退款数量 | refund\_num | Decimal(19,4) |  | y | 售后退款数量 |
| 成交价 | order\_price | Decimal(19,4) |  | y | 成交价,原始单折扣及分摊之后的价格 |
| 分摊后价格 | share\_price | Decimal(19,4) |  | y | 分摊后价格,进入ERP后再次调整的价格，默认值与order\_price一致 |
| 手工调整价 | adjust | Decimal(19,4) |  | y | 手工调整价,正数为加价,负数为减价,暂未处理 |
| 优惠 | discount | Decimal(19,4) |  | y | 优惠 |
| 分摊后总价 | share\_amount | Decimal(19,4) |  | y | 分摊后总价=share\_price\*num |
| 税率 | tax\_rate | Decimal(19,4) |  | y | 税率 |
| 已支付金额 | paid | Decimal(19,4) |  | y | 已支付金额 |
| 货品名称 | goods\_name | String | 255 | y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | y | 货品编号 |
| 规格名称 | spec\_name | String | 100 | y | 规格名称 |
| 商家编码 | spec\_no | String | 40 | y | 商家编码 |
| 规格码 | spec\_code | String | 40 | y | 规格码 |
| 组合装编码 | suite\_no | String | 40 | y | 组合装编码 |
| 组合装名称 | suite\_name | String | 255 | y | 如果是组合装拆分的，此为组合装名称 |
| 组合装数量 | suite\_num | Decimal(19,4) |  | y | 组合装数量,不受拆分合并影响 |
| 组合装分摊后总价 | suite\_amount | Decimal(19,4) |  | y | 组合装分摊后总价 |
| 组合装优惠 | suite\_discount | Decimal(19,4) |  | y | 组合装优惠 |
| 平台货品名称 | api\_goods\_name | String | 255 | y | 平台货品名称 |
| 平台规格名称 | api\_spec\_name | String | 100 | y | 平台规格名称 |
| 平台货品id | api\_goods\_id | String | 40 | Y | 平台货品id |
| 平台规格id | api\_spec\_id | String | 40 | Y | 平台规格id |
| 佣金 | commission | Decimal(19,4) |  | y | 佣金 |
| 货品类型 | goods\_type | Int | 4 | y | 货品类型 |
| 订单内部来源 | from\_mask | Int | 11 | y | 订单内部来源:<br>0：无来源<br>1：手机<br>2：聚划算<br>32：开具电子发票<br>2048：当日达<br>4096：次日达<br>8192：承诺时效<br>2097152：区域零售<br>4194304：拼多多厂家代打<br>8388608：周期购<br>1048576：预售单<br>33554432：前N有礼<br>524288：天猫物流升级<br>64：按需配送<br>256：承诺结构化/QIC<br>16384：商仓鸟配 |
| 子单备注 | remark | String | 255 | y | 子单备注 |
| 修改时间 | modified | String | 40 | y | 修改时间（毫秒级时间戳，例如：1631861379000） |
| 创建时间 | created | String |  | y | 创建时间（毫秒级时间戳，例如：1631861379000） |
| 自定义属性2 | prop2 | String | 255 | y | 自定义属性2 |
| 货品重量 | weight | Decimal(19,4) |  | y | 货品重量（子单货品预估总重量） |
| 图片路径 | img\_url | String | 255 | y | 图片路径 |
| 分摊邮费 | share\_post\_amount | Decimal(19,4) |  | y | 非退款成功/非未付款取消的订单中，(分摊后合计/分摊后合计之和)/对应原始单的邮费之和,相同原始单邮费不累加 |

**5.请求示例**

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2018-10-05 14:21:41"``,``"end_time"``:``"2018-10-20 14:21:41"``}]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>`$pars``=``array`<br>`(`<br>```'start_time'``=>``'2020-06-15 10:05:36'``,`<br>```'end_time'``=>``'2020-06-17 11:05:36'`<br>`);`<br>`$pager``=``new``Pager(50, 0, true);`<br>`$data``=``$client``->pageCall(``"sales.TradeQuery.queryHistorySelfOrderWithDetail"``,``$pager``,``$pars``);``//分页方法`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>``<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [`<br>```{`<br>```"logistics_name"``:``"邮政123"``,`<br>```"warehouse_type"``: 1,`<br>```"fenxiao_nick"``:``""``,`<br>```"consign_time"``: 1611821521000,`<br>```"post_amount"``: 0.0000,`<br>```"trade_time"``: 1611049692000,`<br>```"receiver_ring"``:``""``,`<br>```"raw_goods_type_count"``: 1,`<br>```"remark_flag"``: 0,`<br>```"receiver_dtb"``:``"杭州市 江干区"``,`<br>```"detail_list"``: [`<br>```{`<br>```"rec_id"``: 1045331,`<br>```"trade_id"``: 842375,`<br>```"platform_id"``: 0,`<br>```"src_oid"``:``"AD202101190001"``,`<br>```"src_tid"``:``"ZY202012240121"``,`<br>```"gift_type"``: 0,`<br>```"refund_status"``: 0,`<br>```"guarantee_mode"``: 2,`<br>```"delivery_term"``: 1,`<br>```"num"``: 1.0000,`<br>```"price"``: 0.0000,`<br>```"refund_num"``: 0.0000,`<br>```"order_price"``: 0.0000,`<br>```"share_price"``: 0.0000,`<br>```"adjust"``: 0.0000,`<br>```"discount"``: 0.0000,`<br>```"share_amount"``: 0.0000,`<br>```"paid"``: 0.0000,`<br>```"goods_name"``:``"老爸推荐--检测合格304不锈钢儿童筷子(1双)"``,`<br>```"tax_rate"``: 0.0000,`<br>```"goods_no"``:``"BC00000101"``,`<br>```"spec_name"``:``"老爸推荐--检测合格304不锈钢儿童筷子(1双)"``,`<br>```"spec_no"``:``"BC00000101"``,`<br>```"spec_code"``:``"shuang"``,`<br>```"suite_no"``:``""``,`<br>```"suite_name"``:``""``,`<br>```"suite_num"``: 0.0000,`<br>```"suite_amount"``: 0.0000,`<br>```"suite_discount"``: 0.0000,`<br>```"api_goods_name"``:``"老爸推荐--检测合格304不锈钢儿童筷子(1双)"``,`<br>```"api_spec_name"``:``"老爸推荐--检测合格304不锈钢儿童筷子(1双)"``,`<br>```"commission"``: 0.0000,`<br>```"goods_type"``: 1,`<br>```"from_mask"``: 0,`<br>```"remark"``:``""``,`<br>```"modified"``: 1611821521000,`<br>```"img_url"``:``""``,`<br>```"platform_status"``: 0,`<br>```"created"``: 1611049724000,`<br>```"prop2"``:``""``,`<br>```"weight"``: 0.0000,`<br>```"api_goods_id"``:``""``,`<br>```"api_spec_id"``:``""`<br>```}`<br>```],`<br>```"bad_reason"``: 0,`<br>```"print_remark"``:``""``,`<br>```"discount"``: 0.0000,`<br>```"other_amount"``: 0.0000,`<br>```"pay_account"``:``""``,`<br>```"tax_rate"``: 0.0000,`<br>```"raw_goods_count"``: 1.0000,`<br>```"to_deliver_time"``:``""``,`<br>```"fchecker_name"``:``"系统"``,`<br>```"trade_id"``: 842375,`<br>```"trade_label"``:``""``,`<br>```"shop_remark"``:``"1"``,`<br>```"invoice_id"``: 0,`<br>```"modified"``:``"2021-01-29 01:49:40"``,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"checker_name"``:``"admin"``,`<br>```"receiver_area"``:``"浙江省 杭州市 江干区"``,`<br>```"customer_no"``:``"KH202101150020"``,`<br>```"refund_status"``: 0,`<br>```"receiver_province"``: 330000,`<br>```"buyer_message"``:``""``,`<br>```"created"``: 1611049724000,`<br>```"weight"``: 0.0000,`<br>```"tax"``: 0.0000,`<br>```"logistics_code"``:``"wtt123"``,`<br>```"shop_name"``:``"wdtapi3-test"``,`<br>```"shop_platform_id"``: 127,`<br>```"pay_time"``:``"2021-01-19 17:48:12"``,`<br>```"src_tids"``:``"ZY202012240121"``,`<br>```"shop_id"``: 290,`<br>```"checkouter_name"``:``"系统"``,`<br>```"trade_no"``:``"ORDER202101190014"``,`<br>```"id_card_type"``: 0,`<br>```"freeze_reason"``:``"无"``,`<br>```"single_spec_no"``:``"BC00000101"``,`<br>```"salesman_name"``:``"admin"``,`<br>```"receiver_city"``: 330100,`<br>```"invoice_title"``:``""``,`<br>```"goods_type_count"``: 1,`<br>```"sub_platform_id"``: 0,`<br>```"goods_count"``: 1.0000,`<br>```"cod_amount"``: 0.0000,`<br>```"flag_name"``:``"无"``,`<br>```"receiver_telno"``:``""``,`<br>```"receiver_zip"``:``""``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"invoice_content"``:``""``,`<br>```"trade_status"``: 110,`<br>```"post_cost"``: 0.0000,`<br>```"receiver_name"``:``"chend270"``,`<br>```"commission"``: 0.0000,`<br>```"invoice_type"``: 0,`<br>```"currency"``:``""``,`<br>```"profit"``: 0.0000,`<br>```"trade_from"``: 2,`<br>```"delivery_term"``: 1,`<br>```"logistics_no"``:``"765432342323232"``,`<br>```"goods_amount"``: 0.0000,`<br>```"goods_cost"``: 0.0000,`<br>```"receiver_district"``: 330104,`<br>```"stockout_no"``:``"CKDH2021012820"``,`<br>```"receivable"``: 0.0000,`<br>```"version_id"``: 3,`<br>```"receiver_mobile"``:``"132222222228"``,`<br>```"buyer_nick"``:``"MO2"``,`<br>```"fenxiao_type"``: 0,`<br>```"cs_remark"``:``""``,`<br>```"platform_id"``: 0,`<br>```"trade_type"``: 2,`<br>```"receiver_address"``:``"绿谷"``,`<br>```"logistics_type_name"``:``"中国邮政"``,`<br>```"ext_cod_fee"``: 0.0000,`<br>```"customer_name"``:``"chend270"``,`<br>```"delay_to_time"``:``""`<br>```}`<br>```]`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于60分钟"``}` | |
