---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighing"
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

**wms.stockout.Sales.onceWeighing** **（重量回传2）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：将重量回传写入ERP销售订单出库单 |
| **1.2 适用版本：** 客户端 V1.2.2.8及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 自动化称重机、自动化分拣系统、仓储设备控制系统等称重以后，将重量回传写入ERP销售订单出库单。 |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流单号 | logisticsOrTradeNo | String |  | y | 物流单号或者出库单号 |
| 包装条码 | packageBarcode | String |  |  | 如果没有, 可传"" |
| 重量 | weight | BigDecimal |  | y | 包裹重量 |
| 打包员 | packagerId | Int |  | y | 无打包员则传0 |
| 打包台名称 | operateTableName | String |  | y | 无打包台信息, 则传空字符串 |
| 是否强制称重 | force | boolean |  | y | 默认传false |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | n | 无错误信息不返回 |
| 数据节点 | data | Map<String, Object> |  | n | 有错误信息则不返回此节点 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流公司名称 | logistics\_name | String |  | y | 物流公司名称 |
| 物流名称 | sys\_logistics\_name | String |  | y | 物流名称(系统中物流名称) |
| 物流单号 | logistics\_no | String |  | y | 物流单号 |
| 预估重量 | calc\_weight | BigDecimal(19,4) |  | y | 预估重量 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighing#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighing#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighing#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.onceWeighing#autoTab0_3)

```
["ZS201912060028","", 1,0,null,false]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$logisitcsNo = 'ZS201912060028';
$barcode = '';
$weigh = 1.0;
$packageId = 0;
$operateTableName = null;

$data = $client->call("wms.stockout.Sales.onceWeighing", $logisitcsNo, $barcode, $weigh, $packageId, $operateTableName, false);

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
| JSON | ```<br>{<br>"status": 0,<br>"data": {<br>"logistics_name": "自有物流",<br>"sys_logistics_name": "无需物流",<br>"logistics_no": "ZS201912060028",<br>"calc_weight": 4.0000<br>}<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "单据不存在"<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1