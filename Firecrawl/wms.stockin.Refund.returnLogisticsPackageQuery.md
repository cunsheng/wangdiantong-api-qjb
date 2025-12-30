---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.returnLogisticsPackageQuery"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

售后类

退货入库单查询

原始退款单推送

创建退货预入库

退换单查询

预入库单据查询

退货预入库单取消

历史退换单查询

原始退款单查询

原始退款单推送2

退货入库单推送

快速退货

历史退货入库单查询

历史原始退款单查询

退货物流包裹查询

当前位置： API文档 > 售后类

**wms.stockin.Refund.returnLogisticsPackageQuery（退货物流包裹查询** **）**

**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：退货物流分页查询 |
| **1.2 适用版本：** 客户端 V1.5.1.5及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

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
| 开始时间 | start\_time | String | 40 | Y | 最后修改时间 |
| 结束时间 | end\_time | String | 40 | Y | 最后修改时间 |
| 物流单号 | logistics\_no | String | 40 | N | 物流单号（当传入物流单号，其他不校验） |
| 入库单状态 | stockin\_status | bytre | 1 | N | 0全部；1待处理；2已取消；3编辑中；4待审核；5已完成 |

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
| 返回信息 | data | <Map<String, Object>> |  | 是 | 返回信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | record | List<Map<String, Object>> |  | 是 | 数据节点 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流单唯一键 | rec\_id | Int |  | Y | 物流单唯一主键 |
| 物流公司 | logistics\_name | String |  | Y | 物流公司名称 |
| 物流单号 | logistics\_no | String |  | Y | 物流单号 |
| 操作人员 | operator\_name | String |  | Y | 操作人员 |
| 创建日期 | created | String |  | Y | 创建时间  格式：yyyy-MM-dd HH:mm:ss |
| 退换单号 | refund\_no | String |  | Y | 退换单号 |
| 退换单状态 | refund\_status | Byte |  | Y | 处理状态 10已取消 20待审核 30已同意 40已拒绝 50待财审 60待收货 70部分到货 80待结算 90已完成 |
| 退换单入库状态 | refund\_stockin\_status | Byte |  | Y | 入库状态0未入库1待入库2部分入库3全部入库4终止入库(停止等待) |
| 入库单号 | stockin\_no | String |  | Y | 入库单号 |
| 入库状态 | stockin\_status | Byte |  | Y | -2待处理，10已取消，20编辑者，30待审核，37待质检，40质检待确认，80已完成 |
| 入库人 | stockin\_operator\_name | String |  | Y | 入库人 |
| 入库单审核日期 | check\_time | String |  | Y | 入库单审核日期  格式：yyyy-MM-dd HH:mm:ss |
| 首次拆包时间 | stockin\_time | String |  | Y | 首次拆包时间  格式：yyyy-MM-dd HH:mm:ss |
| 备注 | refund\_remark | String |  | Y | 备注 |
| 入库标记 | flag\_name | String |  | Y | 入库标记 |
| 预入库单号 | pre\_stockin\_no | String |  | Y | 预入库单号 |
| 预入库状态 | pre\_stockin\_status | Byte |  | Y | -2待处理，10已取消，20编辑者，30待审核，37待质检，40质检待确认，80已完成 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | `[`<br>```{`<br>```"startTime"``:``"2024-02-21 00:00:00"``,`<br>```"endTime"``:``"2024-03-18 00:00:00"``,`<br>```"logistics_no"``:``"SF202403050012"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params =``new``stdClass();`<br>``<br>`$params->start_time =``'2022-06-05 11:42:56'``;`<br>`$params->end_time =``'2022-07-19 11:42:56'``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$data = $client->pageCall(``"wms.stockin.Refund.returnLogisticsPackageQuery"``, $pager, $params);` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31 | `{`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"record"``: [`<br>```{`<br>```"rec_id"``: 152,`<br>```"logistics_id"``: 9,`<br>```"logistics_name"``:``"销售退货专用物流"``,`<br>```"logistics_no"``:``"SF202403050012"``,`<br>```"operator_id"``: 0,`<br>```"created"``:``"2024-03-05 10:13:07"``,`<br>```"refund_remark"``:``"签收人: ZPPPP"``,`<br>```"stockin_time"``:``"2024-04-05 12:12:57"``,`<br>```"is_disabled"``:``false``,`<br>```"flag_name"``:``"标记名称"``,`<br>```"refund_no"``:``"TK1811050027"``,`<br>```"refund_status"``: 20,`<br>```"refund_stockin_status"``: 0,`<br>```"stockin_no"``:``"RK1909190004"``,`<br>```"stockin_status"``: 80,`<br>```"stockin_operator_id"``: 1,`<br>```"check_time"``:``"2019-09-19 11:25:42"``,`<br>```"pre_stockin_no"``:``"test"``,`<br>```"pre_stockin_status"``: 0,`<br>```"operator_name"``:``"系统"``,`<br>```"stockin_operator_name"``:``"小二y"`<br>```}`<br>```]`<br>```},`<br>```"status"``: 0`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"end_time 不能为空"`<br>`}` | |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1