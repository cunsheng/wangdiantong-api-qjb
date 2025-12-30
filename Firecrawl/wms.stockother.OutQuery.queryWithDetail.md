---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.OutQuery.queryWithDetail"
title: "API文档"
---
**wms.stockother.OutQuery.queryWithDetail** **（** **其它出库业务单查询** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**获取ERP其他出库业务单信息 |
| **1.2 适用版本：** 客户端 V1.5.4.3及以上版本 |
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
| 时间类型 | time\_type | Int | 40 |  | 1：创建时间；<br>2：最后修改时间<br>不传默认为创建时间 |
| 开始时间 | start\_time | String | 40 | Y | 起始时间，若无业务单号，则为必填。<br>yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间，上同开始时间. |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 业务单号 | other\_out\_no | String | 40 | N | 业务单号 |
| 业务单据状态 | status | string | 4 | N | 业务单据状态：<br>1:编辑中;<br>10:待审核;<br>20:已审核;<br>40:已推送wms;<br>60:部分出库;<br>65:待结算;<br>70:已完成;<br>80:已取消 |
| 模糊查询 | fuzzy\_query | boolean | 1 | N | 默认false,业务单号进行模糊查询匹配，匹配数量大于1条时会报错 |

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
| 单据数据 | data | Map<String, Object> |  | Y | 单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 出库单相关数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**Order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务单id | rec\_id | Int | 11 | Y | 业务单id |
| 业务单编号 | other\_out\_no | String | 40 | Y | 业务单编号 |
| 状态 | status | Int | 4 | Y | 状态：<br>1:编辑中;<br>10:待审核;<br>20:已审核;<br>40:已推送wms;<br>60:部分出库;<br>65:待结算;<br>70:已完成;<br>80:已取消 |
| 出库的仓库编号 | warehouse\_no | String | 40 | Y | 出库的仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称 |
| 仓库id | warehouse\_id | Int | 6 | Y | 仓库id |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 物流名称 | logistics\_name | String |  | Y | 物流名称 |
| 物流id | logistics\_id | Int | 6 | Y | 物流id |
| 收件人姓名 | receiver\_name | varchar | 40 | Y | 收件人姓名 |
| 收货省份 | receiver\_province | String | 40 | Y | 收货省份 |
| 收货城市 | receiver\_city | String | 40 | Y | 收货城市 |
| 收货区县 | receiver\_district | String | 40 | Y | 收货区县 |
| 收件地址 | receiver\_address | String | 256 | Y | 收件地址 |
| 收件电话 | receiver\_mobile | String | 40 | Y | 收件电话 |
| 库存占用 | is\_reserved | bool |  | Y | 是：true<br>否：false |
| 出库单备注 | remark | String | 255 | Y | 出库单备注 |
| 制单人 | employee\_name | String | 40 | Y | 制单人 |
| 便签条数 | note\_count | Int | 4 | Y | 便签条数 |
| 出库原因 | reason | String | 255 | Y | 出库原因 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间 |
| 其他出库业务单自定义属性1 | prop1 | String | 255 | N | 其他出库业务单自定义属性1 |
| 其他出库业务单自定义属性2 | prop2 | String | 255 | N | 其他出库业务单自定义属性2 |
| 其他出库业务单自定义属性3 | prop3 | String | 255 | N | 其他出库业务单自定义属性3 |
| 其他出库业务单自定义属性4 | prop4 | String | 255 | N | 其他出库业务单自定义属性4 |
| 其他出库业务单自定义属性5 | prop5 | String | 255 | N | 其他出库业务单自定义属性5 |
| 其他出库业务单自定义属性6 | prop6 | String | 255 | N | 其他出库业务单自定义属性6 |
| wms单号 | outer\_no | String |  | N | wms单号（奇门自定义场景无此字段返回） |
| 业务单明细 | detail\_list | List<Map<String, Object>> |  | Y | 业务单明细 |

detail\_list

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务单详情id | rec\_id | Int | 11 | Y | 业务单详情id |
| 业务单id | other\_out\_id | Int | 11 | Y | 业务单id |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | Y | 辅助数量 |
| 已出库数量 | out\_num | Decimal(19,4) |  | Y | 已出库数量 |
| 有效期 | expire\_date | String | 40 | Y | 指定出库货品有效期 |
| 出库业务单详情备注 | remark | Sting | 64 | Y | 出库业务单详情备注 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品id | goods\_id | Int | 11 | Y | 货品id |
| 单品id | spec\_id | Int | 11 | Y | 单品id |
| 货品编码 | goods\_no | String | 40 | Y | 货品编码 |
| 货品简称 | short\_name | String | 40 | Y | 货品简称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 条码 | barcode | String | 40 | Y | 条码 |
| 是否残次品 | defect | boolean | 1 | Y | true:  残次品<br>false:  正品 |
| 修改时间 | modified\_date | String |  | Y | 修改时间 |
| 创建时间 | created\_date | String |  | Y | 创建时间 |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 生产日期 | production\_date | String |  | Y | 生产日期 |
| 单价 | price | Decimal(19,4) |  | Y | 单据明细上记录的单价（奇门自定义接口不返回） |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.OutQuery.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.OutQuery.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.OutQuery.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockother.OutQuery.queryWithDetail#autoTab5_3)

```
[{"start_time":"2020-10-23 00:00:00","end_time":"2020-11-22 00:00:00"}]
```

```
<?php
include 'wdtsdk.php';

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")

$parMap = new stdClass();
$parMap->start_time = "2020-10-23 00:00:00";
$parMap->end_time = "2020-11-22 00:00:00";

$pager = new Pager(1, 0, true);
$data = $client->pageCall("wms.stockother.OutQuery.queryWithDetail", $pager, $parMap);
$php_json = json_encode($data);

?>
```

**6.响应示** **例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "total_count": 1,<br>        "order": [<br>            {<br>                "logistics_name": "无",<br>                "reason": "无",<br>                "receiver_city": "",<br>                "detail_list": [<br>                    {<br>                        "rec_id": 41697,<br>                        "other_out_id": 10853,<br>                        "num": 1,<br>                        "num2": 1,<br>                        "defect": false,<br>                        "batch_no": "",<br>                        "expire_date": "",<br>                        "remark": "",<br>                        "spec_id": 1,<br>                        "goods_id": 1,<br>                        "goods_name": "wangdiantong",<br>                        "short_name": "",<br>                        "goods_no": "wangdiantong",<br>                        "spec_code": "wangdiantong",<br>                        "modified_date": "2024-09-24 16:27:08",<br>                        "created_date": "2024-09-24 16:27:08",<br>                        "spec_name": "wangdiantong",<br>                        "spec_no": "wangdiantong",<br>                        "barcode": "11111111",<br>                        "out_num": 0,<br>                        "price": 0,<br>                        "production_date": "2024-09-10"<br>                    }<br>                ],<br>                "remark": "",<br>                "logistics_id": 0,<br>                "is_reserved": false,<br>                "warehouse_no": "wdtapi3-test",<br>                "modified": 1727166428000,<br>                "receiver_name": "",<br>                "note_count": 0,<br>                "receiver_province": "",<br>                "other_out_no": "QC202409240008",<br>                "logistics_no": "",<br>                "created": 1727166428000,<br>                "receiver_district": "",<br>                "employee_name": "wdtapi3-test2",<br>                "rec_id": 10853,<br>                "prop6": "",<br>                "prop5": "",<br>                "receiver_mobile": "",<br>                "prop4": "",<br>                "prop3": "",<br>                "prop2": "",<br>                "prop1": "",<br>                "warehouse_name": "wdtapi3-test",<br>                "receiver_address": "",<br>                "warehouse_id": 311,<br>                "status": 10<br>            }<br>        ]<br>    }<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json | ```<br>{"status":100,"message":"您的查询时间过宽,查询时间不能大于30天"}<br>``` |
