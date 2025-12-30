---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.invoice.InvoiceOrder.search"
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

**finance.invoice.InvoiceOrder.search** **（发票信息查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取发票信息 |
| **1.2 适用版本：** 客户端 V1.5.5.6及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** 发票编号不填写的情况下必须填写开始时间和结束时间 <br>**【权限校验】：店铺权限**<br>**为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")[，拼多多请自行对接平台获取](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")。** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** |

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
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String |  | N | 开始时间（最后更新时间） |
| 结束时间 | end\_time | String |  | N | 结束时间（最后更新时间） |
| 发票编号 | invoice\_order\_no | String | 40 | N | 发票编号 |
| 查询类型 | mode | Int |  | N | 1:按照传入的条件查询,不限制服务商类型和发票状态.<br>默认仅返回线下待开票的数据 |
| 发票状态 | status | Int |  | N | 仅mode=1 时生效，<br>5:取消;10:编辑中;20:待审核;35:导入待确认;40:待开票;45:线下待开票;50:开票中;60:开票成功;70开票申请失败;80:开票失败;85:线下开票失败;90:待上传PDF;100:上传失败;110:上传成功 |
| 服务商类型 | platform\_type | Int | 4 | N | 201 金壬 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 单据数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String,   Object>> |  | Y | 单据数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 发票编号 | invoice\_order\_no | String | 40 | Y | 发票编号，系统内部生成 |
| 发票下载地址 | file\_url | String | 255 | Y | 发票下载地址 |
| 错误信息 | error\_info | String | 100 | Y | 错误信息 |
| 电子邮箱 | payer\_email | String | 64 | Y | 电子邮箱 |
| 收款银行 | payee\_bank\_name | String | 255 | Y | 收款银行（开票方管理页面维护） |
| 收款账户 | payee\_bank\_account | String | 20 | Y | 收款账户（开票方管理页面维护） |
| 税前折扣金额 | discount | Decimal(19,4) |  | Y | 税前折扣金额 |
| 付款方联系电话 | payer\_phone | String | 40 | Y | 付款方联系电话 |
| 收款人 | payee\_receiver | String | 20 | Y | 收款人 |
| 开票金额 | invoice\_amount | Decimal(19,4) |  | Y | 实际合计金额+实际合计税额 |
| 红蓝票 | is\_red | boolean | 1 | Y | false：蓝票<br>true：红票 |
| 发票类型 | invoice\_type | Int | 4 | Y | 0纸质普通发票<br>1电子普通发票 <br>2纸质专用发票<br>3全电普通发票<br>4全电专用发票<br>5电子专用发票 |
| 付款方银行账号 | payer\_account | String | 40 | Y | 付款方银行账号 |
| 税控盘号 | tax\_control\_no | String |  | Y | 税控盘号 |
| 开票人 | payee\_operator | String | 20 | Y | 开票人 |
| 开票类型 | business\_type | Int | 4 | Y | 0：商家对于个人开具<br>1：商家对于企业开具 |
| 付款方税务登记号 | payer\_register\_no | String | 40 | y | 付款方税务登记号 |
| 开票服务商名称 | provider\_name | String | 40 | Y | 开票服务商名称 |
| 付款方地址 | payer\_address | String | 255 | Y | 付款方地址 |
| 实际开票金额 | invoice\_outer\_amount | Decimal(19,4) |  | Y | 实际开票金额 |
| 付款方银行 | payer\_bank | String | 128 | Y | 付款方银行 |
| 收款方纳税人识别号 | payee\_register\_no | String | 40 | Y | 收款方纳税人识别号 |
| 收款方地址 | payee\_address | String | 255 | Y | 收款方地址 |
| 货品合计金额 | goods\_amount | Decimal(19,4) |  | Y | 货品合计金额（未扣除折扣） |
| 货品合计税额 | goods\_tax | Decimal(19,4) |  | Y | 货品合计税额（未扣除折扣） |
| 创建时间 | created | String |  | Y | 创建时间（毫秒级时间戳，例如：1631861379000） |
| 发票打印备注 | invoice\_remark | String | 200 | Y | 发票打印备注 |
| 折扣税率 | discount\_tax | Decimal(19,4) |  | Y | 折扣税率 |
| 收款方联系电话 | payee\_telno | String | 40 | Y | 收款方联系电话 |
| 开票方备注 | payee\_remark | String | 255 | Y | 开票方备注 |
| 店铺编号 | shop\_no | String | 20 | Y | 店铺编号 |
| 店铺名称 | shop\_name | String | 128 | Y | 店铺名称 |
| 实际合计税额 | sum\_tax | Decimal(19,4) |  | Y | 货品合计税额-折扣税额 |
| 收款方公司名称 | payee\_name | String | 64 | Y | 收款方公司名称 |
| 付款方名称 | payer\_name | String | 64 | Y | 对应发票抬头，付款方名称 |
| 关联发票号码 | relation\_invoice\_no\_out | String | 40 | Y | 红字发票对应蓝票的发票号码（为null时不返回） |
| 关联发票代码 | relation\_invoice\_code | String | 40 | Y | 红字发票对应蓝票的发票代码（为null时不返回） |
| 复核人 | payee\_checker | String | 20 | Y | 复核人 |
| 发票流水号 | serial\_no | String | 50 | Y | 发票流水号 |
| 发票状态 | status | Int | 4 | Y | 5:取消;10:编辑中;20:待审核;35:导入待确认;40:待开票;45:线下待开票;50:开票中;60:开票成功;70开票申请失败;80:开票失败;85:线下开票失败;90:待上传PDF;100:上传失败;110:上传成功 |
| 实际合计金额 | sum\_price | Decimal(19,4) |  | Y | 货品合计金额-税前折扣金额 |
| 发票标记 | invoice\_mask | Int | 11 | Y | 1发送短信;2整合开票；4导入发票；8线下订单标记；16等待发票开票成功后重开，重开成功后去除；32重开的发票；64开票后原始发票信息变更；128上传发票；256重开的发票金额跟之前相同；512发送邮件； |
| 发票代码 | invoice\_code | String | 40 | Y | 发票代码 |
| 发票号码 | invoice\_no | String | 40 | Y | 发票号码 |
| 开票日期 | invoice\_time | String |  | Y | 开票日期，<br>格式: yyyy-MM-dd HH:mm:ss |
| 标记名称 | flag\_name | String |  | Y | 标记名称 |
| 订单编号 | trade\_no | String |  | Y | 旺店通系统订单编号 |
| 明细信息 | detail\_list | List<Map<String,Object>> |  | Y | 明细信息 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 发票项目名称 | item\_name | String | 40 | Y | 发票项目名称，即商品名称 |
| 发票项目编码 | item\_no | String | 40 | Y | 发票项目编码，即商品规格 |
| 行类型 | row\_type | String | 4 | Y | 0: 正常行<br>1：折扣行<br>2：被折扣行 |
| 单位名称 | unit\_name | String | 20 | Y | 单位名称<br>row\_type=1不传 |
| 商品数量 | num | Decimal(19,4) |  | Y | 商品数量<br>row\_type=1不传 |
| 税务编码 | tax\_code | String | 32 | Y | 税务编码 |
| 税率 | tax\_rate | Decimal(19,4) |  | Y | 税率 |
| 税前单价 | price | Decimal(19,4) |  | Y | 税前单价<br>row\_type=1不传 |
| 税前总价 | sum\_price | Decimal(19,4) |  | Y | 税前总价（不含折扣） |
| 税额 | tax | Decimal(19,4) |  | Y | 税额（不含折扣） |
| 总价 | sum\_amount | Decimal(19,4) |  | Y | 总价（税前总价+税额） |
| 电子发票明细备注 | remark | String | 100 | Y | 电子发票明细备注 |
| 原始单号 | tid | String | 40 | Y | 原始单号 |
| 原始子单号 | oid | String | 40 | Y | 原始子单号 |
| 订单编号 | trade\_no | String |  | Y | 订单编号 |
| 平台id | platform\_id | short |  | Y | 平台id，可参考 [平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.invoice.InvoiceOrder.search#autoTab4_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.invoice.InvoiceOrder.search#autoTab4_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.invoice.InvoiceOrder.search#autoTab4_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.invoice.InvoiceOrder.search#autoTab4_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2019-03-01 11:00:00"``,``"end_time"``:``"2019-03-01 19:26:31"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``'2019-03-01 11:00:00'``;`<br>`$parMap``->end_time =``'2019-03-01 19:26:31'``;`<br>``<br>`$pager``=``new``Pager(50, 0, true);`<br>``<br>`$data``=``$client``->pageCall(``"finance.invoice.InvoiceOrder.search"``,``$pager``,``$parMap``);`<br>`$php_json``= json_encode(``$data``,JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);`<br>`?>` |

**6.响应示例**

**6.1正常响应示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.invoice.InvoiceOrder.search#autoTab4_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58 | `"status"``: 0,`<br>`"data"``: {`<br>`"total_count"``: 1,`<br>`"order"``: [{`<br>`"invoice_order_no"``:``"FP201902120001"``,`<br>`"file_url"``:``""``,`<br>`"error_info"``:``""``,`<br>`"payer_email"``:``""``,`<br>`"detail_list"``: [{`<br>`"item_name"``:``""``,`<br>`"item_no"``:``"green"``,`<br>`"unit_name"``:``"只"``,`<br>`"num"``: 1,`<br>`"tax_code"``:``"1010101010000000000"``,`<br>`"tax_rate"``: 0.13,`<br>`"price"``: 3.53,`<br>`"sum_price"``: 3.53,`<br>`"tax"``: 0.47,`<br>`"sum_amount"``: 4,`<br>`"discount"``: 0,`<br>`"discount_tax"``: 0,`<br>`"remark"``:``""`<br>`}],`<br>`"payee_bank_name"``:``""``,`<br>`"payee_bank_account"``:``""``,`<br>`"discount"``: 0,`<br>`"payer_phone"``:``"18000000983"``,`<br>`"payee_receiver"``:``"王小二"``,`<br>`"invoice_amount"``: 4,`<br>`"is_red"``:``false``,`<br>`"payer_account"``:``""``,`<br>`"payee_operator"``:``"王小二"``,`<br>`"business_type"``: 0,`<br>`"payer_register_no"``:``""``,`<br>`"provider_name"``:``"金壬普通发票"``,`<br>`"payer_address"``:``"河北省 唐山市 古冶区 xxxxxxxxx生生世世事实上事实上事实上"``,`<br>`"shop_no"``:``"msn001"``,`<br>`"invoice_outer_amount"``: 0,`<br>`"payer_bank"``:``""``,`<br>`"payee_address"``:``"北京"``,`<br>`"goods_amount"``: 3.53,`<br>`"goods_tax"``: 0.47,`<br>`"created"``: 1549943699000,`<br>`"invoice_remark"``:``""``,`<br>`"discount_tax"``: 0,`<br>`"shop_name"``:``"莫胜男的店铺"``,`<br>`"payee_telno"``:``"15936892345"``,`<br>`"payee_remark"``:``""``,`<br>`"sum_tax"``: 0.47,`<br>`"payee_name"``:``"百望"``,`<br>`"payer_name"``:``"个人"``,`<br>`"payee_checker"``:``"王小二"``,`<br>`"serial_no"``:``""``,`<br>`"status"``: 20,`<br>`"sum_price"``: 3.53`<br>`}]`<br>`}`<br>`}` |

6.2异常响应示例

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.invoice.InvoiceOrder.search#autoTab5_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |

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