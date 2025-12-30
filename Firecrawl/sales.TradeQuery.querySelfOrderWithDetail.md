---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.querySelfOrderWithDetail"
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

****sales.TradeQuery.querySelfOrderWithDetail**（订单查询--仅返回自有平台、线下平台订单信息）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP系统内自有平台及线下平台订单信息 |
| **1.2 适用版本：** 客户端 V1.5.9.8及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为60分钟。 |
| **1.5注意事项：** **权限校验：【店铺权限】**<br>仅返回自有平台、线下平台订单信息<br>通过从后往前翻页的方式可以避免漏单问题。 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

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
| 查询参数 | params | Map<String, Object> |  | y | 查询参数 |
| 分页 | pager | Pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | y | 修改起始时间，若无订单编号/原始单号/物流单号，则为必填。示例：“ 2021-11-11 00:00:00” |
| 结束时间 | end\_time | String | 40 | y | 修改结束时间，上同开始时间。示例：“ 2021-11-11 01:00:00” |
| 仓库编号 | warehouse\_no | String | 40 | n | 仓库编号 |
| 订单状态 | status | String | 255 | n | 若多个状态则以“，”隔开。<br>订单状态:  <br>4 线下退款<br>5已取消<br>6 待转预订单(待审核)<br>7 待转已完成<br>10未付款<br>12待尾款<br>15等未付<br>16延时审核<br>19预订单前处理<br>20 审核前处理<br>21自流转待发货<br>23 异常订单<br>24 换货预订单<br>25 待处理预订单<br>27待分配预订单 <br>30待客审<br>35待财审<br>40审核中<br>55已审核<br>95已发货<br>96 成本确认（待录入计划成本，订单结算时有货品无计划成本）<br>101 已过账<br>110已完成 |
| 订单编号 | trade\_no | String | 40 | n | 订单编号 |
| 店铺编号 | shop\_no | String | 20 | n | 店铺编号（暂不支持批量查询） |
| 物流单号 | logistics\_no | String | 40 | n | 物流单号，（V1.4.9.9版本以上支持按照物流单号查询不传入时间范围） |
| 原始单号 | src\_tid | String | 40 | n | 原始单号, 多个原始单号之间使用英文逗号分隔 |
| 是否使用从库查询 | is\_slave | boolean | 1 | n | 使用：true   不使用：false<br>（仅对开通从库配置客户生效） |
| 是否计算分摊邮费 | cal\_share\_post\_amount | boolean | 1 | n | 是否计算分摊邮费<br>默认false<br>计算：true<br>不计算：false |
| 订单来源 | trade\_from | String | 40 | n | 订单来源<br>1、API抓单<br>2、手工建单<br>3、导入<br>4、复制订单<br>5、接口推送<br>6、补发订单<br>7、PDA选货开单<br>8、分销补发订单 |
| 排序类型 | order\_type | Int | 4 | n | 0：默认排序<br>1：修改时间降序 |
| 时间类型 | time\_type | Int | 4 | n | 1：修改时间<br>2：付款时间<br>3：下单时间<br>默认1 |
| 是否返回赠品关联关系 | need\_gift\_relation | boolean | 1 | n | 0：不返回<br>1：返回<br>默认1 |
| 是否强制指定src\_tid精准查询（避免模糊查） | accurate\_query | boolean | 1 | n | 是否精准查询：<br>0：（默认值）否，  <br>1：是； |
| 是否截取物流单号 | cut\_logistics\_no | boolean | 1 | n | 0: (默认值) 不截取<br>1：截取 |

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

****order****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单唯一键 | trade\_id | long | 10 | y | 订单唯一键 |
| 订单编号 | trade\_no | String | 40 | y | 订单编号（旺店通系统订单号） |
| 平台ID | platform\_id | Int | 4 | y | 平台ID（请点击[平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看对应关系） |
| 仓库类型 | warehouse\_type | Int | 4 | y | 仓库类型:<br>1、普通仓库,大于1为委外仓库(如京东仓储,物流宝等)，如订单无仓库的话，则不返回该字段 |
| 原始单号 | src\_tids | String | 255 | y | 原始单号（平台订单号），如果有多个，以","分隔，且以增序排列,不重复,过长将被裁剪 |
| 平台支付帐号 | pay\_account | String | 128 | y | 平台支付帐号 |
| 订单状态 | trade\_status | int | 255 | y | 订单状态:  <br>4 线下退款<br>5已取消<br>6 待转预订单(待审核)<br>7 待转已完成<br>10未付款<br>12待尾款<br>15等未付<br>16延时审核<br>19预订单前处理<br>20 审核前处理<br>21自流转待发货<br>23 异常订单<br>24 换货预订单<br>25 待处理预订单<br>27待分配预订单 <br>30待客审<br>35待财审<br>40审核中<br>55已审核<br>95已发货<br>96 成本确认（待录入计划成本，订单结算时有货品无计划成本）<br>101 已过账<br>110已完成 |
| 订单类型 | trade\_type | Int | 4 | y | 订单类型: <br>1、网店销售<br>2、线下订单<br>3、售后换货<br>4、批发业务<br>5、保修换新<br>6、保修完成<br>7、现款销售<br>8、分销订单<br>101、自定义类型一<br>102、自定义类型二<br>103、自定义类型三<br>104、自定义类型四<br>105、自定义类型五<br>106、自定义类型六<br>107、自定义类型七<br>108、自定义类型八<br>109、自定义类型九<br>110、自定义类型十<br>（与ERP中自定义类型的映射关系 [，点击链接查看](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E8%AE%A2%E5%8D%95%E6%9F%A5%E8%AF%A2%E3%80%81%E9%94%80%E5%94%AE%E5%87%BA%E5%BA%93%E5%8D%95)） |
| 发货条件 | delivery\_term | Int | 4 | y | 发货条件:<br>1、款到发货 <br>2、货到付款(包含部分货到付款)<br>3、分期付款<br>4、挂账 |
| 京东几环 | receiver\_ring | String | 20 | y | 京东几环（淘宝模糊化后的买家昵称） |
| 冻结原因 | freeze\_reason | String | 32 | y | 冻结原因 |
| 退款状态 | refund\_status | Int | 4 | y | 退款状态: <br>0、无退款<br>1、申请退款<br>2、部分退款<br>3、全部退款 |
| 分销类别 | fenxiao\_type | Int | 4 | y | 分销类别: <br>0、非分销订单<br>1、代销<br>2、经销 |
| 分销商昵称 | fenxiao\_nick | String | 40 | y | 分销商昵称 |
| 下单时间 | trade\_time | String | 40 | y | 下单时间（毫秒级时间戳，例如：1631861379000） |
| 付款时间 | pay\_time | String | 40 | y | 付款时间，例如：2020-10-19 00:00:00 |
| 发货时间 | consign\_time | String | 40 | y | 发货时间，订单未发货不返回该字段（毫秒级时间戳，例如：1631861379000） |
| 客户网名 | buyer\_nick | String | 100 | y | 客户网名 |
| 收货人/收件人 | receiver\_name | String | 100 | y | 收货人/收件人 |
| 省份id | receiver\_province | Int | 11 | y | 省份id，可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 城市id | receiver\_city | Int | 11 | y | 城市id，可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地区id | receiver\_district | Int | 11 | y | 地区id，可参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地址 | receiver\_address | String | 256 | y | 收件人地址 |
| 手机 | receiver\_mobile | String | 40 | y | 手机 |
| 固话 | receiver\_telno | String | 40 | y | 固话 |
| 邮编 | receiver\_zip | String | 20 | y | 邮编 |
| 地区 | receiver\_area | String | 128 | y | 省市区空格分隔 |
| 大头笔 | receiver\_dtb | String | 128 | y | 大头笔 |
| 异常订单原因 | bad\_reason | Int | 11 | y | 异常订单原因（位运算）: <br>2、修改地址<br>4、修改发票<br>8、更换仓库<br>16、修改备注<br>32、更换货品<br>128、拦截赠品<br>256、拦截换货<br>512、买家留言变化<br>1024、拦截平台已发货 |
| 物流单号 | logistics\_no | String | 40 | y | 物流单号 |
| 买家留言 | buyer\_message | String | 1024 | y | 买家留言 |
| 客服备注 | cs\_remark | String | 1024 | y | 客服备注 |
| 标旗 | remark\_flag | Int | 4 | y | 标旗（1 红、2 黄、3 绿、4 蓝、5 紫、6 橙、7 浅蓝、8 浅粉、9 深绿、10 桃红） |
| 打印备注 | print\_remark | String | 1024 | y | 打印备注 |
| 货品种类数 | goods\_type\_count | Decimal(19,4) |  | y | 货品种类数 |
| 货品总量 | goods\_count | Decimal(19,4) |  | y | 货品总量 |
| 总货款 | goods\_amount | Decimal(19,4) |  | y | 总货款（折前总额） |
| 邮费 | post\_amount | Decimal(19,4) |  | y | 邮费（买家支付邮费） |
| 其他费用 | other\_amount | Decimal(19,4) |  | y | 其他费用 |
| 优惠 | discount | Decimal(19,4) |  | y | 优惠 |
| 应收 | receivable | Decimal(19,4) |  | y | 应收 |
| COD金额 | cod\_amount | Decimal(19,4) |  | y | COD金额（货到付款金额） |
| 买家COD费用 | ext\_cod\_fee | Decimal(19,4) |  | y | 买家COD费用 |
| 预估货品成本 | goods\_cost | Decimal(19,4) |  | y | 货品预估成本 |
| 预估邮资成本 | post\_cost | Decimal(19,4) |  | y | 预估邮资成本 |
| 预估重量 | weight | Decimal(19,4) |  | y | 预估重量（kg） |
| 预估毛利 | profit | Decimal(19,4) |  | y | 预估毛利 |
| 税额 | tax | Decimal(19,4) |  | y | 税额 |
| 税率 | tax\_rate | Decimal(19,4) |  | y | 税率 |
| 佣金 | commission | Decimal(19,4) |  | y | 佣金 |
| 发票类型 | invoice\_type | Int | 4 | y | 发票类型: <br>0：不需要<br>1：普通发票<br>2：增值税普通发票<br>3：增值税专用发票 |
| 发票抬头 | invoice\_title | String | 1024 | y | 发票抬头 |
| 发票内容 | invoice\_content | String | 1024 | y | 发票内容 |
| 业务员 | salesman\_name | String | 40 | y | 业务员 |
| 审核人 | checker\_name | String | 40 | y | 审核人 |
| 财审人 | fchecker\_name | String | 40 | y | 财审人 |
| 签出人 | checkouter\_name | String | 40 | y | 签出人 |
| 出库单号 | stockout\_no | String | 40 | y | 出库单号（系统产生的出库单号） |
| 标记名称 | flag\_name | String | 32 | y | 标记名称 |
| 订单来源 | trade\_from | Int | 4 | y | 订单来源: <br>1、API抓单<br>2、手工建单<br>3、导入<br>4、复制订单<br>5、接口推送<br>6、补发订单<br>7、PDA选货开单<br>8、分销补发订单 |
| 货品商家编码 | single\_spec\_no | String | 40 | y | 货品商家编码,多种货品为空,组合装时为组合装编码 |
| 原始货品数量 | raw\_goods\_count | Decimal(19,4) |  | y | 原始货品数量 |
| 原始货品种类数 | raw\_goods\_type\_count | Int | 6 | y | 原始货品种类数 |
| 币种 | currency | String | 20 | y | 币种 |
| 发票ID | invoice\_id | Int | 11 | y | 发票ID(自增生成)，0代表没有发票或已取消/已冲红 |
| 版本号 | version\_id | Int | 6 | y | 版本号 |
| 修改时间 | modified | String | 40 | y | 修改时间，例如：2020-10-19 00:00:00 |
| 递交时间 | created | String | 40 | y | 递交时间（毫秒级时间戳，例如：1631861379000） |
| 审核时间 | check\_time | String | 40 | y | 审核时间 |
| 证件类别 | id\_card\_type | Int | 4 | y | 证件类别 |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺名称 | shop\_name | String | 128 | y | 店铺名称 |
| 店铺备注 | shop\_remark | String | 255 | y | 店铺备注 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号，如订单无仓库的话，则不返回该字段 |
| 客户姓名 | customer\_name | String | 40 | y | 客户姓名 |
| 客户编码 | customer\_no | String | 40 | y | 客户编码 |
| 物流公司名称 | logistics\_name | String | 40 | y | 物流公司名称 |
| 物流公司编号 | logistics\_code | String | 60 | y | 物流公司编号 |
| 物流类型 | logistics\_type\_name | String | 64 | y | 物流类型名称 |
| 送货时间 | to\_deliver\_time | String | 20 | y | 送货时间,例如：2020-10-19 00:00:00 |
| 计划发货时间 | delay\_to\_time | String | 40 | y | 计划发货时间 |
| 最晚发货时间 | estimate\_consign\_time | String | 40 | y | 最晚发货时间 |
| 店铺id | shop\_id | Int | 6 | y | 店铺id |
| 仓库id | warehouse\_id | Int | 6 | y | 仓库id |
| 体积 | volume | Decimal(19,4) |  | y | 体积 |
| 订单标签 | trade\_label | String | 40 | y | 订单标签 |
| 订单掩码 | trade\_mask | Int | 11 | y | 1：使用智选物流<br>2：货品标签<br>4：预订单自动激活失败<br>16：订单货品指定批次<br>32：平台自动流转仓库<br>64：部分发货<br>128：全部发货<br>256：优先占用<br>512：待分配转审核失败或订单审核失败<br>1024：催未付款订单短信发送标记<br>2048：拆分<br>在判断的时候使用&运算 |
| 店铺平台id | shop\_platform\_id | Int | 4 | y | 店铺平台id |
| 子平台id | sub\_platform\_id | Int | 4 | y | 子平台id |
| 包装 | package\_name | String | 356 | y | 包装 |
| 包装id | package\_id | Int | 40 | y | 包装id |
| 包装成本 | package\_cost | Decimal(19,4) |  | y | 包装成本（计划成本） |
| 已付 | paid | Decimal(19,4) |  | y | 已付 |
| 大件类型 | large\_type | Int | 4 | y | 大件类型<br>1：普通套件<br>2：独立套件<br>3：分组单发,未使用<br>-1：非单发件    取子单中的最大值 |
| 赠品标记 | gift\_mask | Int | 4 | y | 赠品标记<br>1：自动赠送<br>2：手工赠送<br>4：回购赠送<br>8：平台赠送<br>（注意：如果是3，则表示既有自动赠送也有手工赠送“1+2”） |
| 客户id | customer\_id | Int | 11 | y | 客户id |
| 其他成本 | other\_cost | Decimal(19,4) |  | y | 其他成本 |
| 不可合并拆分 | is\_sealed | boolean | 1 | y | 不可合并拆分 |
| 客户类型 | customer\_type | Int | 4 | y | 客户类型（0：普通客户；1：分销商；2：线下批发） |
| 物流公司id | logistics\_id | Int | 11 | y | 物流公司id |
| 取消原因 | cancel\_reason | String | 256 | y | 取消原因 |
| 驳回原因 | revert\_reason | String | 256 | y | 驳回原因 |
| 订单标签mask | new\_trade\_label | String |  | y | 订单标签掩码 |
| 分销原始单号 | fenxiao\_tid | String |  | y | 分销原始单号（无长度限制） |
| 客户唯一编码 | customer\_unique\_id | String | 256 | y | 客户唯一编码 |
| 平台标签 | platform\_label | String |  |  | 平台标签 |
| 分销商编号 | fenxiao\_nick\_no | String |  | n | 分销商编号 |
| 预物流同步单号 | pre\_sync\_logistics\_no | String | 40 | y | 预物流同步单号 |
| 预物流同步时间 | pre\_sync\_time | String |  | y | 预物流同步时间 |
| 订单结束时间 | end\_time | String |  | y | 订单结束时间 |
| 订单结算时间 | settle\_time | String |  | y | 订单结算时间 |
| 订单明细 | detail\_list | List<Map<String, Object>> |  | y | 订单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单唯一键 | trade\_id | long |  | y | 订单唯一键 |
| 订单明细唯一键 | rec\_id | long |  | y | 订单明细唯一键 |
| 平台ID | platform\_id | Int | 4 | y | 平台ID |
| 原始子单号 | src\_oid | String | 40 | y | 原始子单号 |
| 原始单号 | src\_tid | String | 40 | y | 原始单号 |
| 赠品方式 | gift\_type | Int | 4 | y | 赠品方式 <br>0非赠品<br>1自动赠送<br>2手工赠送<br>4周期购赠送<br>8平台赠送<br>32阶梯满赠 <br>64CRM追加赠送 <br>65 主品  （1.5.7.0版本前主品枚举值为128） |
| 支付状态 | pay\_status | int | 4 | y | 0:未付款 1:部分付款 2:已付款（原始订单的支付状态） |
| 退款状态 | refund\_status | Int | 4 | y | 退款状态: <br>0、无退款<br>1、取消退款<br>2、申请退款<br>3、待退款<br>4、待还原<br>5、退款成功<br>6、已退（未付款关闭，未付款的取消了） |
| 退款模式 | guarantee\_mode | Int | 4 | y | 退款模式: <br>1、担保<br>2、非担保<br>3、在线非担保 |
| 子单平台状态 | platform\_status | Int | 4 | y | 如果没有对应的原始单明细,则返回0.<br>平台状态:<br>10、未确认<br>20、待尾款<br>30、待发货<br>40、部分发货<br>50、已发货<br>60、已签收<br>70、已完成<br>80、已退款<br>90、已关闭 |
| 发货条件 | delivery\_term | Int | 4 | y | 发货条件:1、款到发货 2、货到付款(包含部分货到付款)<br>3、分期付款 |
| 数量 | num | Decimal(19,4) |  | y | 数量 |
| 标价 | price | Decimal(19,4) |  | y | 标价，手工新建时使用货品属性中的“零售价” |
| 售后退款数量 | refund\_num | Decimal(19,4) |  | y | 售后退款数量 |
| 成交价 | order\_price | Decimal(19,4) |  | y | 成交价,原始单折扣及分摊之后的价格 |
| 分摊后价格 | share\_price | Decimal(19,4) |  | y | 分摊后价格，进入ERP后再次调整的价格，默认值与order\_price一致 |
| 手工调整价 | adjust | Decimal(19,4) |  | y | 手工调整价,正数为加价,负数为减价,暂未处理 |
| 优惠 | discount | Decimal(19,4) |  | y | 优惠 |
| 分摊后总价 | share\_amount | Decimal(19,4) |  | y | 分摊后总价 |
| 税率 | tax\_rate | Decimal(19,4) |  | y | 税率 |
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
| 货品id | goods\_id | Int | 11 | Y | 货品id（系统货品主键） |
| 单品id | spec\_id | Int | 11 | Y | 单品id(系统单品主键) |
| 佣金 | commission | Decimal(19,4) |  | y | 佣金 |
| 货品类型 | goods\_type | Int | 4 | y | 货品类型:<br>0：其它<br>1：销售货品<br>2：原材料<br>3：包装物<br>4：周转材料<br>5：虚拟商品<br>6：固定资产<br>8：分装箱 |
| 订单内部来源 | from\_mask | Int | 11 | y | 订单内部来源:<br>0：无来源<br>1：手机<br>2：聚划算<br>32：开具电子发票<br>2048：当日达<br>4096：次日达<br>8192：承诺时效<br>2097152：区域零售<br>4194304：拼多多厂家代打<br>8388608：周期购<br>1048576：预售单<br>33554432：前N有礼<br>524288：天猫物流升级<br>64：按需配送<br>256：承诺结构化/QIC<br>16384：商仓鸟配 |
| 订单内部来源扩展 | from\_mask\_ext | Int | 11 | y | 订单内部来源扩展:<br>2：小时达订单<br>4：自选物流<br>16：国补订单 |
| 子单备注 | remark | String | 255 | y | 子单备注 |
| 修改时间 | modified | String | 40 | y | 修改时间（毫秒级时间戳，例如：1631861379000） |
| 创建时间 | created | String | 40 | y | 创建时间（毫秒级时间戳，例如：1631861379000） |
| 单品自定义属性1 | prop1 | String | 255 | y | 单品自定义属性1 |
| 单品自定义属性2 | prop2 | String | 255 | y | 单品自定义属性2 |
| 单品自定义属性3 | prop3 | String | 255 | y | 单品自定义属性3 |
| 单品自定义属性4 | prop4 | String | 255 | y | 单品自定义属性4 |
| 单品自定义属性5 | prop5 | String | 255 | y | 单品自定义属性5 |
| 单品自定义属性6 | prop6 | String | 255 | y | 单品自定义属性6 |
| 货品重量 | weight | Decimal(19,4) |  | y | 货品重量（子单预估货品总重量） |
| 图片路径 | img\_url | String | 255 | y | 图片路径 |
| 实发数量 | actual\_num | Decimal(19,4) |  | y | 实发数量（此数量为发货数量,删除操作等于将此值设置为0） |
| 条码 | barcode | String | 50 | y | 条码 |
| 已付 | paid | Decimal(19,4) |  | y | 已付 |
| 组合装id | suite\_id | Int | 11 | y | 组合装id |
| bind\_oid | bind\_oid | String | 50 | y | bind\_oid |
| 打印组合装 | print\_suite\_mode | Int | 4 | y | 打印组合装<br>0：组合装明细<br>1：组合装及明细<br>2：组合装 |
| 天猫物流升级信息 | flag | Int | 11 | y | 1：天猫物流升级-顺丰配送<br>2：需要回传<br>4：天猫物流升级-按需配送<br>8：天猫物流升级-承诺发货时效<br>16：天猫物流升级-承诺达时效<br>32：天猫物流升级-预售下沉<br>64：天猫物流升级-预计到货时效<br>128：天猫物流升级-配送线路异常<br>1024：定金链接<br>2048：补款链接<br>4096：确认收货<br>（mask类型值. 在判断的时候使用&运算） |
| 库存保留情况 | stock\_state | Int | 4 | y | 库存保留情况<br>0：未保留（取消的订单或完成）<br>1：无库存记录<br>2：未付款<br>3：已保留待审核<br>4：待发货<br>5：预订单库存 |
| 平台已发货 | is\_consigned | boolean | 1 | y | 平台已发货 |
| 是否付款 | is\_received | Int | 11 | y | 是否付款 |
| 平台类目主键 | cid | Int |  | y | 平台类目主键 |
| 最后更新时间 | modified\_date | String |  | y | 最后更新时间，DateTime格式 |
| 创建时间 | created\_date | String |  | y | 创建时间，DateTime格式 |
| 分摊邮费 | share\_post\_price | Decimal(19,4) |  | y | 分摊邮费 |
| 发票内容 | invoice\_content | String | 255 | y | 发票内容 |
| 支付时间 | pay\_time | String |  | y | 支付时间，DateTime格式，取自原始订单支付时间 |
| 货品简称 | short\_name | String |  | y | 货品简称 |
| 赠品关联关系 | goods\_gift\_relation | String |  | y | 赠品关联关系 |
| 成本价 | avg\_cost | Decimal(19,4) |  | y | 成本价 |

**5.请求示例**

|     |     |
| --- | --- |
| JSON | ```<br>[{<br>"start_time": "2020-01-01 00:00:00",<br>"end_time": "2020-01-20 00:00:00"<br>}]<br>``` |
| PHP | ```<br><php<br>header("Content-Type: text/html; charset=UTF-8");<br>date_default_timezone_set("Asia/Shanghai");<br>require_once('wdtsdk.php');<br> <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");<br> <br>$parMap = new stdClass();<br>$parMap->start_time = "2020-01-01 00:00:00";<br>$parMap->end_time = "2020-01-20 00:00:00";<br> <br>$pager = new Pager(1, 0, true);<br> <br>$response = $client->pageCall("sales.TradeQuery.querySelfOrderWithDetail", $pager, $parMap);<br> <br>?><br>``` |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "total_count": 1,<br>        "order": [<br>            {<br>                "fenxiao_nick": "",<br>                "post_amount": 0,<br>                "estimate_consign_time": "",<br>                "trade_time": 1673366400000,<br>                "receiver_ring": "",<br>                "remark_flag": 0,<br>                "detail_list": [<br>                    {<br>                        "trade_id": 1028159,<br>                        "platform_id": 127,<br>                        "src_oid": "zd2023010898998",<br>                        "src_tid": "zd2023010898998",<br>                        "gift_type": 0,<br>                        "goods_gift_relation": "",<br>                        "refund_status": 0,<br>                        "guarantee_mode": 1,<br>                        "delivery_term": 1,<br>                        "num": 1,<br>                        "price": 10,<br>                        "refund_num": 0,<br>                        "order_price": 10,<br>                        "share_price": 10,<br>                        "adjust": 0,<br>                        "suite_id": 0,<br>                        "bind_oid": "",<br>                        "print_suite_mode": 0,<br>                        "flag": 0,<br>                        "stock_state": 0,<br>                        "is_consigned": false,<br>                        "is_received": 0,<br>                        "cid": 0,<br>                        "modified_date": "2023-01-11 14:36:01",<br>                        "created_date": "2023-01-11 14:31:12",<br>                        "discount": 0,<br>                        "share_amount": 10,<br>                        "paid": 0,<br>                        "goods_name": "zzdd",<br>                        "tax_rate": 0,<br>                        "goods_no": "951027",<br>                        "spec_name": "测试",<br>                        "spec_no": "951027",<br>                        "spec_code": "951027",<br>                        "suite_no": "",<br>                        "suite_name": "",<br>                        "suite_num": 0,<br>                        "suite_amount": 0,<br>                        "suite_discount": 0,<br>                        "api_goods_name": "951027",<br>                        "api_spec_name": "",<br>                        "commission": 0,<br>                        "goods_type": 1,<br>                        "from_mask": 0,<br>                        "remark": "",<br>                        "modified": 1673418961000,<br>                        "img_url": "",<br>                        "platform_status": 30,<br>                        "actual_num": 1,<br>                        "created": 1673418672000,<br>                        "prop1": "杏色",<br>                        "prop2": "22222",<br>                        "weight": 0,<br>                        "api_goods_id": "951027",<br>                        "api_spec_id": "951027",<br>                        "rec_id": 1271983,<br>                        "pay_status": 2,<br>                        "barcode": "951027",<br>                        "spec_id": 235348,<br>                        "goods_id": 83223,<br>                        "post_amount": 0,<br>                        "tid": "zd2023010898998",<br>                        "invoice_content": "",<br>                        "share_post_price": 0,<br>                        "pay_time": ""<br>                    }<br>                ],<br>                "bad_reason": 0,<br>                "discount": 0,<br>                "pay_account": "123456789",<br>                "package_id": 0,<br>                "raw_goods_count": 1,<br>                "fchecker_name": "系统",<br>                "trade_id": 1028159,<br>                "trade_label": "",<br>                "checker_name": "zd3",<br>                "large_type": 0,<br>                "refund_status": 0,<br>                "receiver_province": 0,<br>                "buyer_message": "",<br>                "logistics_code": "KDLL001",<br>                "shop_platform_id": 127,<br>                "trade_mask": 0,<br>                "src_tids": "zd2023010898998",<br>                "shop_id": 290,<br>                "package_cost": "0.0000",<br>                "checkouter_name": "系统",<br>                "id_card_type": 0,<br>                "freeze_reason": "无",<br>                "single_spec_no": "951027",<br>                "sub_platform_id": 0,<br>                "goods_count": 1,<br>                "invoice_content": "",<br>                "post_cost": 0,<br>                "receiver_name": "zd",<br>                "commission": 0,<br>                "currency": "",<br>                "trade_from": 1,<br>                "delivery_term": 1,<br>                "gift_mask": 0,<br>                "logistics_no": "2022301110001",<br>                "goods_cost": 11,<br>                "receiver_district": 0,<br>                "receivable": 10,<br>                "receiver_mobile": "11111",<br>                "cs_remark": "",<br>                "receiver_address": "1111",<br>                "ext_cod_fee": 0,<br>                "customer_name": "zd",<br>                "customer_id": 716844,<br>                "warehouse_id": 311,<br>                "logistics_name": "wdt_快弟来了",<br>                "warehouse_type": 1,<br>                "consign_time": 1673418961000,<br>                "raw_goods_type_count": 1,<br>                "receiver_dtb": "无 无",<br>                "other_cost": 0,<br>                "print_remark": "",<br>                "other_amount": 0,<br>                "tax_rate": 0,<br>                "to_deliver_time": "",<br>                "shop_remark": "ljcs",<br>                "invoice_id": 0,<br>                "modified": "2023-01-11 14:37:00",<br>                "shop_no": "wdtapi3-test",<br>                "receiver_area": "1111",<br>                "customer_no": "KH202103011079",<br>                "created": 1673418672000,<br>                "weight": 0,<br>                "tax": 0,<br>                "shop_name": "wdtapi3-test",<br>                "pay_time": "2023-01-11 00:00:00",<br>                "volume": 0,<br>                "is_sealed": false,<br>                "trade_no": "JY202301110027",<br>                "check_time": "2023-01-11 14:31:51",<br>                "customer_type": 0,<br>                "salesman_name": "系统",<br>                "receiver_city": 0,<br>                "invoice_title": "",<br>                "goods_type_count": 1,<br>                "cod_amount": 50,<br>                "flag_name": "无",<br>                "logistics_id": 332,<br>                "receiver_telno": "",<br>                "receiver_zip": "987654",<br>                "warehouse_no": "wdtapi3-test",<br>                "trade_status": 110,<br>                "invoice_type": 0,<br>                "new_trade_label": "0",<br>                "profit": -1,<br>                "goods_amount": 10,<br>                "stockout_no": "CK202301115",<br>                "version_id": 1,<br>                "buyer_nick": "zd",<br>                "cancel_reason": "无",<br>                "fenxiao_type": 0,<br>                "revert_reason": "无",<br>                "platform_id": 127,<br>                "package_name": "未知",<br>                "paid": 0,<br>                "trade_type": 1,<br>                "logistics_type_name": "快弟来了",<br>                "delay_to_time": ""<br>            }<br>        ]<br>    }<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{"status":100,"message":"您的查询时间过宽,查询时间不能大于60分钟"}<br>``` |

106、自定义类型六

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1