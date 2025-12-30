---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.StockCost.search"
title: "API文档"
---
**finance.StockCost.search** **（存货成本查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内存货成本信息 |
| **1.2 适用版本：** 客户端V1.2.5.6及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：【权限校验】：仓库权限**<br>未开启多仓成本情况下，仓库编号返回空字符串；开启多仓成本后仓库编号返回实际仓库的编号。默认情况下未开启多仓成本。在调用此接口前需咨询客户是否开启多仓成本。 |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | Y | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | Y | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式 [点击这里](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E6%B5%8B%E8%AF%95/%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83%E5%8F%82%E6%95%B0%E4%BF%A1) |
| 盐 | salt | String |  | Y | 由旺店通分配appsecret，是由两部分构成, 冒号前面的部分是secret, 冒号后面的部分是salt. 例如一个appsecret是testsecret:testsalt, 那么secret为testsecret, salt为testsalt. |
| 接口名称 | method | String |  | Y | 调用的接口名称 |
| 版本号 | v | String |  | Y | 1.0 |
| 秒级时间戳 | timestamp | int |  | Y | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | Y | 签名 |
| 分页大小 | page\_size | int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 起始修改时间，若无仓库编号或商家编码，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束修改时间，上同开始时间 |
| 仓库编码 | warehouse\_no | String | 40 | N | 仓库编号 |
| 商家编码 | spec\_nos | String | 40 | N | 多个商家编码使用英文逗号分隔 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 成本数据 | data | Map<String, Object> |  | N | 成本数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 成本数据 | detail\_list | List<Map<String,   Object>> |  | Y | 成本数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 实际成本 | avg\_cost | Decimal(19,4) |  | Y | 实际成本 |
| 是否残次品 | defect | bool | 1 | Y | 是否残次品, false: 非残次品; true: 残次品 |
| 计划成本 | planned\_cost | Decimal(19,4) |  | Y | 计划成本 |
| 备注 | remark | String | 255 | Y | 备注 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 创建时间 | created | String | 40 | Y | 创建时间 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.StockCost.search#autoTab4_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.StockCost.search#autoTab4_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.StockCost.search#autoTab4_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.StockCost.search#autoTab4_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_time"``:``"2019-09-29 15:13:46"``,``"end_time"``:``"2019-09-30 15:13:46"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``'2019-09-29 15:13:46'``;`<br>`$parMap``->end_time =``'2019-09-30 15:13:46'``;`<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"finance.StockCost.search"``,``$pager``,``$parMap``);`<br>`$php_json``= json_encode(``$data``, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);`<br>`echo``$php_json``;`<br>`?>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.StockCost.search#autoTab4_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``:0,`<br>```"data"``:{`<br>```"total_count"``:42,`<br>```"detail_list"``:[`<br>```{`<br>```"defect"``:``false``,`<br>```"warehouse_no"``:``"MAIN"``,`<br>```"created"``:``"2019-09-29 15:13:46"``,`<br>```"avg_cost"``:1.0000,`<br>```"modified"``:``"2019-09-29 15:13:46"``,`<br>```"remark"``:``""``,`<br>```"planned_cost"``:1.0000,`<br>```"spec_no"``:``"TEST"`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.StockCost.search#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
