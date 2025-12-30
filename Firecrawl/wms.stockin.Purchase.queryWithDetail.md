---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.queryWithDetail"
title: "API文档"
---
**wms.stockin.Purchase.queryWithDetail** **（采购入库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP内的采购入库单 |
| **1.2 适用版本：** 客户端 V1.4.5.8及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限、供应商权限。** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | Y | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | Y | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式 [点击这里](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E6%B5%8B%E8%AF%95/%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83%E5%8F%82%E6%95%B0%E4%BF%A1) |
| 盐 | salt | String |  | Y | 由旺店通分配appsecret，是由两部分构成, 冒号前面的部分是secret, 冒号后面的部分是salt. 例如一个appsecret是testsecret:testsalt, 那么secret为testsecret, salt为testsalt. |
| 接口名称 | method | String |  | Y | 调用的接口名称 |
| 版本号 | v | String |  | Y | 1.0 |
| 秒级时间戳 | timestamp | int |  | Y | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | Y | 签名 |
| 分页大小 | page\_size | int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 入库单修改时间,  yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | Y | 入库单修改时间，结束时间 |
| 入库单状态 | status | String | 40 | N | 英文逗号拼接的状态值:<br>10=已取消；20=编辑中；30=待审核；37=待质检；40=质检确认；80=已完成 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 入库单号 | stockin\_no | String | 20 | N | 入库单号 |
| 采购单号 | purchase\_no | String | 20 | N | 采购单号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | N | 库存相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 入库单相关数据 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单唯一键 |
| 入库单号 | order\_no | String | 40 | Y | 入库单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 状态 | status | Int | 4 | Y | 入库单状态<br>10:已取消,20编辑中,30:待审核,37:待质检,40:质检确认,80:已完成 |
| 修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 制单时间 | created\_time | String | 40 | Y | 制单时间 |
| 备注 | remark | String | 255 | Y | 入库单备注 |
| 入库单物流类型 | logistics\_type\_name | Strng |  | Y | 入库单物流类型 |
| 审核时间 | check\_time | String | 40 | Y | 入库单审核时间 |
| 采购单id | purchase\_id | Int | 11 | Y | 采购单唯一键 |
| 采购单号 | purchase\_no | String | 20 | Y | 采购单号 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 供应商编号 | provider\_no | String | 20 | Y | 供应商编号 |
| 供应商名称 | provider\_name | String | 64 | Y | 供应商名称 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 物流公司 | logistics\_name | String | 32 | Y | 物流公司 |
| 货品总价格，不包含优惠 | goods\_amount | Decimal(19,4) |  | Y | 货品总价格，不包含优惠 |
| 税前总货款（折后） | total\_price | Decimal(19,4) |  | Y | 税前总货款（折后） |
| 税后总额（折后） | tax\_amount | Decimal(19,4) |  | Y | 税后总额（折后） |
| 入库总金额 | total\_stockin\_price | Decimal(19,4) |  | Y | 明细入库价\*数量之和 |
| 标记名称 | flag\_name | String | 32 | Y | 标记名称 |
| 经办人 | operator\_name | String | 50 | Y | 经办人 |
| 入库单明细 | details\_list | List<Map<String, Object>> |  | Y | 入库单明细 |

**details\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单明细id | rec\_id | Int | 11 | Y | 入库单明细id |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 折扣 | discount | Decimal(19,4) |  | Y | 折扣 |
| 税前单价 | cost\_price | Decimal(19,4) |  | Y | 税前单价 |
| 税前折后单价 | src\_price | Decimal(19,4) |  | Y | 税前折后单价 |
| 税后单价 | tax\_price | Decimal(19,4) |  | Y | 税后单价（折后） |
| 税后金额（税后总价） | tax\_amount | Decimal(19,4) |  | Y | 税后金额（税后总价） |
| 税率 | tax | Decimal(19,4) |  | Y | 税率 |
| 税前金额（税前总价） | total\_cost | Decimal(19,4) |  | Y | 税前金额（税前总价） |
| 入库单明细备注 | remark | String | 255 | Y | 入库单明细备注 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 采购明细自定义属性1 | prop1 | String | 40 | Y | 采购明细自定义属性1 |
| 采购明细自定义属性2 | prop2 | String | 40 | Y | 采购明细自定义属性2 |
| 采购明细自定义属性3 | prop3 | String | 40 | Y | 采购明细自定义属性3 |
| 采购明细自定义属性4 | prop4 | String | 40 | Y | 采购明细自定义属性4 |
| 规格名称 | spec\_name | String | 255 | Y | 规格名称 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 单位 | unit\_name | String | 20 | Y | 基本单位 |
| 批次 | batch\_no | String | 50 | Y | 若无批次则返回空字符串 |
| 有效期 | expire\_date | String | 40 | Y | 若无有效期则返回空字符串 |
| 生产日期 | production\_date | String | 40 | Y | 若无生产日期则返回空字符串 |
| 货位 | position\_no | String | 20 | Y | 货位 |
| 是否残品 | defect | bool |  | Y | 是否残品<br>true：是<br>false：否 |
| 换算系数 | unit\_ratio | Decimal(19,4) |  | Y | 换算系数 |
| 辅助单位 | purchase\_unit\_name | String | 20 | Y | 辅助单位 |
| 入库价 | stockin\_price | Decimal(19,4) |  | Y | 入库价 |

**5.请求示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.queryWithDetail#autoTab5_0)
- [php](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Purchase.queryWithDetail#autoTab5_3)

```
[{\
       "start_time":   "2024-04-20 00:00:00",\
       "end_time":   "2024-04-22 00:00:00"\
}]
```

```
<?php
header("Content-Type: text/html;   charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url",   "wdtapi3", "appkey", "secret");
$paraMap = new stdClass();
$paraMap->start_time =   "2024-04-20 00:00:00";
$paraMap->end_time =   "2024-04-222 00:00:00";

$pager = new Pager(1, 0, true);
$response =   $client->pageCall("wms.stockin.Purchase.queryWithDetail",$pager, $paraMap);

?>
```

```

```

```

```

**6.响应示例**

**6.1正常响应示例**

|     |     |
| --- | --- |
| json | ```<br>{<br>	"status": 0,<br>	"data": {<br>		"total_count": 1,<br>		"order": [{<br>			"order_no": "RK2023022121",<br>			"logistics_name": "采购专用物流",<br>			"details_list": [{<br>				"rec_id": 211428,<br>				"num": 5,<br>				"discount": 0.9,<br>				"cost_price": 5,<br>				"src_price": 4.5,<br>				"tax_price": 4.5,<br>				"tax_amount": 22.5,<br>				"tax": 0,<br>				"total_cost": 22.5,<br>				"remark": "",<br>				"goods_name": "wangdiantong",<br>				"goods_no": "wangdiantong",<br>				"spec_no": "wangdiantong",<br>				"spec_name": "暂无",<br>				"position_no": "采购未上架",<br>				"unit_ratio": 3,<br>				"batch_no": "",<br>				"stockin_price": 4.5,<br>				"expire_date": "",<br>				"defect": false,<br>				"production_date": "",<br>				"prop1": "",<br>				"prop2": "",<br>				"prop3": "",<br>				"prop4": "",<br>				"brand_name": "发发拉",<br>				"purchase_unit_name": "哒哒哒哒哒",<br>				"unit_name": "箱",<br>				"spec_code": "123"<br>			}, {<br>				"rec_id": 211429,<br>				"num": 5,<br>				"discount": 0.8,<br>				"cost_price": 19.3,<br>				"src_price": 15.44,<br>				"tax_price": 15.44,<br>				"tax_amount": 77.2,<br>				"tax": 0,<br>				"total_cost": 77.2,<br>				"remark": "",<br>				"goods_name": "王小卤01",<br>				"goods_no": "wxl0001",<br>				"spec_no": "wxl0001",<br>				"spec_name": "",<br>				"position_no": "采购未上架",<br>				"unit_ratio": 1,<br>				"batch_no": "",<br>				"stockin_price": 15.44,<br>				"expire_date": "",<br>				"defect": false,<br>				"production_date": "",<br>				"prop1": "",<br>				"prop2": "",<br>				"prop3": "",<br>				"prop4": "",<br>				"brand_name": "无",<br>				"purchase_unit_name": "无",<br>				"unit_name": "袋",<br>				"spec_code": "1111"<br>			}],<br>			"tax_amount": 99.7,<br>			"purchase_no": "RH23022111",<br>			"remark": "",<br>			"goods_count": 10,<br>			"flag_name": "无",<br>			"warehouse_no": "wdtapi3-test",<br>			"total_stockin_price": "99.70000000",<br>			"modified": 1676964121000,<br>			"provider_name": "秋天001",<br>			"provider_no": "20170808002",<br>			"seq_no": 1,<br>			"created_time": 1676964112000,<br>			"stockin_id": 89343,<br>			"total_price": 99.7,<br>			"logistics_no": "",<br>			"goods_amount": "121.50000000",<br>			"purchase_id": 8606,<br>			"operator_name": "aaa",<br>			"logistics_type_name": "未知",<br>			"status": 80,<br>			"check_time": 1676964121000<br>		}]<br>	}<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "code": 2102,<br>    "message": "start_time和end_time为空或不是有效的时间格式[0000-00-00 00:00:00] "<br>}<br>``` |
