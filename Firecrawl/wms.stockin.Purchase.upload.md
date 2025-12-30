---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.upload"
title: "API文档"
---
**wms.stockin.Purchase.upload** **（采购入库单推送）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 推送采购单对应的入库单给ERP |
| **1.2 适用版本：** 客户端 V1.5.7.2及以上版本 |
| **1.3 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| 2.1举例说明：财务系统、SAP、线下ERP、数据分析等系统的对接 |

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
| 入库单单据信息 | stockin\_order | Map<String, Object> |  | Y | 入库单单据信息 |
| 入库单明细 | stockin\_detail\_list | List<Map<String,Object>> |  | Y | 入库单明细信息 |

**stockin\_order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购单号 | purchase\_no | String | 40 | Y | 采购单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 物流编码 | logistics\_code | String | 60 | N | 系统内自定义物流的编码 |
| 物流单号 | logistics\_no | String | 40 | N | 物流单号 |
| 备注 | remark | String | 255 | N | 备注 |
| 创建模式 | create\_mode | Int |  | N | 默认：编辑中<br>1：已提交/待审核<br>2：已审核 |

**stockin\_detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 是否残次品 | defect | boolean | 1 | N | 默认为非残次品 |
| 采购单位 | unit\_name | String | 20 | N | （辅助单位）默认为”无” |
| 批次号 | batch\_no | String | 20 | N | 批次号，如采购入库单内批次与采购单内批次不一致，单据推送无法成功，但批次依然自动建立 |
| 有效期 | expire\_date | String | 40 | N | 有效期 |
| 货位编号 | position\_no | String | 40 | N | 货位编号 |
| sn码 | sn\_strings | String |  | N | sn码，用英文逗号分隔（当传入sn信息时，create\_mode字段需要传为0） |
| 生产日期 | production\_date | String | 40 | N | 生产日期 |
| 备注 | remark | String | 255 | N | 备注 |
| 序列号信息 | sn\_infos | List<SnInfo> |  | N | 序列号和辅助序列号之间的对应关系,<br>有辅助序列号的情况下需要传该字段 |

**SnInfo：**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 序列号 | sn | String |  | N | 序列号 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 辅助序列号 | second\_sn | String |  | N | 辅助序列号 |
| :-- | :-- | :-- | :-- | :-- | :-- |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int | 11 | Y | 返回0为正常 |
| 错误信息 | message | String | 255 | N | 无错误信息不返回 |
| 入库单号 | data | String | 20 | N | 创建的入库单号,创建失败不返回 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.upload#autoTab0_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.upload#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.upload#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.upload#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"purchase_no"``:``"CG2503060002"``,`<br>```"warehouse_no"``:``"testlir"``,`<br>```"create_mode"``: 0`<br>```},`<br>```[`<br>``<br>```{`<br>``<br>```"num"``:``"3"``,`<br>```"spec_no"``:``"lirspec"`<br>``<br>```}`<br>```]`<br>``<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$order``=``new``stdClass();`<br>`$order``->purchase_no=``"CG201911280004"``;`<br>`$order``->warehouse_no=``"1001"``;`<br>`$order``->create_mode=0;`<br>``<br>`$orderDetail``=``new``stdClass();`<br>`$orderDetail``->spec_no=``"PC_2016"``;`<br>`$orderDetail``->num=``"1.5"``;`<br>``<br>``<br>`$response``=``$client``->call(``"wms.stockin.Purchase.upload"``,``$order``, [``$orderDetail``]);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.upload#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``:   0,`<br>```"data"``:``"RK2003200003"`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.upload#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``:   100,`<br>```"message"``:``"仓库编号为 1001x 的仓库不存在或无权限"`<br>`}` |
