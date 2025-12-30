---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryWithDetail"
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

****wms.stockout.Sales.queryWithDetail**（销售出库单查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP销售出库单信息 |
| **1.2 适用版本：** 客户端 V1.5.9.0及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为60分钟。 |
| **1.5注意事项：权限校验：【店铺、仓库权限】**<br>为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据， **相关平台规则** [点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")， **淘系及系统供销平台数据获取办法** **[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")[，拼多多请自行对接平台获取](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")。**<br>本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。具体字段详情见下面表格；<br>通过从后往前翻页的方式可以避免漏单问题。 |

|     |     |
| --- | --- |
| 字段描述 | 字段名 |
| 客户网名 | nick\_name |
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
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | y | 起始时间, status\_type =1,2,3 按照出库单修改时间查询, status\_type=0 按照发货时间查询 |
| 结束时间 | end\_time | String | 40 | y | 结束时间 |
| 出库单状态 | status\_type | Int | 4 | y | 出库单状态: 默认值为0<br>1.已取消<br>2.在企业版状态中对应status=55(已确认),这里为 待分配~延时发货（此条件会返回延时发货状态的订单）<br>3.按照指定的status状态字段查询<br>0.延时发货&已完成 |
| 出库单状态详细 | status | String |  | y | 传status\_type=3情况下，按照修改时间和status查询<br>（status\_type=3的情况下，若不传status字段，按照发货时间查询）<br>出库单状态 **（若多个状态则以“，”隔开）**:  <br>5已取消<br>10待放回(拣货待放回), 小于该值的都是已取消的单子<br>50待审核<br>51缺货<br>52缺货待入库<br>53 WMS已接单<br>54 获取电子面单<br>58 档口锁定<br>60 待分配<br>61 排队中<br>63 待补货<br>65 待处理  <br>70 待发货<br>73 爆款锁定<br>74 预打包<br>75 待拣货<br>77 拣货中,PDA拣货后<br>79 已拣货<br>90 延时发货<br>110已完成<br>-1未发货 |
| 仓库编号 | warehouse\_no | String | 40 | n | 仓库编号 |
| 出库单号 | stockout\_no | String | 20 | n | 出库单号（传入出库单号可以不传时间条件） |
| 店铺编号 | shop\_nos | String |  | n | 多个店铺编号使用英文逗号分隔 |
| 销售订单号 | src\_order\_no | String | 40 | n | 系统订单号（传入ERP订单号可以不传时间条件） |
| 物流单号 | logistics\_no | String | 40 | n | 物流单号（存在匹配的出库单时，可以不传时间条件） |
| 是否返回sn信息 | need\_sn | bool |  | n | true:返回<br>false:不返回 |
| 是否按照货位排序 | position | Int |  | n | 等于0为否，不等于0为是，不填为否 |
| 是否使用从库查询 | is\_slave | boolean | 1 | n | 使用：true  不使用：false<br>(仅对开通从库配置客户生效) |
| 是否获取主播信息 | get\_anchor | boolean |  | n | true:返回   false:不返回 |
| 排序类型 | order\_type | Int | 4 | n | 0：默认<br>1：修改时间降序<br>2：发货时间降序 |
| 是否需要拣货位明细 | need\_pick\_position | Int | 4 | n | 0：不需要（默认）<br>1：需要 |
| 是否需要国补信息 | need\_gov\_subsidy\_info | boolean | 1 | n | 0：不需要（默认）<br>1：需要 |
| 原始单号 | src\_tid | String | 40 | n | 原始单号 |

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
| 虚拟仓编号 | virtual\_warehouse\_no | String | 40 | y | 虚拟仓编号 |
| 虚拟仓名称 | virtual\_warehouse\_name | String | 64 | y | 虚拟仓名称 |
| 系统订单编号 | src\_order\_no | String | 40 | y | ERP系统订单编号 |
| 仓库编号 | warehouse\_no | String | 40 | y | 仓库编号 |
| 仓库名称 | warehouse\_name | String | 64 | y | 仓库名称 |
| 发货时间 | consign\_time | String | 40 | y | 发货时间，订单未发货不返回该字段 例如：2020-09-23 14:56:18 |
| 源单据类别 | order\_type | Int | 4 | y | 1销售订单 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量 |
| 物流单号 | logistics\_no | String | 50 | y | 物流单号 |
| 收件人姓名 | receiver\_name | String | 100 | y | 收件人姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 国家 | receiver\_country | Int | 11 | y | 国家,默认为1 |
| 省份ID | receiver\_province | Int | 11 | y | 省份ID，点击查看 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 城市ID | receiver\_city | Int | 11 | y | 城市ID，点击查看 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地区ID | receiver\_district | Int | 11 | y | 地区ID，点击查看 [城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地址 | receiver\_address | String | 256 | y | 地址，不包含省市区，（**仅自有平台及线下平台返回，其他平台均不返回**） |
| 收件人手机 | receiver\_mobile | String | 40 | y | 收件人手机（**仅自有平台及线下平台返回，其他平台均不返回**） |
| 收件人固话 | receiver\_telno | String | 100 | y | 收件人固话（ **仅自有平****台及线下平台返回，其他平台均不返回**） |
| 收件人邮编 | receiver\_zip | String | 20 | y | 收件人邮编 |
| 省市区 | receiver\_area | String | 128 | y | 省市区空格分隔 |
| 出库单备注 | remark | String | 255 | y | 出库单备注 |
| 重量 | weight | Decimal(19,4) |  | y | 实际称得重量KG |
| 截停原因 | block\_reason | Int | 11 | y | 截停原因:<br>0 正常<br>1 申请退款<br>2 已退款<br>4 地址被修改<br>8 发票被修改<br>16 物流被修改<br>32 仓库变化<br>64 备注修改<br>128 更换货品<br>256 取消退款<br>1024 其它原因<br>2048 拦截赠品<br>8192 修改买家留言<br>16384 平台已发货<br>65536 撤销出库<br>32768 配送时间变更<br>16777216 阶梯满赠赠品重算,发现赠送错误<br>33554432 分销取消<br>1073741824 驳回审核 |
| 物流方式 | logistics\_type | Int | 6 | y | 物流方式，点击 [物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) 查看 |
| 物流编号 | logistics\_code | String | 40 | y | ERP物流编号（查看路径：旺店通客户端设置--基本设置--物流） |
| 物流公司名称 | logistics\_name | String | 40 | y | 物流公司名称（查看路径：旺店通客户端设置--基本设置--物流） |
| 店铺id | shop\_id | Int | 6 | y | 店铺id |
| 仓库id | warehouse\_id | Int | 6 | y | 仓库id |
| 物流id | logistics\_id | Int | 6 | y | 物流id |
| 异常原因 | bad\_reason | Int | 4 | y | 异常原因:  <br>0正常<br>1无库存记录<br>2地址发生变化<br>4发票变化<br>8仓库变化<br>16备注变化<br>32平台更换货品<br>64退款 |
| 大头笔 | receiver\_dtb | String | 128 | y | 大头笔 |
| 退款状态 | refund\_status | Int | 4 | y | 退款状态:<br>0无退款<br>1申请退款<br>2部分退款<br>3全部退款 |
| 销售类型 | trade\_type | Int | 4 | y | 销售类型:<br>1网店销售<br>2线下订单<br>3售后换货<br>4批发业务<br>7现款销售<br>8分销订单<br>101 订单自定义属性1<br>102 订单自定义属性2<br>103 订单自定义属性3<br>104 订单自定义属性4<br>105 订单自定义属性5<br>106 订单自定义属性6<br>107 订单自定义属性7<br>108 订单自定义属性8<br>109 订单自定义属性9<br>110 订单自定义属性10<br>（与ERP中自定义类型的映射关系 [，点击链接查看](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E8%AE%A2%E5%8D%95%E6%9F%A5%E8%AF%A2%E3%80%81%E9%94%80%E5%94%AE%E5%87%BA%E5%BA%93%E5%8D%95)） |
| 业务员编号 | salesman\_no | String | 40 | y | 业务员为"系统"时不返回 |
| 业务员姓名 | fullname | String | 40 | y | 业务员为"系统"时不返回 |
| 拣货员 | picker\_name | String | 50 | y | 拣货员 |
| 验货员 | examiner\_name | String | 50 | y | 验货员 |
| 发货员 | consigner\_name | String | 50 | y | 发货员 |
| 打单员 | printer\_name | String | 50 | y | 打单员 |
| 打包员 | packager\_name | String | 50 | y | 打包员 |
| 订单状态 | trade\_status | Int | 4 | y | 订单状态:  <br>4 线下退款<br>5已取消<br>6 待转预订单(待审核)<br>7 待转已完成<br>10未付款<br>12待尾款<br>15等未付<br>16延时审核<br>19预订单前处理<br>20 审核前处理<br>21自流转待发货<br>23 异常预订单<br>24 换货预订单<br>25 待处理预订单<br>27待分配预订单 <br>30待客审<br>35待财审<br>55已审核<br>95已发货<br>96 成本确认（待录入计划成本，订单结算时有货品无计划成本）<br>101 已过账<br>110已完成 |
| 订单编号 | trade\_no | String | 40 | y | 订单编号 |
| 原始单号 | src\_trade\_no | String | 255 | y | 原始单号(如果有多个，以","分隔且以增序排列,不重复,过长将被裁剪) |
| 客户网名 | nick\_name | String | 100 | y | 客户网名（仅自有平台及线下平台返回，其他平台均不返回） |
| 客户编码 | customer\_no | String | 40 | y | 客户编码 |
| 客户姓名 | customer\_name | String | 100 | y | 客户姓名（仅自有平台及线下平台返回，其他平台均不返回） |
| 下单时间 | trade\_time | String | 40 | y | 下单时间（毫秒级时间戳，例如：1631861379000） |
| 支付时间 | pay\_time | String | 40 | y | 支付时间（毫秒级时间戳，例如：1631861379000） |
| 标记名称 | flag\_name | String | 32 | y | 标记名称（订单标记） |
| 邮费 | post\_amount | Decimal(19,4) |  | y | 邮费/订单邮费 |
| 证件类别 | id\_card\_type | Int | 4 | y | 证件类别 |
| 证件号码 | id\_card | String | 40 | y | 证件号码（仅自有平台及线下平台返回，其他平台均不返回） |
| 店铺名称 | shop\_name | String | 128 | y | 店铺名称 |
| 店铺编号 | shop\_no | String | 20 | y | 店铺编号 |
| 店铺备注 | shop\_remark | String | 255 | y | 店铺备注 |
| 出库单状态 | status | Int | 4 | y | 出库单状态:  <br>5已取消<br>10待放回(拣货待放回), 小于该值的都是已取消的单子<br>50待审核<br>51缺货<br>52缺货待入库<br>53 WMS已接单<br>54 获取电子面单<br>58 档口锁定<br>60 待分配<br>61 排队中<br>63 待补货<br>65 待处理  <br>70 待发货<br>73 爆款锁定<br>74 预打包<br>75 待拣货<br>77 拣货中,PDA拣货后<br>79 已拣货<br>90 延时发货<br>110已完成<br>-1未发货 |
| 发票类型 | invoice\_type | Int | 4 | y | 发票类型:<br>0：不需要<br>1：电子普通发票<br>2：增值税普通发票<br>3：电子增值税专用发票<br>4：纸质普通发票<br>5：纸质增值税专用发票 |
| 发票ID | invoice\_id | Int | 11 | y | 发票id:<br>目前只设0-1，<br>1表示已开发票 |
| 货到付款金额 | cod\_amount | Decimal(19,4) |  | y | 货到付款金额 |
| 发货条件 | delivery\_term | Int | 4 | y | 发货条件:<br>1款到发货<br>2货到付款(包含部分货到付款)<br>3分期付款<br>4挂账 |
| 平台ID | platform\_id | Int | 11 | y | 平台ID（请点击 [平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 查看对应关系） |
| 订单ID | trade\_id | Int | 11 | y | 订单ID |
| 审核员编号 | employee\_no | String | 40 | y | 审核员编号（为系统用户时不返回） |
| 优惠金额 | discount | Decimal(19,4) |  | y | 优惠金额(订单总优惠) |
| 税额 | tax | Decimal(19,4) |  | y | 税额 |
| 税率 | tax\_rate | Decimal(19,4) |  | y | 税率 |
| 币种 | currency | String | 20 | y | 币种 |
| 系统订单建单时间 | created | String | 40 | y | 系统订单建单时间（毫秒级时间戳，例如：1631861379000） |
| 出库单建单时间 | stock\_check\_time | String | 40 | y | 出库单建单时间（毫秒级时间戳，例如：1631861379000） |
| 打印备注 | print\_remark | String | 1000 | y | 打印备注 |
| 买家留言 | buyer\_message | String | 1024 | y | 买家留言 |
| 客服备注 | cs\_remark | String | 1024 | y | 客服备注 |
| 发票抬头 | invoice\_title | String | 255 | y | 发票抬头 |
| 发票内容 | invoice\_content | String | 255 | y | 发票内容 |
| 称重预估邮资 | post\_fee | Decimal(19,4) |  | y | 称重预估邮资<br>(使用根据重量预估的邮费) |
| 包装成本 | package\_fee | Decimal(19,4) |  | y | 包装成本(1.5.9.4及以上版本按照订单包装成本展示的信息返回) |
| 已付金额 | receivable | Decimal(19,4) |  | y | 已付金额(使用应收金额) |
| 总成本价 | goods\_total\_cost | Decimal(19,4) |  | y | 总成本价（对应销售出库明细内实际货品总成本） |
| 总货款 | goods\_total\_amount | Decimal(19,4) |  | y | 总货款 |
| 最后修改时间 | modified | String | 40 | y | 最后修改时间，例如：2021-09-23 15:56:18 |
| 分销商昵称 | fenxiao\_nick | String | 40 | y | 分销商昵称 |
| 订单标签 | trade\_label | String | 255 | y | 订单标签 |
| 订单来源 | trade\_from | Int | 4 | y | 订单来源：<br>1、接口抓取<br>2、手工创建<br>3、Excel导入<br>4、复制订单<br>5、接口推送<br>6、补发订单<br>7、PDA选货开单<br>8、分销补发订单 |
| 分拣波次 | picklist\_no | String | 40 | y | 分拣波次 |
| 分拣序号 | picklist\_seq | Int | 6 | y | 分拣序号 |
| 物流单打印状态 | logistics\_print\_status | Int | 4 | y | 0：未打印<br>1：打印中<br>2：已打印<br>3：无需打印 |
| 已付 | paid | Decimal(19,4) |  | y | 已付 |
| 店铺平台id | shop\_platform\_id | Int |  | y | 店铺平台id |
| 子平台id | sub\_platform\_id | Int |  | y | 子平台id |
| 接口处理错误信息 | error\_info | String | 255 | y | 接口处理错误信息 |
| 其他出库自定义子类别 | custom\_type | Int | 6 | y | 其他出库自定义子类别0,1,2,3,4 |
| 发货单模板id | sendbill\_template\_id | Int | 11 | y | 发货单模板id |
| 客户id | customer\_id | Int | 11 | y | 客户id |
| 仓库类别 | warehouse\_type | Int | 6 | y | 1:普通（内部）,2:自流转,3:平台,4:京东沧海.6:抖音云仓,125:代发仓,126:分销委外 |
| 制单人id（操作员） | operator\_id | Int | 6 | y | 制单人id（操作员） |
| 外部单号 | outer\_no | String | 40 | y | 外部单号 |
| 出库状态 | consign\_status | Int | 6 | y | 出库状态<br>0：无<br>1：已验货<br>2：已称重<br>16：已拣货<br>32：电子面单回传<br>64：已分拣<br>128：配送清单打印状态<br>4096：订单回告（订单生成出库单中间量，暂时只有订单合并回告使用） |
| 货品种类 | goods\_type\_count | Int | 6 | y | 货品种类 |
| 预估邮资成本 | calc\_post\_cost | Decimal(19,4) |  | y | 预估邮资成本 |
| 打印批次 | batch\_no | String | 40 | y | 打印批次 |
| 销售出库单创建时间 | created\_date | String | 40 | y | 销售出库单创建时间,DateTime格式 |
| 分销原始单号 | fenxiao\_tid | String | 40 | y | 分销原始单号 |
| 分销商编号 | fenxiao\_nick\_no | String | 40 | y | 分销商编号 |
| 物流单列表 | logistics\_list | List<Map<String, Object>> |  | y | 物流单详情 |
| 销售出库单详情 | details\_list | List<Map<String, Object>> |  | y | 销售出库单详情 |
| 主播 | anchor\_name | String | 50 | y | 主播 |
| 助播 | assist\_achor\_name | String | 50 | y | 助播 |
| 场控 | control\_achor\_name | String | 50 | y | 场控 |
| 运营 | operation\_anchor\_name | String | 50 | y | 运营 |
| 拣货分组名称 | pick\_group\_name | String | 100 | y | 拣货分组名称 |
| 分销店铺名称 | fenxiao\_shop\_name | String | 40 | y | 分销店铺名称 |
| wms业务单号 | wms\_code | String | 40 | y | wms业务单号 |
| 销售出库单标记名称 | stockout\_flag\_name | String | 32 | y | 销售出库单标记名称 |
| 国补信息 | gov\_subsidy\_info | List<Map<String, Object>> |  | n | 国补信息 |

**logistics\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流单id | rec\_id | Int | 11 | y | 物流单id |
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

**gov\_subsidy\_info**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始单号 | tid | String |  | y | 原始单号 |
| --- | --- | --- | --- | --- | --- |
| 原始子单号 | oid | String |  | y | 原始子单号 |
| --- | --- | --- | --- | --- | --- |
| 公司主体名称 | corp\_entity\_name | String |  | y | 公司主体名称 |
| --- | --- | --- | --- | --- | --- |

**details\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 销售出库单详情的id | rec\_id | Int | 11 | y | 销售出库单详情的id |
| 出库单id | stockout\_id | Int | 11 | y | 出库单id |
| 订单明细id | src\_order\_detail\_id | int | 11 | Y | 订单明细id |
| 单品id | spec\_id | Int | 11 | y | 单品id（系统单品主键） |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 货品数量 | goods\_count | Decimal(19,4) |  | y | 货品数量:  如果按照货位分组就是总货品数量 |
| 总成本 | total\_amount | Decimal(19,4) |  | y | 总成本: 成本价\*货品数量 |
| 成交价 | sell\_price | Decimal(19,4) |  | y | 成交价（当订单货品发生变更导致价格变化，该值不变，若需获取ERP销售出库明细中的货品成交价取share\_price字段） |
| 出库单明细备注 | remark | String | 255 | y | 出库单明细备注 |
| 货品名称 | goods\_name | String | 255 | y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | y | 货品编号 |
| 规格名称 | spec\_name | String | 100 | y | 规格名称 |
| 规格码 | spec\_code | String | 40 | y | 规格码 |
| 货品成本 | cost\_price | Decimal(19,4) |  | y | 货品成本 |
| 总重量 | weight | Decimal(19,4) | 11 | y | 总重量 |
| 货品id | goods\_id | Int | 11 | y | 货品id（系统货品主键） |
| 规格自定义属性1 | prop1 | String | 255 | y | 规格自定义属性1 |
| 规格自定义属性2 | prop2 | String | 255 | y | 规格自定义属性2 |
| 规格自定义属性3 | prop3 | String | 255 | y | 规格自定义属性3 |
| 规格自定义属性4 | prop4 | String | 255 | y | 规格自定义属性4 |
| 规格自定义属性5 | prop5 | String | 255 | y | 规格自定义属性5 |
| 规格自定义属性6 | prop6 | String | 255 | y | 规格自定义属性6 |
| 平台id | platform\_id | Int | 6 | y | 平台id，点击查看 [平台代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) |
| 退款状态 | refund\_status | Int | 4 | y | 退款状态:<br>0无退款<br>1取消退款,<br>2已申请退款<br>3等待退货<br>4等待收货<br>5退款成功---(原始子订单关闭，这里也是退款状态) |
| 单价/货品原单价 | market\_price | Decimal(19,4) |  | y | 单价/货品原单价 |
| 货品总优惠 | discount | Decimal(19,4) |  | y | 货品总优惠 |
| 货品成交价 | share\_price | Decimal(19,4) |  | y | 系统销售出库明细对应的货品成交价 |
| 总货款/货品成交总价 | share\_amount | Decimal(19,4) |  | y | 总货款/货品成交总价 |
| 税率 | tax\_rate | Decimal(19,4) |  | y | 税率 |
| 主条码 | barcode | String | 50 | y | 主条码 |
| 基本单位名称 | unit\_name | String | 20 | y | 基本单位名称 |
| 订单货品(子订单)id | sale\_order\_id | Int | 11 | y | 订单货品(子订单)id |
| 是否是赠品 | gift\_type | Int | 11 | y | 是否是赠品:<br>0非赠品<br>1自动赠送<br>2手工赠送<br>4周期购赠送<br>8平台赠送<br>32阶梯满赠 <br>64CRM追加赠送 <br>65 主品（1.5.7.0版本以上返回） |
| 原始子订单号 | src\_oid | String | 40 | y | 原始子订单号 |
| 子单原始订单号 | src\_tid | String | 40 | y | 子单原始订单号 |
| 订单内部来源 | from\_mask | Int | 11 | y | 订单内部来源:<br>0：无来源<br>1：手机<br>2：聚划算<br>32：开具电子发票<br>2048：当日达<br>4096：次日达<br>8192：承诺时效<br>2097152：区域零售<br>4194304：拼多多厂家代打<br>8388608：周期购<br>1048576：预售单<br>33554432：前N有礼<br>524288：天猫物流升级<br>64：按需配送<br>256：承诺结构化/QIC<br>16384：商仓鸟配<br>ext-2：小时达订单<br>ext-4：自选物流<br>ext-16：国补订单 |
| 货品类型 | goods\_type | Int | 4 | y | 货品类型:<br>0：其它<br>1：销售货品<br>2：原材料<br>3：包装物<br>4：周转材料<br>5：虚拟商品<br>6：固定资产<br>8：分装箱 |
| 货品自定义属性1 | good\_prop1 | String | 255 | y | 货品自定义属性1 |
| 货品自定义属性2 | good\_prop2 | String | 255 | y | 货品自定义属性2 |
| 货品自定义属性3 | good\_prop3 | String | 255 | y | 货品自定义属性3 |
| 货品自定义属性4 | good\_prop4 | String | 255 | y | 货品自定义属性4 |
| 货品自定义属性5 | good\_prop5 | String | 255 | y | 货品自定义属性5 |
| 货品自定义属性6 | good\_prop6 | String | 255 | y | 货品自定义属性6 |
| sn\_list | sn\_list | String |  | y | 当need\_sn=true时返回英文逗号分隔的sn |
| 组合装编码 | suite\_no | String | 40 | y | 系统订单生成时组合装对应的组合装编码 |
| 组合装数量 | suite\_num | Decimal(19,4) |  | y | 组合装数量 |
| 分摊邮费 | share\_post\_amount | Decimal(19,4) |  | y | 分摊邮费 |
| 已付 | paid | Decimal(19,4) |  | y | 已付 |
| 是否包装 | is\_package | boolean | 1 | y | 是否包装<br>true:是<br>false:否 |
| 品牌编号 | brand\_no | String | 32 | y | 品牌编号 |
| 品牌名称 | brand\_name | String | 64 | y | 品牌名称 |
| 源单据类别 | src\_order\_type | Int | 11 | y | 源单据类别<br>1：销售订单 |
| 基本单位id | base\_unit\_id | Int | 11 | y | 基本单位id |
| 辅助单位 | unit\_id | Int | 11 | y | 辅助单位 |
| 单位换算 | unit\_ratio | Decimal(19,4) |  | y | 单位换算 |
| 辅助数量 | num2 | Decimal(19,4) |  | y | 辅助数量 |
| 货品数量 | num | Decimal(19,4) |  | y | 货品数量 |
| 出库货位id | position\_id | Int | 11 | y | 出库货位id |
| 指定出库批次 | batch\_id | Int | 11 | y | 指定出库批次 |
| 是否验货 | is\_examined | Int | 1 | y | 是否验货 |
| 有效期 | expire\_date | String | 40 | y | 有效期，时间格式：yyyy-MM-dd HH:mm:ss |
| 扫描方式 | scan\_type | Int | 11 | y | 扫描方式<br>0：未验货<br>1：扫描验货<br>2：手工验货<br>3：快速验货<br>4：无需验货 |
| 最后修改时间 | modified\_date | String | 40 | y | 最后修改时间，时间格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | created\_date | String | 40 | y | 创建时间，时间格式：yyyy-MM-dd HH:mm:ss |
| 分类 | class\_name | String | 100 | y | 分类名称 |
| 平台货品id | api\_goods\_id | String | 40 | y | 平台货品id |
| 平台规格id | api\_spec\_id | String | 40 | y | 平台规格id |
| 打包积分 | pack\_score | Decimal(19,4) |  | y | 打包积分 |
| 拣货积分 | pick\_score | Decimal(19,4) |  | y | 拣货积分 |
| 验货积分 | scan\_score | Decimal(19,4) |  | y | 验货积分 |
| 平台货品名称 | api\_goods\_name | String | 255 | y | 平台货品名称 |
| 出库货位明细 | position\_details\_list | List<Map<String, Object>> |  | y | 出库货位明细 |
| 拣货位明细 | pick\_position\_details\_list | List<Map<String, Object>> |  | y | 拣货位明细 |

**position\_details\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货位明细id | rec\_id | Int | 11 | y | 货位明细id |
| 销售出库单详情id | stockout\_detail\_id | Int | 11 | y | 销售出库单详情id |
| 货位id | position\_id | Int | 11 | y | 货位id |
| 货位号 | position\_no | String | 20 | y | 货位号 |
| 有效期 | expire\_date | String | 40 | y | 有效期 |
| 生产日期 | production\_date | String |  | y | 生产日期 |
| 批次号 | batch\_no | String | 20 | Y | 批次号 |
| 当前货位出库总货品数量 | position\_goods\_count | Decimal(19,4) |  | y | 当前货位出库货品总量 |

**pick\_position\_details\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货位明细id | rec\_id | Int | 11 | y | 货位明细id |
| 销售出库单详情id | stockout\_detail\_id | Int | 11 | y | 销售出库单详情id |
| 货位id | position\_id | Int | 11 | y | 货位id |
| 货位号 | position\_no | String | 20 | y | 货位号 |
| 有效期 | expire\_date | String | 40 | y | 有效期 |
| 生产日期 | production\_date | String |  | y | 生产日期 |
| 批次号 | batch\_no | String | 20 | Y | 批次号 |
| 当前货位出库总货品数量 | position\_goods\_count | Decimal(19,4) |  | y | 当前货位出库货品总量 |
| 商家编码 | spec\_no | String |  | y | 商家编码 |

**5.请求示例**

- [json](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryWithDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryWithDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryWithDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryWithDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>`"start_time"``:``"2019-12-31 00:00:00"``,`<br>`"end_time"``:``"2019-12-31 01:00:00"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->start_time =``'2019-12-11 00:00:00'``;`<br>`$params``->end_time =``'2019-12-31 00:00:00'``;`<br>``<br>``<br>`$pager``=``new``Pager(2, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.stockout.Sales.queryWithDetail"``,``$pager``,``$params``);`<br>``<br>`?>` |

### **6.响应示例**

#### 6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryWithDetail#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>210<br>211<br>212<br>213<br>214<br>215<br>216<br>217 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [`<br>```{`<br>```"post_amount"``:``"0.0000"``,`<br>```"fenxiao_nick"``:``""``,`<br>```"error_info"``:``""``,`<br>```"trade_time"``: 1746759592000,`<br>```"pick_group_name"``:``"默认"``,`<br>```"bad_reason"``: 0,`<br>```"discount"``:``"0.0000"``,`<br>```"picker_name"``:``"系统用户"``,`<br>```"trade_id"``: 2054992,`<br>```"trade_label"``:``"其他"``,`<br>```"receiver_country"``: 0,`<br>```"refund_status"``: 0,`<br>```"receiver_province"``: 120000,`<br>```"buyer_message"``:``""``,`<br>```"logistics_code"``:``"ZT0002"``,`<br>```"shop_platform_id"``: 127,`<br>```"shop_id"``: 327,`<br>```"warehouse_name"``:``"wdtapi3-test2"``,`<br>```"nick_name"``:``"syf"``,`<br>```"warehouse_mapping_code"``:``""``,`<br>```"id_card_type"``: 0,`<br>```"status"``: 110,`<br>```"package_fee"``:``"0.0000"``,`<br>```"src_trade_no"``:``"zd202505090001"``,`<br>```"post_fee"``:``"0.0000"``,`<br>```"custom_type"``: 0,`<br>```"sub_platform_id"``: 0,`<br>```"goods_count"``: 1,`<br>```"stockout_id"``: 700611,`<br>```"src_order_no"``:``"JY202505090021"``,`<br>```"invoice_content"``:``""``,`<br>```"receiver_name"``:``"zd"``,`<br>```"sendbill_template_id"``: 0,`<br>```"currency"``:``""``,`<br>```"picklist_no"``:``""``,`<br>```"examiner_name"``:``"系统用户"``,`<br>```"logistics_type"``: 5,`<br>```"trade_from"``: 2,`<br>```"delivery_term"``: 1,`<br>```"logistics_no"``:``"2025000501321"``,`<br>```"consigner_name"``:``"zd"``,`<br>```"receiver_district"``: 120105,`<br>```"goods_total_amount"``:``"3.0000"``,`<br>```"receivable"``: 3,`<br>```"receiver_mobile"``:``"18466197764"``,`<br>```"stock_check_time"``: 1746759828000,`<br>```"cs_remark"``:``""``,`<br>```"receiver_address"``:``"13"``,`<br>```"customer_name"``:``"zd"``,`<br>```"printer_name"``:``"系统用户"``,`<br>```"customer_id"``: 10446058,`<br>```"warehouse_id"``: 344,`<br>```"logistics_name"``:``"中通0002"``,`<br>```"details_list"``: [`<br>```{`<br>```"rec_id"``: 920840,`<br>```"stockout_id"``: 700611,`<br>```"spec_id"``: 644718,`<br>```"goods_count"``: 1,`<br>```"src_order_type"``: 1,`<br>```"base_unit_id"``: 5,`<br>```"unit_id"``: 170,`<br>```"unit_ratio"``: 1,`<br>```"num2"``: 1,`<br>```"num"``: 1,`<br>```"position_id"``: 0,`<br>```"batch_id"``: 0,`<br>```"is_examined"``: 0,`<br>```"scan_type"``: 0,`<br>```"modified_date"``:``"2025-05-09 11:03:47"``,`<br>```"created_date"``:``"2025-05-09 11:03:47"``,`<br>```"goods_amount"``: 3,`<br>```"brand_no"``:``"BRAND"``,`<br>```"brand_name"``:``"无"``,`<br>```"api_goods_name"``:``"zd20231108"``,`<br>```"remark"``:``""``,`<br>```"goods_name"``:``"zd20231108"``,`<br>```"goods_no"``:``"zd20231108"``,`<br>```"spec_name"``:``"zd20231108"``,`<br>```"spec_code"``:``"zd20231108"``,`<br>```"spec_no"``:``"zd20231108"``,`<br>```"weight"``: 0,`<br>```"goods_id"``: 423231,`<br>```"prop1"``:``"456"``,`<br>```"prop2"``:``"456"``,`<br>```"prop3"``:``""``,`<br>```"prop4"``:``""``,`<br>```"prop5"``:``""``,`<br>```"prop6"``:``""``,`<br>```"platform_id"``: 0,`<br>```"refund_status"``: 0,`<br>```"barcode"``:``"zd20231108"``,`<br>```"unit_name"``:``"辆"``,`<br>```"sale_order_id"``: 2560202,`<br>```"gift_type"``: 0,`<br>```"src_oid"``:``"AD202505090002"``,`<br>```"src_tid"``:``"zd202505090001"``,`<br>```"from_mask"``: 0,`<br>```"goods_type"``: 1,`<br>```"good_prop1"``:``""``,`<br>```"good_prop2"``:``"123"``,`<br>```"good_prop3"``:``""``,`<br>```"good_prop4"``:``""``,`<br>```"good_prop5"``:``""``,`<br>```"good_prop6"``:``""``,`<br>```"suite_no"``:``""``,`<br>```"src_order_detail_id"``: 2560202,`<br>```"is_package"``:``false``,`<br>```"class_id"``: 0,`<br>```"suite_num"``: 0,`<br>```"class_name"``:``"无"``,`<br>```"sell_price"``: 3,`<br>```"market_price"``: 3,`<br>```"share_price"``: 3,`<br>```"total_amount"``: 0,`<br>```"cost_price"``: 0,`<br>```"discount"``: 0,`<br>```"share_amount"``: 3,`<br>```"tax_rate"``: 0,`<br>```"share_post_amount"``: 6,`<br>```"paid"``: 9,`<br>```"position_details_list"``: [`<br>```{`<br>```"rec_id"``: 306518,`<br>```"stockout_detail_id"``: 920840,`<br>```"position_id"``: -6,`<br>```"position_no"``:``"其它未上架"``,`<br>```"batch_no"``:``""``,`<br>```"expire_date"``:``""``,`<br>```"production_date"``:``""``,`<br>```"position_goods_count"``: 1`<br>```}`<br>```]`<br>```}`<br>```],`<br>```"consign_time"``:``"2025-05-09 11:04:07"``,`<br>```"warehouse_type"``: 1,`<br>```"operator_id"``: 660,`<br>```"receiver_dtb"``:``"天津市 河北区"``,`<br>```"print_remark"``:``""``,`<br>```"employee_no"``:``"zd"``,`<br>```"tax_rate"``:``"0.0000"``,`<br>```"shop_remark"``:``""``,`<br>```"stockout_flag_name"``:``"无"``,`<br>```"outer_no"``:``""``,`<br>```"invoice_id"``: 0,`<br>```"modified"``:``"2025-05-09 11:04:07"``,`<br>```"order_type"``: 1,`<br>```"pick_group"``: 0,`<br>```"shop_no"``:``"wdtapi3-test2"``,`<br>```"picklist_seq"``: 0,`<br>```"seq_no"``: 1,`<br>```"receiver_area"``:``"天津 天津市 河北区"``,`<br>```"customer_no"``:``"KH202307190002"``,`<br>```"src_order_id"``: 2054992,`<br>```"created"``: 1746759731000,`<br>```"weight"``: 0,`<br>```"block_reason"``: 0,`<br>```"tax"``:``"0.0000"``,`<br>```"shop_name"``:``"wdtapi3-test2"``,`<br>```"pay_time"``: 1746759592000,`<br>```"goods_total_cost"``:``"0.0000"``,`<br>```"trade_no"``:``"JY202505090021"``,`<br>```"consign_status"``: 0,`<br>```"order_no"``:``"CK202505095"``,`<br>```"receiver_city"``: 120100,`<br>```"invoice_title"``:``""``,`<br>```"goods_type_count"``: 1,`<br>```"id_card"``:``""``,`<br>```"remark"``:``""``,`<br>```"calc_post_cost"``:``"0.0000"``,`<br>```"cod_amount"``:``"0.0000"``,`<br>```"flag_name"``:``"无"``,`<br>```"logistics_id"``: 420,`<br>```"warehouse_no"``:``"wdtapi3-test2"``,`<br>```"receiver_telno"``:``""``,`<br>```"receiver_zip"``:``"014500"``,`<br>```"trade_status"``: 96,`<br>```"invoice_type"``: 0,`<br>```"new_trade_label"``:``"1"``,`<br>```"batch_no"``:``""``,`<br>```"packager_name"``:``"系统用户"``,`<br>```"salesman_no"``:``"zd"``,`<br>```"platform_id"``: 0,`<br>```"paid"``:``"9.0000"``,`<br>```"trade_type"``: 2,`<br>```"logistics_print_status"``: 0,`<br>```"created_date"``:``"2025-05-09 11:03:48"``,`<br>```"fullname"``:``"zd"``,`<br>```"logistics_list"``: [`<br>```{`<br>```"rec_id"``: 12670612,`<br>```"stockout_id"``: 700611,`<br>```"logistics_id"``: 420,`<br>```"logistics_no"``:``"2025000501321"``,`<br>```"calc_weight"``: 0,`<br>```"weight"``: 0,`<br>```"remark"``:``""``,`<br>```"length"``: 0,`<br>```"width"``: 0,`<br>```"height"``: 0,`<br>```"package_name"``:``"无包装"``,`<br>```"logistics_name"``:``"中通0002"``,`<br>```"volume"``:``"0.000000000000"``,`<br>```"postage"``:``"0.0000"`<br>```}`<br>```]`<br>```}`<br>```]`<br>```}`<br>`}` |

#### 6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Sales.queryWithDetail#autoTab1_0)

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

4.1 公共响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1