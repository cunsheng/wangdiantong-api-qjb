---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.upload"
title: "API文档"
---
****goods.ApiGoods.upload**（平台货品推送）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 推送平台货品信息给ERP |
| **1.2 适用版本：** 客户端 V1.5.3.9及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：店铺权限**<br>(1)仅支持创建自有平台的平台货品<br>（2）接口只创建平台货品，不会关联系统货品，匹配方式为自动匹配<br>（3）平台货品以店铺+goods\_id+spec\_id组成唯一，如果已存在数据则会覆盖 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

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
| 平台货品数据 | param | Map<String,Object> |  | 是 | 平台货品数据 |

**param**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String |  | 是 | 店铺编号 |
| 平台货品明细 | goods\_list | List<Map<String,Object>> |  | 是 | 平台货品数据 |

**goods\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品ID | goods\_id | String | 40 | 否 | 平台货品ID, 不传默认为空 |
| 规格ID | spec\_id | String | 40 | 否 | 平台规格ID, 不传默认为空 |
| 平台货品编号 | goods\_no | String | 40 | 否 | 平台货品编号, 不传默认为空 |
| 平台规格编码 | spec\_no | String | 40 | 否 | 平台规格编码, 不传默认为空 |
| 状态 | status | Int |  | 否 | 0：删除<br>1：在架<br>2：下架<br>不传默认1 |
| 货品名称 | goods\_name | String | 255 | 否 | 平台货品名称, 不传默认为空 |
| 规格名称 | spec\_name | String | 100 | 否 | 平台规格名称, 不传默认为空 |
| 图片url | pic\_url | String | 255 | 否 | 图片url, 不传默认为空 |
| 平台售价 | price | Decimal(19,4) |  | 否 | 平台售价，不传默认为0 |
| 库存数量 | stock\_num | Decimal(19,4) |  | 否 | 库存数量，不传默认为0 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | Map<String,Object> |  | 否 | 返回信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态 | status | Int |  | 是 | 响应成功则返回0 |
| 平台货品主键id字段 | rec\_ids | List<Integer> |  | 是 | 推送成功时返回平台货品主键id字段 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.upload#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.upload#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.upload#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.upload#autoTab0_3)

```
[{\
    "goods_list": [{\
        "spec_id": "wdt20240910",\
        "goods_no": "wdt20240910",\
        "goods_id": "wdt20240910",\
        "spec_no": "wdt20240910"\
    }, {\
        "spec_id": "wdt202409101",\
        "goods_no": "wdt202409101",\
        "goods_id": "wdt202409101",\
        "spec_no": "wdt202409101"\
    }],\
    "shop_no": "wdtapi3-test"\
}]
```

```
<?php
header("Content-Type: text/html;   charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new   WdtErpClient("url", "wdtapi3", "appkey",   "secret");
$param = new stdClass();
$param->shop_no="wdtapi3-test";

$paramDetail = new stdClass();
$paramDetail->goods_id="PC_20163";
$paramDetail->spec_id="1.53";
$paramDetail->goods_no="wtt00013";
$paramDetail->spec_no="wtt00013";
$paramDetail->status=1;   //0:删除; 1：在架;  2：下架;
$paramDetail->goods_name="wtt00013";
$paramDetail->spec_name="wtt00013";
$paramDetail->pic_url="";
$paramDetail->price="1";
$paramDetail->stock_num="1";

$param->goods_list = [$paramDetail];

$response = $client->call("goods.ApiGoods.upload",$param);

?>
```

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "rec_ids": [<br>            763953,<br>            763954<br>        ],<br>        "status": 0<br>    }<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 100,<br>    "message": "店铺不存在/无权限/类型错误"<br>}<br>``` |
