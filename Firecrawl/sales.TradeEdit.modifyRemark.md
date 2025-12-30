---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeEdit.modifyRemark"
title: "API文档"
---
**sales.TradeEdit.modifyRemark** **（订单客服备注修改）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：修改未审核订单客服备注，一次最多100条 |
| **1.2 适用版本：** 客户端 V1.3.5.9及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：店铺权限** |

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
| 请求参数 | data | List<Map<String, Object>> |  | y | 请求参数 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单编号 | trade\_no | String | 40 | y | 系统订单编号 |
| 客服备注 | cs\_remark | String | 1024 | y | 客服备注 |
| 是否按追加方式添加 | is\_super\_add | bool | 1 | n | 是否按追加方式添加，默认否 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | int | 1 | y | 返回0为正常 |
| 返回信息 | data | Map<String, Object> |  | y | 失败订单信息或成功信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 成功信息 | message | String |  | n | 成功信息 |
| 失败信息 | error | Map<String, Object> |  | n | 失败信息 |

**error**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 失败订单编号 | trade\_no | String | 40 | y | 失败订单编号 |
| 失败原因 | message | String |  | y | 失败原因 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeEdit.modifyRemark#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeEdit.modifyRemark#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeEdit.modifyRemark#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeEdit.modifyRemark#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"data"``:[`<br>```{`<br>```"trade_no"``:``"xxxxxxx001"``,`<br>```"cs_remark"``:``"测试a"``,`<br>```"is_super_add"``:``false`<br>```},`<br>```{`<br>```"trade_no"``:``"xxxxx002"``,`<br>```"cs_remark"``:``"测试测试111"``,`<br>```"is_super_add"``:``true`<br>```}`<br>```]`<br>```}`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$pars``=``new``StdClass();`<br>`$parsMap``=``new``StdClass();`<br>`$parsMap``->trade_no =``"ORDER202202070004"``;`<br>`$parsMap``->cs_remark=``"website update1"``;`<br>`$parsMap``->is_super_add=false;`<br>`$pars``->data = [``$parsMap``];`<br>`$data``=``$client``->call(``"sales.TradeEdit.modifyRemark"``,``$pars``);`<br>`echo``json_encode(``$data``)`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeEdit.modifyRemark#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:0,`<br>`"data"``: {`<br>`"message"``:``"成功"`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeEdit.modifyRemark#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:0,`<br>`"data"``: {`<br>`"error"``: [`<br>`{`<br>`"trade_no"``:``"xxxxxx"``,`<br>`"message"``:``"订单状态不正确"`<br>`}`<br>`]`<br>`}`<br>`}` |
