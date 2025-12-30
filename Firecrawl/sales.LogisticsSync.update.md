---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.update"
title: "API文档"
---
****sales.LogisticsSync.update**（物流同步状态回传）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：物流同步是否成功的状态回传给ERP |
| **1.2 适用版本：** 客户端 V1.4.3.2及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** 仅支持自有平台推送 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 自研商城、分销系统、全渠道等系统对接 |

**3.请求参数说明**

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
| 同步结果列表 | syncList | List<Map<String, Object>> |  | y | 同步信息列表 |

**syncList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流同步 | sync\_id | Int | 1 | y | 在物流同步接口获取到的物流同步id |
| 同步结果 | status | Int | 4 | y | 0: 同步成功、-100: 还需同步，2:同步失败 |
| 错误信息 | error\_msg | String |  | n | 失败的错误信息，若成功传“” |

**4.响应参数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int | 11 | y | 状态码,0表示调用成功 |
| 错误信息 | message | String | 255 | y | 无错误信息不返回 |
| 结果数据 | data | List<String> |  | y | 结果数据，如果全部成功则返回空List |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.update#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.update#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.update#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.update#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>`[{`<br>`"sync_id"``: 88950,`<br>`"error_msg"``:``""``,`<br>`"status"``:``"0"`<br>`}]`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>`$parMap``->sync_id = 88950;`<br>`$parMap``->error_msg =``''``;`<br>`$parMap``->status = 0;`<br>``<br>`$data``=``$client``->call(``"sales.LogisticsSync.update"``, [``$parMap``]);`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.update#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 0,`<br>`"data"``: []`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.update#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 0,`<br>`"data"``: [``"同步结果状态为空!"``]`<br>`}` |
