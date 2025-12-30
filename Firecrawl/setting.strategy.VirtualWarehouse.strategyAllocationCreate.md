---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.strategy.VirtualWarehouse.strategyAllocationCreate"
title: "API文档"
---
**setting.strategy.VirtualWarehouse.strategyAllocationCreate（虚拟仓库存分配策略创建** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**<br>虚拟仓库存分配,    功能类似于客户端: 设置-策略设置-虚拟仓策略-虚拟仓库存分配 |
| **1.2 适用版本：** 客户端 V1.5.6.6及以上版本 |
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
| 策略信息 | params | Map<String, Object> |  | Y | 业务请求参数 |
| 策略明细信息 | detail | List<Map<String, Object>> |  | Y | 策略明细信息 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分配范围 | range | Int |  | Y | 分配范围<br>0：指定单据<br>1：所有单据 |
| 分配模式 | mode | Int |  | Y | 分配模式<br>0：货品<br>1：全局<br>2：品牌 |
| 规则编码 | rule\_no | String |  | Y | 规则编码 |
| 规则名称 | rule\_name | String |  | Y | 规则名称 |
| 关联单类型 | src\_order\_type | String |  | N | 关联单类型<br>0：采购单<br>1：其他入库业务单<br>2：调拨单<br>3：生产成品单 |
| 关联单号 | order\_no\_list | String\[\] |  | N | 关联单号 |
| 立刻执行对应策略 | execute\_strategy | boolean |  | N | 默认是 |

**detail**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 虚拟仓编码 | vir\_warehouse\_no | String |  | Y | 虚拟仓编码 |
| 优先级 | priority | Int |  | N | 优先级 |
| 锁定库存量 | num | BigDecimal |  | N | 锁定库存量 |
| 锁定比例 | ratio | BigDecimal |  | N | 锁定比例 |
| 品牌编码 | brand\_no\_list | String\[\] |  | N | 品牌编码 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应信息 | data | Map<String, Object> |  | Y | 响应信息 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | ```<br>[<br>    {<br>        "mode": 0,<br>        "rule_name": "lir_test18",<br>        "src_order_type": 1,<br>        "range": 0,<br>        "rule_no": "lir_test18"<br>    },<br>    [<br>        {<br>            "vir_warehouse_no": "lzxzb2",<br>            "spec_no": "lirspec_sn",<br>            "ratio": 1<br>        }<br>    ]<br>]<br>``` |
| php 请求示例 | ```<br>``` |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "data": "策略创建成功"<br>    }<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json |  |
