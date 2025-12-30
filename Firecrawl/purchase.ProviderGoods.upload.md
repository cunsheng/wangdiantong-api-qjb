---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.upload"
title: "API文档"
---
**purchase.ProviderGoods.upload** **（供应商货品推送）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 推送/更新供应商货品信息 |
| **1.2 适用版本：** 客户端 V1.5.3.9及以上版本 |
| **1.5注意事项：**(1)该接口支持创建和更新，provider\_no+spec\_no已存在则更新，不存在则新建；<br>(2)接口用户需要有\[采购价\]字段权限; 开启供应商权限的情况下需要有对应供应商权限;status = 0且error\_list不为空时, 跳过异常明细, 其他正常创建。 |

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
| 供应商货品明细 | purchase\_provider\_goods\_list | List<Map<String, Object>> |  | 是 | 供应商货品明细 |

**purchase\_provider\_goods\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编号 | provider\_no | String |  | Y | 供应商编号 |
| 商家编码 | spec\_no | String |  | Y | 商家编码 |
| 最小采购量 | min\_purchase\_num | Decimal(19,4) |  | N | 默认1 |
| 采购单位 | purchase\_unit\_name | String |  | N | 默认无，<br>传入的采购单位必须和基本单位(单品无基本单位则取货品的基本单位)匹配 |
| 折扣率 | discount | Decimal(19,4) |  | N | 折扣字段，默认值为1，1代表原价，无折扣；假设需要折扣为一折时，可将字段值传为0.1，同理，折扣为5折时，传值0.5；折扣为八折时，传值0.8，以此类推 |
| 供应商货号 | provider\_goods\_no | String |  | N | 默认空串 |
| 采购价 | price | Decimal(19,4) |  | N | 默认0 |
| 最低采购价 | lowest\_price | Decimal(19,4) |  | N | 默认0 |
| 采购周期 | purchase\_cycle\_day | Int |  | N | 默认0 |
| 税率 | tax\_rate | Decimal(19,4) |  | N | 默认0 |
| 是否主供应商 | is\_master | boolean |  | N | 默认true |
| 备注 | remark | String |  | N | 默认空 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 否 | 无错误信息不返回 |
| 返回信息 | data | Map<String, Object> |  | 否 | 返回信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误信息列表 | error\_list | List<String> |  | 是 | 无异常则list为空 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.upload#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.upload#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.upload#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.upload#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>```[{`<br>```"spec_no"``:``"dongfangshuye"``,`<br>```"provider_no"``:``"LCJtest"`<br>```}, {`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"provider_no"``:``"20170808002"`<br>```}]`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``StdClass();`<br>``<br>`$parMap``->provider_no =’1001’;`<br>`$parMap``->spec_no =’FAQB06201M’;`<br>``<br>`$data``=``$client``->call(``"purchase.ProviderGoods.upload"``,[``$parMap``]);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.upload#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"error_list"``: []`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.upload#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"error_list"``: [`<br>```"LCTtest11 供应商货品重复,商家编码：dongfangshuye"``,`<br>```"秋天001 供应商货品重复,商家编码：wangdiantong"`<br>```]`<br>```}`<br>`}` |
