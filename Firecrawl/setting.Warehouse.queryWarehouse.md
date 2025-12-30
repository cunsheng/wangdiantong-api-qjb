---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Warehouse.queryWarehouse"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

基础类

物流公司查询

供应商查询

仓库查询

店铺查询

供应商信息推送

店铺更新

员工查询

虚拟仓仓库查询

退换原因查询

地址查询-省

地址查询-市

地址查询-区

虚拟仓信息查询

当前位置： API文档 > 基础类

**setting.Warehouse.queryWarehouse**（仓库查询）

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的仓库档案资料 |
| **1.2 适用版本：** 客户端 V1.5.8.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** |
| **1.5注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** |

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
| 仓库编号 | warehouse\_no | String | 40 | 否 | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | 否 | 仓库名称 |
| 类型 | type | Int | 4 | 否 | 1:普通（内部）,2:自流转,3:平台,4:京东沧海.6:抖音云仓,125:代发仓,126:分销委外 |
| 子类型 | sub\_type | Int | 6 | 否 | 0:默认,1:旺店通,2:菜鸟,3:百世WMS,4:巨沃,5:心怡WMS,6:科捷,7:吉客云,8:中通WMS,9:通天晓,10:酷仓宝WMS,11:景天WMS,12:网店管家笛佛WMS,13:九曳WMS,14:万里牛,15:麓客WMS,16:青图WMS(ERP),17:安鲜达WMS,18:顺丰WMS,19苏宁WMS,20:雅澳E,21:EMS,22:递四方,23:中邮WMS,24:云腾WMS,25:天图WMS;26:但丁WMS,27:e仓宝,28:仓卫士,29:山橙WMS,30橙蚁WMS,31:中山邮政WMS,32:赢路WMS,33:无忧WMS,34:筋斗云WMS,35:韵达WMS,36:GEEK |
| 开始时间 | start\_time | String |  | 否 | 最后修改时间 |
| 结束时间 | end\_time | String |  | 否 | 最后修改时间 |
| 是否隐藏已停用数据 | hide\_delete | Int |  | 否 | 0:不隐藏; 1:隐藏已删除; 默认隐藏已删除 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 查询出的详细信息 | data | List<Map<String, Object>> |  | 是 | 详细信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结果总数 | total\_count | Int |  | 是 | 结果总数 |
| 结果详情 | details | List<Map<String, Object>> |  | 是 | 结果详情 |

**details**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库id | warehouse\_id | Int | 11 | 是 | 仓库唯一键 |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 仓库名称 | name | String | 64 | 是 | 仓库名称 |
| 邮编 | zip | String | 255 | 是 | 邮编 |
| 地址 | address | String | 255 | 是 | 地址 |
| 省份 | province | String | 50 | 是 | 省份 |
| 城市 | city | String | 50 | 是 | 城市 |
| 区县 | district | String | 50 | 是 | 区县 |
| 手机 | mobile | String | 40 | 是 | 手机 |
| 备注 | remark | String | 255 | 是 | 备注 |
| 类别 | type | Int | 4 | 是 | 1:普通（内部）,2:自流转,3:平台,4:京东沧海.6:抖音云仓,125:代发仓,126:分销委外 |
| 固话 | telno | String | 20 | 是 | 固话 |
| 子类别 | sub\_type | Int | 6 | 是 | 0:默认,1:旺店通,2:菜鸟,3:百世WMS,4:巨沃,5:心怡WMS,6:科捷,7:吉客云,8:中通WMS,9:通天晓,10:酷仓宝WMS,11:景天WMS,12:网店管家笛佛WMS,13:九曳WMS,14:万里牛,15:麓客WMS,16:青图WMS(ERP),17:安鲜达WMS,18:顺丰WMS,19苏宁WMS,20:雅澳E,21:EMS,22:递四方,23:中邮WMS,24:云腾WMS,25:天图WMS;26:但丁WMS,27:e仓宝,28:仓卫士,29:山橙WMS,30橙蚁WMS,31:中山邮政WMS,32:赢路WMS,33:无忧WMS,34:筋斗云WMS,35:韵达WMS,36:GEEK |
| 联系人 | contact | String | 20 | 是 | 联系人 |
| 修改时间 | modified | String | 40 | 是 | 修改时间 |
| 停用 | is\_disabled | boolean |  | 是 | false:未停用; true:已停用 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 采购联系人 | purchase\_contact | String | 20 | 是 | 采购联系人 |
| 采购联系电话 | purchase\_telno | String | 20 | 是 | 采购联系电话 |
| 采购联系地址 | purchase\_address | String | 20 | 是 | 采购联系地址 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Warehouse.queryWarehouse#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Warehouse.queryWarehouse#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Warehouse.queryWarehouse#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Warehouse.queryWarehouse#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"setting.Warehouse.queryWarehouse"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Warehouse.queryWarehouse#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"details"``: [{`<br>```"zip"``:``""``,`<br>```"address"``:``""``,`<br>```"city"``:``"无"``,`<br>```"created"``:``"2021-11-26 17:02:21"``,`<br>```"is_disabled"``:``false``,`<br>```"mobile"``:``""``,`<br>```"remark"``:``""``,`<br>```"type"``: 1,`<br>```"telno"``:``""``,`<br>```"prop2"``:``""``,`<br>```"prop1"``:``""``,`<br>```"province"``:``""``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"sub_type"``: 0,`<br>```"district"``:``"无"``,`<br>```"contact"``:``""``,`<br>```"name"``:``"wdtapi3-test"``,`<br>```"modified"``: 1675088001000,`<br>```"warehouse_id"``: 624`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.Warehouse.queryWarehouse#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1