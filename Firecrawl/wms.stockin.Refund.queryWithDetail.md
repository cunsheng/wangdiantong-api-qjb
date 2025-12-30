---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryWithDetail"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

售后类

退货入库单查询

原始退款单推送

创建退货预入库

退换单查询

预入库单据查询

退货预入库单取消

历史退换单查询

原始退款单查询

原始退款单推送2

退货入库单推送

快速退货

历史退货入库单查询

历史原始退款单查询

退货物流包裹查询

当前位置： API文档 > 售后类

****wms.stockin.Refund.queryWithDetail** **（退货入库单查询）****

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的退货入库单单据信息 |
| **1.2 适用版本：** 客户端 V1.5.9.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：** **【权限校验】：仓库权限，店铺权限** <br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台数据， **淘系**相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")，拼多多请自行对接平台获取。<br>本接口中涉及到用户隐私的字段数据仅自有平台及线下平台订单返回。具体字段详情见下面表格； |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 客户网名 | nick\_name |
| 客户姓名 | customer\_name |

**2.调用场** **景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

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
| 查询参数 | params | Map<String, Object> |  | y | 查询参数 |
| 分页 | pager | pager |  | y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | n | 仓库编号 |
| 入库单号 | stockin\_no | String | 20 | n | 入库单号 |
| 退换单号 | refund\_no | String | 40 | n | 退换单号 |
| 店铺编号 | shop\_nos | String | 255 | n | 多个编号间使用英文逗号分隔 |
| 入库单状态 | status | String | 255 | n | 英文逗号拼接的状态值:<br>10=已取消；20=编辑中；30=待审核/待处理；80=已完成 |
| 时间条件类型 | time\_type | Int | 1 | n | 查询的时间条件类型, 0:修改时间; 1:入库时间 不传默认为0 |
| 开始时间 | start\_time | String | 40 | y | 起始时间, yyyy-MM-dd HH:mm:ss格式 |
| 结束时间 | end\_time | String | 40 | y | 结束时间, yyyy-MM-dd HH:mm:ss格式 |
| 是否使用从库查询 | is\_slave | boolean | 1 | n | 使用：true  不使用：false<br>（仅对开通从库配置客户生效） |
| 是否返回sn信息 | need\_sn | boolean | 1 | n | 返回：true<br>不返回：false |
| 是否需要汇总数据 | need\_summary | bool | 1 | n | 需要：true<br>不需要：false<br>默认false |
| 是否需要国补信息 | need\_gov\_subsidy\_info | boolean | 1 | n | 0：不需要<br>1：需要<br>默认0 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小 |
| 页号 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 返回0为正常 |
| 错误信息 | message | String |  | n | 无错误信息不返回 |
| 退货入库单信息 | data | Map<String, Object> |  | n | 退货入库信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据仅自有平台及线下平台返回，其他平台均不返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | y | 入库单相关数据 |
| 总数 | total\_count | Int | 11 | n | 查询条件总数单据 |
| 汇总数据 | summary\_data | List<warehouse\_data> |  | y | 汇总数据 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单号 | order\_no | String | 40 | y | 入库单号 |
| 入库单状态 | status | Int | 4 | y | 入库单状态<br>10:已取消；20:编辑中；30:待处理/待审核；80:已完成 |
| 关联类型 | attach\_type | Int | 4 | N | 关联类型<br>0:手动关联；1:强制关联；2:拆分关联；3:自动关联（客户端为空不返回） |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | y | 仓库名称 |
| 制单时间 | created\_time | String | 40 | y | 入库单创建时间（毫秒级时间戳，例如：1631861379000） |
| 备注 | remark | String | 255 | y | 备注 |
| 分销商昵称 | fenxiao\_nick | String | 40 | y | 分销商昵称 |
| 入库人 | operator\_name | String | 40 | y | 入库人 |
| 入库人id | operator\_id | Int |  | y | 入库人id |
| 物流方式 | logistics\_type | Int | 6 | y | 物流方式，点击查看 [物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) |
| 物流公司 | logistics\_name | String | 40 | y | 物流公司名称 |
| 物流单号 | logistics\_no | String | 40 | y | 物流单号 |
| 物流id | logistics\_id | Int | 6 | y | 物流公司唯一键 |
| 审核时间 | check\_time | String | 40 | y | 审核时间（毫秒级时间戳，例如：1631861379000） |
| 退换单号 | refund\_no | String | 40 | y | 退换单号 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量 |
| 退换单实际退款金额 | actual\_refund\_amount | Decimal(19,4) |  | y | 退换单实际退款金额 |
| 客户编码 | customer\_no | String | 40 | y | 客户编码 |
| 退货人姓名 | customer\_name | String | 100 | y | 退货人姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 客户网名 | nick\_name | String | 100 | y | 客户网名（仅自有平台及线下平台返回，其他平台均不返回） |
| 店铺名称 | shop\_name | String | 128 | y | 店铺名称 |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺备注 | shop\_remark | String | 255 | y | 店铺备注 |
| 标记名称 | flag\_name | String | 32 | y | 标记名称（退换单标记） |
| 系统订单编号 | trade\_no\_list | String | 255 | y | 系统订单编号，若为多个以“，”分割，超长会被截取 |
| 原始订单 | tid\_list | String | 255 | y | 原始单号，若为多个以“，”分割，超长会被截取 |
| 退换单id | src\_order\_id | Int | 11 | y | 退换单主键 |
| 入库单id | stockin\_id | Int | 11 | y | 入库单id |
| 店铺平台id | shop\_platform\_id | Int | 6 | y | 店铺平台id，点击 [文档](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看平台id对照表 |
| 子平台id | sub\_platform\_id | Int | 6 | y | 子平台id |
| 店铺id | shop\_id | Int | 6 | y | 店铺唯一键 |
| 仓库id | warehouse\_id | Int | 40 | y | 仓库唯一键 |
| 入库单总成本 | total\_price | Decimal(19,4) |  | y | 入库单总成本<br>子单明细total\_cost的总和 |
| 货品入库总数量 | total\_goods\_stockin\_num | Decimal(19,4) |  | y | 货品入库总数量 |
| 退换单状态 | process\_status | Int | 4 | y | 10:已取消;20:待审核;30:已审核;40:已推送;80:已结算;85:待过账;86:已过账;87:成本确认;90:已完成 |
| 修改时间 | modified | String | 40 | y | 退货入库单修改时间, 样例: 2020-04-23 14:55:08 |
| 审核人 | check\_operator\_name | String | 40 | y | 审核人 |
| 审核人id | check\_operator\_id | Int |  | y | 审核人id |
| 退换说明 | reason | String | 40 | y | 退换说明 |
| 退换说明id | reason\_id | Int |  | y | 退换说明id |
| 入库总金额 | refund\_amount | Decimal(19,4) |  | y | 入库单明细的（价格\*入库数量）之和 |
| 调整数量 | adjust\_num | Decimal(19,4) |  | y | 调整数量 |
| wms业务单号 | wms\_code | String | 50 | y | wms业务单号 |
| 创建时间 | created | String |  | y | 创建时间 |
| 标记id | flag\_id | Int | 6 | y | 标记id（入库单标记id） |
| 货品类型数量 | goods\_type\_count | Int | 6 | y | 货品类型数量 |
| 退换单编号 | src\_order\_no | String | 40 | y | 退换单编号 |
| 便签条数 | note\_count | Int | 6 | y | 便签条数 |
| 源预入库单号 | prop3 | String | 255 | Y | 预入库单拆分前的预入库单号 |
| 业务单类型 | src\_order\_type | Int | 4 | y | 业务单类型，固定12 |
| 类型 | type | Int | 4 | y | 2：退货退款<br>3：换货 |
| 货品退款金额 | sum\_refund\_amount | Decimal(19,4) |  | y | 货品退款金额 |
| 关联时间 | contact\_time |  |  | y | 关联时间（日志中第一次关联的时间） |
| 分销商编码 | fenxiao\_nick\_no | String |  | y | 分销商编码 |
| 退货货品金额 | total\_amount | Decimal(19,4) |  | y | 退货货品金额 |
| 虚拟仓编码 | vir\_warehouse\_no | String |  | n | 虚拟仓编码 |
| 虚拟仓名称 | vir\_warehouse\_name | String |  | n | 虚拟仓名称 |
| 入库单明细 | details\_list | List<Map<String, Object>> |  | y | 入库单明细 |
| 国补信息 | gov\_subsidy\_info | List<Map<String, Object>> |  | n | 国补信息 |

**summary\_data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String |  | 是 | 仓库编号 |
| 店铺维度分组汇总 | shop\_data | List<shop\_data> |  | 是 | 店铺维度分组汇总 |

**shop\_data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String |  | 是 | 店铺编号 |
| 单品数据汇总 | spec\_data | List<spec\_data> |  | 是 | 单品数据汇总 |

****spec\_data****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String |  | 是 | 商家编码 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 退款金额 | total\_refund\_amount | Decimal(19,4) |  |  | 退款金额 |

****details\_list****

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单明细id(主键) | rec\_id | Int | 11 | 是 | 入库单明细ID（主键） |
| 入库单id | stockin\_id | Int | 11 | 是 | 入库单ID |
| 退换单明细id | refund\_detail\_id | String |  | 是 | 退换单明细id,id之间用逗号分隔 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量（退货入库单明细节点的数量字段） |
| 总成本 | total\_cost | Decimal(19,4) |  | 是 | 总成本=明细数量\*成本（以系统配置决定是实际成本/计划成本） |
| 备注 | remark | String | 255 | 是 | 备注 |
| 调整后数量 | right\_num | Decimal(19,4) |  | 是 | 调整后数量 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品编码 | goods\_no | String | 40 | 是 | 货品编码 |
| 货品id | goods\_id | Int |  | 是 | 货品唯一键 |
| 商品id | spec\_id | Int |  | 是 | 单品唯一键 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 是否残次品 | defect | boolean | 1 | 是 | 默认为非残次品 |
| 单品自定义属性1 | prop1 | String | 100 | 是 | 单品自定义属性1（来源货品档案） |
| 单品自定义属性2 | prop2 | String | 100 | 是 | 单品自定义属性2（来源货品档案） |
| 单品自定义属性3 | prop3 | String | 100 | 是 | 单品自定义属性3（来源货品档案） |
| 单品自定义属性4 | prop4 | String | 100 | 是 | 单品自定义属性4（来源货品档案） |
| 单品自定义属性5 | prop5 | String | 100 | 是 | 单品自定义属性5（来源货品档案） |
| 单品自定义属性6 | prop6 | String | 100 | 是 | 单品自定义属性6（来源货品档案） |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 品牌编号 | brand\_no | String | 32 | 是 | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 辅助单位 | goods\_unit | String | 20 | 是 | 辅助单位（入库单对应的辅助单位） |
| 物流名称 | logistics\_name | String | 40 | 是 | 物流名称 |
| 物流单号 | logistics\_no | String | 40 | 是 | 物流单号 |
| 仓库id | warehouse\_id | Int | 40 | 是 | 仓库唯一键 |
| 退换单id | src\_order\_id | Int | 6 | 是 | 退换单主键 |
| 物流id | logistics\_id | Int | 6 | 是 | 物流公司唯一键 |
| 单位 | base\_unit\_name | String | 20 | 是 | 基本单位 |
| 批次号 | batch\_no | String | 40 | 是 | 批次号 |
| 有效期 | expire\_date | String | 40 | 是 | 有效期，样例: 2020-04-20 00:00:00 |
| 生产日期 | production\_date | String | 40 | 是 | 生产日期 |
| 货位 | position\_no | String | 20 | 是 | 货位 |
| 预期数量 | expect\_num | Decimal(19,4) |  | 是 | 预期数量 |
| 入库数量 | stockin\_num | Decimal(19,4) |  | 是 | 入库数量（关联其他数据出来的数量，如需按照ERP退货入库单明细中的数量取值，取num字段对应值即可） |
| 入库单明细成本价 | checked\_cost\_price | Decimal(19,4) |  | 是 | 入库单明细成本价 |
| 退款总额 | refund\_amount | Decimal(19,4) |  | 是 | 退款总额（入库单明细节点的退款总额） |
| sn序列号信息 | sn\_list | String | 255 | 是 | 当need\_sn=true时返回英文逗号分隔的sn |
| 入库单位id | unit\_id | Int | 6 | 是 | 入库单位id |
| 基本单位id | base\_unit\_id | Int | 6 | 是 | 基本单位id |
| 库存明细id | org\_stockin\_detail\_id | Int | 11 | 是 | 库存明细id |
| 批次id | batch\_id | Int | 11 | 是 | 批次id |
| 货位id | position\_id | Int | 11 | 是 | 货位id |
| 有效期天数 | validity\_days | Int | 6 | 是 | 有效期天数 |
| 辅助数量 | num2 | Decimal(19,4) |  | 是 | 辅助数量 |
| 调整数量 | adjust\_num | Decimal(19,4) |  | 是 | 调整数量 |
| 单位换算关系 | unit\_ratio | Decimal(19,4) |  | 是 | 单位换算关系 |
| 最后修改时间 | modified | String | 40 | 是 | 最后修改时间 |
| 创建时间 | created | String | 40 | 是 | 创建时间 |
| 业务单类型 | src\_order\_type | Int | 4 | 是 | 业务单类型，固定12 |
| 自定义金额1 | customer\_price1 | Decimal(19,4) |  | 是 | 单品自定义金额1 |
| 自定义金额2 | customer\_price2 | Decimal(19,4) |  | 是 | 单品自定义金额2 |
| 原始单号 | tid | String | 255 | 是 | 原始单号，多个用英文逗号隔开 |
| 退款金额 | actual\_refund\_amount | Decimal(19,4) |  | 是 | 退款金额（入库单明细节点的退款金额） |
| 原价 | original\_price | Decimal(19,4) |  | 是 | 原价（退换单明细的原价字段） |
| 退换单明细 | refund\_order\_detail\_list | List<Map<String, Object>> |  | 是 | 退换单明细 |

**gov\_subsidy\_info**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始单号 | tid | String |  | 是 | 原始单号 |
| --- | --- | --- | --- | --- | --- |
| 原始子单号 | oid | String |  | 是 | 原始子单号 |
| --- | --- | --- | --- | --- | --- |
| 公司主体名称 | corp\_entity\_name | String |  | 是 | 公司主体名称 |
| --- | --- | --- | --- | --- | --- |

**refund\_order\_detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单明细id | refund\_order\_id | Int | 11 | 是 | 退换单明细id |
| 入库单明细id | stockin\_order\_detail\_id | Int | 11 | 是 | 入库单明细id |
| 价格 | price | Decimal(19,4) |  | 是 | 价格（退换单明细价格字段） |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 实际入库数量 | stockin\_num | Decimal(19,4) |  | 是 | 实际入库数量 |
| 订单类型 | trade\_type | Int |  | 是 | 通过中间表关联到的退换单明细中后关联订单，关联不到的情况下值为0<br>1：网店销售<br>2：线下订单<br>3：售后换货<br>4：批发业务<br>5：保修换新<br>6：保修完成<br>7：现款销售<br>8：分销<br>101~110：自定义1~10 |
| 入库数量 | refund\_order\_stockin\_num | Decimal(19,4) |  | 是 | 退换单明细中记录的入库数量, 在和中间表关联失败时数量为0 |
| 原始子单号 | oid | String | 40 | 是 | 通过中间表关联到的退换单明细中的oid, 关联不到的情况下值为空串 |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 平台货品id | api\_goods\_id | String |  | 否 | 平台货品id |
| 平台规格id | api\_spec\_id | String |  | 否 | 平台规格id |
| 平台货品名称 | api\_goods\_name | String |  | 否 | 平台货品名称 |
| 平台规格名称 | api\_spec\_name | String |  | 否 | 平台规格名称 |
| 退款总额 | total\_amount | Decimal(19,4) |  | 是 | 退换单明细的退款总额 |
| 退款金额 | refund\_amount | Decimal(19,4) |  | 是 | 退换单明细的退换金额 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryWithDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryWithDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryWithDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryWithDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>`"start_time"``:``"2019-09-01 00:00:00"``,`<br>`"end_time"``:``"2019-10-01 23:59:59"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$paraMap =``new``stdClass();`<br>`$paraMap->start_time =``"2019-09-01 00:00:00"``;`<br>`$paraMap->end_time =``"2019-10-01 23:59:59"``;`<br>``<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$response = $client->pageCall(``"wms.stockin.Refund.queryWithDetail"``,$pager, $paraMap);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryWithDetail#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"summary_data"``: [`<br>```{`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"shop_data"``: [`<br>```{`<br>```"spec_data"``: [`<br>```{`<br>```"num"``: 2,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"total_refund_amount"``: 0`<br>```}`<br>```],`<br>```"shop_no"``:``"wdtapi3-test"`<br>```}`<br>```]`<br>```}`<br>```],`<br>```"total_count"``: 1,`<br>```"order"``: [`<br>```{`<br>```"logistics_name"``:``"无"``,`<br>```"details_list"``: [`<br>```{`<br>```"stockin_id"``: 55185,`<br>```"num"``: 2,`<br>```"remark"``:``""``,`<br>```"right_num"``: 2,`<br>```"rec_id"``: 202147,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"defect"``:``false``,`<br>```"prop2"``:``""``,`<br>```"spec_name"``:``"wangdiantong"``,`<br>```"spec_code"``:``"wangdiantong"``,`<br>```"batch_no"``:``""``,`<br>```"brand_no"``:``"BRAND"``,`<br>```"brand_name"``:``"无"``,`<br>```"unit_id"``: 0,`<br>```"base_unit_id"``: 37,`<br>```"expire_date"``:``""``,`<br>```"position_no"``:``"销退暂存"``,`<br>```"logistics_id"``: 0,`<br>```"logistics_no"``:``""``,`<br>```"src_order_id"``: 57759,`<br>```"warehouse_id"``: 311,`<br>```"goods_id"``: 1,`<br>```"spec_id"``: 1,`<br>```"expect_num"``: 10,`<br>```"org_stockin_detail_id"``: 201850,`<br>```"batch_id"``: 0,`<br>```"position_id"``: -5,`<br>```"validity_days"``: 0,`<br>```"num2"``: 2,`<br>```"adjust_num"``: 0,`<br>```"unit_ratio"``: 1,`<br>```"modified"``:``"2024-08-30 17:38:45"``,`<br>```"created"``:``"2024-08-30 17:38:35"``,`<br>```"src_order_type"``: 12,`<br>```"prop1"``:``""``,`<br>```"prop3"``:``""``,`<br>```"prop4"``:``""``,`<br>```"prop5"``:``""``,`<br>```"prop6"``:``""``,`<br>```"custom_price1"``: 0,`<br>```"custom_price2"``: 0,`<br>```"tid"``:``"20240830001"``,`<br>```"refund_order_detail_list"``: [`<br>```{`<br>```"refund_order_id"``: 60180,`<br>```"stockin_order_detail_id"``: 202147,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"stockin_num"``: 2,`<br>```"oid"``:``"AD202408300004"``,`<br>```"trade_type"``: 2,`<br>```"refund_order_stockin_num"``: 2,`<br>```"price"``: 29.98`<br>```}`<br>```],`<br>```"goods_unit"``:``"无"``,`<br>```"base_unit_name"``:``"KG"``,`<br>```"logistics_name"``:``"无"``,`<br>```"total_cost"``: 0.2366,`<br>```"checked_cost_price"``: 0.1167,`<br>```"refund_amount"``: 59.96,`<br>```"refund_detail_id"``:``"60180"``,`<br>```"production_date"``:``""``,`<br>```"stockin_num"``:``"2.0000"`<br>```}`<br>```],`<br>```"fenxiao_nick"``:``""``,`<br>```"reason"``:``"无"``,`<br>```"operator_id"``: 502,`<br>```"refund_no"``:``"TK2408300021"``,`<br>```"adjust_num"``: 0,`<br>```"shop_remark"``:``"ljcs"``,`<br>```"modified"``:``"2024-08-30 17:38:45"``,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"check_operator_name"``:``"aaa2"``,`<br>```"seq_no"``: 1,`<br>```"created_time"``: 1725010715000,`<br>```"stockin_id"``: 55185,`<br>```"customer_no"``:``"KH201709190002"``,`<br>```"src_order_id"``: 57759,`<br>```"created"``:``"2024-08-30 17:38:35"``,`<br>```"trade_no_list"``:``"JY202408300111"``,`<br>```"shop_name"``:``"wdtapi3-test"``,`<br>```"shop_platform_id"``: 127,`<br>```"shop_id"``:``"290"``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"actual_refund_amount"``: 299.8,`<br>```"nick_name"``:``"aaa"``,`<br>```"process_status"``: 30,`<br>```"status"``: 80,`<br>```"check_time"``: 1725010725000,`<br>```"order_no"``:``"RK2024083013"``,`<br>```"flag_id"``: 0,`<br>```"tid_list"``:``"20240830001"``,`<br>```"goods_type_count"``: 1,`<br>```"remark"``:``""``,`<br>```"sub_platform_id"``: 0,`<br>```"goods_count"``: 2,`<br>```"flag_name"``:``""``,`<br>```"logistics_id"``: 0,`<br>```"src_order_no"``:``"TK2408300021"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"check_operator_id"``: 502,`<br>```"refund_amount"``: 59.96,`<br>```"note_count"``: 0,`<br>```"total_price"``: 0.2366,`<br>```"logistics_no"``:``""``,`<br>```"src_order_type"``: 12,`<br>```"reason_id"``: 0,`<br>```"prop3"``:``""``,`<br>```"operator_name"``:``"aaa2"``,`<br>```"total_goods_stockin_num"``:``"2.0000"``,`<br>```"customer_name"``:``""``,`<br>```"warehouse_id"``: 311`<br>```}`<br>```]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Refund.queryWithDetail#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"仓库不存在"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

4.响应参数

4.响应参数

4.响应参数

4.响应参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1