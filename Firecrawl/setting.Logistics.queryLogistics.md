---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Logistics.queryLogistics"
title: "API文档"
---
****setting.Logistics.queryLogistics**（物流公司查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP物流公司信息 |
| **1.2 适用版本：** 客户端 V1.5.9.0及以上版本 |
| **1.3 增量获取：** 不支持 |
| **1.4 时间跨度：** |
| **1.5注意事项：** 结果不含已停用的物流 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** |

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
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 否 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流编号 | logistics\_no | String | 40 | n | 物流编号 |
| 物流名称 | logistics\_name | String |  | n | 物流名称 |
| 是否隐藏已停用 | hide\_delete | boolean | 1 | n | true:隐藏；false:不隐藏 |
| 是否需要刷新单量余额 | need\_quantity | bool |  | n | 0：否（默认）<br>1：是 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 返回信息 | data | List<Map<String, Object>> |  | y | 返回信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总条数 | total\_count | Int |  | 是 | 总条数 |
| 查询结果 | details | List<Map<String, Object>> |  | 是 | 查询结果 |
| details |  |  |  |  |  |
| 物流id | logistics\_id | Int | 6 | 是 | 物流唯一键 |
| 物流类型 | logistics\_type | Int | 6 | 是 | 物流类型， [点击查看物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) |
| 是否支持货到付款 | is\_support\_cod | boolean |  | 是 | true：支持   <br>false：不支持 |
| 物流编号 | logistics\_no | String | 40 | 是 | 物流编号 |
| 物流名称 | logistics\_name | String | 40 | 是 | 物流名称 |
| 联系人 | contact | String | 64 | 是 | 联系人 |
| 固话/联系电话 | telno | String | 20 | 是 | 固话/联系电话 |
| 手机 | mobile | String | 20 | 是 | 手机 |
| 地址 | address | String | 255 | 是 | 地址 |
| 单号来源 | ebill\_api | Int |  | 是 | 0：纸质面单 1：线下热敏 2：菜鸟电子面单（淘宝云栈）3：京东无界 4：拼多多金虹桥 5：区域零售 6：云集电子面单 11：唯品JIT电子面单 16:ASCP电子面单  17：菜鸟集货电子面单  18:抖音电子面单 19：得物品牌直发 20：快手电子面单 21：美团电子面单 22：唯品MP电子面单 23：商家仓自营配电子面单 24：鲸灵电子面单  25:腾讯惠聚电子面单 |
| 是否预支单号 | is\_preset\_no | boolean |  | 是 | true：是<br>false：否 |
| 货运方式 | send\_type | Int |  | 是 | 0: 标准快递,1:  生鲜速配,2: 冷运速配 |
| 停用 | is\_disabled | boolean |  | 是 | true：已停用   <br>false：未停用<br>（当hide\_delete传true时返回） |
| 重量上限 | max\_weight | Decimal(19,4） |  | 是 | 重量上限 |
| 备注 | remark | String |  | 是 | 备注 |
| 修改时间 | modified | String | 40 | 是 | 修改时间，格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String | 40 | 是 | 创建时间，格式: yyyy-MM-dd HH:mm:ss |
| 月结卡号 | month\_card | String | 40 | 是 | 月结卡号 |
| 抛重比 | volume\_weight\_ratio | Decimal(19,4) |  | 是 | 抛重比 |
| 是否使用分区抛重比 | volume\_weight\_ratio\_switch | Int | 1 | 是 | 0：否<br>1：是 |
| 分区类型 | volume\_type | Int | 1 | 是 | 分区类型<br>0：体积<br>1：长宽高之和 |
| 阈值（体积或长宽高之和） | volume\_threshold | Decimal(19,4) |  | 是 | 使用分区抛重比时，体积或者长宽高之和大于该值时，分区抛重比生效 |
| 分区抛重比 | volume\_weight\_ratio\_special | Decimal(19,4) |  | 是 | 分区抛重比 |
| 业务类型 | type | varchar | 40 | 是 | 业务类型<br>1：销售出库<br>2：销售退货<br>3：WMS销售<br>4：JIT销售<br>10：采购业务<br>127：其它业务 |
| 主物流 | main\_logistics\_name | String |  | 是 | 主物流名称 |
| 单量余额 | quantity | String |  | 是 | 单量余额 |

**5.请求示例**

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Logistics.queryLogistics#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Logistics.queryLogistics#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Logistics.queryLogistics#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Logistics.queryLogistics#autoTab0_3)

```
[{"logistics_no":"001"}]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$parMap = new stdClass();
$parMap->logistics_no = "3456789876789";

$pager = new Pager(1, 0, true);

$response = $client->pageCall("setting.Logistics.queryLogistics", $pager, $parMap);

?>
```

```

```

```

```

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "total_count": 1,<br>        "details": [{<br>            "logistics_name": "2524352345",<br>            "address": "",<br>            "is_preset_no": false,<br>            "logistics_no": "534245",<br>            "send_type": 0,<br>            "created": "2022-09-01 11:53:23",<br>            "is_disabled": false,<br>            "mobile": "",<br>            "remark": "",<br>            "ebill_api": 25,<br>            "type":1,<br>            "telno": "",<br>            "logistics_id": 974,<br>            "max_weight": 0,<br>            "contact": "54325",<br>            "modified": "2022-09-01 11:53:23",<br>            "logistics_type": 3,<br>            "is_support_cod": false<br>        }]<br>    }<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "XXXX "<br>}<br>``` |
