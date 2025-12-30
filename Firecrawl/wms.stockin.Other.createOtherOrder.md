---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.createOtherOrder"
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

**wms.stockin.Other.createOtherOrder** **（其他入库单新建）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**ERP需要增加库存且入库单据没有对应的业务类型，推送其他入库单给ERP |
| **1.2 适用版本：** 客户端 V1.5.7.4及以上版本 |
| **1.3 增量获取：** |
| 1.4 时间跨度： |
| **1.5注意事项：****【权限校验】：仓库权限**<br>**不支持批量创建，一次只能推一单** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：** 线下ERP、SAP等系统对接 |

**3.请求参数说明**

3.1 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | http://47.92.239.46/openapi |
| 正式环境 | http://wdt.wangdian.cn/openapi |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单单据信息 | stockin\_order | Map<String, Object> |  | Y | 入库单单据信息 |

**stockin\_order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 外部单号 | outer\_no | String | 40 | Y | 外部单号，创建到ERP后最为入库单号展示 |
| 业务单号 | src\_order\_no | String | 40 | N | 当不传入业务单号的情况下，自动创建业务单并关联 |
| 仓库编码 | warehouse\_no | String | 40 | Y | 仓库编码 |
| 物流单号 | logistics\_no | String | 40 | N | 物流单号 |
| 物流编号 | logistics\_code | String | 60 | N | 物流编号（ERP系统物流编号） |
| 创建后的单据状态 | is\_check | Int |  | N | 0：待审核<br>1：已审核<br>2：编辑中<br>默认0 |
| 入库原因 | reason | String | 255 | N | 入库原因（在ERP内要维护才可以推送成功） |
| 备注 | remark | String | 255 | N | 备注 |
| 货品详情 | goods\_list | List<Map<String, Object>> |  | Y | 货品详情 |

**goods\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 入库数量 | num | Decimal(19,4) |  | Y | 入库数量 |
| 备注 | remark | String | 255 | N | 备注 |
| 批次号 | batch\_no | String | 20 | N | 批次号（如果传入系统内不存在的批次信息, 将自动创建此批次信息） |
| 货位编号 | position\_no | String | 50 | N | 货位编号 |
| 生产日期 | production\_date | String | 40 | N | 生产日期 |
| 有效期 | expire\_date | String | 40 | N | 有效期 |
| 残次品 | defect | bool | 1 | N | 残次品<br>true：是<br>false：否 |
| 入库价 | stockin\_price | Decimal(19,4) |  | N | 不填取该货品在对应仓库下的实际成本或计划成本（以系统配置中的【系统运行成本价(实际成本)计算方式】为准） |
| 序列号 | sn\_list | List<String> | 255 | N | 序列号（序列号个数要与入库数量保持一致） |
| sn新列表 | sn\_new\_list | List<Map<String, Object>> |  | N | sn新列表<br>sn\_list和sn\_new\_list当存在序列号的情况下 有一个必传，sn\_list优先级最高 |

**sn\_new\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 序列号 | sn\_no | String | 80 | Y | 序列号 |
| --- | --- | --- | --- | --- | --- |
| 序列号集合码 | sn\_suite\_no | String | 80 | Y | 序列号集合码 |
| --- | --- | --- | --- | --- | --- |

**4.响应参** **数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | Y | 结果信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回信息 | message | String |  | Y | 如果创建/修改成功message内容为入库单号,否则为错误信息 |
| 状态码 | status | Int |  | Y | 0：操作全部成功<br>20：审核失败 |

**5.请求示例**

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.createOtherOrder#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.createOtherOrder#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.createOtherOrder#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.createOtherOrder#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | `[`<br>```{`<br>```"outer_no"``:``"CG2019112800061234567890"``,`<br>```"warehouse_no"``:``"ytz"``,`<br>```"goods_list"``: [`<br>```{`<br>```"spec_no"``:``"gy01"``,`<br>```"num"``:``"3"``,`<br>```"stockin_price"``: 123,`<br>```"sn_list"``:[``"sn001"``,``"sn002"``,``"sn003"``]`<br>```}`<br>```]`<br>```}`<br>`]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19 | `<?php`<br>`header(``"Content-Type: text/html;   charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$order``=``new``stdClass();`<br>`$order``->outer_no=``"CG201911280004"``;`<br>`$order``->warehouse_no=``"1001"``;`<br>``<br>`$orderDetail``=``new``stdClass();`<br>`$orderDetail``->spec_no=``"PC_2016"``;`<br>`$orderDetail``->num=``"1.5"``;`<br>`$order``->goods_list = [``$orderDetail``];`<br>``<br>``<br>`$response``=``$client``->call(``"wms.stockin.Other.createOtherOrder"``,``$order``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.createOtherOrder#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"message"``:``"ljcs39423423422"``,`<br>```"status"``: 0`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.Other.createOtherOrder#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"外部单号重复!"`<br>`}` |

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

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1