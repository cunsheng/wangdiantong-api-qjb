---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.warehouseSearch"
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

**setting.strategy.VirtualWarehouse.warehouseSearch** **（虚拟仓仓库查询)**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP虚拟仓仓库信息 |
| **1.2 适用版本：** 客户端 V1.3.8.3 及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** 起止时间跨度不超过30天 |
| **1.5注意事项：** **【权限校验】：虚拟仓权限，实体仓权限**<br>tips: 多个实体仓对应同一个虚拟仓的情况, 只要有其中一个仓库的权限就可以查到改虚拟仓 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

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
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 是 | 修改时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | 是 | yyyy-MM-dd HH:mm:ss格式 |
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 否 | 虚拟仓编号 |
| 实体仓编号 | warehouse\_no | String |  | 否 | 实体仓编号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

**返回值为一个Map<String, Object>**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据信息 | data | Map<String, Object> |  | 是 | 单据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据 | detail\_list | List<Map<String, Object>> |  | 是 | 明细数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 模式 | warehouse\_type | Int |  | 是 | 0：普通店铺<br>1：分销模式 |
| 虚拟仓编号 | virtual\_warehouse\_no | String |  | 是 | 虚拟仓编号 |
| 虚拟仓id | virtual\_warehouse\_id | Int |  | 是 | 虚拟仓唯一键 |
| 虚拟仓名称 | virtual\_warehouse\_name | String |  | 是 | 虚拟仓名称 |
| 停用 | is\_disabled | Int |  | 是 | 0：正常    1：停用 |
| 备注 | remark | String |  | 是 | 备注 |
| 修改时间 | modified | String |  | 是 | 修改时间 |
| 创建时间 | created | String |  | 是 | 创建时间 |
| 实体仓列表 | warehouse\_list | List<Map<String, Object>> |  | 是 | 实体仓列表 |

**warehouse\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 实体仓id | sys\_warehouse\_id | Int |  | 是 | 实体仓唯一键 |
| 虚拟仓id | virtual\_warehouse\_id | Int |  | 是 | 虚拟仓唯一键 |
| 是否启用 | is\_start\_up | Int |  | 是 | 0：未启用  1：已启用 |
| 实体仓编号 | warehouse\_no | String |  | 是 | 实体仓编号 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.warehouseSearch#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.warehouseSearch#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.warehouseSearch#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.warehouseSearch#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>```"start_time"``:``"2020-02-03 17:15:17"``,`<br>```"end_time"``:``"2020-02-03 17:55:17"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-02-03 17:15:17"``;`<br>`$parMap``->end_time =``"2020-02-03 17:55:17"``;`<br>`$parMap``->virtual_warehouse_no =``""``;`<br>`$parMap``->warehouse_no =``""``;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"setting.strategy.VirtualWarehouse.warehouseSearch"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.warehouseSearch#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 2,`<br>```"detail_list"``: [{`<br>```"virtual_warehouse_no"``:``"wdtapi3-test---"``,`<br>```"virtual_warehouse_name"``:``"wdtapi3-test-虚拟仓"``,`<br>```"warehouse_type"``: 0,`<br>```"created"``:``"2022-04-14 10:32:55"``,`<br>```"is_disabled"``: 1,`<br>```"modified"``:``"2022-04-19 15:54:34"``,`<br>```"warehouse_list"``: [{`<br>```"virtual_warehouse_id"``: 7,`<br>```"sys_warehouse_id"``: 311,`<br>```"is_start_up"``: 1,`<br>```"warehouse_no"``:``"wdtapi3-test"`<br>```}],`<br>```"remark"``:``""``,`<br>```"virtual_warehouse_id"``: 7`<br>```}, {`<br>```"virtual_warehouse_no"``:``"xunicang"``,`<br>```"virtual_warehouse_name"``:``"小丸子虚拟仓"``,`<br>```"warehouse_type"``: 1,`<br>```"created"``:``"2022-04-20 16:22:55"``,`<br>```"is_disabled"``: 0,`<br>```"modified"``:``"2022-04-20 16:22:55"``,`<br>```"warehouse_list"``: [{`<br>```"virtual_warehouse_id"``: 8,`<br>```"sys_warehouse_id"``: 311,`<br>```"is_start_up"``: 1,`<br>```"warehouse_no"``:``"wdtapi3-test"`<br>```}],`<br>```"remark"``:``"备注一下"``,`<br>```"virtual_warehouse_id"``: 8`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.warehouseSearch#autoTab1_0)

|     |     |
| --- | --- |
| 1 | `<br><br>` |

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