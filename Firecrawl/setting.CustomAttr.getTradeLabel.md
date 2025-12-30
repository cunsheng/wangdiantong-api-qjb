---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.CustomAttr.getTradeLabel"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

[登录](javascript:gologin()) [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

订单类

销售出库单查询

物流同步状态回传

原始单推送

订单查询

待同步列表查询

重量回传

重量回传2

发票信息查询

发票信息更新

平台账单查询

平台账单推送

取消当前同步

库存同步失败

库存同步成功

获取自有平台货品需要同步信息

历史销售出库单查询

历史订单查询

平台对账单查询

原始单查询

被合并订单查询

收付款单查询

重量回传3

库存同步计算查询

重量回传4

订单客服备注修改

物流单查询

历史原始单查询

JIT退货单查询

原始单推送2

销售出库实际出库明细查询

销售收付单查询

已完成订单推送

已取消出库单查询

订单日志查询

订单标签查询

订单转异常订单

库存同步计算查询（批量）

订单查询（仅返回自有平台、线下平台订单信息）

历史原始单查询（仅返回自有平台、线下平台订单）

历史订单查询（仅返回自有平台、线下平台订单）

原始单查询（仅返回自有平台、线下平台订单）

当前位置： API文档 > 订单类

**setting.CustomAttr.getTradeLabel（订单标签查询** **）**

**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取订单标签数据 |
| **1.2 适用版本：** 客户端 V1.4.9.3及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：**<br>- 不传起止时间则默认返回全部数据, 起止时间最大间隔30天<br>  <br>- 建议在第一次全量获取数据, 后续按照最后变更时间获取变更数据<br>  <br>- 通过其他接口获取到订单标签mask后, 与当前接口返回的所有数据进行make\_set操作即可获取完整的标签<br>  <br>  - 例如 mask= 37, 完整的订单标签数据中前7个分别为a, b, c, d, e, f, g 则mask对应的订单标签为a,c,g<br>    <br>  - mask 转换为2进制为 100101 , 反转后为101001. 结合前7个标签的顺序可得出订单标签为a,c,g |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

**3.请求参数说明**

3.1 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | http://47.92.239.46/openapi |
| 正式环境 | http://wdt.wangdian.cn/openapi |

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
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数， 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | N | 最后修改时间 |
| 结束时间 | end\_time | String | 40 | N | 最后修改时间 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | <Map<String, Object>> |  | 是 | 返回信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | detail\_list | List<Map<String, Object>> |  | 是 | 数据节点 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 标签唯一id | rec\_id | Int | 11 | Y | 标签唯一id |
| 标签类型 | attr\_type | short |  | Y | 标签类型 |
| 标签key | attr\_key | Int | 11 | Y | 标签key |
| 标签名称 | attr\_name | String | 40 | Y | 标签名称 |
| 是否内置 | is\_builtin | boolean |  | Y | 是否内置 |
| 创建时间 | created | String |  | Y | 创建时间，yyyy-MM-dd HH:mm:ss格式 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间，yyyy-MM-dd HH:mm:ss格式 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6 | `[`<br>```{`<br>```"start_time"``:``"2023-10-01 00:00:00"``,`<br>```"end_time"``:``"2023-10-02 00:00:00"`<br>```}`<br>`]` | |
| PHP | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params =``new``stdClass();`<br>`//$params->jit_refund_no = 'l3453245345l';`<br>`$params->start_time =``'2022-06-05 11:42:56'``;`<br>`$params->end_time =``'2022-07-19 11:42:56'``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$data = $client->pageCall(``"setting.CustomAttr.getTradeLabel"``, $pager, $params);`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22 | `{`<br>```"data"``: {`<br>```"detail_list"``: [`<br>```{`<br>```"attr_key"``: 1,`<br>```"attr_name"``:``"其他"``,`<br>```"attr_type"``: 12,`<br>```"is_builtin"``:``true``,`<br>```"rec_id"``: 87`<br>```},`<br>```{`<br>```"attr_key"``: 2,`<br>```"attr_name"``:``" 不同仓库发货"``,`<br>```"attr_type"``: 12,`<br>```"is_builtin"``:``true``,`<br>```"rec_id"``: 88`<br>```}`<br>```],`<br>```"total_count"``: 93`<br>```},`<br>```"status"``: 0`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"message"``:``"未知错误"``,`<br>```"status"``: 100`<br>`}` | |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

[常用工具](javascript:dgoto('G%E5%B8%B8%E7%94%A8%E5%B7%A5%E5%85%B7'))

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1