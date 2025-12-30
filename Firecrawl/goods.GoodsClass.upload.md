---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsClass.upload"
title: "API文档"
---
**goods.GoodsClass.upload（新建分类** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：新建分类 |
| **1.2 适用版本：** 客户端 V1.5.0.9及以上版本 |
| **1.3注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 描述 |
| --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式 [点击这里](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E6%B5%8B%E8%AF%95/%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83%E5%8F%82%E6%95%B0%E4%BF%A1) |
| 盐 | salt | String |  | 由旺店通分配appsecret，是由两部分构成, 冒号前面的部分是secret, 冒号后面的部分是salt. 例如一个appsecret是testsecret:testsalt, 那么secret为testsecret, salt为testsalt. |
| 接口名称 | method | String |  | 调用的接口名称 |
| 版本号 | v | String |  | 1.0 |
| 秒级时间戳 | timestamp | Int |  | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), <br>时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 签名 |
| 分页大小 | page\_size | Int |  | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 是否计算查询结果的总条数， 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 父分类名称 | parent\_class\_name | String | 64 | N | 默认情况下创建为一级分类 |
| 分类名称 | class\_name | String | 64 | Y | 分类名称 |
| 是否叶子节点 | is\_leaf | boolean |  | Y | true:不允许有子节点，创建为分类<br>false:允许有子节点，创建为分组 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应正文 | data | Map<String,object> |  | Y | 响应正文数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分类id | class\_id | int | 11 | Y | 分类id |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsClass.upload#autoTab0_0)
- [php](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsClass.upload#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsClass.upload#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsClass.upload#autoTab0_3)

|     |     |
| --- | --- |
|  | `[`<br>```{`<br>```"class_name"``:``"api-service-test"``,`<br>```"is_leaf"``:``false`<br>```}`<br>`]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`include``'wdtsdk.php'``;`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``)`<br>``<br>`$params``=``new``stdClass();`<br>`$params``->class_name =``"api-service-test2"``;`<br>`$params``->is_leaf = true;`<br>``<br>`$data``=``$client``->call(``"goods.GoodsClass.upload"``,``$params``);` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsClass.upload#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>```"data"``: {`<br>```"class_id"``: 744`<br>```},`<br>```"status"``: 0`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.GoodsClass.upload#autoTab2_0)

|     |     |
| --- | --- |
|  | `{`<br>```"message"``:``"is_leaf 不能为null"``,`<br>```"status"``: 100`<br>`}` |
