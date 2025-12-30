---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Process.queryWithDetail"
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

**wms.stockout.Process.queryWithDetail** **（生产出库查询 ）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")¥标准**

**1.接口说明**

|     |
| --- |
| 1.1 接口描述：获取ERP生产出库信息 |
| 1.2 适用版本：客户端 V1.4.6.8及以上版本 |
| 1.3 增量获取： |
| 1.4 时间跨度：start\_time和end\_time最大跨度为30天 |
| 1.5 注意事项：【权限校验】：仓库权限 |

2.调用场景

|     |
| --- |
| 2.1举例说明：SAP、线下ERP、SRM、SCM等系统对接 |

3.请求参数说明

3.1 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | http://47.92.239.46/openapi |
| 正式环境 | http://wdt.wangdian.cn/openapi |

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

params

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无出库单编码或生产单编码，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int | 4 | N | 时间判断的类型，1为建单时间，2为出库时间，3为最后修改时间<br>默认为建单时间 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 出库单号 | stockout\_no | String | 40 | N | 出库单号 |
| 生产单号 | process\_no | String | 64 | N | 生产单号 |
| 出库单状态 | status | String | 255 | N | 出库单状态：<br>5: 已取消<br>48: 未确认<br>50: 待审核<br>77: 拣货中<br>110: 已完成<br>用逗号分隔开数字的分隔符 |

pager

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小不能超过2000 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

4.响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 单据相关数据 |

data

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 生产出库单 | order | List<Map<String, Object>> |  | Y | 生产出库单数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

Order

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单id | stockout\_id | Int |  | Y | 出库单id |
| 物流公司 | logistics\_name | String | 40 | Y | 物流公司名称 |
| 发货时间 | consign\_time | String | 40 | Y | 出库单执行出库操作的时间 |
| 错误信息 | error\_info | String | 255 | Y | 接口处理错误信息 |
| 货品种类数 | goods\_type\_count | Int | 6 | Y | 货品种类数 |
| 备注 | remark | String | 255 | Y | 备注 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 总成本价 | checked\_goods\_total\_cost | Decimal(19,4) |  | Y | 审核时货品总成本价 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 便签条数 | note\_count | Int | 6 | Y | 便签条数 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 制单时间 | created | String | 40 | Y | 制单时间 |
| 出库单号 | stockout\_no | String | 40 | Y | 出库单号 |
| 出库单源单据类型 | src\_order\_type | Int | 4 | Y | 5生产出库 |
| 制单人 | operator\_name | String | 40 | Y | 制单人 |
| 邮费 | weigh\_post\_cost | Decimal(19,4) |  | Y | 邮费 |
| 生产商名称 | producer\_name | String | 40 | Y | 生产商名称 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 出库的仓库名称 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 签出人 | checkouter\_name | String | 40 | Y | 签出人 |
| 生产单号 | process\_no | String | 40 | Y | 生产单号 |
| 状态 | status | Int | 4 | Y | 出库单状态：<br>5: 已取消<br>48: 未确认<br>50: 待审核<br>77: 拣货中<br>110: 已完成 |
| 标记id | flag\_id | Int |  | Y | 标记id |
| 标记名称 | flag\_name | String | 32 | Y | 标记名称 |
| 生产出库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 生产出库单的明细信息 |

detail\_list

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细id | rec\_id | Int | 11 | Y | 明细id |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品简称 | short\_name | String | 255 | Y | 货品简称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 条码 | barcode | String | 50 | Y | 条码 |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 验货方式 | scan\_type | Int | 4 | Y | 验货方式<br>0：未验货<br>1：扫描验货<br>2：手工验货 |
| 残次品 | defect | bool | 1 | Y | 是否残次品<br>true:残次品<br>false:正品 |
| 有效期 | expire\_date | String | 40 | N | 指定出库货品有效期 |
| 备注 | remark | String | 255 | Y | 备注 |
| 货位 | position\_no | String | 20 | N | 货位编号 |
| 批次 | batch\_no | String | 40 | N | 批次号 |
| 预期出库量 | expect\_num | Decimal(19,4) |  | Y | 预期出库量 |
| 成本价 | checked\_cost\_price | Decimal(19,4) |  | Y | 审核时成本价 |
| 品牌 | brand\_name | String | 64 | Y | 品牌名称 |
| 辅助单位 | aux\_unit\_name | String | 20 | Y | 辅助单位 |
| 单位 | base\_unit\_name | String | 20 | Y | 单位 |
| 出库货位明细 | position\_details\_list | List<Map<String, Object>> |  | Y | 出库货位明细 |

**position\_details\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库货位明细主键 | rec\_id | Int | 11 | Y | 出库货位明细主键 |
| --- | --- | --- | --- | --- | --- |
| 出库明细主键 | stockout\_detail\_id | Int | 11 | Y | 出库明细主键 |
| --- | --- | --- | --- | --- | --- |
| 货位id | position\_id | Int | 11 | Y | 货位id |
| --- | --- | --- | --- | --- | --- |
| 货位号 | position\_no | String | 20 | Y | 货位号 |
| --- | --- | --- | --- | --- | --- |
| 有效期 | expire\_date | String |  | Y | 有效期 |
| --- | --- | --- | --- | --- | --- |
| 生产日期 | production\_date | String |  | Y | 生产日期 |
| --- | --- | --- | --- | --- | --- |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| --- | --- | --- | --- | --- | --- |
| 当前货位出库总货品数量 | position\_goods\_count | Decimal(19,4) |  | Y | 当前货位出库总货品数量 |
| --- | --- | --- | --- | --- | --- |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Process.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Process.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Process.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Process.queryWithDetail#autoTab5_3)

|     |     |
| --- | --- |
| 1<br>2 | `[{``"stockout_no"``:``""``,``"warehouse_no"``:``"lich0313"``,``"process_no"``:``"PS2018101002"``,``"status"``:``"5,110"``,``"time_type"``:``"2"``,``"start_time"``:``"2020-06-15`<br>`10:05:36"``,``"end_time"``:``"2020-06-17 11:05:36"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19 | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>`$pars``=``array`<br>`(`<br>```'stockout_no'``=>``''``,`<br>```'warehouse_no'``=>``'lich0313'``,`<br>```'process_no'``=>``'PS2018101002'``,`<br>```'time_type'``=>``'2'``,`<br>```'start_time'``=>``'2020-06-15 10:05:36'``,`<br>```'end_time'``=>``'2020-06-17 11:05:36'`<br>`);`<br>`$pager``=``new``Pager(50, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.Process.queryWithDetail"``,``$pager``,``$pars``);``//分页方法`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | `Client client = DefaultClient.get(sid, url, appkey, appsecret);`<br>`StockoutAPI stockoutApi = ApiFactory.get(client, StockoutAPI.``class``);`<br>`ProcessStockoutRequest request =``new``ProcessStockoutRequest();`<br>`request.setProcessNo(``"PS2020062202"``);`<br>`request.setStatus(``"5,110"``);`<br>`ProcessStockoutResponse response = stockoutApi.searchProcess(request,``new``Pager(50, 0, true));` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | `IClient client =``new``DefaultClient(sid, url, appkey, appsecret);`<br>`stockout.StockoutAPI stockinAPI = ApiFactory<stockout.StockoutAPI>.Get(client);`<br>`var``pars =``new``stockout.ProcessStockoutParams`<br>`{`<br>`processNo =``"PS2020062202"`<br>`};`<br>`var``pager =``new``Pager(50, 0, true);`<br>`stockout.ProcessStockoutResult result = stockinAPI.SearchProcess(pars, pager);` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Process.queryWithDetail#autoTab5_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [`<br>```{`<br>```"flag_id"``: 0,`<br>```"logistics_name"``:``"无"``,`<br>```"consign_time"``:``"2024-08-22 13:40:50"``,`<br>```"error_info"``:``""``,`<br>```"detail_list"``: [`<br>```{`<br>```"rec_id"``: 879427,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"short_name"``:``"简称测试"``,`<br>```"spec_code"``:``"wangdiantong"``,`<br>```"spec_name"``:``"wangdiantong"``,`<br>```"spec_id"``: 1,`<br>```"barcode"``:``"6971415833474"``,`<br>```"num"``: 2,`<br>```"scan_type"``: 0,`<br>```"defect"``:``false``,`<br>```"expire_date"``:``""``,`<br>```"remark"``:``"快速生产原料出库"``,`<br>```"position_no"``:``""``,`<br>```"batch_no"``:``""``,`<br>```"expect_num"``: 2,`<br>```"checked_cost_price"``: 0.1168,`<br>```"brand_name"``:``"淘淘乐"``,`<br>```"aux_unit_name"``:``"20件/套"``,`<br>```"base_unit_name"``:``"KG"``,`<br>```"position_details_list"``: [`<br>```{`<br>```"rec_id"``: 257172,`<br>```"stockout_detail_id"``: 879427,`<br>```"position_id"``: -2,`<br>```"position_no"``:``"采购未上架"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"production_date"``:``""``,`<br>```"position_goods_count"``: 2`<br>```}`<br>```]`<br>```}`<br>```],`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"goods_count"``: 2,`<br>```"stockout_id"``: 675378,`<br>```"flag_name"``:``"无"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"checked_goods_total_cost"``: 0.2336,`<br>```"modified"``:``"2024-08-22 13:40:50"``,`<br>```"note_count"``: 0,`<br>```"logistics_no"``:``""``,`<br>```"created"``:``"2024-08-22 13:40:50"``,`<br>```"stockout_no"``:``"CK2024082224"``,`<br>```"src_order_type"``: 5,`<br>```"operator_name"``:``"aaa2"``,`<br>```"weigh_post_cost"``: 0,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"checkouter_name"``:``"系统"``,`<br>```"producer_name"``:``"刘子渲生产商"``,`<br>```"process_no"``:``"PS2024082201"``,`<br>```"status"``: 110`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Process.queryWithDetail#autoTab6_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"状态参数格式不正确，请用以逗号隔开的整数字符串为参数"``}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1正常响应示例

6.2异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1