---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.search"
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

**aftersales.refund.Refund.search**（退换单查询）

**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP销售退货（换货）订单信息 |
| **1.2 适用版本：** 客户端 V1.5.9.0及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** 请求时间最大跨度为30天。 |
| **1.5注意事项：** **【权限校验】：店铺权限**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台货品数据，相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")，拼多多请自行对接平台获取。<br>本接口中涉及到用户隐私的字段数据仅自有平台及线下平台订单返回。具体字段详情见下面表格； |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 买家支付宝账号 | pay\_account |
| 客户网名 | buyer\_nick |
| 退款订单中收件人姓名 | receiver\_name |
| 退款订单中收件人电话 | receiver\_telno |
| 客户姓名 | customer\_name |

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
| 店铺编号 | shop\_nos | String | 255 | 否 | 由英文逗号分隔的店铺编号 |
| 原始单号 | tid | String | 40 | 否 | 原始单号 |
| 客户网名 | buyer\_nick | String | 100 | 否 | 客户网名 |
| 系统订单编号 | trade\_no | String | 40 | 否 | 系统订单编号 |
| 退换单号 | refund\_no | String | 40 | 否 | 退换单号 |
| 物流单号 | return\_logistics\_no | String | 40 | 否 | 物流单号（退换单上的退回物流单号） |
| 修改起始时间 | modified\_from | String | 40 | 否 | 修改起始时间 |
| 修改结束时间 | modified\_to | String | 40 | 否 | 修改结束时间 |
| 开始时间 | settle\_from | String | 40 | 否 | 结算时间 |
| 结束时间 | settle\_to | String | 40 | 否 | 结算时间 |
| 审核起始时间 | agree\_from | String | 40 | 否 | 审核起始时间 |
| 审核结束时间 | agree\_to | String | 40 | 否 | 审核结束时间 |
| 退换单状态 | status | Int | 4 | 否 | 10:已取消;20:待审核;30:已审核;40已推送:80:已结算;81:待回传;85:待过账;86:已过账;87:成本确认;90:已完成 |
| 入库状态 | stockin\_status | Int | 4 | 否 | 0:无需入库;1:待入库;2:部分入库;3:全部入库;4:终止入库 |
| 退回仓库编号 | return\_warehouse\_nos | String | 1000 | 否 | 退回仓库编号，用英文逗号分隔 |
| 退换单类型 | type | Int | 4 | 否 | 1:售前退款;2:退货;3:换货;4:退款不退货;6:保价退款 |
| 模糊查询 | fuzzy\_query | boolean | 1 | 否 | 默认false,业务单号进行模糊查询匹配，匹配数量大于1条时会报错 |
| 是否为拦截件 | return\_mask\_manual\_intercept | boolean | 1 | 否 | 0：否   1：是<br>不传不判断 |
| 是否拒收 | refund\_mask\_reject\_return | boolean | 1 | 否 | 0：否   1：是<br>不传不判断 |
| 排序类型 | order\_type | Int | 4 | 否 | 0：默认排序<br>1：修改时间降序 |
| 平台状态 | rr\_status | Int | 4 | 否 | 1：取消退款<br>2：申请退款<br>3：等待退货<br>4：等待收货<br>5：退款成功<br>不传默认全部 |
| 退款成功时间起始 | current\_phase\_timeout\_from | String | 40 | 否 | 退款成功时间起始 |
| 退款成功时间结束 | current\_phase\_timeout\_to | String | 40 | 否 | 退款成功时间结束 |
| 是否需要国补信息 | need\_gov\_subsidy\_info | boolean | 1 | 否 | 0：不需要<br>1：需要<br>默认0 |
| 原始退款单号 | raw\_refund\_nos | String | 255 | 否 | 原始退款单号 |

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

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据仅自有平台及线下平台订单返回，其他平台均不返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 单据数据 |
| 数据总条数 | total\_count | Int |  | 是 | 单据数据总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单id | refund\_id | Int | 11 | 是 | 退换单id |
| 原始单号 | src\_tids | String | 255 | 是 | 原始单号（关联的销售单平台订单号） |
| 退换单号 | refund\_no | String | 40 | 是 | 退换单号 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 退换单类型 | type | Int | 4 | 是 | 1:售前退款;2:退货;3:换货;4:退款不退货;6:保价退款 |
| 入库状态 | stockin\_status | Int | 4 | 是 | 0:无需入库;1:待入库;2:部分入库;3:全部入库;4:终止入库 |
| 标记名称 | flag\_name | String | 32 | 是 | 标记名称 |
| 退回货品数量 | return\_goods\_count | Decimal(19,4) |  | 是 | 退回货品数量 |
| 退款订单中收件人电话 | receiver\_telno | String | 100 | 是 | 退款订单中收件人电话（仅自有平台及线下平台返回，其他平台均不返回） |
| 退款订单中收件人姓名 | receiver\_name | String | 100 | 是 | 退款订单中收件人姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 修改时间 | modified | String | 40 | 是 | 修改时间 |
| 便签数量 | note\_count | Int | 6 | 是 | 便签数量 |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 建单方式 | from\_type | Int | 4 | 是 | 0:API抓单;1:手工建单;2:Excel导入;3:分销商推送 |
| 建单时间 | created | string | 40 | 是 | 建单时间 |
| 结算时间 | settle\_time | string | 40 | 是 | 若无结算时间，返回空字符串 |
| 审核时间 | check\_time | string |  | 是 | 未审核，返回空字符串 |
| 退货物流单号 | return\_logistics\_no | String | 40 | 是 | 退货物流单号 |
| 系统订单号列表 | trade\_no\_list | String | 255 | 是 | 系统订单号列表 |
| 平台退款金额 | guarantee\_refund\_amount | Decimal(19,4) |  | 是 | 平台退款金额（担保退款金额） |
| 退货金额 | return\_goods\_amount | Decimal(19,4) |  | 是 | 退货金额 |
| 物流公司名称 | return\_logistics\_name | String | 40 | 是 | 物流公司名称 |
| 退换说明 | reason\_name | String | 255 | 是 | 退换说明 |
| 退款原因 | refund\_reason | String | 255 | 否 | 退款原因 |
| 客户网名 | buyer\_nick | String | 100 | 是 | 客户网名（仅自有平台及线下平台返回，其他平台均不返回） |
| 建单者 | operator\_name | String | 40 | 是 | 建单者 |
| 实际退款金额 | actual\_refund\_amount | Decimal(19,4) |  | 是 | 实际退款金额 |
| 驳回原因 | revert\_reason\_name | String | 255 | 是 | 驳回原因 |
| 退回仓库编号 | return\_warehouse\_no | String | 40 | 是 | 退回仓库编号 |
| 线下退款金额 | direct\_refund\_amount | Decimal(19,4) |  | 是 | 线下退款金额（非担保退款金额） |
| 收款金额 | receive\_amount | Decimal(19,4) |  | 是 | 收款金额，买家支付给卖家 |
| 客户姓名 | customer\_name | String | 40 | 是 | 客户姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 分销商昵称 | fenxiao\_nick\_name | String | 40 | 否 | 分销商昵称，若无值则字段不返回 |
| 退换单状态 | status | Int | 4 | 是 | 10:已取消;20:待审核;30:已审核;40已推送:80:已结算;81:待回传;85:待过账;86:已过账;87:成本确认;90:已完成 |
| 店铺id | shop\_id | Int | 11 | 是 | 店铺id |
| 订单id | trade\_id | Int | 11 | 是 | 订单id |
| 原始退换单号 | raw\_refund\_nos | String | 255 | 是 | 原始退换单号 多个原始退款单号之间使用英文逗号隔开 |
| 支付订单号 | pay\_id | String | 40 | 是 | 支付订单号 |
| 分销退换单号 | provider\_refund\_no | String | 40 | 是 | 分销原始单号 |
| 店铺平台id | shop\_platform\_id | Int |  | 是 | 店铺平台id |
| 原始单号 | tid\_list | String |  | 是 | 原始单号（同退换单管理界面原始单号字段） |
| 子平台id | sub\_platform\_id | Int |  | 是 | 子平台id |
| 退回仓库id | return\_warehouse\_id | Int |  | 是 | 退回仓库id |
| 平台id | platform\_id | Int |  | 是 | 平台id |
| 奇门货主编号 | wms\_owner\_no | String | 40 | 否 | 奇门货主编号 |
| 退回仓库类型 | warehouse\_type | Int | 4 | 是 | 退回仓库类型 1:普通（内部）,2:自流转,3:平台,4:京东沧海.6:抖音云仓,125:代发仓,126:分销委外 |
| 拦截原因 | bad\_reason | Int | 11 | 是 | 拦截原因 |
| 最后修改时间 | modified\_date | String | 40 | 是 | 最后修改时间 |
| 退换信息 | return\_mask\_info | String | 255 | 是 | 退换信息 |
| 处理状态 | process\_status | Int | 4 | 是 | 处理状态<br>0：待递交<br>15：已递交<br>25：待回传<br>35：已回传 |
| 退款原因id | reason\_id | Int | 11 | 是 | 退款原因id |
| 驳回原因id | revert\_reason | Int | 11 | 是 | 驳回原因id |
| 客户id | customer\_id | Int | 11 | 是 | 客户id |
| 发货方式 | consign\_mode | Int |  | 是 | 0：并行<br>1：交替<br>2：顺延 |
| 退款创建时间 | refund\_time | String | 40 | 是 | 退款创建时间，格式: yyyy-MM-dd HH:mm:ss |
| 分销原始单号 | fenxiao\_tid | String | 40 | 是 | 分销原始单号 |
| 分销商编码 | fenxiao\_nick\_no | String | 40 | 是 | 分销商编码 |
| wms单号 | wms\_code | String |  | 是 | wms单号(奇门自定义接口不返回该字段) |
| 平台状态 | rr\_status | Int | 4 | 是 | 0：空<br>1：取消退款<br>2：申请退款<br>3：等待退货<br>4：等待收货<br>5：退款成功 |
| 退款成功时间 | current\_phase\_timeout | String | 40 | 是 | 退款成功时间 |
| 退换单详情 | detail\_list | List<Map<String, Object>> |  | 是 | 退换单详情 |
| 金额明细 | amount\_detail\_list | List<Map<String, Object>> |  | 是 | 金额明细 |
| 换出订单 | swap\_order | Map<String,Object> |  | 否 | 非换货类型的单据不返回 |
| 国补信息 | gov\_subsidy\_info | List<Map<String, Object>> |  | 否 | 国补信息 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单明细Id | rec\_id | Int | 11 | 是 | 明细唯一键 |
| 退换单id | refund\_id | Int | 11 | 是 | 退换单id |
| 原始子单号 | oid | String | 40 | 是 | 原始子单号 |
| 订单明细id | trade\_order\_id | Int | 11 | 是 | 订单明细id |
| 平台id | platform\_id | Int | 11 | 是 | 平台id， [见附件](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 系统订单编号 | trade\_no | String | 40 | 是 | 系统订单编号 |
| 数量 | num | Decimal(19,4) |  | 是 | 实际发出数量 |
| 价格 | price | Decimal(19,4) |  | 是 | 价格, 系统订单明细分摊后价格 |
| 原价 | original\_price | Decimal(19,4) |  | 是 | 原价, 系统订单明细标价 |
| 成本价 | checked\_cost\_price | Decimal(19,4) |  | 是 | 成本价 |
| 退款数量 | refund\_num | Decimal(19,4) |  | 是 | 退款数量 |
| 退款总额 | total\_amount | Decimal(19,4) |  | 是 | 退款总额, 系统订单明细的分摊后金额 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 已经退款的总金额 |
| 担保退款 | is\_guarantee | bool | 1 | 是 | 是否担保退款<br>是:true；否:false |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 规格名 | spec\_name | String | 100 | 是 | 规格名 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 平台货品id | goods\_id | String | 40 | 是 | 平台货品id |
| 平台规格id | spec\_id | String | 40 | 是 | 平台规格id |
| 系统货品id | sys\_goods\_id | Int | 11 | 是 | 系统货品id（旺店通货品档案中货品维度自增生成的id） |
| 系统规格id | sys\_spec\_id | Int | 11 | 是 | 系统规格id（旺店通货品档案中单品维度自增生成的id） |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 入库数量 | stockin\_num | Decimal(19,4) |  | 是 | 退货入库数量 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 平台规格名称 | api\_spec\_name | String | 100 | 是 | 平台规格名称 |
| 平台货品名称 | api\_goods\_name | String | 255 | 是 | 平台货品名称 |
| 最后修改时间 | modified | String | 40 | 是 | 最后修改时间 |
| 组合装编号 | suite\_no | String | 40 | 是 | 组合装编号（单据中若不包含组合装，该字段不返回） |
| 组合装名称 | suite\_name | String | 255 | 是 | 组合装名称（单据中若不包含组合装，该字段不返回） |
| 原始退款单号 | raw\_refund\_nos | String |  | 是 | 按照oid和platform\_id匹配原始退款单数据, 包含已取消的原始退款单号，<br>多个原始退款单号之间使用英文逗号隔开 |
| 原始退款单号 | raw\_refund\_no | String | 40 | 是 | 原始退款单递交时刷新该值，取值与客户端保持一致 |
| 订单id | sales\_trade\_id | Int | 11 | 是 | 订单id |
| 总折扣金额 | discount | Decimal(19,4) |  | 是 | 总折扣金额 |
| 已支付金额 | paid | Decimal(19,4) |  | 是 | 已支付金额 |
| 组合装id | suite\_id | Int |  | 是 | 组合装id |
| 组合装数量 | suite\_num | Decimal(19,4) |  | 是 | 组合装数量 |
| 创建时间 | created | String | 40 | 是 | 创建时间 |
| 最后修改时间 | modified\_date | String | 40 | 是 | 最后修改时间 |
| 赠品类型 | gift\_type | Int | 11 | 是 | 是否赠品<br>0：非赠品<br>1：自动赠送<br>2：手工赠送<br>4：周期购赠送<br>8：平台赠送<br>32：阶梯满赠<br>64：CRM追加赠送<br>128：主品 |

**gov\_subsidy\_info**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始单号 | tid | String |  | 是 | 原始单号 |
| --- | --- | --- | --- | --- | --- |
| 原始子单号 | oid | String |  | 是 | 原始子单号 |
| --- | --- | --- | --- | --- | --- |
| 公司主体名称 | corp\_entity\_name | String |  | 是 | 公司主体名称 |
| --- | --- | --- | --- | --- | --- |

**amount\_detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 金额明细记录id | rec\_id | Int | 11 | 是 | 金额明细记录id |
| 退换单id | refund\_id | Int | 11 | 是 | 退换单id |
| 退换类型 | refund\_type | Int | 11 | 是 | 1: 货款 2:邮费 99:返现 |
| 金额流向 | is\_return | Int | 4 | 是 | 0:商家->买家<br>1:买家->商家 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 退款金额 |
| 收款金额 | receive\_amount | Decimal(19,4) |  | 是 | 收款金额 |
| 是否担保支付 | is\_guarantee | bool |  | 是 | 1:担保支付<br>0:非担保支付 |
| 支付账户 | account\_id | Int | 11 | 是 | 支付账户 |
| 买家账号 | pay\_account | String | 128 | 是 | 买家账号（仅自有平台及线下平台返回，其他平台均不返回） |
| 买家开户人姓名 | account\_name | String | 100 | 是 | 买家开户人姓名 |
| 开户银行 | account\_bank | String | 40 | 是 | 开户银行 |
| 是否系统自动生成 | is\_auto | boolean |  | 是 | 是否系统自动生成 |
| 备注 | remark | String | 255 | 是 | 备注 |

**swap\_order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 换出订单原始单号 | tid | String | 40 | 是 | 换出订单原始单号 |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 店铺名称 | shop\_name | String | 50 | 是 | 店铺名称 |
| 仓库名称 | warehouse\_no | String | 40 | 是 | 仓库名称 |
| 店铺id | shop\_id | Int |  | 是 | 店铺id |
| 仓库id | warehouse\_id | Int |  | 是 | 仓库id |
| 省份id | swap\_province | Int | 11 | 是 | 省份id |
| 城市id | swap\_city | Int | 11 | 是 | 城市id |
| 地区 | swap\_area | String | 40 | 是 | 地区 |
| 地区id | swap\_district | Int | 11 | 是 | 地区id |
| 换货新订单物流公司id | swap\_logistics\_id | Int | 6 | 是 | 换货新订单物流公司id |
| 换货邮费 | post\_amount | Decimal(19,4) |  | 是 | 换货邮费 |
| 其他金额 | other\_amount | Decimal(19,4) |  | 是 | 其他金额 |
| 换出订单明细 | swap\_order\_detail\_list | List<Map<String, Object>> |  | 是 | 换出订单明细 |

**swap\_order\_detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始子单号 | oid | String | 40 | 是 | 原始子单号 |
| 货品类型 | target\_type | Byte | 6 | 是 | 货品类型（1 单品，2 组合装） |
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

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.search#autoTab0_1)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>`"modified_from"``:``"2020-01-01 00:00:00"``,`<br>`"modified_to"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->modified_from=``"2020-01-01 00:00:00"``;`<br>`$parMap``->modified_to=``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"aftersales.refund.Refund.search"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.search#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"warehouse_type"``: 1,`<br>```"provider_refund_no"``:``""``,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 1137182,`<br>```"refund_id"``: 1130899,`<br>```"platform_id"``: 127,`<br>```"oid"``:``"lj2323823489293842938343422"``,`<br>```"tid"``:``"lj8234232389293842938422344"``,`<br>```"trade_no"``:``"A18449"``,`<br>```"checked_cost_price"``: 0,`<br>```"num"``: 1,`<br>```"price"``: 1,`<br>```"original_price"``: 1,`<br>```"refund_num"``: 1,`<br>```"total_amount"``: 1,`<br>```"refund_amount"``: 0,`<br>```"is_guarantee"``:``true``,`<br>```"goods_no"``:``"hcf"``,`<br>```"goods_name"``:``"hcf"``,`<br>```"spec_name"``:``"hcf"``,`<br>```"spec_no"``:``"hcf"``,`<br>```"spec_code"``:``"hcf"``,`<br>```"barcode"``:``"hcf"``,`<br>```"stockin_num"``: 0,`<br>```"remark"``:``""``,`<br>```"api_goods_name"``:``"hcf"``,`<br>```"sales_trade_id"``: 2740715,`<br>```"api_spec_name"``:``"hcf"``,`<br>```"trade_order_id"``: 5271780,`<br>```"modified"``: 1686712380000,`<br>```"goods_id"``:``"hcf"``,`<br>```"spec_id"``:``"hcf"``,`<br>```"sys_goods_id"``: 105064,`<br>```"sys_spec_id"``: 273312,`<br>```"discount"``: 0,`<br>```"paid"``: 0,`<br>```"suite_id"``: 0,`<br>```"suite_no"``:``""``,`<br>```"suite_name"``:``""``,`<br>```"suite_num"``: 0,`<br>```"created"``:``"2023-06-14 11:05:17"``,`<br>```"modified_date"``:``"2023-06-14 11:13:00"``,`<br>```"raw_refund_no"``:``"TKljcs2202180006"``,`<br>```"raw_refund_nos"``:``"TKljcs2202180006"`<br>```}],`<br>```"refund_no"``:``"TK2306140001"``,`<br>```"bad_reason"``: 0,`<br>```"return_telno"``:``""``,`<br>```"type"``: 2,`<br>```"trade_id"``: 2740715,`<br>```"modified"``: 1686712380000,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"created"``: 1686711917000,`<br>```"trade_no_list"``:``"A18449"``,`<br>```"return_logistics_no"``:``"238943957239"``,`<br>```"return_goods_amount"``: 1,`<br>```"modified_date"``:``"2023-06-14 11:13:00"``,`<br>```"shop_platform_id"``: 127,`<br>```"refund_id"``: 1130899,`<br>```"shop_id"``: 711,`<br>```"src_tids"``:``"lj8234232389293842938422344"``,`<br>```"actual_refund_amount"``: 0,`<br>```"refund_time"``:``"2022-06-08 00:00:00"``,`<br>```"receive_amount"``: 0,`<br>```"pay_id"``:``"1495759864643715076"``,`<br>```"status"``: 30,`<br>```"check_time"``:``"2023-06-14 11:13:00"``,`<br>```"return_mask_info"``:``""``,`<br>```"tmp_data"``: 624,`<br>```"tid_list"``:``"lj8234232389293842938422344"``,`<br>```"remark"``:``""``,`<br>```"sub_platform_id"``: 0,`<br>```"stockin_status"``: 1,`<br>```"flag_name"``:``"无"``,`<br>```"return_goods_count"``: 1,`<br>```"receiver_telno"``:``"18621578833"``,`<br>```"receiver_name"``:``"Tony"``,`<br>```"refund_reason"``:``"1"``,`<br>```"return_warehouse_id"``: 624,`<br>```"note_count"``: 0,`<br>```"from_type"``: 0,`<br>```"raw_refund_nos"``:``"TKljcs2202180006"``,`<br>```"amount_detail_list"``: [],`<br>```"consign_mode"``: 0,`<br>```"guarantee_refund_amount"``: 0,`<br>```"return_logistics_name"``:``"中通"``,`<br>```"settle_time"``:``""``,`<br>```"reason_id"``: 0,`<br>```"buyer_nick"``:``"lj"``,`<br>```"operator_name"``:``"系统"``,`<br>```"revert_reason"``: 0,`<br>```"return_warehouse_no"``:``"wdtapi3-test"``,`<br>```"direct_refund_amount"``: 0,`<br>```"platform_id"``:``"127"``,`<br>```"sync_return"``:``true``,`<br>```"customer_name"``:``"lj"``,`<br>```"reason_name"``:``"无"``,`<br>```"customer_id"``: 17588392,`<br>```"return_mask"``: 0,`<br>```"revert_reason_name"``:``"无"`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.Refund.search#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |

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