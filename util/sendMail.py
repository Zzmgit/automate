# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zhangzheming
@Version        :  
------------------------------------
@File           :  sendMail.py
@Description    :  
@CreateTime     :  2019/10/22 17:52
------------------------------------
@ModifyTime     :  
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendMail(object):
    def __init__(self, mail_host, mail_user, mail_pass, sender, receivers):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender
        self.receivers = receivers

    def send_enclosure(self, filename, report_name):
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        msg['From'] = Header("Zzm", 'utf-8')
        msg['To'] = Header("测试组", 'utf-8')
        subject = 'GitHub自动搜索敏感信息词组检测报告'
        msg['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        msg.attach(MIMEText('这是一封来自遥远星球的邮件~~~', 'plain', 'utf-8'))

        # 构造附件
        att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename={}'.format(report_name)
        msg.attach(att)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 587)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s 无法发送邮件" % e)
