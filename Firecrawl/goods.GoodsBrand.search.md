---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsBrand.search"
title: "API文档"
---
**goods.GoodsBrand.search** **（品牌查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP的货品品牌信息 |
| **1.2 适用版本：** 客户端 V1.3.7.1 及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

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
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | Date | 时间格式 | 否 | 开始时间（最后修改时间） |
| 结束时间 | end\_time | Date | 时间格式 | 否 | 结束时间（最后修改时间） |
| 品牌编号 | brand\_no | String |  | 否 | 品牌编号 |
| 品牌名称 | brand\_name | String |  | 否 | 品牌名称 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

**返回值为一个Map<String, Object>**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 货品数据 | data | Map<String, Object> |  | 是 | 货品分类相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据 | detail\_list | List<Map<String, Object>> |  | 是 | 品牌数据 |
| 总条数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 品牌id | brand\_id | Int | 11 | 是 | 品牌id，唯一键 |
| 品牌编号 | brand\_no | String |  | 是 | 品牌编号 |
| 品牌名称 | brand\_name | String |  | 是 | 品牌名称 |
| 是否停用 | is\_disabled | Int |  | 是 | 0：启用<br>1：停用 |
| 备注 | remark | String |  | 是 | 备注 |
| 创建时间 | created | String |  | 是 | 时间格式,样例: 2022-01-25 16:40:06 |
| 最后修改时间 | modified | String |  | 是 | 时间格式,样例: 2022-01-25 16:40:06 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsBrand.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsBrand.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsBrand.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsBrand.search#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"brand_no"``:``"brand_no"``,`<br>```"brand_name"``:``"brand_name"``,`<br>```"start_time"``:``"2022-02-11"``,`<br>```"end_time"``:``"2022-02-13"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2022-02-11"``;`<br>`$parMap``->end_time =``"2022-02-11"``;`<br>`$parMap``->brand_no =``"brand_no"``;`<br>`$parMap``->brand_name =``"brand_name"``;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"goods.GoodsBrand.search"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsBrand.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"detail_list"``: [{`<br>```"brand_no"``:``"BD202201250001"``,`<br>```"created"``:``"2022-01-25 16:40:06"``,`<br>```"is_disabled"``: 0,`<br>```"modified"``:``"2022-01-25 16:40:06"``,`<br>```"brand_name"``:``"香蕉你个巴拉"``,`<br>```"remark"``:``""``,`<br>```"brand_id"``: 34`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsBrand.search#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"errormsg"`<br>`}` |
