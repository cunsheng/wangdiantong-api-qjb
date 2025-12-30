---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=statistic.StockinCollect.queryCostWithDetail"
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

**statistic.StockinCollect.queryCostWithDetail（入库瞬时成本查询** **）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP入库瞬时成本信息 |
| **1.2 适****用版本：** 客户端V1.4.3.4及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** start\_time与end\_time时间跨度不能超过7天 |
| **1.5 注意事项：【权限校验】：仓库权限。**<br>未开启多仓成本情况下，仓库编号返回空字符串；开启多仓成本后仓库编号返回实际仓库的编号 |

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
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无出库单号则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间. |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 时间查询类型 | time\_type | Int | 4 | N | 1：创建时间<br>2：审核时间<br>默认创建时间 |
| 入库单号 | stockin\_no | String | 40 | N | 出库单号，多个入库单号之间英文逗号分隔 |

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
| 单据数据 | order | List<Map<String, Object>> |  | Y | 出库相关数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**Order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单号 | stockin\_no | String | 40 | Y | 入库单号 |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单主键 |
| 退换单id | src\_order\_id | Int | 11 | Y | 退换单主键 |
| 标记id | flag\_id | Int | 11 | Y | 标记主键 |
| 物流公司id | logistics\_id | Int | 11 | Y | 物流公司主键 |
| 仓库id | warehouse\_id | Int | 11 | Y | 仓库主键 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 40 | Y | 仓库名称 |
| 便签条数 | note\_count | Int | 6 | Y | 便签条数 |
| 入库类型 | src\_order\_type | Int | 4 | Y | 单据类型<br>2：调拨入库<br>4：盘点入库<br>5：生产原料入库<br>6：生产成品入库<br>8：正残转换入库<br>10：采购入库<br>12：销售退货入库<br>13：JIT退货入库<br>20：其它入库<br>22：退货预入库<br>23：调整入库<br>33：初始化入库 |
| 业务单号 | src\_order\_no | String | 40 | Y | 业务单号 |
| 状态 | status | Int | 4 | Y | 状态<br>80：已完成 |
| 制单人 | operator\_name | String | 40 | Y | 制单人 |
| 物流公司 | logistics\_name | String | 40 | Y | 物流公司 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 货品数量 | goods\_count | Int | 11 | Y | 货品数量 |
| 货品种类数 | goods\_type\_count | Int | 11 | Y | 货品种类数 |
| 备注 | remark | String | 255 | Y | 备注 |
| 制单时间 | created | String | 40 | Y | 制单时间 |
| 审核时间 | check\_time | String | 40 | Y | 审核时间 |
| 瞬时成本总额 | checked\_goods\_total\_cost | Decimal(19,4) |  | Y | 瞬时成本总额 |
| 计划成本总额 | planned\_goods\_total\_cost | Decimal(19,4) |  | Y | 计划成本总额 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 入库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 入库单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单详情id | rec\_id | Int | 11 | Y | 入库单详情id |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单id |
| 货品数量 | num | Decimal(19,4) |  | Y | 货品数量 |
| 有效期 | expire\_date | String | 40 | Y | 指定出库货品有效期 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编码 | goods\_no | String | 40 | Y | 货品编码 |
| 简称 | short\_name | String | 40 | Y | 简称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 条码 | barcode | String | 40 | Y | 条码 |
| 是否残次品 | defect | boolean | 1 | Y | true:  残次品<br>false:  正品 |
| 瞬时实际成本 | checked\_cost\_price | Decimal(19,4) |  | Y | 瞬时实际成本 |
| 总瞬时实际成本 | total\_checked\_cost\_price | Decimal(19,4) |  | Y | 总瞬时实际成本 |
| 计划成本 | planned\_cost | Decimal(19,4) |  | Y | 计划成本 |
| 总计划成本 | total\_planned\_cost | Decimal(19,4) |  | Y | 总计划成本 |
| 货位编号 | position\_no | String | 40 | Y | 货位编号 |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 生产日期 | production\_date | String | 40 | Y | 生产日期 |
| 重量 | weight | Decimal(19,4) |  | Y | 重量 |
| 总重量 | goods\_weight | Decimal(19,4) |  | Y | 总重量 |
| 单位 | unit\_name | String | 40 | Y | 单位 |
| 品牌 | brand\_name | String | 40 | Y | 品牌 |
| 单品id | spec\_id | Int | 11 | Y | 单品主键 |
| 货品id | goods\_id | Int | 11 | Y | 货品主键 |
| 基本单位id | base\_unit\_id | Int | 6 | Y | 基本单位主键 |
| 辅助单位id | unit\_id | Int | 6 | Y | 辅助单位主键 |
| 辅助数量 | num2 | Decimal(19,4) |  | Y | 辅助数量 |
| 品牌id | brand\_id | Int | 11 | Y | 品牌主键 |
| 货位id | position\_id | Int | 11 | Y | 货位主键 |
| 预期入库量 | expect\_num | Decimal(19,4) |  | Y | 预期入库量 |
| 备注 | remark | String | 255 | Y | 备注 |
| 换算系数 | unit\_ratio | Decimal(19,4) |  | Y | 换算系数 |
| 有效期天数 | validity\_days | Int | 6 | Y | 有效期天数 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | `[`<br>```{`<br>```"start_time"``:``"2022-12-23 00:00:00"``,`<br>```"end_time"``:``"2022-12-28 17:59:59"`<br>```}`<br>`]` | |
| php 请求示例 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2022-12-23 00:00:00'``;`<br>`$params``->end_time =``'2022-12-28 17:59:59'``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"statistic.StockinCollect.queryCostWithDetail"``,``$pager``,``$params``);`<br>``<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 29,`<br>```"order"``: [`<br>```{`<br>```"flag_id"``: 0,`<br>```"logistics_name"``:``"无"``,`<br>```"planned_goods_total_cost"``:``"0"``,`<br>```"stockin_id"``: 11462,`<br>```"src_order_id"``: 1105,`<br>```"logistics_no"``:``""``,`<br>```"created"``:``"2022-12-28 16:41:19"``,`<br>```"detail_list"``: [`<br>```{`<br>```"rec_id"``: 26570,`<br>```"stockin_id"``: 11462,`<br>```"spec_id"``: 4729,`<br>```"goods_id"``: 20220352,`<br>```"goods_name"``:``"中娅"``,`<br>```"short_name"``:``"金身"``,`<br>```"goods_no"``:``"ycz1"``,`<br>```"spec_code"``:``"2"``,`<br>```"spec_name"``:``"20"``,`<br>```"spec_no"``:``"ycz12"``,`<br>```"barcode"``:``"ycz12"``,`<br>```"expire_date"``:``""``,`<br>```"production_date"``:``""``,`<br>```"base_unit_id"``: 0,`<br>```"num"``: 1.0000,`<br>```"num2"``: 1.0000,`<br>```"brand_id"``: 47,`<br>```"position_id"``: -6,`<br>```"position_no"``:``"其它未上架"``,`<br>```"expect_num"``: 1.0000,`<br>```"remark"``:``""``,`<br>```"weight"``: 0.0000,`<br>```"goods_weight"``: 0.0000,`<br>```"defect"``:``false``,`<br>```"unit_ratio"``: 1.0000,`<br>```"validity_days"``: 0,`<br>```"unit_id"``: 0,`<br>```"checked_cost_price"``: 0.0000,`<br>```"total_checked_cost_price"``: 0E-8,`<br>```"planned_cost"``: 0.0000,`<br>```"total_planned_cost"``: 0E-8,`<br>```"brand_name"``:``"lol牌"``,`<br>```"unit_name"``:``"无"`<br>```}`<br>```],`<br>```"src_order_type"``: 20,`<br>```"goods_type_count"``: 2,`<br>```"remark"``:``","``,`<br>```"goods_count"``: 2.0000,`<br>```"src_order_no"``:``"QR0847"``,`<br>```"logistics_id"``: 0,`<br>```"operator_name"``:``"张彪03"``,`<br>```"warehouse_name"``:``"zb03的仓库"``,`<br>```"warehouse_no"``:``"zb03"``,`<br>```"stockin_no"``:``"RK202212280008"``,`<br>```"checked_goods_total_cost"``: 0.0000,`<br>```"modified"``:``"2022-12-28 17:02:37"``,`<br>```"note_count"``: 0,`<br>```"status"``: 80,`<br>```"warehouse_id"``: 361,`<br>```"check_time"``:``"2022-12-28 17:02:36"`<br>```}`<br>```]`<br>```}`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"您的查询时间过宽,查询时间不能大于7天"`<br>`}` | |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1