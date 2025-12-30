---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search"
title: "API文档"
---
**wms.PositionCapacity.search** **（默认货位查询)**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP单品（sku）默认货位 |
| **1.2 适用版本：** 客户端 V1.4.1.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：**start\_time、end\_time时间跨度不能大于7天 |
| **1.5注意事项：** **【权限校验】：仓库权限**、时间不传的情况下，warehouse\_no和spec\_no必传 |

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
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | Int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 否 | 开始时间，最后修改时间 |
| 结束时间 | end\_time | String | 40 | 否 | 结束时间，最后修改时间 |
| 仓库编号 | warehouse\_no | String | 40 | 否 | 仓库编号（时间不传的情况下，仓库编号必传） |
| 商家编码 | spec\_no | String | 40 | 否 | 商家编码（时间不传的情况下，商家编码必传） |
| 货品编号 | goods\_no | String | 40 | 否 | 货品编号 |

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
| 货品数据 | data | Map<String, Object> |  | 是 | 货品相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据 | detail\_list | List<Map<String, Object>> |  | 是 | 数据明细 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键id | rec\_id | Int | 11 | 是 | 主键id |
| 残次品 | defect | boolean | 1 | 是 | true:残次品<br>false:正品 |
| 总库存 | stock\_num | Decimal(19,4) |  | 是 | 总库存 |
| 单品id | spec\_id | Int | 11 | 是 | 单品id |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品简称 | short\_name | String | 255 | 是 | 货品简称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 品牌名称 | brand\_name | String | 50 | 是 | 品牌名称 |
| 品牌id | brand\_id | Int | 11 | 是 | 品牌id |
| 分类名称 | class\_name | String | 50 | 是 | 分类名称 |
| 分类id | class\_id | Int | 11 | 是 | 分类id |
| 仓库id | warehouse\_id | Int | 11 | 是 | 仓库id |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 货区id | zone\_id | Int | 11 | 是 | 货区id |
| 货区编号 | zone\_no | String | 40 | 是 | 货区编号 |
| 货位id | position\_id | Int | 11 | 是 | 货位id |
| 货位编号 | position\_no | String | 40 | 是 | 货位编号 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"spec_no"``:``"all1"``,``"warehouse_no"``:``"daj1"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->spec_no =``"all1"``;`<br>`$parMap``->warehouse_no =``"daj1"``;`<br>`$parMap``->goods_no = all;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.PositionCapacity.search"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 2,`<br>```"detail_list"``: [{`<br>```"spec_code"``:``"all1"``,`<br>```"goods_name"``:``"阿拉蕾"``,`<br>```"class_id"``: 0,`<br>```"goods_no"``:``"all"``,`<br>```"stock_num"``: 217,`<br>```"brand_name"``:``"康师傅"``,`<br>```"zone_no"``:``"daj001"``,`<br>```"rec_id"``: 6804,`<br>```"spec_no"``:``"all1"``,`<br>```"brand_id"``: 5,`<br>```"zone_id"``: 915,`<br>```"defect"``:``true``,`<br>```"warehouse_no"``:``"daj1"``,`<br>```"spec_id"``: 158800,`<br>```"position_no"``:``"AD-1-2-1"``,`<br>```"short_name"``:``"阿拉啊啊"``,`<br>```"spec_name"``:``"颜色:蓝色"``,`<br>```"barcode"``:``"all1"``,`<br>```"class_name"``:``"无"``,`<br>```"position_id"``: 80095,`<br>```"warehouse_id"``: 533`<br>```}, {`<br>```"spec_code"``:``"all1"``,`<br>```"goods_name"``:``"阿拉蕾"``,`<br>```"class_id"``: 0,`<br>```"goods_no"``:``"all"``,`<br>```"stock_num"``: 3,`<br>```"brand_name"``:``"康师傅"``,`<br>```"zone_no"``:``"daj001"``,`<br>```"rec_id"``: 6803,`<br>```"spec_no"``:``"all1"``,`<br>```"brand_id"``: 5,`<br>```"zone_id"``: 915,`<br>```"defect"``:``false``,`<br>```"warehouse_no"``:``"daj1"``,`<br>```"spec_id"``: 158800,`<br>```"position_no"``:``"AD-1-1-2"``,`<br>```"short_name"``:``"阿拉啊啊"``,`<br>```"spec_name"``:``"颜色:蓝色"``,`<br>```"barcode"``:``"all1"``,`<br>```"class_name"``:``"无"``,`<br>```"position_id"``: 80098,`<br>```"warehouse_id"``: 533`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:100,`<br>`"message"``:``"商家编码不能为空"`<br>`}` |
