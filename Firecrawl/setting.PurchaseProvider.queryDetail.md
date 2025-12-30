---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.queryDetail"
title: "API文档"
---
**setting.PurchaseProvider.queryDetail** **（供应商查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP供应商档案资料 |
| **1.2 适用版本：** 客户端 V1.5.8.8及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：供应商权限**（旺店通客户端-采购-采购权限管理界面控制权限） |

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
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编号 | provider\_no | String | 20 | n | 供应商编号 |
| 供应商名称 | provider\_name | String | 64 | n | 供应商名称 |
| 电话 | telno | String | 20 | n | 电话 |
| 手机 | mobile | String | 20 | n | 手机 |
| 采购平台供应商账户名 | description | String | 128 | n | 采购平台供应商账户名 |
| 联系人 | contact | String | 40 | n | 联系人 |
| 创建开始时间 | created\_begin | String | 40 | n | 创建开始时间 |
| 创建结束时间 | created\_end | String | 40 | n | 创建结束时间 |
| 修改开始时间 | modified\_begin | String | 40 | n | 修改开始时间 |
| 修改结束时间 | modified\_end | String | 40 | n | 修改结束时间 |
| 是否停用 | is\_disabled | Int | 1 | n | 1: 停用,0:未停用 |
| 是否删除 | deleted | Int | 1 | n | 0: 未删除 1:已删除 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 详细信息 | data | List<Map<String, Object>> |  | y | 详细信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结果总数 | total\_count | Int |  | 是 | 结果总数 |
| 结果详情 | details | List<Map<String, Object>> |  | 是 | 结果详情 |

**details**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商id | provider\_id | Int | 11 | n | 供应商唯一键 |
| 供应商编号 | provider\_no | String | 20 | 是 | 供应商编号 |
| 供应商名称 | provider\_name | String | 64 | 是 | 供应商名称 |
| 联系人 | contact | String | 64 | 是 | 联系人 |
| 跟进人 | follower\_name | String | 64 | 是 | 跟进人 |
| 固话 | telno | String | 20 | 是 | 固话 |
| 手机 | mobile | String | 20 | 是 | 手机 |
| 传真 | fax | String | 20 | 是 | 传真 |
| 邮编 | zip | String | 20 | 是 | 邮编 |
| 邮件 | email | String | 20 | 是 | 邮件 |
| QQ | qq | String | 20 | 是 | QQ |
| 旺旺 | wangwang | String | 64 | 是 | 旺旺 |
| 地址 | address | String | 128 | 是 | 地址 |
| 网址 | website | String | 128 | 是 | 网址 |
| 到货天数 | arrive\_cycle\_days | Int | 11 | 是 | 到货天数 |
| 上次采购日期 | last\_purchase\_time | String | 40 | 否 | 上次采购日期（若供应商未进行过采购，该字段不返回） |
| 备注 | remark | String | 256 | 是 | 备注 |
| 停用 | is\_disabled | bool | 1 | 是 | false: 未停用, true:停用 |
| 是否删除 | deleted | Int | 1 | 是 | 0:  正常（非0代表已删除） |
| 最后修改时间 | modified | String |  | 是 | 最后修改时间 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 省 | province | String |  | 是 | 省 |
| 市 | city | String |  | 是 | 市 |
| 区 | district | String |  | 是 | 区 |
| 收款银行 | account\_bank | String |  | 是 | 收款银行 |
| 收款人 | collect\_name | String |  | 是 | 收款人 |
| 银行账号 | account\_bank\_no | String |  | 是 | 银行账号 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.queryDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.queryDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.queryDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.queryDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"created_end"``:``"2022-04-20"``,``"created_begin"``:``"2022-03-01"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"setting.PurchaseProvider.queryDetail"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.queryDetail#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"details"``: [`<br>```{`<br>```"city"``:``"北京市"``,`<br>```"wangwang"``:``" "``,`<br>```"remark"``:``"小丸子说需要采购"``,`<br>```"account_bank"``:``""``,`<br>```"telno"``:``""``,`<br>```"province"``:``"北京"``,`<br>```"contact"``:``""``,`<br>```"modified"``: 1753854378000,`<br>```"follower_name"``:``"系统"``,`<br>```"provider_name"``:``"LCJtest11"``,`<br>```"fax"``:``"aaaaa"``,`<br>```"email"``:``"123567890@qq.com"``,`<br>```"provider_no"``:``"LCJtest11"``,`<br>```"zip"``:``"300457"``,`<br>```"qq"``:``"123567890"``,`<br>```"website"``:``"www.baidu.cn"``,`<br>```"address"``:``"小丸子聚居地"``,`<br>```"last_purchase_time"``: 1752567283000,`<br>```"created"``: 1502093567000,`<br>```"is_disabled"``:``false``,`<br>```"mobile"``:``""``,`<br>```"arrive_cycle_days"``: 10,`<br>```"deleted"``: 0,`<br>```"collect_name"``:``""``,`<br>```"district"``:``"通州区"``,`<br>```"provider_id"``: 7,`<br>```"account_bank_no"``:``""`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.queryDetail#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
