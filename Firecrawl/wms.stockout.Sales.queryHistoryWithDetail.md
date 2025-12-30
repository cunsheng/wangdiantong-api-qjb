---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryHistoryWithDetail"
title: "API文档"
---
****wms.stockout.Sales.queryHistoryWithDetail**（历史销售出库单查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP历史销售出库单信息 |
| **1.2 适用版本：** 客户端 V1.4.1.3及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为60分钟。 |
| **1.5注意事项：权限校验：【店铺、仓库权限】**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据， **淘系** **相关平台规则** [点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")， **淘系数据获取办法** **[点击这里，拼多多请自行对接平台获取。](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")**<br>本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。具体字段详情见下面表格； |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 买家昵称 | nick\_name |
| 收件人姓名 | receiver\_name |
| 收件地址 | receiver\_address |
| 收件人手机 | receiver\_mobile |
| 收件人固话 | receiver\_telno |
| 客户姓名 | customer\_name |
| 证件号码 | id\_card |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

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
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | y | 起始时间, status\_type =1,2 按照出库单修改时间查询, status\_type=0 按照发货时间查询 |
| 结束时间 | end\_time | String | 40 | y | 结束时间 |
| 出库单状态 | status\_type | Int | 4 | y | 出库单状态: 默认值为.已取消<br>2.在企业版状态中对应status=55(已确认),这里为 待分配~延时发货<br>0.已发货 |
| 仓库编码 | warehouse\_no | String | 40 | n | 仓库编码 |
| 出库单编号 | stockout\_no | String | 20 | n | 出库单编号 |
| 店铺编号 | shop\_nos | String | 255 | n | 多个店铺编号使用英文逗号分隔 |
| 销售订单号 | src\_order\_no | String | 40 | n | 系统订单号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | n | 分页大小（单量较大的卖家，page\_size建议200以下） |
| 页号 | page\_no | Int | 4 | n | 从0开始 |

**4.响应参数**

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 出库单信息 | data | Map<String, Object> |  | n | 出库信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | n | 查询条件总单据数 |
| 单据数据 | order | List<Map<String, Object>> |  | y | 出库单相关数据 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单ID | stockout\_id | Int | 11 | y | 出库单ID |
| 出库单号 | order\_no | String | 40 | y | 出库单号 |
| 系统订单编号 | src\_order\_no | String | 40 | y | 系统订单编号 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | y | 仓库名称 |
| 发货时间 | consign\_time | String | 40 | y | 发货时间，例如：2020-01-28 16:12:01 |
| 源单据类别 | order\_type | Int | 4 | y | 源单据类别:<br>1销售订单<br>2调拨出库<br>3采购退货出库<br>4盘亏出库<br>5生产出库<br>6现款销售出库<br>7其他出库 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量 |
| 物流单编号 | logistics\_no | String | 50 | y | 物流单编号 |
| 收件人姓名 | receiver\_name | String | 100 | y | 收件人姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 国家 | receiver\_country | Int | 11 | y | 国家 |
| 省份ID | receiver\_province | Int | 11 | y | 省份ID |
| 城市ID | receiver\_city | Int | 11 | y | 城市ID |
| 地区ID | receiver\_district | Int | 11 | y | 地区ID |
| 地址 | receiver\_address | String | 256 | y | 地址，不包含省市区（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人手机 | receiver\_mobile | String | 40 | y | 收件人手机（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人电话 | receiver\_telno | String | 100 | y | 收件人电话（仅自有平台及线下平台返回，其他平台均不返回） |
| 收件人邮编 | receiver\_zip | String | 20 | y | 收件人邮编 |
| 省市区 | receiver\_area | String | 128 | y | 省市区空格分隔 |
| 出库单备注 | remark | String | 255 | y | 出库单备注 |
| 称重结果 | weight | Decimal(19,4) |  | y | 称重结果（实际称重重量kg） |
| 截停原因 | block\_reason | Int | 11 | y | 截停原因:<br>0正常<br>1申请退款<br>2已退款<br>4地址被修改<br>8发票被修改<br>16物流被修改<br>32仓库变化<br>64备注修改<br>128更换货品<br>256取消退款 |
| 物流方式 | logistics\_type | Int | 6 | y | 物流方式 |
| 物流编号 | logistics\_code | String | 40 | y | 物流编号 |
| 物流公司名称 | logistics\_name | String | 40 | y | 物流公司名称 |
| 异常原因 | bad\_reason | Int | 4 | y | 异常原因:  <br>0正常<br>1无库存记录<br>2地址发生变化<br>4发票变化<br>8仓库变化<br>16备注变化<br>32平台更换货品<br>64退款 |
| 大头笔 | receiver\_dtb | String | 128 | y | 大头笔 |
| 退款状态 | refund\_status | Int | 4 | y | 退款状态:<br>0无退款<br>1申请退款<br>2部分退款<br>3全部退款 |
| 销售类型 | trade\_type | Int | 4 | y | 销售类型:<br>1网店销售<br>2线下零售<br>3售后换货<br>4批发业务 |
| 业务员编号 | salesman\_no | String | 40 | y | 业务员编号 |
| 业务员姓名 | fullname | String | 40 | y | 业务姓名 |
| 订单状态 | trade\_status | Int | 4 | y | 订单状态:  <br>4 线下退款<br>5已取消<br>6 待确认订单, 导入放入这个状态  待转预订单(待审核)<br>7待确认订单,导入时先放到这个状态（此状态不占用库存,可删除,离开这个状态就不能删除了)<br>10待付款<br>15等未付<br>16延时审核<br>19预订单前处理<br>20前处理(赠品，合并，拆分)<br>21委外前处理<br>23 异常预订单<br>24 换货预订单<br>26 待激活预订单<br>27待分配预<br>30待客审<br>35待财审<br>55已确认<br>95已发货<br>96 待录入计划成本，订单结算时有货品无计划成本<br>99 待过账<br>100已签收<br>101 已过账<br>105部分打款<br>110已完成 |
| 订单编号 | trade\_no | String | 40 | y | 订单编号 |
| 原始单号 | src\_trade\_no | String | 255 | y | 原始单号(如果有多个，以","分隔且以增序排列,不重复,过长将被裁剪) |
| 客户网名 | nick\_name | String | 100 | y | 客户网名（仅自有平台及线下平台返回，其他平台均不返回） |
| 客户编码 | customer\_no | String | 40 | y | 客户编码 |
| 客户姓名 | customer\_name | String | 100 | y | 客户姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 下单时间 | trade\_time | String | 40 | y | 下单时间（毫秒级时间戳，例如：1631861379000） |
| 支付时间 | pay\_time | String | 40 | y | 支付时间（毫秒级时间戳，例如：1631861379000） |
| 标记名称 | flag\_name | String | 32 | y | 标记名称 |
| 邮费 | post\_amount | Decimal(19,4) |  | y | 邮费 |
| 证件类别 | is\_card\_type | Int | 4 | y | 证件类别 |
| 证件号码 | id\_card | String | 40 | y | 证件号码（仅自有平台及线下平台返回，其他平台均不返回） |
| 店铺名称 | shop\_name | String | 128 | y | 店铺名称 |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺备注 | shop\_remark | String | 255 | y | 店铺备注 |
| 出库单状态 | status | Int | 4 | y | 出库单状态:  <br>5已取消<br>10待放回(拣货待放回), 小于该值的都是已取消的单子<br>48 未确认 <br>50待审核<br>51 缺货无法发货<br>54 获取面单号<br>60 待分配,电子面单获取成功后<br>61 排队中,将出库单加入到队伍中<br>65待人工处理  <br>75待拣货,创建批次之后<br>77 拣货中,PDA拣货后<br>79 已拣货<br>90延时发货, 到指定时间后会自动发货<br>95已发货<br>110已完成 |
| 发票类型 | invoice\_type | Int | 4 | y | 发票类型:<br>0不需要<br>1普通发票<br>2增值税发票 |
| 发票ID | invoice\_id | Int | 11 | y | 发票id:<br>目前只设0-1，<br>1表示已开发票 |
| 货到付款金额 | cod\_amount | Decimal(19,4) |  | y | 货到付款金额 |
| 发货条件 | delivery\_term | Int | 4 | y | 发货条件:<br>1款到发货<br>2货到付款(包含部分货到付款)<br>3分期付款 |
| 平台ID | platform\_id | Int | 11 | y | 平台ID（请点击 [平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看对应关系） |
| 订单ID | trade\_id | Int | 11 | y | 订单ID |
| 审核员编号 | employee\_no | String | 40 | y | 审核员编号 |
| 优惠金额 | discount | Decimal(19,4) |  | y | 优惠金额 |
| 税额 | tax | Decimal(19,4) |  | y | 税额 |
| 税率 | tax\_rate | Decimal(19,4) |  | y | 税率 |
| 币种 | currency | String | 20 | y | 币种 |
| 建单时间 | created | String | 40 | y | 建单时间（毫秒级时间戳，例如：1631861379000） |
| 出库单建单时间 | stock\_check\_time | String | 40 | y | 出库单建单时间（毫秒级时间戳，例如：1631861379000） |
| 打印备注 | print\_remark | String | 255 | y | 打印备注 |
| 买家留言 | buyer\_message | String | 255 | y | 买家留言 |
| 客服备注 | cs\_remark | String | 255 | y | 客服备注 |
| 发票标题 | invoice\_title | String | 255 | y | 发票标题 |
| 发票内容 | invoice\_content | String | 255 | y | 发票内容 |
| 称重预估邮资 | post\_fee | Decimal(19,4) |  | y | 称重预估邮资<br>(使用根据重量预估的邮费) |
| 包装成本 | package\_fee | Decimal(19,4) |  | y | 包装成本(使用包装的计划成本) |
| 已付金额 | receivable | Decimal(19,4) |  | y | 已付金额(使用应收金额) |
| 总成本价 | goods\_total\_cost | Decimal(19,4) |  | y | 总成本价 |
| 总货款 | goods\_total\_amount | Decimal(19,4) |  | y | 总货款 |
| 最后修改时间 | modified | String | 40 | y | 最后修改时间，例如：2020-01-28 16:12:01 |
| 订单标签 | trade\_label | String | 11 | y | 订单标签 |
| 订单来源 | trade\_from | Int | 4 | y | 订单来源：<br>1、API抓单<br>2、手工建单<br>3、导入<br>4、复制订单<br>5、接口推送<br>6、补发订单<br>7、PDA选货开单 |
| 店铺平台ID | shop\_platform\_id | int |  | y | 店铺平台类型ID |
| 店铺ID | shop\_id | int |  | y | 店铺id |
| 查询的记录数 | seq\_no | int |  | y | 返回分页页数\*一页条数 +1 |
| 物流id | logistics\_id | int |  | y | 物流id |
| 仓库id | warehouse\_id | int |  | y | 仓库id |
| 销售出库单详情 | details\_list | List<Map<String, Object>> |  | y | 销售出库单详情 |
| 物流单列表 | logistics\_list | List<Map<String, Object>> |  | y | 物流单详情 |

**logistics\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流单id | rec\_id | Int | 11 | y | 销售出库单详情id |
| 出库单id | stockout\_id | Int | 11 | y | 出库单id |
| 物流单号 | logistics\_no | String | 40 | y | 物流单号 |
| 估算重量 | calc\_weight | Decimal(19,4) |  | y | 估算重量 |
| 称重重量 | weight | Decimal(19,4) |  | y | 称重重量 |
| 包装 | package\_name | String | 40 | y | 包装 |
| 物流名称 | logistics\_name | String | 40 | y | 物流公司名称（查看路径：旺店通客户端设置--基本设置--物流） |
| 物流ID | logistics\_id | Integer | 6 | y | 物流ID |
| 估算邮资 | postage | BigDecimal | 19,4 | y | 估算邮资 |
| 备注 | remark | String | 256 | y | 备注 |
| 长 | length | BigDecimal | 19,4 | y | 长 |
| 宽 | width | BigDecimal | 19,4 | y | 宽 |
| 高 | height | BigDecimal | 19,4 | y | 高 |
| 体积 | volume | BigDecimal | 19,4 | y | 长\*宽\*高 |

**details\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 销售出库单详情的id | rec\_id | Int | 11 | y | 销售出库单详情的id |
| 订单明细id | src\_order\_detail\_id | Int | 11 | y | 订单明细id |
| 出库单id | stockout\_id | Int | 11 | y | 出库单id |
| 规格id | spec\_id | Int | 11 | y | 规格id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量:  如果按照货位分组就是总货品数量 |
| 总成本 | total\_amount | Decimal(19,4) |  | y | 总成本: 成本价\*货品数量 |
| 已支付金额 | paid | Decimal(19,4) |  | y | 已支付金额:<br>如果按照货位分组就是总的已经支付的金额 |
| 成交价 | sell\_price | Decimal(19,4) |  | y | 成交价 |
| 出库单明细备注 | remark | String | 255 | y | 出库单明细备注 |
| 货品名称 | goods\_name | String | 255 | y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | y | 货品编号 |
| 规格名称 | spec\_name | String | 100 | y | 规格名称 |
| 规格码 | spec\_code | String | 40 | y | 规格码 |
| 成本价 | cost\_price | Decimal(19,4) |  | y | 成本价:<br>平均成本如果为空或者小于0,就是计划成本 |
| 总重量 | weight | Decimal(19,4) | 11 | y | 总重量 |
| 货品id | goods\_id | Int | 11 | y | 货品id |
| 规格自定义属性1 | prop1 | String | 255 | y | 规格自定义属性1 |
| 规格自定义属性2 | prop2 | String | 255 | y | 规格自定义属性2 |
| 规格自定义属性3 | prop3 | String | 255 | y | 规格自定义属性3 |
| 规格自定义属性4 | prop4 | String | 255 | y | 规格自定义属性4 |
| 规格自定义属性5 | prop5 | String | 255 | y | 规格自定义属性5 |
| 规格自定义属性6 | prop6 | String | 255 | y | 规格自定义属性6 |
| 平台ID | platform\_id | Int | 6 | y | 平台ID |
| 退款状态 | refund\_status | Int | 4 | y | 退款状态:<br>0无退款<br>1取消退款,<br>2已申请退款<br>3等待退货<br>4等待收货<br>5退款成功---(原始子订单关闭，这里也是退款状态) |
| 销售单价 | market\_price | Decimal(19,4) |  | y | 销售单价:<br>手工新建时使用货品属性中的“零售价” |
| 总折扣金额 | discount | Decimal(19,4) |  | y | 总折扣金额 |
| 分摊后合计应收 | share\_amount | Decimal(19,4) |  | y | 分摊后合计应收 |
| 税率 | tax\_rate | Decimal(8,4) |  | y | 税率 |
| 主条码 | barcode | String | 50 | y | 主条码 |
| 单位名称 | unit\_name | String | 20 | y | 单位名称 |
| 订单货品(子订单)id | sale\_order\_id | Int | 11 | y | 订单货品(子订单)id |
| 是否是赠品 | gift\_type | Int | 11 | y | 是否是赠品:<br>0非赠品<br>1自动赠送<br>2手工赠送<br>4周期购赠送<br>8平台赠送 |
| 原始子单号 | src\_oid | String | 40 | y | 原始子单号 |
| 原始单号 | src\_tid | String | 40 | y | 原始单号 |
| 订单内部来源 | from\_mask | Int | 11 | y | 订单内部来源:<br>1手机<br>2聚划算 |
| 货品类型 | goods\_type | Int | 4 | y | 货品类型:<br>1销售商品<br>2原材料<br>3包装<br>4周转材料<br>5虚拟商品<br>6固定资产<br>0其它 |
| 货品自定义属性1 | good\_prop1 | String | 255 | y | 货品自定义属性1 |
| 货品自定义属性2 | good\_prop2 | String | 255 | y | 货品自定义属性2 |
| 货品自定义属性3 | good\_prop3 | String | 255 | y | 货品自定义属性3 |
| 货品自定义属性4 | good\_prop4 | String | 255 | y | 货品自定义属性4 |
| 货品自定义属性5 | good\_prop5 | String | 255 | y | 货品自定义属性5 |
| 货品自定义属性6 | good\_prop6 | String | 255 | y | 货品自定义属性6 |
| 批次号 | batch\_no | String | 20 | y | 批次号 |
| 有效期 | expire\_date | String | 20 | y | 有效期 |
| 是否包装 | is\_package | boolean | 1 | y | 是否包装<br>true:是<br>false:否 |

**5.请求示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryHistoryWithDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryHistoryWithDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryHistoryWithDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryHistoryWithDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2018-10-05 14:21:41"``,``"end_time"``:``"2018-10-20 14:21:41"``}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>`$pars``=``array`<br>`(`<br>```'start_time'``=>``'2020-06-15 10:05:36'``,`<br>```'end_time'``=>``'2020-06-17 11:05:36'`<br>`);`<br>`$pager``=``new``Pager(50, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.Sales.queryHistoryWithDetail"``,``$pager``,``$pars``);``//分页方法`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>``<br>`?>` |

### **6.响应示例**

#### 6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryHistoryWithDetail#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [`<br>```{`<br>```"post_amount"``: 10.0000,`<br>```"fenxiao_nick"``:``""``,`<br>```"trade_time"``: 1598233470000,`<br>```"error_info"``:``""``,`<br>```"bad_reason"``: 0,`<br>```"discount"``: 0.0000,`<br>```"picker_name"``:``"系统用户"``,`<br>```"trade_id"``: 595978,`<br>```"trade_label"``:``""``,`<br>```"receiver_country"``: 0,`<br>```"refund_status"``: 0,`<br>```"receiver_province"``: 330000,`<br>```"buyer_message"``:``""``,`<br>```"logistics_code"``:``"momo1"``,`<br>```"shop_platform_id"``: 127,`<br>```"shop_id"``: 290,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"nick_name"``:``"QQP"``,`<br>```"id_card_type"``: 0,`<br>```"status"``: 110,`<br>```"package_fee"``: 0,`<br>```"src_trade_no"``:``"121111111"``,`<br>```"post_fee"``: 0.0000,`<br>```"custom_type"``: 0,`<br>```"sub_platform_id"``: 0,`<br>```"goods_count"``: 2.0000,`<br>```"stockout_id"``: 396275,`<br>```"src_order_no"``:``"ORDER202008240010"``,`<br>```"invoice_content"``:``""``,`<br>```"receiver_name"``:``"QQP"``,`<br>```"currency"``:``""``,`<br>```"sendbill_template_id"``: 0,`<br>```"picklist_no"``:``""``,`<br>```"examiner_name"``:``"系统用户"``,`<br>```"logistics_type"``: 4,`<br>```"trade_from"``: 4,`<br>```"delivery_term"``: 1,`<br>```"logistics_no"``:``"134354646464646"``,`<br>```"consigner_name"``:``"aaa2"``,`<br>```"receiver_district"``: 330109,`<br>```"goods_total_amount"``: 30.0000,`<br>```"receivable"``: 40.0000,`<br>```"receiver_mobile"``:``"12345678900"``,`<br>```"stock_check_time"``: 1598233524000,`<br>```"cs_remark"``:``""``,`<br>```"receiver_address"``:``"牛"``,`<br>```"customer_name"``:``"QQP"``,`<br>```"printer_name"``:``"系统用户"``,`<br>```"customer_id"``: 649926,`<br>```"warehouse_id"``: 311,`<br>```"logistics_name"``:``"陌陌-圆通"``,`<br>```"details_list"``: [`<br>```{`<br>```"rec_id"``: 556013,`<br>```"stockout_id"``: 396275,`<br>```"spec_id"``: 203575,`<br>```"goods_count"``: 1.0000,`<br>```"goods_amount"``: 20.0000,`<br>```"paid"``: 0.0000,`<br>```"sell_price"``: 20.0000,`<br>```"remark"``:``""``,`<br>```"goods_name"``:``"wttABCD"``,`<br>```"goods_no"``:``"wttAABCD"``,`<br>```"spec_name"``:``"wttAABCD"``,`<br>```"spec_code"``:``"wttAABCD"``,`<br>```"spec_no"``:``"wttAABCD"``,`<br>```"cost_price"``: 0.0000,`<br>```"weight"``: 0.0000,`<br>```"total_amount"``: 0.0000,`<br>```"goods_id"``: 54367,`<br>```"prop1"``:``""``,`<br>```"prop2"``:``""``,`<br>```"prop3"``:``""``,`<br>```"prop4"``:``""``,`<br>```"prop5"``:``""``,`<br>```"prop6"``:``""``,`<br>```"platform_id"``: 0,`<br>```"refund_status"``: 0,`<br>```"market_price"``: 20.0000,`<br>```"discount"``: 0.0000,`<br>```"share_amount"``: 20.0000,`<br>```"tax_rate"``: 0.0000,`<br>```"barcode"``:``"wttAABCD"``,`<br>```"unit_name"``:``"部"``,`<br>```"sale_order_id"``: 784940,`<br>```"gift_type"``: 0,`<br>```"src_oid"``:``"AD202008240001"``,`<br>```"src_tid"``:``"121111111"``,`<br>```"from_mask"``: 131072,`<br>```"goods_type"``: 1,`<br>```"batch_no"``:``""``,`<br>```"good_prop1"``:``"P1"``,`<br>```"good_prop2"``:``"P2"``,`<br>```"good_prop3"``:``"P13"``,`<br>```"good_prop4"``:``"P14"``,`<br>```"good_prop5"``:``"P15"``,`<br>```"good_prop6"``:``"P16"``,`<br>```"src_order_detail_id"``: 784940,`<br>```"suite_no"``:``""``,`<br>```"share_post_amount"``: 10.0000,`<br>```"brand_no"``:``"BD202001030001"``,`<br>```"brand_name"``:``"新建品牌3"``,`<br>```"src_order_type"``: 1,`<br>```"base_unit_id"``: 0,`<br>```"unit_id"``: 0,`<br>```"unit_ratio"``: 1.0000,`<br>```"is_package"``:``false``,`<br>```"num2"``: 0.0000,`<br>```"batch_id"``: 0,`<br>```"is_examined"``: 0,`<br>```"scan_type"``: 0,`<br>```"modified_date"``:``"2020-08-24 09:45:23"``,`<br>```"created_date"``:``"2020-08-24 09:45:23"``,`<br>```"share_price"``: 20.0000,`<br>```},`<br>```{`<br>```"rec_id"``: 556014,`<br>```"stockout_id"``: 396275,`<br>```"spec_id"``: 205266,`<br>```"goods_count"``: 1.0000,`<br>```"goods_amount"``: 10.0000,`<br>```"paid"``: 0.0000,`<br>```"sell_price"``: 10.0000,`<br>```"remark"``:``""``,`<br>```"goods_name"``:``"认养一头牛250ml梦幻盖10入内衬"``,`<br>```"goods_no"``:``"30500033"``,`<br>```"spec_name"``:``""``,`<br>```"spec_code"``:``""``,`<br>```"spec_no"``:``"30500033"``,`<br>```"cost_price"``: 0.0000,`<br>```"weight"``: 0.0000,`<br>```"total_amount"``: 0.0000,`<br>```"goods_id"``: 55959,`<br>```"prop1"``:``""``,`<br>```"prop2"``:``""``,`<br>```"prop3"``:``""``,`<br>```"prop4"``:``""``,`<br>```"prop5"``:``""``,`<br>```"prop6"``:``""``,`<br>```"platform_id"``: 0,`<br>```"refund_status"``: 0,`<br>```"market_price"``: 10.0000,`<br>```"discount"``: 0.0000,`<br>```"share_amount"``: 10.0000,`<br>```"tax_rate"``: 0.0000,`<br>```"barcode"``:``"30500033"``,`<br>```"unit_name"``:``"个子"``,`<br>```"sale_order_id"``: 784941,`<br>```"gift_type"``: 0,`<br>```"src_oid"``:``"AD202008240002"``,`<br>```"src_tid"``:``"121111111"``,`<br>```"from_mask"``: 131072,`<br>```"goods_type"``: 1,`<br>```"batch_no"``:``""``,`<br>```"good_prop1"``:``""``,`<br>```"good_prop2"``:``""``,`<br>```"good_prop3"``:``""``,`<br>```"good_prop4"``:``""``,`<br>```"good_prop5"``:``""``,`<br>```"good_prop6"``:``""``,`<br>```"src_order_detail_id"``: 784941,`<br>```"suite_no"``:``""``,`<br>```"share_post_amount"``: 0.0000,`<br>```"brand_no"``:``"BRAND"``,`<br>```"brand_name"``:``"无"``,`<br>```"src_order_type"``: 1,`<br>```"base_unit_id"``: 0,`<br>```"unit_id"``: 0,`<br>```"unit_ratio"``: 1.0000,`<br>```"is_package"``:``false``,`<br>```"num2"``: 0.0000,`<br>```"batch_id"``: 0,`<br>```"is_examined"``: 0,`<br>```"scan_type"``: 0,`<br>```"modified_date"``:``"2020-08-24 09:45:23"``,`<br>```"created_date"``:``"2020-08-24 09:45:23"``,`<br>```"share_price"``: 10.0000,`<br>``<br>```"consign_time"``:``"2020-08-24 09:46:15"``,`<br>```"warehouse_type"``: 1,`<br>```"receiver_dtb"``:``"杭州市 萧山区"``,`<br>```"operator_id"``: 502,`<br>```"print_remark"``:``""``,`<br>```"employee_no"``:``"wtt"``,`<br>```"tax_rate"``: 0.0000,`<br>```"shop_remark"``:``"ljcs"``,`<br>```"outer_no"``:``""``,`<br>```"invoice_id"``: 0,`<br>```"modified"``:``"2020-08-24 09:46:14"``,`<br>```"order_type"``: 1,`<br>```"shop_no"``:``"wdtapi3-test"``,`<br>```"picklist_seq"``: 0,`<br>```"seq_no"``: 1,`<br>```"receiver_area"``:``"浙江省 杭州市 萧山区"``,`<br>```"customer_no"``:``"KH202007270002"``,`<br>```"created"``: 1598233487000,`<br>```"weight"``: 0.0000,`<br>```"block_reason"``: 0,`<br>```"tax"``: 0.0000,`<br>```"shop_name"``:``"wdtapi3-test"``,`<br>```"pay_time"``: 1598233470000,`<br>```"goods_total_cost"``: 0.0000,`<br>```"trade_no"``:``"ORDER202008240010"``,`<br>```"consign_status"``: 0,`<br>```"order_no"``:``"CKDH202008242"``,`<br>```"receiver_city"``: 330100,`<br>```"invoice_title"``:``""``,`<br>```"goods_type_count"``: 2,`<br>```"id_card"``:``""``,`<br>```"remark"``:``""``,`<br>```"calc_post_cost"``: 0.0000,`<br>```"cod_amount"``: 0.0000,`<br>```"flag_name"``:``"无"``,`<br>```"logistics_id"``: 207,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"receiver_telno"``:``""``,`<br>```"receiver_zip"``:``""``,`<br>```"trade_status"``: 110,`<br>```"invoice_type"``: 0,`<br>```"new_trade_label"``:``"0"``,`<br>```"batch_no"``:``""``,`<br>```"packager_name"``:``"系统用户"``,`<br>```"salesman_no"``:``"wtt"``,`<br>```"platform_id"``: 0,`<br>```"paid"``: 0.0000,`<br>```"trade_type"``: 2,`<br>```"logistics_print_status"``: 2,`<br>```"fullname"``:``"aaa1"``,`<br>```"logistics_list"``: [`<br>```{`<br>```"rec_id"``: 10074105,`<br>```"stockout_id"``: 396275,`<br>```"logistics_id"``: 207,`<br>```"logistics_no"``:``"134354646464646"``,`<br>```"calc_weight"``: 0.0000,`<br>```"weight"``: 0.0000,`<br>```"postage"``: 0.0000,`<br>```"remark"``:``""``,`<br>```"length"``: 0.0000,`<br>```"width"``: 0.0000,`<br>```"height"``: 0.0000,`<br>```"package_name"``:``"未知"``,`<br>```"logistics_name"``:``"陌陌-圆通"``,`<br>```"volume"``:``"0.000000000000"`<br>```}`<br>```]`<br>```}`<br>```]`<br>```}`<br>`}` |\
\
#### 6.2 异常响应示例\
\
- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryHistoryWithDetail#autoTab1_0)\
\
|     |     |\
| --- | --- |\
| 1 | `{``"status"``:100,``"message"``:``"您的查询时间过宽,查询时间不能大于30天"``}` |\
\
