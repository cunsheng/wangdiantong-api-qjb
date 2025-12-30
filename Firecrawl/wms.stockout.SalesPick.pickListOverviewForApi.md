---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.SalesPick.pickListOverviewForApi"
title: "API文档"
---
### **wms.stockout.SalesPick.pickListOverviewForApi****（分拣单全览）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内分拣波次信息 |
| **1.2 适用版本：** 客户端V1.5.3.3及以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：仓库权限。** |

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
| 波次单编号 | pick\_no | String |  | 是 | 波次单编号 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 分货信息 | data | Map<String, Object> |  | Y | 分货信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 拣货区通道长度 | aisle\_no\_len | byte |  | N | 拣货区通道长度 |
| 物流公司主键 | logistics\_id | Int |  | N | 物流公司主键 |
| 订单数量 | order\_count | Int |  | Y | 订单数量 |
| 拣货分组主键 | pick\_group\_id | Int |  | N | 拣货分组主键 |
| 分拣单号主键 | pick\_id | Int |  | Y | 分拣单号主键 |
| 分拣波次号 | pick\_no | String |  | Y | 分拣波次号 |
| 拣货方式 | pick\_type | byte |  | N | 拣货方式<br>0：边拣边分<br>1：先拣后分<br>2：电子分拣单<br>3：通道拣货<br>4：多货区拣货（拣+分）<br>5：按单放框<br>6：多货区拣货（拣->分） |
| 打印类型 | print\_type | byte |  | N | 打印类型<br>0：不打印<br>1：领取波次后立即打印<br>2：波次拣货后打印 |
| 扫描方式 | scan\_type | byte |  | N | 扫描方式<br>0：自由/默认<br>1：逐个扫描 |
| 是否进入分货 | sort | boolean |  | N | 是否进入分货 |
| 分货模式 | sort\_mode | byte |  | N | 分货模式<br>-1：默认<br>0：非动态<br>1：动态 |
| 分货方式 | sort\_type | byte |  | N | 分货方式<br>0：任意分货<br>1：一单多货分货 |
| 货区id | zone\_id | Int |  | N | 货区id |
| 货品列表 | pick\_goods\_data\_list | List<Map<String, Object>> |  | Y | 货品列表 |

**pick\_goods\_data\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 辅助单位名称 | aux\_name | String |  | Y | 辅助单位名称 |
| 条码 | barcode | String |  | Y | 条码 |
| 批次id | batch\_id | Int |  | Y | 批次id |
| 正残品 | defect | boolean |  | Y | 正残品<br>0：正品<br>1：残次品 |
| 货品名称 | goods\_name | String |  | Y | 货品名称 |
| 货品编号 | goods\_no | String |  | Y | 货品编号 |
| 图片url | img\_url | String |  | Y | 图片url |
| 货品数量 | num | Int |  | Y | 货品数量 |
| 库存货位 | possible\_position | String |  | Y | 库存货位 |
| 货品简称 | short\_name | String |  | Y | 货品简称 |
| 序列号类型 | sn\_type | byte |  | Y | 序列号类型<br>0：未开启序列号<br>1：强序列号<br>2：弱序列号 |
| 规格码 | spec\_code | String |  | Y | 规格码 |
| 规格id | spec\_id | Int |  | Y | 规格id |
| 规格名称 | spec\_name | String |  | Y | 规格名称 |
| 商家编码 | spec\_no | String |  | Y | 商家编码 |
| 基本单位名称 | unit\_name | String |  | Y | 基本单位名称 |
| 辅助单位与基本单位之间的换算关系 | unit\_ratio | BigDecimal |  | Y | 辅助单位与基本单位之间的换算关系 |
| 保质期 | validity\_days | Int |  | Y | 保质期 |
| 批次编号 | batch\_no | String |  | N | 批次编号 |
| 有效期 | expire\_date | date |  | N | 有效期 |
| 保质期计算方式 | validity\_type | Int |  | Y | 保质期计算方式<br>0：按天<br>1：按月<br>默认为0 |
| 拣货分组id | pick\_group\_id | Int |  | Y | 拣货分组id |
| 货品所在货位的信息 | position\_data | Map<String, Object> |  | Y | 货品所在货位的信息 |
| 货品其余货位的信息 | position\_list | List<Map<String, Object>> |  | Y | 货品其余货位的信息<br>注：货位分配模式为默认货位模式时不返回position\_list |
| 货品所在出库单的信息 | stockout\_list | List<Map<String, Object>> |  | Y | 货品所在出库单的信息 |

**position\_data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货位id | position\_id | Int |  | Y | 货位id |
| 货位编号 | position\_no | String |  | Y | 货位编号 |
| 货位排序编号 | sort\_no | String |  | Y | 货位排序编号 |
| 货区id | zone\_id | Int |  | Y | 货区id |
| 货区编号 | zone\_no | String |  | Y | 货区编号 |
| 货位库存明细 | stock\_detail\_list | List<Map<String, Object>> |  | Y | 货位库存明细 |

**position\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货位id | position\_id | Int |  | Y | 货位id |
| 货位编号 | position\_no | String |  | Y | 货位编号 |
| 货位排序编号 | sort\_no | String |  | Y | 货位排序编号 |
| 货区id | zone\_id | Int |  | Y | 货区id |
| 货区编号 | zone\_no | String |  | Y | 货区编号 |
| 货位库存明细 | stock\_detail\_list | List<Map<String, Object>> |  | Y | 货位库存明细 |

**stockout\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分拣序号 | index | Int |  | Y | 分拣序号 |
| 货品数量 | num | Int |  | Y | 货品数量 |
| 已分货数量 | sort\_num | Int |  | Y | 已分货数量 |
| 出库单id | stockout\_id | Int |  | Y | 出库单id |
| 物流单号 | logistics\_no | String |  | Y | 物流单号 |
| 出库单号 | stockout\_no | String |  | Y | 出库单号 |

**stock\_detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 批次id | batch\_id | Int |  | Y | 批次id |
| 批次编号 | batch\_no | String |  | Y | 批次编号 |
| 有效期 | expire\_date | date |  | Y | 有效期 |
| 库存数量 | stock\_num | Int |  | Y | 库存数量 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.SalesPick.pickListOverviewForApi#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.SalesPick.pickListOverviewForApi#autoTab0_1)

|     |     |
| --- | --- |
| 1 | `[``"FJ2104220004"``]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$pickNo``=``"FJ2104220004"``;`<br>``<br>`$data``=``$client``->call(``"wms.stockout.SalesPick.pickListOverviewForApi"``,``$pickNo``);`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.SalesPick.pickListOverviewForApi#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"data"``: {`<br>```"aisle_no_len"``: 0,`<br>```"can_hang_up"``:``false``,`<br>```"is_one_type_in_order"``:``false``,`<br>```"logistics_id"``: 0,`<br>```"order_count"``: 1,`<br>```"pick_goods_data_list"``: [`<br>```{`<br>```"aux_name"``:``"盒（10）"``,`<br>```"barcode"``:``"11111111"``,`<br>```"batch_id"``: 0,`<br>```"contain_num"``: 1,`<br>```"defect"``:``false``,`<br>```"goods_name"``:``"货品名称"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"img_url"``:``""``,`<br>```"num"``: 2,`<br>```"pick_group_id"``: 0,`<br>```"position_data"``: {`<br>```"position_id"``: 64229,`<br>```"position_no"``:``"B01-01"``,`<br>```"sort_no"``:``"B01-01"``,`<br>```"stock_detail_list"``: [`<br>```{`<br>```"batch_id"``: 1724,`<br>```"batch_no"``:``"PC2303270004"``,`<br>```"expire_date"``: 1722009600000,`<br>```"stock_num"``: 1189`<br>```}`<br>```],`<br>```"zone_id"``: 663,`<br>```"zone_no"``:``"J"`<br>```},`<br>```"position_list"``: [`<br>```{`<br>```"position_id"``: 64231,`<br>```"position_no"``:``"B01-02"``,`<br>```"sort_no"``:``"B01-02"``,`<br>```"stock_detail_list"``: [`<br>```{`<br>```"batch_id"``: 1722,`<br>```"batch_no"``:``"PC2303270002"``,`<br>```"stock_num"``: 40`<br>```}`<br>```],`<br>```"zone_id"``: 663,`<br>```"zone_no"``:``"J"`<br>```}`<br>```],`<br>```"possible_position"``:``""``,`<br>```"short_name"``:``""``,`<br>```"sn_type"``: 0,`<br>```"spec_code"``:``"wangdiantong"``,`<br>```"spec_id"``: 1,`<br>```"spec_name"``:``"测试产品"``,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"stockout_list"``: [`<br>```{`<br>```"index"``: 1,`<br>```"logistics_no"``:``"14454584112210"``,`<br>```"num"``: 2,`<br>```"sort_num"``: 0,`<br>```"stockout_id"``: 520062,`<br>```"stockout_no"``:``"CK202303274"`<br>```}`<br>```],`<br>```"unit_name"``:``"只"``,`<br>```"unit_ratio"``: 10.0000,`<br>```"validity_days"``: 0,`<br>```"validity_type"``: 0`<br>```}`<br>```],`<br>```"pick_group_id"``: 0,`<br>```"pick_id"``: 4023,`<br>```"pick_no"``:``"FJ2303270001"``,`<br>```"pick_type"``: 0,`<br>```"print_type"``: 2,`<br>```"scan_type"``: 0,`<br>```"sort"``:``false``,`<br>```"sort_mode"``: 0,`<br>```"sort_type"``: 0,`<br>```"zone_id"``: 0`<br>```},`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.SalesPick.pickListOverviewForApi#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"分拣单不存在"``}` |
