---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search"
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

**wms.StockSpec.search** **（库存查询）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP单品（sku）的库存量 |
| **1.2 适用版本：** 客户端 V1.6.0.10及以上版本 |
| **1.3 增量获取：** 支持增量获取 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5 注意事项：** **【权限校验】：仓库权限**<br>销量统计数据字段说明及计算方式， [**点击链接查看**](https://www.yuque.com/wdterpqjb/cangchu/zggh20xg7n1ywwao)<br>库存量字段说明， [**点击链接查看**](https://www.yuque.com/wdterpqjb/cangchu/bah0eaw8vacegf08)<br>**接口已过时, 请使用[wms.StockSpec.search2](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search2)** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：** 自研商城、分销系统、全渠道等系统对接 |

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
| 开始时间 | start\_time | String | 40 | N | 开始时间(最后更新时间) , 传入商家编码时可传空值 |
| 结束时间 | end\_time | String | 40 | N | 结束时间(最后更新时间), 传入商家编码时可传空值 |
| 商家编码 | spec\_nos | List<String> | 40 | N | 商家编码列表 |
| 仓库编号 | warehouse\_no | String | 40 | N | 仓库编号 |
| 掩码 | mask | Int | 11 | N | 1: 返回销量统计数据; 2: 返回成本价数据; 3:返回销售统计数据和成本价数据<br>不传默认为0 |
| 是否需要警戒相关信息 | need\_alarm\_info | Int | 1 | N | 0：否<br>1：是  （比较影响性能 慎用）<br>不传默认为0 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | N | 分页大小（最大不超1000） |
| 页号 | page\_no | Int | 4 | N | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int | 11 | Y | 返回0为正常 |
| 数据条数 | total | Int | 11 | N | 查询结果总条数 |
| 错误信息 | message | String | 255 | N | 无错误信息不返回 |
| 单据数据 | data | List<Map<String, Object>> |  | N | 库存相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细唯一键 | rec\_id | Int | 11 | Y | 明细唯一键 |
| 残次品 | defect | Int | 1 | Y | 0,正品;1,残品 |
| 库存量 | stock\_num | Decimal(19,4) |  | Y | 库存量 |
| 外部库存 | wms\_sync\_stock | Decimal(19,4) |  | Y | 外部WMS同步时库存 |
| 库存差异 | wms\_stock\_diff | Decimal(19,4) |  | Y | 外部WMS同步时,与系统库存的差 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 单品id | spec\_id | Int |  | Y | 单品唯一键 |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 规格码 | spec\_code | String | 40 | Y | 规格码 |
| 品牌名称 | brand\_name | String | 40 | Y | 品牌名称 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 条码 | barcode | String | 50 | Y | 条码 |
| 未付款量 | unpay\_num | Decimal(19,4) |  | Y | 未付款量 |
| 预订单量 | subscribe\_num | Decimal(19,4) |  | Y | 预订单量 |
| 待审核量 | order\_num | Decimal(19,4) |  | Y | 待审核量 |
| 待发货量 | sending\_num | Decimal(19,4) |  | Y | 待发货量 |
| 采购在途量 | purchase\_num | Decimal(19,4) |  | Y | 采购在途量 |
| 调拨在途量 | transfer\_num | Decimal(19,4) |  | Y | 调拨在途量 |
| 待采购量 | to\_purchase\_num | Decimal(19,4) |  | Y | 待采购量 |
| 采购到货量 | purchase\_arrive\_num | Decimal(19,4) |  | Y | 采购到货量 |
| 外部WMS同步时占用库存 | wms\_preempty\_stock | Decimal(19,4) |  | Y | 外部WMS同步时占用库存 |
| 重量 | weight | Decimal(19,4) |  | Y | 重量 |
| 图片URL | img\_url | String | 1024 | Y | 图片URL |
| 仓库编号 | warehouse\_no | String | 40 | Y | 仓库编号 |
| 仓库id | warehouse\_id | Int | 6 | Y | 仓库id，仓库唯一键 |
| 仓库名称 | warehouse\_name | String | 64 | Y | 仓库名称 |
| 仓库类型 | warehouse\_type | Int | 4 | Y | 仓库类型0为普通,非0为外部WMS |
| 可发库存 | available\_send\_stock | Decimal(19,4) |  | Y | 可发库存 |
| 创建时间 | created | String | 40 | Y | 创建时间 |
| 修改时间 | modified | String | 40 | Y | 修改时间 |
| 部分付款库存 | part\_paid\_num | Decimal(19,4) |  | Y | 部分付款库存 |
| 销售换货在途量 | refund\_exch\_num | Decimal(19,4) |  | Y | 销售换货在途量(卖家发给买家) |
| 销售退货量 | refund\_num | Decimal(19,4) |  | Y | 销售退货量 |
| 销售退货在途量 | refund\_onway\_num | Decimal(19,4) |  | Y | 销售换货在途量(从买家回到卖家) |
| 采购换货量 | return\_exch\_num | Decimal(19,4) |  | Y | 采购换货量 |
| 采购退货量 | return\_num | Decimal(19,4) |  | Y | 采购退货量 |
| 采购换货在途量 | return\_onway\_num | Decimal(19,4) |  | Y | 采购换货在途量 |
| 待调出量 | to\_transfer\_num | Decimal(19,4) |  | Y | 待调出量 |
| 外部WMS同步时,占用库存差 | wms\_preempty\_diff | Decimal(19,4) |  | Y | 外部WMS同步时,占用库存差 |
| 与外部wms同步时间 | wms\_sync\_time | String | 40 | Y | 与外部wms同步时间 |
| 库存备注 | remark | String | 500 | Y | 单品在当前仓库记录的备注 |
| 锁定量 | lock\_num | Decimal(19,4) |  | Y | 库存锁定量 |
| 标记id | flag\_id | Int |  | Y | 标记id |
| 标记名称 | flag\_name | String |  | Y | 标记名称 |
| 品牌编号 | brand\_no | Sring |  | Y | 品牌编号 |
| 其他待出库量 | to\_other\_out\_num | Decimal(19,4) |  | Y | 其他待出库量 |
| 其他待入库量 | to\_other\_in\_num | Decimal(19,4) |  | Y | 其他待入库量 |
| 生产待出库量 | to\_process\_out\_num | Decimal(19,4) |  | Y | 生产待出库量 |
| 生产待入库量 | to\_process\_in\_num | Decimal(19,4) |  | Y | 生产待入库量 |
| 待调拨量 | wait\_transfer\_num | Decimal(19,4) |  | Y | 待调拨量 |
| 上次盘点时间 | last\_pd\_time | String |  | Y | 上次盘点时间 |
| 上次出入库时间 | last\_inout\_time | String |  | Y | 上次出入库时间 |
| 自定义库存1 | sys\_user\_define\_stock1 | Decimal(19,4) |  | Y | 自定义库存1 |
| 自定义库存2 | sys\_user\_define\_stock2 | Decimal(19,4) |  | Y | 自定义库存2 |
| 已质检库存 | inspect\_num | Decimal(19,4) |  | Y | 已质检库存 |
| 未发货订单总数 | trade\_reserve\_num | Decimal(19,4) |  | Y | 未发货订单总数 |
| 单位 | unit\_name | String | 20 | Y | 单位 |
| 辅助单位 | aux\_unit\_name | String | 20 | Y | 辅助单位 |
| 生产在途量 | process\_onway\_num | Decimal(19,4) |  | Y | 生产在途量 |
| 状态 | status | Int |  | Y | 0：未启用<br>1：启用<br>2：停用 |
| 销量统计数据 |  |  |  |  |  |
| 今日销量 | today\_num | Decimal(19,4) |  | Y | 今日销量      请求参数：mask（掩码）传为1和3时返回 |
| 昨日销量 | num\_yesterday | Decimal(19,4) |  | Y | 昨日销量      请求参数：mask（掩码）传为1和3时返回 |
| 7天销量 | num\_7days | Decimal(19,4) |  | Y | 7天销量       请求参数：mask（掩码）传为1和3时返回 |
| 14天销量 | num\_14days | Decimal(19,4) |  | Y | 14天销量请求参数：mask（掩码）传为1和3时返回 |
| 月销量 | num\_month | Decimal(19,4) |  | Y | 月销量请求参数：mask（掩码）传为1和3时返回 |
| 总销量 | num\_all | Decimal(19,4) |  | Y | 总销量         请求参数：mask（掩码）传为1和3时返回 |
| 60天销量 | num\_60days | Decimal(19,4) |  | Y | 60天销量         请求参数：mask（掩码）传为1和3时返回 |
| 90天销量 | num\_90days | Decimal(19,4) |  | Y | 90天销量         请求参数：mask（掩码）传为1和3时返回 |
| 成本价数据 |  |  |  |  |  |
| 成本价 | cost\_price | Decimal(19,4) |  | Y | 成本价          请求参数：mask（掩码）传为2和3时返回 |
| 警戒相关 |  |  |  |  |  |
| 警戒库存下限 | safe\_stock | Decimal(19,4) |  | N | 警戒库存下限 |
| 警戒库存上限 | safe\_stock\_uppe | Decimal(19,4) |  | N | 警戒库存上限 |
| 警戒类型 | alarm\_type | Int |  | N | 0:"使用全局设置",<br>1:"不刷新警戒库存",<br>2:"按销售增长率刷新",<br>3:"按历史平均销量刷新",<br>4:"按历史加权平均销量刷新" |
| 警戒天数下限 | alarm\_days | Decimal(19,4) |  | N | 警戒天数下限 |
| 警戒天数上限 | alarm\_days\_upper | Decimal(19,4) |  | N | 警戒天数上限 |
| 计算周期（天) | cycle\_days | Decimal(19,4) |  | N | 计算周期（天) |

**5.请求示例**

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.StockSpec.search#autoTab0_3)

```
[{\
      "start_time":   "2019-12-01 00:00:00",\
      "end_time":   "2019-12-20 00:00:00",\
      "spec_nos":   ["daba1"]\
}]
```

```
<?php
header("Content-Type: text/html;   charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new   WdtErpClient("url", "wdtapi3", "appkey",   "secret");

$parMap = new stdClass();
$parMap->start_time = '2019-12-01   00:00:00';
$parMap->end_time = '2019-12-20   00:00:00';
$parMap->spec_nos =   ["daba1"];

$pager = new Pager(10, 0, true);
$data =   $client->pageCall("wms.StockSpec.search", $pager,  $parMap);
$php_json = json_encode($data,   JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
echo $php_json;
?>
```

```

```

```

```

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "total": 1,<br>    "data": [{<br>        "goods_no": "wangdiantong",<br>        "goods_name": "wangdiantong",<br>        "spec_code": "LL ",<br>        "spec_name": "暂无",<br>        "barcode": "wangdiantong",<br>        "weight": 0.2,<br>        "img_url": "cos:\/\/IMG135.jpg",<br>        "spec_no": "wangdiantong",<br>        "spec_id": 1,<br>        "brand_name": "发发拉",<br>        "brand_no": "ffl",<br>        "rec_id": 291344,<br>        "defect": 1,<br>        "status": 1,<br>        "stock_num": 3,<br>        "unpay_num": 0,<br>        "subscribe_num": 0,<br>        "order_num": 0,<br>        "sending_num": 0,<br>        "purchase_num": 0,<br>        "transfer_num": 0,<br>        "to_transfer_num": 0,<br>        "to_other_out_num": 0,<br>        "to_process_out_num": 0,<br>        "to_process_in_num": 0,<br>        "to_purchase_num": 0,<br>        "purchase_arrive_num": 0,<br>        "return_num": 0,<br>        "return_exch_num": 0,<br>        "return_onway_num": 0,<br>        "refund_num": 0,<br>        "refund_exch_num": 0,<br>        "refund_onway_num": 0,<br>        "part_paid_num": 0,<br>        "wms_sync_stock": 0,<br>        "wms_stock_diff": 0,<br>        "wms_preempty_stock": 0,<br>        "wms_preempty_diff": 0,<br>        "modified": "2023-04-10 14:09:55",<br>        "created": "2023-02-09 18:14:31",<br>        "warehouse_id": 624,<br>        "warehouse_no": "wdtapi3-test",<br>        "warehouse_name": "wdtapi3-test",<br>        "warehouse_type": 1,<br>        "available_send_stock": 3,<br>        "remark": "",<br>        "flag_id": 0,<br>        "flag_name": "无",<br>        "lock_num": 0,<br>        "last_pd_time": "2023-04-10 14:09:55",<br>        "last_inout_time": "2023-04-10 14:09:55",<br>        "today_num": 0,<br>        "num_7days": 0,<br>        "num_14days": 0,<br>        "num_month": 0,<br>        "num_all": 80,<br>        "cost_price": 0<br>    }]<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>       "status":   100,<br>       "message":   "仓库不存在 仓库编号: daba1"<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

1.接口说明

2.调用场景

3.请求参数说明

3.1 请求地址

3.3 业务请求参数

4.响应参数

5.请求示例

6.响应示例

6.1 正常响应示例

6.2 异常响应示例

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1