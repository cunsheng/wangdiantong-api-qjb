---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.orderSearch"
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

**setting.strategy.VirtualWarehouse.orderSearch** **（虚拟仓单据查询)**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥定制**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP虚拟仓单据信息 |
| **1.2 适用版本：** 客户端 V1.4.0.0及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：**start\_time与end\_time时间跨度不超过30天 |
| **1.5注意事项：权限校验：【虚拟仓权限】**<br>tips:有虚拟仓权限的情况下, 只要有明细中某个实体仓的权限就可以查到单据 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

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
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 是 | 最后修改时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | 是 | 最后修改时间, yyyy-MM-dd HH:mm:ss格式 |
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 否 | 虚拟仓编号 |
| 实体仓编号 | warehouse\_no | String |  | 否 | 实体仓编号 |
| 单据类型 | order\_type | Int |  | 否 | 单据类型<br>1：锁定入库<br>2：释放出库<br>3：调拨<br>4：采购入库 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

**返回值为一个Map<String, Object>**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据信息 | data | Map<String, Object> |  | 是 | 单据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 单据数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据id | order\_id | Int | 11 | 是 | 虚拟仓单据id |
| 单据编号 | order\_no | String | 40 | 是 | 单据编号 |
| 单据类型 | order\_type | Int | 6 | 是 | 1：锁定入库<br>2：释放出库<br>3：调拨<br>4：采购入库 |
| 虚拟仓仓库编号 | virtual\_warehouse\_no | String | 40 | 是 | 虚拟仓仓库编号 |
| 虚拟仓id | virtual\_warehouse\_id | Int |  | 是 | 虚拟仓id |
| 目标虚拟仓编号 | to\_virtual\_warehouse\_no | String | 40 | 是 | 目标虚拟仓仓库编号 |
| 目标虚拟仓id | to\_virtual\_id | Int |  | 是 | 目标虚拟仓id |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 预审核时间 | pre\_check\_time | String |  | 是 | 预审核时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 状态 | status | Int | 11 | 是 | 1：锁定<br>2：释放 |
| 审核时间 | check\_time | String |  | 是 | 审核时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 审核时间 | checked\_time | String |  | 是 | 审核时间毫 秒级时间戳，例如：1631861379000） |
| 单据状态 | order\_status | Int | 11 | 是 | 10：编辑中<br>20：待审核<br>25：待自动审核<br>30：已审核<br>90：已取消 |
| 货品种类 | type\_num | Decimal(19,4) |  | 是 | 货品种类 |
| 总金额 | total\_amount | Decimal(19,4) |  | 是 | 总金额 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 实体仓 | warehouse\_names | String |  | 是 | 实体仓名称，多个实体仓使用英文逗号分隔 |
| 实体仓id | warehouse\_id\_str | String |  | 是 | 实体仓id，多个实体仓使用英文逗号分隔 |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 创建时间 | created | String |  | 是 | 创建时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 明细信息 | detail\_list | List<Map<String, Object>> |  | 是 | 明细数据 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细唯一id | rec\_id | Int | 11 | 是 | 明细唯一id |
| 虚拟仓单据id | order\_id | Int | 11 | 是 | 虚拟仓单据id |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 规格编码 | spec\_code | String | 40 | 是 | 规格编码 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 实体仓id | warehouse\_id | Int | 11 | 是 | 实体仓id |
| 实体仓编号 | warehouse\_no | String | 40 | 是 | 实体仓编号 |
| 实体仓 | warehouse\_name | String | 64 | 是 | 实体仓名称 |
| 入库数量 | num | Decimal(19,4) |  | 是 | 入库数量 |
| 预期数量 | expected\_num | Decimal(19,4) |  | 是 | 预期数量 |
| 实际数量 | final\_num | Decimal(19,4) |  | 是 | 实际数量 |
| 成本价 | price | Decimal(19,4) |  | 是 | 成本价 |
| 采购在途量 | purchase\_num | Decimal(19,4) |  | 是 | 采购在途量 |
| 工厂库存 | factory\_num | Decimal(19,4) |  | 是 | 工厂库存 |
| 创建时间 | created | String |  | 是 | 创建时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间<br>yyyy-MM-dd HH:mm:ss格式 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.orderSearch#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.orderSearch#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.orderSearch#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.orderSearch#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | `[`<br>```{`<br>```"start_time"``:``"2022-06-22 17:07:11"``,`<br>```"end_time"``:``"2022-06-25 17:07:11"``,`<br>```"virtual_warehouse_no"``:``"sss02"``,`<br>```"warehouse_no"``:``"0423"``,`<br>```"order_type"``: 1`<br>```}`<br>`]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``'2020-12-15 13:18:30'``;`<br>`$parMap``->end_time =``'2021-01-10 13:18:59'``;`<br>`$pager``=``new``Pager(2, 0, true);`<br>`$data``=``$client``->pageCall(``"setting.strategy.VirtualWarehouse.orderSearch"``,``$pager``,``$parMap``);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.orderSearch#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [`<br>```{`<br>```"order_no"``:``"VO202206240001"``,`<br>```"created"``:``"2022-06-24 17:07:10"``,`<br>```"detail_list"``: [`<br>```{`<br>```"rec_id"``: 1058,`<br>```"order_id"``: 743,`<br>```"spec_no"``:``"sj-xin"``,`<br>```"spec_code"``:``"sj-xin"``,`<br>```"goods_no"``:``"sj-xin"``,`<br>```"goods_name"``:``"sj-xin"``,`<br>```"warehouse_id"``: 11,`<br>```"num"``: 4.0000,`<br>```"final_num"``: 0.0000,`<br>```"price"``: 9.8000,`<br>```"purchase_num"``: 0.0000,`<br>```"factory_num"``: 0.0000,`<br>```"created"``:``"2022-06-24 17:07:11"``,`<br>```"modified"``:``"2022-06-24 17:07:11"``,`<br>```"warehouse_no"``:``"0423"``,`<br>```"warehouse_name"``:``"盛洁的仓库"`<br>```},`<br>```{`<br>```"rec_id"``: 1057,`<br>```"order_id"``: 743,`<br>```"spec_no"``:``"lzxxnc1"``,`<br>```"spec_code"``:``"lzxxnc1"``,`<br>```"goods_no"``:``"lzxxnc"``,`<br>```"goods_name"``:``"刘子渲虚拟仓货品"``,`<br>```"warehouse_id"``: 6,`<br>```"num"``: 3.0000,`<br>```"final_num"``: 0.0000,`<br>```"price"``: 1.2000,`<br>```"purchase_num"``: 0.0000,`<br>```"factory_num"``: 0.0000,`<br>```"created"``:``"2022-06-24 17:07:11"``,`<br>```"modified"``:``"2022-06-24 17:07:11"``,`<br>```"warehouse_no"``:``"lzx"``,`<br>```"warehouse_name"``:``"刘子渲超级大仓"`<br>```}`<br>```],`<br>```"num"``: 7.0000,`<br>```"remark"``:``"remark"``,`<br>```"to_virtual_id"``: 0,`<br>```"pre_check_time"``:``""``,`<br>```"order_status"``: 20,`<br>```"type_num"``: 2,`<br>```"total_amount"``: 42.8000,`<br>```"modified"``:``"2022-06-24 17:07:11"``,`<br>```"virtual_warehouse_id"``: 3,`<br>```"order_id"``: 743,`<br>```"order_type"``: 1,`<br>```"status"``: 1,`<br>```"check_time"``:``""``,`<br>```"warehouse_names"``:``"刘子渲超级大仓,盛洁的仓库"`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.orderSearch#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"虚拟仓不存在或已停用:sss02x"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1