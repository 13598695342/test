#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlwt
f=xlwt.Workbook()
sheet=f.add_sheet('study')
d=[]
with open('a.txt','r',encoding='utf-8') as n:
    j=0
    while True:
        c=n.readline()
        z=c.split(',')
        print(z)
        for i in range(len(z)):
            sheet.write(j,i,'{}'.format(z[i]))
        if c=='':
            break
        j=j+1
f.save('a.xls')
