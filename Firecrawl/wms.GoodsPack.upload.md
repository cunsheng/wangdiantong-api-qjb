---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.GoodsPack.upload"
title: "API文档"
---
**wms.GoodsPack.upload（箱码创建** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 创建箱码信息 |
| **1.2 适用版本：** 客户端 V1.5.2.5及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5 注意事项：** |

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
| 业务请求参数 | params | Map<String, Object> |  | Y | 业务请求参数 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String |  | Y | 仓库编号 |
| 商家编码 | src\_spec\_no | String |  | Y | 商家编码 |
| 数量 | num | BigDecimal(19,4) |  | Y | 数量 |
| 状态 | status | byte |  | Y | 状态<br>0：未入库<br>2：已入库 |
| 箱码 | pack\_barcode | String |  | N | 箱码（不传值则自动生成） |
| 批次号 | batch\_no | String |  | N | 批次号 |
| 有效期 | expire\_date | String |  | N | 有效期 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应信息 | data | Map<String, Object> |  | Y | 响应信息 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"num"``: 1,`<br>```"src_spec_no"``:``"lzx0612-3"``,`<br>```"status"``: 0,`<br>```"warehouse_no"``:``"1001"`<br>```}`<br>`]` | |
| php 请求示例 | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$param``=``new``stdClass();`<br>`$param``->warehouse_no =``'1001'``;`<br>`$param``->src_spec_no =``'lzx0612-3'``;`<br>`$param``->num = 1;`<br>`$param``->status = 0;`<br>`$data``=``$client``->call(``"wms.GoodsPack.upload"``,``$param``);`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"data"``:``"Z202406170016"``,`<br>```"status"``: 0`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"状态错误"``,`<br>```"status"``: 100`<br>`}` | |
