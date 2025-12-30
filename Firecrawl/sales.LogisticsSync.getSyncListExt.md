---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.getSyncListExt"
title: "API文档"
---
**sales.LogisticsSync.getSyncListExt（待同步列表查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：查询待同步物流列表 |
| **1.2 适用版本：** 客户端 V1.5.9.60及以上版本 |
| **1.3 增量获取：** 不支持 |
| **1.4 注意事项：【权限校验】：店铺权限（仅支持自有平台）** |
| **1.5** **常见场景处理：** <br>****1.5.1**拆分发货：** 商城推送过来的是一个订单，但是因为实际情况需要（例：库存不足有货先发），在ERP系统拆分开了，分开发货。<br>①：商城订单只有一条货品明细，且货品数量>=2被拆分成多个系统订单的<br>-   一个tid对应一个oid，num>=2,拆分后的多个系统订单tid和oid相同，此情景下拆分后的多个系统单，只有一个系统订单可成功同步物流单号，其余系统单不同步。<br>  <br>②：商城订单有多条货品明细，被拆分成多个系统订单的<br>- 一个tid对应多个oid，拆分后的多个系统订单tid相同、oid不同，此情景下拆分后的多个系统单，每个系统订单可以同步一个单号<br>  <br>③注意事项：<br>- 物流同步时物流单号对应的最小维度是子订单（oid），一个子订单只能同步一个单号<br>  <br>- 需要在客户端设置--系统设置--物流设置中勾选开启拆单发货的配置，否则一个平台订单编号只能回传一个物流单号<br>  <br>- 平台（商城、官网等）必须支持拆分发货功能<br>  <br>****1.5.2**多包裹发货：** ERP系统内单个订单包含的货品数量过多或者重量过重，因实际包装需要或物流公司要求（例如：单个包裹不能超过5kg），此时单个订单需要打印多个物流单进行发货。<br>①：单个系统订单，实际多个包裹发货，每个包裹对应一个物流单号<br>- 一个trade\_no,对应多个logistics\_no，此情景下与系统订单包含子订单（oid）条数无关，只能同步一个物流单号 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、分销系统、全渠道等系统对接 |

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
| 店铺编号 | shop\_no | String | 20 | n | 店铺编号，不支持传入多个店铺编号 |
| 是否自有平台 | is\_own\_platform | bool | 1 | n | **是否自有平台（自有平台调用传true）**<br>是：true  否：false<br>不填默认为false |
| 原始单号 | tid | String | 40 | n | 原始单号 |
| 物流单号 | logistics\_no | String | 40 | n | 物流单号 |
| 是否拆单发货 | is\_part\_sync | Int | 1 | n | 1拆单发货，0非拆单发货  不传则不使用该条件 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小（最大1000） |
| 分页 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int | 11 | y | 状态码,0表示调用成功 |
| 总条数 | total | Int | 11 | n | 总条数 |
| 错误信息 | message | String | 255 | n | 无错误信息不返回 |
| 单据数据 | data | List<Map<String, Object>> |  | n | 单据数据 |

**dat** **a**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流同步id | sync\_id | Int | 11 | 是 | 物流同步id |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 物流单号 | logistics\_no | String | 40 | 是 | 物流单号 |
| 物流公司编号 | logistics\_code | String | 60 | 是 | 系统内自定义物流公司的编号，在ERP设置--基本设置--物流页面查看 |
| 物流公司名称 | logistics\_name | String | 32 | 是 | 通用物流公司名称,例如申通快递 |
| 是否拆单发货 | is\_part\_sync | int | 1 | 是 | 是：1  否：0     店铺下“拆单发货配置”需要为“子单拆分发货”或才可以正确标记拆分情况 |
| 原始子单号 | oids | String | 208 | 是 | 原始子单号,仅拆单发货和部分退款成功的单据该字段有值。 |
| 订单id | trade\_id | Int | 11 | 是 | 订单id |
| 平台id | platform\_id | Byte | 4 | 是 | 平台id |
| 创建时间 | created | String |  | 是 | 格式: yyyy-MM-dd HH:mm:ss |
| 货品数量 | goods\_count | decimal(19,4) |  | 否 | 物流单号对应的货品数量，当is\_part\_sync = 1且订单对应店铺为【数量拆单发货】时返回；其他场景不返回 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.getSyncListExt#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.getSyncListExt#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.getSyncListExt#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.getSyncListExt#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"shop_no"``:``"fx_test"``,`<br>```"is_own_platform"``:``true`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->shop_no =``'fx_test'``;`<br>`$parMap``->is_own_platform = true;`<br>``<br>`$syncList``=``array``();`<br>`array_push``(``$syncList``,``$parMap``);`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$data``=``$client``->pageCall(``"sales.LogisticsSync.getSyncListExt"``,``$pager``,``$parMap``);`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.getSyncListExt#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"total"``: 1,`<br>```"data"``: [{`<br>```"sync_id"``: 152650,`<br>```"tid"``:``"ceshi20220922001"``,`<br>```"logistics_no"``:``"2345676543223"``,`<br>```"logistics_code"``:``"YZBK"``,`<br>```"logistics_name"``:``"中国邮政"``,`<br>```"is_part_sync"``: 0,`<br>```"oids"``:``""``,`<br>```"trade_id"``: 952727,`<br>```"platform_id"``: 127,`<br>```"created"``:``"2022-09-22 15:15:00"`<br>```}]`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.LogisticsSync.getSyncListExt#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
