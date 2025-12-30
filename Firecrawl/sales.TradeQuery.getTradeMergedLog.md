---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getTradeMergedLog"
title: "API文档"
---
****sales.TradeQuery.getTradeMergedLog**（被合并订单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：查询被合并订单信息 |
| **1.2 适用版本：** 客户端 V1.2.9.0及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：**此数据仅保留七天, 每周一凌晨1点删除七天前数据; 查询时间间隔不可以超过七天 |

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

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | y | yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | y | 结束时间，上同开始时间 |

**4.响应参数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | n | 单据数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int |  | y | 查询条件总单据数 |
| 信息列表 | log\_list | List<Map<String, Object>> |  | y | 信息列表 |
| **log\_list** |  |  |  |  |  |
| 唯一id | rec\_id | Int |  | y | 唯一id |
| 被合并订单id | trade\_id | Int |  | y | 被合并订单id |
| 被合并订单号 | trade\_no | String |  | y | 被合并订单号 |
| 被合并到的订单号 | main\_trade\_no | String |  | y | 被合并到的订单号 |
| 合并时间 | created | String |  | y | 合并时间 |

**5.请求示例**

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getTradeMergedLog#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getTradeMergedLog#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getTradeMergedLog#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getTradeMergedLog#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2021-02-21 13:46:12"``,``"end_time"``:``"2021-02-25 13:46:12"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``'2021-02-21 13:46:12'``;`<br>`$parMap``->end_time =``'2021-02-25 13:46:12'``;`<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>``<br>`$data``=``$client``->pageCall(``"sales.TradeQuery.getTradeMergedLog"``,``$pager``,``$parMap``);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getTradeMergedLog#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"total_count"``: 1,`<br>`"log_list"``: [{`<br>`"trade_id"``: 54461,`<br>`"created"``:``"2021-02-22 13:46:12"``,`<br>`"trade_no"``:``"JY202102220013"``,`<br>`"rec_id"``: 6,`<br>`"main_trade_no"``:``"JY202102220012"`<br>`}]`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getTradeMergedLog#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:100,`<br>`"message"``:``"您的查询时间过宽,查询时间不能大于7天"`<br>`}` |
