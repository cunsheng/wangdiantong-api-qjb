---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.queryDetail"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

采购类

供应商货品查询

采购退货单及明细查询

采购退货单取消

采购退货单新建

采购入库单推送

采购单及明细查询

采购单新建

采购结算单查询

采购入库单查询

采购退货出库单查询

采购入库单取消

采购单取消

采购单停止等待

采购退货单停止等待

供应商货品推送

采购退货出库单创建

采购单标记更新

采购申请单创建

采购申请单查询

采购退货批量取消

创建采购结算单

采购单取消（新）

采购申请单取消

采购申请单停止引用

预约入库单查询

创建采购退货结算单

当前位置： API文档 > 采购类

****purchase.ProviderGoods.queryDetail**（供应商货品查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP中供应商货品界面的供应商货品资料 |
| **1.2 适用版本：** 客户端 V1.6.0.10及以上版本 |
| **1.5注意事项：** **【权限校验】：供应商权限**   PS：不传入业务请求参数的情况下，全量获取数据<br>销量字段说明及计算方式， [**点击链接查看**](https://www.yuque.com/wdterpqjb/cangchu/zggh20xg7n1ywwao) |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、分销系统、全渠道等系统对接 |

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
| 供应商编号 | provider\_no | String | 20 | 否 | 供应商编号 |
| 货品编号 | goods\_no | String | 40 | 否 | 货品编号 |
| 商家编码 | spec\_no | String | 40 | 否 | 商家编码 |
| 供应商货号 | provider\_goods\_no | String | 64 | 否 | 供应商货号 |
| 货品名称 | goods\_name | String | 255 | 否 | 货品名称 |
| 条码 | barcode | String | 50 | 否 | 条码 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 查询出的详细信息 | data | List<Map<String, Object>> |  | 是 | 详细信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结果总数 | total\_count | Int |  | 是 | 结果总数 |
| 结果详情 | details | List<Map<String, Object>> |  | 是 | 结果详情 |

**details**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编号 | provider\_no | String | 20 | 是 | 供应商编号 |
| 供应商名称 | provider\_name | String | 64 | 是 | 供应商名称 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 最后采购时间 | last\_purchase\_time | String | 40 | 否 | 最后采购时间（毫秒级时间戳格式）最后采购时间为空情况下不返回该字段 |
| 产地 | origin | String | 64 | 是 | 产地 |
| 货品简称 | short\_name | String | 255 | 是 | 货品简称 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 分类名称 | class\_name | String | 255 | 是 | 分类名称 |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 是否主供应商 | is\_master | boolean | 1 | 是 | true：主供应商<br>false：不是主供应商 |
| 基本单位 | base\_unit\_name | String | 20 | 是 | 基本单位 |
| 供应商货号 | provider\_goods\_no | String | 64 | 是 | 供应商货号 |
| 总库存 | stock\_num | Decimal(19,4) |  | 是 | 总库存 |
| 待采购量 | to\_purchase\_num | Decimal(19,4) |  | 是 | 待采购量 |
| 预订单量 | subscribe\_num | Decimal(19,4) |  | 是 | 预订单量 |
| 待审核量 | order\_num | Decimal(19,4) |  | 是 | 待审核量 |
| 待发货量 | sending\_num | Decimal(19,4) |  | 是 | 待发货量 |
| 可发库存 | avaliable\_num | Decimal(19,4) |  | 是 | 可发库存 |
| 图片地址 | img\_url | String | 255 | 是 | 图片地址 |
| 采购在途量 | purchase\_num | Decimal(19,4) |  | 是 | 采购在途量 |
| 采购到货量 | purchase\_arrive\_num | Decimal(19,4) |  | 是 | 采购到货量 |
| 折扣 | discount | Decimal(19,4) |  | 是 | 折扣 |
| 采购价 | price | Decimal(19,4) |  | 是 | 采购价 |
| 零售价 | retail\_price | Decimal(19,4) |  | 是 | 零售价 |
| 最后采购价 | last\_price | Decimal(19,4) |  | 是 | 最后采购价 |
| 上一次采购价 | last\_second\_price | Decimal(19,4) |  | 是 | 上一次采购价 |
| 最低采购价 | lowest\_price | Decimal(19,4) |  | 是 | 最低采购价 |
| 今日销量 | today\_num | Decimal(19,4) |  | 是 | 今日销量 |
| 昨日销量 | yesterday\_num | Decimal(19,4) |  | 是 | 昨日销量 |
| 七天销量 | num\_7days | Decimal(19,4) |  | 是 | 七天销量 |
| 14天销量 | num\_14days | Decimal(19,4) |  | 是 | 14天销量 |
| 月销量 | num\_month | Decimal(19,4) |  | 是 | 月销量 |
| 总销量 | num\_all | Decimal(19,4) |  | 是 | 总销量 |
| 采购单位 | unit\_name | String | 20 | 是 | 采购单位 |
| 单位变换率 | unit\_ratio | Decimal(19,4) |  | 是 | 辅助单位和单位的换算系数 |
| 最小采购量 | min\_purchase\_num | Decimal(19,4) |  | 是 | 最小采购量 |
| 税率 | tax\_rate | Decimal(19,4) |  | 是 | 税率 |
| 是否停用 | is\_disabled | boolean | 1 | 是 | true：停用<br>false：未停用 |
| 单品自定义属性1 | prop1 | String | 255 | 是 | 单品自定义属性1 |
| 单品自定义属性2 | prop2 | String | 255 | 是 | 单品自定义属性2 |
| 单品自定义属性3 | prop3 | String | 255 | 是 | 单品自定义属性3 |
| 单品自定义属性4 | prop4 | String | 255 | 是 | 单品自定义属性4 |
| 单品自定义属性5 | prop5 | String | 255 | 是 | 单品自定义属性5 |
| 单品自定义属性6 | prop6 | String | 255 | 是 | 单品自定义属性6 |
| 备注 | remark | String | 255 | 是 | 供应商货品的备注 |
| 供应商属性 | provider\_type | Int | 4 | 是 | 供应商属性<br>0：常规 1：档口 |
| 采购跟进人id | follower\_id | Int | 11 | 是 | 采购跟进人id |
| 采购周期 | purchase\_cycle\_day | Int | 11 | 是 | 采购周期天数 |

**5.请求示例**

- [JASON格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.queryDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.queryDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.queryDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.queryDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"spec_no"``:``"404010100301005"``,``"provider_no"``:``"LCJtest"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->spec_no =``"404010100301005"``;`<br>`$parMap``->provider_no =``"LCJtest"``;`<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>``<br>`$response``=``$client``->pageCall(``"purchase.ProviderGoods.queryDetail"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.queryDetail#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"details"``: [{`<br>```"provider_type"``: 0,`<br>```"spec_code"``:``"箱(100件)"``,`<br>```"discount"``: 1,`<br>```"min_purchase_num"``: 1,`<br>```"spec_no"``:``"404010100301005"``,`<br>```"tax_rate"``: 0,`<br>```"retail_price"``: 0,`<br>```"price"``: 0,`<br>```"num_14days"``: 0,`<br>```"goods_name"``:``"亲亲30g60虾条（烧烤味）（高原版）"``,`<br>```"follower_id"``: 0,`<br>```"is_master"``:``true``,`<br>```"last_second_price"``: 0,`<br>```"last_purchase_time"``: 1648095714000,`<br>```"unit_ratio"``: 5,`<br>```"is_disabled"``:``false``,`<br>```"subscribe_num"``: 0,`<br>```"num_all"``: 0,`<br>```"brand_name"``:``"淘淘乐"``,`<br>```"sending_num"``: 0,`<br>```"num_month"``: 0,`<br>```"unit_name"``:``"袋（5包）"``,`<br>```"img_url"``:``""``,`<br>```"short_name"``:``""``,`<br>```"order_num"``: 0,`<br>```"last_price"``: 0,`<br>```"num_7days"``: 0,`<br>```"to_purchase_num"``: 0,`<br>```"purchase_cycle_day"``: 0,`<br>```"origin"``:``""``,`<br>```"goods_no"``:``"404010100301005"``,`<br>```"stock_num"``: 0,`<br>```"purchase_arrive_num"``: 0,`<br>```"lowest_price"``: 0,`<br>```"remark"``:``"自动新建供应商货品"``,`<br>```"purchase_num"``: 0,`<br>```"yesterday_num"``: 0,`<br>```"avaliable_num"``: 0,`<br>```"base_unit_name"``:``"包"``,`<br>```"class_name"``:``"无"``,`<br>```"provider_no"``:``"LCJtest"``,`<br>```"today_num"``: 0,`<br>```"prop6"``:``""``,`<br>```"prop5"``:``""``,`<br>```"prop4"``:``""``,`<br>```"prop3"``:``""``,`<br>```"prop2"``:``""``,`<br>```"prop1"``:``""``,`<br>```"spec_name"``:``"箱(100件)"``,`<br>```"provider_goods_no"``:``""`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.ProviderGoods.queryDetail#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"...."`<br>`}` |

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