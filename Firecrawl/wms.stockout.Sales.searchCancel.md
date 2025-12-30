---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.searchCancel"
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

**wms.stockout.Sales.searchCancel** **（已取消出库单查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取已取消的销售出库单 |
| **1.2 适用版本：** 客户端 V1.4.7.3及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5 注意事项：** 起止时间差最大1小时 |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

**3.请求参数说明**

3.1 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | http://47.92.239.46/openapi |
| 正式环境 | http://wdt.wangdian.cn/openapi |

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
| 分页大小 | page\_size | int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String |  | Y | 修改时间<br>yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String |  | Y | 修改时间<br>yyyy-MM-dd HH:mm:ss格式 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | Y | 分页大小 |
| 页号 | page\_no | Int | 4 | Y | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 出库单相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | order\_list | List<Map<String, Object>> |  | Y | 数据节点 |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单id | stockout\_id | Int |  | Y | 出库单id |
| 出库单编号 | stockout\_no | String |  | Y | 出库单编号 |
| 出库单状态 | status | Byte |  | Y | 5：已取消<br>10：待放回<br>51：缺货<br>53：wms已接单<br>54：获取电子面单<br>60：待分配<br>61：排队中<br>63：待补货<br>65：待处理<br>70：待发货<br>73：爆款锁定<br>75：待拣货<br>77：拣货中，PDA拣货后<br>79：已拣货<br>90：延时发货<br>110：已完成 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | ```<br>[{<br>"start_time": "2022-07-19 10:42:56",<br>"end_time": "2022-07-19 11:42:56"<br>}]<br>``` |
| php 请求示例 | ```<br><?php  <br>header("Content-Type: text/html; charset=UTF-8");  <br>date_default_timezone_set("Asia/Shanghai");  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")<br>  <br>$params = new stdClass();  <br> <br>$params->start_time = '2022-07-19 10:42:56';  <br>$params->end_time = '2022-07-19 11:42:56';  <br>  <br>$pager = new Pager(1, 0, true);  <br>$data = $client->pageCall("wms.stockout.Sales.searchCancel", $pager, $params);?><br>``` |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "total_count": 2,<br>        "order_list": [{<br>            "stockout_no": "CH202210175",<br>            "modified": "2022-10-17 14:03:36",<br>            "stockout_id": 1630025,<br>            "status": 110<br>        }, {<br>            "stockout_no": "CH202210176",<br>            "modified": "2022-10-17 14:08:38",<br>            "stockout_id": 1630026,<br>            "status": 110<br>        }]<br>    }<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 100,<br>    "message": "起止时间差最大1小时"<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1