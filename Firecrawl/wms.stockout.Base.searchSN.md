---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Base.searchSN"
title: "API文档"
---
**wms.stockout.Base.searchSN（出库SN查询** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 查询已出库的SN信息 |
| **1.2 适用版本：** 客户端 V1.5.7.2及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5 注意事项：【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

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
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String |  | Y | 出库SN记录创建的时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String |  | Y | 出库SN记录创建的时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 出库单号 | stockout\_no | String |  | N | 出库单号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | Y | 分页大小 |
| 页号 | page\_no | Int | 4 | Y | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 出库单相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | detail\_list | List<Map<String, Object>> |  | Y | 数据节点 |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库sn记录id | rec\_id | Int | 11 | Y | 出库sn记录id，不是sn的id |
| 出库单id | stockout\_id | Int | 11 | Y | 出库单id |
| 出库单号 | stockout\_no | String | 40 | Y | 出库单号 |
| 出库单明细id | stockout\_detail\_id | Int | 11 | Y | 出库单明细id |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| sn | sn | String | 80 | Y | sn |
| 是否残次品 | defect | boolean |  | Y | 出库单明细记录的正残品属性 |
| 创建时间 | created | String |  | Y | 出库SN记录创建的时间，yyyy-MM-dd HH:mm:ss格式 |
| 辅助序列号 | second\_sn | String |  | N | 辅助序列号 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"end_time"``:``"2023-07-30 16:56:14"``,`<br>```"start_time"``:``"2023-06-31 15:56:14"`<br>```}`<br>`]` | |
| php 请求示例 | |     |     |
| --- | --- |
|  | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params``=``new``stdClass();`<br>``<br>`$params``->start_time =``'2023-06-31 15:56:14'``;`<br>`$params``->end_time =``'2023-07-30 16:56:14'``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.Base.searchSN"``,``$pager``,``$params``);?>` | |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"detail_list"``: [`<br>```{`<br>```"created"``:``"2023-07-03 10:03:24"``,`<br>```"defect"``:``false``,`<br>```"rec_id"``: 1587,`<br>```"sn"``:``"ytzxhl2022001"``,`<br>```"spec_id"``: 2264,`<br>```"spec_no"``:``"ytzxlh"``,`<br>```"stockout_detail_id"``: 324176,`<br>```"stockout_id"``: 83305,`<br>```"stockout_no"``:``"CK2023070301"`<br>```},`<br>```{`<br>```"created"``:``"2023-07-03 10:12:37"``,`<br>```"defect"``:``false``,`<br>```"rec_id"``: 1588,`<br>```"sn"``:``"ytzxhl2022001"``,`<br>```"spec_id"``: 2264,`<br>```"spec_no"``:``"ytzxlh"``,`<br>```"stockout_detail_id"``: 324177,`<br>```"stockout_id"``: 83306,`<br>```"stockout_no"``:``"CK2023070302"`<br>```}`<br>```],`<br>```"total_count"``: 518`<br>```},`<br>```"status"``: 0`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"end_time 不能为空"``,`<br>```"status"``: 100`<br>`}` | |
