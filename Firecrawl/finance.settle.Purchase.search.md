---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Purchase.search"
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

**finance.settle.Purchase.search** **（采购结算单查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：获取ERP采购结算单信息 |
| **1.2 适用版本：** 客户端 V1.5.6.2及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4注意事项：【权限校验】：仓库权限** |

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
| 秒级时间戳 | timestamp | int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 供应商编号 | provider\_no | String | 20 | N | 供应商编号 |
| 采购员姓名 | purchaser\_name | String | 50 | N | 采购员姓名 |
| 结算单号 | settle\_no | String | 64 | N | 结算单号 |
| 采购单号 | purchase\_no | String | 20 | N | 采购单号 |
| 结算单状态 | status | String | 4 | N | 10:编辑中,20:待审核,30:已审核,40 已取消.不传默认显示全部. |
| 创建起始时间 | create\_from | String | 40 | N | 创建起始时间 |
| 创建结束时间 | create\_to | String | 40 | N | 创建结束时间 |
| 修改开始时间 | modified\_from | String | 40 | N | 修改开始时间 |
| 修改结束时间 | modified\_to | String | 40 | N | 修改结束时间 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 否 | 0表示调用成功,在调用错误时候不返回该值。 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据数据 | data | List<Map<String, Object>> |  | 否 | 单据数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据数据 | order | List<Map<String, Object>> |  | 是 | 单据数据 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总税额 | tax\_amount | Decimal(19,4) |  | Y | 总税额 |
| 物流公司名称 | logistics\_type\_name | String | 40 | Y | 物流公司名称，参考附录物流对照表 |
| 审核员 | checker\_name | String | 40 | Y | 审核员 |
| 运费 | post\_fee | Decimal(19,4) |  | Y | 运费 |
| 总金额 | total\_cost | Decimal(19,4) |  | Y | 总金额 |
| 总货款 | goods\_amount | Decimal(19,4) |  | Y | 总货款 |
| 创建时间 | created | string | 40 | Y | 创建时间 |
| 审核时间 | check\_time | string | 40 | Y | 审核时间 |
| 发票号码 | invoice\_no | String | 100 | Y | 发票号码 |
| 备注 | remark | String | 255 | Y | 备注 |
| 含税总货款 | tax\_goods\_amount | Decimal(19,4) |  | Y | 含税总货款 |
| 标记名称 | flag\_name | String | 32 | Y | 标记名称 |
| 结算单号 | settle\_no | String | 40 | Y | 结算单号 |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 物流单号 | logistics\_no\_list | String | 40 | Y | 物流单号 |
| 分摊运费 | is\_share\_post\_fee | bool | 1 | Y | 是否分摊运费<br>true：是<br>false：否 |
| 分摊其他费用 | is\_share\_other | bool | 1 | Y | 是否分摊其他费用<br>true：是<br>false：否 |
| 发票类型 | invoice\_type | Int | 4 | Y | 0:无,1: 普通发票,2: 增值税发票,3: 专用增值税发票 |
| 采购单号 | purchase\_no | String | 255 | Y | 采购单号 |
| 货品总数 | goods\_count | Decimal(19,4) |  | Y | 货品总数 |
| 其他费用 | other\_total | Decimal(19,4) |  | Y | 其他费用 |
| 入库单号 | stockin\_no | String | 100 | Y | 入库单号 |
| 状态 | status | Int | 4 | Y | 状态 |
| 供应商编号 | provider\_no | String |  | Y | 供应商编号 |
| 结算员 | settler\_name | String |  | Y | 结算员 |
| 结算单详情 | detail\_list | List<Map<String, Object>> |  | Y | 结算单详情 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 换算系数 | unit\_ratio | Decimal(19,4) |  | Y | 采购单位与基本单位之间的换算系数 |
| 结算数量 | settle\_num | Decimal(19,4) |  | Y | 结算数量 |
| 开票数量 | invoice\_num | Decimal(19,4) |  | Y | 开票数量 |
| 单价 | price | Decimal(19,4) |  | Y | 单价 |
| 折扣 | discount | Decimal(19,4) |  | Y | 折扣 |
| 税前折扣价 | dis\_price | Decimal(19,4) |  | Y | 税前折扣价 |
| 税率 | tax\_rate | Decimal(19,4) |  | Y | 税率 |
| 含税单价 | tax\_price | Decimal(19,4) |  | Y | 含税单价 |
| 税额 | total\_tax\_amount | Decimal(19,4) |  | Y | 税额 |
| 货款 | total\_amount | Decimal(19,4) |  | Y | 货款 |
| 分摊运费 | share\_post\_fee | Decimal(19,4) |  | Y | 分摊运费 |
| 含税货款 | tax\_total\_amount | Decimal(19,4) |  | Y | 含税货款 |
| 采购单号 | purchase\_no | String | 20 | Y | 采购单号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 条码 | barcode | String | 50 | Y | 条码 |
| 供应商货号 | provider\_goods\_no | String | 64 | Y | 供应商货号 |
| 备注 | remark | String | 128 | Y | 备注 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 基本单位 | unit\_name | String | 20 | Y | 基本单位 |
| 采购单位名称 | purchase\_unit\_name | String | 20 | Y | 采购单位名称 |
| 品牌名称 | brand\_name | String | 64 | Y | 品牌名称 |
| 分摊其他费用 | share\_other | Decimal(19,4) |  | Y | 分摊其他费用 |

**5.请求示例**

- [Json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Purchase.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Purchase.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Purchase.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Purchase.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"warehouse_no"``:``"1001"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`require_once(``'wdtsdk.php'``);`<br>``<br>`$client =``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap =``new``stdClass();`<br>`$parMap->warehouse_no =``"1001"``;`<br>`$pager =``new``Pager(``1``,``0``,``true``);`<br>`$data = $client->pageCall(``"finance.settle.Purchase.search"``, $pager, $parMap);`<br>`$php_json = json_encode($data, JSON_UNESCAPED_UNICODE);`<br>`echo $php_json;`<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Purchase.search#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88 | `{`<br>```"status"``:0,`<br>```"data"``:{`<br>```"total_count"``:392,`<br>```"order"``:[`<br>```{`<br>```"tax_amount"``:3592.974,`<br>```"purchase_no"``:``"CG202006190001"``,`<br>```"post_fee"``:555,`<br>```"total_cost"``:16346.554,`<br>```"detail_list"``:[`<br>```{`<br>```"unit_ratio"``:1,`<br>```"settle_num"``:3,`<br>```"invoice_num"``:3,`<br>```"price"``:1111,`<br>```"discount"``:0.98,`<br>```"dis_price"``:1088.78,`<br>```"tax_rate"``:1.1,`<br>```"tax_price"``:2286.438,`<br>```"total_tax_amount"``:3592.974,`<br>```"total_amount"``:3266.34,`<br>```"share_post_fee"``:244.5104,`<br>```"tax_total_amount"``:6859.314,`<br>```"purchase_no"``:``"CG202006190001"``,`<br>```"goods_name"``:``"赵阳的货品02 RPG"``,`<br>```"goods_no"``:``"098812"``,`<br>```"spec_code"``:``""``,`<br>```"spec_name"``:``""``,`<br>```"spec_no"``:``"088804"``,`<br>```"barcode"``:``""``,`<br>```"provider_goods_no"``:``""``,`<br>```"remark"``:``""``,`<br>```"created"``:1592794124000,`<br>```"unit_name"``:``"个"``,`<br>```"purchase_unit_name"``:``"无"``,`<br>```"brand_name"``:``"无"`<br>```},`<br>```{`<br>```"unit_ratio"``:1,`<br>```"settle_num"``:4,`<br>```"invoice_num"``:4,`<br>```"price"``:2222,`<br>```"discount"``:0.98,`<br>```"dis_price"``:2177.56,`<br>```"tax_rate"``:0,`<br>```"tax_price"``:2177.56,`<br>```"total_tax_amount"``:0,`<br>```"total_amount"``:8710.24,`<br>```"share_post_fee"``:310.4896,`<br>```"tax_total_amount"``:8710.24,`<br>```"purchase_no"``:``"CG202006190001"``,`<br>```"goods_name"``:``"赵阳的货品01 M4A1"``,`<br>```"goods_no"``:``"09811"``,`<br>```"spec_code"``:``""``,`<br>```"spec_name"``:``""``,`<br>```"spec_no"``:``"088805"``,`<br>```"barcode"``:``""``,`<br>```"provider_goods_no"``:``""``,`<br>```"remark"``:``""``,`<br>```"created"``:1592794124000,`<br>```"unit_name"``:``"个"``,`<br>```"purchase_unit_name"``:``"无"``,`<br>```"brand_name"``:``"赵阳品牌01"`<br>```}],`<br>```"remark"``:``""``,`<br>```"goods_count"``:7,`<br>```"flag_name"``:``"无"``,`<br>```"settle_no"``:``"JS202006220001"``,`<br>```"is_share_other"``:``true``,`<br>```"warehouse_no"``:``""``,`<br>```"is_share_post_fee"``:``true``,`<br>```"invoice_type"``:1,`<br>```"other_total"``:222,`<br>```"provider_no"``:``"085400"``,`<br>```"settler_name"``:``"系统"``,`<br>```"checker_name"``:``"系统"``,`<br>```"goods_amount"``:11976.58,`<br>```"created"``:1592794124000,`<br>```"invoice_no"``:``""``,`<br>```"tax_goods_amount"``:15569.554,`<br>```"stockin_no"``:``""``,`<br>```"logistics_no_list"``:``""``,`<br>```"logistics_type_name"``:``"未知"``,`<br>```"status"``:10`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Purchase.search#autoTab1_0)

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

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1