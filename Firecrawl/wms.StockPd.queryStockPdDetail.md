---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPdDetail"
title: "API文档"
---
**wms.StockPd.queryStockPdDetail（盘** **点单明细查询** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内盘点单明细信息 |
| **1.2 适用版本：** 客户端V1.4.5.3及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：仓库权限** |

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
| 业务请求参数 | params | Map<String, Object> |  | 是 | 业务请求参数 |
| 分页 | pager | pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 盘点单号 | pd\_no | String | 20 | 否 | 系统盘点单编号，默认PD开头 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 总数 | total | Int | 11 | Y | 总数 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应正文数据 | data | Map<String, Object> |  | Y | 响应正文数据 |

data

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | pd\_detail\_list | List<Map<String, Object>> |  | Y | 响应数据节点 |

pd\_detail\_list

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细id | rec\_id | Int | 11 | 是 | 明细id |
| 盘点单id | pd\_id | Int | 11 | 是 | 盘点单id |
| 单品id | spec\_id | Int | 11 | 是 | 单品id |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 规格名称 | spec\_name | String | 255 | 是 | 规格名称 |
| 条码 | barcode | String | 40 | 是 | 条码 |
| 最后修改时间 | modified | Date | 40 | 是 | 最后修改时间 |
| 创建时间 | created | Date | 40 | 是 | 创建时间 |
| 盘点前库存 | old\_num | Decimal(19,4) |  | 是 | 盘点前库存 |
| 盘点后库存 | new\_num | Decimal(19,4) |  | 是 | 盘点后库存 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 品牌id | brand\_id | Int |  | 是 | 品牌id |
| 基本单位 | unit | Int | 6 | 是 | 基本单位 |
| 辅助单位 | aux\_unit | Int | 6 | 是 | 辅助单位 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 有效期 | expire\_date | Date | 40 | 是 | 有效期 |
| 批次号 | batch\_no | String | 40 | 是 | 批次号 |
| 货位 | position\_no | String | 40 | 是 | 货位 |
| 货品简称 | short\_name | String |  | 是 | 货品简称 |
| 是否残次品 | defect | Int |  | 是 | 0：正品<br>1：残次品 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"pd_no"``:``"PD2023010306"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->pd_no =``'PD2023010306'``;`<br>``<br>`$data``=``$client``->call(``"method: wms.StockPd.queryStockPdDetail"``,``$params``);` | |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"total"``: 1,`<br>```"data"``: [{`<br>```"rec_id"``: 37597,`<br>```"pd_id"``: 9806,`<br>```"defect"``: 1,`<br>```"spec_id"``: 1,`<br>```"remark"``:``""``,`<br>```"position_no"``:``"其它未上架"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"short_name"``:``""``,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"spec_name"``:``"暂无"``,`<br>```"spec_code"``:``"LL "``,`<br>```"barcode"``:``"wangdiantong"``,`<br>```"brand_id"``: 2179,`<br>```"created"``:``"2023-04-10 14:09:55"``,`<br>```"modified"``:``"2023-04-10 14:09:55"``,`<br>```"brand_name"``:``"发发拉"``,`<br>```"unit"``: 31,`<br>```"aux_unit"``: 577,`<br>```"old_num"``: 0,`<br>```"new_num"``: 2`<br>```}]`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"invalid http status 502"`<br>`}` | |
