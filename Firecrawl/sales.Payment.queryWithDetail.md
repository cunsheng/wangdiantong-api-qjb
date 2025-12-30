---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.Payment.queryWithDetail"
title: "API文档"
---
### **sales.Payment.queryWithDetail（销售收付单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内销售收付款单信息 |
| **1.2 适用版本：** 客户端V1.4.3.7及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** 最大跨度不能超过30天 |
| **1.5注意事项：** 为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")[，拼多多请自行对接平台获取](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")。<br>本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。具体字段详情见下面表格； |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 客户网名 | buyer\_nick |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** |

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
| 业务请求参数 | params | Map<String, Object> |  | 是 | 业务请求参数 |
| 分页 | pager | pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 是 | 开始时间，yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | 是 | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int | 4 | 否 | 0：创建时间<br>1：收付时间<br>默认0 |
| 状态 | status | Int | 4 | 否 | 10：已取消<br>20：待审核<br>30：待结算<br>40：已完成 |
| 方向 | is\_refund | Int | 4 | 否 | 0：收款<br>1：退款 |
| 收付单号 | payment\_no | String | 40 | 否 | 收付单号 |
| 业务单号 | sales\_order\_no | String | 40 | 否 | 业务单号 |
| 店铺编号 | shop\_nos | String | 20 | 否 | 店铺编号，多个使用英文逗号分隔 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应正文数据 | data | Map<String, Object> |  | Y | 响应正文数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | Y | 查询单据总条数 |
| 单据信息 | payment\_list | List<Map<String, Object>> |  | Y | 单据信息 |

**payment\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键id | payment\_id | Int | 11 | 是 | 主键id |
| 收付单号 | payment\_no | String | 40 | 是 | 收付单号 |
| 状态 | status | Int | 4 | 是 | 10: 编辑中 <br>20: 待审核 <br>30: 待结算 <br>40: 已完成 |
| 店铺编号 | shop\_no | String | 40 | 是 | 店铺编号 |
| 业务单号 | sales\_order\_no | String | 40 | 是 | 业务单号 |
| 原始单号 | raw\_nos | String | 40 | 是 | 原始单号 |
| 业务类型 | order\_type | Int | 4 | 是 | 1：订单<br>2：原始单<br>3：退换单<br>4：线下退款 |
| 款项类型 | refund\_type | String | 40 | 是 | 款项类型 |
| 收款账户 | account\_name | String | 40 | 是 | 收款账户 |
| 网名 | buyer\_nick | String | 40 | 是 | 网名（**仅自有平台及线下平台返回，其他平台均不返回**） |
| 付款账户 | pay\_account | String | 40 | 是 | 付款账户 |
| 买家开户银行 | account\_bank | String | 40 | 是 | 买家开户银行 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 退款金额 |
| 收款金额 | receive\_amount | Decimal(19,4) |  | 是 | 收款金额 |
| 实际收退款金额 | real\_amount | Decimal(19,4) |  | 是 | 实际收退款金额 |
| 核销金额 | verify\_amount | Decimal(19,4) |  | 是 | 核销金额 |
| 建单人 | operator\_name | String | 40 | 是 | 建单人 |
| 建单时间 | created | String | 40 | 是 | 建单时间 |
| 收付人 | checker\_name | String | 40 | 是 | 收付人 |
| 收付时间 | pay\_time | String | 40 | 是 | 收付时间 |
| 异常退款标记 | error\_type | Int | 4 | 是 | 退款异常标记<br>1：取消<br>2：已退款<br>3：待撤销 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 建单人id | operator\_id | Int | 11 | 是 | 建单人id |
| 收付人id | checker\_id | Int | 11 | 是 | 收付人id |
| 业务单id | sales\_order\_id | Int | 11 | 是 | 业务单id（若是销售订单对应的是订单主键，若是退款单对应的是退换单主键） |
| 方向 | is\_refund | boolean | 1 | 是 | true：退款<br>false：收款 |
| 店铺id | shop\_id | Int | 11 | 是 | 店铺id |
| 收款账户id | account\_id | Int | 11 | 是 | 收款账户id |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"start_time"``:``"2022-12-01 00:00:00"``,`<br>```"end_time"``:``"2022-12-28 17:59:59"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>``<br>`$parMap``->start_time =``'2022-12-01 00:00:00'``;`<br>`$parMap``->end_time =``'2022-12-28 17:59:59'``;`<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>``<br>`try``{`<br>```$data``=``$client``->pageCall(``"sales.Payment.queryWithDetail"``,``$pager``,``$parMap``);`<br>`}``catch``(WdtErpException``$e``)`<br>`{`<br>```echo``$e``->getMessage();`<br>`}`<br>`?>` | |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 25,`<br>```"payment_list"``: [`<br>```{`<br>```"operator_id"``: 149,`<br>```"remark"``:``"手工建单,立即收款199.0000元"``,`<br>```"pay_account"``:``""``,`<br>```"account_bank"``:``""``,`<br>```"checker_id"``: 149,`<br>```"sales_order_no"``:``"AT202212120003-9"``,`<br>```"verify_amount"``: 199.0000,`<br>```"payment_id"``: 14412,`<br>```"sales_order_id"``: 0,`<br>```"error_type"``: 0,`<br>```"account_name"``:``"现金-A"``,`<br>```"refund_amount"``: 0.0000,`<br>```"order_type"``: 2,`<br>```"is_refund"``:``false``,`<br>```"shop_no"``:``"00212"``,`<br>```"checker_name"``:``"gwc"``,`<br>```"refund_type"``: 0,`<br>```"created"``:``"2022-12-28 16:40:58"``,`<br>```"version_id"``: 0,`<br>```"pay_time"``:``"2022-12-28 16:40:58"``,`<br>```"shop_id"``: 57,`<br>```"real_amount"``: 199.0000,`<br>```"buyer_nick"``:``"xi9"``,`<br>```"operator_name"``:``"gwc"``,`<br>```"account_id"``: 1,`<br>```"payment_no"``:``"SF2022122800014"``,`<br>```"receive_amount"``: 199.0000,`<br>```"raw_nos"``:``""``,`<br>```"status"``: 40`<br>```}`<br>```]`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` | |
