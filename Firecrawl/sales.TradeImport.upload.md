---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeImport.upload"
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

**sales.TradeImport.upload** **（已完成订单推送）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送已完成订单给ERP |
| **1.2 适用版本：** 客户端 V1.4.7.3及以上版本 |
| **1.5注意事项：** **【权限校验】：店铺权限、仓库权限**<br>- 一次最多传入200条数据<br>  <br>- 数据不支持更新，需要保证请求参数正确<br>  <br>- 推送的单据状态在客户端-销售-订单导入界面为待转已完成状态 |

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
| 秒级时间戳 | timestamp | int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |

**3.3 业务请求参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单列表 | trade\_list | List<Map<String, Object>> |  | Y | 订单列表 |

**trade\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单编号 | trade\_no | String | 40 | Y | 订单编号 |
| 原始单号 | src\_tids | String | 255 | N | 原始单号 |
| 原始子单号 | src\_oid | String | 40 | N | 原始子单号 |
| 订单类别 | trade\_type | Byte |  | N | 订单类别<br>1：网店销售<br>2：线下订单<br>3：售后换货<br>4：批发业务<br>7：现款销售 |
| 订单来源 | trade\_from | Byte |  | N | 订单来源<br>1：API抓单<br>2：手工建单<br>3：导入<br>5：接口推送<br>6：补发订单<br>7：PDA选货开单 |
| 应收金额 | receivable | Decimal(19,4) |  | Y | 应收金额 |
| 店铺名称 | shop\_name | String | 128 | Y | 店铺名称 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称 |
| 物流公司名称 | logistics\_name | String | 40 | Y | 系统内自定义的物流公司名称 |
| 邮费 | post\_amount | Decimal(19,4) |  | N | 邮费 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 商家编码 | merchant\_no | String | 40 | Y | 商家编码 |
| 货品数量 | num | Decimal(19,4) |  | Y | 货品数量 |
| 货品价格 | order\_price | Decimal(19,4) |  | Y | 货品价格 |
| 业务员 | salesman | String | 50 | N | 业务员 |
| 审单员 | checker | String | 50 | N | 审单员 |
| 发票类型 | invoice\_type | Byte |  | N | 发票类型<br>0：不需要发票<br>1：普通发票<br>2：增值税发票 |
| 发票抬头 | invoice\_title | String | 255 | N | 发票抬头 |
| 发票内容 | invoice\_contect | String | 255 | N | 发票内容 |
| 客户网名 | buyer\_nick | String | 100 | N | 客户网名 |
| 收件人 | receiver\_name | String | 100 | Y | 收件人 |
| 省份 | province | String |  | N | 省份 |
| 城市 | city | String |  | N | 城市 |
| 区县 | district | String |  | N | 区县 |
| 大头笔 | receiver\_dtb | String | 128 | N | 大头笔 |
| 地址 | receiver\_address | String | 256 | Y | 地址 |
| 邮编 | receiver\_zip | String | 20 | N | 邮编 |
| 电话 | receiver\_mobile | String | 40 | Y | 电话 |
| 买家留言 | buyer\_message | String | 1024 | N | 买家留言 |
| 客服备注 | cs\_remark | String | 1024 | N | 客服备注 |
| 下单时间 | trade\_time | String |  | N | 下单时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 付款时间 | pay\_time | String |  | N | 付款时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 审单时间 | check\_time | String |  | N | 审单时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 打单时间 | print\_time | String |  | N | 打单时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 扫描时间 | scan\_time | String |  | N | 扫描时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 发货时间 | consign\_time | String |  | N | 发货时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 赠品方式 | gift\_type | Byte |  | N | 赠品方式<br>0：非赠品<br>1：自动赠送<br>2：手动赠送<br>3：回购自动赠送 |
| 货品优惠 | goods\_discount | Decimal(19,4) |  | N | 货品优惠 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码为0，表示调用成功 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | Y | 结果信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回信息 | message | String |  | Y | 固定返回ok,该值不可以作为请求是否成功的标志 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | ```<br>[<br>    [<br>        {<br>            "logistics_name": "自有",<br>            "logistics_no": "JYA2023071200005",<br>            "merchant_no": 4205,<br>            "num": 4,<br>            "receivable": 12.5,<br>            "receiver_address": "北京 北京市 西城区 西直门北大街凯德茂T1",<br>            "receiver_mobile": "13512340987",<br>            "shop_name": "东升的tb店铺",<br>            "trade_no": "JYA2023071200005",<br>            "trade_time": "2023-07-12 00:01:02",<br>            "warehouse_name": "高筱原的仓库1"<br>        }<br>    ]<br>]<br>``` |
| PHP | ```<br><?php  <br>header("Content-Type: text/html; charset=UTF-8");  <br>date_default_timezone_set("Asia/Shanghai");  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")<br>  <br>$trade1 = new stdClass();<br>$trade1-> trade_no = 'JYA2023071200005';<br>$trade1-> shop_name = '东升的tb店铺';<br>$trade1-> warehouse_name = '高筱原的仓库1';<br>$trade1-> logistics_name = '自有';<br>$trade1-> logistics_no = $trade1->trade_no;<br>$trade1-> merchant_no = 4205;<br>$trade1-> num = 4;<br>$trade1-> receivable = 12.5;<br>$trade1-> receiver_address = '北京 北京市 西城区 西直门北大街凯德茂T1';<br>$trade1-> receiver_mobile = '13512340987';<br>//$trade1-> receiver_name = '张张张';<br>//$trade1-> order_price = 2.5;<br>$trade1-> trade_time = '2023-07-12 00:01:02';<br>  <br>$tradeList = array();<br>array_push($tradeList, $trade1);<br>$response = $client->call("sales.TradeImport.upload", $tradeList); <br>?><br>``` |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "data": {<br>        "message": "OK"<br>    },<br>    "status": 0<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "message": "订单编号已存在",<br>    "status": 100<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1