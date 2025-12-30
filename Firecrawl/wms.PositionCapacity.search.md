---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search"
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

**wms.PositionCapacity.search** **（默认货位查询)**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP单品（sku）默认货位 |
| **1.2 适用版本：** 客户端 V1.4.1.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：**start\_time、end\_time时间跨度不能大于7天 |
| **1.5注意事项：** **【权限校验】：仓库权限**、时间不传的情况下，warehouse\_no和spec\_no必传 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

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
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | 否 | 开始时间，最后修改时间 |
| 结束时间 | end\_time | String | 40 | 否 | 结束时间，最后修改时间 |
| 仓库编号 | warehouse\_no | String | 40 | 否 | 仓库编号（时间不传的情况下，仓库编号必传） |
| 商家编码 | spec\_no | String | 40 | 否 | 商家编码（时间不传的情况下，商家编码必传） |
| 货品编号 | goods\_no | String | 40 | 否 | 货品编号 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

**返回值为一个Map<String, Object>**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 货品数据 | data | Map<String, Object> |  | 是 | 货品相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据 | detail\_list | List<Map<String, Object>> |  | 是 | 数据明细 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键id | rec\_id | Int | 11 | 是 | 主键id |
| 残次品 | defect | boolean | 1 | 是 | true:残次品<br>false:正品 |
| 总库存 | stock\_num | Decimal(19,4) |  | 是 | 总库存 |
| 单品id | spec\_id | Int | 11 | 是 | 单品id |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品简称 | short\_name | String | 255 | 是 | 货品简称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 品牌名称 | brand\_name | String | 50 | 是 | 品牌名称 |
| 品牌id | brand\_id | Int | 11 | 是 | 品牌id |
| 分类名称 | class\_name | String | 50 | 是 | 分类名称 |
| 分类id | class\_id | Int | 11 | 是 | 分类id |
| 仓库id | warehouse\_id | Int | 11 | 是 | 仓库id |
| 仓库编号 | warehouse\_no | String | 40 | 是 | 仓库编号 |
| 货区id | zone\_id | Int | 11 | 是 | 货区id |
| 货区编号 | zone\_no | String | 40 | 是 | 货区编号 |
| 货位id | position\_id | Int | 11 | 是 | 货位id |
| 货位编号 | position\_no | String | 40 | 是 | 货位编号 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_3)

|     |     |
| --- | --- |
| 1 | `[{``"spec_no"``:``"all1"``,``"warehouse_no"``:``"daj1"``}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->spec_no =``"all1"``;`<br>`$parMap``->warehouse_no =``"daj1"``;`<br>`$parMap``->goods_no = all;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"wms.PositionCapacity.search"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"total_count"``: 2,`<br>```"detail_list"``: [{`<br>```"spec_code"``:``"all1"``,`<br>```"goods_name"``:``"阿拉蕾"``,`<br>```"class_id"``: 0,`<br>```"goods_no"``:``"all"``,`<br>```"stock_num"``: 217,`<br>```"brand_name"``:``"康师傅"``,`<br>```"zone_no"``:``"daj001"``,`<br>```"rec_id"``: 6804,`<br>```"spec_no"``:``"all1"``,`<br>```"brand_id"``: 5,`<br>```"zone_id"``: 915,`<br>```"defect"``:``true``,`<br>```"warehouse_no"``:``"daj1"``,`<br>```"spec_id"``: 158800,`<br>```"position_no"``:``"AD-1-2-1"``,`<br>```"short_name"``:``"阿拉啊啊"``,`<br>```"spec_name"``:``"颜色:蓝色"``,`<br>```"barcode"``:``"all1"``,`<br>```"class_name"``:``"无"``,`<br>```"position_id"``: 80095,`<br>```"warehouse_id"``: 533`<br>```}, {`<br>```"spec_code"``:``"all1"``,`<br>```"goods_name"``:``"阿拉蕾"``,`<br>```"class_id"``: 0,`<br>```"goods_no"``:``"all"``,`<br>```"stock_num"``: 3,`<br>```"brand_name"``:``"康师傅"``,`<br>```"zone_no"``:``"daj001"``,`<br>```"rec_id"``: 6803,`<br>```"spec_no"``:``"all1"``,`<br>```"brand_id"``: 5,`<br>```"zone_id"``: 915,`<br>```"defect"``:``false``,`<br>```"warehouse_no"``:``"daj1"``,`<br>```"spec_id"``: 158800,`<br>```"position_no"``:``"AD-1-1-2"``,`<br>```"short_name"``:``"阿拉啊啊"``,`<br>```"spec_name"``:``"颜色:蓝色"``,`<br>```"barcode"``:``"all1"``,`<br>```"class_name"``:``"无"``,`<br>```"position_id"``: 80098,`<br>```"warehouse_id"``: 533`<br>```}]`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.PositionCapacity.search#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``:100,`<br>`"message"``:``"商家编码不能为空"`<br>`}` |

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