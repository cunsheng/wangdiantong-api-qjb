---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.StockSync.getSelfWaitSyncIdListOpen"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

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

### **sales.StockSync.getSelfWaitSyncIdListOpen（获取自有平台货品需要同步信息）**

### **¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取自有平台货品需要同步信息 |
| **1.2 适用版本：** 客户端V1.3.9.1以上版本 |
| **1.3 增量获取:** |
| **1.4 时间跨度：** |
| **1.5注意事项：【权限校验】：店铺权限** |

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
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 一次的记录数 | count | Int |  | 是 | 一次的记录数最小值10, 最大值5000 |
| 起始位置 | position | Int |  | 是 | 第一次用0, 后面则使用上一次调用返回的position |

**4.响应参数**

响应参数为一个Map<String, Object>

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 状态码,0表示正常 |
| 错误信息 | message | String |  | N | 无错误信息不返回 |
| 数据信息 | data | Map<String, Object> |  | N | 数据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| rec\_id的集合 | id\_list | List<long> |  | Y | 待同步的api\_goodsspec表rec\_id |
| 下次调用的起始位置 | position | Int |  | N | list中对应最后一条的disable\_syn\_until |

**5** **.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
| 1 | `[``"500"``,``"0"``]` | |
| php 请求示例 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$data``=``$client``->call(``"sales.StockSync.getSelfWaitSyncIdListOpen"``, 500, 0);`<br>``<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示例**

**6.1正常响应示例**

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"id_list"``: [174004, 175511, 175512, 175522, 175523, 175524, 175525, 175526, 175527, 175533, 175534, 175535, 175536, 175537, 175538, 175539, 175540, 175541, 175568, 175574, 175576, 173687, 173688],`<br>```"position"``: 239126414`<br>```}`<br>`}` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json |  |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1