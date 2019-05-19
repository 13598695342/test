#!/usr/bin/python
#-*- coding:utf-8 -*-
import pymysql
import xlwt
import xlrd
conn=pymysql.connect(host='192.168.2.119',port=3306,user='root',passwd='123456')
mycusor=conn.cursor()
mycusor.execute('use zhilian')
mycusor.execute('select * from zhilian;')
b=mycusor.fetchall()
print(b)
a=xlwt.Workbook()
sheet=a.add_sheet('zhilian')
sheet.write(0,0,'shijian')
sheet.write(0,1,'city')
sheet.write(0,2,'gongzi')
sheet.write(0,3,'jingyan')
sheet.write(0,4,'gongsi')
sheet.write(0,5,'gongzuo')
i=1
for q,w,e,r,t,y in b:
   sheet.write(i,0,'{}'.format(q))
   sheet.write(i,1,'{}'.format(w))
   sheet.write(i,2,'{}'.format(e))
   sheet.write(i,3,'{}'.format(r))
   sheet.write(i,4,'{}'.format(t))
   sheet.write(i,5,'{}'.format(y))
   i+=1
a.save('hh.xls')


