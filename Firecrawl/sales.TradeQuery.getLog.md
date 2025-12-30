---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=sales.TradeQuery.getLog"
title: "API文档"
---
**sales.TradeQuery.getLog（订单日志查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：按照订单编号查询订单日志 |
| **1.2 适用版本：** 客户端V1.4.7.9及以上版本 |
| **1.3 增量获取：** |
| **1.4 时间跨度：** |
| **1.5注意事项：** 不支持批量查询 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**财务系统、SAP、数据分析等系统的对接 |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | Y | 查询参数 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单编号 | trade\_no | String |  | y | 订单编号 |

4.响应参数

4.1 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | y | 状态码,0表示调用成功 |
| 错误信息 | message | String |  | y | 无错误信息不返回 |
| 响应正文信息 | data | Map<String, Object> |  | y | 响应正文信息 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 数据节点 | detail\_list | List<Map<String, Object>> |  | y | 数据节点 |

**detail\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 创建时间 | created | String |  | y | 创建时间，yyyy-MM-dd HH:mm:ss格式 |
| 员工昵称 | shortname | String |  | y | 员工昵称 |
| 操作类型 | type | Int |  | y | 操作类型<br>1: 下单或建单<br>2: 付款<br>3: 递交<br>6: 拦截出库<br>12: 修改仓库<br>16: 修改标记<br>20: 填写物流单号<br>21: 订单拆分<br>30: 驳回到客审<br>44: 进入财审<br>45: 订单审核<br>46: 财务审核<br>50: 历史订单导入<br>69: 修改包装<br>80: 客户打款<br>90: 修改打印状态<br>91: 打单<br>100: 验货<br>101: 打包<br>102: 称重<br>105: 发货<br>106: 包裹分拣<br>120: 取消拦截<br>123: 归档<br>124: 反归档<br>132: 撤销发货/拣货放回<br>133: 拣货<br>134: 登记检视员<br>135: 物流同步<br>140: 翱向发货单翱向建单时间<br>141:翱向发货单实际落库时间<br>142: 翱向发货单递交<br>143: 翱向补赠赠品<br>155: 热敏获取物流单号<br>160: 清除订单拦截<br>165: 销售出库签入<br>166: 销售出库签出<br>300: 推送/取消外部wms入/出库单<br>305: 回收物流单号<br>310: 打印小票日志<br>330: 档口锁定<br>340: 订单回告<br>345: 不记录绩效<br>350: 删除出库单货区<br>360: 重选出库单货区<br>365: 订单撤销出库发货<br>366: 解析主单客服备注到子单<br>1000: 无具体意义<br>1001: 更换货品<br>1002: 添加货品<br>1003: 删除货品<br>1004: 修改货品金额<br>1005: 修改收件人信息<br>1006: 修改物流<br>1007: 修改仓库<br>1008: 修改打印备注<br>1009: 修改客服备注<br>1010: 冻结订单<br>1011: 解冻订单<br>1012: 清除异常<br>1013: 退款/子订单退款<br>1014: 订单审核失败<br>1015: 未付款递交<br>1016: 下载原始单<br>1020: 递交后处理<br>1021: 重试物流<br>1022: 订单修改和新增标记<br>1031: 分单<br>1032: 取消分单<br>1041: 放行<br>1042: 退回<br>1051: 历史订单导入转完成<br>1060: 极速直发<br>1061: 生成出库单<br>1062: 原始单发货变更触发发货<br>1063: 原始单变更触发发货失败<br>1064:出库单状态变化<br>1065:货位分配失败<br>1066:订单归档失败<br>1099: 未付款转移<br>1100: 委外推单<br>1101: 获取面单 |

**5.请求示例**

|     |     |
| --- | --- |
| json | ```<br>[<br>    {<br>        "trade_no": "JY202308170028s"<br>    }<br>]<br>``` |
| PHP | ```<br><?php  <br>header("Content-Type: text/html; charset=UTF-8");  <br>date_default_timezone_set("Asia/Shanghai");  <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret")<br>  <br>$params = new stdClass();  <br>$parMap->trade_no = "JY202308170028s";<br>$data = $client->call("sales.TradeQuery.getLog", $params);<br>?><br>``` |
| JAVA |  |
| C# |  |

### **6.响应示例**

#### 6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "detail_list": [<br>        {<br>            "created": "2023-08-17 14:41:36",<br>            "shortname": "wds",<br>            "type": 105<br>        },<br>        {<br>            "created": "2023-08-17 14:40:58",<br>            "shortname": "wds",<br>            "type": 45<br>        },<br>        {<br>            "created": "2023-08-17 14:40:13",<br>            "shortname": "系统",<br>            "type": 3<br>        },<br>        {<br>            "created": "2023-08-17 14:39:32",<br>            "shortname": "系统",<br>            "type": 2<br>        },<br>        {<br>            "created": "2023-08-17 14:39:32",<br>            "shortname": "系统",<br>            "type": 1<br>        },<br>        {<br>            "created": "2023-08-17 14:39:32",<br>            "shortname": "系统",<br>            "type": 12<br>        },<br>        {<br>            "created": "2023-08-17 14:45:03",<br>            "shortname": "系统",<br>            "type": 0<br>        },<br>        {<br>            "created": "2023-08-17 14:42:00",<br>            "shortname": "系统",<br>            "type": 0<br>        },<br>        {<br>            "created": "2023-08-17 14:41:02",<br>            "shortname": "wds",<br>            "type": 61<br>        },<br>        {<br>            "created": "2023-08-17 14:40:51",<br>            "shortname": "wds",<br>            "type": 14<br>        },<br>        {<br>            "created": "2023-08-17 14:40:47",<br>            "shortname": "wds",<br>            "type": 6<br>        },<br>        {<br>            "created": "2023-08-17 14:40:39",<br>            "shortname": "wds",<br>            "type": 7<br>        },<br>        {<br>            "created": "2023-08-17 14:40:13",<br>            "shortname": "系统",<br>            "type": 0<br>        }<br>    ]<br>}<br>``` |

#### 6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "message": "订单不存在或无店铺权限",<br>    "status": 100<br>}<br>``` |
