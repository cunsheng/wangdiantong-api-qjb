---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.AlipayAccountCheck.search"
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

**finance.AlipayAccountCheck.search** **（平台对账单查询）**

### **¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内平台对账单信息 |
| **1.2 适用版本：** 客户端V1.2.6.9及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：店铺权限**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台数据，相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")，拼多多请自行对接平台获取。 |

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
| 开始时间 | start\_time | String | 40 | 是 | 开始时间 |
| 结束时间 | end\_time | String | 40 | 是 | 结束时间 |
| 时间条件类型 | time\_type | Byte |  | 否 | 1：最后修改时间<br>2：发货时间<br>3：对账时间<br>4：确认收货时间<br>默认1 |
| 平台id | platform\_id | Short |  | 是 | 平台id，映射表点击 [详情](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看 |
| 对账单状态 | status | Byte |  | 否 | 0：未确认<br>1：部分对账<br>2：对账失败<br>3：对账成功<br>4：设置对账成功 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 单据信息 | data | Map<String, Object> |  | N | 单据信息 |

****data****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细信息 | order | List<Map<String, Object>> |  | Y | 明细信息 |
| 总数 | total\_count | Int | 11 | N | 查询单据总条数 |

****order****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 对账单唯一id | rec\_id | Int | 11 | 是 | 对账单唯一id |
| 对账单号 | account\_check\_no | String | 40 | 是 | 对账单号 |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 平台id | platform\_id | Short | 6 | 是 | 平台id，映射表点击 [详情](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看 |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 店铺名称 | shop\_name | String | 128 | 是 | 店铺名称 |
| 店铺id | shop\_id | short | 6 | 是 | 店铺id |
| 对账状态 | status | Byte | 4 | 是 | 对账状态<br>0：未确认<br>1：部分对账<br>2：对账失败<br>3：对账成功<br>4：设置对账成功 |
| 发货金额 | send\_amount | Decimal(19,4) |  | 是 | 发货金额 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 退款金额 |
| 应收金额 | receivable | Decimal(19,4) |  | 是 | 应收金额 |
| 已收金额 | received | Decimal(19,4) |  | 是 | 已收金额 |
| 收支金额 | pay\_amount | Decimal(19,4) |  | 是 | 收支金额 |
| 其他费用 | cost\_amount | Decimal(19,4) |  | 是 | 其他费用 |
| 发货数量 | send\_num | Decimal(19,4) |  | 是 | 发货数量 |
| 退款数量 | refund\_num | Decimal(19,4) |  | 是 | 退款数量 |
| 账单数量 | payment\_num | Decimal(19,4) |  | 是 | 账单数量 |
| 对账比例 | check\_ratio | Decimal(19,4) |  | 是 | 对账比例 |
| 发货时间 | consign\_time | String |  | 是 | 发货时间 |
| 确认收货时间 | confirm\_time | String |  | 是 | 确认收货时间 |
| 对账时间 | check\_time | String |  | 是 | 对账时间 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.AlipayAccountCheck.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.AlipayAccountCheck.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.AlipayAccountCheck.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.AlipayAccountCheck.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2020-11-09 14:04:17"``,``"end_time"``:``"2020-12-05 01:58:22"``,``"platform_id"``:125}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client = new WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap = new stdClass();`<br>`$parMap->start_time =``'2020-11-09 14:04:17'``;`<br>`$parMap->end_time =``'2020-12-05 01:58:22'``;`<br>`$parMap->platform_id = 125;`<br>``<br>`$pager = new Pager(2, 0,``true``);`<br>``<br>`try {`<br>```$data = $client->pageCall(``"finance.AlipayAccountCheck.search"``, $pager, $parMap);`<br>`}catch(WdtErpException $e)`<br>`{`<br>```echo $e->getMessage();`<br>`}`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.AlipayAccountCheck.search#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58 | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"total_count"``: 224,`<br>`"order"``: [`<br>`{`<br>`"consign_time"``:``""``,`<br>`"created"``:``"2020-12-03 01:58:22"``,`<br>`"pay_amount"``: 0.0000,`<br>`"received"``: 0.0000,`<br>`"receivable"``: 0.0000,`<br>`"rec_id"``: 2286,`<br>`"shop_name"``:``"系统分销店铺2ddd6ea0"``,`<br>`"tid"``:``"26bb8645-CK2020y33"``,`<br>`"confirm_time"``:``""``,`<br>`"send_num"``: 6.0000,`<br>`"shop_id"``: 145,`<br>`"send_amount"``: 1.0000,`<br>`"check_ratio"``: 0.0000,`<br>`"cost_amount"``: 0.0000,`<br>`"refund_num"``: 0.0000,`<br>`"platform_id"``: 125,`<br>`"refund_amount"``: 0.0000,`<br>`"payment_num"``: 0.0000,`<br>`"modified"``:``"2020-12-03 01:58:22"``,`<br>`"account_check_no"``:``"AC202012030002"``,`<br>`"status"``: 0,`<br>`"check_time"``:``""``,`<br>`"shop_no"``:``"2ddd6ea0"`<br>`},`<br>`{`<br>`"consign_time"``:``"2020-10-14 15:16:03"``,`<br>`"created"``:``"2020-10-14 17:05:48"``,`<br>`"pay_amount"``: 0.0000,`<br>`"received"``: 0.0000,`<br>`"receivable"``: 0.0000,`<br>`"rec_id"``: 1919,`<br>`"shop_name"``:``"系统分销店铺2ddd6ea0"``,`<br>`"tid"``:``"67007c08-CK2020101429-1"``,`<br>`"confirm_time"``:``""``,`<br>`"send_num"``: 1.0000,`<br>`"shop_id"``: 145,`<br>`"send_amount"``: 8.5700,`<br>`"check_ratio"``: 0.0000,`<br>`"cost_amount"``: 0.0000,`<br>`"refund_num"``: 0.0000,`<br>`"platform_id"``: 125,`<br>`"refund_amount"``: 0.0000,`<br>`"payment_num"``: 0.0000,`<br>`"modified"``:``"2020-11-25 17:55:41"``,`<br>`"account_check_no"``:``"AC202010140008"``,`<br>`"status"``: 0,`<br>`"check_time"``:``""``,`<br>`"shop_no"``:``"2ddd6ea0"`<br>`}`<br>`]`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.AlipayAccountCheck.search#autoTab1_0)

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

3.3 业务请求参数

4.响应参数

4.响应参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1