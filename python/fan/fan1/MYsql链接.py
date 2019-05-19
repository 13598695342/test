#!/usr/bin/python
#-*- coding:utf-8 -*-
# import mysql.connector
# #连接数据
# my=mysql.connector.connect(
#     host="192.168.1.117",
#     user="root",
#     passwd="123456"
# )
import pymysql
# 连接数据库
conn=pymysql.connect(host='192.168.1.117',port=3306,user='root',passwd='123456')
# 创建游标
mycusor=conn.cursor()
# 执行sql语句
# mycusor.execute('create database fanshilong')
mycusor.execute('use fanshilong')
# mycusor.execute('create table fan1(name char(255),age int)')
# for i in range(100):
    # mycusor.execute('insert into fan1 values("{}","{}");'.format(i,i+1))
# 提交
#     conn.commit()
# mycusor.execute('alter table fan1 add  primary key(name);')
mycusor.execute('select * from fan1;')
# 1.fetchall 获取上一个sql语句的结果
# a=mycusor.fetchall()
# 2.fetchmany(参数)默认只获取结果中的第一个数据，如果传入的参数是个数字，数字是几他就获取几条数据
# a=mycusor.fetchmany(2)
# 3.fetchone()每次只获取一条结果，本身有迭代的功能
a=mycusor.fetchone()
a1=mycusor.fetchone()
a2=mycusor.fetchone()
print(a,a1,a2)
# for i in mycusor:
#     print(i)
#断开连接
conn.close()
