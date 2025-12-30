---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.queryWithDetail"
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

**wms.stockin.Other.queryWithDetail** **（其他入库单查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP其他入库单单据信息 |
| **1.2 适用版本：** 客户端 V1.5.6.6及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

**3.请求参数说明**

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

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 起始修改时间，若无入库单号或源单号，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束修改时间，上同开始时间 |
| 入库单状态 | status | String | 255 | N | 英文逗号拼接的状态值:<br>10=已取消，20=编辑中，30=待审核/待处理，37=待质检 ，40=质检待确认，80=已完成 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 入库单号 | stockin\_no | String | 20 | N | 入库单号 |
| 其它入库业务单号 | other\_stockin\_no | String | 40 | N | 其它入库业务单号 |
| 入库原因 | reason\_name | String |  | N | 入库原因 |
| wms借调单号 | wms\_stock\_change\_no | String | 40 | N | wms借调单号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 入库单相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 入库单相关数据 |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |

**Order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单ID | stockin\_id | Int | 11 | Y | 入库单ID |
| 入库单号 | order\_no | String | 20 | Y | 入库单号 |
| 状态 | status | Int | 4 | Y | 入库单状态<br>10=已取消，20=编辑中，30=待审核/待处理，37=待质检 ，40=质检待确认，80=已完成 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称 |
| 入库时间 | stockin\_time | String | 40 | Y | 入库时间 |
| 建单时间 | created\_time | String | 40 | Y | 建单时间 |
| 其他入库原因 | reason | String | 255 | Y | 其他入库原因 |
| 备注 | remark | String | 255 | Y | 入库单备注 |
| 货品总数 | goods\_count | Decimal(19,4) |  | Y | 货品总数 |
| 物流类型 | logistics\_type | Int | 6 | Y | 物流类型，点击查看 [物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb)（单据没有设置物流公司时 不返回） |
| 审核时间 | check\_time | String |  | Y | 审核时间 |
| 业务单号 | src\_order\_no | String | 40 | Y | 其它入库业务单号 |
| 操作员 | operator\_name | String | 40 | Y | 操作员（操作员为系统时不返回） |
| 总成本价 | total\_price | Decimal(19,4) |  | Y | 总成本价 |
| 入库总金额 | total\_cost | Decimal(19,4) |  | Y | 入库总金额 |
| 物流公司编号 | logistics\_company\_no | String | 20 | Y | 系统物流公司编号<br>（设置--基本设置--物流页面查看）（奇门自定义接口不返回） |
| wms借调单号 | wms\_stock\_change\_no | String | 40 | Y | wms借调单号 |
| 入库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 入库单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单ID | stockin\_id | Int | 11 | Y | 入库单ID |
| 数量 | goods\_count | Decimal(19,4) |  | Y | 数量 |
| 总成本 | total\_cost | Decimal(19,4) |  | Y | 总成本（存货成本\*数量） |
| 备注 | remark | String | 255 | Y | 备注 |
| 调整后数量 | right\_num | Decimal(19,4) |  | Y | 调整后数量 |
| 单位 | goods\_unit | String | 20 | Y | 单位 |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 明细id | rec\_id | Int | 11 | Y | 明细id(主键) |
| 生产日期 | production\_date | String | 40 | Y | 生产日期 |
| 有效期 | expire\_date | String | 40 | Y | 有效期 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 自定义属性2 | prop2 | String | 255 | Y | 自定义属性2（货品档案单品自定义属性2） |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 是否残品 | defect | bool | 1 | Y | true：残次品<br>false：正品 |
| 入库价 | checked\_cost\_price | Decimal(19,4) |  | Y | 入库价 |
| 货位编号 | position\_no | String | 20 | Y | 货位编号 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.queryWithDetail#autoTab5_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>```"start_time"``:``"2019-12-11 00:00:00"``,`<br>```"end_time"``:``"2019-12-31 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2019-12-11 00:00:00'``;`<br>`$params``->end_time =``'2019-12-31 00:00:00'``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockin.Other.queryWithDetail"``,``$pager``,``$params``);`<br>``<br>`?>` |

**6.响应示例**

6.1正常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.queryWithDetail#autoTab5_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"order_no"``:``"RK20230131126"``,`<br>```"created_time"``: 1675146120000,`<br>```"reason"``:``"赠品"``,`<br>```"stockin_id"``: 88995,`<br>```"total_cost"``: 91.12,`<br>```"total_price"``: 91.12,`<br>```"logistics_no"``:``"4569521447558522"``,`<br>```"detail_list"``: [{`<br>```"stockin_id"``: 88995,`<br>```"goods_count"``: 2,`<br>```"total_cost"``: 27.12,`<br>```"defect"``:``false``,`<br>```"remark"``:``""``,`<br>```"right_num"``: 2,`<br>```"goods_unit"``:``"箱"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"rec_id"``: 210759,`<br>```"production_date"``:``""``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"prop2"``:``"自定义属性2"``,`<br>```"spec_name"``:``"暂无"``,`<br>```"spec_code"``:``"LL "``,`<br>```"brand_no"``:``"ffl"``,`<br>```"brand_name"``:``"发发拉"``,`<br>```"checked_cost_price"``: 13.56,`<br>```"position_no"``:``"其它未上架"`<br>```}, {`<br>```"stockin_id"``: 88995,`<br>```"goods_count"``: 5,`<br>```"total_cost"``: 64,`<br>```"defect"``:``false``,`<br>```"remark"``:``""``,`<br>```"right_num"``: 5,`<br>```"goods_unit"``:``"只"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"rec_id"``: 210760,`<br>```"production_date"``:``""``,`<br>```"goods_name"``:``"wtt"``,`<br>```"goods_no"``:``"wtt"``,`<br>```"spec_no"``:``"wtt"``,`<br>```"prop2"``:``""``,`<br>```"spec_name"``:``"wtt"``,`<br>```"spec_code"``:``"wtt"``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"brand_name"``:``"无"``,`<br>```"checked_cost_price"``: 12.8,`<br>```"position_no"``:``"其它未上架"`<br>```}],`<br>```"remark"``:``"备注备注"``,`<br>```"goods_count"``: 7,`<br>```"logistics_company_no"``:``"qtyw"``,`<br>```"src_order_no"``:``"QR202301310015"``,`<br>```"operator_name"``:``"aaa"``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"logistics_type"``: 6,`<br>```"stockin_time"``: 1675146126000,`<br>```"status"``: 80,`<br>```"check_time"``: 1675146126000`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.queryWithDetail#autoTab6_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"仓库不存在"`<br>`}` |

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