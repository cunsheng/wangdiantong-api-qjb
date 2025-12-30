---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Edit.createOrder"
title: "API文档"
---
**wms.stocktransfer.Edit.createOrder** **（调拨单新建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送调拨单给ERP |
| **1.2 适用版本：** 客户端 V1.5.6.2及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

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
| 调拨单单据信息 | orderInfo | Map<String, Object> |  | Y | 调拨单单据信息 |
| 调拨单明细信息 | detailList | List<Map<String, Object>> |  | Y | 调拨单明细信息 |
| 是否审核 | isCheck | boolean |  | Y | 是否审核<br>审核：true<br>不审核：false |

**orderInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 外部单号 | outer\_no | String | 20 | Y | 调拨单号 |
| 调出仓库 | from\_warehouse\_no | String | 40 | Y | 调出仓库 |
| 调入仓库 | to\_warehouse\_no | String | 40 | Y | 调入仓库 |
| 调拨类型 | mode | Int | 40 | Y | 调拨类型：<br>0：单品调拨<br>1：货位调拨<br>2：明细调拨<br>5：单品调拨(出+入)<br>6：货位调拨(出+入)<br>7：明细调拨(出+入)<br>分步调拨使用类型：0,1,2；快速调拨使用类型：5,6,7 |
| 备注 | remark | String | 255 | N | 备注 |
| 目标仓联系人 | contact | String | 40 | N | 目标仓联系人 |
| 联系电话 | telno | String | 40 | N | 联系电话 |
| 目标仓省份 | province | String | 40 | N | 目标仓省份，不校验是否与系统地址库匹配 |
| 目标仓城市 | city | String | 40 | N | 目标仓城市，不校验是否与系统地址库匹配 |
| 目标仓地区 | district | String | 40 | N | 目标仓地区，不校验是否与系统地址库匹配 |
| 目标仓地址 | address | String | 255 | N | 目标仓地址，不校验是否与系统地址库匹配 |

****detailList****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 调拨数量 | num | Decimal(19,4) |  | Y | 调拨数量，若调拨数量小于可用库存数量会提示报错 |
| 调出货位 | from\_position\_no | String | 50 | N | 调出货位 |
| 调入货位 | to\_position\_no | String | 50 | N | 调入货位 |
| 批次号 | batch\_no | String |  | N | 批次号，mode=2或者7，才有效 |
| 有效期 | expire\_date | String |  | N | 有效期，mode=2或者7，才有效 |
| 是否残次品 | defect | bool | 1 | N | 是否残次品<br>残次品：true<br>正品：false |
| 备注 | remark | String |  | N | 备注 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 结果信息 | data | Map<String, String> |  | Y | 结果信息 |

****data****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回信息 | message | String |  | Y | 如果创建/修改成功message内容为调拨单号,否则为错误信息 |
| 调拨单号 | transfer\_no | String |  | N | 单据创建成功，审核失败的情况下会返回调拨单号 |
| 状态码 | status | Int |  | Y | 0：操作全部成功<br>20：审核失败 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Edit.createOrder#autoTab3_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Edit.createOrder#autoTab3_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Edit.createOrder#autoTab3_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Edit.createOrder#autoTab3_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"from_warehouse_no"``:``"lz"``,`<br>`"to_warehouse_no"``:``"jziyy"``,`<br>`"mode"``: 3,`<br>`"outer_no"``:``"test1111"`<br>`},`<br>`[{`<br>`"num"``: 1,`<br>`"spec_no"``:``"lz11"``,`<br>`"remark"``:``"test1"`<br>`}, {`<br>`"num"``: 1,`<br>`"spec_no"``:``"lz12"``,`<br>`"remark"``:``"test2"`<br>`}],``true`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$stockTransfer``=``new``stdClass();`<br>`$stockTransfer``->from_warehouse_no=``'lz'``;`<br>`$stockTransfer``->to_warehouse_no=``'jziyy'``;`<br>`$stockTransfer``->mode=3;`<br>`$stockTransfer``->outer_no=``'test1111'``;`<br>``<br>`$transferList``=``array``();`<br>`$transferDetail1``=``new``stdClass();`<br>`$transferDetail1``->num=1;`<br>`$transferDetail1``->spec_no=``'lz11'``;`<br>`$transferDetail1``->remark=``'test1'``;`<br>``<br>`$transferDetail2``=``new``stdClass();`<br>`$transferDetail2``->num=1;`<br>`$transferDetail2``->spec_no=``'lz12'``;`<br>`$transferDetail2``->remark=``'test2'``;`<br>`array_push``(``$transferList``,``$transferDetail1``);`<br>`array_push``(``$transferList``,``$transferDetail2``);`<br>``<br>`$data``=``$client``->call("wms.stocktransfer.Edit.`<br>`createOrder",``$stockTransfer``,``$transferList``,true);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Edit.createOrder#autoTab3_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"message"``:``"TF202204180004"``,`<br>`"status"``: 0`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Edit.createOrder#autoTab4_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"单品不存在检查商家编码"`<br>`}` |
