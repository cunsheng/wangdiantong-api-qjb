---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.salesWeighing"
title: "API文档"
---
**wms.stockout.Sales.salesWeighing** **（重量回传4）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：将重量回传写入ERP销售订单出库单 |
| **1.2 适用版本：** 客户端 V1.5.7.2及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：仓库权限**<br>接口回传的长宽高在客户端-账款-单据结算-邮资结算-物流单管理界面查看 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**外部应用回传包裹重量\\包裹长宽高\\发货 |

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
| 请求参数 | params | Map<String, Object> |  | y | 回传请求参数 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据编号 | order\_no | String |  | y | 物流单号或者出库单号 |
| 重量 | weight | BigDecimal(19,4) |  | y | 重量 |
| 包装条码 | package\_barcode | String |  | n | 包装条码 |
| 打包员编号 | packager\_no | String |  | n | 打包员编号，优先级高于打包员id |
| 打包员id | packager\_id | int |  | n | 打包员id,如果传入打包员编号会覆盖id |
| 打包台名称 | operator\_table\_name | String |  | n | 打包台名称 |
| 是否强制称重 | force | boolean |  | n | 默认传false，常用于超重或与预估重量差距较大时强制称重 |
| 长 | length | BigDecimal(19,4) |  | n | 单位CM，回传至物流单管理界面展示 |
| 宽 | width | BigDecimal(19,4) |  | n | 单位CM，回传至物流单管理界面展示 |
| 高 | height | BigDecimal(19,4) |  | n | 单位CM，回传至物流单管理界面展示 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | n | 无错误信息不返回 |
| 数据节点 | data | Map<String, Object> |  | n | 有错误信息则不返回此节点 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流公司名称 | logistics\_name | String |  | y | 物流公司名称 |
| 物流名称 | sys\_logistics\_name | String |  | y | 物流名称(系统中物流名称) |
| 物流单号 | logistics\_no | String |  | y | 物流单号 |
| 预估重量 | calc\_weight | BigDecimal(19,4) |  | y | 预估重量 |
| 省 | province | String |  | y | 省编码， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 市 | city | String |  | y | 市编码， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 区 | district | String |  | y | 区编码， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.salesWeighing#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.salesWeighing#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.salesWeighing#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.salesWeighing#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"order_no"``:``"654564591"``,``"package_barcode"``:``""``,``"weight"``:1,``"packager_no"``:``"POS"``,``"force"``:``false``,``"length"``:2,``"width"``:3,``"height"``:4}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$params``=``new``stdClass();`<br>`$params``->order_no =``'654564591'``;`<br>`$params``->package_barcode =``''``;`<br>`$params``->weight = 1.0;`<br>`$params``->packager_no =``'POS'``;`<br>`$params``->force = false;`<br>`$params``->length = 2;`<br>`$params``->width = 3;`<br>`$params``->height = 4;`<br>`$data``=``$client``->call(``"wms.stockout.Sales.salesWeighing"``,``$params``);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.salesWeighing#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"logistics_name"``:``"自有物流"``,`<br>```"sys_logistics_name"``:``"自由物流"``,`<br>```"province"``: 120000,`<br>```"city"``: 120100,`<br>```"logistics_no"``:``"ZS202503310005"``,`<br>```"district"``: 120116,`<br>```"calc_weight"``: 10`<br>```}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.salesWeighing#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"单据不存在"``}` |
