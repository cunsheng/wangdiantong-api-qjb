---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryAvailableStock"
title: "API文档"
---
**wms** **.StockSpec.queryAvailableStock** **（可用库存查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内单品的可用库存量 |
| **1.2 适用版本：** 客户端 V1.2.9.3及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** |

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
| 秒级时间戳 | timestamp | Int |  | Y | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | Y | 签名 |
| 分页大小 | page\_size | Int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | N | 开始时间(最后更新时间) |
| 结束时间 | end\_time | String | 40 | N | 结束时间(最后更新时间) |
| 商家编码 | spec\_no | String | 40 | N | 商家编码，为空时时间段必填 |
| 货品编号 | goods\_no | String | 40 | N | 货品编号 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |

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
| 单据数据 | data | Map<String, Object> |  | N | 库存相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | stocks | List<Map<String,   Object>> |  | Y | 库存信息列表 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**stocks**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 可用库存 | num | Decimal(19,4) |  | Y | 可用库存数量 |
| 仓库编号 | warehouse\_no | String |  | Y | 仓库编号 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 品牌 | brand\_name | String | 64 | Y | 品牌名称 |
| 类型 | type | Int | 4 | Y | 0正常 1质检 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 残次品 | defect | bool | 1 | Y | true：残次品<br>false：正品 |
| 货品简称 | short\_name | String | 255 | Y | 货品简称 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 条码 | barcode | String | 50 | Y | 条码 |
| 分类 | class\_name | String | 64 | Y | 分类名称 |
| 状态 | status | Int | 4 | Y | 0 正常 1缺货 2到货 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryAvailableStock#autoTab4_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryAvailableStock#autoTab4_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryAvailableStock#autoTab4_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryAvailableStock#autoTab4_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"start_time"``:``"2020-01-01 00:00:00"``,`<br>```"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"wms.StockSpec.queryAvailableStock"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示例**

6.1正常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryAvailableStock#autoTab4_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 17,`<br>```"stocks"``: [{`<br>```"goods_name"``:``"ytz1"``,`<br>```"spec_code"``:``"ytz1"``,`<br>```"num"``: 0.0000,`<br>```"goods_no"``:``"ytz1"``,`<br>```"brand_name"``:``"新建品牌3"``,`<br>```"type"``: 0,`<br>```"spec_no"``:``"ytz1"``,`<br>```"defect"``:``false``,`<br>```"warehouse_no"``：``"wdtwms"``,`<br>```"short_name"``:``"ą"``,`<br>```"spec_name"``:``"ytz1"``,`<br>```"barcode"``:``"ytz1"``,`<br>```"class_name"``:``"无"``,`<br>```"status"``: 1`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryAvailableStock#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"参数中必须包含起止时间"`<br>`}` |
