---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.reserveExtractAdd"
title: "API文档"
---
**setting.strategy.VirtualWarehouse.reserveExtractAdd（虚拟仓库存释放策略创建** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**<br>虚拟仓库存分配,    功能类似于客户端: 设置-策略设置-虚拟仓策略-虚拟仓库存分配 |
| **1.2 适用版本：** 客户端 V1.5.5.2及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5 注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

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
| 分页大小 | page\_size | int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 策略信息 | orderInfo | Map<String, Object> |  | Y | 策略信息 |
| 策略明细信息 | detail | List<Map<String, Object>> |  | Y | 策略明细信息 |

**orderInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单号 | order\_no | Int |  | Y | 单号 |
| 单据类型 | order\_type | Int |  | Y | 单据类型<br>2：调拨单<br>4：盘点单<br>14：采购退货<br>21：其他出库业务单 |

**detail**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | y | 平台规格编码，不传默认为空 |
| 虚拟仓编码 | vir\_warehouse\_no | String | 40 | y | 虚拟仓编码 |
| 入库虚拟仓 | to\_virwarehouse\_no | String | 40 | n | 入库虚拟仓 |
| 释放优先级 | priority | Int | 10 | y | 释放优先级 |
| 出库数量 | num | BigDecimal |  | n | 出库数量 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应信息 | data | Map<String, Object> |  | Y | 响应信息 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 |  |
| php 请求示例 |  |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | |     |     |
| --- | --- |
| 1 | `<br>` | |

6.2异常响应示例

|     |     |
| --- | --- |
| json |  |
