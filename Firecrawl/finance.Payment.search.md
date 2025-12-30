---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.Payment.search"
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

### **finance.Payment.search（收付款单查询）**

### **¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内收付款单信息 |
| **1.2 适用版本：** 客户端V1.3.7.7及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：起止时间跨度不超过30天** |
| **1.5注意事项：权限校验：【店铺权限】**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")[，拼多多请自行对接平台获取](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")。 |

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
| 开始时间 | start\_time | String | 40 | 是 | 开始时间，yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | 是 | 结束时间，上同开始时间 |
| 时间类型 | time\_type | Int |  | 否 | 1: 创建时间 <br>2: 最后修改时间 <br>默认1 |
| 收付单类型 | type | byte |  | 否 | 1: 收款<br>2: 付款 <br>3: 其它收款 <br>4: 其他付款 |
| 收付单状态 | status | byte |  | 否 | 10: 编辑中 <br>20: 待审核 <br>30: 已审核 <br>40: 已取消 |

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

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | Y | 查询单据总条数 |
| 单据信息 | order | List<Map<String, Object>> |  | Y | 单据信息 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 收付单唯一id | rec\_id | Int |  | 是 | 收付单唯一id |
| 收付单号 | payment\_no | String |  | 是 | 收付单号 |
| 状态 | status | byte |  | 是 | 10: 编辑中 <br>20: 待审核 <br>30: 已审核 <br>40: 已取消 |
| 往来对象编号 | object\_no | String |  | 是 | 往来对象编号 |
| 往来名称 | object\_name | String |  | 是 | 往来名称 |
| 支付单号 | pay\_no | String |  | 是 | 支付单号 |
| 账号 | account\_no | String |  | 是 | 账号 |
| 类型 | type | byte |  | 是 | 1: 收款<br>2: 付款 <br>3: 其它收款 <br>4: 其他付款 |
| 备注 | remark | String |  | 是 | 备注 |
| 业务员 | teller\_name | String |  | 是 | 业务员 |
| 金额 | amount | Decimal(19,4) |  | 是 | 金额 |
| 收支项目 | receipt\_name | String |  | 是 | 收支项目 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间 |
| 审核时间 | check\_time | String |  | 是 | 审核时间 |
| 使用预收付款金额 | use\_amount | Decimal(19,4) |  | 是 | 使用预收付款金额 |
| 明细列表 | detail\_list | List<Map<String, Object>> |  | 是 | 明细列表 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务类型 | src\_order\_type | Int |  | 是 | 1: 销售订单<br>4: 盘点单<br>5: 生产单<br>10: 采购单<br>12: 销售退货<br>14: 采购退货<br>20: 其它入库<br>21: 其它出库<br>23: 入库调整单<br>24: 出库调整单 |
| 收付单唯一id | payment\_order\_id | int |  | 是 | 对应主节点的收付单唯一ID（rec\_id）字段 |
| 明细主键ID | rec\_id | int |  | 是 | 收款单明细行唯一主键ID |
| 业务单号 | src\_order\_no | String |  | 是 | 业务单号 |
| 费用类型 | fee\_type | byte |  | 是 | 1:货款 <br>2:运费 <br>3:税款 <br>4:材料成本差异 <br>5:其他费用 |
| 金额 | amount | Decimal(19,4) |  | 是 | 金额 |
| 店铺ID | shop\_id | int |  | 是 | 店铺主键ID |
| 店铺名称 | shop\_name | String |  | 是 | 店铺名称，非销售订单下返回空字符串 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.Payment.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.Payment.search#autoTab0_1)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2021-03-08 11:00:00"``,``"end_time"``:``"2021-04-07 11:26:31"``,``"time_type"``:2}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19 | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>``<br>`$parMap``->start_time =``'2021-03-08 11:00:00'``;`<br>`$parMap``->end_time =``'2021-04-07 11:26:31'``;`<br>`$parMap``->time_type = 2;`<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>``<br>`try``{`<br>```$data``=``$client``->pageCall(``"finance.Payment.search"``,``$pager``,``$parMap``);`<br>`}``catch``(WdtErpException``$e``)`<br>`{`<br>```echo``$e``->getMessage();`<br>`}`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.Payment.search#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68 | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"total_count"``: 149,`<br>`"order"``: [`<br>`{`<br>`"receipt_name"``:``"销售订单"``,`<br>`"amount"``: 60.0000,`<br>`"created"``:``"2021-03-05 11:34:08"``,`<br>`"detail_list"``: [`<br>`{`<br>`"payment_order_id"``: 3965,`<br>`"src_order_t ype"``: 1,`<br>`"src_order_no"``:``"AT202101110002-2"``,`<br>`"fee_type"``: 0,`<br>`"amount"``: 60.0000,`<br>`"operate_type"``: 0`<br>`}`<br>`],`<br>`"teller_name"``:``"杨国钢"``,`<br>`"receipt_id"``: 4,`<br>`"remark"``:``"销售收付单结算：SF202103050003"``,`<br>`"rec_id"``: 3965,`<br>`"type"``: 1,`<br>`"account_no"``:``"支付宝-zfb"``,`<br>`"account_id"``: 2,`<br>`"teller_id"``: 85,`<br>`"pay_no"``:``""``,`<br>`"object_no"``:``"WL202002270004"``,`<br>`"object_name"``:``"杨国钢"``,`<br>`"payment_no"``:``"SFK202103050003"``,`<br>`"modified"``:``"2021-03-08 1 3:43:02"``,`<br>`"status"``: 30,`<br>`"use_amount"``: 0.0000`<br>`},`<br>`{`<br>`"receipt_name"``:``"销售订单"``,`<br>`"amount"``: 1.0000,`<br>`"created"``:``"2021-03-08 14:48:17"``,`<br>`"detail_list"``: [`<br>`{`<br>`"payment_order_id"``: 3966,`<br>`"src_order_type"``: 1,`<br>`"src_ord er_no"``:``"AT202103080001"``,`<br>`"fee_type"``: 0,`<br>`"amount"``: 1.0000,`<br>`"operate_type"``: 0`<br>`}`<br>`],`<br>`"teller_name"``:``"lsy"``,`<br>`"receipt_id"``: 4,`<br>`"remark"``:``"销售收付单结算：SF202103080010"``,`<br>`"rec_id"``: 3966,`<br>`"type"``: 1,`<br>`"account_no"``:``"招行-LCJTEST"``,`<br>`"account_id"``: 13,`<br>`"teller_id"``: 91,`<br>`"pay_no"``:``""``,`<br>`"object_no"``:``"WL201909260001"``,`<br>`"object_name"``:``""``,`<br>`"payment_no"``:``"SFK202103080001"``,`<br>`"modified"``:``"2021-03-08 14:48:18"``,`<br>`"status"``: 30,`<br>`"us e_amount"``: 0.0000`<br>`}`<br>`]`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.Payment.search#autoTab1_0)

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

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1