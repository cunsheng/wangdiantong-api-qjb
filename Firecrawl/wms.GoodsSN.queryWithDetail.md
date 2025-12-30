---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.GoodsSN.queryWithDetail"
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

**wms.GoodsSN.queryWithDetail（SN码查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP序列号管理页面的数据 |
| **1.2 适用版本：** 客户端 V1.5.7.2及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** start\_time与end\_time起止时间跨度不超过30天 |
| **1.5注意事项：** |

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
| 开始时间 | start\_time | String | 40 | n | sn创建开始时间 |
| 结束时间 | end\_time | String | 40 | n | sn创建结束时间 |
| 时间类型 | time\_type | Int |  | n | 0：创建时间<br>1：更新时间<br>默认0 |
| 单据类型 | order\_type | Byte |  | n | 0：出库单<br>1：入库单<br>默认0 |
| 源单据类型 | src\_order\_type | Byte |  | n | 源单据类型<br>1：销售出库<br>2：调拨出库/调拨入库<br>5：生产出库/生产原料入库<br>6：生产入库<br>10：采购入库<br>12：退货入库<br>14：采购退货出库<br>20：其他入库<br>21：其他出库 |
| 序列号 | sn | String |  | n | 序列号，传入该字段可以不传起止时间 |
| 出入库单号 | order\_no | String |  | n | 出入库单号，传入该字段可以不传起止时间 |
| 商家编码 | spec\_no | String |  | n | 商家编码 |
| 状态 | status | Int |  | n | 10：初始录入<br>15：二次录入<br>20：已入库<br>30：已占用<br>40：已出库 |
| 仓库编号 | warehouse\_no | String |  | n | 仓库编号 |

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
| 单据数据 | data | Map<String, Object> |  | n | 单据数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 序列号信息 | sn\_list | List<Map<String, Object>> |  | y | 序列号信息 |
| 总数 | total\_count | Int | 11 | n | 查询条件总数单据 |

**sn\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一键 | rec\_id | Int | 11 | y | 唯一键 |
| sn编号 | sn | String | 80 | y | sn编号 |
| 商家编码 | spec\_no | String | 40 | y | 商家编码 |
| 出库单号 | stockout\_no | String | 40 | y | 出库单号<br>order\_type=0时返回 |
| 入库单号 | stockin\_no | String | 40 | y | 入库单号<br>order\_type=1时返回 |
| 源单号 | src\_order\_no | String | 40 | y | 源单号 |
| 源单据类型 | src\_order\_type | Byte |  | y | 源单据类型<br>1：销售出库<br>2：调拨出库/调拨入库<br>5：生产出库/生产原料入库<br>6：生产入库<br>10：采购入库<br>12：退货入库<br>14：采购退货出库<br>20：其他入库<br>21：其他出库 |
| 创建时间 | created | String |  | y | 创建时间<br>格式: yyyy-MM-dd HH:mm:ss |
| 状态 | status | Integer |  | y | 10：初始录入<br>15：二次录入<br>20：已入库<br>30：已占用<br>40：已出库 |
| 仓库名称 | warehouse\_name | String | 40 | y | 仓库名称 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 辅助序列号 | second\_sn | String |  | n | 辅助序列号 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | `[`<br>```{`<br>```"start_time"``:``"2022-11-01 00:00:00"``,`<br>```"end_time"``:``"2022-11-28 17:59:59"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params =``new``stdClass();`<br>`$params->start_time =``'2022-11-01 00:00:00'``;`<br>`$params->end_time =``'2022-11-28 17:59:59'``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$data = $client->pageCall(``"wms.GoodsSN.queryWithDetail"``, $pager, $params);`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 22,`<br>```"sn_list"``: [`<br>```{`<br>```"created"``:``"2022-11-03 16:06:15"``,`<br>```"stockout_no"``:``"CK2022042917"``,`<br>```"src_order_type"``: 1,`<br>```"sn"``:``"ytzxlh6000"``,`<br>```"rec_id"``: 5857,`<br>```"spec_no"``:``"ytzxlh6"``,`<br>```"src_order_no"``:``"JY202204290019"`<br>```}`<br>```]`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"您的查询时间过宽,查询时间不能大于30天"`<br>`}` | |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1