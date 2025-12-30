---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.stockDetailSearch"
title: "API文档"
---
**wms.StockSpec.stockDetailSearch** **（库存明细查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取库存管理页面下明细库存tab |
| **1.2 适用版本：** 客户端 V1.5.4.3及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5 注意事项：** 需要配合 [库存查询](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search2 "库存查询") 接口，库存查询接口返回的rec\_id作为该接口的入参 |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |

params

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键id | stock\_spec\_id | Int | 20 | Y | 库存管理主键id  取值来源：配合 [库存查询](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search2 "库存查询") 接口使用，库存查询接口返回的rec\_id作为该接口的入参 |
| 主键id（批量） | stock\_spec\_id\_list | String |  | Y | 库存管理主键id,多个用逗号隔开 例："1,2,3,4,5"  取值来源：配合 [库存查询](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search2 "库存查询") 接口使用，库存查询接口返回的rec\_id作为该接口的入参 |

4.响应参数

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

**detail****\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 货位 | position\_no | String | 20 | Y | 货位 |
| 货区 | zone\_no | String | 20 | Y | 货区 |
| 库存量 | stock\_num | Decimal(19,4) |  | Y | 库存量 |
| 占用库存量 | reserve\_num | Decimal(19,4) |  | Y | 占用库存量 |
| 批次编号 | batch\_no | String | 40 | Y | 批次编号 |
| 有效期 | expire\_date | String | 20 | Y | 有效期 |
| 生产日期 | production\_date | String | 20 | Y | 生产日期 |
| 库存管理主键id | stock\_spec\_id | Integer | 20 | Y | 库存管理主键id |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"stock_spec_id"``: 13047,`<br>```"stock_spec_id_list"``:``"13047,1,2,3"``//如果两个id都传了，   以这个为主`<br>```}`<br>`]` | |
| php 请求示例 | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->stock_spec_id = 1;`<br>``<br>`$data``=``$client``->Call(``"wms.StockSpec.stockDetailSearch"``,``$params``);`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 6,`<br>```"detail_list"``: [{`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"position_no"``:``"其它未上架"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"production_date"``:``""``,`<br>```"zone_no"``:``""``,`<br>```"stock_num"``:``"52.0000"``,`<br>```"reserve_num"``:``"0.0000"`<br>```}]`<br>```}`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"库存id格式错误"`<br>`}` | |
