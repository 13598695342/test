#!/usr/bin/python
#-*- coding:utf-8 -*-
a=[]
b=input('请输入一组数据，并以逗号隔开：')
c=b.split(',')
for i in c:
    a.append(int(i))
d=list(set(a))
d.sort()
print(d)
