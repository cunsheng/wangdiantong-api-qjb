---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.queryWithDetail"
title: "API文档"
---
**wms.stockin.Transfer.queryWithDetail** **（调拨入库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP调拨入库单单据信息 |
| **1.2 适用版本：** 客户端 V1.6.0.10及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

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
| 开始时间 | start\_time | String | 40 | Y | 修改起始时间，若无入库单号或调拨单号，则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 修改结束时间，上同开始时间 |
| 入库单状态 | status | String | 255 | N | 英文逗号拼接的状态值: <br>10=已取消，<br>20=编辑中，<br>30=待审核，<br>37=待质检，<br>40=质检确认，<br>80=已完成 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 入库单号 | stockin\_no | String | 20 | N | 入库单号 |
| 调拨单号 | transfer\_no | String | 40 | N | 调拨单号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 入库单相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 入库单相关数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单id |
| 入库单号 | order\_no | String | 20 | Y | 入库单号 |
| 建单时间 | created\_time | String | 40 | Y | 建单时间 |
| 入库单审核时间 | check\_time | String | 40 | Y | 入库单审核时间 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 入库单备注 | remark | String | 255 | Y | 入库单备注 |
| 调拨单号 | src\_order\_no | String | 20 | Y | 调拨单号 |
| 调拨单创建时间 | st\_created | String | 40 | Y | 调拨单创建时间 |
| 入库单状态 | status | Int |  | Y | 入库单状态<br>10=已取消，<br>20=编辑中，<br>30=待审核，<br>37=待质检，<br>40=质检确认，<br>80=已完成 |
| 入库单入库数量 | goods\_count | Decimal(19,4) |  | Y | 入库单入库数量 |
| 源仓库编号 | from\_warehouse\_no | String | 40 | Y | 源仓库编号 |
| 源仓库名称 | from\_warehouse\_name | String | 64 | Y | 源仓库名称 |
| 目标仓库编号 | to\_warehouse\_no | String | 40 | Y | 目标仓库编号<br>调拨停止等待并回补库存时生成的入库单仓库编号为调拨单源仓 |
| 目标仓库名称 | to\_warehouse\_name | String | 64 | Y | 目标仓库名称<br>调拨停止等待并回补库存时生成的入库单仓库编号为调拨单源仓 |
| 经办人 | operator\_name | String | 40 | Y | 经办人 |
| 总成本价 | total\_price | Decimal(19,4) | 6 | Y | 总成本价 |
| 物流类型 | logistics\_type | Int | 11 | Y | 物流类型，点击查看 [物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb)（当物流名称为空时不返回此字段） |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 物流公司名称 | logistics\_name | String | 40 | Y | 物流公司名称（当物流名称为空时不返回此字段） |
| 物流公司编号 | logistics\_code | String | 60 | Y | 物流公司编号（系统物流公司编号,当物流名称为空时不返回此字段） |
| 调拨单id | transfer\_id | Int | 11 | Y | 调拨单id |
| 入库单明细 | detail\_list | List<Map<String, Object>> |  | Y | 入库单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int | 11 | Y | 入库单id |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 总成本价 | total\_cost | Decimal(19,4) |  | Y | 总成本价（审核时成本\*数量） |
| 入库单明细备注 | remark | String | 255 | Y | 入库单明细备注 |
| 校准数量 | right\_num | Decimal(19,4) |  | Y | 校准数量 |
| 入库明细唯一id | rec\_id | Int | 11 | Y | 入库明细唯一id |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 自定义属性2 | prop2 | String | 255 | Y | 自定义属性2（货品档案单品自定义属性2） |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 品牌编号 | brand\_no | String | 32 | Y | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 基本单位 | goods\_unit | String | 20 | Y | 基本单位 |
| 是否残次品 | defect | bool | 1 | Y | true：残次品<br>false：正品 |
| 批次号 | batch\_no | String | 40 | Y | 如果没有则返回空字符串 |
| 有效期 | expire\_date | String | 40 | Y | 如果没有则返回空字符串 |
| 生产日期 | production\_date | String | 40 | Y | 如果没有则返回空字符串 |
| 货位编号 | position\_no | String | 20 | Y | 货位编号 |
| 调拨单明细id | src\_order\_detail\_id | Int | 11 | Y | 调拨单明细id |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Transfer.queryWithDetail#autoTab5_3)

```
[{\
       "start_time": "2020-01-01 00:00:00",\
       "end_time": "2020-01-20 00:00:00"\
}]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$parMap = new stdClass();
$parMap->start_time = "2020-01-01 00:00:00";
$parMap->end_time = "2020-01-20 00:00:00";

$pager = new Pager(1, 0, true);

$response = $client->pageCall("wms.stockin.Transfer.queryWithDetail", $pager, $parMap);

?>
```

```

```

```

```

**6.响应示** **例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "total_count": 1,<br>        "order": [{<br>            "order_no": "RK2022122922",<br>            "logistics_name": "ceshi-004其它业务",<br>            "created_time": 1672279105000,<br>            "from_warehouse_name": "wdtapi3-test",<br>            "stockin_id": 88501,<br>            "total_price": 0,<br>            "to_warehouse_id": 630,<br>            "logistics_no": "455611258884",<br>            "detail_list": [{<br>                "stockin_id": 88501,<br>                "num": 1,<br>                "remark": "",<br>                "right_num": 1,<br>                "rec_id": 209941,<br>                "defect": false,<br>                "goods_name": "相印",<br>                "goods_no": "xiangyin",<br>                "spec_no": "xiangyin01",<br>                "prop2": "",<br>                "spec_name": "",<br>                "spec_code": "xiangyin01",<br>                "brand_no": "BRAND",<br>                "brand_name": "无",<br>                "goods_unit": "箱",<br>                "batch_no": "",<br>                "total_cost": 0,<br>                "expire_date": "",<br>                "production_date": "",<br>                "position_no": "其它未上架"<br>            }],<br>            "remark": "",<br>            "goods_count": 1,<br>            "logistics_code": "ceshi-004",<br>            "src_order_no": "TF2212290044",<br>            "from_warehouse_no": "wdtapi3-test",<br>            "from_warehouse_id": 624,<br>            "operator_name": "aaa",<br>            "to_warehouse_name": "wdtapi3-test2",<br>            "st_created": 1672279097000,<br>            "modified": 1672279105000,<br>            "logistics_type": 5,<br>            "check_time": 1672279105000,<br>            "status": 80,<br>            "to_warehouse_no": "wdtapi3-test2"<br>        }]<br>    }<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>       "status": 100,<br>       "message": "仓库不存在"<br>}<br>``` |
