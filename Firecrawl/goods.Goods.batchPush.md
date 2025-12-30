---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.batchPush"
title: "API文档"
---
**goods.Goods.batchPush** **（货品批量推送）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** ①批量推送货品资料给ERP ②更新ERP货品档案资料 |
| **1.2 适用版本：** 客户端 V1.4.3.2及以上版本 |
| 1.3注意事项：spu维度一次不超过50条，一个goodsInfo下sku维度一次不超过500条 |

**2.调用场景**

|     |
| --- |
| **2.1 举例说明：**自研商城、SCM、SRM、财务系统、SAP等系统的对接 |

**3.请求参数说明**

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
| 货品信息 | goodsInfo | List<Map<String, Object>> |  | 是 | 货品信息 |

**goodsInfo**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品编号 | goods\_no | String | 40 | Y | 货品编号 |
| 货品名称 | goods\_name | String | 255 | Y | 货品名称 |
| 分类名称 | class\_name | String | 64 | N | 分类名称,不传或为空则默认为’无’ |
| 品牌名称 | brand\_name | String | 64 | N | 品牌名称, 不传或为空则默认为’无’ |
| 基本单位名称 | unit\_name | String | 20 | N | 基本单位名称, 不传或为空则默认为’无’ |
| 辅助单位名称 | aux\_unit\_name | String | 20 | N | 辅助单位名称, 不传或为空则默认为’无’ |
| 货品标记名称 | flag\_name | String | 32 | N | 货品标记名称, 不传或为空则默认为’无’ |
| 货品类别 | goods\_type | Int | 4 | N | 默认0, <br>0：其它<br>1：销售货品<br>2：原材料<br>3：包装物<br>4：周转材料<br>5：虚拟商品<br>6：固定资产<br>8：分装箱 |
| 货品简称 | short\_name | String | 255 | N | 货品简称 |
| 货品别名 | alias | String | 255 | N | 货品别名 |
| 拼音 | pinyin | String | 40 | N | 拼音 |
| 产地 | origin | String | 64 | N | 产地 |
| 货品备注 | remark | String | 512 | N | 货品备注 |
| 货品自定义属性1 | prop1 | String | 255 | N | 货品自定义属性1 |
| 货品自定义属性2 | prop2 | String | 255 | N | 货品自定义属性2 |
| 货品自定义属性3 | prop3 | String | 255 | N | 货品自定义属性3 |
| 货品自定义属性4 | prop4 | String | 255 | N | 货品自定义属性4 |
| 货品自定义属性5 | prop5 | String | 255 | N | 货品自定义属性5 |
| 货品自定义属性6 | prop6 | String | 255 | N | 货品自定义属性6 |
| 是否自动创建品牌和分类 | auto\_create\_bc | bool | 1 | N | 如果品牌,分类不存在,是否自动创建.不填默认为false |
| 单品信息列表 | spec\_list | List<Map<String, Object>> |  | Y | 单品信息列表 |

**spec\_list**

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

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 0表示成功推送。 |
| 返回信息 | message | String |  | 否 | 如果创建/修改成功message内容为空,否则为错误信息 |
| error\_list | data | List<Map<String, Object>> |  | 是 | 错误信息 |

**error\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品编号 | no | String | 40 | 是 | 货品编号 |
| 错误信息 | error | String | 40 | 是 | 错误信息 |

**5.请求示例**

|     |     |
| --- | --- |
| json格式请求报文 | |     |     |
| --- | --- |
|  | `[`<br>```[`<br>```{`<br>```"goods_no"``:``"testGoodsQ12-26 11:28:14_0"``,`<br>```"goods_name"``:``"testGoodsNameQ12-26 11:28:14_0"``,`<br>```"short_name"``:``"shortName"``,`<br>```"auto_create_bc"``:``true``,`<br>```"class_name"``:``"社区团购三级"``,`<br>```"brand_name"``:``"新建品牌3"``,`<br>```"goods_type"``: 1,`<br>```"alias"``:``"alias"``,`<br>```"pinyin"``:``"ceshi"``,`<br>```"origin"``:``"内蒙古呼和浩特市"``,`<br>```"remark"``:``"货品备注"``,`<br>```"prop1"``:``"P1"``,`<br>```"prop2"``:``"P2"``,`<br>```"prop3"``:``"P13"``,`<br>```"prop4"``:``"P14"``,`<br>```"prop5"``:``"P15"``,`<br>```"prop6"``:``"P16"``,`<br>```"flag_name"``:``""``,`<br>```"spec_list"``: [`<br>```{`<br>```"spec_no"``:``"spec_noQ12-26 11:28:14_0_0"``,`<br>```"spec_name"``:``"spec_nameQ12-26 11:28:14_0_0"``,`<br>```"spec_code"``:``"spec_code"``,`<br>```"barcode"``:``"spec_noQ12-26 11:28:14_0_0"``,`<br>```"is_not_need_examine"``: 1,`<br>```"pack_score"``: 12,`<br>```"lowest_price"``: 200,`<br>```"remark"``:``"单品备注"``,`<br>```"sn_type"``: 1,`<br>```"retail_price"``: 1,`<br>```"wholesale_price"``: 1,`<br>```"market_price"``: 1,`<br>```"is_single_batch"``: 1,`<br>```"custom_price1"``: 1,`<br>```"custom_price2"``: 2`<br>```},`<br>```{`<br>```"spec_no"``:``"spec_noQ12-26 11:28:14_0_1"``,`<br>```"spec_name"``:``"spec_nameQ12-26 11:28:14_0_1"``,`<br>```"spec_code"``:``"spec_code"``,`<br>```"barcode"``:``"spec_noQ12-26 11:28:14_0_1"``,`<br>```"is_not_need_examine"``: 1,`<br>```"pack_score"``: 12,`<br>```"lowest_price"``: 200,`<br>```"remark"``:``"单品备注"``,`<br>```"sn_type"``: 1,`<br>```"retail_price"``: 1,`<br>```"wholesale_price"``: 1,`<br>```"market_price"``: 1,`<br>```"is_single_batch"``: 1,`<br>```"custom_price1"``: 1,`<br>```"custom_price2"``: 2`<br>```}`<br>```]`<br>```},`<br>```{`<br>```"goods_no"``:``"testGoodsQ12-26 11:28:14_1"``,`<br>```"goods_name"``:``"testGoodsNameQ12-26 11:28:14_1"``,`<br>```"short_name"``:``"shortName"``,`<br>```"auto_create_bc"``:``true``,`<br>```"class_name"``:``"社区团购三级"``,`<br>```"brand_name"``:``"新建品牌3"``,`<br>```"goods_type"``: 1,`<br>```"alias"``:``"alias"``,`<br>```"pinyin"``:``"ceshi"``,`<br>```"origin"``:``"内蒙古呼和浩特市"``,`<br>```"remark"``:``"货品备注"``,`<br>```"prop1"``:``"P1"``,`<br>```"prop2"``:``"P2"``,`<br>```"prop3"``:``"P13"``,`<br>```"prop4"``:``"P14"``,`<br>```"prop5"``:``"P15"``,`<br>```"prop6"``:``"P16"``,`<br>```"flag_name"``:``""``,`<br>```"spec_list"``: [`<br>```{`<br>```"spec_no"``:``"spec_noQ12-26 11:28:14_1_0"``,`<br>```"spec_name"``:``"spec_nameQ12-26 11:28:14_1_0"``,`<br>```"spec_code"``:``"spec_code"``,`<br>```"barcode"``:``"spec_noQ12-26 11:28:14_1_0"``,`<br>```"is_not_need_examine"``: 1,`<br>```"pack_score"``: 12,`<br>```"lowest_price"``: 200,`<br>```"remark"``:``"单品备注"``,`<br>```"sn_type"``: 1,`<br>```"retail_price"``: 1,`<br>```"wholesale_price"``: 1,`<br>```"market_price"``: 1,`<br>```"is_single_batch"``: 1,`<br>```"custom_price1"``: 1,`<br>```"custom_price2"``: 2`<br>```},`<br>```{`<br>```"spec_no"``:``"spec_noQ12-26 11:28:14_1_1"``,`<br>```"spec_name"``:``"spec_nameQ12-26 11:28:14_1_1"``,`<br>```"spec_code"``:``"spec_code"``,`<br>```"barcode"``:``"spec_noQ12-26 11:28:14_1_1"``,`<br>```"is_not_need_examine"``: 1,`<br>```"pack_score"``: 12,`<br>```"lowest_price"``: 200,`<br>```"remark"``:``"单品备注"``,`<br>```"sn_type"``: 1,`<br>```"retail_price"``: 1,`<br>```"wholesale_price"``: 1,`<br>```"market_price"``: 1,`<br>```"is_single_batch"``: 1,`<br>```"custom_price1"``: 1,`<br>```"custom_price2"``: 2`<br>```}`<br>```]`<br>```}`<br>```]`<br>`]` | |
| PHP | |     |     |
| --- | --- |
| 1 | `<br>` | |
| JAVA |  |
| C# |  |

**6.响应示** **例**

6.1 正常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"error_list"``: []`<br>```}`<br>`}` | |

6.2 异常响应示例

|     |     |
| --- | --- |
| JSON | |     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"error_list"``: [`<br>```{`<br>```"error"``:``"单品条数不得超过500条或为空"``,`<br>```"no"``:``"testGoodsQ12-21 10:52:32_0"`<br>```},`<br>```{`<br>```"error"``:``"单品条数不得超过500条或为空"``,`<br>```"no"``:``"testGoodsQ12-21 10:52:32_1"`<br>```}`<br>```]`<br>```}`<br>`}` | |
