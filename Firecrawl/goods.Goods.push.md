---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.push"
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

****goods.Goods.push**（货品推送）**

**[查看收费规则](https://open.wangdian.cn/open/guide?path=guide_fwfgz "查看收费规则")****¥标准**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** ①推送货品资料给ERP ②更新ERP货品档案资料 |
| **1.2 适用版本：** 客户端 V1.5.7.2及以上版本 |
| **1.3注意事项：**<br>（1）该接口是pushGoods的替代接口. 接口以goods\_no和spec\_no来匹配货品和单品, 所以如果接口传入已经存在的goods\_no或spec\_no的时候对应的操作是修改操作。<br>（2）spu维度一次只能推一条，一个货品可以推送多条明细 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

**3.请求参数说明** 3.1 请求地址

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
| 货品信息 | goodsInfo | Map<String,Object> |  | 是 | 货品信息 |
| 单品信息列表 | specInfoList | List<Map<String, Object>> |  | 是 | 规格信息列表 |

**goodsInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称’ |
| 分类名称 | class\_name | String | 64 | N | 分类名称,不传或为空则默认为’无’ |
| 品牌名称 | brand\_name | String | 64 | N | 品牌名称, 不传或为空则默认为’无’ |
| 基本单位名称 | unit\_name | String | 20 | N | 基本单位名称, 不传或为空则默认为’无’ |
| 辅助单位名称 | aux\_unit\_name | String | 20 | N | 辅助单位名称, 不传或为空则默认为’无’ |
| 标记名称 | flag\_name | String | 32 | N | 货品标记名称, 不传或为空则默认为’无’ |
| 货品类别 | goods\_type | Int | 4 | N | 默认0, <br>0：其它<br>1：销售货品<br>2：原材料<br>3：包装物<br>4：周转材料<br>5：虚拟商品<br>6：固定资产<br>8：分装箱<br>9：周期送货品<br>10：赠品 |
| 货品简称 | short\_name | String | 255 | N | 货品简称 |
| 货品别名 | alias | String | 255 | N | 货品别名 |
| 产地 | origin | String | 64 | N | 产地 |
| 备注 | remark | String | 512 | N | 货品备注 |
| 货品自定义属性1 | prop1 | String | 255 | N | 货品自定义属性1 |
| 货品自定义属性2 | prop2 | String | 255 | N | 货品自定义属性2 |
| 货品自定义属性3 | prop3 | String | 255 | N | 货品自定义属性3 |
| 货品自定义属性4 | prop4 | String | 255 | N | 货品自定义属性4 |
| 货品自定义属性5 | prop5 | String | 255 | N | 货品自定义属性5 |
| 货品自定义属性6 | prop6 | String | 255 | N | 货品自定义属性6 |
| 是否自动创建品牌和分类 | auto\_create\_bc | bool | 1 | N | 如果品牌,分类不存在,是否自动创建.不填默认为false |

**specInfoList**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | Y | 商家编码 |
| 规格码 | spec\_code | String | 40 | N | 规格码 |
| 条码 | barcode | String | 50 | N | 条码 |
| 规格名称 | spec\_name | String | 100 | N | 规格名称 |
| 仓库流程 | wms\_process\_mask | Int | 4 | N | 默认0 （需要的仓库流程相加）<br>2、无需验货 8、需要质检 16、无需拣货<br>32、无需唯一码<br>64、无需自动打印吊牌 |
| 货品标签 | goods\_label | String | 11 | N | 默认无,可选值:自定义货品标签的名称(参考属性名称编辑页面->货品标签)多个标签使用英文逗号拼接 |
| 启用序列号 | sn\_type | Int | 4 | N | 默认0,0不启用序列号 1强序列号 2弱序列号 |
| 最低价 | lowest\_price | Decimal(19,4) |  | N | 最低价 |
| 零售价 | retail\_price | Decimal(19,4) |  | N | 零售价 |
| 批发价 | wholesale\_price | Decimal(19,4) |  | N | 批发价 |
| 会员价 | member\_price | Decimal(19,4) |  | N | 会员价 |
| 市场价 | market\_price | Decimal(19,4) |  | N | 市场价 |
| 有效期天数 | validity\_days | Int | 6 | N | 有效期天数 |
| 最佳销售天数 | sales\_days | Int | 11 | N | 最佳销售天数 |
| 最佳收货天数 | receive\_days | Int | 11 | N | 最佳收货天数 |
| 重量 | weight | Decimal(19,4) |  | N | 重量 |
| 高 | height | Decimal(19,4) |  | N | 高 |
| 长 | length | Decimal(19,4) |  | N | 长 |
| 宽 | width | Decimal(19,4) |  | N | 宽 |
| 拆分 | large\_type | Int | 4 | N | 默认0, 0非大件1普通大件2独立大件（不可和小件一起发) 3按箱规拆分 -1非单发件 |
| 单品自定义属性1 | prop1 | String | 255 | N | 单品自定义属性1 |
| 单品自定义属性2 | prop2 | String | 255 | N | 单品自定义属性2 |
| 单品自定义属性3 | prop3 | String | 255 | N | 单品自定义属性3 |
| 单品自定义属性4 | prop4 | String | 255 | N | 单品自定义属性4 |
| 单品自定义属性5 | prop5 | String | 255 | N | 单品自定义属性5 |
| 单品自定义属性6 | prop6 | String | 255 | N | 单品自定义属性6 |
| 自定义价格1 | custom\_price1 | Decimal(19,4) |  | N | 自定义价格1 |
| 自定义价格2 | custom\_price2 | Decimal(19,4) |  | N | 自定义价格2 |
| 允许低于成本 | is\_lower\_cost | boolean | 1 | N | 默认0,0:不允许,1 允许 |
| 图片链接 | img\_url | String | 1024 | N | 图片链接 |
| 单品备注 | remark | String | 512 | N | 单品备注 |
| 销售积分 | sale\_score | Decimal(19,4) |  | N | 销售积分 |
| 打包积分 | pack\_score | Decimal(19,4) |  | N | 打包积分 |
| 拣货积分 | pick\_score | Decimal(19,4) |  | N | 拣货积分 |
| 分拣积分 | sort\_score | Decimal(19,4) |  | N | 分拣积分 |
| 扫描积分 | scan\_score | Decimal(19,4) |  | N | 扫描积分 |
| 补货积分 | supply\_score | Decimal(19,4) |  | N | 补货积分 |
| 上架积分 | shelve\_score | Decimal(19,4) |  | N | 上架积分 |
| 入库积分 | stockin\_score | Decimal(19,4) |  | N | 入库积分 |
| 质检积分 | inspect\_score | Decimal(19,4) |  | N | 质检积分 |
| 分装积分 | packing\_score | Decimal(19,4) |  | N | 分装积分 |
| 操作积分 | operate\_score | Decimal(19,4) |  | N | 操作积分 |
| 称重积分 | weigh\_score | Decimal(19,4) |  | N | 称重积分 |
| 发货积分 | consign\_score | Decimal(19,4) |  | N | 发货积分 |
| 税务编码 | tax\_code | String | 40 | N | 税务编码 |
| 基本单位名称 | unit\_name | String | 20 | N | 基本单位名称 |
| 辅助单位名称 | aux\_unit\_name | String | 20 | N | 辅助单位名称 |
| 保质期计算方式 | validity\_type | Int | 4 | N | 保质期计算方式<br>0：按天<br>1：按月<br>默认0 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 0表示成功推送。 |
| 货品id | data | Int |  | 否 | 调用成功返回货品id,调用失败不返回该字段 |
| 返回信息 | message | String |  | 否 | 如果创建/修改成功message内容为空,否则为错误信息 |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.push#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.push#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.push#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.push#autoTab0_3)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67 | `[{`<br>`"goods_no"``:``"testGoodsQ03-26 00:51:10_0"``,`<br>`"goods_name"``:``"testGoodsNameQ03-26 00:51:10_0"``,`<br>`"short_name"``:``"shortName"``,`<br>`"auto_create_bc"``:``true``,`<br>`"class_name"``:``"新建分类3"``,`<br>`"brand_name"``:``"新建品牌3"``,`<br>`"unit_name"``:``"个"``,`<br>`"aux_unit_name"``:``"件"``,`<br>`"goods_type"``: 1,`<br>`"alias"``:``"alias"``,`<br>`"pinyin"``:``"ceshi"``,`<br>`"origin"``:``"内蒙古呼和浩特市"``,`<br>`"remark"``:``"货品备注"``,`<br>`"prop1"``:``"P1"``,`<br>`"prop2"``:``"P2"``,`<br>`"prop3"``:``"P13"``,`<br>`"prop4"``:``"P14"``,`<br>`"prop5"``:``"P15"``,`<br>`"prop6"``:``"P16"``,`<br>`"flag_name"``:``"g_f"`<br>`},`<br>`[{`<br>`"spec_no"``:``"spec_noQ03-26 00:51:10_0_0"``,`<br>`"spec_name"``:``"spec_nameQ03-26 00:51:10_0_0"``,`<br>`"spec_code"``:``"spec_code"``,`<br>`"barcode"``:``"spec_noQ03-26 00:51:10_0_0"``,`<br>`"pack_score"``: 12,`<br>`"lowest_price"``: 200,`<br>`"unit_name"``:``"个"``,`<br>`"aux_unit_name"``:``"10个"``,`<br>`"remark"``:``"单品备注"``,`<br>`"goods_label"``:``"6"`<br>`}, {`<br>`"spec_no"``:``"spec_noQ03-26 00:51:10_0_1"``,`<br>`"spec_name"``:``"spec_nameQ03-26 00:51:10_0_1"``,`<br>`"spec_code"``:``"spec_code"``,`<br>`"barcode"``:``"spec_noQ03-26 00:51:10_0_1"``,`<br>`"pack_score"``: 12,`<br>`"lowest_price"``: 200,`<br>`"unit_name"``:``"个"``,`<br>`"aux_unit_name"``:``"10个"``,`<br>`"remark"``:``"单品备注"``,`<br>`"goods_label"``:``"6"`<br>`}, {`<br>`"spec_no"``:``"spec_noQ03-26 00:51:10_0_2"``,`<br>`"spec_name"``:``"spec_nameQ03-26 00:51:10_0_2"``,`<br>`"spec_code"``:``"spec_code"``,`<br>`"barcode"``:``"spec_noQ03-26 00:51:10_0_2"``,`<br>`"pack_score"``: 12,`<br>`"lowest_price"``: 200,`<br>`"unit_name"``:``"个"``,`<br>`"aux_unit_name"``:``"10个"``,`<br>`"remark"``:``"单品备注"``,`<br>`"goods_label"``:``"6"`<br>`}, {`<br>`"spec_no"``:``"spec_noQ03-26 00:51:10_0_3"``,`<br>`"spec_name"``:``"spec_nameQ03-26 00:51:10_0_3"``,`<br>`"spec_code"``:``"spec_code"``,`<br>`"barcode"``:``"spec_noQ03-26 00:51:10_0_3"``,`<br>`"pack_score"``: 12,`<br>`"lowest_price"``: 200,`<br>`"unit_name"``:``"个"``,`<br>`"aux_unit_name"``:``"10个"``,`<br>`"remark"``:``"单品备注"``,`<br>`"goods_label"``:``"6"`<br>`}]]` |

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60 | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$goodListNum``= 2;`<br>`$specListNum``= 4;`<br>`$editValue``=``"Q"``;`<br>``<br>`$goodsList``=``array``();`<br>``<br>`//for ($i = 0; $i < $goodListNum; $i++) {`<br>`$i``= 0;`<br>`$goods``=``new``stdClass();`<br>`$goodsSuffix``=``$editValue``.``$dateStr``.``"_"``.``$i``;`<br>`$goods``->goods_no =``"testGoods"``.``$goodsSuffix``;`<br>`$goods``->goods_name =``"testGoodsName"``.``$goodsSuffix``;`<br>`$goods``->short_name =``"shortName"``;`<br>`$goods``->auto_create_bc = true;`<br>`$goods``->class_name =``"新建分类3"``;`<br>`$goods``->brand_name =``"新建品牌3"``;`<br>`$goods``->unit_name =``"个"``;`<br>`$goods``->aux_unit_name =``"件"``;`<br>`//$goods->cycle_name = "无";`<br>`$goods``->goods_type = 1;`<br>``<br>`$goods``->alias =``"alias"``;`<br>`$goods``->pinyin =``"ceshi"``;`<br>`$goods``->origin =``"内蒙古呼和浩特市"``;`<br>`$goods``->remark =``"货品备注"``;`<br>`$goods``->prop1 =``"P1"``;`<br>`$goods``->prop2 =``"P2"``;`<br>`$goods``->prop3 =``"P13"``;`<br>`$goods``->prop4 =``"P14"``;`<br>`$goods``->prop5 =``"P15"``;`<br>`$goods``->prop6 =``"P16"``;`<br>`$goods``->flag_name =``'g_f'``;`<br>``<br>`$specList``=``array``();`<br>`for``(``$y``= 0;``$y``<``$specListNum``;``$y``++) {`<br>`$specSuffix``=``$goodsSuffix``.``"_"``.``$y``;`<br>```$spec``=``new``stdClass();`<br>`$spec``->spec_no =``'spec_no'``.``$specSuffix``;`<br>`$spec``->spec_name =``'spec_name'``.``$specSuffix``;`<br>`$spec``->spec_code =``'spec_code'``;`<br>`$spec``->barcode =``$spec``->spec_no;`<br>`$spec``->pack_score = 12.0000;`<br>`$spec``->lowest_price = 200.0000;`<br>`$spec``->unit_name =``'个'``;`<br>`$spec``->aux_unit_name =``'10个'``;`<br>`$spec``->remark =``'单品备注'``;`<br>`$spec``->goods_label = 6;`<br>`array_push``(``$specList``,``$spec``);`<br>`}`<br>`$response``=``$client``->call(``"goods.Goods.push "``, $ goods, $ specList);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.push#autoTab0_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>```"status"``: 0,`<br>```"data"``: 54645`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.push#autoTab1_0)

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | `{`<br>`"status"``: 100,`<br>`"message"``:``"商家编码已存在"`<br>`}` |

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