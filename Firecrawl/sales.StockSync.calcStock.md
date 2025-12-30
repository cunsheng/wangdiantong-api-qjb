---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.calcStock"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

订单类

销售出库单查询

物流同步状态回传

原始单推送

订单查询

待同步列表查询

重量回传

重量回传2

发票信息查询

发票信息更新

平台账单查询

平台账单推送

取消当前同步

库存同步失败

库存同步成功

获取自有平台货品需要同步信息

历史销售出库单查询

历史订单查询

平台对账单查询

原始单查询

被合并订单查询

收付款单查询

重量回传3

库存同步计算查询

重量回传4

订单客服备注修改

物流单查询

历史原始单查询

JIT退货单查询

原始单推送2

销售出库实际出库明细查询

销售收付单查询

已完成订单推送

已取消出库单查询

订单日志查询

订单标签查询

订单转异常订单

库存同步计算查询（批量）

订单查询（仅返回自有平台、线下平台订单信息）

历史原始单查询（仅返回自有平台、线下平台订单）

历史订单查询（仅返回自有平台、线下平台订单）

原始单查询（仅返回自有平台、线下平台订单）

当前位置： API文档 > 订单类

### **sales.StockSync.calcStock（库存同步计算查询）**

### **¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**计算自有平台货品应该同步的库存 |
| **1.2 适用版本：** 客户端V1.3.3.1以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：** 原sales.StockSync.calcStockWithAuth替代接口（仅支持自有平台推送）如需批量查询请用下面接口： [库存同步计算查询(支持批量查询)](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.batchCalcStock "库存同步计算查询(支持批量查询)") |

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
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台货品的rec\_id | apiGoodsId | long |  | 是 | 平台货品的rec\_id |
| 货品是否开启检测 | forceSync | Boolean |  | 是 | True开启；False未开启，（主要用于被停用平台货品或临时停止库存同步时强制同步库存，无该逻辑传false即可） |

**4.响应参数**

响应参数为一个Map<String, Object>

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 数据信息 | data | Map<String, Object> |  | N | 数据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 编码 | match\_code | String | 40 | 是 | 如果是根据商家编码自动匹配的，那么这个字段记录了商家编码，可以是货品的编码+规格的编码 |
| 定时上架时间 | list\_time | String | 40 | 是 | 定时上架时间 |
| 最小同步库存量 | stock\_syn\_min | Decimal(19,4) |  | 是 | 最小同步库存量 |
| 平台库存 | stock\_num | Decimal(19,4) |  | 是 | 平台库存 |
| 库存同步的仓库id | stock\_syn\_warehouses | String | 1024 | 是 | 库存同步的仓库id，多个仓库则用,分隔 |
| 子平台ID | sub\_platform\_id | Int | 4 | 是 | 子平台ID,子平台只是业务流程上有差别，订单、货品应该是同一管理方式 |
| 平台货品编码 | outer\_id | String | 40 | 是 | 平台货品编码 |
| 平台规格编码 | spec\_outer\_id | String | 40 | 是 | 平台规格编码 |
| 同步百分比 | stock\_syn\_percent | Int | 11 | 是 | 同步百分比 |
| 平台规格id | spec\_id | String | 40 | 是 | 平台规格id |
| 是否自动下架 | is\_auto\_delisting | Boolean | 1 | 是 | 是否自动下架 |
| 增加值 | stock\_syn\_plus | Decimal(19,4) |  | 是 | 增加值 |
| 是否自动上架 | is\_auto\_listing | Boolean | 1 | 是 | 是否自动上架 |
| 系统货品的ID | match\_target\_id | Int | 11 | 是 | 系统货品的ID，如果match\_target\_type=1，这值是goods\_spec的主键，如果match\_target\_id=2，这值是goods\_suite的主键 |
| target\_id的类型 | match\_target\_type | Int | 11 | 是 | target\_id的类型 <br>0未绑定 <br>1规格 <br>2组合装 |
| 掩码 | mask | Int | 11 | 是 | 掩码,1临时延时 |
| 需要同步库存的量 | syn\_stock | Int | 11 | 是 | 需要进行同步库存的量 |
| 保留 | reserve\_s | String | 50 | 是 | 保留 |
| 同步规则策略id | stock\_syn\_rule\_id | Int | 11 | 是 | 同步规则策略id |
| 库存计算方法的掩码 | stock\_syn\_mask | Int | 11 | 是 | 库存计算方法的掩码 |
| 平台货品id | goods\_id | String | 40 | 是 | 平台货品号 |
| Api\_goodsspec表的主键id | rec\_id | Int | 20 | 是 | Api\_goodsspec表的主键id |
| 最后同步库存量 | last\_syn\_num | Decimal(19,4) |  | 是 | 最后同步库存量 |
| 店铺ID | shop\_id | Int | 6 | 是 | 店铺id |
| 最大同步 | stock\_syn\_max | Decimal(19,4) |  | 是 | 最大同步 |
| 最后同步时间 | last\_syn\_time | String | 40 | 是 | 最后同步时间 |
| 定时下架时间 | delist\_time | String | 40 | 是 | 定时下架时间 |
| 平台id | platform\_id | Int | 4 | 是 | 因为是自有平台，所以固定是127 |
| 同步规则策略编号 | stock\_syn\_rule\_no | String | 40 | 是 | 在此映射记录上起作用的同步规则策略编号 |
| 平台货品状态 | status | Int | 4 | 是 | 0删除 1在架 2下架 |
| 库存变化量 | stock\_change\_count | Int | 11 | 是 | 库存变化时自增 |

**5** **.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.calcStock#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.calcStock#autoTab0_1)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[`<br>`2447,`<br>`false`<br>`]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$data``=``$client``->call(``"sales.StockSync.calcStock"``, 2447, false);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.calcStock#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36 | `{`<br>`"status"``:0,`<br>`"data"``:{`<br>`"match_code"``:``"lz38"``,`<br>`"list_time"``:``""``,`<br>`"stock_syn_min"``:1.0000,`<br>`"stock_num"``:0,`<br>`"stock_syn_warehouses"``:``"6"``,`<br>`"sub_platform_id"``:0,`<br>`"outer_id"``:``"lz3"``,`<br>`"spec_outer_id"``:``"lz38"``,`<br>`"stock_syn_percent"``:100,`<br>`"spec_id"``:``"lz38"``,`<br>`"is_auto_delisting"``:1,`<br>`"stock_syn_plus"``:1.0000,`<br>`"is_auto_listing"``:1,`<br>`"match_target_id"``:12581,`<br>`"match_target_type"``:1,`<br>`"mask"``:0,`<br>`"syn_stock"``:1,`<br>`"reserve_s"``:``""``,`<br>`"stock_syn_rule_id"``:-10000,`<br>`"stock_syn_mask"``:0,`<br>`"goods_id"``:``"lz3"``,`<br>`"rec_id"``:2447,`<br>`"last_syn_num"``:-1,`<br>`"shop_id"``:69,`<br>`"stock_syn_max"``:550.0000,`<br>`"last_syn_time"``:``""``,`<br>`"delist_time"``:``""``,`<br>`"platform_id"``:127,`<br>`"stock_syn_rule_no"``:``""``,`<br>`"status"``:1,`<br>`"stock_change_count"``:2`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.calcStock#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``:100,`<br>`"message"``:``"货品id:jitx002规格Id:jitx002 已停用或者未开启同步"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1