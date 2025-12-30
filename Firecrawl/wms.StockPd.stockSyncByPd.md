---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.stockSyncByPd"
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

**wms.StockPd.stockSyncByPd** **（创建盘点单）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**ERP库存需要调整时，推送盘点库存单据给ERP |
| **1.2 适用版本：** 客户端 V1.5.9.52及以上版本 |
| **1.3 注意事项：【权限校验】：仓库权限**<br>盘点模式只允许单品盘点，该接口会将库存数据直接覆盖。相当于直接在ERP操作新建盘点单，盘点录入，执行盘点三个步骤。 |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** 线下ERP、SAP等系统对接 |

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
| 盘点单信息 | pdOrder | Map<String, Object> |  | Y | 盘点单信息 |
| 盘点单明细 | specList | List<Map<String, Object>> |  | Y | 盘点单明细，可以为空 |

**pdOrder**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 正残次品处理方式 | defect\_mode | Int | 4 | Y | 正残次品处理方式: <br>0 全部 <br>1 只盘正品 <br>2 只盘残品 |
| 备注 | remark | String | 255 | Y | 备注，若无可为”” |
| 是否严格模式 | is\_post\_error | bool | 1 |  | 0：非严格模式<br>1：严格模式（盘点单中某个单品不存在时会报错，单据创建失败）<br>默认0 |

**specList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 备注 | remark | String | 255 | Y | 备注(盘点录入的备注) |
| 盘点数量 | new\_num | String | 20 | Y | 盘点数量（仅支持正数盘点） |
| 残次品 | defect | Boolean | 1 | Y | 是否为残次品 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int | 11 | Y | 返回0为正常 |
| 错误信息 | message | String | 255 | Y | 无错误信息不返回 |
| 返回值 | data | Map<String, String> |  | Y | key为盘点ID，value为结算时错误信息，若无则为“ok”。 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 盘点单号 | pd\_no | String |  | Y | 盘点单号 |
| --- | --- | --- | --- | --- | --- |
| 有问题的商家编码（跳过的商家编码） | skip\_spec\_no | String |  | Y | 有问题的商家编码（跳过的商家编码） |
| --- | --- | --- | --- | --- | --- |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.stockSyncByPd#autoTab2_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.stockSyncByPd#autoTab2_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.stockSyncByPd#autoTab2_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.stockSyncByPd#autoTab2_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12 | `[{`<br>```"warehouse_no"``:``"1002"``,`<br>```"defect_mode"``:   1,`<br>```"remark"``:``"API TEST"`<br>```},`<br>```[{`<br>```"spec_no"``:``"PC_2018"``,`<br>```"remark"``:``"PD TEST"``,`<br>```"new_num"``:``"200.0000"``,`<br>```"defect"``:``false`<br>```}]`<br>`]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22 | `<?php`<br>`header(``"Content-Type: text/html;   charset=UTF-8"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$pdOrder``=``new``stdClass();`<br>`$pdOrder``->warehouse_no =``"1002"``;`<br>`$pdOrder``->defect_mode = 1;`<br>`$pdOrder``->remark =``"API   TEST"``;`<br>``<br>`$spec``=``new``stdClass();`<br>`$spec``->spec_no =``"PC_2018"``;`<br>`$spec``->remark =``"PD TEST"``;`<br>`$spec``->new_num =``"200.0000"``;`<br>`$spec``->defect = false;`<br>`$specList``=``array``();`<br>`array_push``(``$specList``,``$spec``);`<br>``<br>`$data``=``$client``->call(``"wms.StockPd.stockSyncByPd"``,``$pdOrder``,``$specList``);`<br>`$php_json``= json_encode(``$data``);`<br>`echo``$php_json``;`<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.stockSyncByPd#autoTab2_0)

|     |     |
| --- | --- |
| 1 | `{``"status"``:0,``"data"``:{``"pd_no"``:``"WP202503070003"``,``"8638"``:``"ok"``}}` |

#### 6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockPd.stockSyncByPd#autoTab3_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``:   100,`<br>```"message"``:``"商家编码全不存在或都已删除"`<br>`}` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2公共请求参数

3.3 业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1