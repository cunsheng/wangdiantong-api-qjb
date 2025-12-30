---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.process.search"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

[登录](javascript:gologin()) [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

货品类

货品推送

组合装查询

货品档案查询

平台货品查询

平台货品推送

物料清单推送

生产单推送

生产单查询

货品分类查询

品牌查询

组合装创建/更新

平台类目查询

货品批量推送

物料清单查询

条码上传

货品推送2

新建分类

货品品牌新建/更新

生产结算单查询

当前位置： API文档 > 货品类

**finance.settle.process.search** **（生产结算单查询)**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP生产结算单信息 |
| **1.2 适用版本：** 客户端 V1.5.9.6及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

**3.请求参数说明**

3.1 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | http://47.92.239.46/openapi |
| 正式环境 | http://wdt.wangdian.cn/openapi [查看正式环境动态获取方式](javascript:view_document('zhengshihuanjing') "查看正式环境动态获取方式") |

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
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 生产单号 | process\_no | String |  | 否 | 生产单号 |
| 结算单号 | settle\_no | String |  | 否 | 结算单号 |
| 生产商编码 | producer\_no | String |  | 否 | 生产商编码 |
| 开始时间 | start\_time | String |  | 否 | 开始时间（生产结算单的创建时间） |
| 结束时间 | end\_time | String |  | 否 | 结束时间（生产结算单的创建时间） |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小，最大1000 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

**返回值为一个Map<String, Object>**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 单据信息 | data | Map<String, Object> |  | 是 | 单据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据 | order | List<Map<String, Object>> |  | 是 | 明细数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结算单主键 | settle\_id | Int |  | 是 | 结算单主键 |
| 结算单号 | settle\_no | String |  | 是 | 结算单号 |
| 结算状态 | status | String |  | 是 | 结算状态<br>10：编辑中<br>20：待审核<br>30：已审核<br>40：已取消 |
| 生产商名称 | producer\_name | String |  | 是 | 生产商名称 |
| 生产商编号 | producer\_no | String |  | 是 | 生产商编号 |
| 生产商id | producer\_id | Int |  | 是 | 生产商id |
| 生产单id | process\_id | Int |  | 是 | 生产单id |
| 备注 | remark | String |  | 是 | 备注 |
| 分摊其它费用 | is\_share\_other\_fee | Int |  | 是 | 分摊其它费用<br>0：否<br>1：是 |
| 货品总数 | goods\_count | String |  | 是 | 货品总数 |
| 原料成本 | material\_amount | String |  | 是 | 原料成本 |
| 生产费用 | process\_fee | String |  | 是 | 生产费用 |
| 其他费用 | other\_fee | Decimal(19,4) |  | 是 | 其他费用 |
| 建单时间 | created | String |  | 是 | 建单时间 |
| 结算单明细 | detail\_list | List<Map<String, Object>> |  | 是 | 结算单明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结算单主键 | settle\_id | Int |  | 是 | 结算单主键 |
| 生产单主键 | process\_id | Int |  | 是 | 生产单主键 |
| 生产单号 | process\_no | String |  | 是 | 生产单号 |
| 商家编码 | spec\_no | String |  | 是 | 商家编码 |
| 残次品 | defect | Int |  | 是 | 残次品<br>0：正品<br>1：残次品 |
| 批次号 | batch\_no | String |  | 是 | 批次号 |
| 有效期 | expire\_date | String |  | 是 | 有效期 |
| 单位 | base\_unit\_name | String |  | 是 | 单位 |
| 结算数量 | settle\_num | Decimal(19,4) |  | 是 | 结算数量 |
| 结算单价 | cost | String |  | 是 | 结算单价 |
| 参考成本 | cost\_price | String |  | 是 | 参考成本 |
| 分配比例 | proportion | String |  | 是 | 分配比例 |
| 结算总金额 | cost\_total | String |  | 是 | 结算总金额 |
| 分摊其他费用 | share\_other\_fee | String |  | 是 | 分摊其他费用 |
| 入库结算单价 | stockin\_price | String |  | 是 | 入库结算单价 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.process.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.process.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.process.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.process.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"start_time"``:``"2025-05-16 13:48:29"``,``"end_time"``:``"2025-06-14 13:48:29"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17 | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2025-05-16 13:48:29"``;`<br>`$parMap``->end_time =``"2025-06-14 13:48:29"``;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"finance.settle.process.search"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.process.search#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176 | `{`<br>```"data"``: {`<br>```"total_count"``: 2,`<br>```"order"``: [`<br>```{`<br>```"settle_id"``: 507,`<br>```"settle_no"``:``"JS202505280004"``,`<br>```"status"``: 20,`<br>```"producer_id"``: 30,`<br>```"process_id"``: 2016,`<br>```"goods_count"``: 2,`<br>```"settler_id"``: 553,`<br>```"remark"``:``"自动结算，业务单号：PS2024121307"``,`<br>```"producer_no"``:``"PV2021120104"``,`<br>```"producer_name"``:``"nff333"``,`<br>```"created"``:``"2025-05-28 10:26:54"``,`<br>```"is_share_other_fee"``: 0,`<br>```"material_amount"``:``"3.1936"``,`<br>```"process_fee"``:``"0.0000"``,`<br>```"other_fee"``:``"0.0000"``,`<br>```"detail_list"``: [`<br>```{`<br>```"settle_id"``: 507,`<br>```"rec_id"``: 1001,`<br>```"process_id"``: 2016,`<br>```"spec_id"``: 8666,`<br>```"batch_no"``:``"00PS2024121307DFH20250528cp002"``,`<br>```"expire_date"``:``""``,`<br>```"settle_num"``: 1,`<br>```"proportion"``: 0.4545,`<br>```"warehouse_id"``: 319,`<br>```"cost_total"``: 1.4514,`<br>```"stockin_price"``: 1.4514,`<br>```"process_no"``:``"PS2024121307"``,`<br>```"spec_code"``:``"cp002"``,`<br>```"spec_name"``:``""``,`<br>```"base_unit_id"``: 2,`<br>```"spec_no"``:``"cp002"``,`<br>```"barcode"``:``"cp002"``,`<br>```"remark"``:``""``,`<br>```"cost"``:``"1.4514"``,`<br>```"defect"``: 0,`<br>```"cost_price"``:``"11.1000"``,`<br>```"share_other_fee"``:``"0.0000"``,`<br>```"warehouse_name"``:``"nff正品仓"``,`<br>```"base_unit_name"``:``"支"`<br>```},`<br>```{`<br>```"settle_id"``: 507,`<br>```"rec_id"``: 1002,`<br>```"process_id"``: 2016,`<br>```"spec_id"``: 8667,`<br>```"batch_no"``:``"00PS2024121307DFH20250528cp003"``,`<br>```"expire_date"``:``""``,`<br>```"settle_num"``: 1,`<br>```"proportion"``: 0.5455,`<br>```"warehouse_id"``: 319,`<br>```"cost_total"``: 1.7421,`<br>```"stockin_price"``: 1.7421,`<br>```"process_no"``:``"PS2024121307"``,`<br>```"spec_code"``:``"cp003"``,`<br>```"spec_name"``:``""``,`<br>```"base_unit_id"``: 2,`<br>```"spec_no"``:``"cp003"``,`<br>```"barcode"``:``"cp003"``,`<br>```"remark"``:``""``,`<br>```"cost"``:``"1.7421"``,`<br>```"defect"``: 0,`<br>```"cost_price"``:``"6.5900"``,`<br>```"share_other_fee"``:``"0.0000"``,`<br>```"warehouse_name"``:``"nff正品仓"``,`<br>```"base_unit_name"``:``"支"`<br>```}`<br>```]`<br>```},`<br>```{`<br>```"settle_id"``: 506,`<br>```"settle_no"``:``"JS202505280003"``,`<br>```"status"``: 20,`<br>```"producer_id"``: 30,`<br>```"process_id"``: 2016,`<br>```"goods_count"``: 3,`<br>```"settler_id"``: 553,`<br>```"remark"``:``"自动结算，业务单号：PS2024121307"``,`<br>```"producer_no"``:``"PV2021120104"``,`<br>```"producer_name"``:``"nff333"``,`<br>```"created"``:``"2025-05-28 09:56:24"``,`<br>```"is_share_other_fee"``: 0,`<br>```"material_amount"``:``"4.3546"``,`<br>```"process_fee"``:``"0.0000"``,`<br>```"other_fee"``:``"0.0000"``,`<br>```"detail_list"``: [`<br>```{`<br>```"settle_id"``: 506,`<br>```"rec_id"``: 998,`<br>```"process_id"``: 2016,`<br>```"spec_id"``: 8665,`<br>```"batch_no"``:``"PS2024121307DFH20250528202505cp001"``,`<br>```"expire_date"``:``"2025-05-30"``,`<br>```"settle_num"``: 1,`<br>```"proportion"``: 0.2666,`<br>```"warehouse_id"``: 319,`<br>```"cost_total"``: 1.1609,`<br>```"stockin_price"``: 1.1609,`<br>```"process_no"``:``"PS2024121307"``,`<br>```"spec_code"``:``"cp001"``,`<br>```"spec_name"``:``""``,`<br>```"base_unit_id"``: 2,`<br>```"spec_no"``:``"cp001"``,`<br>```"barcode"``:``"cp001"``,`<br>```"remark"``:``""``,`<br>```"cost"``:``"1.1609"``,`<br>```"defect"``: 0,`<br>```"cost_price"``:``"17.5800"``,`<br>```"share_other_fee"``:``"0.0000"``,`<br>```"warehouse_name"``:``"nff正品仓"``,`<br>```"base_unit_name"``:``"支"`<br>```},`<br>```{`<br>```"settle_id"``: 506,`<br>```"rec_id"``: 999,`<br>```"process_id"``: 2016,`<br>```"spec_id"``: 8666,`<br>```"batch_no"``:``"PS2024121307DFH20250528202505cp002"``,`<br>```"expire_date"``:``"2025-05-31"``,`<br>```"settle_num"``: 1,`<br>```"proportion"``: 0.3333,`<br>```"warehouse_id"``: 319,`<br>```"cost_total"``: 1.4513,`<br>```"stockin_price"``: 1.4513,`<br>```"process_no"``:``"PS2024121307"``,`<br>```"spec_code"``:``"cp002"``,`<br>```"spec_name"``:``""``,`<br>```"base_unit_id"``: 2,`<br>```"spec_no"``:``"cp002"``,`<br>```"barcode"``:``"cp002"``,`<br>```"remark"``:``""``,`<br>```"cost"``:``"1.4513"``,`<br>```"defect"``: 0,`<br>```"cost_price"``:``"11.1000"``,`<br>```"share_other_fee"``:``"0.0000"``,`<br>```"warehouse_name"``:``"nff正品仓"``,`<br>```"base_unit_name"``:``"支"`<br>```},`<br>```{`<br>```"settle_id"``: 506,`<br>```"rec_id"``: 1000,`<br>```"process_id"``: 2016,`<br>```"spec_id"``: 8667,`<br>```"batch_no"``:``"PS2024121307DFH20250528202505cp003"``,`<br>```"expire_date"``:``"2025-06-01"``,`<br>```"settle_num"``: 1,`<br>```"proportion"``: 0.4001,`<br>```"warehouse_id"``: 319,`<br>```"cost_total"``: 1.7422,`<br>```"stockin_price"``: 1.7422,`<br>```"process_no"``:``"PS2024121307"``,`<br>```"spec_code"``:``"cp003"``,`<br>```"spec_name"``:``""``,`<br>```"base_unit_id"``: 2,`<br>```"spec_no"``:``"cp003"``,`<br>```"barcode"``:``"cp003"``,`<br>```"remark"``:``""``,`<br>```"cost"``:``"1.7422"``,`<br>```"defect"``: 0,`<br>```"cost_price"``:``"6.5900"``,`<br>```"share_other_fee"``:``"0.0000"``,`<br>```"warehouse_name"``:``"nff正品仓"``,`<br>```"base_unit_name"``:``"支"`<br>```}`<br>```]`<br>```}`<br>```]`<br>```},`<br>```"status"``: 0`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.process.search#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"参数中必须包含起止时间"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

[1.接口说明](javascript:dgoto('1.%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E'))

[2.调用场景](javascript:dgoto('2.%E8%B0%83%E7%94%A8%E5%9C%BA%E6%99%AF'))

[3.请求参数说明](javascript:dgoto('3.%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E'))

[3.1 请求地址](javascript:dgoto('3.1 %E8%AF%B7%E6%B1%82%E5%9C%B0%E5%9D%80'))

[3.2 公共请求参数](javascript:dgoto('3.2 %E5%85%AC%E5%85%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0'))

[3.3 业务请求参数](javascript:dgoto('3.3 %E4%B8%9A%E5%8A%A1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0'))

[4.响应参数](javascript:dgoto('4.%E5%93%8D%E5%BA%94%E5%8F%82%E6%95%B0'))

[5.请求示例](javascript:dgoto('5.%E8%AF%B7%E6%B1%82%E7%A4%BA%E4%BE%8B'))

[6.响应示例](javascript:dgoto('6.%E5%93%8D%E5%BA%94%E7%A4%BA%E4%BE%8B'))

[6.1 正常响应示例](javascript:dgoto('6.1 %E6%AD%A3%E5%B8%B8%E5%93%8D%E5%BA%94%E7%A4%BA%E4%BE%8B '))

[6.2 异常响应示例](javascript:dgoto('6.2 %E5%BC%82%E5%B8%B8%E5%93%8D%E5%BA%94%E7%A4%BA%E4%BE%8B'))

[常用工具](javascript:dgoto('G%E5%B8%B8%E7%94%A8%E5%B7%A5%E5%85%B7'))

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1