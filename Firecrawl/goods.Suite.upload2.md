---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Suite.upload2"
title: "API文档"
---
**goods.Suite.upload2** **（组合装推送/更新）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：**推送组合装信息 |
| **1.2 适用版本：** 客户端V1.5.8.6版本以上 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：**组合装更新的时候，需要保证suite\_no不变，组合组信息，组合装明细行全量更新。并非只传更新的部分货品信息。（如原来明细是三个货品，更新时也需要完整传输三个货品的信息，如果只传两个货品，第三个货品会被删除）. 其他检验逻辑和客户端逻辑保持一致。 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段 |
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
| 组合装信息 | suite | Map<String,Object> |  | 是 | 组合装信息 |
| 组合装明细 | suite\_detail\_list | List<Map<String, Object>> |  | 是 | 组合装明细 |
| **suite** |  |  |  |  |  |
| 组合装名称 | suite\_name | String |  | Y | 组合装名称 |
| 组合装编号 | suite\_no | String |  | Y | 组合装编号 |
| 分类名称 | class\_name | String |  | N | 分类名称 |
| 品牌名称 | brand\_name | String |  | N | 品牌名称 |
| 基本单位名称 | unit\_name | String |  | N | 基本单位名称 |
| 辅助单位名称 | aux\_unit\_name | String |  | N | 辅助单位名称 |
| 简称 | short\_name | String |  | N | 简称 |
| 条码 | barcode | String |  | N | 条码 |
| 重量 | weight | Decimal(19,4) |  | N | 重量 |
| 货品自定义属性1 | prop1 | String |  | N | 货品自定义属性1 |
| 货品自定义属性2 | prop2 | String |  | N | 货品自定义属性2 |
| 货品自定义属性3 | prop3 | String |  | N | 货品自定义属性3 |
| 货品自定义属性4 | prop4 | String |  | N | 货品自定义属性4 |
| 货品自定义属性5 | prop5 | String |  | N | 货品自定义属性5 |
| 货品自定义属性6 | prop6 | String |  | N | 货品自定义属性6 |
| 零售价 | retail\_price | Decimal(19,4) |  | N | 零售价 |
| 批发价 | wholesale\_price | Decimal(19,4) |  | N | 批发价 |
| 会员价 | member\_price | Decimal(19,4) |  | N | 会员价 |
| 市场价 | market\_price | Decimal(19,4) |  | N | 市场价 |
| 备注 | remark | String |  | N | 备注 |
| 打印模式 | print\_suite\_mode | Byte |  | N | 0:组合装明细<br>1:组合装及明细 <br>2: 组合装 <br>默认0 |
| 货品标签 | goods\_label\_name | String |  | Y | 打印方式为明细时不允许设置标签<br>(1)当不设置标签时，需传入空字符串<br>(2)当传入客户端不存在的货品标签时，原货品标签会重置为空值 |
| 拆分属性 | large\_type | Byte |  | N | 0: 非大件 <br>1:普通大件 <br>2: 独立大件 <br>默认0 |
| **suite\_detail\_list** |  |  |  |  |  |
| 名称 | 字段 | 类型 | 长度 | 是否必须 | 描述 |
| 商家编码 | spec\_no | String |  | Y | 商家编码 |
| 是否固定价格 | is\_fixed\_price | Boolean |  | N | 默认false |
| 数量 | num | Decimal(19,4) |  | Y | 数量 |
| 固定价格 | fixed\_price | Decimal(19,4) |  | N | 仅is\_fixed\_price=true 有效. -1: 使用货品档案内单品零售价 |
| 金额占比 | ratio | Decimal(19,4) |  | N | -1: 按照明细金额自动计算比例 |

**响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 0表示正常，其他表示失败 |
| 组合装id | data | Int |  | 否 | 调用成功返回组合装id,调用失败则不返回该字段 |
| 返回信息 | message | String |  | 否 | 如果创建/修改成功message内容为空,否则为错误信息 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[{`<br>```"suite_no"``:``"20220421002"``,`<br>```"suite_name"``:``"20220421002"``,`<br>```"goods_label_name"``:``"222222"``,`<br>```"print_suite_mode"``: 2`<br>```},`<br>```[{`<br>```"num"``: 1,`<br>```"spec_no"``:``"dongfangshuye"`<br>```}, {`<br>```"num"``: 10,`<br>```"spec_no"``:``"xiaowanzi01"`<br>```}]`<br>`]` | |
| PHP | |     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>`$parMap``=``new``stdClass();`<br>`$parMap``->suite_name =``'20220421002'``;`<br>`$parMap``->suite_no =``'20220421002'``;`<br>`$parMap``->print_suite_mode= 2;`<br>`$parMap``->goods_label_name=``'222222'``;`<br>``<br>`$Detail``=``array`<br>`(`<br>```array``(``'spec_no'``=>``'dongfangshuye'``,`<br>```'num'``=> 1.0000,`<br>```),`<br>```array``(``'spec_no'``=>``'xiaowanzi01'``,`<br>```'num'``=> 10.0000,`<br>```));`<br>`$data``=``$client``->call(``"goods.Suite.upload2"``,``$parMap``,``$Detail``);`<br>`//var_dump($data);`<br>`$php_json``= json_encode(``$data``);`<br>`?>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `response: {`<br>`"status"``:0,`<br>`"data"``:274`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>`"status"``:100,`<br>`"message"``:``"商家编码:aaaaa 单品不存在"`<br>`}` | |
