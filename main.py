# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zhangzheming
@Version        :  
------------------------------------
@File           :  main.py
@Description    :  
@CreateTime     :  2019/10/28 16:23
------------------------------------
@ModifyTime     :  
"""
import os
import configparser

from util.gitHub import GitHub
from util.sendMail import SendMail


if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath('.'))
    configpath = os.path.join(root_dir, r'conf\config.ini')

    cf = configparser.ConfigParser()
    cf.read(configpath, encoding='utf-8')  # 拼接得到config.ini文件的路径，直接使用

    # 获取敏感信息词组
    keyword_list = []
    for i in cf.items('KEYWORD'):
        keyword_list.append(i[1])
    print('\033[35m敏感信息词组: {}\033[0m'.format(keyword_list))

    # 获取邮件信息
    mail_host = cf.get('EMAIL', 'mail_host')
    mail_user = cf.get('EMAIL', 'mail_user')
    mail_pass = cf.get('EMAIL', 'mail_pass')

    # 获取GitHub信息
    username = cf.get('GitHub', 'username')
    password = cf.get('GitHub', 'password')
    login_url = cf.get('GitHub', 'login_url')
    search_url = cf.get('GitHub', 'search_url')

    # 获取发件人信息
    sender = cf.get('SENDER', 'sender')

    # 获取收件人信息
    CC_list = []
    for i in cf.items('RECEIVER'):
        CC_list.append(i[1])
    print('\033[34m收件人群组: {}\033[0m'.format(CC_list))

    # 对敏感词进行检索
    for keyword in keyword_list:
        res = GitHub()
        res.login(url=login_url, username=username, password=password)    # 进行登录，可以减少GitHub资源滥用机制(Whoa there!)的触发
        print('\033[32m即将处理的敏感关键词为: {}\033[0m'.format(keyword))
        res.search(search_url, keyword)
        res.save_data(keyword, search_url)

    # 拼接附件地址，并发送含附件邮件
    path = os.path.join(root_dir, r'report')
    report_file = os.listdir(path)[0]
    print(report_file)
    file = os.path.join(root_dir, r'report\{}'.format(report_file))
    print(file)
    sm = SendMail(mail_host, mail_user, mail_pass, sender, CC_list)
    sm.send_enclosure(filename=file, report_name=report_file)
