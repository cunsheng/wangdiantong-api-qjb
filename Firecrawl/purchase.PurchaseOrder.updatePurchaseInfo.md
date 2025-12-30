---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.updatePurchaseInfo"
title: "API文档"
---
**purchase.PurchaseOrder.updatePurchaseInfo**（采购单标记更新）

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：修改采购单标记 |
| **1.2 适用版本：** 客户端 V1.3.8.7及以上版本 |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 请求参数 | params | Map<String, Object> |  | 否 | 请求参数 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购单号 | purchase\_no | String |  | 是 | 采购单号 |
| 标记名称 | flag\_name | String |  | 是 | 标记名称必须是采购单所属标记<br>当传入无时，清除采购单标记 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.updatePurchaseInfo#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.updatePurchaseInfo#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.updatePurchaseInfo#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.updatePurchaseInfo#autoTab0_3)

```
[{"purchase_no":"CG2204130001","flag_name":"aa"}]
```

```
<php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$paraMap = new stdClass();
$paraMap->purchase_no = "CG2204130001";
$paraMap->flag_name = "无";

$pager = new Pager(2, 0, true);

$data = $client->call("purchase.PurchaseOrder.updatePurchaseInfo", $paraMap );
?>
```

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{"status":0}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{"status":100,"message":"采购标记不存在:采购量和到货量不一致"}<br>``` |
