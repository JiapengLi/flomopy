# flomopy
**Flomo 浮墨**命令行工具。

## 使用方法


0. 安装python，安装requests包 (`pip install requests`)
1. 系统创建环境变量FLOMOAPI，内容可于https://flomoapp.com/mine?source=incoming_webhook 获取
2. 保存此 flomo.py 源码文件至本地路径
3. 将存放 flomo.py 的路径添加至系统PATH路径中

### 利用命令行编辑并发送 MEMO
 执行 ` flomo.py '文本...'`

### 利用编辑器编辑并发送 MEMO

创建 FLOMOEDITOR 环境变量。flomo.py 将会调出本地编辑器，保存并关闭文件后自动上传。类似于 `git commit` 的实现。

- vscode: `code --wait`
- sublime: `subl -w`

运行 flomo.py

## 说明

1. 文本中不包含#的 MEMO，将会增加`#待整理`标签
2. 独立的文本参数分行记录

## 注意

- 命令行输入**#**，请使用单引号括起来，否则会被当成注释
- 文本中有**空格**的，请使用单引号括起来，否则会被识别为多行

