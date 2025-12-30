---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch"
title: "API文档"
---
**setting.strategy.VirtualWarehouse.stockSearch** **（虚拟仓库存查询)**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP虚拟仓库存信息 |
| **1.2 适用版本：** 客户端 V1.5.6.2及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：**start\_time与end\_time时间跨度不超过30天 |
| **1.5注意事项：权限校验：【仓库和虚拟仓权限】** |

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
| 开始时间 | start\_time | String | 40 | 否 | 修改时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | 否 | yyyy-MM-dd HH:mm:ss格式 |
| 商家编码 | spec\_nos | String |  | 否 | 英文逗号分割,最多500个; 不填时间条件时必填 |
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 否 | 虚拟仓编号 |
| 实体仓编号 | warehouse\_no | String |  | 否 | 实体仓编号 |

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
| 最小警戒库存 | alarm\_num | Decimal(19,4) |  | 是 | 最小警戒库存 |
| 已分配数 | assigned\_num | Decimal(19,4) |  | 是 | 已分配数 |
| 公有仓可用数 | avaliable\_num | Decimal(19,4) |  | 是 | 公有仓可用数 |
| 可发数 | can\_use\_lock\_num | Decimal(19,4) |  | 是 | 可发数 |
| 可用数 | can\_use\_num | Decimal(19,4) |  | 是 | 可用数 |
| 自定义数量 | factory\_num | Decimal(19,4) |  | 是 | 自定义数量 |
| 虚拟仓警戒库存 | lock\_num | Decimal(19,4) |  | 是 | 虚拟仓警戒库存 |
| 货品名称 | goods\_name | String |  | 是 | 货品名称 |
| 货品编号 | goods\_no | String |  | 是 | 货品编号 |
| 当前锁定数（入库数量） | now\_lock\_num | Decimal(19,4) |  | 是 | 当前锁定数（入库数量） |
| 14天销量 | num\_14days | Decimal(19,4) |  | 是 | 14天销量 |
| 7天销量 | num\_7days | Decimal(19,4) |  | 是 | 7天销量 |
| 今日销量 | num\_day | Decimal(19,4) |  | 是 | 今日销量 |
| 月销量 | num\_month | Decimal(19,4) |  | 是 | 月销量 |
| 昨日销量 | num\_yesterday | Decimal(19,4) |  | 是 | 昨日销量 |
| 已出库数 | out\_num | Decimal(19,4) |  | 是 | 已出库数 |
| 总锁定数 | sum\_lock\_num | Decimal(19,4) |  | 是 | 总锁定数 |
| 明细id | rec\_id | Int |  | 是 | 唯一键 |
| 商家编码 | spec\_no | String |  | 是 | 商家编码 |
| 规格名称 | spec\_name | String |  | 是 | 规格名称 |
| 虚拟仓名称 | vir\_warehouse\_name | String |  | 是 | 虚拟仓名称 |
| 虚拟仓编号 | vir\_warehouse\_no | String |  | 是 | 虚拟仓编号 |
| 仓库名称 | warehouse\_name | String |  | 是 | 仓库名称 |
| 仓库编号 | warehouse\_no | String |  | 是 | 仓库编号 |
| 仓库id | warehouse\_id | Int |  | 是 | 仓库id |
| 采购在途量 | purchase\_num | String |  | 是 | 采购在途量<br>（开启客户端系统配置：开启虚拟仓锁定预售库存功能，返回对应值，未开通下返回0） |
| 单品id | spec\_id | int |  | 是 | 单品id（系统单品主键） |
| 虚拟仓id | vir\_warehouse\_id | int |  | 是 | 虚拟仓id |
| 预计其他入库锁定量 | trial\_other\_in\_num | Decimal(19,4) |  | 是 | 预计其他入库锁定量 |
| 成本价 | avg\_cost |  |  | 是 | 成本价 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>```"start_time"``:``"2022-03-09 15:50:01"``,`<br>```"end_time"``:``"2022-03-09 15:50:58"``,`<br>```"spec_nos"``:``"4204"`<br>`}]` |

|     |     |
| --- | --- |
|  | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$paraMap``=``new``stdClass();`<br>`$paraMap``->start_time =``"2022-03-09 15:50:01"``;`<br>`$paraMap``->end_time =``"2022-03-09 15:50:58"``;`<br>`$paraMap``->spec_nos =``"4204"``;`<br>`$pager``=``new``Pager(2, 0, true);`<br>`$data``=``$client``->pageCall(``"setting.strategy.VirtualWarehouse.stockSearch"``,``$pager``,``$paraMap``);`<br>`>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 2,`<br>```"detail_list"``: [{`<br>```"alarm_num"``: 0.0000,`<br>```"trial_other_in_num"``: 0.0000,`<br>```"goods_no"``:``"4204"``,`<br>```"spec_no"``:``"4204"``,`<br>```"purchase_num"``: 0.0000,`<br>```"avaliable_num"``: 1155.0000,`<br>```"spec_id"``: 1992,`<br>```"vir_warehouse_name"``:``"daj虚拟仓"``,`<br>```"num_14days"``: 0.0000,`<br>```"out_num"``: 0.0000,`<br>```"goods_name"``:``"高筱原的水杯"``,`<br>```"lock_num"``: 10.0000,`<br>```"now_lock_num"``: 10.0000,`<br>```"num_day"``: 0.0000,`<br>```"rec_id"``: 700,`<br>```"num_month"``: 0.0000,`<br>```"can_use_lock_num"``: 10.0000,`<br>```"vir_warehouse_id"``: 5,`<br>```"can_use_num"``: 10.0000,`<br>```"factory_num"``: 0.0000,`<br>```"sum_lock_num"``: 10.0000,`<br>```"num_yesterday"``: 0.0000,`<br>```"spec_name"``:``""``,`<br>```"assigned_num"``: 0.0000,`<br>```"warehouse_id"``: 330,`<br>```"num_7days"``: 0.0000`<br>```},`<br>```{`<br>```"alarm_num"``: 0.0000,`<br>```"goods_no"``:``"4204"``,`<br>```"spec_no"``:``"4204"``,`<br>```"purchase_num"``: 0.0000,`<br>```"avaliable_num"``: 1155.0000,`<br>```"spec_id"``: 1992,`<br>```"vir_warehouse_name"``:``"gyy001"``,`<br>```"num_14days"``: 0.0000,`<br>```"out_num"``: 0.0000,`<br>```"goods_name"``:``"高筱原的水杯"``,`<br>```"lock_num"``: 21.0000,`<br>```"now_lock_num"``: 5.0000,`<br>```"num_day"``: 0.0000,`<br>```"rec_id"``: 399,`<br>```"num_month"``: 0.0000,`<br>```"can_use_lock_num"``: 5.0000,`<br>```"vir_warehouse_id"``: 10,`<br>```"can_use_num"``: 5.0000,`<br>```"factory_num"``: 0.0000,`<br>```"sum_lock_num"``: 5.0000,`<br>```"num_yesterday"``: 0.0000,`<br>```"spec_name"``:``""``,`<br>```"assigned_num"``: 0.0000,`<br>```"warehouse_id"``: 330,`<br>```"num_7days"``: 0.0000`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.stockSearch#autoTab1_0)
