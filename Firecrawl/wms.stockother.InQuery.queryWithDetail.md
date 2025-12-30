---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.InQuery.queryWithDetail"
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

**wms.stockother.InQuery.queryWithDetail** **（** **其它入库业务单查询** **）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**获取ERP其他入库业务单信息 |
| **1.2 适用版本：** 客户端 V1.5.4.3及以上版本 |
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
| 时间类型 | time\_type | Int | 40 |  | 1：创建时间；<br>2：最后修改时间<br>不传默认为创建时间 |
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无业务单号，则为必填。<br>yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间. |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 业务单号 | other\_in\_no | String | 40 | N | 业务单号 |
| 业务单据状态 | status | string | 4 | N | 业务单据状态：<br>1:编辑中;<br>10:待审核;<br>20:已审核;<br>40:已推送wms;<br>60:部分入库<br>65:待结算;<br>70:已完成;<br>80:已取消 |
| 模糊查询 | fuzzy\_query | boolean | 1 | N | 默认false,业务单号模糊查询匹配，匹配数量大于1条时会报错 |

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
| 单据数据 | order | List<Map<String, Object>> |  | Y | 入库单相关数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**Order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务单id | rec\_id | Int | 11 | Y | 业务单id |
| 业务单号 | other\_in\_no | String | 40 | Y | 业务单号 |
| 状态 | status | Int | 4 | Y | 状态：<br>1:编辑中;<br>10:待审核;<br>20:已审核;<br>40:已推送wms;<br>60:部分入库;<br>65:待结算;<br>70:已完成;<br>80:已取消 |
| 入库的仓库编号 | warehouse\_no | String | 40 | Y | 入库的仓库编号 |
| 仓库名称 | warehouse\_name | String |  | Y | 仓库名称 |
| 仓库id | warehouse\_id | Int | 6 | Y | 仓库id |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 物流名称 | logistics\_name | String |  | Y | 物流名称 |
| 物流id | logistics\_id | Int | 6 | Y | 物流id |
| 入库单备注 | remark | String | 255 | Y | 入库单备注 |
| 制单人 | employee\_name | String | 40 | Y | 制单人 |
| 便签条数 | note\_count | Int | 4 | Y | 便签条数 |
| 入库原因 | reason | String | 255 | Y | 入库原因 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 其他入库业务单自定义属性1 | prop1 | String | 255 | N | 其他入库业务单自定义属性1 |
| 其他入库业务单自定义属性2 | prop2 | String | 255 | N | 其他入库业务单自定义属性2 |
| 其他入库业务单自定义属性3 | prop3 | String | 255 | N | 其他入库业务单自定义属性3 |
| 其他入库业务单自定义属性4 | prop4 | String | 255 | N | 其他入库业务单自定义属性4 |
| 其他入库业务单自定义属性5 | prop5 | String | 255 | N | 其他入库业务单自定义属性5 |
| 其他入库业务单自定义属性6 | prop6 | String | 255 | N | 其他入库业务单自定义属性6 |
| wms单号 | outer\_no | String |  | N | wms单号（奇门自定义场景无此字段返回） |
| 业务单明细 | detail\_list | List<Map<String, Object>> |  | Y | 业务单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务单详情id | rec\_id | Int | 11 | Y | 业务单详情id |
| 业务单id | other\_in\_id | Int | 11 | Y | 业务单id |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | Y | 辅助数量 |
| 已入库数量 | in\_num | Decimal(19,4) |  | Y | 已入库数量 |
| 有效期 | expire\_date | String | 40 | Y | 指定入库货品有效期 |
| 备注 | remark | Sting | 64 | Y | 入库业务单详情备注 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编码 | goods\_no | String | 40 | Y | 货品编码 |
| 货品id | goods\_id | Int | 11 | Y | 货品id |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 货品简称 | short\_name | String | 40 | Y | 货品简称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 条码 | barcode | String | 40 | Y | 条码 |
| 货位编号 | position\_no | String | 20 | N | 货位编号 |
| 是否残次品 | defect | boolean | 1 | Y | true:  残次品<br>false:  正品 |
| 修改时间 | modified\_date | String |  | Y | 修改时间 |
| 创建时间 | created\_date | String |  | Y | 创建时间 |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 生产日期 | production\_date | String |  | Y | 生产日期 |
| 单价 | price | Decimal(19,4) |  | Y | 单据明细上记录的单价(奇门自定义接口不返回) |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.InQuery.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.InQuery.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.InQuery.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.InQuery.queryWithDetail#autoTab5_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2020-10-23 00:00:00"``,``"end_time"``:``"2020-11-22 00:00:00"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client = new WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$parMap = new stdClass();`<br>`$parMap->start_time =``"2020-10-23 00:00:00"``;`<br>`$parMap->end_time =``"2020-11-22 00:00:00"``;`<br>``<br>``<br>`$pager = new Pager(1, 0,``true``);`<br>`$data = $client->pageCall(``"wms.stockother.InQuery.queryWithDetail"``, $pager, $parMap);`<br>`$php_json = json_encode($data);`<br>``<br>`?>` |

**6.响应示** **例**

6.1正常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.InQuery.queryWithDetail#autoTab5_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [`<br>```{`<br>```"logistics_name"``:``"无"``,`<br>```"reason"``:``"无"``,`<br>```"logistics_no"``:``""``,`<br>```"created"``: 1727166220000,`<br>```"detail_list"``: [`<br>```{`<br>```"rec_id"``: 141412,`<br>```"other_in_id"``: 17529,`<br>```"num"``: 1,`<br>```"num2"``: 0.05,`<br>```"defect"``:``false``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"remark"``:``""``,`<br>```"spec_id"``: 1,`<br>```"goods_id"``: 1,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"short_name"``:``""``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_code"``:``"wangdiantong"``,`<br>```"spec_name"``:``"wangdiantong"``,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"barcode"``:``"11111111"``,`<br>```"in_num"``: 0,`<br>```"price"``: 0.1162,`<br>```"modified_date"``:``"2024-09-24 16:36:07"``,`<br>```"created_date"``:``"2024-09-24 16:23:40"``,`<br>```"production_date"``:``"2024-09-14"`<br>```}`<br>```],`<br>```"remark"``:``""``,`<br>```"employee_name"``:``"wdtapi3-test2"``,`<br>```"rec_id"``: 17529,`<br>```"prop6"``:``""``,`<br>```"prop5"``:``""``,`<br>```"prop4"``:``""``,`<br>```"logistics_id"``: 0,`<br>```"prop3"``:``""``,`<br>```"prop2"``:``""``,`<br>```"prop1"``:``""``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"modified"``: 1727166952000,`<br>```"other_in_no"``:``"QR202409240009"``,`<br>```"note_count"``: 0,`<br>```"warehouse_id"``: 311,`<br>```"status"``: 1`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.InQuery.queryWithDetail#autoTab6_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` |

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