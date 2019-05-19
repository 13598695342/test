#!/usr/bin/python
#-*- coding:utf-8 -*-
import pymysql
conn=pymysql.connect(host='192.168.1.117',port=3306,user='root',passwd='123456')
my=conn.cursor()
while True:
    a=input('请输入命令语句：')
    if a=='exit':
        break
    try:
        my.execute('{};'.format(a))
        conn.commit()
        b=my.fetchall()
        print(b)
    except:
        print('输入错误,请重新输入')
        continue

conn.close()
