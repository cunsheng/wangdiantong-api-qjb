---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Manage.queryWithDetail"
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

**wms.stocktransfer.Manage.queryWithDetail** **（调拨单查询）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP调拨单据信息 |
| **1.2 适用版本：** 客户端 V1.5.7.2及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** 财务系统、SAP、线下ERP、数据分析等系统的对接 |

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
| 分页大小 | page\_size | int |  | N | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | N | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | N | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |
| 分页 | pager | Pager |  | Y | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 最后修改时间 |
| 结束时间 | end\_time | String | 40 | Y | 最后修改时间 |
| 源仓库编号 | from\_warehouse\_no | String | 40 | N | 源仓库编号 |
| 目标仓库编号 | to\_warehouse\_no | String | 40 | N | 目标仓库编号 |
| 调拨单号 | transfer\_no | String | 20 | N | 调拨单号 |
| 调拨单状态 | status | String | 4 | N | 10：已取消<br>20：编辑中<br>30：待审核<br>40：已审核<br>50：调拨中<br>80：待结算<br>90：调拨完成<br>多个状态之间使用英文逗号分隔 |
| 模糊查询 | fuzzy\_query | boolean | 1 | N | 默认false,业务单号进行模糊查询匹配，匹配数量大于1条时会报错 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小 |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 单据信息 | data | Map<String,Object> |  | N | 单据信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | N | 查询条件总单据数 |
| 单据数据 | order | List<Map<String, Object>> |  | Y | 单据数据 |

**order**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调拨单id | transfer\_id | Int | 11 | Y | 调拨单id |
| 调拨单号 | transfer\_no | String | 40 | Y | 调拨单号 |
| 调拨模式 | mode | Int | 4 | Y | 调拨类型：<br>0：单品调拨<br>1：货位调拨<br>2：明细调拨<br>4：外仓快速调拨<br>5：单品调拨(出+入)<br>6：货位调拨(出+入)<br>7：明细调拨(出+入)<br>8：单品调拨(仅出库)<br>9：货位调拨(仅出库)<br>10：明细调拨(仅出库)<br>11：自动调拨<br>14：外仓明细调拨（出+入） |
| 调拨单状态 | status | Int | 4 | Y | 调拨单状态: <br>10：已取消<br>20：编辑中<br>30：待审核<br>40：已审核<br>50：调拨中<br>80：待结算<br>90：调拨完成 |
| 出入库状态 | stock\_out\_in\_status | Int | 4 | Y | 出入库状态<br>10：待出库<br>20：部分出库未入库<br>30：部分出库部分入库<br>40：全部出库未入库<br>50：全部出库部分入库<br>60：已完成 |
| 目标仓联系人 | contact | String | 40 | Y | 目标仓联系人 |
| 联系电话 | telno | String | 40 | Y | 联系人电话 |
| 调拨开单量 | goods\_count | Decimal(19,4) |  | Y | 调拨开单量 |
| 货品种类 | goods\_type\_count | Int | 6 | Y | 货品种类 |
| 已入库总量 | goods\_in\_count | Decimal(19,4) |  | Y | 已入库总量 |
| 已出库总量 | goods\_out\_count | Decimal(19,4) |  | Y | 已出库总量 |
| 最后修改时间 | modified | String | 40 | Y | 最后修改时间（时间戳格式） |
| 创建时间 | created | String | 40 | Y | 创建时间（时间戳格式） |
| 审核时间 | check\_time | String | 40 | Y | 审核时间 |
| 备注 | remark | String | 255 | Y | 备注 |
| 源仓库编号 | from\_warehouse\_no | String | 40 | Y | 源仓库编号 |
| 目标仓库编号 | to\_warehouse\_no | String | 40 | Y | 目标仓库编号 |
| 物流方式 | logistics\_type | Int | 6 | N | 物流方式，可点击查看 [物流代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_wlysb) |
| 物流单号 | logistics\_no | String | 40 | Y | 物流单号 |
| 物流名称 | logistics\_name | String | 40 | Y | 系统物流公司名称 |
| 物流公司编号 | logistics\_code | String | 20 | Y | 系统物流公司编号 |
| 物流公司主键 | logistics\_id | Int | 6 | Y | 物流公司主键 |
| 创建者 | creator\_name | String | 40 | Y | 创建者 |
| 目标仓库id | to\_warehouse\_id | Int | 6 | Y | 目标仓库id |
| 调出仓库id | from\_warehouse\_id | Int | 6 | Y | 调出仓库id |
| 修改时间 | modified\_date | String | 40 | Y | 修改时间（时间格式） |
| 创建时间 | created\_date | String | 40 | Y | 创建时间（时间格式） |
| wms出库业务单号 | wms\_out\_code | String | 100 | N | wms出库业务单号 |
| wms入库业务单号 | wms\_in\_code | String | 100 | N | wms入库业务单号 |
| 标记名称 | flag\_name | String |  | Y | 标记名称 |
| 调拨单详情 | details\_list | List<Map<String, Object>> |  | Y | 调拨单详情 |

**details\_list**

| 字段 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调拨单id | transfer\_id | Int | 11 | Y | 调拨单id |
| 明细id | rec\_id | Int | 11 | Y | 明细id |
| 有效期 | expire\_date | String | 40 | N | 有效期 |
| 批次id | batch\_id | Int | 11 | Y | 批次id |
| 批次号 | batch\_no | String | 40 | Y | 批次号 |
| 库存数量 | stock\_num | Decimal(19,4) |  | Y | 库存数量 (显示用,不做依据) |
| 调拨数量 | num | Decimal(19,4) |  | Y | 调拨数量 |
| 已出库数量 | out\_num | Decimal(19,4) |  | Y | 已出库数量 |
| 已入库数量 | in\_num | Decimal(19,4) |  | Y | 已入库数量 |
| 备注 | remark | String | 255 | Y | 备注 |
| 辅助数量 | aux\_num | Decimal(19,4) |  | Y | 辅助数量 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 规格名称 | spec\_name | String | 255 | Y | 规格名称 |
| 货品主键id | goods\_id | Int | 11 | Y | 货品主键id |
| 单品主键id | spec\_id | Int | 11 | Y | 单品主键id |
| 出库货位 | from\_position | String | 20 | Y | 出库货位 |
| 主条码 | barcode | String | 50 | Y | 主条码 |
| 入库货位 | to\_position | String | 20 | N | 入库货位 |
| 单位 | unit\_name | String | 20 | N | 单位 |
| 辅助单位 | aux\_unit\_name | String | 20 | N | 辅助单位 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间，<br>格式: yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | String |  | Y | 创建时间，<br>格式: yyyy-MM-dd HH:mm:ss |
| 是否残次品 | defect | bool | 1 | Y | 残次品：true<br>正品：false |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Manage.queryWithDetail#autoTab5_0)
- [php 请求示例](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Manage.queryWithDetail#autoTab5_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Manage.queryWithDetail#autoTab5_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stocktransfer.Manage.queryWithDetail#autoTab5_3)

```
[{\
       "start_time": "2019-12-11 00:00:00",\
       "end_time": "2019-12-31 00:00:00"\
}]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$params=new stdClass();
$params->start_time = '2019-12-11 00:00:00';
$params->end_time = '2019-12-31 00:00:00';

$pager = new Pager(1, 0, true);
$data = $client->pageCall("wms.stocktransfer.Manage.queryWithDetail", $pager, $params);

?>
```

```

```

```

```

**6.响应示** **例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "total_count": 1,<br>        "order": [{<br>            "details_list": [{<br>                "rec_id": 8778,<br>                "transfer_id": 4379,<br>                "batch_id": 0,<br>                "batch_no": "",<br>                "stock_num": 412025,<br>                "num": 1,<br>                "out_num": 0,<br>                "in_num": 0,<br>                "remark": "test1",<br>                "aux_num": 0.1,<br>                "goods_id": 83223,<br>                "goods_no": "951027",<br>                "spec_id": 235348,<br>                "spec_no": "951027",<br>                "spec_code": "",<br>                "spec_name": "false",<br>                "barcode": "95102711",<br>                "from_position": "",<br>                "unit_name": "\u516c\u65a4",<br>                "aux_unit_name": "\u7bb1\u89c4",<br>                "defect": false,<br>                "created": "2024-07-24 14:00:21",<br>                "modified": "2024-07-24 14:00:21"<br>            }, {<br>                "rec_id": 8779,<br>                "transfer_id": 4379,<br>                "batch_id": 0,<br>                "batch_no": "",<br>                "stock_num": 659,<br>                "num": 1,<br>                "out_num": 0,<br>                "in_num": 0,<br>                "remark": "test2",<br>                "aux_num": 1,<br>                "goods_id": 399586,<br>                "goods_no": "cmc",<br>                "spec_id": 612030,<br>                "spec_no": "cmc",<br>                "spec_code": "",<br>                "spec_name": "111",<br>                "barcode": "",<br>                "from_position": "",<br>                "unit_name": "\u8f86",<br>                "defect": false,<br>                "created": "2024-07-24 14:00:21",<br>                "modified": "2024-07-24 14:00:21"<br>            }],<br>            "logistics_name": "",<br>            "to_warehouse_id": 1249,<br>            "goods_type_count": 2,<br>            "remark": "",<br>            "goods_count": 2,<br>            "wms_in_code": "OSI202407240010",<br>            "telno": "13833332222",<br>            "logistics_id": 0,<br>            "from_warehouse_no": "wdtapi3-test9",<br>            "mode": 0,<br>            "transfer_no": "zd20240724000123",<br>            "contact": "zd",<br>            "stock_out_in_status": 10,<br>            "modified": 1721800821000,<br>            "to_warehouse_no": "zd001",<br>            "goods_out_count": 0,<br>            "logistics_no": "",<br>            "goods_in_count": 0,<br>            "created": 1721800821000,<br>            "transfer_id": 4379,<br>            "logistics_code": "",<br>            "modified_date": "2024-07-24 14:00:21",<br>            "from_warehouse_id": 884,<br>            "creator_name": "",<br>            "created_date": "2024-07-24 14:00:21",<br>            "status": 40,<br>            "check_time": "2024-07-24 14:00:21"<br>        }]<br>    }<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>       "status": 100,<br>       "message": "参数中必须包含起止时间"<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.2 公共请求参数

3.3业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1正常响应示例

6.2异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1