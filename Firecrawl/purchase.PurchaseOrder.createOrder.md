---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.createOrder"
title: "API文档"
---
**purchase.PurchaseOrder.createOrder** **（采购单新建）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送采购单据给ERP |
| **1.2 适用版本：** 客户端 V1.4.5.8及以上版本 |
| **1.5注意事项：** **【权限校验】：供应商权限、仓库权限**<br>**如果客户端勾选系统配置“开启采购权限（供应商，品牌）”采购单货品需要先维护"供应商货品"才能推送采购单****详见链接：****[供应商货品维护](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E9%87%87%E8%B4%AD%E5%8D%95%E6%96%B0%E5%BB%BA%E6%8F%90%E7%A4%BA'%E4%B8%8D%E5%B1%9E "供应商货品维护")**<br>    金额计算逻辑: 基于系统配置【采购、采购退货-开单&结算价格计算方式】的计算逻辑<br>- 已知-税前折后单价&税率-求-税后单价: 按照税前单价,折扣,税率 计算 税前折后价,税后单价,税后金额<br>  <br>- 已知-税后单价&税率-求-税前折后单价: 按照税后单价,折扣,税率 计算 税后金额,税前折后单价,税前单价 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

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
| 新建参数 | params | Map<String, Object> |  | Y | 新建参数 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购单编号 | purchase\_no | String | 40 | N | 采购单编号 |
| 供应商编号 | provider\_no | String | 20 | Y | 供应商编号 |
| 收货仓编号 | receive\_warehouse\_nos | String | 40 | Y | 收货仓编号（不⽀持分销委外仓，开启系统配置     路径：设置--系统设置--采购设置--采购协同--采购入库支持使用采购预约单入库后，⽀持传⼊多个平台仓编号） |
| 预计入库仓库编号 | expect\_warehouse\_no | String | 40 | Y | 预计入库仓库编号（不支持分销委外仓） |
| 采购员 | purchaser\_name | String | 40 | Y | 采购员（员工页面对应"昵称"字段，员工的"工种"需要有"采购员"） |
| 是否要审核 | is\_check | bool | 1 | N | 审核：true<br>不审核：false<br>不传默认为false |
| 引用的采购申请单编号 | apply\_nos | String | 255 | N | 采购申请单编号,使用英文逗号隔开 |
| 收货地址 | receive\_address | String | 255 | N | 收货地址 |
| 联系人 | contact | String | 40 | N | 联系人 |
| 电话 | telno | String | 32 | N | 电话 |
| 标记名称 | flag\_name | String | 32 | N | 标记名称 |
| 预计到货时间 | expect\_time | String | 19 | N | 预计到货时间，例如：2021-07-10 10:35:\. 若系统不启用【采购开单时自动完善期望到货时间】配置，则采用接口传递的时间<br>2\. 若系统启用【采购开单时自动完善期望到货时间】配置：<br>\- 供应商未设置或设置到货天数为0，仍使用接口传递的时间<br>\- 供应商设置了到货天数，以单据创建时间加到货天数来计算 |
| 创建时间 | created | String | 19 | N | 不传或为空,则为当前时间，例如：2021-07-10 10:30:01 |
| 付款方式 | pay\_type | Int | 4 | N | 1:现付 2:到付 |
| 运费支付方式 | postfee\_pay\_type | Int | 4 | N | 0 无 1 现付 2 到付 3 包邮 |
| 备注 | remark | String | 255 | N | 备注 |
| 邮费 | post\_fee | Decimal(19,4) |  | N | 邮费 |
| 其他费用 | other\_fee | Decimal(19,4) |  | N | 其他费用 |
| 物流公司编号 | logistics\_no | String |  | N | ERP内维护的采购业务类型的物流公司编号 |
| 采购单自定义属性1 | prop1 | String | 255 | N | 采购单自定义属性1 |
| 采购单自定义属性2 | prop2 | String | 255 | N | 采购单自定义属性2 |
| 采购单自定义属性3 | prop3 | String | 255 | N | 采购单自定义属性3 |
| 采购单自定义属性4 | prop4 | String | 255 | N | 采购单自定义属性4 |
| 采购单详情 | purchase\_details | List<Map<String, Object>> |  | N | 采购单详情 |

**purchase\_details**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 采购数量 | num | Int | 11 | Y | 采购数量 |
| 采购单位 | purchase\_unit\_name | String | 20 | N | 采购单位（对应辅助单位） |
| 备注 | remark | String | 255 | N | 备注 |
| 自定义属性1 | prop1 | String | 255 | N | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | N | 自定义属性2 |
| 自定义属性3 | prop3 | String | 255 | N | 自定义属性3 |
| 自定义属性4 | prop4 | String | 255 | N | 自定义属性4 |
| 税前单价 | price | Decimal(19,4) |  | N | 税前单价（当接口账户没有采购价字段权限时，price推送值无效，客户端税前单价字段按照供应商货品页面维护的采购价进行引用） |
| 税后单价 | tax\_price | Decimal(19,4) |  | N | 税后单价（1、需系统配置【采购、采购退货-开单&结算价格计算方式】为【已知税后单价&税率求税前折后单价】时有效     <br>2、当接口账户没有采购价字段权限时，tax\_price推送值无效） |
| 折扣 | discount | Decimal(19,4) |  | N | 折扣字段，默认值为1，1代表原价，无折扣；假设需要折扣为一折时，可将字段值传为0.1，同理，折扣为5折时，传值0.5；折扣为八折时，传值0.8，以此类推 |
| 税率 | tax\_rate | Decimal(19,4) |  | N | 税率（当接口账户没有采购价字段权限时，tax\_rate推送值无效） |
| 批次号 | batch\_no | String | 40 | N | 批次号（如需使用，需要单独开通配置，开启配置的情况下不允许超量入库，开启配置情况下支持创建不存在的批次） |
| 有效期 | expire\_date | String | 40 | N | 有效期（如需使用，需要单独开通配置，开启配置的情况下不允许超量入库） |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码为0，表示调用成功 |
| 错误信息 | message | String |  | Y | 成功返回创建成功的采购单号,否则返回错误信息 |
| 结果信息 | data | Map<String, Object> |  | Y | 结果信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 0：操作全部成功<br>20：审核失败 |
| 返回信息 | message | String |  | Y | 成功返回创建成功的采购单号,否则返回错误信息 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.createOrder#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.createOrder#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.createOrder#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseOrder.createOrder#autoTab0_3)

```
[{\
	"receive_warehouse_nos": "wdtapi3-test",\
	"purchase_details": [{\
		"num": "1",\
		"spec_no": "hcf"\
	}],\
	"purchaser_name": "lj",\
	"expect_warehouse_no": "wdtapi3-test",\
	"provider_no": "LCJtest"\
}]
```

```
<php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$purchase = new stdClass();
$purchase->provider_no='CMS4418046511659';
$purchase->receive_warehouse_nos='lz';
$purchase->expect_warehouse_no='lz';
$purchase->purchaser_name='lz';
$purchase->is_submit=1;

$purchaseDetails = array();
$purchaseDetails1 = new stdClass();
$purchaseDetails1->spec_no='lz11';
$purchaseDetails1->num=1;
array_push($purchaseDetails, $purchaseDetails1);
$purchase->purchase_details = $purchaseDetails;

$data = $client->call("purchase.PurchaseOrder.createOrder", $purchase);
?>
```

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 0,<br>"data": {<br>"message": "CG202003260001",<br>"status": 0<br>}<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "供应商不存在"<br>}<br>``` |
