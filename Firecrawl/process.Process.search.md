---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Process.search"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

货品类

货品推送

组合装查询

货品档案查询

平台货品查询

平台货品推送

物料清单推送

生产单推送

生产单查询

货品分类查询

品牌查询

组合装创建/更新

平台类目查询

货品批量推送

物料清单查询

条码上传

货品推送2

新建分类

货品品牌新建/更新

生产结算单查询

当前位置： API文档 > 货品类

**process.Process.search** **（生产单查询）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP生产单信息 |
| **1.2 适用版本：** 客户端 V1.5.3.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time与end\_time 起止时间区间不能超过30天 |
| **1.5 注意事项：** |

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
| 开始时间 | start\_time | String | 40 | N | yyyy-MM-dd HH:mm:ss格式, 最后修改时间。当不使用其它条件时必须使用时间条件 |
| 结束时间 | end\_time | String | 40 | N | 结束时间，上同开始时间 |
| 出库仓库编号 | out\_warehouse\_no | String |  | N | 出库仓库编号 |
| 入库仓库编号 | in\_warehouse\_no | String |  | N | 入库仓库编号 |
| 当前状态 | status | Int |  | N | 当前状态<br>10:已取消;20:编辑中;30:待审核;40:待领料;45:已领料;50:执行中;60:生产结束;70:已完成 |
| 生产单号 | process\_no | String |  | N | 生产单号 |

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
| 单据数据 | data | Map<String, Object> |  | Y | 单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 单据数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 生产单唯一键 | process\_id | Int | 11 | Y | 生产单唯一键 |
| 生产单号 | process\_no | String | 64 | Y | 生产单号 |
| 当前状态 | status | byte | 4 | Y | 当前状态<br>10:已取消;20:编辑中;30:待审核;40:待领料;45:已领料;50:执行中;60:生产结束;70:已完成80:待推送  ;90:委外待加工 |
| 结算状态 | settle\_status | byte | 4 | Y | 结算状态<br>0:不可结算;1:待结算;3:已结算 |
| 生产员 | operator\_name | String | 50 | Y | 生产员（员工昵称） |
| 生产员id | operator\_id | Int | 11 | Y | 生产员id |
| 生产商 | producer\_name | String | 64 | Y | 生产商名称 |
| 生产商id | producer\_id | Int | 11 | Y | 生产商id |
| 物料清单名称 | bom\_name | String | 255 | Y | 物料清单名称 |
| 生产费用 | bom\_fee | BigDecimal(19,4) |  | Y | 生产费用 |
| 损耗费用 | loss\_fee | BigDecimal(19,4) |  | Y | 损耗费用 |
| 物料单备注 | bom\_remark | String | 255 | Y | 物料单备注 |
| 生产费用合计 | total\_fee | BigDecimal(19,4) |  | Y | 生产费用合计 |
| 计划生产次数 | process\_count | BigDecimal(19,4) |  | Y | 计划生产次数 |
| 实际生产次数 | reality\_count | BigDecimal(19,4) |  | Y | 实际生产次数 |
| 生产类型 | process\_type | Boolean |  | Y | true：分步生产  <br>false：快速生产 |
| 出库仓库编号 | out\_warehouse\_no | String | 40 | Y | 出库仓库编号 |
| 出库仓库id | out\_warehouse\_id | Int | 11 | Y | 出库仓库id |
| 入库仓库编号 | in\_warehouse\_no | String | 40 | Y | 入库仓库编号 |
| 入库仓库id | in\_warehouse\_id | Int | 11 | Y | 入库仓库id |
| 标记名称 | flag\_name | String | 32 | Y | 标记名称 |
| 标记名称id | flag\_id | Int | 11 | Y | 标记名称id |
| 建单人 | creator\_name | String | 50 | Y | 建单人（员工昵称） |
| 建单人id | creator\_id | Int | 11 | Y | 建单人id |
| 审核人 | checker\_name | String | 50 | Y | 审核人（员工昵称） |
| 审核人id | checker\_id | Int | 11 | Y | 审核人id |
| 生产单备注 | remark | String | 255 | Y | 生产单备注 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间 |
| 预计完成时间 | estimated\_time | String |  | Y | 预计完成时间 |
| 审核时间 | check\_time | String |  | Y | 审核时间 |
| 建单时间 | created | String |  | Y | 建单时间 |
| 生产单明细 | detail\_list | List<Map<String, Object>> |  | Y | 生产单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 生产单唯一键 | process\_id | Int | 11 | Y | 生产单唯一键 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 已损坏数量 | bad\_num | BigDecimal(19,4) |  | Y | 已损坏数量 |
| 损坏已入库数量 | bad\_in\_num | BigDecimal(19,4) |  | Y | 损坏已入库数量 |
| 余料/成品已入库数量 | in\_num | BigDecimal(19,4) |  | Y | 余料/成品已入库数量 |
| 已出库数量 | out\_num | BigDecimal(19,4) |  | Y | 已出库数量 |
| 已生产数量 | process\_num | BigDecimal(19,4) |  | Y | 已生产数量 |
| 数量 | num | BigDecimal(19,4) |  | Y | 数量 |
| 是否成品 | is\_product | bool | 1 | Y | 0：原料<br>1：成品 |
| 货位编号 | position\_no | String | 20 | Y | 货位编号(无货位信息该字段不返回) |
| 批次编号 | batch\_no | String | 20 | Y | 批次编号(无批次信息该字段不返回) |
| 生产日期 | production\_date | String |  | Y | 生产日期（无生产日期该字段不返回） |
| 保质期 | validity\_days | Int | 6 | Y | 保质期（无保质期该字段不返回） |
| 生产单备注 | remark | String | 255 | Y | 生产单备注 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Process.search#autoTab4_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Process.search#autoTab4_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Process.search#autoTab4_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Process.search#autoTab4_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2021-08-01 00:00:00"``,``"end_time"``:``"2021-08-31 23:59:59"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2021-08-00 00:00:00'``;`<br>`$params``->end_time =``'2021-08-15 00:00:00'``;`<br>``<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>`$data``=``$client``->pageCall(``"process.Process.search"``,``$pager``,``$params``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1正常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Process.search#autoTab4_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"flag_id"``: 0,`<br>```"out_warehouse_no"``:``"wdtapi3-test"``,`<br>```"process_id"``: 471,`<br>```"in_warehouse_no"``:``"wdtapi3-test"``,`<br>```"operator_id"``: 504,`<br>```"detail_list"``: [{`<br>```"process_id"``: 471,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"bad_num"``: 0.0000,`<br>```"bad_in_num"``: 0.0000,`<br>```"in_num"``: 0.0000,`<br>```"out_num"``: 2.0000,`<br>```"process_num"``: 2.0000,`<br>```"num"``: 2.0000,`<br>```"is_product"``:``false``,`<br>```"batch_no"``:``""``,`<br>```"remark"``:``""`<br>```}, {`<br>```"process_id"``: 471,`<br>```"spec_no"``:``"08070201"``,`<br>```"bad_num"``: 0.0000,`<br>```"bad_in_num"``: 0.0000,`<br>```"in_num"``: 1.0000,`<br>```"out_num"``: 0.0000,`<br>```"process_num"``: 1.0000,`<br>```"num"``: 1.0000,`<br>```"is_product"``:``true``,`<br>```"batch_no"``:``""``,`<br>```"production_date"``: 1724256000000,`<br>```"validity_days"``: 0,`<br>```"remark"``:``""`<br>```}],`<br>```"remark"``:``""``,`<br>```"checker_id"``: 0,`<br>```"flag_name"``:``"无"``,`<br>```"total_fee"``: 0.0000,`<br>```"modified"``:``"2024-08-22 13:40:50"``,`<br>```"process_type"``:``false``,`<br>```"bom_name"``:``""``,`<br>```"checker_name"``:``"系统"``,`<br>```"reality_count"``: 1.0000,`<br>```"in_warehouse_id"``: 311,`<br>```"out_warehouse_id"``: 311,`<br>```"created"``:``"2024-08-22 13:40:50"``,`<br>```"process_count"``: 1.0000,`<br>```"settle_status"``: 3,`<br>```"operator_name"``:``"wdtapi3-test2_c"``,`<br>```"producer_name"``:``"刘子渲生产商"``,`<br>```"creator_id"``: 502,`<br>```"producer_id"``: 1,`<br>```"creator_name"``:``"aaa2"``,`<br>```"process_no"``:``"PS2024082201"``,`<br>```"loss_fee"``: 0.0000,`<br>```"bom_remark"``:``""``,`<br>```"bom_fee"``: 0.0000,`<br>```"status"``: 70,`<br>```"estimated_time"``:``""``,`<br>```"check_time"``:``"2024-08-22 13:40:50"`<br>```}]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Process.search#autoTab5_0)

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

3.3业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1正常响应示例

6.2异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1