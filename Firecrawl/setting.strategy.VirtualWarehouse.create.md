---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.create"
title: "API文档"
---
**setting.strategy.VirtualWarehouse.create** **（虚拟仓订单创建)**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥定制**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**创建虚拟仓订单给ERP |
| **1.2 适用版本：** 客户端 V1.3.8.3及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：权限校验：【虚拟仓权限】** |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据信息 | orderMap | Map<String, Object> |  | 是 | 单据信息 |
| 明细信息 | detailList | List<Map<String, Object>> |  | 是 | 明细信息 |

**orderMap**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 是 | 虚拟仓编号 |
| 单据类型 | order\_type | byte |  | 否 | 1:锁定分配,2:释放出库,3:虚拟仓间调拨,4:采购入库<br>默认值为1 |
| 目标虚拟仓编号 | to\_virtual\_warehouse\_no | String |  | 否 | order\_type=3时必传 |
| 是否预审核 | is\_pre\_check | Int |  | 否 | 仅在order\_type=3时生效<br>1：预设审核，   0：不审核 |
| 库存不足则不审核 | insufficient\_stock\_not\_pre\_check | Int |  | 否 | 仅在order\_type=3时生效，默认：审核，  0：不审核 |
| 审核时间 | pre\_time | String |  | 否 | 仅在order\_type=3时生效, 格式: yyyy-MM-dd HH:mm, 时间要大于当前服务器时间2分钟以上 |
| 备注 | remark | String |  | 否 | 默认为空 |
| 是否审核单据 | is\_check | Int |  | 否 | 1：审核，   0：不审核<br>默认0不审核 |

**detailList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String |  | 是 | 商家编码 |
| 实体仓编号 | warehouse\_no | String |  | 是 | 实体仓编号 |
| 入库数量 | num | BigDecimal<19,4> |  | 否 | 入库数量，默认为1 |
| 成本 | price | BigDecimal<19,4> |  | 否 | 成本，默认为0 |
| 采购在途数量 | purchase\_num | BigDecimal<19,4> |  | 否 | 采购在途数量，默认为0 |
| 自定义数量 | factory\_num | BigDecimal<19,4> |  | 否 | 自定义数量，默认为0 |

**4.响应参数**

**返回值为一个Map<String, Object>**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | 是 | 结果信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回信息 | message | String |  | 是 | 如果创建成功message内容为单号，否则为错误信息 |
| 状态码 | status | Int |  | 是 | 0：操作全部成功<br>20：审核失败 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.create#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.create#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.create#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.create#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"virtual_warehouse_no"``:``"yxfxnc001"``,`<br>```"order_type"``: 3,`<br>```"to_virtual_warehouse_no"``:``"gyy001"``,`<br>```"is_pre_check"``:``true``,`<br>```"insufficient_stock_not_pre_check"``:``true``,`<br>```"pre_time"``:``"2022-04-09 11:11"``,`<br>```"remark"``:``"api_test"``,`<br>```"is_check"``: 0`<br>`},`<br>`[{`<br>```"warehouse_no"``:``"lzx"``,`<br>```"spec_no"``:``"all3"``,`<br>```"num"``: 2,`<br>```"purchase_num"``: 2,`<br>```"factory_num"``: 2,`<br>```"price"``: 5`<br>`}]]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$order``=``new``stdClass();`<br>`$order``->virtual_warehouse_no =``'yxfxnc001'``;`<br>`$order``->order_type = 4;`<br>`$order``->to_virtual_warehouse_no =``'gyy001'``;`<br>`$order``->is_pre_check = true;`<br>`$order``->insufficient_stock_not_pre_check = false;`<br>`$order``->pre_time =``'2022-04-09 11:11'``;`<br>`$order``->remark =``'api_test'``;`<br>`$order``->is_check = true;`<br>`$detail``=``new``stdClass();`<br>`$detail``->warehouse_no =``'lzx'``;`<br>`$detail``->spec_no =``'all3'``;`<br>`$detail``->num = 2;`<br>`$detail``->purchase_num = 3;`<br>`$detail``->factory_num = 4;`<br>`$detail``->price = 5;`<br>`$detailList``=``array``();`<br>`array_push``(``$detailList``,``$detail``);`<br>`try``{`<br>```$response``=``$client``->call(``"setting.strategy.VirtualWarehouse.create"``,``$order``,``$detailList``);`<br>```echo``json_encode(``$response``, JSON_PRETTY_PRINT);`<br>`}``catch``(exception``$e``)`<br>`{`<br>```echo``"exception info:"``.``$e``->getMessage();`<br>`}`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.create#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"message"``:``"VO202203290031"``,`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.create#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"虚拟仓不存在:lzx"` |
