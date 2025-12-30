---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.outer.OuterTransfer.createByApi"
title: "API文档"
---
**wms.outer.OuterTransfer.createByApi（外仓快速调拨** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送调拨单给ERP |
| **1.2 适用版本：** 客户端 V1.5.8.6及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：仓库权限**<br>**(1)使用外仓明细调拨的情况下，仓库需要开启外仓库存明细配置**<br>**(2)使用mode=3/4调拨方案的情况下，需要联系旺店通实施开通增值配置** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务请求参数 | params | Map<String, Object> |  | Y | ye |
| 明细信息 | detail\_list | List<Map<String, Object>> |  | Y | 明细信息 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 创建模式 | create\_mode | Int |  | N | 0：保存<br>1：提交<br>2：快速审核<br>默认0 |
| 调出仓库 | from\_warehouse\_no | String | 40 | Y | 调出仓库 |
| 调入仓库 | to\_warehouse\_no | String | 40 | Y | 调入仓库 |
| 执行wms借调单编辑中状态 | wms\_edit | Int |  | N | 0：否<br>1：是<br>默认0 |
| 调拨方案 | mode | Int |  | Y | 1：外仓单品调拨（出+入）<br>2：外仓明细调拨（出+入）<br>3：外仓单品调拨（出+入+接口）<br>4：外仓明细调拨（出+入+接口） |
| 备注 | remark | String |  | N | 备注 |

****detail\_list****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String |  | Y | 商家编码 |
| 调拨数量 | num | Decimal(19,4) |  | Y | 调拨数量 |
| 批次号 | batch\_no | String |  | N | 批次号  mode=2/4有效 |
| 有效期 | expire\_date | String |  | N | 有效期  mode=2/4有效 |
| 是否残次品 | defect | Int | 1 | N | 是否残次品<br>0：否<br>1：是 |
| 备注 | remark | String |  | N | 备注 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 结果信息 | data | Map<String, String> |  | Y | 结果信息 |

****data****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调拨单号 | transfer\_no | String |  | Y | 创建成功后返回调拨单号 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"mode"``:``"2"``,`<br>```"wms_edit"``:``"1"``,`<br>```"create_mode"``:``"2"``,`<br>```"remark"``:``"testMainRemark"``,`<br>```"from_warehouse_no"``:``"daj-wms-wdt"``,`<br>```"to_warehouse_no"``:``"lz-002"`<br>```},`<br>```[`<br>```{`<br>```"defect"``:``"0"``,`<br>```"num"``:``"10"``,`<br>```"remark"``:``"testDetailRemark"``,`<br>```"spec_no"``:``"daj1"`<br>```}`<br>```]`<br>`]` | |
| php 请求示例 | |     |     |
| --- | --- |
| 1 | `<br>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1 | `{``"status"``:0,``"data"``:{``"transfer_no"``:``"TF38580"``}}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1 | `{``"status"``:100,``"message"``:``"源仓库不存在"``}` | |
