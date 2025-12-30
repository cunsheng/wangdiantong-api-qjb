---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.search"
title: "API文档"
---
### **finance.RawPayment.search****（平台账单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内平台账单信息 |
| **1.2 适用版本：** 客户端V1.5.8.0及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：**start\_time和end\_time最大跨度为30天 |
| **1.5注意事项：【权限校验】：店铺权限**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，淘系相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")[，拼多多请自行对接平台获取](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")。 |

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
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | pager |  | 是 | 分页 |

params

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String | 20 | 否 | 店铺编号 |
| 关联单号 | order\_no | String | 40 | 否 | 关联单号 |
| 时间类型 | time\_type | Int |  | 否 | 1：收付时间<br>2：下载时间<br>默认按照收付时间进行获取 |
| 类型 | type | Int | 4 | 否 | 0：其他<br>1：收款<br>2：退款 |
| 时间起始 | start\_time | String | 40 | 是 | 时间起始 |
| 时间结束 | end\_time | String | 40 | 是 | 时间结束 |

pager

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

4.响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 单据信息 | data | Map<String, Object> |  | N | 单据信息 |

data

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细信息 | detail\_list | List<Map<String, Object>> |  | Y | 明细信息 |
| 总数 | total\_count | Int | 11 | N | 查询单据总条数 |

detail\_list

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一键 | rec\_id | Int | 20 | 是 | 平台账单唯一键 |
| 平台ID | platform\_id | Int | 6 | 是 | 平台ID，对应关系请点击 [这里](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看 |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 状态 | status | Int | 4 | 是 | 状态<br>未确认：0<br>已确认：1<br>未关联：3<br>已对账：4 |
| 类型 | type | Int | 4 | 是 | 类型<br>0：其他<br>1：收款<br>2：退款 |
| 关联单号 | order\_no | String | 40 | 是 | 关联单号 |
| 支付单号 | pay\_order\_no | String | 40 | 是 | 支付单号 |
| 收入 | in\_amount | Decimal(19,4) |  | 是 | 收入 |
| 支出 | out\_amount | Decimal(19,4) |  | 是 | 支出 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 余额 | balance | Decimal(19,4) |  | 是 | 余额 |
| 是否担保 | is\_guarantee | boolean | 1 | 是 | 是否担保 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 收付时间 | create\_time | String | 40 | 是 | 收付时间（毫秒级时间戳，例如：1631861379000） |
| 下载时间 | created | String | 40 | 是 | 下载时间（毫秒级时间戳，例如：1631861379000） |
| 最后修改时间 | modified | String | 40 | 是 | 最后修改时间（毫秒级时间戳，例如：1631861379000） |
| 业务类型 | item | String | 40 | 是 | 业务类型（该值来源于平台） |
| 对方支付宝账号 | opt\_pay\_account | String | 128 | 是 | 对方支付宝账号（该值来源于平台） |
| 业务描述 | description | String | 128 | 是 | 业务描述（该值来源于平台） |
| 支付宝流水号 | fa\_order\_no | String | 40 | 是 | 支付宝流水号（奇门自定义不返回） |
| 商品名称 | goods\_name | String | 255 | 是 | 商品名称（奇门自定义不返回） |
| 平台支付单号 | platform\_pay\_order\_no | String | 40 | 是 | 平台支付单号（奇门自定义不返回） |
| 支付宝id | pay\_user\_id | String | 255 | 是 | 支付宝id |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.search#autoTab0_1)

|     |     |
| --- | --- |
|  | `[`<br>`{`<br>`"start_time"``:``"2021-01-04 15:01:40"``,`<br>`"end_time"``:``"2021-02-03 15:01:40"`<br>`}`<br>`]` |

|     |     |
| --- | --- |
|  | `< php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$params``=``new``stdClass();`<br>```$params``->start_time =``'2020-07-20 17:43:50'``;`<br>```$params``->end_time =``'2020-08-19 00:00:00'``;`<br>``<br>``<br>`$data``=``$client``->pageCall(``"finance.RawPayment.search"``,``$pager``,``$params``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"detail_list"``: [`<br>```{`<br>```"order_no"``:``"QQQQ20211126003"``,`<br>```"item"``:``""``,`<br>```"pay_order_no"``:``"QQQQQQQ222224"``,`<br>```"create_time"``: 1638435635000,`<br>```"created"``: 1638435635000,`<br>```"num"``: 0.0000,`<br>```"is_guarantee"``:``false``,`<br>```"description"``:``""``,`<br>```"remark"``:``""``,`<br>```"rec_id"``: 11898,`<br>```"type"``: 0,`<br>```"in_amount"``: 0.0000,`<br>```"balance"``: 0.0000,`<br>```"platform_id"``: 127,`<br>```"out_amount"``: 0.0000,`<br>```"modified"``: 1638553832000,`<br>```"opt_pay_account"``:``""``,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"status"``: 4`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.search#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:100,`<br>`"message"``:``"您的查询时间过宽,查询时间不能大于30天"`<br>`}` |
