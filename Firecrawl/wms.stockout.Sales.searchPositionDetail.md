---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchPositionDetail"
title: "API文档"
---
**wms.stockout.Sales.searchPositionDetail（销售出库实际出库明细查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取销售出库实际出库明细 |
| **1.2 适用版本：** 客户端V1.5.3.9及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** 起止时间跨度不超过60分钟 |
| **1.5注意事项：权限校验：【仓库权限】** |

**2.调用场景**

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
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | Int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | y | 出库单最后修改时间，<br>格式: yyyy-MM-dd HH:mm:ss |
| 结束时间 | end\_time | String | 40 | y | 最后修改时间<br>格式: yyyy-MM-dd HH:mm:ss |
| 出库单号 | stockout\_no | String | 20 | n | 出库单号 |
| 销售订单号 | trade\_no | String | 40 | n | 系统订单号（ERP订单号） |
| 仓库编号 | warehouse\_no | String | 40 | n | 仓库编号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小（单量较大的卖家，page\_size建议200以下） |
| 页号 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 出库单信息 | data | Map<String, Object> |  | n | 出库单信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | n | 查询条件总单据数 |
| 单据数据 | order\_list | List<Map<String, Object>> |  | y | 单据数据 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单ID | stockout\_id | Int | 11 | y | 出库单ID |
| 出库单号 | stockout\_no | String | 40 | y | 出库单号 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 仓库id | warehouse\_id | Int | 11 | y | 仓库主键 |
| 订单编号 | trade\_no | String | 40 | y | 订单编号 |
| 销售出库单详情 | detail\_list | List<Map<String, Object>> |  | y | 销售出库单详情 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 销售出库单id | stockout\_id | Int | 11 | y | 销售出库单id |
| 销售出库单明细id | stockout\_detail\_id | Int | 11 | y | 销售出库单明细id |
| 分配明细id | rec\_id | Int | 11 | y | 分配明细id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | y | 规格名称 |
| 货品编号 | goods\_no | String | 40 | y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | y | 货品名称 |
| 货品简称 | short\_name | String | 255 | y | 货品简称 |
| 条码 | barcode | String | 50 | y | 条码 |
| 分摊后单价 | share\_price | Decimal(19,4) |  | y | 分摊后单价（对应页面货品成交价字段） |
| 数量 | num | Decimal(19,4) |  | y | 数量 |
| 分配数量 | dis\_num | Decimal(19,4) |  | y | 分配数量（实际货位/批次分配到的数量） |
| 货品批次 | batch\_no | String | 40 | y | 货品批次号 |
| 有效期 | expire\_date | String |  | y | 有效期 |
| 货位 | position\_no | String | 20 | y | 货位 |
| 备注 | remark | String | 255 | y | 订单明细备注 |
| 原始入库单号 | stockin\_no | String | 255 | y | 原始入库单号 |

**5.请求示例**

|     |     |
| --- | --- |
| json | ```<br>[<br>    {<br>        "start_time": "2022-12-05 15:54:02",<br>        "end_time": "2022-12-05 15:54:05",<br>        "trade_no": "JY202212050006",<br>        "stockout_no": "CK2022120534"<br>    }<br>]<br>``` |
| PHP | ```<br><?php  <br>header("Content-Type: text/html; charset=UTF-8");  <br>date_default_timezone_set("Asia/Shanghai");  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")<br>  <br>$parMap = new stdClass();<br>$parMap->start_time = '2022-12-05 15:54:02';<br>$parMap->end_time = '2022-12-05 15:54:05';<br>$parMap->trade_no = 'JY202212050006';<br>$parMap->stockout_no = 'CK2022120534';<br>//$parMap->warehouse_no = '0423';<br>$pager = new Pager(5, 0, true);<br>$data = $client->pageCall("wms.stockout.Sales.searchPositionDetail", $pager, $parMap);<br>?><br>``` |
| JAVA |  |
| C# |  |

### **6.响应示例**

#### 6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "total_count": 1,<br>        "order_list": [<br>            {<br>                "warehouse_no": "wdtapi3-test",<br>                "detail_list": [<br>                    {<br>                        "stockout_id": 675846,<br>                        "stockout_detail_id": 880045,<br>                        "rec_id": 257861,<br>                        "barcode": "11111111",<br>                        "position_no": "B01-01",<br>                        "batch_no": "",<br>                        "dis_num": 2,<br>                        "spec_no": "wangdiantong",<br>                        "spec_name": "wangdiantong",<br>                        "goods_no": "wangdiantong",<br>                        "goods_name": "wangdiantong",<br>                        "short_name": "",<br>                        "share_price": 15,<br>                        "remark": "",<br>                        "num": 2,<br>                        "stockin_no": "RK2024091025",<br>                        "expire_date": ""<br>                    }<br>                ],<br>                "stockout_no": "CK202409064",<br>                "trade_no": "JY202407290093",<br>                "stockout_id": 675846,<br>                "warehouse_id": 311<br>            }<br>        ]<br>    }<br>}<br>``` |

#### 6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 100,<br>    "message": "您的查询时间过宽,查询时间不能大于60分钟"<br>}<br>``` |
