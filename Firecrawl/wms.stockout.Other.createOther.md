---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Other.createOther"
title: "API文档"
---
**wms.stockout.Other.createOther** **（其他出库单新建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**ERP需要减少库存且出库单据没有对应的业务类型，推送其他出库单给ERP |
| **1.2 适用版本：** 客户端 V1.5.6.4及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5 注意事项：不支持批量创建，一次只能推一单** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**线下ERP、SAP等系统对接 |

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
| 出库单单据信息 | stockout\_order | Map<String, Object> |  | Y | 出库单单据信息 |

**stockout\_order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 外部单号 | outer\_no | String | 40 | Y | 外部单号（创建成功后作为系统出库单号） |
| 业务单号 | src\_order\_no | String | 40 | N | 当不传入业务单号的情况下，自动创建业务单并关联 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 物流编号 | logistics\_code | String | 60 | N | 物流编号（系统物流编号） |
| 物流单号 | logistics\_no | String | 40 | N | 物流单号 |
| 邮费 | post\_fee | Decimal(19,4) |  | N | 邮费 |
| 创建后的单据状态 | is\_check | Int |  | N | 0：待审核<br>1：已审核<br>2：未确认<br>默认0 |
| 出库原因 | reason | String | 255 | N | 出库原因（在ERP内要维护才能推送成功） |
| 备注 | remark | String | 255 | N | 备注 |
| 货品详情 | goods\_list | List<Map<String, Object>> |  | Y | 货品详情 |

****goods\_list****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单品信息 | spec\_no | String | 40 | Y | 单品信息 |
| 出库数量 | num | Decimal(19,4) |  | Y | 出库数量 |
| 货位编号 | position\_no | String | 20 | N | 货位编号 |
| 备注 | remark | String | 255 | N | 备注 |
| 批次号 | batch\_no | String | 40 | N | 批次号 |
| 生产日期 | production\_date | String | 40 | N | 生产日期 |
| 有效期 | expire\_date | String | 40 | N | 有效期 |
| 是否残次品 | defect | bool |  | N | 是：true<br>否：false |
| 是否开启序列号 | is\_enable\_sn | Int |  | N | 0：不开启<br>1：开启<br>默认不开启 |
| 序列号列表 | sn\_list | String |  | N | 序列号列表，多个序列号用","分隔，<br>例如："xxx1,xxx2,xxx3"，开启序列号后序列号数量要与出库数量保持一致 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0表示成功推送 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | Y | 结果信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回信息 | message | String |  | Y | 如果创建/修改成功message内容为出库单号,否则为错误信息 |
| 状态码 | status | Int |  | Y | 0：表示操作全部成功<br>20：审核失败 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Other.createOther#autoTab2_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Other.createOther#autoTab2_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Other.createOther#autoTab2_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Other.createOther#autoTab2_3)

|     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"outer_no"``:``"QTC123K-041610221"``,`<br>```"warehouse_no"``:``"lz"``,`<br>```"remark"``:``"aa"``,`<br>```"prop1"``:``"aa"``,`<br>```"is_check"``:``true``,`<br>```"goods_list"``: [`<br>```{`<br>```"spec_no"``:``"lz11"``,`<br>```"num"``: 1,`<br>```"defect"``:``false``,`<br>```"remark"``:``"test"``,`<br>```"batch_no"``:``"124545-02-21"``,`<br>```"production_date"``:``"2019-09-04 18:57:13"``,`<br>```"expire_date"``:``"2019-09-04 18:57:13"``,`<br>```"is_enable_sn"``:1，`<br>```"sn_list"``:``"SN20250102001,SN20250102002"`<br>```}`<br>```]`<br>```}`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$order``=``new``stdClass();`<br>`$order``->outer_no=``"CG201911280004"``;`<br>`$order``->warehouse_no=``"1001"``;`<br>``<br>`$orderDetail``=``new``stdClass();`<br>`$orderDetail``->spec_no=``"PC_2016"``;`<br>`$orderDetail``->num=``"1.5"``;`<br>`$order``->goods_list = [``$orderDetail``];`<br>``<br>`$response``=``$client``->call(``"wms.stockout.Other.createOther"``,``$order``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示例**

6.1正常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Other.createOther#autoTab2_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"message"``:``"lj3284923423322"``,`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Other.createOther#autoTab3_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"外部单号重复!"`<br>`}` |
