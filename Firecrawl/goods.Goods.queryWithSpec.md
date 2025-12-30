---
url: "https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.queryWithSpec"
title: "API文档"
---
****goods.Goods.queryWithSpec**（货品档案查询）**

**1.接口说明**

|     |
| --- |
| **1.1 接口描述：** 获取ERP的货品档案资料 |
| **1.2 适用版本：** 客户端 V1.6.0.10及以上版本 |
| **1.3 增量获取：** 支持 |
| **1.4 时间跨度：** start\_time和end\_time最大跨度为30天 |
| **1.5注意事项：** 开始时间和结束时间是 货品 或 单品 最后修改时间的范围<br>**【权限校验】：品牌权限**（旺店通客户端-采购-采购权限管理界面控制品牌权限） |

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
| 分页大小 | page\_size | int |  | 否 | 分页大小，分页查询必传 |
| 分页编号 | page\_no | int |  | 否 | 分页编号，分页查询必传，标准接口page\_no从0开始 |
| 是否计算查询结果的总条数 | calc\_total | int |  | 否 | 是否计算查询结果的总条数, 需要计算则1, 否则填0 |

3.3 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 查询参数 | params | Map<String, Object> |  | 是 | 查询参数 |
| 分页 | pager | Pager |  | 是 | 分页 |

**params**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec\_no | String | 40 | 否 | 商家编码（如果不传时间，则spec\_no和goods\_no必须传一个） |
| 货品编号 | goods\_no | String | 40 | 否 | 货品编号 |
| 品牌名称 | brand\_name | String | 64 | 否 | 品牌名称 |
| 分类名称 | class\_name | String | 100 | 否 | 分类名称 |
| 条码 | barcode | String | 50 | 否 | 条码 |
| 是否隐藏已删除的货品。 | hide\_deleted | boolean | 1 | 否 | 0:返回全部;1:隐藏已删除   默认隐藏 |
| 开始时间 | start\_time | String | 40 | 否 | 起始修改时间    最大跨度为30天 |
| 结束时间 | end\_time | String | 40 | 否 | 结束修改时间, 不填默认为当前时间   最大跨度为30天 |

**pager**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page\_size | Int | 4 | 否 | 分页大小 |
| 页号 | page\_no | Int | 4 | 否 | 从0开始 |

**4.响应参数**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 状态码 | status | Int |  | 是 | 状态码,0表示正常 |
| 错误信息 | message | String |  | 是 | 无错误信息不返回 |
| 货品数据 | data | Map<String, Object> |  | 是 | 货品相关数据 |

**data**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品数据 | goods\_list | List<Map<String, Object>> |  | 是 | 货品数据 |
| 总数 | total\_count | Int | 11 | 是 | 查询条件总单据数 |

**goods\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品id | goods\_id | Int |  | 是 | 唯一键 |
| 货品编号 | goods\_no | String | 40 | 是 | 货品编号 |
| 货品名称 | goods\_name | String | 255 | 是 | 货品名称 |
| 货品简称 | short\_name | String | 255 | 是 | 货品简称 |
| 货品别名 | alias | String | 255 | 是 | 货品别名 |
| 货品类别 | goods\_type | int | 4 | 是 | 货品类别<br>0：其它<br>1：销售货品<br>2：原材料<br>3：包装物<br>4：周转材料<br>5：虚拟商品<br>6：固定资产<br>8：分装箱<br>9：周期送货品<br>10：赠品 |
| 规格数 | spec\_count | Int | 11 | 是 | 规格数 |
| 品牌名称 | brand\_name | String | 64 | 是 | 品牌名称 |
| 品牌id | brand\_id | Int | 11 | 是 | 品牌id |
| 备注 | remark | String | 512 | 是 | 备注 |
| 自定义属性1 | prop1 | String | 255 | 是 | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | 是 | 自定义属性2 |
| 自定义属性3 | prop3 | String | 255 | 是 | 自定义属性3 |
| 自定义属性4 | prop4 | String | 255 | 是 | 自定义属性4 |
| 自定义属性5 | prop5 | String | 255 | 是 | 自定义属性5 |
| 自定义属性6 | prop6 | String | 255 | 是 | 自定义属性6 |
| 产地 | origin | String | 64 | 是 | 产地 |
| 分类名称 | class\_name | String | 64 | 是 | 分类名称 |
| 分类ID | class\_id | int |  | 是 | 分类ID主键 |
| 基本单位 | unit\_name | String | 20 | 是 | 基本单位 |
| 辅助单位 | aux\_unit\_name | String | 20 | 是 | 辅助单位 |
| 标记名称 | flag\_name | String | 32 | 是 | 标记名称 |
| 货品已删除 | deleted | Int | 11 | 是 | 0代表未删除   大于0代表已删除 |
| 最后修改时间 | goods\_modified | String | 40 | 是 | 最后修改时间 |
| 创建时间 | goods\_created | String | 40 | 是 | 创建时间, 时间格式 YYYY-MM-DD HH:MM:SS |
| 最后修改时间 | modified | String | 40 | 是 | 最后修改时间，格式：yyyy-MM-dd HH:mm:ss |
| 品牌编号 | brand\_no | String | 64 | 是 | 品牌编号 |
| 水洗标 | washing\_label | String | 20 | 是 | 水洗标 |
| 单品信息详情 | spec\_list | List<Map<String, Object>> |  | 是 | 单品信息详情 |

**spec\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品id | goods\_id | Int |  | 是 | 货品唯一键 |
| 单品id | spec\_id | Int |  | 是 | 单品唯一键 |
| 商家编码 | spec\_no | String | 40 | 是 | 商家编码 |
| 规格码 | spec\_code | String | 40 | 是 | 规格码 |
| 主条码 | barcode | String | 50 | 是 | 主条码 |
| 规格名称 | spec\_name | String | 100 | 是 | 规格名称 |
| 最低价 | lowest\_price | Decimal(19,4) |  | 是 | 最低价 |
| 零售价 | retail\_price | Decimal(19,4) |  | 是 | 零售价 |
| 批发价 | wholesale\_price | Decimal(19,4) |  | 是 | 批发价 |
| 会员价 | member\_price | Decimal(19,4) |  | 是 | 会员价 |
| 市场价 | market\_price | Decimal(19,4) |  | 是 | 市场价 |
| 有效期天数 | validity\_days | Int | 11 | 是 | 有效期天数 |
| 最佳销售天数 | sales\_days | Int | 11 | 是 | 最佳销售天数 |
| 最佳收货天数 | receive\_days | Int | 11 | 是 | 最佳收货天数 |
| 重量(kg) | weight | Decimal(19,4) |  | 是 | 重量(kg) |
| 长(cm) | length | Decimal(19,4) |  | 是 | 长(cm) |
| 宽(cm) | width | Decimal(19,4) |  | 是 | 宽(cm) |
| 高(cm) | height | Decimal(19,4) |  | 是 | 高(cm) |
| 启用序列号 | sn\_type | Int | 4 | 是 | 启用序列号(原is\_sn\_enable)  0:未启用  1:已启用 |
| 允许低于成本价 | is\_lower\_cost | boolean | 1 | 是 | 允许低于成本价<br>true：是<br>false：否 |
| 航空禁运 | is\_not\_use\_air | Int | 1 | 是 | 航空禁运 |
| 仓库流程 | wms\_process\_mask | int | 4 | 是 | 默认0：无仓库流程<br>（需要的仓库流程相加）<br>2：无需验货 <br>8：需要质检 <br>16：无需拣货<br>32：无需唯一码<br>64：无需自动打印吊牌<br>128：不计结构<br>256：电子面单不打印<br>512：不计绩效<br>1024：管理克重<br>2048：退货入库不校验 |
| 税率 | tax\_rate | Decimal(19,4） |  | 是 | 税率 |
| 拆分 | large\_type | int | 4 | 是 | 大件类别<br>0、 普通件<br>1、 普通大件（可与非大件一起发）<br>2、 独立大件（不可和小件一起发）<br>3、按箱规拆分<br>      -1、非单发件 |
| 货品标签 | goods\_label | String | 255 | 是 | 货品标签，多个标签用英文逗号隔开 |
| 货品已删除 | deleted | int | 11 | 是 | 0代表未删除  大于0代表已删除 |
| 备注 | remark | String | 512 | 是 | 备注 |
| 最后修改时间 | spec\_modified | int | 40 | 是 | 最后修改时间 |
| 创建时间 | spec\_created | String | 40 | 是 | 创建时间, 时间格式 YYYY-MM-DD HH:MM:SS |
| 自定义属性1 | prop1 | String | 255 | 是 | 自定义属性1 |
| 自定义属性2 | prop2 | String | 255 | 是 | 自定义属性2 |
| 自定义属性3 | prop3 | String | 255 | 是 | 自定义属性3 |
| 自定义属性4 | prop4 | String | 255 | 是 | 自定义属性4 |
| 自定义属性5 | prop5 | String | 255 | 是 | 自定义属性5 |
| 自定义属性6 | prop6 | String | 255 | 是 | 自定义属性6 |
| 自定义价格1 | custom\_price1 | Decimal(19,4） |  | 是 | 自定义价格1 |
| 自定义价格2 | custom\_price2 | Decimal(19,4） |  | 是 | 自定义价格2 |
| 图片URL | img\_url | String | 1024 | 是 | 图片URL |
| 基本单位 | spec\_unit\_name | String | 20 | 是 | 基本单位 |
| 辅助单位 | spec\_aux\_unit\_name | String | 20 | 是 | 辅助单位 |
| 税务编码 | tax\_code | String | 40 | 是 | 税务编码 |
| 打包积分 | pack\_score | Decimal(19,4） |  | 是 | 打包积分 |
| 拣货积分 | pick\_score | Decimal(19,4） |  | 是 | 拣货积分 |
| 验货积分 | scan\_score | Decimal(19,4） |  | 是 | 验货积分 |
| 单品标记名称 | spec\_flag\_name | String | 32 | 是 | 单品标记名称 |
| 条码个数 | barcode\_count | Int |  | 是 | 条码个数 |
| 销售积分 | sale\_score | Decimal(19,4） |  | 是 | 销售积分 |
| 是否出库不验货 | is\_not\_need\_examine | Int |  | 是 | 是否出库不验货<br>1：出库不验货<br>0：出库验货 |
| 条码信息 | barcode\_list | List<Map<String,Object>> |  | 是 | 条码信息，没有时为空数组 |

**barcode\_list**

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 条码 | barcode | String | 50 | 否 | 条码 |
| 类型 | type | Int | 4 | 否 | 货品类型，这里默认为1 |
| 是否主条码 | is\_master | Int | 1 | 否 | 是否主条码<br>1：是<br>0：否· |
| 最后修改时间 | modified | String | 40 | 否 | 最后修改时间，<br>格式: yyyy-MM-dd HH:mm:ss |

**5.请求示例**

- [json格式请求报文](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.queryWithSpec#autoTab0_0)
- [PHP](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.queryWithSpec#autoTab0_1)
- [JAVA](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.queryWithSpec#autoTab0_2)
- [C#](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.queryWithSpec#autoTab0_3)

|     |     |
| --- | --- |
|  | `[{`<br>`"start_time"``:``"2020-01-01 00:00:00"``,`<br>`"end_time"``:``"2020-01-20 00:00:00"``,`<br>`"hide_deleted"``: 1`<br>`}]` |

|     |     |
| --- | --- |
|  | `<?php`<br>`header(``"Content-Type: text/html; charset=UTF-8"``);`<br>`date_default_timezone_set(``"Asia/Shanghai"``);`<br>`require_once``(``'wdtsdk.php'``);`<br>``<br>`$client``=``new``WdtErpClient(``"url"``,``"wdtapi3"``,``"appkey"``,``"secret"``);`<br>``<br>`$parMap``=``new``stdClass();`<br>`$parMap``->start_time =``"2020-01-01 00:00:00"``;`<br>`$parMap``->end_time =``"2020-01-20 00:00:00"``;`<br>`$parMap``->hide_deleted=1;`<br>``<br>``<br>`$pager``=``new``Pager(1, 0, true);`<br>`$data``=``$client``->pageCall(``"goods.Goods.queryWithSpec"``,``$pager``,``$parMap``);`<br>``<br>`?>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

|     |     |
| --- | --- |
| 1 | `<br>` |

**6.响应示** **例**

6.1 正常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.queryWithSpec#autoTab0_0)

|     |     |
| --- | --- |
|  | `{`<br>```"status"``: 0,`<br>```"data"``: {`<br>```"goods_list"``: [{`<br>```"goods_no"``:``"wangdiantong"``,`<br>```"origin"``:``""``,`<br>```"class_id"``: 7,`<br>```"goods_modified"``: 1678351062000,`<br>```"remark"``:``"12323213aaa"``,`<br>```"aux_unit_name"``:``"哒哒哒哒哒"``,`<br>```"goods_created"``:``"2017-08-06 22:01:20"``,`<br>```"flag_name"``:``"无"``,`<br>```"spec_list"``: [{`<br>```"spec_id"``: 1,`<br>```"goods_id"``: 1,`<br>```"spec_no"``:``"wangdiantong"``,`<br>```"spec_code"``:``"LL "``,`<br>```"barcode"``:``"wangdiantong"``,`<br>```"spec_name"``:``"暂无"``,`<br>```"lowest_price"``: 0,`<br>```"retail_price"``: 234,`<br>```"wholesale_price"``: 0,`<br>```"member_price"``: 0,`<br>```"market_price"``: 0,`<br>```"spec_created"``:``"2017-08-06 22:01:20"``,`<br>```"validity_days"``: 0,`<br>```"sales_days"``: 0,`<br>```"receive_days"``: 0,`<br>```"weight"``: 0.2,`<br>```"length"``: 1,`<br>```"width"``: 2,`<br>```"height"``: 3,`<br>```"sn_type"``: 0,`<br>```"is_lower_cost"``:``false``,`<br>```"tax_rate"``: 0,`<br>```"wms_process_mask"``: 8,`<br>```"deleted"``: 0,`<br>```"large_type"``: 0,`<br>```"remark"``:``"dsfdk;ds123"``,`<br>```"spec_modified"``: 1683771314000,`<br>```"prop1"``:``"自定义属性1"``,`<br>```"prop2"``:``"自定义属性2"``,`<br>```"prop3"``:``"自定义属性3"``,`<br>```"prop4"``:``"自定义属性4"``,`<br>```"prop5"``:``"自定义属性5"``,`<br>```"prop6"``:``"自定义属性6"``,`<br>```"img_url"``:``"cos:\/\/IMG135.jpg"``,`<br>```"is_not_use_air"``: 0,`<br>```"custom_price1"``: 0,`<br>```"custom_price2"``: 0,`<br>```"spec_unit_name"``:``"口"``,`<br>```"spec_aux_unit_name"``:``"锅"``,`<br>```"goods_label"``:``""``,`<br>```"tax_code"``:``""``,`<br>```"barcode_list"``: [{`<br>```"barcode"``:``"wangdiantong"``,`<br>```"type"``: 1,`<br>```"is_master"``: 1,`<br>```"modified"``:``"2022-08-31 11:18:59"`<br>```}]`<br>```}],`<br>```"alias"``:``""``,`<br>```"modified"``:``"2023-03-09 16:37:42"``,`<br>```"spec_count"``: 1,`<br>```"class_name"``:``"短袖1"``,`<br>```"goods_name"``:``"wangdiantong"``,`<br>```"goods_id"``: 1,`<br>```"brand_name"``:``"发发拉"``,`<br>```"prop6"``:``""``,`<br>```"prop5"``:``""``,`<br>```"prop4"``:``""``,`<br>```"brand_id"``: 2179,`<br>```"prop3"``:``""``,`<br>```"prop2"``:``""``,`<br>```"unit_name"``:``"箱"``,`<br>```"prop1"``:``""``,`<br>```"pinyin"``:``""``,`<br>```"deleted"``: 0,`<br>```"short_name"``:``""``,`<br>```"goods_type"``: 1`<br>```}],`<br>```"total_count"``: 1`<br>```}`<br>`}` |

6.2 异常响应示例

- [JSON](https://open.wangdian.cn/qjb/open/apidoc/doc?path=goods.Goods.queryWithSpec#autoTab1_0)

|     |     |
| --- | --- |
|  | `{`<br>`"status"``: 100,`<br>`"message"``:``"参数中必须包含起止时间"`<br>`}` |
