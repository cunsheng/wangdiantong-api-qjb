---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.JitRefund.searchOrderWithDetail"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

库存类

移位单查询

库存查询

创建盘点单

其他入库单新建

调拨单查询

其他出库单查询

其他入库单查询

调拨入库单查询

可用库存查询

其他出库单新建

调拨出库单查询

调拨单入库取消

盘点入库单查询

盘点出库单查询

调拨单出库取消

调拨单取消

调拨入库单新建

调拨出库单新建

调拨单新建

补货单查询

库存变化查询

存货成本查询

调拨单停止等待

其它出库业务单创建

其它入库业务单创建

生产出库查询

生产入库查询

外仓调整出库单创建

外仓调整入库单创建

外仓调整出库单查询

外仓调整入库单查询

调拨结算查询

正残转换单查询

其它出库业务单查询

其它入库业务单查询

分拣单全览

默认货位查询

虚拟仓库存查询

虚拟仓单据创建

虚拟仓单据查询

装箱单查询

JIT退货入库单查询

JIT出库单查询

SN码查询

其它入库业务结算单创建

库存查询2

出库瞬时成本查询

入库瞬时成本查询

盘点单查询

盘点单明细查询

入库单查询

出库单查询

库存明细查询

出库SN查询

入库SN查询

入库SN明细推送

出库SN明细推送

其他入库单取消

其他出库单取消

电子面单号查询

箱码新建

其他入库业务单据取消

其他出库业务单据取消

虚拟仓库存分配策略创建

虚拟仓库存释放策略新建

外仓快速调拨

当前位置： API文档 > 库存类

****wms.stockin.JitRefund.searchOrderWithDetail** **（JIT退货入库单查询）****

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的JIT退货入库单单据信息 |
| **1.2 适用版本：** 客户端 V1.5.3.3及以上版本 |
| **1.3 增量获取：**按照最后修改时间获取 |
| **1.4 时间跨度：请求时间最大跨度为30天。** |
| **1.5注意事项：** **【权限校验】：仓库权限** |

**2.调用场** **景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

**3.请求参数说明**

3.1 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | http://47.92.239.46/openapi |
| 正式环境 | http://wdt.wangdian.cn/openapi |

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
| 查询参数 | params | Map<String, Object> |  | y | 查询参数 |
| 分页 | pager | pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | y | 起始时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | y | 结束时间, yyyy-MM-dd HH:mm:ss格式 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小 |
| 页号 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 返回0为正常 |
| 错误信息 | message | String |  | n | 无错误信息不返回 |
| 退货入库单信息 | data | Map<String, Object> |  | n | 退货入库信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据仅自有平台及线下平台返回，其他平台均不返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | y | JIT入库单相关数据 |
| 总数 | total\_count | Int | 11 | n | 查询条件总数单据 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int | 11 | y | 入库单id |
| 入库单号 | stockin\_no | String | 40 | y | 入库单号 |
| 退货单号 | refund\_no | String | 40 | y | 退货单号 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | y | 仓库名称 |
| 入库单状态 | status | Int | 4 | y | 入库单状态<br>10：已取消<br>20：编辑中<br>30：待审核<br>37：待质检<br>40：质检待确认<br>80：已完成 |
| 最后修改时间 | modified | String | 40 | y | 入库单最后修改时间 |
| 创建时间 | created | String | 40 | y | 入库单创建时间 |
| 审核时间 | check\_time | String | 40 | y | 审核时间 |
| 备注 | remark | String | 255 | y | 备注 |
| 平台退货单号 | jit\_refund\_no | String | 50 | y | 平台退货单号 |
| 制单人 | operator\_name | String | 40 | y | 制单人 |
| 标记名称 | flag\_name | String | 32 | y | 标记名称 |
| 便签数量 | note\_count | Int | 6 | y | 便签数量 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量 |
| 货品种类 | goods\_type\_count | Int | 6 | y | 货品种类 |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺id | shop\_id | Int | 6 | y | 店铺id |
| 含税货款总额 | tax\_amount | Decimal(19,4) |  | y | 含税货款总额 |
| 货款金额 | amount | Decimal(19,4) |  | y | 货款金额 |
| 货品总成本 | total\_cost | Decimal(19,4) |  | y | 货品总成本 |
| 仓库id | warehouse\_id | short |  | y | 仓库id |
| 入库单明细列表 | detail\_list | List<Map<String, Object>> |  | y | 入库单明细列表 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int | 11 | 是 | 入库单ID |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 预期入库数量 | expect\_num | Decimal(19,4) |  | 是 | 预期入库数量 |
| 数量 | num | Decimal(19,4) |  | 是 | 入库数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | 是 | 辅助数量 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品编码 | goods\_no | String | 40 | 是 | 货品编码 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 是否残次品 | defect | bool | 1 | 是 | 是否残次品 |
| 基本单位 | base\_unit\_name | String | 20 | 是 | 基本单位 |
| 辅助单位 | aux\_unit\_name | String | 20 | 是 | 辅助单位 |
| 品牌编号 | brand\_no | String | 32 | 是 | 品牌编号 |
| 品牌id | brand\_id | Int | 11 | 是 | 品牌id |
| 成本价 | checked\_cost\_price | Decimal(19,4) |  | 是 | 成本价 |
| 价格 | price | Decimal(19,4) |  | 是 | 价格 |
| 含税价格 | tax\_price | Decimal(19,4) |  | 是 | 含税价格 |
| 金额 | amount | Decimal(19,4) |  | 是 | 金额 |
| 含税金额 | tax\_amount | Decimal(19,4) |  | 是 | 含税金额 |
| PO单 | po\_no | String | 40 | 是 | PO单 |
| 总成本 | checked\_cost\_amount | Decimal(19,4) |  | 是 | 总成本（建议使用该字段） |
| 总成本 | total\_cost | Decimal(19,4) |  | 是 | 总成本 |
| 明细id | rec\_id | int |  | 是 | 明细id |
| 单品id | spec\_id | int |  | 是 | 单品id |
| 货品id | goods\_id | int |  | 是 | 货品id |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间 格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String |  |  | 创建时间 格式: yyyy-MM-dd HH:mm:ss |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.JitRefund.searchOrderWithDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.JitRefund.searchOrderWithDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.JitRefund.searchOrderWithDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.JitRefund.searchOrderWithDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>`"start_time"``:``"2019-09-01 00:00:00"``,`<br>`"end_time"``:``"2019-10-01 23:59:59"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$paraMap =``new``stdClass();`<br>`$paraMap->start_time =``"2019-09-01"``;`<br>`$paraMap->end_time =``"2019-10-01"``;`<br>``<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$response = $client->pageCall(``"wms.stockin.JitRefund.searchOrderWithDetail"``,$pager, $paraMap);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.JitRefund.searchOrderWithDetail#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>101<br>102 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 2,`<br>```"order_list"``: [{`<br>```"tax_amount"``:``"0"``,`<br>```"stockin_id"``: 88526,`<br>```"amount"``:``"0"``,`<br>```"total_cost"``:``"8.8888"``,`<br>```"created"``:``"2022-12-30 09:48:13"``,`<br>```"detail_list"``: [{`<br>```"stockin_id"``: 88526,`<br>```"spec_no"``:``"FFFFFFFFFFFFFFFF202011268479"``,`<br>```"remark"``:``""``,`<br>```"goods_name"``:``"半身裙A8QZ920040"``,`<br>```"goods_no"``:``"QZ920040555"``,`<br>```"spec_name"``:``"绿色 S"``,`<br>```"spec_code"``:``""``,`<br>```"defect"``:``false``,`<br>```"brand_id"``: 0,`<br>```"checked_cost_price"``: 2,`<br>```"price"``: 0,`<br>```"tax_price"``: 0,`<br>```"po_no"``:``"12345678"``,`<br>```"amount"``: 0,`<br>```"tax_amount"``: 0,`<br>```"checked_cost_amount"``: 2,`<br>```"base_unit_name"``:``"无"``,`<br>```"aux_unit_name"``:``"无"``,`<br>```"num"``:``"1.0000"``,`<br>```"expect_num"``:``"1.0000"``,`<br>```"num2"``:``"1.0000"``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"total_cost"``:``"2"`<br>```}, {`<br>```"stockin_id"``: 88526,`<br>```"spec_no"``:``"FFFFFFFFFFFFFFFF202011268477"``,`<br>```"remark"``:``""``,`<br>```"goods_name"``:``"半身裙A8QZ920040"``,`<br>```"goods_no"``:``"QZ920040556"``,`<br>```"spec_name"``:``"绿色 M"``,`<br>```"spec_code"``:``""``,`<br>```"defect"``:``false``,`<br>```"brand_id"``: 0,`<br>```"checked_cost_price"``: 2.3333,`<br>```"price"``: 0,`<br>```"tax_price"``: 0,`<br>```"po_no"``:``"12345678"``,`<br>```"amount"``: 0,`<br>```"tax_amount"``: 0,`<br>```"checked_cost_amount"``: 4.6666,`<br>```"base_unit_name"``:``"无"``,`<br>```"aux_unit_name"``:``"无"``,`<br>```"num"``:``"2.0000"``,`<br>```"expect_num"``:``"6.0000"``,`<br>```"num2"``:``"2.0000"``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"total_cost"``:``"4.6666"`<br>```}, {`<br>```"stockin_id"``: 88526,`<br>```"spec_no"``:``"FFFFFFFFFFFFFFFF202011268478"``,`<br>```"remark"``:``""``,`<br>```"goods_name"``:``"半身裙A8QZ920040"``,`<br>```"goods_no"``:``"QZ920040558"``,`<br>```"spec_name"``:``"绿色 XL"``,`<br>```"spec_code"``:``""``,`<br>```"defect"``:``false``,`<br>```"brand_id"``: 0,`<br>```"checked_cost_price"``: 1.1111,`<br>```"price"``: 0,`<br>```"tax_price"``: 0,`<br>```"po_no"``:``"12345678"``,`<br>```"amount"``: 0,`<br>```"tax_amount"``: 0,`<br>```"checked_cost_amount"``: 2.2222,`<br>```"base_unit_name"``:``"无"``,`<br>```"aux_unit_name"``:``"无"``,`<br>```"num"``:``"2.0000"``,`<br>```"expect_num"``:``"2.0000"``,`<br>```"num2"``:``"2.0000"``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"total_cost"``:``"2.2222"`<br>```}],`<br>```"refund_no"``:``"2342344234"``,`<br>```"goods_type_count"``: 3,`<br>```"remark"``:``""``,`<br>```"goods_count"``:``"5.0000"``,`<br>```"flag_name"``:``"无"``,`<br>```"jit_refund_no"``:``"3453245345"``,`<br>```"operator_name"``:``"刘子渲"``,`<br>```"shop_id"``: 281,`<br>```"warehouse_name"``:``"nff1"``,`<br>```"warehouse_no"``:``"234234234"``,`<br>```"stockin_no"``:``"RK202212302"``,`<br>```"modified"``:``"2022-12-30 09:48:22"``,`<br>```"note_count"``: 0,`<br>```"status"``: 80,`<br>```"check_time"``:``"2022-12-30 09:48:22"``,`<br>```"shop_no"``:``"vip_yqf"`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.JitRefund.searchOrderWithDetail#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"您的查询时间过宽,查询时间不能大于30天"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

4.响应参数

4.响应参数

4.响应参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1