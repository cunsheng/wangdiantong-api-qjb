---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Process.queryWithDetail"
title: "API文档"
---
**wms.stockin.Process.queryWithDetail** **（生产入库查询 ）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP生产入库信息 |
| **1.2 适用版本：** 客户端 V1.4.6.8及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** <br>传入参数如果没有入库单号或者生产单号，就必须传入时间，和时间类型作为参数 |

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
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无入库单编码或生产单编码，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int |  | N | 时间判断的类型，1为建单时间，2为审核时间，3为最后修改时间<br>默认为建单时间 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 入库单号 | stockin\_no | String |  | N | 入库单号 |
| 生产单号 | process\_no | String |  | N | 生产单号 |
| 入库单状态 | status | String |  | N | 入库单状态<br>10: 已取消<br>20: 编辑中<br>30: 待审核<br>37: 待质检<br>40: 质检待确认<br>80: 已完成<br>用逗号分隔开数字的分隔符 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小不能超过2000 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 生产入库单 | order | List<Map<String, Object>> |  | Y | 生产入库单数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**Order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int |  | Y | 入库单id |
| 物流公司 | logistics\_name | String |  | Y | 物流公司名称 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 创建时间 | created | String |  | Y | 创建时间 |
| 入库单源单据类型 | src\_order\_type | Int |  | Y | 5生产原料单<br>6生产成品单 |
| 货品种类数 | goods\_type\_count | Int |  | Y | 货品种类数 |
| 备注 | remark | String |  | Y | 备注 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 经办人 | operator\_name | String |  | Y | 经办人 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 入库的仓库名称 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 生产商名 | producer\_name | String |  | Y | 生产商名 |
| 入库单号 | stockin\_no | String |  | Y | 入库单号 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间 |
| 生产单号 | process\_no | String |  | Y | 生产单号 |
| 调整后数量 | right\_num | Decimal(19,4) |  | Y | 货品数量加纠错数量 |
| 便签条数 | note\_count | Int |  | Y | 便签条数 |
| 审核时间 | check\_time | String |  | Y | 审核时间 |
| 标记id | flag\_id | Int |  | Y | 标记id |
| 标记名称 | flag\_name | String | 32 | Y | 入库单标记 |
| 入库单状态 | status | Int |  | Y | 入库单状态<br>10: 已取消<br>20: 编辑中<br>30: 待审核<br>37: 待质检<br>40: 质检待确认<br>80: 已完成 |
| 生产入库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 生产入库单的明细信息 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细id | rec\_id | Int | 11 | Y | 明细id |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品编码 | goods\_no | String | 40 | Y | 货品编码 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品简称 | short\_name | String |  | Y | 货品简称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 主条码 | barcode | String | 50 | Y | 主条码 |
| 有效期 | expire\_date | String | 40 | N | 有效期 |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 辅助单位数量 | num2 | Decimal(19,4) |  | Y | 辅助单位数量 |
| 生产日期 | production\_date | String | 40 | N | 生产日期 |
| 货位编号 | position\_no | String | 20 | N | 货位编号 |
| 批次号 | batch\_no | String | 40 | N | 批次号 |
| 预期入库量 | expect\_num | Decimal(19,4) |  | Y | 预期入库量 |
| 备注 | remark | String | 255 | Y | 备注 |
| 预估重量 | weight | Decimal(19,4) |  | Y | 预估重量 |
| 单品总重量 | goods\_weight | Decimal(19,4) |  | Y | 单品总重量 |
| 是否残次品 | defect | bool | 1 | Y | true：残次品<br>false：正品 |
| 系数 | unit\_ratio | Decimal(19,4) |  | Y | 单位换算系数 |
| 保质期 | validity\_days | Int |  | Y | 保质期，天数 |
| 待质检数量 | need\_inspect\_num | Decimal(19,4) |  | Y | 待质检数量 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 辅助单位 | aux\_unit\_name | String | 20 | Y | 辅助单位 |
| 单位 | base\_unit\_name | String | 20 | Y | 单位 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Process.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Process.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Process.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Process.queryWithDetail#autoTab5_3)

|     |     |
| --- | --- |
|  | `[{``"stockin_no"``:``""``,``"warehouse_no"``:``"lich0313"``,``"process_no"``:``"PS2018101002"``,``"time_type"``:``"2"``,``"start_time"``:``"2020-06-15`<br>`10:05:36"``,``"end_time"``:``"2020-06-17 11:05:36"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>``<br>`$pars``=``array`<br>`(`<br>```'stockin_no'``=>``''``,`<br>```'warehouse_no'``=>``'lich0313'``,`<br>```'process_no'``=>``'PS2018101002'``,`<br>```'time_type'``=>``'2'``,`<br>```'start_time'``=>``'2020-06-15 10:05:36'``,`<br>```'end_time'``=>``'2020-06-17 11:05:36'`<br>`);`<br>`$pager``=``new``Pager(50, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockin.Process.queryWithDetail"``,``$pager``,``$pars``);``//分页方法`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>``<br>`?>` |

|     |     |
| --- | --- |
|  | `Client client = DefaultClient.get(sid, url, appkey, appsecret);`<br>`StockinAPI stockinAPI = ApiFactory.get(client, StockinAPI.``class``);`<br>`ProcessStockinRequest request =``new``ProcessStockinRequest();`<br>`request.setStatus(``"aaa"``);`<br>`request.setStockinNo(``"RK2006160023"``);`<br>`ProcessStockinResponse response = stockinAPI.searchProcess(request,``new``Pager(50, 0, true));` |

|     |     |
| --- | --- |
|  | `IClient client =``new``DefaultClient(sid, url, appkey, appsecret);`<br>`stockin.StockinAPI stockinAPI = ApiFactory<stockin.StockinAPI>.Get(client);`<br>`var``pars =``new``stockin.ProcessStockinParams`<br>`{`<br>`processNo =``"PS2020062202"`<br>`};`<br>`var``pager =``new``Pager(50, 0, true);`<br>`stockin.ProcessStockinResult result = stockinAPI.SearchProcess(pars, pager);` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Process.queryWithDetail#autoTab5_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"flag_id"``: 0,`<br>```"logistics_name"``:``"无"``,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 214183,`<br>```"goods_name"``:``"爆款"``,`<br>```"short_name"``:``"zxybk"``,`<br>```"goods_no"``:``"zxydbk"``,`<br>```"spec_code"``:``"bk01"``,`<br>```"spec_name"``:``"bk01"``,`<br>```"spec_no"``:``"bk001"``,`<br>```"barcode"``:``"bk01"``,`<br>```"expire_date"``:``""``,`<br>```"num"``: 2,`<br>```"num2"``: 2,`<br>```"spec_id"``: 391776,`<br>```"production_date"``:``""``,`<br>```"batch_no"``:``""``,`<br>```"expect_num"``: 0,`<br>```"remark"``:``"生产成品入库"``,`<br>```"weight"``: 1,`<br>```"goods_weight"``: 2,`<br>```"defect"``:``false``,`<br>```"unit_ratio"``: 1,`<br>```"validity_days"``: 0,`<br>```"need_inspect_num"``: 0,`<br>```"brand_name"``:``"康师傅"``,`<br>```"aux_unit_name"``:``"无"``,`<br>```"base_unit_name"``:``"无"`<br>```}, {`<br>```"rec_id"``: 214184,`<br>```"goods_name"``:``"爆款"``,`<br>```"short_name"``:``"zxybk"``,`<br>```"goods_no"``:``"zxydbk"``,`<br>```"spec_code"``:``"bk02"``,`<br>```"spec_name"``:``"bk02"``,`<br>```"spec_no"``:``"bk002"``,`<br>```"barcode"``:``"bk02"``,`<br>```"expire_date"``:``""``,`<br>```"num"``: 2,`<br>```"num2"``: 2,`<br>```"spec_id"``: 391777,`<br>```"production_date"``:``""``,`<br>```"batch_no"``:``""``,`<br>```"expect_num"``: 0,`<br>```"remark"``:``"生产成品入库"``,`<br>```"weight"``: 1,`<br>```"goods_weight"``: 2,`<br>```"defect"``:``false``,`<br>```"unit_ratio"``: 1,`<br>```"validity_days"``: 0,`<br>```"need_inspect_num"``: 0,`<br>```"brand_name"``:``"康师傅"``,`<br>```"aux_unit_name"``:``"无"``,`<br>```"base_unit_name"``:``"无"`<br>```}],`<br>```"goods_type_count"``: 2,`<br>```"remark"``:``"库存异动生产生成"``,`<br>```"goods_count"``: 4,`<br>```"flag_name"``:``"无"``,`<br>```"warehouse_no"``:``"wms_lt_erp30"``,`<br>```"modified"``:``"2023-06-06 15:42:11"``,`<br>```"right_num"``: 4,`<br>```"note_count"``: 0,`<br>```"stockin_id"``: 90729,`<br>```"logistics_no"``:``""``,`<br>```"created"``:``"2023-06-06 15:42:11"``,`<br>```"src_order_type"``: 6,`<br>```"operator_name"``:``"系统"``,`<br>```"warehouse_name"``:``"wmslt旺店通联调仓库"``,`<br>```"producer_name"``:``"A"``,`<br>```"stockin_no"``:``"RK2023060661"``,`<br>```"process_no"``:``"PS2023060604"``,`<br>```"status"``: 80,`<br>```"check_time"``:``"2023-06-06 15:42:11"`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Process.queryWithDetail#autoTab6_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"状态参数格式不正确，请用以逗号隔开的整数字符串为参数"``}` |
