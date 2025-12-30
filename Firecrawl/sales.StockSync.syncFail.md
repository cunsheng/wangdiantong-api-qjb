---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.syncFail"
title: "API文档"
---
### **sales.StockSync.syncFail（库存同步失败）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**库存同步失败时调用 |
| **1.2 适用版本：** 客户端V1.2.4.9及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：** 仅支持自有平台推送 |

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
| Api\_goodsspec表的rec\_id | apiGoodsId | long |  | 是 | Api\_goodsspec表的rec\_id |
| 同步失败后要保存的信息 | info | Map<String, Object> |  | 是 | 同步失败后要保存的信息 |

**info**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 最后同步库存量 | syn\_stock | Decimal(19,4) |  | 是 | 最后同步库存量 |
| 库存变化量 | stock\_change\_count | Decimal(19,4) |  | 是 | 库存变化量 |
| 同步规则策略id | stock\_syn\_rule\_id | Int | 11 | 是 | 同步规则策略id |
| 同步规则策略编号 | stock\_syn\_rule\_no | String | 40 | 是 | 同步规则策略编号 |
| 同步策略的其他信息 | stock\_syn\_other | String | 1024 | 是 | 同步策略的其他信息 |
| 库存同步的仓库id | stock\_syn\_warehouses | String | 1024 | 是 | 库存同步的仓库id，多个仓库则用,分隔 |
| 库存计算方法的掩码 | stock\_syn\_mask | Int | 11 | 是 | 库存计算方法的掩码 |
| 同步百分比 | stock\_syn\_percent | Int | 11 | 是 | 同步百分比 |
| 增加值 | stock\_syn\_plus | Decimal(19,4) |  | 是 | 增加值 |
| 最小同步库存量 | stock\_syn\_min | Decimal(19,4) |  | 是 | 最小同步库存量 |
| 最大同步 | stock\_syn\_max | Decimal(19,4) |  | 是 | 最大同步 |
| 是否自动上架 | is\_auto\_listing | Boolean | 1 | 是 | 是否自动上架 |
| 是否自动下架 | is\_auto\_delisting | Boolean | 1 | 是 | 是否自动下架 |
| 是否同步成功 | is\_syn\_success | Boolean | 1 | 是 | 是否同步成功 |
| 是否手动同步 | is\_manual | Boolean | 1 | 是 | 是否手动同步 |
| 同步结果 | syn\_result | String | 1024 | 是 | 同步结果 |

**4.响应参数**

响应参数为一个Map<String, Object>

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |

**5** **.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.syncFail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.syncFail#autoTab0_1)

|     |     |
| --- | --- |
|  | `[`<br>`2447,`<br>`{`<br>`"stock_syn_min"``:1.0000,`<br>`"stock_syn_rule_id"``:-10000,`<br>`"stock_syn_mask"``:0,`<br>`"stock_syn_warehouses"``:``"6"``,`<br>`"stock_syn_max"``:550.0000,`<br>`"stock_syn_percent"``:100,`<br>`"is_auto_delisting"``:``true``,`<br>`"stock_syn_plus"``:1.0000,`<br>`"is_auto_listing"``:``true``,`<br>`"stock_syn_rule_no"``:``""``,`<br>`"syn_stock"``:1,`<br>`"stock_change_count"``:2`<br>`}`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``StdClass();`<br>``<br>`$parMap``->stock_syn_min=1.0000;`<br>`$parMap``->stock_syn_rule_id=-10000;`<br>`$parMap``->stock_syn_mask=0;`<br>`$parMap``->stock_syn_warehouses=``"6"``;`<br>`$parMap``->stock_syn_max=550.0000;`<br>`$parMap``->stock_syn_percent=100;`<br>`$parMap``->is_auto_delisting=true;`<br>`$parMap``->stock_syn_plus=1.0000;`<br>`$parMap``->is_auto_listing=true;`<br>`$parMap``->stock_syn_rule_no=``""``;`<br>`$parMap``->syn_stock=1;`<br>`$parMap``->stock_change_count=2;`<br>``<br>`$data``=``$client``->call(``"sales.StockSync.syncFail"``, 2447,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.syncFail#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:0`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.syncFail#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``:1064,`<br>`"message"``:” Unknown Database Error”`<br>`}` |
