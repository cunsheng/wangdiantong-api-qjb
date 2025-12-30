---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.query"
title: "API文档"
---
**setting.strategy.VirtualWarehouse.query** **（虚拟仓信息查询)**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP虚拟仓、店铺、实体仓关联信息 |
| **1.2 适用版本：** 客户端 V1.5.9.4 及以上版本 |
| **1.3 增量获取：** |
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
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 否 | 虚拟仓编号 |
| 实体仓编号 | sys\_warehouse\_no | String |  | 否 | 实体仓编号 |

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
| 单据信息 | data | Map<String, Object> |  | 是 | 单据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据 | detail\_list | List<Map<String, Object>> |  | 是 | 明细数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 是 | 虚拟仓编号 |
| 虚拟仓id | virtual\_warehouse\_id | Int |  | 是 | 虚拟仓唯一键 |
| 虚拟仓名称 | name | String |  | 是 | 虚拟仓名称 |
| 实体仓列表 | sys\_warehouse\_list | List<Map<String, Object>> |  | 否 | 实体仓列表 |
| 店铺列表 | shop\_list | List<Map<String, Object>> |  | 否 | 店铺列表 |

**sys\_warehouse\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 实体仓id | warehouse\_id | byte |  | 是 | 实体仓唯一键 |
| 实体仓名称 | warehouse\_name | String |  | 是 | 实体仓名称 |
| 实体仓编号 | warehouse\_no | String |  | 是 | 实体仓编号 |

**shop\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺id | shop\_id | byte |  | 是 | 店铺唯一键 |
| 店铺名称 | shop\_name | String |  | 是 | 店铺名称 |
| 店铺编号 | shop\_no | String |  | 是 | 店铺编号 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.query#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.query#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.query#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.query#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"virtual_warehouse_no"``:``"3221342131"``,``"sys_warehouse_no"``:``"testcsyc"``}]` |

|     |     |
| --- | --- |
|  | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-02-03 17:15:17"``;`<br>`$parMap``->end_time =``"2020-02-03 17:55:17"``;`<br>`$parMap``->virtual_warehouse_no =``""``;`<br>`$parMap``->warehouse_no =``""``;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"setting.strategy.VirtualWarehouse.warehouseSearch"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.query#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"detail_list"``: [`<br>```{`<br>```"virtual_warehouse_id"``: 86,`<br>```"virtual_warehouse_no"``:``"3221342131"``,`<br>```"name"``:``"312321321"``,`<br>```"shop_id_list"``:``""``,`<br>```"sys_warehouse_list"``: [`<br>```{`<br>```"warehouse_no"``:``"testcsyc"``,`<br>```"warehouse_name"``:``"testcsyc"``,`<br>```"warehouse_id"``: 717`<br>```}`<br>```],`<br>```"shop_list"``: [`<br>```]`<br>```}`<br>```]`<br>```},`<br>```"status"``: 0`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.query#autoTab1_0)
