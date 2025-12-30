---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.queryWithDetail"
title: "API文档"
---
**purchase.PurchaseOrder.queryWithDetail** **（采购单及明细查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP内采购单信息 |
| **1.2 适用版本：** 客户端 V1.4.4.9及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：【权限校验】：仓库权限、供应商权限**<br>如果不填写采购单号则必须填写开始时间和结束时间；填写了采购单号的时候起止时间条件失效； |

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
| 采购单号 | purchase\_no | String | 40 | N | 采购单号 |
| 供应商编号 | provider\_no | String | 20 | N | 供应商编号 |
| 预计入库仓编号 | expect\_warehouse\_no | String | 40 | N | 预计入库仓 |
| 收货仓编号 | receive\_warehouse\_no | String | 40 | N | 收货仓 |
| 开始时间 | start\_time | String | 40 | N | 采购单修改时间 |
| 结束时间 | end\_time | String | 40 | N | 采购单修改时间 |
| 入库状态 | stockin\_status | Int | 4 | N | 入库状态,0 未入库 1部分入库 2已入库 3停止入库 4超量入库 5部分-超量入库 |
| 采购单状态 | status | String | 64 | N | 10 已取消<br>20 编辑中<br>30 待审核<br>35 待财审<br>40 已审核<br>50 部分到货<br>60 已到货<br>70 待结算<br>80 部分结算<br>90 已完成<br>多个状态间使用英文逗号隔开 |
| 模糊查询 | fuzzy\_query | boolean | 1 | N | 默认false,业务单号进行模糊查询匹配，匹配数量大于1条时会报错 |

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

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 单据数据 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购单id | purchase\_id | Int | 11 | Y | 采购单唯一键 |
| 采购单号 | purchase\_no | String | 40 | Y | 采购单号 |
| 供应商编号 | provider\_no | String | 20 | Y | 供应商编号 |
| 供应商id | provider\_id | Int | 11 | Y | 供应商唯一键 |
| 供应商名称 | provider\_name | String | 40 | Y | 供应商名称 |
| 当前状态（采购单状态） | status | Int | 4 | Y | 采购单状态：10 已取消,20 编辑中,30 待审核,35 待财审,40 已审核,50 部分到货,60 已到货,70 待结算,80 部分结算,90 已完成 |
| 入库状态 | stockin\_status | Int | 4 | Y | 0 未入库 1部分入库 2已入库 3停止入库 4超量入库 5部分-超量入库 |
| 结算状态 | settle\_status | Int | 4 | Y | 0不可结算 1待结算 2部分结算 3已结算 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称（预计入库仓库） |
| 仓库id | warehouse\_id | Int | 11 | Y | 仓库唯一键（预计入库仓库） |
| 仓库编码 | warehouse\_no | String | 40 | Y | 仓库编码（预计入库仓库） |
| 建单者 | creator\_name | String | 40 | Y | 建单者 |
| 采购员 | purchaser\_name | String | 40 | Y | 采购员 |
| 审核员 | check\_operator\_name | String | 40 | Y | 审核员 |
| 财审员 | facheck\_operator\_name | String | 40 | Y | 财审员 |
| 标记名称 | flag\_name | String | 32 | Y | 标记名称 |
| 标记id | flag\_id | Int | 11 | Y | 标记id |
| 货运方式 | logistics\_name | String | 40 | Y | 货运方式 |
| 物流方式 | logistics\_type | Int | 6 | Y | 物流方式，点击 [链接查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) 物流代码表 |
| 物流公司编号 | logistics\_no | String |  | Y | ERP内维护的采购业务类型的物流公司编号 |
| 物流公司主键 | logistics\_id | Int | 6 | Y | 物流公司主键 |
| 付款方式 | pay\_type | Int | 20 | Y | 1:现付 2:到付 3:挂账 |
| 运费付款方式 | postfee\_pay\_type | Int | 4 | Y | 1:现付 2:到付 3:包邮 |
| 税前总货款 | goods\_fee | Decimal |  | Y | 税前总货款 |
| 邮资 | post\_fee | Decimal |  | Y | 邮资 |
| 其他费用 | other\_fee | Decimal |  | Y | 其他费用 |
| 总金额 | total\_fee | Decimal |  | Y | 总金额 |
| 税后总货款 | tax\_fee | Decimal |  | Y | 税后总货款 |
| 货品种类数 | goods\_type\_count | Int |  | Y | 货品种类数 |
| 采购开单量 | goods\_count | Decimal |  | Y | 采购开单量 |
| 采购到货量 | goods\_arrive\_count | Decimal |  | Y | 采购到货量 |
| 采购入库量 | goods\_stockin\_count | Decimal |  | Y | 采购入库量 |
| 采购单备注 | remark | String | 255 | Y | 采购单备注 |
| 预计到货日期 | expect\_arrive\_time | String |  | Y | 预计到货日期 |
| 建单日期 | created | String | 40 | Y | 建单日期 |
| 审核时间 | check\_time | String | 40 | Y | 审核时间 |
| 最后修改日期 | modified | String | 40 | Y | 最后修改日期 |
| 采购单自定义属性1 | prop1 | String | 255 | Y | 采购单自定义属性1 |
| 采购单自定义属性2 | prop2 | String | 255 | Y | 采购单自定义属性2 |
| 采购单自定义属性3 | prop3 | String | 255 | Y | 采购单自定义属性3 |
| 采购单自定义属性4 | prop4 | String | 255 | Y | 采购单自定义属性4 |
| 采购单详情 | detail\_list | List<Map<String, Object>> |  | Y | 采购单详情 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购单id | purchase\_id | Int | 11 | Y | 采购单id |
| 明细id | rec\_id | Int | 11 | Y | 明细唯一键 |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 零售价格 | retail\_price | Decimal(19,4) |  | Y | 零售价格 |
| 供应商货号 | provider\_goods\_no | String | 64 | Y | 供应商货号 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品简称 | short\_name | String | 255 | Y | 货品简称 |
| 单品备注 | spec\_remark | String | 512 | Y | 单品备注 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 单品条码 | barcode | String | 50 | Y | 单品条码 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 图片地址 | img\_url | String | 255 | Y | 图片地址 |
| 采购量 | num | Decimal(19,4) |  | Y | 采购量 |
| 辅助采购量 | num2 | Decimal(19,4) |  | Y | 辅助采购量 |
| 采购确认量 | confirm\_num | Decimal(19,4) |  | Y | 采购确认量 |
| 到货未入库量 | arrive\_num | Decimal(19,4) |  | Y | 到货未入库量 |
| 结算数量 | settle\_num | Decimal(19,4) |  | Y | 结算数量 |
| 多到货量 | arrive\_more\_num | Decimal(19,4) |  | Y | 多到货量 |
| 到货入库量 | stockin\_num | Decimal(19,4) |  | Y | 到货入库量 |
| 入库总金额 | stockin\_amount | Decimal(19,4) |  | Y | 入库总金额 |
| 停止等待数量 | stopwait\_num | Decimal(19,4) |  | Y | 停止等待数量 |
| 未到货量 | lack\_num | Decimal(19,4) |  | Y | 未到货量 |
| 采购单位 | purchase\_unit\_name | String | 20 | Y | 采购单位 |
| 单位变换率 | unit\_ratio | Decimal(19,4) |  | Y | 单位变换率 |
| 基本单位 | base\_unit\_name | String | 20 | Y | 基本单位 |
| 税前单价 | price | Decimal(19,4) |  | Y | 税前单价 |
| 采购价 | purchase\_price | Decimal(19,4) |  | Y | 采购价格 |
| 辅助采购价 | aux\_price | Decimal(19,4) |  | Y | 辅助采购价 |
| 折扣 | discount | Decimal(19,4) |  | Y | 折扣 |
| 税率 | tax\_rate | Decimal(19,4) |  | Y | 税率 |
| 税后单价 | tax\_price | Decimal(19,4) |  | Y | 税后单价 |
| 税后金额 | tax\_amount | Decimal(19,4) |  | Y | 税后金额 |
| 税前折后单价 | dis\_price | Decimal(19,4) |  | Y | 税前折后单价 |
| 税前金额 | amount | Decimal(19,4) |  | Y | 税前总金额 |
| 预估重量 | weight | Decimal(19,4) |  | Y | 预估重量 |
| 辅助金额 | aux\_amount | Decimal(19,4) |  | Y | 辅助金额 |
| 采购单详情备注 | remark | String | 255 | Y | 采购单详情备注 |
| 自定义属性1 | prop1 | String | 255 | Y | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | Y | 自定义属性2 |
| 自定义属性3 | prop3 | String | 255 | Y | 自定义属性3（接口创建的采购单不返回该字段） |
| 自定义属性4 | prop4 | String | 255 | Y | 自定义属性4（接口创建的采购单不返回该字段） |
| 单品自定义属性1 | gs\_prop1 | String | 255 | Y | 单品自定义属性1 |
| 单品自定义属性2 | gs\_prop2 | String | 255 | Y | 单品自定义属性2 |
| 单品自定义属性3 | gs\_prop3 | String | 255 | Y | 单品自定义属性3 |
| 单品自定义属性4 | gs\_prop4 | String | 255 | Y | 单品自定义属性4 |
| 单品自定义属性5 | gs\_prop5 | String | 255 | Y | 单品自定义属性5 |
| 单品自定义属性6 | gs\_prop6 | String | 255 | Y | 单品自定义属性6 |
| 批次 | batch\_no | String | 40 | N | 批次号（如需使用，需要单独开通配置，开启配置的情况下返回） |
| 有效期 | expire\_date | String | 40 | N | 有效期 |
| 修改时间 | modified | String |  | N | 修改时间 |
| 创建时间 | created | String |  | N | 创建时间 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.queryWithDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.queryWithDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.queryWithDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.queryWithDetail#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap =``new``stdClass();`<br>`$parMap->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>``<br>`$response = $client->pageCall(``"purchase.PurchaseOrder.queryWithDetail"``, $pager, $parMap);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.queryWithDetail#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"flag_id"``: 0,`<br>```"logistics_name"``:``"未知"``,`<br>```"purchase_no"``:``"RH23011215"``,`<br>```"goods_stockin_count"``: 0,`<br>```"post_fee"``: 0,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 23887,`<br>```"purchase_id"``: 8490,`<br>```"spec_id"``: 1,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"retail_price"``: 5,`<br>```"provider_goods_no"``:``""``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"short_name"``:``""``,`<br>```"spec_remark"``:``"dsfdk;ds123"``,`<br>```"spec_code"``:``"LL "``,`<br>```"spec_name"``:``"暂无"``,`<br>```"barcode"``:``"wangdiantong"``,`<br>```"img_url"``:``"cos:\/\/IMG135.jpg"``,`<br>```"num"``: 1,`<br>```"num2"``: 0.3333,`<br>```"arrive_num"``: 0,`<br>```"settle_num"``: 0,`<br>```"arrive_more_num"``: 0,`<br>```"stockin_num"``: 0,`<br>```"stockin_amount"``: 0,`<br>```"stopwait_num"``: 0,`<br>```"expire_date"``:``""``,`<br>```"lack_num"``: 1,`<br>```"unit_ratio"``: 3,`<br>```"price"``: 0,`<br>```"purchase_price"``:``"0.0000"``,`<br>```"aux_price"``: 0,`<br>```"discount"``: 1,`<br>```"tax_rate"``: 0,`<br>```"tax_price"``: 0,`<br>```"tax_amount"``: 0,`<br>```"dis_price"``: 0,`<br>```"amount"``: 0,`<br>```"weight"``: 0.2,`<br>```"confirm_num"``: 0,`<br>```"created"``:``"2023-01-12 16:27:55"``,`<br>```"aux_amount"``: 0,`<br>```"modified"``:``"2023-01-12 16:27:55"``,`<br>```"remark"``:``""``,`<br>```"prop1"``:``"采购货品自定义属性1"``,`<br>```"prop2"``:``"采购货品自定义属性2"``,`<br>```"prop3"``:``"采购货品自定义属性3"``,`<br>```"prop4"``:``"采购货品自定义属性4"``,`<br>```"gs_prop1"``:``"自定义属性1"``,`<br>```"gs_prop2"``:``"自定义属性2"``,`<br>```"gs_prop3"``:``"自定义属性3"``,`<br>```"gs_prop4"``:``"自定义属性4"``,`<br>```"gs_prop5"``:``"自定义属性5"``,`<br>```"gs_prop6"``:``"自定义属性6"``,`<br>```"base_unit_name"``:``"箱"``,`<br>```"purchase_unit_name"``:``"哒哒哒哒哒"``,`<br>```"brand_name"``:``"发发拉"`<br>```}],`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"goods_count"``: 1,`<br>```"stockin_status"``: 0,`<br>```"flag_name"``:``"无"``,`<br>```"logistics_id"``: 15,`<br>```"tax_fee"``: 0,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"total_fee"``: 0,`<br>```"purchaser_name"``:``"aaa"``,`<br>```"modified"``: 1673511761000,`<br>```"pay_type"``: 2,`<br>```"provider_name"``:``"刘子渲供应商"``,`<br>```"logistics_type"``: 0,`<br>```"other_fee"``: 0,`<br>```"provider_no"``:``"lzx"``,`<br>```"check_operator_name"``:``"系统"``,`<br>```"facheck_operator_name"``:``"系统"``,`<br>```"logistics_no"``:``"1023"``,`<br>```"created"``: 1673511761000,`<br>```"purchase_id"``: 8490,`<br>```"settle_status"``: 0,`<br>```"postfee_pay_type"``: 0,`<br>```"goods_arrive_count"``: 0,`<br>```"prop2"``:``""``,`<br>```"prop1"``:``""``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"expect_arrive_time"``:``"2023-01-17 16:27:55"``,`<br>```"provider_id"``: 14,`<br>```"goods_fee"``: 0,`<br>```"creator_name"``:``"aaa"``,`<br>```"status"``: 20,`<br>```"warehouse_id"``: 624,`<br>```"check_time"``:``""`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.queryWithDetail#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
