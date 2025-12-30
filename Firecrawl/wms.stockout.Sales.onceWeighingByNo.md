---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighingByNo"
title: "API文档"
---
**wms.stockout.Sales.onceWeighingByNo** **（重量回传3）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：将重量回传写入ERP销售订单出库单 |
| **1.2 适用版本：** 客户端 V1.3.2.4及以上版本 |
| **1.3 增量获取：** 不支持 |
| **1.4注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 自动化称重机、自动化分拣系统、仓储设备控制系统等称重以后，将重量回传写入ERP销售订单出库单。 |

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
| 物流单号 | logisticsOrTradeNo | String |  | y | 物流单号或者出库单号 |
| 包装条码 | packageBarcode | String |  |  | 如果没有, 可传"" |
| 重量 | weight | BigDecimal |  | y | 包裹重量 |
| 打包员编号 | packagerNo | String |  | y | 必须为系统内已存在的员工编号 |
| 打包台名称 | operateTableName | String |  | y | 无打包台信息, 则传空字符串 |
| 是否强制称重 | force | boolean |  | y | 默认传false |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | n | 无错误信息不返回 |
| 数据节点 | data | Map<String, Object> |  | n | 有错误信息则不返回此节点 |

****data****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流公司名称 | logistics\_name | String |  | y | 物流公司名称 |
| 物流名称 | sys\_logistics\_name | String |  | y | 物流名称(系统中物流名称) |
| 物流单号 | logistics\_no | String |  | y | 物流单号 |
| 预估重量 | calc\_weight | BigDecimal(19,4) |  | y | 预估重量 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighingByNo#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighingByNo#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighingByNo#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighingByNo#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[``"ZS201912060028"``,``""``,1,``"pos"``,null,``false``]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$logisitcsNo``=``'133545677890987'``;`<br>`$barcode``=``''``;`<br>`$weigh``= 11.0;`<br>`$packagerNo``=``'admin'``;`<br>`$operateTableName``=``''``;`<br>``<br>`$data``=``$client``->call(``"wms.stockout.Sales.onceWeighingByNo"``,``$logisitcsNo``,``$barcode``,``$weigh``,``$packagerNo``,``$operateTableName``,false);`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighingByNo#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>```"logistics_name"``:``"中国邮政"``,`<br>```"sys_logistics_name"``:``"邮政测试物流"``,`<br>```"logistics_no"``:``"133545677890987"``,`<br>```"calc_weight"``: 10`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighingByNo#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"单据不存在"`<br>`}` |
