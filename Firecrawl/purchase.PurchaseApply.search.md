---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.search"
title: "API文档"
---
**purchase.PurchaseApply.search** **（采购申请单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP内采购申请单信息 |
| **1.2 适用版本：** 客户端 V1.4.1.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式 [点击这里](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E6%B5%8B%E8%AF%95/%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83%E5%8F%82%E6%95%B0%E4%BF%A1) |
| 盐 | salt | String |  | 是 | 由旺店通分配appsecret，是由两部分构成, 冒号前面的部分是secret, 冒号后面的部分是salt. 例如一个appsecret是testsecret:testsalt, 那么secret为testsecret, salt为testsalt. |
| 接口名称 | method | String |  | 是 | 调用的接口名称 |
| 版本号 | v | String |  | 是 | 1.0 |
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | Int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数， 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | N | 开始时间，格式: yyyy-MM-dd HH:mm:ss |
| 结束时间 | end\_time | String | 40 | N | 结束时间，格式: yyyy-MM-dd HH:mm:ss |
| 采购申请单号 | purchase\_apply\_no | String |  | N | 采购申请单号 V1.5.1.0版本以上支持 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | List<Map<String, Object>> |  | 是 | 返回信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | 是 | 单据数据 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购申请单号 | purchase\_apply\_no | String | 20 | Y | 采购申请单号 |
| 采购申请单状态 | status | Int | 4 | Y | 采购申请单状态<br>5：已取消<br>10：编辑中<br>20：待确认<br>23：待引用<br>25：部分引用<br>30：已引用 |
| 申请人 | apply\_name | String | 50 | Y | 申请人 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称 |
| 供应商编号 | provider\_no | String | 40 | Y | 供应商编号（为空时不返回） |
| 供应商名称 | provider\_name | String | 64 | Y | 供应商名称（为空时不返回） |
| 备注 | remark | String | 255 | Y | 备注 |
| 期望到货时间 | expected\_time | String |  | Y | 期望到货时间，格式: yyyy-MM-dd HH:mm:ss |
| 修改时间 | modified | String |  | Y | 修改时间，格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String |  | Y | 创建时间，格式: yyyy-MM-dd HH:mm:ss |
| 采购申请单明细 | detail\_list | List<Map<String, Object>> |  | Y | 采购申请单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购申请单号 | purchase\_apply\_no | String | 20 | Y | 采购申请单号 |
| 采购申请单ID | rec\_id | int |  | Y | 采购申请单ID |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 申请量 | num | Decimal(19,4) |  | Y | 申请量 |
| 引用量 | ref\_num | Decimal(19,4) |  | Y | 引用量 |
| 入库量 | stockin\_num | Decimal(19,4) |  | Y | 入库量 |
| 供应商编号 | provider\_no | String | 40 | Y | 供应商编号（为空时不返回） |
| 供应商名称 | provider\_name | String | 64 | Y | 供应商名称（为空时不返回） |
| 备注 | remark | String | 255 | Y | 备注 |
| 品牌 | brand\_name | String | 64 | Y | 品牌 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.search#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>`$parMap =``new``stdClass();`<br>`$parMap->start_time =``'2022-08-25 11:10:04'``;`<br>`$parMap->end_time =``'2022-08-30 11:10:04'``;`<br>`$pager =``new``Pager(``2``,``0``,``true``);`<br>`try``{`<br>```$data = $client->pageCall(``"purchase.PurchaseApply.search"``, $pager, $parMap);`<br>`}``catch``(WdtErpException $e)`<br>`{`<br>```echo $e->getMessage();`<br>`}`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"total_count"``: 1,`<br>```"order_list"``: [{`<br>```"purchase_apply_no"``:``"POA202212130002"``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"created"``:``"2022-12-13 16:50:02"``,`<br>```"detail_list"``: [{`<br>```"purchase_apply_no"``:``"POA202212130002"``,`<br>```"goods_name"``:``"测试产品"``,`<br>```"stockin_num"``:``"0.0000"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"num"``:``"1.0000"``,`<br>```"brand_name"``:``"无"``,`<br>```"remark"``:``""``,`<br>```"rec_id"``: 377,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"ref_num"``:``"0.0000"``,`<br>```"spec_name"``:``"测试产品"``,`<br>```"provider_name"``:``"LCTtest11"``,`<br>```"provider_no"``:``"LCJtest"`<br>```}],`<br>```"modified"``:``"2022-12-13 16:50:02"``,`<br>```"remark"``:``""``,`<br>```"provider_name"``:``"LCTtest11"``,`<br>```"expected_time"``:``""``,`<br>```"apply_name"``:``"aaaaa"``,`<br>```"status"``: 20,`<br>```"provider_no"``:``"LCJtest"`<br>```}]`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseApply.search#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"日期格式不合法"`<br>`}` |
