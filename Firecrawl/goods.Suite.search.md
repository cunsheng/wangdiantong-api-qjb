---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Suite.search"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

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

****goods.Suite.search**（组合装查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述**：获取ERP中组合装界面的组合装资料 |
| **1.2 适用版本：** 客户端 V1.5.8.6及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5注意事项：**<br>1、 **【权限校验】：品牌权限**（旺店通客户端-采购-采购权限管理界面控制品牌权限）<br>2、开始时间和结束时间是 组合装 或 组合装明细 最后修改时间的范围 |

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
| 商家编码 | spec\_no | String | 40 | 否 | 商家编码 |
| 货品编号 | goods\_no | String | 40 | 否 | 货品编号 |
| 品牌编号 | brand\_name | String | 64 | 否 | 品牌编号 |
| 分类名称 | class\_name | String | 100 | 否 | 分类名称 |
| 条码 | barcode | String | 50 | 否 | 条码 |
| 组合装商家编码 | suite\_no | String | 40 | 否 | 组合装商家编码（如果不传时间，组合装商家编码必传） |
| 组合装名称 | suite\_name | String | 255 | 否 | 组合装名称 |
| 是否隐藏已删除的货品 | hide\_deleted | boolean | 1 | 否 | 默认隐藏 |
| 开始时间 | start\_time | String | 40 | 否 | 起始修改时间 |
| 结束时间 | end\_time | String | 40 | 否 | 结束修改时间, 不填默认为当前时间 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 货品数据 | data | Map<String, Object> |  | 是 | 货品相关数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品数据 | suite\_list | List<Map<String, Object>> |  | 是 | 货品数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总数单据 |

**suite\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 组合装id | suite\_id | Int |  | 是 | 组合装主键 |
| 商家编码 | suite\_no | String | 80 | 是 | 组合装商家编码 |
| 组合装名称 | suite\_name | String | 255 | 是 | 组合装名称 |
| 重量 | weight | Decimal(19,4) |  | 是 | 重量 |
| 会员价 | member\_price | Decimal(19,4) |  | 是 | 会员价 |
| 备注 | remark | String | 255 | 否 | 备注 |
| 品牌id | brand\_id | Int | 11 | 是 | 品牌id |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 零售价 | retail\_price | Decimal(19,4) |  | 是 | 零售价 |
| 标记名称 | flag\_name | String | 32 | 是 | 标记名称 |
| 基本单位 | unit\_name | String | 20 | 是 | 基本单位 |
| 辅助单位 | aux\_unit\_name | String | 20 | 是 | 辅助单位 |
| 自定义属性1 | prop1 | String | 255 | 是 | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | 是 | 自定义属性2 |
| 自定义属性3 | prop3 | String | 255 | 是 | 自定义属性3 |
| 自定义属性4 | prop4 | String | 255 | 是 | 自定义属性4 |
| 自定义属性5 | prop5 | String | 255 | 是 | 自定义属性5 |
| 自定义属性6 | prop6 | String | 255 | 是 | 自定义属性6 |
| 批发价 | wholesale\_price | Decimal(19,4) |  | 是 | 批发价 |
| 市场价 | market\_price | Decimal(19,4) |  | 是 | 市场价 |
| 组合装简称 | short\_name | String | 255 | 是 | 组合装简称 |
| 货品标签 | goods\_label | String | 255 | 是 | 货品标签 |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 分类名称（类别） | class\_name | String | 100 | 是 | 分类名称 |
| 打印内容 | print\_suite\_mode | byte | 1 | 是 | 打印内容<br>0：组合装明细<br>1：组合装及明细<br>2：组合装 |
| 是否已删除 | deleted | Int | 11 | 是 | 大于0表示已删除，删除后自增生成的id值 |
| 组合装修改时间 | suite\_modified | String | 40 | 是 | 组合装修改时间 |
| 组合装创建时间 | suite\_created | String | 40 | 是 | 组合装创建时间 |
| 条码个数 | barcode\_count | Int | 11 | 是 | 条码个数 |
| 组合装明细 | detail\_list | List<Map<String,Object>> |  | 是 | 组合装明细 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 明细主键id | rec\_id | Int |  | 是 | 明细主键id |
| 组合装id | suite\_id | Int |  | 是 | 组合装主键 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 单品id | spec\_id | Int |  | 是 | 单品主键 |
| 基本单位id | unit | Int |  | 是 | 基本单位id |
| 删除id | deleted | Int |  | 是 | 删除后自增生成的id值 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 条码 | barcode | String | 50 | 是 | 条码 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品id | goods\_id | Int |  | 是 | 货品主键 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 固定售价 | fixed\_price | Decimal(19,4) |  | 是 | 固定售价/单价 |
| 金额占比 | ratio | Decimal(19,4) |  | 是 | 金额占比 |
| 固定价格 | is\_fixed\_price | boolean | 1 | 是 | 是否固定价格<br>true:是<br>false:否 |
| 组合装明细修改时间 | modified | String | 40 | 是 | 组合装明细修改时间 |
| 组合装明细创建时间 | created | String | 40 | 是 | 组合装明细创建时间 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Suite.search#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Suite.search#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Suite.search#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Suite.search#autoTab0_3)

```
[{\
"start_time": "2020-01-01 00:00:00",\
"end_time": "2020-01-20 00:00:00"\
}]
```

```
<?php
header("Content-Type: text/html; charset=UTF-8");
date_default_timezone_set("Asia/Shanghai");
require_once('wdtsdk.php');

$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret");

$parMap = new stdClass();
$parMap->start_time = "2020-01-01 00:00:00";
$parMap->end_time = "2020-01-20 00:00:00";

$pager = new Pager(1, 0, true);
$data = $client->pageCall("goods.Suite.search", $pager, $parMap);

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
| JSON | ```<br>{<br>	"status": 0,<br>	"data": {<br>		"total_count": 1,<br>		"suite_list": [{<br>			"suite_modified": "2023-03-10 13:42:56",<br>			"detail_list": [{<br>				"rec_id": 12773,<br>				"suite_id": 5757,<br>				"num": 1,<br>				"fixed_price": 0,<br>				"ratio": 0.5,<br>				"is_fixed_price": false,<br>				"modified": "2022-12-28 14:42:59",<br>				"created": "2022-12-28 14:42:59",<br>				"spec_no": "xiangyin01",<br>				"spec_name": "",<br>				"spec_code": "xiangyin01",<br>				"barcode": "xiaowanzi01",<br>				"unit": 2,<br>				"deleted": 0,<br>				"goods_no": "xiangyin",<br>				"goods_name": "相印",<br>				"spec_id": 361673,<br>				"goods_id": 167946<br>			}, {<br>				"rec_id": 12774,<br>				"suite_id": 5757,<br>				"num": 1,<br>				"fixed_price": 0,<br>				"ratio": 0.5,<br>				"is_fixed_price": false,<br>				"modified": "2022-12-28 14:42:59",<br>				"created": "2022-12-28 14:42:59",<br>				"spec_no": "xiangyin02",<br>				"spec_name": "",<br>				"spec_code": "",<br>				"barcode": "xiaowanzi02",<br>				"unit": 0,<br>				"deleted": 0,<br>				"goods_no": "xiangyin",<br>				"goods_name": "相印",<br>				"spec_id": 361674,<br>				"goods_id": 167946<br>			}],<br>			"suite_name": "相印",<br>			"member_price": 0,<br>			"remark": "",<br>			"aux_unit_name": "无",<br>			"retail_price": 0,<br>			"flag_name": "无",<br>			"wholesale_price": 0,<br>			"suite_id": 5757,<br>			"barcode": "xiangyin01+02",<br>			"class_name": "无",<br>			"suite_created": "2022-12-28 14:42:59",<br>			"barcode_count": 4,<br>			"weight": 0,<br>			"brand_name": "BM",<br>			"goods_label": "",<br>			"prop4": "",<br>			"brand_id": 2014,<br>			"prop3": "",<br>			"prop2": "",<br>			"unit_name": "无",<br>			"prop1": "",<br>			"deleted": 0,<br>			"suite_no": "xiangyin01+02",<br>			"market_price": 0,<br>			"short_name": "相印",<br>			"print_suite_mode": 0<br>		}]<br>	}<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "参数中必须包含起止时间"<br>}<br>``` |

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