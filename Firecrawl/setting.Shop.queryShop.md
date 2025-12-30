---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.queryShop"
title: "API文档"
---
**setting.Shop.queryShop**（店铺查询）

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的店铺档案资料 |
| **1.2 适用版本：** 客户端 V1.4.4.7及以上版本 |
| **1.3 增量获取：** 不支持 |
| **1.4 时间跨度：** 店铺编号不传则全量获取 |
| **1.5注意事项：** **【权限校验】：店铺权限** |

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
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String | 20 | 否 | 店铺编号 |
| 平台id | platform\_id | Int | 6 | 否 | 平台id,点击 [查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 获取平台id |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | List<Map<String, Object>> |  | 是 | 返回信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总条数 | total\_count | Int |  | 是 | 结果总数 |
| 查询结果 | details | List<Map<String, Object>> |  | 是 | 查询结果 |

**details**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺id | shop\_id | Int | 11 | 是 | 店铺唯一键 |
| 店铺名称 | shop\_name | String | 128 | 是 | 店铺名称 |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 平台id | platform\_id | Int | 4 | 是 | 平台id，点击查看 [平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) |
| 子平台id | sub\_platform\_id | Int | 4 | 是 | 子平台id |
| 联系人 | contact | String | 32 | 是 | 联系人 |
| 省份 | province | String | 40 | 是 | 省份 |
| 城市 | city | String | 60 | 是 | 城市 |
| 区县 | district | String | 40 | 是 | 区县 |
| 地址 | address | String | 255 | 是 | 地址 |
| 电话 | telno | String | 40 | 是 | 电话 |
| 手机 | mobile | String | 40 | 是 | 手机 |
| 邮编 | zip | String | 16 | 是 | 邮编 |
| Email | email | String | 64 | 是 | Email |
| 备注 | remark | String | 255 | 是 | 备注 |
| 网址 | website | String | 1024 | 是 | 网址 |
| 分组 | group\_id | String | 100 | 是 | 分组 |
| 平台的主键 | account\_id | String |  | 是 | 平台的主键（平台店铺授权时平台有推送对应值则返回，不推送则返回空字符串） |
| 停用 | is\_disabled | bool | 1 | 是 | true:停用 false:未停用 |
| 授权状态 | auth\_state | byte | 4 | 是 | 授权状态<br>0：未授权<br>1：已授权<br>2：授权失效<br>3：授权停用 |
| 授权时间 | auth\_time | String |  | 是 | 授权时间 |
| refresh\_token过期时间 | re\_expire\_time | String |  | 是 | refresh\_token过期时间 |
| 修改时间 | modified | String |  | 是 | 修改时间 |
| session过期时间 | expire\_time | String |  | 是 | session过期时间 |
| 创建时间 | created | String |  | 是 | 创建时间 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.queryShop#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.queryShop#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.queryShop#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.queryShop#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"platform_id"``:``"127"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->platform_id = 127;`<br>`$parMap``->shop_no =``"wdtapi3-test"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"setting.Shop.queryShop"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.queryShop#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"details"``: [{`<br>```"city"``:``"北京市"``,`<br>```"re_expire_time"``:``""``,`<br>```"sub_platform_id"``: 0,`<br>```"remark"``:``""``,`<br>```"telno"``:``""``,`<br>```"province"``:``"北京"``,`<br>```"contact"``:``""``,`<br>```"auth_time"``:``"2022-08-19 08:16:07"``,`<br>```"modified"``:``"2023-03-28 16:48:12"``,`<br>```"email"``:``""``,`<br>```"shop_no"``:``"JD_test_wdt"``,`<br>```"zip"``:``""``,`<br>```"website"``:``""``,`<br>```"address"``:``"西直门外大街1号西环广场T1座7层"``,`<br>```"created"``:``"2023-03-08 10:35:57"``,`<br>```"is_disabled"``:``false``,`<br>```"mobile"``:``""``,`<br>```"auth_state"``: 1,`<br>```"expire_time"``:``"2029-11-19 05:59:59"``,`<br>```"shop_name"``:``"京东二次上架测试店铺"``,`<br>```"shop_id"``: 1122,`<br>```"account_id"``:``""``,`<br>```"group_id"``:``"无"``,`<br>```"district"``:``"西城区"``,`<br>```"platform_id"``: 3`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Shop.queryShop#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
