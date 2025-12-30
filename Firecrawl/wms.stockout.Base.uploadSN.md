---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockout.Base.uploadSN"
title: "API文档"
---
**wms.stockout.Base.uploadSN（出库SN明细推送** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 针对已经创建好的出库单推送关联的SN信息 |
| **1.2 适用版本：** 客户端 V1.4.7.5及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5 注意事项：当前仅支持生产出库、调拨出库、其他出库、采购退货出库  单据状态需要为 编辑中才能推送SN【权限校验】：仓库权限** |

**2.调用场景**

|     |
| --- |
| **2.1** **举例说明：**SAP、线下ERP、SRM、SCM等系统对接 |

**3.请求参数说明**

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
| 单据信息 | params | Map<String, Object> |  | Y | 单据信息 |
| 明细信息 | detailList | List<Map<String,Object>> |  | Y | 明细信息 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单号 | stockout\_no | String |  | Y | 出库单号 |
| 单据类型 | order\_type | byte |  | Y | 2：调拨出库<br>5：生产原料出库<br>14：采购退货出库<br>21：其他出库 |

**detailList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 是否残次品 | defect | boolean |  | N | 默认false |
| sn列表 | sn\_list | List<String> |  | Y | sn列表 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | Y | 返回0为正常 |
| 错误信息 | message | String |  | Y | 无错误信息不返回 |
| 响应信息 | data | Map<String, Object> |  | Y | 响应信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回信息 | message | String |  | Y | 此字段为方便后续响应内容调整所添加，不可以作为接口响应成功的标志 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | ```<br>[<br>    {<br>        "order_type": 2,<br>        "stockout_no": "CK202307260007"<br>    },<br>    [<br>        {<br>            "sn_list": [<br>                "0090x001"<br>            ],<br>            "spec_no": "009"<br>        },<br>        {<br>            "sn_list": [<br>                "SNTEST0x001",<br>                "SNTEST0x002"<br>            ],<br>            "spec_no": "SNTEST"<br>        }<br>    ]<br>]<br>``` |
| php 请求示例 | ```<br>< php  <br>header("Content-Type: text/html; charset=UTF-8");  <br>date_default_timezone_set("Asia/Shanghai");  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")<br>  <br>$orderInfo = new stdClass();<br>$orderInfo->stockout_no = 'CK202307260007';<br>$orderInfo->order_type = 2;<br>$detail1 = new stdClass();<br>$detail1->spec_no = '009';<br>$detail1->sn_list = array('0090x001');<br>$detail2 = new stdClass();<br>$detail2->spec_no = 'SNTEST';<br>$detail2->sn_list = array('SNTEST0x001', 'SNTEST0x002');<br>$detailList = array($detail1, $detail2);;  <br>  <br>$data = $client->call("wms.stockout.Base.uploadSN", $orderInfo, $detailList);<br>?><br>``` |
| JAVA |  |
| C# |  |

**6.响应示例**

6.1正常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "data": {<br>        "message": "OK"<br>    },<br>    "status": 0<br>}<br>``` |

6.2异常响应示例

|     |     |
| --- | --- |
| json | ```<br>{<br>    "message": "出库单号不可以为空",<br>    "status": 100<br>}<br>``` |
