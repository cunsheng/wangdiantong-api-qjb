---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.push"
title: "API文档"
---
### **finance.RawPayment.push****（平台账单推送）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 推送平台账单信息 |
| **1.2 适用版本：** 客户端V1.2.4.3及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：店铺权限（仅支持自有平台推送）** |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 账单信息列表 | detailList | List<Map<String, Object>> |  | 是 | 账单信息列表 |

**detailList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号,，仅支持自有平台店铺 |
| 关联单号 | order\_no | String | 40 | 是 | 关联单号（原始单号） |
| 支付单号 | pay\_order\_no | String | 40 | 否 | 支付单号 |
| 收付时间 | create\_time | String | 40 | 否 | 收付时间，不传默认当前时间 |
| 是否担保 | is\_guarantee | Int | 1 | 否 | 是否担保 |
| 商户订单号 | raw\_order\_no | String | 64 | 否 | 商户订单号 |
| 类型 | type | Int | 4 | 否 | 类型<br>0：其他<br>1：收款<br>2：退款<br>默认0 |
| 收入金额 | in\_amount | Decimal(19,4) |  | 否 | 收入金额 |
| 支出金额 | out\_amount | Decimal(19,4) |  | 否 | 支出金额 |
| 数量 | num | Decimal(19,4) |  | 否 | 数量（正数发货，负数退货） |
| 余额 | balance | Decimal(19,4) |  | 否 | 余额 |
| 对方支付账号 | opt\_pay\_account | String | 128 | 否 | 对方支付账号 |
| 备注 | remark | String | 128 | 否 | 备注 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 错误条数 | total | int |  | N | 有错误信息则返回 |
| 单据信息 | data | List<Map<String, Object>> |  | N | 单据信息 |

****data****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 关联单号 | order\_no | String |  | Y | 关联单号 |
| 错误信息 | error | String |  | N | 错误信息 |

**5** **.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.push#autoTab0_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.push#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.push#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.push#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>`[{`<br>`"shop_no"``:``"POS"``,`<br>`"order_no"``:``"AFpUNQaX4Ysss"``,`<br>`"create_time"``:``"2020-08-18 09:20:35"``,`<br>`"remark"``:``"duplicate remark update 2222"`<br>`}, {`<br>`"shop_no"``:``"POS"``,`<br>`"order_no"``:``"0Be1tqsxdb"``,`<br>`"pay_order_no"``:``"0Be1tqsxdb"``,`<br>`"type"``: 1,`<br>`"in_amount"``: 1,`<br>`"out_amount"``: 0,`<br>`"num"``: 5,`<br>`"balance"``: 98,`<br>`"opt_pay_account"``:``"xxxx"``,`<br>`"remark"``:``"duplicate remark update 2222"``,`<br>`"create_time"``:``"2020-08-18 09:20:35"`<br>`}]`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$detailList``=``array``();`<br>`$rawPayment1``=``new``stdClass();`<br>`$rawPayment1``->shop_no =``'POS'``;`<br>`$rawPayment1``->order_no =``'AFpUNQaX4Ysss'``;`<br>`$rawPayment1``->create_time =``'2020-08-18 09:20:35'``;`<br>`$rawPayment1``->remark =``'duplicate remark update 2222'``;`<br>``<br>`$rawPayment2``=``new``stdClass();`<br>`$rawPayment2``->shop_no =``'POS'``;`<br>`$rawPayment2``->order_no =``'0Be1tqsxdb'``;`<br>`$rawPayment2``->pay_order_no =``'0Be1tqsxdb'``;`<br>`$rawPayment2``->type = 1;`<br>`$rawPayment2``->in_amount = 1;`<br>`$rawPayment2``->out_amount = 0;`<br>`$rawPayment2``->num = 5;`<br>`$rawPayment2``->balance = 98;`<br>`$rawPayment2``->opt_pay_account =``'xxxx'``;`<br>`$rawPayment2``->remark =``'duplicate remark update 2222'``;`<br>`$rawPayment2``->create_time =``'2020-08-18 09:20:35'``;`<br>``<br>`array_push``(``$detailList``,``$rawPayment1``,``$rawPayment2``);`<br>``<br>`try`<br>`{`<br>```$response``=``$client``->call(``"finance.RawPayment.push"``,``$detailList``);`<br>`}`<br>`catch``(WdtErpException``$e``)`<br>`{`<br>```echo``$e``->getMessage();`<br>`}` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.push#autoTab0_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:0,``"data"``:[]}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.RawPayment.push#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:0,``"total"``:1,``"data"``:[{``"order_no"``:``"AFpUNQaX4Ysss"``,``"error"``:``"关联单号不存在"``}]}` |
