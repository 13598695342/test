#!/usr/bin/python
#-*- coding:utf-8 -*-
a=[1,2,3,4,5,6,7,8,9]
for i in range(1,len(a)):
    a[i-1],a[i]=a[i],a[i-1]
print(a)
