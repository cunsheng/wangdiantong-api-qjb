---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=statistic.StockoutCollect.queryCostWithDetail"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

当前位置： API文档

**statistic.StockoutCollect.queryCostWithDetail（出库瞬时成本查询** **）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP出库瞬时成本信息 |
| **1.2 适用版本：** 客户端 V1.5.7.0及以上版本 |
| **1.4 时间跨度：** start\_time与end\_time起止时间跨度不超过7天 |
| **1.5 注意事项：** **【权限校验】：仓库权限。**<br>未开启多仓成本情况下，仓库编号返回空字符串；开启多仓成本后仓库编号返回实际仓库的编号 |

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
| 开始时间 | start\_time | String | 40 | Y | 起始时间（发货时间），若无出库单号则为必填。 |
| 结束时间 | end\_time | String | 40 | Y | 结束时间（发货时间） |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 出库单号 | stockout\_no | String | 40 | N | 出库单号，多个出库单号之间英文逗号分隔 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | Y | 单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 出库相关数据 |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单id | stockout\_id | Int | 11 | Y | 出库单id |
| 出库单号 | stockout\_no | String | 40 | Y | 出库单号 |
| 仓库id | warehouse\_id | Int | 11 | Y | 仓库主键 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 40 | Y | 仓库名称 |
| 出库类型 | src\_order\_type | Int | 4 | Y | 单据类型<br>1：销售出库<br>2：调拨单<br>4：盘点单<br>5：生产单<br>8：正残转换单<br>9：JIT出库<br>14：采购退货出库<br>21：其他出库<br>24：调整出库 |
| 业务单号 | src\_order\_no | String | 40 | Y | 业务单号 |
| 状态 | status | Int | 4 | Y | 状态<br>110：已完成 |
| 制单人 | employee\_name | String | 40 | Y | 制单人 |
| 物流公司id | logistics\_id | Int | 11 | Y | 物流公司主键 |
| 物流公司 | logistics\_name | String | 40 | Y | 物流公司 |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 邮费 | weigh\_post\_cost | Decimal(19,4) |  |  |