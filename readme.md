# 电子发票管理系统
Southwest Minzu University
author:wcy
这是一个基于OCR技术的电子发票识别与管理系统。系统支持增值税发票的批量上传、识别、存储和管理,提供发票信息的查询、打印和下载等功能。

## 功能特点

- 发票批量上传与OCR识别
- 发票信息自动提取与存储
- 发票信息查询(按发票代码、发票号码)
- 发票批量打印
- 发票批量下载
- 发票详细信息查看

## 技术栈

### 前端
- Vue 3
- Element Plus UI
- TypeScript
- Axios
- PDF Merger

### 后端
- Python Flask
- SQLAlchemy ORM
- OCR识别技术

## 系统架构

## 系统界面展示

### 主界面
![主界面](images/1.png)
主界面提供发票查询、上传、下载和打印等核心功能操作。用户可以通过发票代码和发票号码进行精确查询，支持批量选择发票进行下载或打印操作。

### 发票详情
![发票详情](images/2.png)
发票详情界面展示单张发票的完整信息，包括购买方信息、销售方信息、发票金额等详细数据。

## 项目结构
├── Invoice-project/ # 后端项目
│ ├── orm/ # 数据库相关
│ │ ├── config.py # 数据库配置
│ │ ├── invoice.py # 发票模型
│ │ └── repo/ # 数据库操作
│ ├── services/ # API服务
│ │ ├── file_api.py # 文件处理API
│ │ └── invoice_api.py # 发票管理API
│ └── utils/ # 工具类
│ └── Extractor.py # OCR提取器
│
├── invoice-client/ # 前端项目
│ ├── src/
│ │ ├── components/ # 组件
│ │ ├── store/ # 状态管理
│ │ └── VAT_invoice.vue # 主页面
## 前端
yarn 
yarn serve


## 使用说明

1. 发票上传
   - 点击"上传"按钮
   - 选择需要上传的发票文件(支持ZIP格式批量上传)
   - 系统会自动识别发票信息并存储

2. 发票查询
   - 输入发票代码或发票号码
   - 点击"查询"按钮获取结果

3. 发票打印
   - 选择需要打印的发票
   - 点击"打印"按钮
   - 系统会自动合并PDF并调用打印服务

4. 发票下载
   - 选择需要下载的发票
   - 点击"下载"按钮
   - 系统会将选中的发票打包成ZIP文件下载

## 注意事项

- 支持的发票格式: PDF
- 批量上传时需将发票文件打包为ZIP格式
- 为保证OCR识别准确性,上传的发票图片需清晰可辨
- 重复上传相同发票会被系统自动过滤

## 许可证

[MIT License](LICENSE)