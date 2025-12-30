# 旺店通 (Wangdiantong) API 文档索引项目

## 项目背景

本项目旨在构建一个专门针对**旺店通旗舰版 API** 的文档索引库。

> **⚠️ 注意**：旺店通**旗舰版**与**企业版**的 API 并不通用，接口定义和调用方式存在显著差异。本项目仅适用于**旗舰版** API。

本项目主要服务于 **Context7** 或其他 RAG (Retrieval-Augmented Generation) 系统。

通过将旺店通的官方 API 文档进行抓取、清洗和结构化，我们可以将其作为上下文提供给 AI 助手。这使得开发者在 Cursor 等 IDE 中开发对接旺店通 API 的功能时，可以通过 **MCP (Model Context Protocol)** 工具直接查询和调用最新的 API 规范，极大地提高开发效率和准确性。

## 项目结构

*   `Firecrawl/`: 存放 API 文档 Markdown 文件的目录。
*   `rename_firecrawl_files.py`: 用于批量重命名抓取下来的文件，去除冗余的前缀（如 URL 路径参数），使文件名更加简洁易读。
*   `clean_firecrawl_md.py`: 用于清洗 Markdown 文件内容。它会去除网页导航、页脚、无关的 UI 元素（如“常用工具”）、冗余的请求地址说明以及格式混乱的文本，只保留核心的 API 接口定义和参数说明。
*   `requirements.txt`: 项目依赖列表。

## 使用说明

### 1. 环境准备

确保已安装 Python 3，并安装项目依赖：

```bash
pip install -r requirements.txt
```

### 2. 文件重命名

如果是初次导入抓取的原始文件，文件名可能包含较长的前缀。运行重命名脚本进行清理：

```bash
python rename_firecrawl_files.py
```

该脚本会将文件名中形如 `open.wangdian.cn_qjb_open_apidoc_doc_path=` 的前缀去除。

### 3. 文档清洗

原始的文档文件可能包含大量网页特有的干扰信息。运行清洗脚本提取核心内容：

```bash
python clean_firecrawl_md.py
```

该脚本会遍历 `Firecrawl` 目录下的所有 `.md` 文件，执行以下操作：
*   保留 YAML Front Matter。
*   截取 "当前位置： API文档" 之后的内容。
*   去除 "常用工具" 及其之后的内容。
*   移除特定的干扰行（如包含 "¥标准" 的行）。
*   修复格式问题（如连在一起的标题和内容）。
*   删除冗余的“请求地址”板块（通常这部分信息在 Context7 索引中属于噪音）。

### 4. 接入 Context7

处理完成后的 `Firecrawl/` 目录中的 Markdown 文件即可作为 Context7 的知识库源文件进行索引。

