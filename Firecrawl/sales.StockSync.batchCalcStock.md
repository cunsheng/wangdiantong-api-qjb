---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.batchCalcStock"
title: "API文档"
---
### **sales.StockSync.batchCalcStock 库存同步计算查询(支持批量查询)**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**批量库存同步计算查询 |
| **1.2 适用版本：** 客户端V1.5.3.9以上版本 |
| **1.3 增量获取:** |
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
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务请求参数 | params | List<Map<String, Object>> |  | 是 | 业务请求参数 |

params

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台货品的rec\_id | api\_goods\_id | long |  | 是 | 平台货品的rec\_id |
| 货品是否开启检测 | force\_sync | Boolean |  | 是 | true开启；false未开启，（主要用于被停用平台货品或临时停止库存同步时强制同步库存，无该逻辑传false即可） |

4.响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 数据信息 | data | Map<String, Object> |  | N | 数据信息 |

data

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 成功数据 | success\_date | List<Map<String, Object>> |  | Y | 成功数据 |
| 失败数据 | error\_date | List<Map<String, Object>> |  | N | 失败数据 |

success\_date

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 编码 | match\_code | String | 40 | 是 | 如果是根据商家编码自动匹配的，那么这个字段记录了商家编码，可以是货品的编码+规格的编码 |
| 定时上架时间 | list\_time | String | 40 | 是 | 定时上架时间 |
| 最小同步库存量 | stock\_syn\_min | Decimal(19,4) |  | 是 | 最小同步库存量 |
| 平台库存 | stock\_num | Decimal(19,4) |  | 是 | 平台库存 |
| 库存同步的仓库id | stock\_syn\_warehouses | String | 1024 | 是 | 库存同步的仓库id，多个仓库则用,分隔 |
| 子平台ID | sub\_platform\_id | Int | 4 | 是 | 子平台ID,子平台只是业务流程上有差别，订单、货品应该是同一管理方式 |
| 平台货品编码 | outer\_id | String | 40 | 是 | 平台货品编码 |
| 平台规格编码 | spec\_outer\_id | String | 40 | 是 | 平台规格编码 |
| 同步百分比 | stock\_syn\_percent | Int | 11 | 是 | 同步百分比 |
| 平台规格id | spec\_id | String | 40 | 是 | 平台规格id |
| 是否自动下架 | is\_auto\_delisting | Boolean | 1 | 是 | 是否自动下架 |
| 增加值 | stock\_syn\_plus | Decimal(19,4) |  | 是 | 增加值 |
| 是否自动上架 | is\_auto\_listing | Boolean | 1 | 是 | 是否自动上架 |
| 系统货品的ID | match\_target\_id | Int | 11 | 是 | 系统货品的ID，如果match\_target\_type=1，这值是goods\_spec的主键，如果match\_target\_id=2，这值是goods\_suite的主键 |
| target\_id的类型 | match\_target\_type | Int | 11 | 是 | target\_id的类型 <br>0未绑定 <br>1规格 <br>2组合装 |
| 掩码 | mask | Int | 11 | 是 | 掩码,1临时延时 |
| 需要同步库存的量 | syn\_stock | Int | 11 | 是 | 需要进行同步库存的量 |
| 保留 | reserve\_s | String | 50 | 是 | 保留 |
| 同步规则策略id | stock\_syn\_rule\_id | Int | 11 | 是 | 同步规则策略id |
| 库存计算方法的掩码 | stock\_syn\_mask | Int | 11 | 是 | 库存计算方法的掩码 |
| 平台货品id | goods\_id | String | 40 | 是 | 平台货品号 |
| Api\_goodsspec表的主键id | rec\_id | Int | 20 | 是 | Api\_goodsspec表的主键id |
| 最后同步库存量 | last\_syn\_num | Decimal(19,4) |  | 是 | 最后同步库存量 |
| 店铺ID | shop\_id | Int | 6 | 是 | 店铺id |
| 最大同步 | stock\_syn\_max | Decimal(19,4) |  | 是 | 最大同步 |
| 最后同步时间 | last\_syn\_time | String | 40 | 是 | 最后同步时间 |
| 定时下架时间 | delist\_time | String | 40 | 是 | 定时下架时间 |
| 平台id | platform\_id | Int | 4 | 是 | 因为是自有平台，所以固定是127 |
| 同步规则策略编号 | stock\_syn\_rule\_no | String | 40 | 是 | 在此映射记录上起作用的同步规则策略编号 |
| 平台货品状态 | status | Int | 4 | 是 | 0删除 1在架 2下架 |
| 库存变化量 | stock\_change\_count | Int | 11 | 是 | 库存变化时自增 |

error\_date

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台货品id | rec\_id | int |  | 是 | 失败的irec\_id |
| 失败数据 | err\_msg | string | 11 | N | 失败原因 |

**5** **.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.batchCalcStock#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.batchCalcStock#autoTab0_1)

|     |     |
| --- | --- |
|  | `[`<br>```[`<br>```{`<br>```"api_goods_id"``: 2447,`<br>```"force_sync"``:``false`<br>```},`<br>```{`<br>```"api_goods_id"``: 2448,`<br>```"force_sync"``:``false`<br>```}`<br>```]`<br>`]` |

|     |     |
| --- | --- |
|  | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$pars1``=``new``stdClass();`<br>`$pars1``->api_goods_id = 2447;`<br>`$pars1``->force_sync = false;`<br>`$pars2``=``new``stdClass();`<br>`$pars2``->api_goods_id = 2448;`<br>`$pars2``->force_sync = false;`<br>`$pars``=``array``();`<br>`array_push``(``$pars``,``$pars2``,``$pars1``);`<br>`//$data = $client->call("sales.StockSync.getSelfWaitSyncIdListOpen", $count, $position);`<br>`$data``=``$client``->call(``"sales.StockSync.batchCalcStock"``,``$pars``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.batchCalcStock#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"success_date"``: [`<br>```{`<br>```"match_code"``:``"notebook【临】33333"``,`<br>```"list_time"``:``""``,`<br>```"stock_syn_min"``: 200,`<br>```"stock_num"``: 0,`<br>```"stock_syn_warehouses"``:``"6,12,11"``,`<br>```"sub_platform_id"``: 0,`<br>```"outer_id"``:``"notebook"``,`<br>```"spec_outer_id"``:``"【临】33333"``,`<br>```"stock_syn_percent"``: 100,`<br>```"spec_id"``:``"0"``,`<br>```"is_auto_delisting"``:``true``,`<br>```"stock_syn_plus"``: 1,`<br>```"is_auto_listing"``:``true``,`<br>```"match_target_id"``: 2695,`<br>```"match_target_type"``: 1,`<br>```"mask"``: 4,`<br>```"syn_stock"``: 0,`<br>```"area_stock"``: [`<br>```{`<br>```"api_warehouse_id"``: 1,`<br>```"api_warehouse_no"``:``"111"``,`<br>```"api_warehouse_name"``:``"sss门店1"``,`<br>```"outer_yc_owner_code"``:``""``,`<br>```"type"``: 0,`<br>```"stock_syn_rule_id"``: 13,`<br>```"stock_syn_rule_no"``:``"lzx2"``,`<br>```"stock_syn_warehouses"``:``"16,6,56,54,52,42,29,26,28,25,24,20,19,14,13,30,12,10,4,11"``,`<br>```"stock_syn_mask"``: 0,`<br>```"stock_syn_percent"``: 100,`<br>```"stock_syn_plus"``: 1,`<br>```"stock_syn_min"``: 10,`<br>```"stock_syn_max"``: 0,`<br>```"mask"``: 0,`<br>```"is_disable_syn"``:``false``,`<br>```"last_syn_num"``: -1,`<br>```"syn_stock"``: 0`<br>```}`<br>```],`<br>```"stock_syn_rule_id"``: 1,`<br>```"stock_syn_mask"``: 33263,`<br>```"goods_id"``:``"578208424251"``,`<br>```"rec_id"``: 2448,`<br>```"last_syn_num"``: -1,`<br>```"shop_id"``: 3,`<br>```"stock_syn_max"``: 500,`<br>```"last_syn_time"``:``""``,`<br>```"delist_time"``:``""``,`<br>```"stock_syn_high_frequency"``: 10.1,`<br>```"platform_id"``: 1,`<br>```"stock_syn_rule_no"``:``"001"``,`<br>```"status"``: 1,`<br>```"stock_change_count"``: 54`<br>```}`<br>```],`<br>```"error_date"``: [`<br>``<br>```]`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.batchCalcStock#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"success_date"``: [`<br>```{`<br>```}`<br>```],`<br>```"error_date"``: [`<br>```{`<br>```"err_msg"``:``"force_sync"``,`<br>```"rec_id"``: 2447`<br>```}`<br>```]`<br>`}` |
