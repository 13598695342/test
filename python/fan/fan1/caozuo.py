#!/usr/bin/python
#-*- coding:utf-8 -*-
# 自带的库，是与操作系统交互
# 通过os模块来控制操作系统
import os
# 删除文件
# os.remove('b.xls')
# 执行windows命令
# b=os.popen('ipconfig/all')
# print(b.read())
#获取当前所在的位置
# print(os.getcwd())
#切换目录
# os.chdir(r'D:\python')
# print(os.getcwd())
#获取当前文件夹下面有多少文件 '.'：代表当前目录
# a=os.listdir('.')
# b='.py'
# for i in a:
#     if b in i:
#         print(i)
# # 将路径与文件分隔开
# a=os.path.split(r'C:\Users\fansl\Desktop\20190121练习题.docx')
# print(a)
# 将文件后缀名与路径分隔开
# b=os.path.splitext(r'C:\Users\fansl\Desktop\20190121练习题.docx')
# print(b)
#将盘符与路径分隔开
# c=os.path.splitdrive(r'C:\Users\fansl\Desktop\20190121练习题.docx')
# print(c)
# 判断文件是否是一个目录
# a=os.path.isdir('C:')
# print(a)
# 判断文件是否是一个普通文件
# b=os.path.isfile('a.xls')
# print(b)
# 创建文件夹
# os.mkdir('aaa')
# 创建递归文件夹
# os.makedirs('bbb/ccc/vvv')
# 删除空文件夹
# os.rmdir('aaa')
# 删除递归文件夹空得
# os.removedirs('bbb/ccc/vvv')
import paramiko
#创建一个远程客户端
# ssh1=paramiko.SSHClient()
# 跳过验证，不到know_hosts文件中去查找
# ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接主机
# ssh1.connect(hostname='192.168.2.119',port=22,username='root',password='123456')
# 执行命令，只能执行有结果的命令 例如：切换目录 cd /home
# stuin,stuout,stuerr=ssh1.exec_command('ls -al')
# stuin：执行的命令
# stuout：执行的结果
# stuerr：执行的报错
# print(stuout.read().decode())
# ssh1.close()


# 传输文件
# 建立一个传输通道，填入IP地址需要是一个元组
# ssh1=paramiko.Transport(('192.168.2.119',22))
# 连接主机，只需要输入用户名和密码
# ssh1.connect(username='root',password='123456')
# 创建一个SFTP客户端
# sftp=paramiko.SFTPClient.from_transport(ssh1)
# 从linux文件到windows
# 从linux下载文件到windows，如果是其他目录需要加路径 sftp.get('anaconda-ks.cfg','aaa.cfg')可以重命名
# sftp.get('anaconda-ks.cfg','aaa.cfg')
# 从windows上传文件到linux
# sftp.put('a.py','/home/a.py')
# ssh1.close()


# import smtplib  #封装了smtp协议
# import email.mime.multipart #处理邮件中的组成部分
# import email.mime.text #处理邮件中的正文
# # 发件人
# sp='13598695342@163.com'
# # 收件人
# ap='694120137@qq.com'
# # 服务器
# server='smtp.163.com'
# # 授权码 授予登录客户端的权限的密码
# passwd='739146shi'
# # 创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# # 给邮件里添加一个发件人
# message['from']=sp
# # 给邮件里添加一个收件人
# message['to']=ap
# # 添加一个主题
# message['subject']='python learn'
# # 写的邮件正文
# text='你好!!! \n hello world'
# # 处理正文文本
# txt=email.mime.text.MIMEText(text)
# message.attach(txt)
#
# # 添加附件(附加的文件)
# att2 = email.mime.text.MIMEText(open('a.py', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="a.py"'
# ## 头部字段
# message.attach(att2)
#
# # 定义服务器
# smtp1=smtplib.SMTP_SSL(server,465)
# # 登录服务器
# smtp1.login(sp,passwd)
# # 发送邮件
# smtp1.sendmail(sp,ap,message.as_string())
# # 断开连接
# smtp1.close()


# socket 简单
# 函数 面向对象 列表推导式 lambda with
# import  os
# os.remove()
# b=os.popen('ipconfig/all')
# print(b.read())
# print(os.getcwd())
# os.chdir(r'c:')
# print(os.getcwd())
# a=os.listdir('..')
# print(a)
# b=os.path.splitext(r'D:\python\fan\fan1')
# print(b)
# os.path.isdir()
# os.path.isfile()


import paramiko
ssh1=paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh1.connect(hostname='192.168.2.119',port=3306,username='root',password='123456')
stutin,stuout,stuerr=ssh1.exec_command('ls -al')
print(stuout.read().decode())
