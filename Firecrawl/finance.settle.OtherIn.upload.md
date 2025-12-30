---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.OtherIn.upload"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

库存类

移位单查询

库存查询

创建盘点单

其他入库单新建

调拨单查询

其他出库单查询

其他入库单查询

调拨入库单查询

可用库存查询

其他出库单新建

调拨出库单查询

调拨单入库取消

盘点入库单查询

盘点出库单查询

调拨单出库取消

调拨单取消

调拨入库单新建

调拨出库单新建

调拨单新建

补货单查询

库存变化查询

存货成本查询

调拨单停止等待

其它出库业务单创建

其它入库业务单创建

生产出库查询

生产入库查询

外仓调整出库单创建

外仓调整入库单创建

外仓调整出库单查询

外仓调整入库单查询

调拨结算查询

正残转换单查询

其它出库业务单查询

其它入库业务单查询

分拣单全览

默认货位查询

虚拟仓库存查询

虚拟仓单据创建

虚拟仓单据查询

装箱单查询

JIT退货入库单查询

JIT出库单查询

SN码查询

其它入库业务结算单创建

库存查询2

出库瞬时成本查询

入库瞬时成本查询

盘点单查询

盘点单明细查询

入库单查询

出库单查询

库存明细查询

出库SN查询

入库SN查询

入库SN明细推送

出库SN明细推送

其他入库单取消

其他出库单取消

电子面单号查询

箱码新建

其他入库业务单据取消

其他出库业务单据取消

虚拟仓库存分配策略创建

虚拟仓库存释放策略新建

外仓快速调拨

当前位置： API文档 > 库存类

**finance.settle.OtherIn.upload（其它入库业务结算单创建）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：创建其它入库业务结算单给ERP |
| **1.2 适用版本：** 客户端 V1.4.4.1及以上版本 |
| **1.3 权限校验：【仓库权限】、【供应商权限】** |
| **1.4注意事项：** 不支持批量创建 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据信息 | order\_info | Map<String, Object> |  | 是 | 单据信息 |
| 明细信息 | detail\_list | List<Map<String, Object>> |  | 否 | 明细信息 |

**order\_info**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 其它入库业务单号 | other\_in\_no | String | 40 | 是 | 其它入库业务单号 |
| 物流单号 | logistics\_no | String | 100 | 否 | 物流单号 |
| 物流公司编号 | logistics\_company\_no | String | 20 | 否 | ERP内手动维护的物流公司编号 |
| 运费 | post\_fee | Decimal(19,4) |  | 否 | 运费 |
| 供应商编号 | provider\_no | String | 40 | 否 | 填写供应商的情况下会校验供应商权限 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 是否审核 | is\_check | boolean |  | 否 | 默认false,审核失败情况下单据会创建失败 |
| 模糊查询 | fuzzy\_query | boolean |  | 否 | 默认false,业务单号进行模糊查询匹配，匹配数量大于1条时会报错 |

**detail\_list**

| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 是否残次品 | defect | boolean |  | 否 | true:残次品<br>false:正品<br>默认false |
| 入库价 | stockin\_price | Decimal(19,4) |  | 否 | 匹配对应入库价的明细，没有则按照商家编码+残次品的维度匹配 |
| 单价 | price | Decimal(19,4) |  | 否 | 不传默认为入库单明细的入库价 |
| 分摊邮费 | share\_post\_fee | Decimal(19,4) |  | 否 | 分摊邮费 |
| 备注 | remark | String |  | 否 | 备注 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 响应正文数据 | data | <Map<String, Object> |  | 否 | 有错误信息时不返回此节点 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 结算单号 | order\_no | String | 64 | 是 | 结算单号 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31 | `[`<br>```{`<br>```"other_in_no"``:``"QR0812"``,`<br>```"logistics_no"``:``"204875027045785"``,`<br>```"logistics_company_no"``:``"ytz3"``,`<br>```"post_fee"``:``"5"``,`<br>```"provider_no"``:``""``,`<br>```"remark"``:``"这是个备注o"``,`<br>```"is_check"``:``true`<br>```},`<br>```[`<br>```{`<br>```"spec_no"``:``"daba1"``,`<br>```"price"``:``"2.05"``,`<br>```"share_post_fee"``:``"1"``,`<br>```"remark"``:``"spec1"`<br>```},`<br>```{`<br>```"spec_no"``:``"daba2"``,`<br>```"price"``:``"1.05"``,`<br>```"share_post_fee"``:``"2"``,`<br>```"remark"``:``"spec2"`<br>```},`<br>```{`<br>```"spec_no"``:``"daba3"``,`<br>```"price"``:``"3.05"``,`<br>```"share_post_fee"``:``"3"``,`<br>```"remark"``:``"spec3"`<br>```}`<br>```]`<br>`]` | |
| PHP | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client = new WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$order = new stdClass();`<br>`$order->other_in_no =``'QR0812'``;`<br>`$order->logistics_no =``'204875027045785'``;`<br>`$order->logistics_company_no =``'ytz3'``;`<br>`$order->post_fee =``'5'``;`<br>`$order->provider_no =``''``;`<br>`$order->remark =``'这是个备注o'``;`<br>`$order->is_check = 1;`<br>`$spec1 = new stdClass();`<br>`$spec1->spec_no =``'daba1'``;`<br>`$spec1->price =``'2.05'``;`<br>`$spec1->share_post_fee =``'1'``;`<br>`$spec1->remark =``'spec1'``;`<br>`$spec2 = new stdClass();`<br>`$spec2->spec_no =``'daba2'``;`<br>`$spec2->price =``'1.05'``;`<br>`$spec2->share_post_fee =``'2'``;`<br>`$spec2->remark =``'spec2'``;`<br>`$spec3 = new stdClass();`<br>`$spec3->spec_no =``'daba3'``;`<br>`$spec3->price =``'3.05'``;`<br>`$spec3->share_post_fee =``'3'``;`<br>`$spec3->remark =``'spec3'``;`<br>`$specList = array($spec1, $spec2, $spec3);`<br>`$data = $client->call(``"finance.settle.OtherIn.upload"``, $order, $specList);`<br>`?>` | |
| JAVA |  |
| C# |  |

### **6.响应示例**

### 6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | `{`<br>```"status"``: 0,`<br>```"data"``:`<br>```{`<br>```"order_no"``:``"JS202212210005"`<br>```}`<br>`}` | |

#### 6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"物流公司不存在或类型错误"`<br>`}` | |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1