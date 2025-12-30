---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.search"
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

**process.Bom.search** **（物料清单）**

[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")**¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP物料清单数据 |
| **1.2 适用版本：** 客户端V1.4.3.4及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time与end\_time起止时间跨度不超过30天 |
| **1.5 注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

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
| 开始时间 | start\_time | String | 40 | N | 物料清单最后修改时间 |
| 结束时间 | end\_time | String | 40 | N | 物料清单最后修改时间 |
| 物料清单编号 | bom\_no | String |  | N | 物料清单编号为空时，时间条件必填 |
| 是否展示已停用清单 | show\_disabled | boolean | 1 | N | 是：true<br>否：false<br>默认false |

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
| 单据数据 | data | Map<String, Object> |  | Y | 单据相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总数 | total\_count | Int | 11 | Y | 查询条件总单据数 |
| 数据节点 | order\_list | Map<String, Object> |  | Y | 数据节点 |

**order\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物料清单唯一键 | bom\_id | Int | 11 | Y | 物料清单唯一键 |
| 物料清单编号 | bom\_no | String | 64 | Y | 物料清单编号 |
| 物料清单名称 | bom\_name | String | 255 | Y | 物料清单名称 |
| 操作人 | operator\_name | String | 50 | Y | 操作人 |
| 操作人id | operator\_id | Int | 11 | Y | 操作人id |
| 生产费用 | fee | Decimal(19,4) |  | Y | 生产费用 |
| 备注 | remark | String | 1024 | Y | 备注 |
| 是否停用 | is\_disabled | boolean | 1 | Y | 是否停用<br>是：true<br>否：false |
| 创建时间 | created | String |  | Y | 创建时间<br>格式: yyyy-MM-dd HH:mm:ss |
| 最后修改时间 | modified | String |  | Y | 最后修改时间<br>格式: yyyy-MM-dd HH:mm:ss |
| 成品列表 | product\_list | List<Map<String,Object>> |  | Y | 成品列表 |
| 原料列表 | material\_list | List<Map<String,Object>> |  | Y | 原料列表 |

**product\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物料清单唯一键 | bom\_id | Int | 11 | Y | 物料清单唯一键 |
| 物料清单明细唯一键 | bom\_detail\_id | Int | 11 | Y | 物料清单明细唯一键 |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 是否为主物料清单 | is\_master | boolean | 1 | Y | 是否主物料清单<br>是：true<br>否：false |
| 是否成品 | is\_product | boolean | 1 | Y | 是否成品<br>是：true<br>否：false |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格编码 | spec\_code | String | 40 | Y | 规格编码 |
| 条码 | barcode | String | 50 | Y | 条码 |
| sn类型 | sn\_type | byte |  | Y | 0：未启用<br>1：强sn<br>2：弱sn |
| 零售价 | retail\_price | Decimal(19,4) |  | Y | 单品零售价 |
| 成本价 | cost | Decimal(19,4) |  | Y | 成本价 |
| 总成本 | all\_cost | Decimal(19,4) |  | Y | 总成本 |
| 备注 | remark | String | 255 | Y | 备注 |

**material\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物料清单唯一键 | bom\_id | Int | 11 | Y | 物料清单唯一键 |
| 物料清单明细唯一键 | bom\_detail\_id | Int | 11 | Y | 物料清单明细唯一键 |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 是否为主物料清单 | is\_master | boolean | 1 | Y | 是否主物料清单<br>是：true<br>否：false |
| 是否成品 | is\_product | boolean | 1 | Y | 是否成品<br>是：true<br>否：false |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格名称 | spec\_name | String | 100 | Y | 规格名称 |
| 规格编码 | spec\_code | String | 40 | Y | 规格编码 |
| 条码 | barcode | String | 50 | Y | 条码 |
| sn类型 | sn\_type | byte |  | Y | 0：未启用<br>1：强sn<br>2：弱sn |
| 零售价 | retail\_price | Decimal(19,4) |  | Y | 单品零售价 |
| 成本价 | cost | Decimal(19,4) |  | Y | 成本价 |
| 总成本 | all\_cost | Decimal(19,4) |  | Y | 总成本 |
| 备注 | remark | String | 255 | Y | 备注 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | ```<br>[<br>    {<br>        "start_time": "2022-12-01 00:00:00",<br>        "end_time": "2022-12-24 00:00:00"<br>    }<br>]<br>``` |
| php 请求示例 | ```<br><?php<br>header("Content-Type: text/html; charset=UTF-8");  <br>date_default_timezone_set("Asia/Shanghai");  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")<br>  <br>$parMap = new stdClass();<br>$parMap->start_time = "2022-12-01 00:00:00";<br>$parMap->end_time = "2022-12-24 00:00:00";<br>$pager = new Pager(50, 0, true);<br>$data = $client->pageCall("process.Bom.search", $pager, $parMap);<br>  <br>?><br>``` |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 0,<br>    "data":<br>    {<br>        "total_count": 1,<br>        "order_list":<br>        [<br>            {<br>                "bom_id": 86,<br>                "operator_name": "张卓",<br>                "operator_id": 158,<br>                "created": "2022-12-13 14:41:18",<br>                "fee": 5.0000,<br>                "is_disabled": false,<br>                "material_list":<br>                [<br>                    {<br>                        "bom_detail_id": 1475,<br>                        "bom_id": 86,<br>                        "num": 1.0000,<br>                        "is_product": false,<br>                        "is_master": false,<br>                        "remark": "",<br>                        "goods_no": "zz03",<br>                        "goods_name": "潮系男士短袖",<br>                        "spec_no": "zz0302",<br>                        "spec_name": "黑色S码",<br>                        "spec_code": "02",<br>                        "barcode": "zz0302",<br>                        "sn_type": 0,<br>                        "retail_price": 50.0000,<br>                        "cost": 0.0000,<br>                        "all_cost": 0.0000<br>                    },<br>                    {<br>                        "bom_detail_id": 1476,<br>                        "bom_id": 86,<br>                        "num": 1.0000,<br>                        "is_product": false,<br>                        "is_master": false,<br>                        "remark": "",<br>                        "goods_no": "zz02",<br>                        "goods_name": "潮洗男生夏凉裤",<br>                        "spec_no": "zz0202",<br>                        "spec_name": "黑色S码",<br>                        "spec_code": "02",<br>                        "barcode": "zz0202",<br>                        "sn_type": 0,<br>                        "retail_price": 60.0000,<br>                        "cost": 0.0000,<br>                        "all_cost": 0.0000<br>                    }<br>                ],<br>                "modified": "2022-12-13 14:41:18",<br>                "bom_no": "GP202212130001",<br>                "remark": "",<br>                "product_list":<br>                [<br>                    {<br>                        "bom_detail_id": 1477,<br>                        "bom_id": 86,<br>                        "num": 1.0000,<br>                        "is_product": true,<br>                        "is_master": false,<br>                        "remark": "",<br>                        "goods_no": "090909",<br>                        "goods_name": "阿拉蕾 新品黄色",<br>                        "spec_no": "090909",<br>                        "spec_name": "黄色",<br>                        "spec_code": "",<br>                        "barcode": "",<br>                        "sn_type": 0,<br>                        "retail_price": 1.0000,<br>                        "cost": 0.0000,<br>                        "all_cost": 0.0000<br>                    }<br>                ],<br>                "bom_name": "潮服一套"<br>            }<br>        ]<br>    }<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "status": 100,<br>    "message": "开始时间与结束时间间隔最大30天"<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1