---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryChangeHistory"
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

**wms.StockSpec.queryChangeHistory** **（库存变化查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP库存变化信息 |
| **1.2 适用版本：** 客户端 V1.5.3.6及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_date和end\_date最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** <br>如传入商家编码，start\_date和end\_date最大跨度为30天，<br>如不传入商家编码，start\_date和end\_date最大跨度为60min。 |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** |

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
| 秒级时间戳 | timestamp | int |  | Y | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法. |
| 签名 | sign | String |  | Y | 签名 |
| 分页大小 | page\_size | int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_date | String | 40 | Y | 开始时间(最后更新时间) |
| 结束时间 | end\_date | String | 40 | Y | 结束时间(最后更新时间) |
| 商家编码 | spec\_no | String | 40 | N | 商家编码 |
| 类型 | type | Int | 4 | N | 1.入库   2.出库   不传为出入库 |
| 是否残次品 | defect | boolean | 1 | N | true：残次品；false：正品<br>**默认false只返回正品库存变化** |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | N | 单据数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | data | List<Map<String,   Object>> |  | Y | 库存信息列表 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 操作 | src\_order\_type | Int | 4 | Y | 1 销售出库<br>2 调拨单<br>4 盘点单<br>5 生产单<br>6 生产成品入库<br>7 保修入库<br>8 正残转换<br>10 采购入库<br>12 退货入库<br>13 JIT退货入库<br>14 采购退货出库<br>20 其它入库<br>21 其它出库<br>22 退货预入库<br>23 调整入库<br>24 调整出库<br>33 初始化入库<br>34 初始化出库 |
| 类型 | type | Int | 4 | Y | 类型，1、入库 2、出库 |
| 仓库名称 | warehouse\_name | String |  | Y | 仓库名称 |
| 仓库编码 | warehouse\_no | String |  | Y | 仓库编码 |
| 商家编码 | spec\_no | String |  | Y | 商家编码 |
| 前库存 | stock\_num\_old | Decimal(19,4) |  | Y | 前库存 |
| 本次出入库存 | num | Decimal(19,4) |  | Y | 本次出入库存 |
| 后库存 | stock\_num\_new | Decimal(19,4) |  | Y | 后库存 |
| 出入库单号 | stockio\_no | String | 40 | Y | 出入库单号 |
| 来源单号 | src\_order\_no | String | 40 | Y | 来源单号 |
| 操作人 | operator\_name | String | 40 | Y | 操作人 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 备注 | remark | String | 255 | Y | 备注 |
| 是否残次品 | defect | bool | 1 | Y | 残次品：true<br>正品：false |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryChangeHistory#autoTab4_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryChangeHistory#autoTab4_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryChangeHistory#autoTab4_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryChangeHistory#autoTab4_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>```"start_date"``:``"2020-01-01 00:00:00"``,`<br>```"end_date"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_date =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_date =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"wms.StockSpec.queryChangeHistory"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryChangeHistory#autoTab4_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"data"``: [{`<br>```"actual_weight_new"``: 0.0000,`<br>```"created"``: 1724225774000,`<br>```"src_order_type"``: 1,`<br>```"num"``: 10.0000,`<br>```"stock_num_new"``: 100155.0000,`<br>```"remark"``:``""``,`<br>```"type"``: 2,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"src_order_no"``:``"JY202408210092"``,`<br>```"actual_weight"``: 0.0000,`<br>```"operator_name"``:``"aaa2"``,`<br>```"defect"``:``false``,`<br>```"stock_num_old"``: 100165.0000,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"stockio_no"``:``"CK2024082138"``,`<br>```"actual_weight_old"``: 0.0000`<br>```}],`<br>```"total_count"``: 1`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.queryChangeHistory#autoTab5_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"您的查询时间过宽,不传商家编码,查询时间不能大于1小时"`<br>`}` |

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