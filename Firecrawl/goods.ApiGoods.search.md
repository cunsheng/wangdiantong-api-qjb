---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search"
title: "API文档"
---
**goods.ApiGoods.search** **（平台货品查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP的平台货品资料 |
| **1.2 适用版本：** 客户端 V1.4.4.7及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5注意事项：【权限校验】：店铺权限**<br>开始时间和结束时间是平台货品数据最后修改时间的范围<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台货品数据，淘系及系统供销平台相关规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")，拼多多请自行对接平台获取。 |

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
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String | 20 | 否 | 店铺编号 |
| 平台货品ID | goods\_id | String | 40 | 否 | 平台货品ID |
| 平台规格ID | spec\_id | String | 40 | 否 | 平台规格ID |
| 开始时间 | start\_time | String | 40 | 是 | 起始修改时间, 时间格式 YYYY-MM-DD HH:MM:SS |
| 结束时间 | end\_time | String | 40 | 是 | 结束修改时间 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 货品数据 | data | Map<String, Object> |  | 是 | 货品相关数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品数据 | goods\_list | List<Map<String, Object>> |  | 是 | 货品数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**goods\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台货品唯一键 | rec\_id | Int | 11 | 是 | 平台货品唯一键 |
| 店铺id | shop\_id | Int | 11 | 是 | 店铺id |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 店铺名称 | shop\_name | String | 40 | 是 | 店铺名称 |
| 货品名称 | goods\_name | String | 255 | 是 | 平台货品名称 |
| 规格名称 | spec\_name | String | 100 | 是 | 平台规格名称 |
| 平台规格编码 | spec\_outer\_id | String | 40 | 是 | 平台规格编码 |
| 平台货品编号 | outer\_id | String | 40 | 是 | 平台货品编号 |
| 货品ID | goods\_id | String | 40 | 是 | 平台货品ID |
| 规格ID | spec\_id | String | 40 | 是 | 平台规格ID |
| 活动状态 | is\_deleted | Int | 1 | 是 | 0正常货品，1平台删除，2手工删除 |
| 价格 | price | Decimal(19,4) |  | 是 | 平台价格 |
| 平台库存 | stock\_num | Decimal(19,4) |  | 是 | 平台库存 |
| 状态 | status | Int | 4 | 是 | 0删除，1在架，2下架 |
| 自动匹配 | is\_auto\_match | Int | 1 | 是 | 1自动匹配，0 手动匹配 |
| 系统货品 | match\_target\_type | Int | 1 | 是 | 0未指定，1单品，2组合装 |
| 平台id | platform\_id | Int |  | 是 | 平台id,点击查看 [平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) |
| 占用库存 | hold\_stock | Decimal(19,4) |  | 是 | 占用库存 |
| 占用方式 | hold\_stock\_type | Int | 4 | 是 | 1拍下减库存 <br>2付款减库存 |
| 自动上架 | is\_auto\_listing | bool | 1 | 是 | 是否自动上架<br>true：是<br>false：否 |
| 自动下架 | is\_auto\_delisting | bool | 1 | 是 | 是否自动下架<br>true：是<br>false：否 |
| 最后修改时间 | modified | String | 40 | 是 | 系统中平台货品最后修改时间, 时间格式 YYYY-MM-DD HH:MM:SS |
| 系统商家编码 | merchant\_no | String | 40 | 是 | match\_target\_type=1时返回的为单品商家编码、match\_target\_type=2时返回的为组合装商家编码 |
| 系统货品名称 | merchant\_name | String | 255 | 是 | match\_target\_type=1时返回的为单品的规格名称、match\_target\_type=2时返回的为组合装货品名称 |
| 系统规格码 | merchant\_code | String | 40 | 是 | match\_target\_type=1时返回的为单品规格码、match\_target\_type=2时返回为空字符串 |
| 平台类目id | cid | String | 40 | 是 | 平台类目id |
| 自动匹配的商家编码 | match\_code | String | 40 | 是 | 如果是根据商家编码自动匹配的，那么这个字段记录了商家编码，可以是货品的编码+规格的编码 |
| 系统货品id | match\_target\_id | Int | 11 | 是 | match\_target\_type=1，这值是单品的主键，如果match\_target\_type=2，这值是组合装的主键 |
| 平台条码信息 | barcode | string | 11 | 是 | 平台上的条码，可能存在多个 用 , 号分隔 |
| 平台规格码 | spec\_code | String | 40 | 是 | 平台规格码 |
| 平台sku属性串 | spec\_sku\_properties | String | 1024 | 是 | 平台sku属性串 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 后台信息同步库存 | disable\_syn\_until | Int | 11 | 是 | 后台信息同步库存 |
| 停止同步原因 | disabled\_reason | String | 255 | 是 | 停止同步原因 |
| 最后同步库存量 | last\_syn\_num | Decimal(19,4) |  | 是 | 最后同步库存量 |
| 品牌id | brand\_id | Int | 11 | 是 | 品牌id |
| 是否停止库存同步 | is\_disable\_syn | boolean | 1 | 是 | 是否停止库存同步 |
| 图片url | pic\_url | String | 255 | 是 | 图片url |
| 库存变化时自增量 | stock\_change\_count | Int |  | 是 | 库存变化时自增量 |
| 标记id | flag\_id | Int |  | 是 | 标记id |
| 标记名称 | flag\_name | String |  | 是 | 标记名称 |
| 货品编号 | goods\_no | String |  | 是 | 系统货品编号 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_time"``:``"2020-05-26 16:10:40"``,``"end_time"``:``"2020-05-26 16:11:46"``,``"shop_no"``:``"test"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-05-26 16:10:40"``;`<br>`$parMap``->end_time =``"2020-05-26 16:11:46"``;`<br>`$parMap``->shop_no=``"test"``;`<br>`$pager``=``new``Pager(10, 0, true);`<br>`$data``=``$client``->pageCall(``"goods.ApiGoods.search"``,``$pager``,``$parMap``);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"goods_list"``: [{`<br>```"is_auto_match"``: 1,`<br>```"flag_id"``: 0,`<br>```"hold_stock"``: 0,`<br>```"spec_code"``:``""``,`<br>```"match_code"``:``"AZ38-2\/33+p\/108"``,`<br>```"merchant_code"``:``""``,`<br>```"list_time"``:``""``,`<br>```"stock_num"``: 0,`<br>```"hold_stock_type"``: 0,`<br>```"outer_id"``:``""``,`<br>```"flag_name"``:``"无"``,`<br>```"spec_outer_id"``:``"AZ38-2\/33+p\/108"``,`<br>```"is_deleted"``: 0,`<br>```"spec_id"``:``"123949335"``,`<br>```"price"``: 899,`<br>```"is_auto_delisting"``:``true``,`<br>```"is_auto_listing"``:``true``,`<br>```"modified"``:``"2022-10-14 17:50:32"``,`<br>```"match_target_id"``: 343734,`<br>```"barcode"``:``""``,`<br>```"match_target_type"``: 1,`<br>```"shop_no"``:``"wxxsd"``,`<br>```"goods_name"``:``"【飒爽干练款】全手织真发假发短发妈妈中老年真人发丝逼时尚轻薄透气蓬松假发套"``,`<br>```"spec_sku_properties"``:``""``,`<br>```"merchant_no"``:``"AZ38-2\/33+p\/108"``,`<br>```"created"``:``"2022-04-21 13:39:00"``,`<br>```"goods_id"``:``"63832855"``,`<br>```"disable_syn_until"``: 0,`<br>```"merchant_name"``:``""``,`<br>```"rec_id"``: 382396,`<br>```"disabled_reason"``:``""``,`<br>```"shop_name"``:``"wxxsd"``,`<br>```"last_syn_num"``: -1,`<br>```"brand_id"``: 0,`<br>```"shop_id"``: 681,`<br>```"is_disable_syn"``:``true``,`<br>```"last_syn_time"``:``""``,`<br>```"delist_time"``:``""``,`<br>```"platform_id"``: 90,`<br>```"spec_name"``:``""``,`<br>```"pic_url"``:``""``,`<br>```"status"``: 1,`<br>```"cid"``:``""``,`<br>```"stock_change_count"``: 1`<br>```}],`<br>```"total_count"``: 1`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
