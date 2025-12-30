---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.upload"
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

****process.Bom.upload**（物料清单推送）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 推送物料清单给ERP |
| **1.2 适用版本：** 客户端 V1.3.3.1及以上版本 |
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
| 物料清单数据 | param | Map<String,Object> |  | 是 | 物料清单数据 |

**param**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物料清单名称 | bom\_name | String |  | 是 | 物料清单名称 |
| 生产费用 | fee | Decimal(19,4) |  | 否 | 生产费用 |
| 备注 | remark | String |  | 否 | 备注 |
| 货品列表 | detail\_list | List<Map<String,Object>> |  | 是 | 货品列表 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String |  | 是 | 商家编码 |
| 数量 | num | Decimal(19,4) |  | 是 | 数量 |
| 是否成品 | is\_product | bool |  | 否 | 默认false |
| 备注 | remark | String |  | 否 | 备注 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | Map<String,Object> |  | 否 | 返回信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态 | status | Int |  | 是 | 响应成功则返回0 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.upload#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.upload#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.upload#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.upload#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | `[{`<br>```"detail_list"``: [{`<br>```"is_product"``:``true``,`<br>```"num"``: 1,`<br>```"spec_no"``:``"aaaaa"`<br>```}, {`<br>```"is_product"``:``false``,`<br>```"num"``: 10,`<br>```"spec_no"``:``"xiaowanzi01"`<br>```}],`<br>```"fee"``:``""``,`<br>```"remark"``:``"1"``,`<br>```"bom_name"``:``"Test"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23 | `<?php`<br>`header(``"Content-Type: text/html;   charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once(``'wdtsdk.php'``);`<br>`$client = new   WdtErpClient($service_url, $sid, $appkey, $appsecret);`<br>`$param = new stdClass();`<br>`$param->bom_name=``"Test"``;``//物料清单名称`<br>`$param->fee=``""``;``//生产费用`<br>`$param->remark=``"1"``;``//备注信息`<br>`$DetailList = array`<br>`(`<br>```array(``'spec_no'``=>``'aaaa'``,``'num'``=> 1.0000,``'is_product'``=>``true``),`<br>```array(``'spec_no'``=>``'xiaowanzi01'``,``'num'``=> 10.0000,``'is_product'``=>``false``));`<br>`$param->detail_list = $DetailList;`<br>``<br>`$response = $client->call(``"process.Bom.upload"``,$param);`<br>`$php_json = json_encode($response);`<br>`echo $php_json;`<br>``<br>`?>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.upload#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"status"``: 0`<br>```}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=process.Bom.upload#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 100,`<br>```"message"``:``"已经存在同名物料单！"`<br>`}` |

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