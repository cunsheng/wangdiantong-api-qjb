---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.createExt"
title: "API文档"
---
****wms.stockin.PreStockin.createExt**** **（创建退货预入库）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送退货预入库单据给ERP |
| **1.2 适用版本：** 客户端 V1.5.8.8及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：仓库权限、**<br>不支持外部仓储 |

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
| 入库单信息 | stockinOrder | Map<String, Object> |  | 是 | 入库单信息 |
| 入库单明细 | specList | List<Map<String, Object>> |  | 是 | 入库单明细，不能为为空 |

stockinOrder

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号（不支持外部仓储） |
| 入库单号 | stockin\_no | String | 20 | 是 | 入库单号 |
| 备注 | remark | String | 255 | 是 | 备注，若无可为”” |
| 寄回物流单号 | logistics\_no | String |  | 否 | 寄回物流单号 |
| 自定义属性1 | prop1 | String | 255 | 否 | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | 否 | 自定义属性2 |

**specList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 数量 | num | Int | 11 | 是 | 入库数量 |
| 残次品 | defect | Boolean | 1 | 是 | 是否为残次品 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 成功返回0 |
| 返回值 | data | String |  | 是 | 成功返回入库单id |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |

**5.请求示例**

- [Json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.createExt#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.createExt#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.createExt#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.PreStockin.createExt#autoTab0_3)

```
[{\
"warehouse_no": "lz",\
"remark": "test"\
},\
[{\
"spec_no": "lz11",\
"remark": "test1",\
"num": 1,\
"defect": false\
}, {\
"spec_no": "lz12",\
"remark": "test2",\
"num": 1,\
"defect": false\
}]\
]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$stockinOrder = new stdClass();
$stockinOrder->warehouse_no='lz';
$stockinOrder->remark='test';

$stockinOrderDetailList = array();
$stockinOrderDetail1 = new stdClass();
$stockinOrderDetail1-> spec_no='lz11';
$stockinOrderDetail1-> remark = 'test1';
$stockinOrderDetail1-> num=1;
$stockinOrderDetail1-> defect = false;

$stockinOrderDetail2 = new stdClass();
$stockinOrderDetail2-> spec_no='lz12';
$stockinOrderDetail2-> remark = 'test2';
$stockinOrderDetail2-> num=1;
$stockinOrderDetail2-> defect = false;
array_push($stockinOrderDetailList,$stockinOrderDetail1);
array_push($stockinOrderDetailList,$stockinOrderDetail2);
$response = $client->call("wms.stockin.PreStockin.createExt", $ stockinOrder, $ stockinOrderDetailList);

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
| JSON | ```<br>{<br>        "status": 0,<br>        "data": 2724<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "没有该仓库权限"<br>}<br>``` |
