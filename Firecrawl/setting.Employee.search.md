---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Employee.search"
title: "API文档"
---
**setting.Employee.search** **（员工查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP的员工页面信息 |
| **1.2 适用版本：** 客户端 V1.3.6.3及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

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
| 开始时间 | start\_time | date |  | 是 | 开始修改时间 |
| 结束时间 | end\_time | date |  | 是 | 结束修改时间 |
| 员工编号 | employee\_no | String |  | 否 | 员工编号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 员工数据 | data | Map<String, Object> |  | 是 | 员工相关数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order\_list | List<Map<String, Object>> |  | 是 | 员工数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 员工id | employee\_id | Int | 11 | 是 | 员工id |
| 员工编号 | employee\_no | String |  | 是 | 员工编号 |
| 姓名 | name | String |  | 是 | 姓名 |
| 昵称 | shortname | String |  | 是 | 昵称 |
| 性别 | gender | Int | 4 | 是 | 性别：<br>1：男  2：女 |
| 职位 | position\_name | String |  | 是 | 职位 |
| 部门 | department\_name | String |  | 是 | 部门 |
| 工种 | roles\_mask | Int | 11 | 是 | 工种：<br>1 业务员 2审单员 4打单员 8验货员 16打包员 32拣货员 64发货员 128结算员 512采购员 1024质检员 2048生产员<br>（注意：如果是3，则表示该员工有业务员和审单员的工种“1+2”，如果是15，则表示该员工有业务员审单员打单员验货员四个工种“1+2+4+8”，其他数字以此类推） |
| 备注 | remark | String |  | 是 | 备注 |
| 内置员工 | is\_system\_user | boolean | 1 | 是 | 是否是系统内置员工 |
| 是否停用 | is\_disabled | boolean |  | 是 | true: 停用 |
| 删除状态 | deleted | int | 1 | 是 | 不为0则表示已经删除 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Employee.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Employee.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Employee.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Employee.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2021-12-01 00:00:00"``,``"end_time"``:``"2021-12-12 12:00:00"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client = new WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap = new stdClass();`<br>`$parMap->start_time =``"2021-12-01 00:00:00"``;`<br>`$parMap->end_time =``"2021-12-12 00:00:00"``;`<br>``<br>``<br>`$pager = new Pager(1, 0,``true``);`<br>`$data = $client->pageCall(``"setting.Employee.search"``, $pager, $parMap);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Employee.search#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 14,`<br>```"order_list"``: [`<br>```{`<br>```"roles_mask"``: 0,`<br>```"gender"``: 0,`<br>```"is_system_user"``:``false``,`<br>```"employee_id"``: 374,`<br>```"name"``:``""``,`<br>```"position_name"``:``"慧策技术支持"``,`<br>```"employee_no"``:``"lxxx-test2"``,`<br>```"remark"``:``"开放接口"``,`<br>```"shortname"``:``"lxxxx-test2"`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Employee.search#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 100,`<br>```"message"``:``"超过每分钟最大调用频率限制,请稍后重试"`<br>`}` |
