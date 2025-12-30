---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.push"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

基础类

物流公司查询

供应商查询

仓库查询

店铺查询

供应商信息推送

店铺更新

员工查询

虚拟仓仓库查询

退换原因查询

地址查询-省

地址查询-市

地址查询-区

虚拟仓信息查询

当前位置： API文档 > 基础类

****setting.PurchaseProvider.push(供应商信息推送**）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送供应商档案资料给ERP |
| **1.2 适用版本：** 客户端 V1.5.9.8及以上版本 |
| **1.3 增量获取：** 不支持 |
| **1.4 时间跨度：** |
| **1.5注意事项：** 供应商创建和修改为一个接口，如果provider\_no已存在为修改，不存在为新增 |

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
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商 | provider | Map<String, Object> |  | y | 供应商 |

**provider**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编号 | provider\_no | String | 20 | y | 供应商编号 |
| 供应商名称 | provider\_name | String | 64 | y | 供应商名称 |
| 联系人 | contact | String | 64 | n | 联系人 |
| 固话 | telno | String | 20 | n | 固话 |
| 手机 | mobile | String | 20 | n | 手机 |
| 传真 | fax | String | 20 | n | 传真 |
| QQ | qq | String | 20 | n | QQ |
| 邮编 | zip | String | 20 | n | 邮编 |
| 旺旺 | wangwang | String | 64 | n | 旺旺 |
| 邮箱 | email | String | 64 | n | 邮箱 |
| 网址 | website | String | 128 | n | 网址 |
| 地址 | address | String | 128 | n | 地址 |
| 到货天数 | arrive\_cycle\_days | Int | 11 | n | 到货天数 |
| 备注 | remark | String | 256 | n | 备注 |
| 是否停用 | is\_disabled | Int | 1 | n | 是否停用  0:否 1:是 默认为0 |
| 银行卡号 | account\_bank\_no | String | 30 | n | 银行卡号 |
| 收款银行 | account\_bank | String | 30 | n | 收款银行 |
| 收款人 | collect\_name | String | 64 | n | 收款人 |
| 省份ID | province | Int | 11 | n | 省份ID， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 城市ID | city | Int | 11 | n | 城市ID， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 地区ID | district | Int | 11 | n | 地区ID， [点击查看城市代码表](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_ccdmb) |
| 供应商分组 | provider\_group | String |  | n | 供应商分组 |
| 跟进人 | shortname | String |  | n | 跟进人（传值为员工的员工昵称） |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 结果信息 | data | Map<String, Object> |  | y | 结果信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项（如隐私数据淘系平台不返回，其他平台正常返回）

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 0表示推送成功 |
| 结果信息 | message | String |  | 是 | 结果信息 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.push#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.push#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.push#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.push#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | `[{`<br>`"provider_no"``:``"lztest"``,`<br>`"provider_name"``:``"lztest"``,`<br>`"contact"``:``"lz"`<br>`}]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | `<php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$provider``=``new``stdClass();`<br>`$provider``->provider_no=``'lztest'``;`<br>`$provider``->provider_name=``'lztest'``;`<br>`$provider``->contact=``'lz'``;`<br>``<br>`$data``=``$client``->call(``"setting.PurchaseProvider.push"``,``$provider``);`<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.push#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | `{`<br>`"status"``: 0,`<br>`"data"``: {`<br>`"message"``:``"OK"``,`<br>`"status"``: 0`<br>`}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=setting.PurchaseProvider.push#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"供应商名称不能重复"`<br>`}` |

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