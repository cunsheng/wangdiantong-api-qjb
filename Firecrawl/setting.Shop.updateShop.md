---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.updateShop"
title: "API文档"
---
**setting.Shop.updateShop**（店铺更新）

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：更新ERP的店铺档案资料 |
| **1.2 适用版本：** 客户端 V1.2.5.6及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

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
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 联系人 | contact | String | 32 | 否 | 联系人 |
| 省 | province | Int | 11 | 否 | 代码表参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 市 | city | Int | 11 | 否 | 代码表参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 区 | district | Int | 11 | 否 | 代码表参考 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地址 | address | String | 255 | 否 | 地址 |
| 电话 | telno | String | 40 | 否 | 电话 |
| 手机 | mobile | String | 40 | 否 | 手机 |
| 邮编 | zip | String | 16 | 否 | 邮编 |
| 邮箱 | email | String | 64 | 否 | 邮箱 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 网址 | website | String | 1024 | 否 | 网址 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | List<Map<String, Object>> |  | 是 | 返回信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 更新成功返回0 |
| 查询结果 | message | String |  | 是 | 更新成功返回OK |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.updateShop#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.updateShop#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.updateShop#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.updateShop#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"shop_no"``:``"test"``,``"website"``:``"website update"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$shop``=``new``StdClass();`<br>`$shop``->shop_no =``"test"``;`<br>`$shop``->website =``"website update"``;`<br>`$data``=``$client``->call(``"setting.Shop.updateShop"``,``$shop``);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.updateShop#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:0,``"data"``:`<br>`{`<br>`"message"``:``"OK"``,``"status"``:0`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.updateShop#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:100,``"message"``:``"店铺编号为 testxxxxx 的店铺不存在"`<br>`}` |
