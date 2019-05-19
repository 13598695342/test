#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
f=xlrd.open_workbook('a.xls')
sheet=f.sheet_by_name('study')
b=f.sheets()[0]
c=sheet.nrows
d=sheet.ncols
print(c)
print(d)
aa=[]
with open('b.txt','w',encoding='utf-8') as l:
    for i in range(c):
      i=sheet.row_values(i)
      for j,k in enumerate(i):
        if j==len(i)-1:
            l.write(k)
        else:
            l.write(k+',')
