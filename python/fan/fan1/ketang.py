#!/usr/bin/python
#-*- coding:utf-8 -*-
# a='sdfdsf'
# b=1
# c=2
# def hanshu(a,b,c):
#     print(list(a))
#     l=[]
#     for j in a:
#        l.append(j)
#     for i in l[b:c+1]:
#         l.remove(i)
#     return l
# print(hanshu(a,b,c))
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',443))
# s.listen(3)
# client,addr=s.accept()
# rev=client.recv(1024)
# print(rev.decode('utf-8'))
# mes='nihao'
# client.send(mes.encode('utf-8'))
# import smtplib
# import email.mime.multipart
# import email.mime.text
# sp='13598695342@163.com'
# ap='694120137@qq.com'
# server='smtp.163.com'
# passwd='739146shi'
# mes=email.mime.multipart.MIMEMultipart()
# mes['from']=sp
# mes['to']=ap
# mes['subject']='python'
# text='nihaoma'
# txt=email.mime.text.MIMEText(text)
# mes.attach(txt)
#
# ser=smtplib.SMTP_SSL(server,465)
# ser.login(sp,passwd)
# ser.sendmail(sp,ap,mes.as_string())
# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
#质数之和
# a=int(input('>>>'))
# b=0
# for i in range(2,a+1):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#        b+=i
# print(b)
#阶乘之和
# a=int(input('>>>'))
# c=0
# for i in range(1,a+1):
#     b=1
#     for j in range(1,i+1):
#         b=b*j
#     c+=b
# print(c)
#判断三角形
# a=input('>>>')
# b=a.split(',')
# c=[]
# for i in b:
#    c.append(i)
# c.sort()
# if a[0]+a[1]>a[2]:
#     if a[0]**2+a[1]**2>a[2]**2:
#         print('锐角三角形')
#     elif a[0]**2+a[1]**2==a[2]**2:
#         print('直角三角形')
#     elif a[0]**2+a[1]**2<a[2]**2:
#         print('钝角三角形')
# else:
#     print('不是三角形')
#判断以什么开头，以什么结束
# a=input('>>>')
# if a.startswith('a') and a.endswith('b'):
#     print('hello world')
# elif a.startswith('a'):
#     print('hello')
# elif a.endswith('b'):
#     print('world')
# else:
#     print(110)
#去重并排序
# a=[12,32,12,112,32,435,12,34,12,32]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
# print(b)
#判断字符串是否回文
# a=input('>>>')
# b=len(a)
# for i in range(b//2):
#     if a[i]!=a[-i-1]:
#         print('不是回文')
#         break
# else:
#     print('是回文')
#choice
# a=input('>>>')
# b=a.split(',')
# c=[]
# for i in b:
#     c.append(int(i))
# d=len(c)
# for j in range(d):
#     for f in range(d):
#         if c[j]<c[f]:
#             c[f],c[j]=c[j],c[f]
#
#     print(c)
# import random
# a=random.randrange(1,10)
# print(a)
# n=1
# while True:
#     i=int(input('>>>'))
#     if i==a:
#         print('正确')
#     elif i>a:
#         print('大，还剩{}次机会'.format(3-n))
#     elif i<a:
#         print('小，还剩{}次机会'.format(3-n))
#     if n>3:
#         print('次数已用完')
#         break
#     n+=1
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     d=a**3+b**3+c**3
#     if i==d:
#         print(i)
# a='2314214341243542142'
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b+=j*10**i
# print(b)
#
a=[132,434,54,65,87,97]
for
print(b)
