---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=wms.stockin.SmartRefund.upload"
title: "API文档"
---

![](https://open.wangdian.cn/assets/open_res/icon_normal_profile.png?v=49b3bbcb)个人资料


![](https://open.wangdian.cn/assets/open_res/icon_normal_password.png?v=e9e3a6f7)修改密码


![](https://open.wangdian.cn/assets/open_res/icon_normal_exit.png?v=4b481af7)退出


[慧策开放平台-旗舰版](https://open.wangdian.cn/open)

[首页](https://open.wangdian.cn/qjb/open/welcome) [自助对接](https://open.wangdian.cn/qjb/open/abut) [API文档](https://open.wangdian.cn/qjb/open/apidoc) [文档中心](https://open.wangdian.cn/qjb/open/guide?path=qjbguide_kfzn) [支持中心](https://open.wangdian.cn/qjb/open/support?path=%E6%89%80%E6%9C%89%E9%97%AE%E9%A2%98) [平台公告](https://open.wangdian.cn/qjb/open/notice?path=%E6%89%80%E6%9C%89%E5%85%AC%E5%91%8A)

登录 [注册](https://open.wangdian.cn/qjb/open/user/register)

所有接口

售后类

退货入库单查询

原始退款单推送

创建退货预入库

退换单查询

预入库单据查询

退货预入库单取消

历史退换单查询

原始退款单查询

原始退款单推送2

退货入库单推送

快速退货

历史退货入库单查询

历史原始退款单查询

退货物流包裹查询

当前位置： API文档 > 售后类

**wms.stockin.SmartRefund.upload（快速退货）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描** **述**：推送快速退货单据信息给ERP |
| **1.2 适用版本：** 客户端 V1.4.3.9及以上版本 |
| **1.3 注意事项：【权限校验】：仓库权限** |
| **1.4 常见场景：**<br>**1.4.1客户端中已有退换单：**当订单发货的情况下，通过变更原始单的状态 系统生成了对应的退换单（待审核，已审核状态），此时调用快速退货接口，推送的快速退货单据可以关联到退换管理页面的退换单，状态更新为已审核，入库状态更新为部分入库、全部入库<br>**1.4.2客户端中没有退换单：**通过接口推送快速退货单会在退换管理页面生成一条对应的退换单 |

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

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退货信息 | refundInfo | Map<String, Object> |  | 是 | 退货信息 |
| 退货货品详细信息 | detailMapList | List<Map<String, Object>> |  | 是 | 退货货品详细信息 |
| 是否允许退货货品数量大于购买数量 | createPreStockin | boolean | 1 | 是 | 是否允许退货货品数量大于购买数量 |

**refundInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始单号 | tid | String | 40 | 是 | 原始单号 |
| 退货入库仓编号 | return\_warehouse\_no | String | 40 | 是 | 退货入库仓编号（不支持外部仓库） |
| 退货备注 | remark | String | 255 | 是 | 退货备注,无备注可以传空字符串 |

**detailMapList**

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 入库数量 | stockin\_num | Decimal |  | 是 | 入库数量 |
| 备注 | remark | String | 255 | 是 | 备注,无备注可以传空字符串 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 返回0为正常 |
| 返回信息 | message | String |  | 是 | 无错误信息不返回 |
| 返回值 | data | Map<String,Object> |  | 是 | 返回值 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单id | stockin\_id | Int |  | 是 | 入库单id |
| 类型 | type | byte |  | 是 | 12：退货入库 |

**5.请求示例**

|     |     |
| --- | --- |
| Json格式请求报文 | ```<br>[{<br>"tid": "pos-6776312",<br>"return_warehouse_no": "pos",<br>"remark": "pos refundInfo remark"<br>},<br>[{<br>"spec_no": "RRWDMS018040S",<br>"stockin_num": 1,<br>"remark": "POS 退货测试"<br>}], false<br>]<br>``` |
| PHP | ```<br><?php<br>header("Content-Type: text/html; charset=UTF-8");<br>require_once('wdtsdk.php');<br> <br>$client = new WdtErpClient("url", "wdtapi3", "appkey", "secret"); <br>$refundInfo = array(<br>'tid' => 'pos-6776312',<br>//'return_logistics_no' => 'apopopopopopopopopopu',// 必须传入,并且必须有值<br>//'return_logistics_name' => '',// 可以为空<br>'return_warehouse_no' => 'pos',<br>'remark' => 'pos refundInfo remark',<br>);<br> <br>$detailMap1 = array(<br>'spec_no' => 'RRWDMS018040S',// 'spec_id' => 18113, test_001<br>//'defect' => false,<br>//'refund_num' => 1,<br>'stockin_num' => 1,<br>'remark' => 'POS 退货测试' // 详情的退货备注<br>);<br> <br>$detailMapList = array();<br>array_push($detailMapList,  $detailMap1);<br> <br>$createPreStockin = false;<br>$data = $client->call("wms.stockin.SmartRefund.upload",$refundInfo, $detailMapList, $createPreStockin);<br>echo json_encode($data, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);<br>?><br>``` |
| JAVA |  |
| C# |  |

### **6.响应示例**

### 6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>    "status": 0,<br>    "data":<br>    {<br>        "stockin_id": 1,<br>        "type": 12<br>    }<br>}<br>``` |

#### 6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | ```<br>{<br>"status": 100,<br>"message": "未找到对应的单据信息!"<br>}<br>``` |

常用工具

[SDK下载](https://open.wangdian.cn/open/guide?path=guide_sdk_qjb)

常用工具

北京掌上先机网络科技有限公司 版权所有 京ICP备13053703号-1