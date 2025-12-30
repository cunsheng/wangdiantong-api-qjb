---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.queryStockPd"
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

**wms.StockPd.queryStockPd（盘点单查询** **）**

### **¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内盘点单信息 |
| **1.2 适用版本：** 客户端V1.5.6.6及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：仓库权限** |

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
| 业务请求参数 | params | Map<String, Object> |  | 是 | 业务请求参数 |
| 分页 | pager | pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 是 | 开始时间，按照最后修改时间增量查询数据，yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | 是 | 结束时间，上同开始时间 |
| 仓库编号 | warehouse\_no | String | 40 | 否 | 仓库编号 |
| 盘点单号 | pd\_no | String | 20 | 否 | 系统盘点单编号，默认PD开头 |
| 商家编码 | spec\_no | String | 40 | 否 | 商家编码 |
| 货品编号 | goods\_no | String | 40 | 否 | 货品编号 |
| 状态 | status | Int | 4 | 否 | 不传默认获取全部<br>10：已取消<br>20：编辑中<br>30：待盘点<br>31：盘点中<br>33：部分盘点<br>35：待结算<br>40：已完成 |
| 制单人 | employee\_no | String | 40 | 否 | 制单人（员工编号） |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应正文数据 | data | Map<String, Object> |  | Y | 响应正文数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | pd\_list | List<Map<String, Object>> |  | Y | 响应数据节点 |
| 总数 | total\_count | Int | 11 | Y | 总数 |

**pd\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 盘点单id | rec\_id | Int | 11 | 是 | 盘点单id |
| 盘点单号 | pd\_no | String | 20 | 是 | 系统盘点单号，默认PD开头 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 仓库id | warehouse\_id | Int |  | 是 | 仓库id |
| 盘点方案 | mode | Int | 4 | 是 | 盘点方案<br>0：单品盘点<br>1：货位明细盘点<br>2：明细盘点<br>3：货位单品盘点 |
| 盘点单状态 | status | Int | 4 | 是 | 盘点单状态<br>10：已取消<br>20：编辑中<br>30：待盘点<br>31：盘点中<br>33：部分盘点<br>35：待结算<br>40：已完成 |
| 制单人 | creator\_no | String | 40 | 是 | 制单人（员工编号） |
| 操作员 | operator\_no | String | 40 | 是 | 操作员（员工编号） |
| 备注 | remark | String | 255 | 是 | 备注 |
| 修改时间 | modified | Date | 40 | 是 | 最后修改时间 |
| 创建时间 | created | Date | 40 | 是 | 创建时间 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | `[`<br>```{`<br>```"start_time"``:``"2023-1-1 00:00:00"``,`<br>```"end_time"``:``"2023-1-31 00:00:00"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2023-1-1 00:00:00'``;`<br>`$params``->end_time =``'2023-1-31 00:00:00'``;`<br>``<br>`$data``=``$client``->call(``"method: wms.StockPd.queryStockPd"``,``$params``);` | |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"pd_list"``: [{`<br>```"mode"``: 2,`<br>```"creator_no"``:``"nff"``,`<br>```"pd_no"``:``"PD2023022108"``,`<br>```"warehouse_no"``:``"234234234"``,`<br>```"created"``:``"2023-02-21 14:59:27"``,`<br>```"modified"``:``"2023-02-21 14:59:27"``,`<br>```"remark"``:``""``,`<br>```"rec_id"``: 9650,`<br>```"operator_no"``:``"nff"``,`<br>```"warehouse_id"``: 330,`<br>```"status"``: 40`<br>```}],`<br>```"total_count"``: 1`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"invalid http status 502"`<br>`}` | |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1