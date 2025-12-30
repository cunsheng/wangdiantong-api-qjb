---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=finance.settle.Logistics.search"
title: "API文档"
---
**finance.settle.Logistics.search（电子面单号查询** **）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：接口描述: 查询省份信息 |
| **1.2 适用版本：** 客户端 V1.5.2.0及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为1小时 |
| **1.5注意事项：** |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、线下ERP、数据分析等系统的对接 |

**3.请求参数说明**

3.2 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式 [点击这里](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98#%E6%B5%8B%E8%AF%95/%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83%E5%8F%82%E6%95%B0%E4%BF%A1) |
| 盐 | salt | String |  | 是 | 由旺店通分配appsecret，是由两部分构成, 冒号前面的部分是secret, 冒号后面的部分是salt. 例如一个appsecret是testsecret:testsalt, 那么secret为testsecret, salt为testsalt. |
| 接口名称 | method | String |  | 是 | 调用的接口名称 |
| 版本号 | v | String |  | 是 | 1.0 |
| 秒级时间戳 | timestamp | Int |  | 是 | 秒级时间戳, 当前时间戳减去 2012-01-01 00:00:00(1325347200), 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | 签名 |
| 分页大小 | page\_size | Int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | Int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | Int |  | 否 | 是否计算查询结果的总条数， 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start\_time | String | 40 | Y | 最后修改时间 |
| 结束时间 | end\_time | String | 40 | Y | 最后修改时间 |
| 状态 | status | Short |  | N | 0:待分配<br>1:已分配<br>2:已完成<br>4:回收失败<br>5:待回收<br>6:已回收<br>8:手工作废 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回信息 | data | <Map<String, Object>> |  | 是 | 返回信息 |

**data**

响应参数说明示例值或者格式、具体含义、使用方法及注意事项

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | detail\_list | List<Map<String, Object>> |  | 是 | 数据节点 |
| 总条数 | total\_count | Int |  | 是 | 总条数 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 电子面单号唯一id | rec\_id | Int |  | Y | 电子面单号唯一id |
| 状态 | satus | Short |  | Y | 0:待分配<br>1:已分配<br>2:已完成<br>4:回收失败<br>5:待回收<br>6:已回收<br>8:手工作废 |
| 订单编号 | trade\_no | String |  | Y | 订单编号 |
| 电子面单类型 | ebill\_api | Byte |  | Y | 0:纸质面单<br>1:旺店通直接对接物流<br>2:云栈热敏<br>3:京东阿尔法<br>4:拼多多<br>5:区域零售<br>6:云集<br>11:唯品会<br>16:ascp电子面单<br>17:菜鸟集货<br>18:抖音电子面单<br>19:得物品牌直发<br>20:快手电子面单<br>21:美团电子面单<br>22:唯品会MP<br>23:商家仓自营配电子面单<br>24:鲸灵(好衣库)<br>25:腾讯荟聚电子面单<br>26:华为商城电子面单<br>27:小红书<br>28:微信视频号<br>29:有赞<br>30:爱库存 |
| 物流类型 | logistics\_type | Short |  | Y | 见物流代码表 |
| 物流单号 | logistics\_no | String |  | Y | 物流单号 |
| 创建时间 | created | String |  | Y | 创建时间 |
| 最后修改时间 | modified | String |  | Y | 最后修改时间 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | ```<br>[<br>    {<br>        "end_time": "2024-05-21 16:08:00",<br>        "start_time": "2024-05-21 16:05:00",<br>        "status": 5<br>    }<br>]<br>``` |
| PHP | ```<br><?php  <br>header("Content-Type: text/html; charset=UTF-8");  <br>date_default_timezone_set("Asia/Shanghai");  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")<br>  <br>$params = new stdClass();  <br>$params->start_time = '2024-05-21 16:05:00';  <br>$params->end_time = '2024-05-21 16:05:09';  <br>  <br>$pager = new Pager(1, 0, true);  <br>$data = $client->pageCall("finance.settle.Logistics.search", $pager, $params);<br>``` |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "data": {<br>        "detail_list": [<br>            {<br>                "created": "2024-05-21 16:04:51",<br>                "ebill_api": 1,<br>                "logistics_no": "SF7444483757120",<br>                "logistics_type": 8,<br>                "modified": "2024-05-21 16:07:00",<br>                "rec_id": 3567,<br>                "status": 5,<br>                "trade_no": "JY202405150034"<br>            }<br>        ],<br>        "total_count": 1<br>    },<br>    "status": 0<br>}<br>``` |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "message": "start_time 不能为空",<br>    "status": 100<br>}<br>``` |
