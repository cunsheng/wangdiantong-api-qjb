---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockdefect.DefectChange.search"
title: "API文档"
---
wms.stockdefect.DefectChange.search（正残转换单查询）

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP正残转换单信息 |
| **1.2 适用版本：** 客户端 V1.5.9.8及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5注意事项：** |

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
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 否 | 起始时间，最后修改时间 |
| 结束时间 | end\_time | String | 40 | 否 | 最后修改时间 |
| 转换单号 | change\_no | String | 20 | 否 | 转换单号 |
| 转换状态 | status | Byte | 4 | 否 | 10:已取消 20:编辑中 30: 待审核 40:已审核 45:待结算 50: 已完成 |
| 转换类型 | type | Boolean | 1 | 否 | true:残转正；false: 正转残 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 查询出的详细信息 | data | <Map<String, Object>> |  | 是 | 详细信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结果总数 | total\_count | Int | 11 | 是 | 结果总数 |
| 结果详情 | order | List<Map<String, Object>> |  | 是 | 结果详情 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 正残转换单唯一id | rec\_id | Int | 11 | 是 | 正残转换单唯一id |
| 转换单号 | change\_no | String | 20 | 是 | 转换单号 |
| 转换状态 | status | Byte | 4 | 是 | 10:已取消 20:编辑中 30: 待审核 40:已审核 45:待结算 50: 已完成 |
| 仓库id | warehouse\_id | Int | 6 | 是 | 仓库id |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 转换类型 | type | Boolean | 1 | 是 | true：残转正<br>false:：正转残 |
| 转换开单量 | goods\_count | BigDecimal(19,4) |  | 是 | 转换开单量 |
| 货品种类数量 | goods\_type\_count | Int | 6 | 是 | 货品种类数量 |
| 制单人 | creator\_name | String | 20 | 是 | 制单人 |
| 制单人id | creator\_id | Int | 11 | 是 | 制单人id |
| 备注 | remark | String | 255 | 是 | 备注 |
| 修改时间 | modified | String |  | 是 | 修改时间 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 明细信息 | details\_list | List<Map<String, Object>> |  | 是 | 明细信息 |

**details\_list**

| 明细唯一id | rec\_id | Int | 11 | 是 | 明细唯一id |
| 正残转换单id | change\_id | Int | 11 | 是 | 正残转换单id |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单品id | spec\_id | Int | 11 | 是 | 单品id |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 出库货位 | from\_position\_no | String | 50 | 是 | 出库货位 |
| 入库货位 | to\_position\_no | String | 50 | 是 | 入库货位 |
| 单位 | unit\_name | String | 20 | 是 | 单位 |
| 辅助单位 | aux\_unit\_name | String | 20 | 是 | 辅助单位 |
| 辅助单位id | unit\_id | Int | 6 | 是 | 辅助单位id |
| 单位id | base\_unit\_id | Int | 6 | 是 | 单位id |
| 单位换算系数 | unit\_ratio | BigDecimal(19,4) |  | 是 | 单位换算系数 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 正残品 | defect | Boolean | 1 | 是 | true:残次品<br>false:正品 |
| 转换数量 | num | Decimal(19,4) |  | 是 | 转换数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | 是 | 辅助数量 |
| 有效期 | expire\_date | String |  | 是 | 有效期 |
| 批次号 | batch\_no | String |  | 是 | 批次号 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockdefect.DefectChange.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockdefect.DefectChange.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockdefect.DefectChange.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockdefect.DefectChange.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2020-07-20 17:43:50"``,``"end_time"``:``"2020-08-19 00:00:00"``}]` |

|     |     |
| --- | --- |
|  | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$params``=``new``stdClass();`<br>```$params``->start_time =``'2020-07-20 17:43:50'``;`<br>```$params``->end_time =``'2020-08-19 00:00:00'``;`<br>``<br>``<br>`$data``=``$client``->pageCall(``"wms.stockdefect.DefectChange.search"``,``$pager``,``$params``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockdefect.DefectChange.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"total_count"``: 21,`<br>`"order"``: [`<br>`{`<br>`"details_list"``: [`<br>`{`<br>`"rec_id"``: 1,`<br>`"change_id"``: 1,`<br>`"defect"``:``true``,`<br>`"base_unit_id"``: 0,`<br>`"unit_id"``: 0,`<br>`"unit_ratio"``: 1.0000,`<br>`"remark"``:``""``,`<br>`"created"``: 1595843030000,`<br>`"modified"``: 1595843030000,`<br>`"from_position_no"``:``"B_xht_B"``,`<br>`"to_position_no"``:``"B_xht_D"``,`<br>`"spec_id"``: 12778,`<br>`"spec_no"``:``"AQ9JH0430228"``,`<br>`"unit_name"``:``"无"``,`<br>`"aux_unit_name"``:``"无"`<br>`}`<br>`],`<br>`"created"``: 1595843030000,`<br>`"goods_type_count"``: 1,`<br>`"creator_id"``: 116,`<br>`"modified"``: 1595843282000,`<br>`"remark"``:``""``,`<br>`"goods_count"``: 1.0000,`<br>`"rec_id"``: 1,`<br>`"type"``:``true``,`<br>`"change_no"``:``"ZC202007270001"``,`<br>`"warehouse_id"``: 405,`<br>`"status"``: 50`<br>`}`<br>`]`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockdefect.DefectChange.search#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` |
