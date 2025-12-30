---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Category.search"
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

**goods.Category.search** **（平台类目查询）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP平台类目数据 |
| **1.2 适用版本：** 客户端 V1.4.2.6及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** 起止时间跨度不超过30天 |
| **1.5注意事项：【权限校验】：店铺权限**<br>1.为了达到保护用户隐私数据安全的目的，本接口不返回淘系及系统供销平台货品数据，相关平台规则[点击这里](https://open.taobao.com/announcement.htm?docId=25247&docType=12 "单击查看文档详情")，淘系及系统供销平台数据获取办法[点击这里](https://open.wangdian.cn/qjb/open/guide?path=qjb_guide_qm_customize "淘系订单获取说明")。<br>2.本接口不返回类目下的平台货品信息，需要到[平台货品](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.ApiGoods.search) 查询接口进行类目关联 |

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
| 分页 | pager | pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺编号 | shop\_no | String | 20 | 否 | 店铺编号 |
| 开始时间 | start\_time | String | 40 | 是 | 开始时间（最后修改时间） |
| 结束时间 | end\_time | String | 40 | 是 | 结束时间（最后修改时间） |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 货品分类数据 | data | Map<String, Object> |  | 是 | 货品分类数据 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品类目数据信息 | category\_list | List<Map<String, Object>> |  | 是 | 货品类目数据信息 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**category\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一键 | rec\_id | Int | 11 | 是 | 唯一键 |
| 平台id | platform\_id | Int | 11 | 是 | 平台id，点击 [链接查看](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ptdmbb) 平台代码表 |
| 店铺id | shop\_id | Int | 11 | 是 | 店铺id |
| 店铺编号 | shop\_no | String | 20 | 是 | 店铺编号 |
| 佣金系数 | commission\_factor | Decimal(19,4) |  | 是 | 佣金系数 |
| 状态 | status | Int | 1 | 是 | 状态<br>0：正常<br>1：类目已删除<br>2：无效类目 |
| 类目id | cid | String | 40 | 是 | 类目id |
| 父级分类id | parent\_id | String | 40 | 是 | 父级分类id |
| 是否根节点 | is\_leaf | Int | 1 | 是 | 是否根节点 |
| 类目名称 | category\_name | String | 64 | 是 | 类目名称 |
| 记录了从根元素到当前元素的ID，以逗号分隔 | path | String | 1024 | 是 | 记录了从根元素到当前元素的ID，以逗号分隔 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | ```<br>[{"start_time":"2022-10-01 00:00:00","end_time":"2022-10-10 00:00:00"}]<br>``` |
| PHP | ```<br><?php<br>header("Content-Type: text/html; charset=UTF-8");<br>date_default_timezone_set("Asia/Shanghai");<br>require_once('wdtsdk.php');<br>  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret"); <br>$parMap = new stdClass();<br>$parMap->start_time = "2022-10-01 00:00:00";<br>$parMap->end_time = "2022-10-10 00:00:00";<br>$parMap->shop_no="test";<br>$pager = new Pager(10, 0, true);<br>$data = $client->pageCall("goods.Category.search", $pager, $parMap);<br>?><br>``` |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "data": {<br>        "category_list": [{<br>            "commission_factor": 0.0000,<br>            "shop_id": 28,<br>            "path": "0,30,50010158,",<br>            "category_name": "夹克",<br>            "parent_id": "30",<br>            "platform_id": 3,<br>            "is_leaf": 1,<br>            "rec_id": 532,<br>            "cid": "50010158",<br>            "status": 0,<br>            "shop_no": "zlc_test"<br>        }],<br>        "total_count": 19<br>    }<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 100,<br>    "message": "您的查询时间过宽,查询时间不能大于30天"<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1