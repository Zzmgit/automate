# 介绍

## 功能描述

该项目主要是通过调用selenium工具，模拟用户行为进行自动化登录GitHub，然后进行关键词搜索，检索出相应的代码仓库，将仓库相关信息进行保存

## 初始化项目

```shell
git clone git@github.com:Zzmgit/automate.git
```

## 依赖环境

```shell
# python(Linux/Unix)
## 创建虚拟环境
virtualenv -p /usr/bin/python3.5 env
# 激活虚拟环境并安装依赖包
source env/bin/activate
pip install -r requirements.txt
```

## 其他说明

main.py为程序执行入口，将调用conf/config.ini文件信息。clone代码后需要将conf/config.example.ini文件名改为config.ini，并配置自己所需的字段信息