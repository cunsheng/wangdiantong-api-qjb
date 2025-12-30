---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Transfer.search"
title: "API文档"
---
**finance.settle.Transfer.search** **（调拨结算查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP调拨结算单信息 |
| **1.2 适用版本：** 客户端 V1.5.9.4及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：** **【权限校验】：仓库权限** |

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
| 秒级时间戳 | timestamp | int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 源仓库编号 | from\_warehouse\_no | String | 40 | N | 源仓库编号 |
| 目标仓库编号 | to\_warehouse\_no | String | 40 | N | 目标仓库编号 |
| 结算单号 | settle\_no | String | 64 | N | 结算单号 （按结算单号查询可不传时间参数） |
| 调拨单号 | transfer\_no | String | 20 | N | 调拨单号 （按调拨单号查询可不传时间参数） |
| 结算单状态 | status | String | 4 | N | 10:编辑中,20:待审核,30:已审核,40 已取消.<br>不传默认显示全部.<br>传入多个状态时使用英文逗号分隔 |
| 开始时间 | start\_time | String | 40 | Y | 开始时间，默认创建时间 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，默认创建时间 |
| 时间类型 | time\_type | Int |  | N | 时间类型<br>0：创建时间<br>1：修改时间<br>默认0 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | String |  | 否 | 0表示调用成功,在调用错误时候不返回该值。 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | 否 | 单据数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 单据数据 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品总成本 | total\_cost | Decimal(19,4) |  | Y | 货品总成本 |
| 审核员 | checker\_name | String | 40 | Y | 审核员 |
| 邮费 | post\_cost | Decimal(19,4) |  | Y | 邮费 |
| 其它金额 | other\_fee | Decimal(19,4) |  | Y | 其它金额 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 调拨单号 | transfer\_no | String | 40 | Y | 调拨单号 |
| 备注 | remark | String | 255 | Y | 备注 |
| 结算单号 | settle\_no | String | 40 | Y | 结算单号 |
| 源仓库编号 | from\_warehouse\_no | String | 40 | Y | 源仓库编号 |
| 目标仓库编号 | to\_warehouse\_no | String | 40 | Y | 目标仓库编号 |
| 状态 | status | Int | 4 | Y | 状态<br>10:编辑中,20:待审核,30:已审核,40 已取消 |
| 结算员 | settler\_name | String | 40 | Y | 结算员 |
| 调拨单id | transfer\_order\_id | Int | 11 | Y | 调拨单id |
| 总成本 | total\_amount | Decimal(19,4) |  | Y | 总成本 |
| 调拨结算明细列表 | detail\_list | List<Map<String, Object>> |  | Y | 调拨结算明细列表 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品名称 | goods\_name | String | 40 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 255 | Y | 货品编号 |
| 规格名称 | spec\_name | String | 40 | Y | 规格名称 |
| 规格码 | spec\_code | String | 100 | Y | 规格码 |
| 条码 | barcode | String | 50 | Y | 条码 |
| 是否残次品 | defect | boolean | 1 | Y | true:残次品<br>false:正品 |
| 调拨数量 | num | Decimal(19,4) |  | Y | 调拨数量 |
| 入库数量 | in\_num | Decimal(19,4) |  | Y | 入库数量 |
| 出库数量 | out\_num | Decimal(19,4) |  | Y | 出库数量 |
| 入库结算单价 | cost\_price | Decimal(19,4) |  | Y | 入库结算单价 |
| 分摊邮费 | share\_post\_fee | Decimal(19,4) |  | Y | 分摊邮费 |
| 分摊其它费用 | share\_other | Decimal(19,4) |  | Y | 分摊其它费用 |
| 备注 | remark | String | 255 | Y | 备注 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Transfer.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Transfer.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Transfer.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Transfer.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2020-05-12 11:00:00"``,``"end_time"``:``"2020-06-02 11:26:31"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>`$pars = array`<br>`(`<br>```'start_time'``=>``'2020-05-12 11:00:00'``,`<br>```'end_time'``=>``'2020-06-02 11:26:31'`<br>`);`<br>`$pager =``new``Pager(``50``,``0``,``true``);`<br>`$data = $client->pageCall(``"finance.settle.Transfer.search"``, $pager,  $pars);``//分页方法`<br>`$php_json = json_encode($data);`<br>`echo $php_json;`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Transfer.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"total_count"``: 1,`<br>`"order"``: [`<br>`{`<br>`"checker_name"``:``"系统"``,`<br>`"total_cost"``: 0.9800,`<br>`"created"``: 1617259250000,`<br>`"detail_list"``: [`<br>`{`<br>`"defect"``:``false``,`<br>`"num"``: 1.0000,`<br>`"in_num"``: 0.0000,`<br>`"out_num"``: 1.0000,`<br>`"cost_price"``: 0.9800,`<br>`"remark"``:``""``,`<br>`"goods_name"``:``"ytz"``,`<br>`"goods_no"``:``"ytz"``,`<br>`"spec_code"``:``"ytz1"``,`<br>`"spec_name"``:``"ytz1"``,`<br>`"spec_no"``:``"ytz1"``,`<br>`"barcode"``:``"ytz1"`<br>`},`<br>`{`<br>`"defect"``:``false``,`<br>`"num"``: 1.0000,`<br>`"in_num"``: 0.0000,`<br>`"out_num"``: 1.0000,`<br>`"cost_price"``: 0.0000,`<br>`"remark"``:``""``,`<br>`"goods_name"``:``"ytz"``,`<br>`"goods_no"``:``"ytz"``,`<br>`"spec_code"``:``"ytz2"``,`<br>`"spec_name"``:``"ytz2"``,`<br>`"spec_no"``:``"ytz2"``,`<br>`"barcode"``:``"ytz2"`<br>`},`<br>`{`<br>`"defect"``:``false``,`<br>`"num"``: 1.0000,`<br>`"in_num"``: 0.0000,`<br>`"out_num"``: 1.0000,`<br>`"cost_price"``: 0.0000,`<br>`"remark"``:``""``,`<br>`"goods_name"``:``"ytz"``,`<br>`"goods_no"``:``"ytz"``,`<br>`"spec_code"``:``"ytz3"``,`<br>`"spec_name"``:``"ytz3"``,`<br>`"spec_no"``:``"ytz3"``,`<br>`"barcode"``:``"ytz3"`<br>`}`<br>`],`<br>`"transfer_order_id"``: 990,`<br>`"remark"``:``""``,`<br>`"settle_no"``:``"JS202104010042"``,`<br>`"from_warehouse_no"``:``"ytz"``,`<br>`"transfer_no"``:``"TF202102230007"``,`<br>`"total_amount"``: 0.9800,`<br>`"post_cost"``: 0.0000,`<br>`"other_fee"``: 0.0000,`<br>`"status"``: 20,`<br>`"to_warehouse_no"``:``"ytz3"``,`<br>`"settler_name"``:``"小二y"`<br>`}`<br>`]`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Transfer.search#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` |
