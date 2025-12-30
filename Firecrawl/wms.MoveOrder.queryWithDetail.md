---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.MoveOrder.queryWithDetail"
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

**wms.MoveOrder.queryWithDetail**（移位单查询）

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的移位单信息 |
| **1.2 适用版本：** 客户端 V1.4.4.9及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** |

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
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | n | 开始时间(最后更新时间) |
| 结束时间 | end\_time | String | 40 | n | 结束时间(最后更新时间) |
| 商家编码 | spec\_no | String | 40 | n | 商家编码 |
| 移位单号 | order\_no | String | 40 | n | 移位单号，不填则需要填写时间条件 |
| 业务类型 | type | Int |  | n | 0：移位<br>1：采购入库上架<br>2：补货上架<br>3：销退上架<br>4：拣货放回<br>5：货位清点<br>6：拣货下架<br>7：货位调优<br>8：清点处理<br>9：货品归集<br>10：其它入库上架<br>11：补货下架<br>12：补货放回<br>15：其它下架<br>16：其它上架<br>17：销退质检上架<br>18：补货暂存上架<br>19：补货移位<br>20：出库单驳回 |
| 移位单状态 | status | Int |  | n | 5:已取消,10:待审核,20:已审核 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | 否 | 库存相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 库存信息列表 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 移位单ID | rec\_id | Int | 11 | 是 | 移位单ID |
| 移位单号 | order\_no | String | 20 | 是 | 移位单号 |
| 业务类型 | type | Int | 1 | 是 | 0：移位<br>1：采购入库上架<br>2：补货上架<br>3：销退上架<br>4：拣货放回<br>5：货位清点<br>6：拣货下架<br>7：货位调优<br>8：清点处理<br>9：货品归集<br>10：其它入库上架<br>11：补货下架<br>12：补货放回<br>15：其它下架<br>16：其它上架<br>17：销退质检上架<br>18：补货暂存上架<br>19：补货移位<br>20：出库单驳回 |
| 状态 | status | Int | 1 | 是 | 5:已取消,10:待审核,20:已审核 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 修改时间 | modified | String |  | 是 | 修改时间 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 制单人 | creator\_name | String | 50 | 是 | 制单人 |
| 移位单明细 | detail\_list | List<Map<String, Object>> |  | 是 | 移位单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 移位单id | order\_id | Int | 11 | 是 | 移位单id |
| 单品id | spec\_id | Int | 11 | 是 | 单品id(货品档案单品的主键) |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 移位数量 | num | Decimal(19,4) |  | 是 | 移位数量 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 源货位 | from\_position\_no | String | 50 | 是 | 源货位 |
| 目标货位 | to\_position\_no | String | 50 | 是 | 目标货位 |
| 是否残品 | defect | bool | 1 | 是 | 是否残品 |
| 货品简称 | short\_name | String | 255 | 是 | 货品简称 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 批次号 | batch\_no | String | 40 | 是 | 批次号 |
| 有效期 | expire\_date | String | 40 | 是 | 有效期（毫秒级时间戳） |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.MoveOrder.queryWithDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.MoveOrder.queryWithDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.MoveOrder.queryWithDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.MoveOrder.queryWithDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"wms.MoveOrder.queryWithDetail"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.MoveOrder.queryWithDetail#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"order_no"``:``"YW2302160007"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"created"``: 1676535460000,`<br>```"detail_list"``: [{`<br>```"order_id"``: 23159,`<br>```"spec_id"``: 1,`<br>```"num"``: 2,`<br>```"defect"``:``false``,`<br>```"batch_no"``:``"230213001"``,`<br>```"from_position_no"``:``"销退暂存"``,`<br>```"to_position_no"``:``"20220317B"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"short_name"``:``""``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_code"``:``"LL "``,`<br>```"spec_name"``:``"暂无"``,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"barcode"``:``"wangdiantong"`<br>```}],`<br>```"modified"``: 1676535460000,`<br>```"remark"``:``""``,`<br>```"creator_name"``:``"aaa"``,`<br>```"rec_id"``: 23159,`<br>```"type"``: 0,`<br>```"status"``: 20`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.MoveOrder.queryWithDetail#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

4.响应参数

4.1 公共响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1