---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.jit.JitRefund.search"
title: "API文档"
---
**sales.jit.JitRefund.search（JIT退货单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的JIT退货单据信息 |
| **1.2 适用版本：** 客户端 V1.4.7.9及以上版本 |
| **1.3 增量获取：**按照最后修改时间返回 |
| **1.4 时间跨度：** 起止时间跨度不超过30天 |
| **1.5注意事项：** |

**2.调用场** **景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

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
| 查询参数 | params | Map<String, Object> |  | y | 查询参数 |
| 分页 | pager | pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | n | 起始时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | n | 结束时间, yyyy-MM-dd HH:mm:ss格式 |
| 平台退货单号 | jit\_refund\_no | String | 50 | n | 平台退货单号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小 |
| 页号 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 返回0为正常 |
| 错误信息 | message | String |  | n | 无错误信息不返回 |
| 退货单信息 | data | Map<String, Object> |  | n | 退货单信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | y | JIT退货单相关数据 |
| 总数 | total\_count | Int | 11 | n | 查询条件总数单据 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退货单唯一键 | rec\_id | Int | 11 | y | 退货单唯一键 |
| 退货单号 | refund\_no | String | 50 | y | 退货单号 |
| 状态 | status | Int | 6 | y | 状态<br>5：已取消<br>10：待递交<br>20：递交失败<br>25：待审核<br>30：已审核<br>33：待推送<br>35：已推送<br>40：部分入库<br>50：已完成 |
| 店铺主键id | shop\_id | Int | 11 | y | 店铺主键id |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 平台退货单号 | jit\_refund\_no | String | 50 | y | 平台退货单号 |
| 唯品会出库仓库编号 | jit\_warehouse | String | 50 | y | 唯品会出库仓库编号 |
| 收货仓仓库编号 | warehouse\_no | String | 40 | y | 收货仓仓库编号 |
| 收货仓仓库id | warehouse\_id | String |  | y | 收货仓仓库id（奇门自定义接口不返回） |
| 退货类型 | refund\_type | String | 30 | y | 退货类型 |
| 退款方式 | pay\_type | String | 20 | y | 退款方式 |
| 收件人姓名 | receiver | String | 30 | y | 收件人姓名 |
| 收件人国家 | country | String | 30 | y | 收件人国家 |
| 收件人省份 | state | String | 30 | y | 收件人省份 |
| 收件人城市 | city | String | 30 | y | 收件人城市 |
| 收件人区县 | region | String | 30 | y | 收件人区县 |
| 收件人街道 | town | String | 50 | y | 收件人街道 |
| 收件人地址 | address | String | 255 | y | 收件人地址 |
| 收件人电话 | telephone | String | 30 | y | 收件人电话 |
| 收件人手机 | mobile | String | 30 | y | 收件人手机 |
| 送货方式 | self\_reference | String | 30 | y | 送货方式 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量 |
| 货品种类 | goods\_type | Int | 6 | y | 货品种类 |
| 最后修改时间 | modified | String |  | y | 格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String |  | y | 格式: yyyy-MM-dd HH:mm:ss |
| 退货单明细列表 | detail\_list | List<Map<String, Object>> |  | y | 退货单明细列表 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退货明细id | rec\_id | Int | 11 | y | 退货明细id |
| 平台退货单号 | jit\_efund\_no | String | 50 | y | 平台退货单号 |
| PO编号 | po\_no | String· | 50 | y | PO编号 |
| 单品id | spec\_id | Int | 11 | y | 单品id |
| 商家编码 | merchant\_no | String | 40 | y | 商家编码 |
| 平台货品编码 | spec\_no | String | 40 | y | 平台货品编码 |
| 条码 | barcode | String | 50 | y | 条码 |
| 组合装id | suite\_id | Int | 11 | y | 组合装id |
| 组合装编码 | suite\_no | String | 40 | y | 组合装编码 |
| 组合装数量 | suite\_num | Decimal(19,4) |  | y | 组合装数量 |
| 退货数量 | num | Decimal(19,4) |  | y | 退货数量 |
| 入库数量 | stockin\_num | Decimal(19,4) |  | y | 入库数量 |
| 价格 | price | Decimal(19,4) |  | y | 价格 |
| 税后价 | tax\_price | Decimal(19,4) |  | y | 税后价 |
| 货品id | goods\_id | Int | 11 | y | 货品id |
| 货品编号 | goods\_no | String | 40 | y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | y | 货品名称 |
| 规格名称 | spec\_name | String | 255 | y | 规格名称 |
| 规格码 | spec\_code | String | 50 | y | 规格码 |
| 平台货品名称 | plat\_goods\_name | String | 255 | y | 平台货品名称 |
| 唯品会箱号 | box\_no | String | 50 | y | 唯品会箱号 |
| 退货原因 | return\_reason | String | 50 | y | 退货原因 |
| 备注 | remark | String | 255 | y | 备注 |
| 最后修改时间 | modified | String |  | y | 格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String |  | y | 格式: yyyy-MM-dd HH:mm:ss |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.jit.JitRefund.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.jit.JitRefund.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.jit.JitRefund.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.jit.JitRefund.search#autoTab0_3)

```
[\
    {\
        "start_time": "2022-06-05 11:42:56",\
        "end_time": "2022-06-19 11:42:56"\
    }\
]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")

$params = new stdClass();
//$params->jit_refund_no = 'l3453245345l';
$params->start_time = '2022-06-05 11:42:56';
$params->end_time = '2022-07-19 11:42:56';

$pager = new Pager(1, 0, true);
$data = $client->pageCall("sales.jit.JitRefund.search", $pager, $params);
?>
```

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "data":<br>    {<br>        "total_count": 2,<br>        "order_list":<br>        [<br>            {<br>                "country": "",<br>                "refund_type": "",<br>                "address": "",<br>                "receiver": "",<br>                "town": "",<br>                "city": "",<br>                "created": "2022-06-09 10:34:52",<br>                "detail_list":<br>                [<br>                    {<br>                        "rec_id": 27748,<br>                        "jit_refund_no": "l3453245345l",<br>                        "po_no": "098098098",<br>                        "spec_no": "pt-sjbm001",<br>                        "spec_id": 4522,<br>                        "merchant_no": "pt-sjbm001",<br>                        "barcode": "pt-sjbm001",<br>                        "suite_id": 0,<br>                        "suite_no": "",<br>                        "suite_num": 0.0000,<br>                        "num": 2.0000,<br>                        "plat_spec_num": 0.0000,<br>                        "stockin_num": 2.0000,<br>                        "price": 0.0000,<br>                        "tax_price": 0.0000,<br>                        "goods_id": 20220217,<br>                        "goods_no": "",<br>                        "goods_name": "",<br>                        "spec_name": "",<br>                        "spec_code": "",<br>                        "plat_goods_name": "",<br>                        "box_no": "BOX00011",<br>                        "return_reason": "",<br>                        "is_check_box": 0,<br>                        "remark": "",<br>                        "modified": "2022-06-09 10:39:11",<br>                        "created": "2022-06-09 10:34:52"<br>                    },<br>                    {<br>                        "rec_id": 27749,<br>                        "jit_refund_no": "l3453245345l",<br>                        "po_no": "098098098",<br>                        "spec_no": "pt-sjbm002",<br>                        "spec_id": 4523,<br>                        "merchant_no": "pt-sjbm002",<br>                        "barcode": "pt-sjbm002",<br>                        "suite_id": 0,<br>                        "suite_no": "",<br>                        "suite_num": 0.0000,<br>                        "num": 1.0000,<br>                        "plat_spec_num": 0.0000,<br>                        "stockin_num": 1.0000,<br>                        "price": 0.0000,<br>                        "tax_price": 0.0000,<br>                        "goods_id": 20220217,<br>                        "goods_no": "",<br>                        "goods_name": "",<br>                        "spec_name": "",<br>                        "spec_code": "",<br>                        "plat_goods_name": "",<br>                        "box_no": "BOX00022",<br>                        "return_reason": "",<br>                        "is_check_box": 0,<br>                        "remark": "",<br>                        "modified": "2022-06-09 11:42:56",<br>                        "created": "2022-06-09 10:34:52"<br>                    }<br>                ],<br>                "refund_no": "R1212121212123",<br>                "mobile": "",<br>                "telephone": "",<br>                "goods_count": 3.0000,<br>                "rec_id": 85,<br>                "jit_refund_no": "l3453245345l",<br>                "warehouse_no": "",<br>                "jit_warehouse": "VIP_BJ",<br>                "self_reference": "",<br>                "modified": "2022-06-09 11:42:56",<br>                "pay_type": "",<br>                "state": "",<br>                "goods_type": 2,<br>                "region": "",<br>                "status": 50,<br>                "warehouse_id": 60<br>            }<br>        ]<br>    }<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 100,<br>    "message": "您的查询时间过宽,查询时间不能大于30天"<br>}<br>``` |
