---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.queryWithDetail"
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

****purchase.PurchaseReturn.queryWithDetail**（采购退货单及明细查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP的采购退货单信息 |
| **1.2 适用版本：** 客户端 V1.5.5.2及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天。 |
| **1.5注意事项：【权限校验】：仓库权限**<br>如果不填写采购退货单号则必须填写开始时间和结束时间；填写了采购退货单号则起止时间条件失效。 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

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
| 供应商编号 | provider\_no | String | 20 | N | 供应商编号 |
| 采购退货单号 | return\_no | String | 20 | N | 采购退货单号 |
| 采购退货单状态 | status | Int | 4 | N | 10 已取消,20 编辑中,30 待审核,40 已审核,60 已完成 |
| 开始时间 | start\_time | String | 40 | N | 修改时间 |
| 结束时间 | end\_time | String | 40 | N | 修改时间 |
| 模糊查询 | fuzzy\_query | boolean | 1 | N | 默认false，业务单号进行模糊查询匹配，匹配数量大于1条时会报错 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态 | status | Int |  | Y | 0表示调用成功,在调用错误时候不返回该值。 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据数据 | data | Map<String, Object> |  | N | 单据数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 单据数据 |
| 数据总条数 | total\_count | Int |  | Y | 单据数据总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购退货单id | return\_id | Int | 11 | Y | 采购退货单id |
| 审核人 | check\_operator\_name | String | 40 | Y | 审核人 |
| 审核时间 | check\_time | String | 40 | Y | 审核时间 |
| 市 | city | String | 50 | Y | 市 |
| 供应商联系人姓名 | contact | String | 40 | Y | 供应商联系人姓名 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 制单员 | creator\_name | String | 40 | Y | 制单员 |
| 区 | district | String | 50 | Y | 区 |
| 货品数量 | goods\_count | Decimal(19,4) |  | Y | 货品数量 |
| 货款 | goods\_fee | Decimal(19,4) |  | Y | 货款 |
| 退货出库量 | goods\_out\_count | Decimal(19,4) |  | Y | 退货出库量 |
| 货品种类数 | goods\_type\_count | Int | 6 | Y | 货品种类数 |
| 是否占用库存 | is\_reserved | boolean | 1 | Y | true : 已占用, false: 未占用 |
| 物流方式 | logistics\_type | Int | 11 | Y | 物流方式，点击查看 [代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) |
| 物流公司编号 | logistics\_no | String |  | Y | ERP内维护的物流公司编号 |
| 物流公司id | logistics\_id | Int | 6 | Y | 物流公司id |
| 修改时间 | modified | String | 40 | Y | 修改时间 |
| 便签条数 | note\_count | Int | 6 | Y | 便签条数 |
| 其他费用 | other\_fee | Decimal(19,4) |  | Y | 其他费用 |
| 外部单号 | outer\_no | String | 40 | Y | 外部单号 |
| 邮费 | post\_fee | Decimal(19,4) |  | Y | 邮费 |
| 供应商名称 | provider\_name | String | 40 | Y | 供应商名称 |
| 省 | province | String | 50 | Y | 省 |
| 采购员 | purchaser\_name | String | 40 | Y | 采购员 |
| 退货地址 | receive\_address | String | 255 | Y | 退货地址 |
| 备注 | remark | String | 255 | Y | 备注 |
| 采购退货单号 | return\_no | String | 25 | Y | 采购退货单号 |
| 结算状态 | settle\_status | Int | 4 | Y | 0:不可结算,1:待结算2:部分结算,3已结算 |
| 状态 | status | Int | 4 | Y | 状态  10 已取消,20 编辑中,30 待审核,40 已审核,60 已完成 |
| 供应商联系电话 | telno | String | 32 | Y | 供应商联系电话 |
| 类型 | type | Int | 4 | Y | 1:退货,2:换货 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库id | warehouse\_id | Int | 11 | Y | 仓库id |
| 供应商编号 | provider\_no | String | 40 | Y | 供应商编号 |
| 原采购单号 | purchase\_no | String | 30 | Y | 只引用一个采购单号时有值，引用多个采购单号或者是未引用采购单返回空字符串 |
| 出库状态 | stockout\_status | Int | 4 | Y | 出库状态<br>0：未出库<br>1：部分出库<br>2：已出库<br>3：停止出库 |
| 采购退货单自定义属性1 | prop1 | String | 255 | Y | 采购退货单自定义属性1 |
| 采购退货单自定义属性2 | prop2 | String | 255 | Y | 采购退货单自定义属性2 |
| 采购退货单详情 | detail\_list | List<Map<String, Object>> |  | Y | 采购退货单详情 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键id | rec\_id | Int | 11 | Y | 主键id |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 单品ID | spec\_id | int |  | Y | 旺店通系统单品ID |
| 自定义属性2 | prop1 | String |  | Y | 退货单明细的自定义属性1 |
| 自定义属性2 | prop2 | String |  | Y | 退货单明细的自定义属性2 |
| 采购退货单id | return\_id | Int | 11 | Y | 采购退货单id |
| 是否残次品 | defect | bool | 1 | Y | 是否残次品 |
| 供应商货号 | provider\_goods\_no | String | 40 | Y | 供应商货号 |
| 退货数量 | num | Decimal(19,4) |  | Y | 退货数量 |
| 辅助数量 | num2 | Decimal(19,4) |  | Y | 辅助数量 |
| 出库数量 | out\_num | Decimal(19,4) |  | Y | 出库数量 |
| 结算数量 | settle\_num | Decimal(19,4) |  | Y | 结算数量 |
| 单位变换率 | unit\_ratio | Decimal(19,4) |  | Y | 单位变换率 |
| 单价 | price | Decimal(19,4) |  | Y | 单价（优惠前） |
| 折扣 | discount | Decimal(19,4) |  | Y | 折扣 |
| 税率 | tax\_rate | Decimal(19,4) |  | Y | 税率 |
| 税后单价 | tax\_price | Decimal(19,4) |  | Y | 税后单价（优惠后） |
| 金额 | amount | Decimal(19,4) |  | Y | 税前折后金额（税前折后单价\*退货数量） |
| 出库金额 | out\_amount | Decimal(19,4) |  | Y | 出库金额（税前折后单价\*出库数量） |
| 备注 | remark | String | 255 | Y | 备注 |
| 修改时间 | modified | String | 40 | Y | 修改时间 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 退货单位 | unit\_name | String | 20 | Y | 退货单位 |
| 基本单位 | base\_unit\_name | String | 20 | Y | 基本单位 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.queryWithDetail#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.queryWithDetail#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.queryWithDetail#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.queryWithDetail#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap =``new``stdClass();`<br>`$parMap->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap->end_time =``"2020-01-20 00:00:00"``;`<br>``<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>``<br>`$response = $client->pageCall(``"purchase.PurchaseReturn.queryWithDetail"``, $pager, $parMap);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.queryWithDetail#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 1,`<br>```"order"``: [{`<br>```"purchase_no"``:``""``,`<br>```"post_fee"``: 0,`<br>```"city"``:``"0"``,`<br>```"detail_list"``: [{`<br>```"rec_id"``: 2826,`<br>```"return_id"``: 1752,`<br>```"spec_id"``: 1,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"defect"``:``false``,`<br>```"provider_goods_no"``:``""``,`<br>```"num"``: 1,`<br>```"num2"``: 0.3333,`<br>```"out_num"``: 0,`<br>```"settle_num"``: 0,`<br>```"unit_ratio"``: 3,`<br>```"price"``: 5,`<br>```"discount"``: 1,`<br>```"tax_rate"``: 0,`<br>```"tax_price"``: 5,`<br>```"amount"``: 5,`<br>```"out_amount"``: 0,`<br>```"remark"``:``""``,`<br>```"prop1"``:``""``,`<br>```"prop2"``:``""``,`<br>```"modified"``: 1660117745000,`<br>```"created"``: 1660117745000,`<br>```"unit_name"``:``"哒哒哒哒哒"``,`<br>```"base_unit_name"``:``"箱"`<br>```}],`<br>```"goods_type_count"``: 1,`<br>```"return_id"``: 1752,`<br>```"remark"``:``""``,`<br>```"goods_count"``: 1,`<br>```"type"``: 1,`<br>```"telno"``:``""``,`<br>```"logistics_id"``: 0,`<br>```"is_reserved"``:``true``,`<br>```"province"``:``"0"``,`<br>```"warehouse_no"``:``"wdtapi3-test"``,`<br>```"stockout_status"``: 0,`<br>```"outer_no"``:``""``,`<br>```"contact"``:``"lcj"``,`<br>```"purchaser_name"``:``"系统"``,`<br>```"modified"``: 1660117751000,`<br>```"provider_name"``:``"LCJtest22222"``,`<br>```"logistics_type"``: 0,`<br>```"receive_address"``:``""``,`<br>```"other_fee"``: 0,`<br>```"note_count"``: 0,`<br>```"provider_no"``:``"LCJtest"``,`<br>```"check_operator_name"``:``"aaa"``,`<br>```"goods_out_count"``: 0,`<br>```"logistics_no"``:``""``,`<br>```"created"``: 1660117745000,`<br>```"settle_status"``: 0,`<br>```"return_no"``:``"CR202208100006"``,`<br>```"warehouse_name"``:``"wdtapi3-test"``,`<br>```"district"``:``"0"``,`<br>```"goods_fee"``: 5,`<br>```"creator_name"``:``"aaa"``,`<br>```"status"``: 40,`<br>```"warehouse_id"``: 624,`<br>```"check_time"``: 1660117751000`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=purchase.PurchaseReturn.queryWithDetail#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3 业务请求参数

3.3 业务请求参数

3.3 业务请求参数

4.响应参数

3.3 业务请求参数

3.3 业务请求参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1