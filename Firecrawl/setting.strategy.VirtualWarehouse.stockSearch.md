---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch"
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

**setting.strategy.VirtualWarehouse.stockSearch** **（虚拟仓库存查询)**

**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP虚拟仓库存信息 |
| **1.2 适用版本：** 客户端 V1.5.6.2及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：**start\_time与end\_time时间跨度不超过30天 |
| **1.5注意事项：权限校验：【仓库和虚拟仓权限】** |

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
| 开始时间 | start\_time | String | 40 | 否 | 修改时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | 否 | yyyy-MM-dd HH:mm:ss格式 |
| 商家编码 | spec\_nos | String |  | 否 | 英文逗号分割,最多500个; 不填时间条件时必填 |
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 否 | 虚拟仓编号 |
| 实体仓编号 | warehouse\_no | String |  | 否 | 实体仓编号 |

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
| 数据 | detail\_list | List<Map<String, Object>> |  | 是 | 明细数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 最小警戒库存 | alarm\_num | Decimal(19,4) |  | 是 | 最小警戒库存 |
| 已分配数 | assigned\_num | Decimal(19,4) |  | 是 | 已分配数 |
| 公有仓可用数 | avaliable\_num | Decimal(19,4) |  | 是 | 公有仓可用数 |
| 可发数 | can\_use\_lock\_num | Decimal(19,4) |  | 是 | 可发数 |
| 可用数 | can\_use\_num | Decimal(19,4) |  | 是 | 可用数 |
| 自定义数量 | factory\_num | Decimal(19,4) |  | 是 | 自定义数量 |
| 虚拟仓警戒库存 | lock\_num | Decimal(19,4) |  | 是 | 虚拟仓警戒库存 |
| 货品名称 | goods\_name | String |  | 是 | 货品名称 |
| 货品编号 | goods\_no | String |  | 是 | 货品编号 |
| 当前锁定数（入库数量） | now\_lock\_num | Decimal(19,4) |  | 是 | 当前锁定数（入库数量） |
| 14天销量 | num\_14days | Decimal(19,4) |  | 是 | 14天销量 |
| 7天销量 | num\_7days | Decimal(19,4) |  | 是 | 7天销量 |
| 今日销量 | num\_day | Decimal(19,4) |  | 是 | 今日销量 |
| 月销量 | num\_month | Decimal(19,4) |  | 是 | 月销量 |
| 昨日销量 | num\_yesterday | Decimal(19,4) |  | 是 | 昨日销量 |
| 已出库数 | out\_num | Decimal(19,4) |  | 是 | 已出库数 |
| 总锁定数 | sum\_lock\_num | Decimal(19,4) |  | 是 | 总锁定数 |
| 明细id | rec\_id | Int |  | 是 | 唯一键 |
| 商家编码 | spec\_no | String |  | 是 | 商家编码 |
| 规格名称 | spec\_name | String |  | 是 | 规格名称 |
| 虚拟仓名称 | vir\_warehouse\_name | String |  | 是 | 虚拟仓名称 |
| 虚拟仓编号 | vir\_warehouse\_no | String |  | 是 | 虚拟仓编号 |
| 仓库名称 | warehouse\_name | String |  | 是 | 仓库名称 |
| 仓库编号 | warehouse\_no | String |  | 是 | 仓库编号 |
| 仓库id | warehouse\_id | Int |  | 是 | 仓库id |
| 采购在途量 | purchase\_num | String |  | 是 | 采购在途量<br>（开启客户端系统配置：开启虚拟仓锁定预售库存功能，返回对应值，未开通下返回0） |
| 单品id | spec\_id | int |  | 是 | 单品id（系统单品主键） |
| 虚拟仓id | vir\_warehouse\_id | int |  | 是 | 虚拟仓id |
| 预计其他入库锁定量 | trial\_other\_in\_num | Decimal(19,4) |  | 是 | 预计其他入库锁定量 |
| 成本价 | avg\_cost |  |  | 是 | 成本价 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | `[{`<br>```"start_time"``:``"2022-03-09 15:50:01"``,`<br>```"end_time"``:``"2022-03-09 15:50:58"``,`<br>```"spec_nos"``:``"4204"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$paraMap``=``new``stdClass();`<br>`$paraMap``->start_time =``"2022-03-09 15:50:01"``;`<br>`$paraMap``->end_time =``"2022-03-09 15:50:58"``;`<br>`$paraMap``->spec_nos =``"4204"``;`<br>`$pager``=``new``Pager(2, 0, true);`<br>`$data``=``$client``->pageCall(``"setting.strategy.VirtualWarehouse.stockSearch"``,``$pager``,``$paraMap``);`<br>`>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 2,`<br>```"detail_list"``: [{`<br>```"alarm_num"``: 0.0000,`<br>```"trial_other_in_num"``: 0.0000,`<br>```"goods_no"``:``"4204"``,`<br>```"spec_no"``:``"4204"``,`<br>```"purchase_num"``: 0.0000,`<br>```"avaliable_num"``: 1155.0000,`<br>```"spec_id"``: 1992,`<br>```"vir_warehouse_name"``:``"daj虚拟仓"``,`<br>```"num_14days"``: 0.0000,`<br>```"out_num"``: 0.0000,`<br>```"goods_name"``:``"高筱原的水杯"``,`<br>```"lock_num"``: 10.0000,`<br>```"now_lock_num"``: 10.0000,`<br>```"num_day"``: 0.0000,`<br>```"rec_id"``: 700,`<br>```"num_month"``: 0.0000,`<br>```"can_use_lock_num"``: 10.0000,`<br>```"vir_warehouse_id"``: 5,`<br>```"can_use_num"``: 10.0000,`<br>```"factory_num"``: 0.0000,`<br>```"sum_lock_num"``: 10.0000,`<br>```"num_yesterday"``: 0.0000,`<br>```"spec_name"``:``""``,`<br>```"assigned_num"``: 0.0000,`<br>```"warehouse_id"``: 330,`<br>```"num_7days"``: 0.0000`<br>```},`<br>```{`<br>```"alarm_num"``: 0.0000,`<br>```"goods_no"``:``"4204"``,`<br>```"spec_no"``:``"4204"``,`<br>```"purchase_num"``: 0.0000,`<br>```"avaliable_num"``: 1155.0000,`<br>```"spec_id"``: 1992,`<br>```"vir_warehouse_name"``:``"gyy001"``,`<br>```"num_14days"``: 0.0000,`<br>```"out_num"``: 0.0000,`<br>```"goods_name"``:``"高筱原的水杯"``,`<br>```"lock_num"``: 21.0000,`<br>```"now_lock_num"``: 5.0000,`<br>```"num_day"``: 0.0000,`<br>```"rec_id"``: 399,`<br>```"num_month"``: 0.0000,`<br>```"can_use_lock_num"``: 5.0000,`<br>```"vir_warehouse_id"``: 10,`<br>```"can_use_num"``: 5.0000,`<br>```"factory_num"``: 0.0000,`<br>```"sum_lock_num"``: 5.0000,`<br>```"num_yesterday"``: 0.0000,`<br>```"spec_name"``:``""``,`<br>```"assigned_num"``: 0.0000,`<br>```"warehouse_id"``: 330,`<br>```"num_7days"``: 0.0000`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab1_0)

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