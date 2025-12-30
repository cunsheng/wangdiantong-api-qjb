---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.PurchaseReturn.upload"
title: "API文档"
---
**finance.settle.PurchaseReturn.upload（创建采购退货结算单** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：创建采购退换结算单给ERP |
| **1.2 适用版本：** 客户端 V1.5.6.2及以上版本 |
| **1.3 权限校验：** |

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
| 单据信息 | settle\_order | Map<String, Object> |  | 是 | 单据信息 |
| 明细信息 | detail\_list | List<Map<String, Object>> |  | 是 | 明细信息 |

**settle\_order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购退货单号 | return\_no | String | 40 | 是 | 采购退货单号 |
| 物流公司编号 | logistics\_company\_no | String | 20 | 否 | ERP内手动维护的物流公司编号 |
| 物流单号 | logistics\_no | String | 100 | 否 | 物流单号 |
| 发票类型 | invoice\_type | byte |  | 否 | 发票类型<br>0：无发票<br>1：电子普通发票<br>2：纸质普通发票<br>3：电子增值税专用发票<br>4：纸质增值税专用发票 |
| 发票号码 | invoice\_no | String | 100 | 否 | 发票号码 |
| 邮费 | post\_fee | Decimal(19,4) |  | 否 | 邮费 |
| 其他费用 | other\_fee | Decimal(19,4) |  | 否 | 其他费用 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 是否审核 | is\_check | boolean | 1 | 否 | 默认false,审核失败情况下单据会创建失败 |
| 模糊查询 | fuzzy\_query | boolean | 1 | 否 | 默认false,业务单号进行模糊查询匹配，匹配数量大于1条时会报错 |

**detail\_list**

| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 结算数量 | settle\_num | Decimal(19,4) |  | 是 | 结算数量 |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单价 | price | Decimal(19,4) |  | 否 | 默认值为采购退货单明细税前单价\*单位系数 |
| 税率 | tax\_rate | Decimal(19,4) |  | 否 | 默认值为采购退货单明细税率 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 批次号 | batch\_no | String |  | 否 | 如果采购退货单包含批次则需传入 |
| 有效期 | expire\_date | String |  | 否 | 如果采购退货单包含有效期则需传入 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 响应正文数据 | data | <Map<String, Object> |  | 否 | 有错误信息时不返回此节点 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结算单号 | order\_no | String | 40 | 是 | 结算单号 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"return_no"``:``"CR202410240004"``,`<br>```"post_fee"``:``"12"``,`<br>```"logistics_no"``:``"test999"``,`<br>```"invoice_type"``:``"1"``,`<br>```"remark"``:``"testremark"``,`<br>```"fuzzy_query"``:``"0"``,`<br>```"is_check"``: 1,`<br>```"logistics_company_no"``:``"testttt"`<br>```},`<br>```[`<br>```{`<br>```"settle_num"``:``"1"``,`<br>```"batch_no"``:``""``,`<br>```"price"``:``"20"``,`<br>```"remark"``:``"512023"``,`<br>```"spec_no"``:``"zx1"`<br>```}`<br>```]`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client = new WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$parMap = new stdClass();`<br>`$parMap->return_no =``"CR202410240004"``;`<br>`//$parMap->logistics_company_no = 'hsdhsdfh';`<br>`//$parMap->logistics_no = '102810840284';`<br>`//$parMap->invoice_type = 1;`<br>`//$parMap->post_fee = 1.5;`<br>`//$parMap->remark = 'remark test';`<br>`//$parMap->is_check = false;`<br>`$detail1 = new stdClass();`<br>`$detail1->spec_no =``'water'``;`<br>`$detail1->settle_num = 2;`<br>`;`<br>`$detail2 = new stdClass();`<br>`$detail2->spec_no =``'mgh1'``;`<br>`$detail2->settle_num = 10;`<br>`$detailList = array($detail1, $detail2);`<br>`$data = $client->call(``"finance.settle.PurchaseReturn.upload"``, $parMap, $detailList);`<br>`?>` | |
| JAVA |  |
| C# |  |

### **6.响应示例**

### 6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``:`<br>```{`<br>```"order_no"``:``"JS202412020004"`<br>```}`<br>`}` | |

#### 6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"模糊搜索无匹配或有多条匹配"`<br>`}` | |
