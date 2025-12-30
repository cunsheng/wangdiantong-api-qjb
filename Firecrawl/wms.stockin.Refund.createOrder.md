---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.createOrder"
title: "API文档"
---
**wms.stockin.Refund.createOrder（退货入库单推送）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送退货入库单给ERP |
| **1.2 适用版本：** 客户端 V1.4.3.5及以上版本 |
| **1.3 权限校验：** |
| **1.4注意事项：** 不支持批量创建、不支持委外仓储 |

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
| 入库单据信息 | stockin\_order | Map<String, Object> |  | 是 | 入库单据信息 |

**stockin\_order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单号 | refund\_no | String | 20 | 是 | 退换单号 |
| 外部单号 | out\_stockin\_no | String | 20 | 否 | 外部单号 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号（不支持传入多个仓库编号） |
| 系统物流公司编号 | logistics\_code | String | 60 | 否 | 系统物流公司编号 |
| 物流单号 | logistics\_no | String | 40 | 否 | 物流单号 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 创建模式 | create\_mode | Int |  | 否 | 默认：编辑中<br>1：已提交<br>2：已审核 |
| 是否创建批次 | is\_create\_batch | boolean |  | 否 | true：创建<br>false：不创建<br>默认不创建 |
| 单据明细 | detail\_list | List<Map<String, Object>> |  | 是 | 明细信息 |

**detail\_list**

| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 是否残次品 | defect | boolean |  | 否 | true：残次品<br>false：正品<br>默认false |
| sn码 | sn\_strings | String |  | 否 | 多个之间使用英文逗号分隔，当传入sn信息时，create\_mode需要传为0 |
| 批次号 | batch\_no | String | 20 | 否 | 批次号 |
| 有效期 | expire\_date | String | 40 | 否 | 有效期 |
| 货位编号 | position\_no | String | 40 | 否 | 货位编号 |
| 生产日期 | production\_date | String | 40 | 否 | 生产日期 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 批次备注 | batch\_remark | String | 128 | 否 | 批次备注 |
| 入库价 | stockin\_price | Decimal(19,4) |  | 否 | 不传默认取退换单明细中的价格字段 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 否 | 无错误信息不返回 |
| 入库单号 | data | String |  | 否 | 入库单号 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"warehouse_no"``:``"lz"``,`<br>```"remark"``:``"test"``,`<br>```"out_stockin_no"``:``"testtqesad23"``,`<br>```"logistics_code"``:``"426"``,`<br>```"refund_no"``:``"TK2212050018"``,`<br>```"detail_list"``: [`<br>```{`<br>```"spec_no"``:``"sjdcsz"``,`<br>```"remark"``:``"test1"``,`<br>```"num"``: 1,`<br>```"unit_name"``:``"5"``,`<br>```"position_no"``:``"01"``,`<br>```"expire_date"``:``"2022-08-01 11:05:36"``,`<br>```"batch_no"``:``"PC2203300007"``,`<br>```"production_date"``:``"2022-08-01 11:05:36"``,`<br>```"defect"``:``false`<br>```}`<br>```]`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$stockinOrder =``new``stdClass();`<br>`$stockinOrder ->refund_no=``'TK2212270001'``;`<br>`$stockinOrder ->out_stockin_no=``'202212271203'``;`<br>`$stockinOrder ->warehouse_no=``'wdtapi3-test'``;`<br>`$stockinOrder ->create_mode=``2``;`<br>``<br>`$detailList = array(`<br>`array(`<br>`'spec_no'``=>``'wangdiantong'``,`<br>`'num'``=>``1``,`<br>`)`<br>`);`<br>`$stockinOrder->detail_list = $detailList;`<br>``<br>`$data = $client->call(``"wms.stockin.Refund.createOrder"``, $stockinOrder);`<br>`?>` | |
| JAVA |  |
| C# |  |

### **6.响应示例**

### 6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``:``"testtqesad23"`<br>`}` | |

#### 6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"仓库不存在  仓库编号: 1002x"`<br>`}` | |
