---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.RawRefund.upload"
title: "API文档"
---
****aftersales.refund.RawRefund.upload**** **（原始退款单推送）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：创建售后退货单给ERP，更新售后单退货物流信息、退货单退款金额等 |
| **1.2 适用版本：** 客户端 V1.2.5.6及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：店铺权限** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 自研商城、分销系统、全渠道等系统对接 |

**3.请求参数说明**

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String |  | 是 | 店铺编号 |
| 原始退款单列表 | order\_list | List<Map<String, Object>> |  | 是 | 原始退款单列表 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始退款单号 | refund\_no | String | 40 | Y | 原始退款单号 |
| 货品数量 | num | Decimal(19,4) |  | Y | 货品数量 |
| 原始单号 | tid | String | 40 | Y | 原始单号 |
| 原始子单号 | oid | String | 40 | Y | 原始子单号 |
| 退款单类型 | type | Int | 4 | Y | 0取消订单1退款(未发货，退款申请)2退货3换货4退款不退货<br>当type=3时原始退款单递交不会生成系统退货单 |
| 平台状态 | status | Int | 4 | Y | 1取消退款,2已申请退款,3等待退货,4等待收货,5退款成功 |
| 退款版本 | refund\_version | String | 40 | Y | 退款版本，默认传1即可 |
| 申请退款金额 | refund\_amount | Decimal(19,4) |  | Y | 申请退款金额 |
| 实际退款金额 | actual\_refund\_amount | Decimal(19,4) |  | Y | 实际退款金额 |
| 标题 | title | String | 255 | Y | 标题，对应原始退款单页面主单货品字段,若无传空字符串 |
| 物流公司名称 | logistics\_name | String | 40 | N | 物流公司名称（支持自定义推送），若无传空字符串 |
| 物流单号 | logistics\_no | String | 40 | N | 物流单号 |
| 客户网名 | buyer\_nick | String | 100 | Y | 客户网名 |
| 退款创建时间 | refund\_time | String | 40 | N | 退款创建时间 |
| 退款成功时间 | current\_phase\_timeout | String | 40 | N | 退款成功时间 |
| 是否售后退款单 | is\_aftersale | Int | 1 | Y | 是否售后退款单 |
| 退款原因 | reason | String | 255 | Y | 退款原因 |
| 单价 | price | Decimal(19,4) |  | N | 单价 |
| 买家支付帐号 | pay\_account | String | 128 | N | 买家支付帐号 |
| 支付订单号 | pay\_no | String | 60 | N | 支付订单号 |
| 备注 | remark | String | 255 | N | 备注 |
| 退款货品总价 | total\_amount | Decimal(19,4) |  | N | 退款货品总价 |
| 平台规格编号 | spec\_no | String | 40 | N | 平台规格编号 |
| 平台规格id | spec\_id | String | 40 | N | 平台规格id |
| 平台货品编号 | goods\_no | String | 40 | N | 平台货品编号 |
| 平台货品id | goods\_id | String | 40 | N | 平台货品id |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int | 11 | Y | 执行失败,则返回,执行成功不返回 |
| 错误信息 | messge | string | 255 | N | 执行失败,则返回错误信息, 执行成功不返回 |
| 结果数据 | data | Map<String,Object> |  | N | 结果数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 更新订单数 | chg\_count | Int |  | N | 执行成功，返回更新订单的数量 |
| 新增订单数 | new\_count | int |  | N | 执行成功，返回新增订单的数量 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.RawRefund.upload#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.RawRefund.upload#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.RawRefund.upload#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=aftersales.refund.RawRefund.upload#autoTab0_3)

```
["LCJ", [{\
"refund_no": "lztest",\
"num": 1,\
"tid": "TID6NAFAmwYMM",\
"oid": "deb718e2afe5",\
"type": 1,\
"status": 2,\
"refund_version": "1",\
"refund_amount": 1,\
"actual_refund_amount": 1,\
"title": "test",\
"logistics_name": "",\
"logistics_no": "",\
"buyer_nick": "123444",\
"refund_time": "2020-05-22 09:07:18",\
"is_aftersale": 0,\
"reason": ""\
}]]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$shopNo='LCJ';

$orderList = array();

$orderList1 = new stdClass();
$orderList1->refund_no='lztest';
$orderList1->num=1;
$orderList1->tid='TID6NAFAmwYMM';
$orderList1->oid='deb718e2afe5';
$orderList1->type=1;
$orderList1->status=2;
$orderList1->refund_version='1';
$orderList1->refund_amount=1;
$orderList1->actual_refund_amount=1;
$orderList1->title='test';
$orderList1->logistics_name='';
$orderList1->logistics_no='';
$orderList1->buyer_nick='可用库存';
$orderList1->is_aftersale=0;
$orderList1->reason='';

array_push($orderList, $orderList1);

$data = $client->call("aftersales.refund.RawRefund.upload", $shopNo, $orderList);
?>
```

```

```

```

```

**6.响应示例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 0,<br>"data": {<br>"chg_count": 0,<br>"new_count": 1<br>}<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "退换单已存在"<br>}<br>``` |
