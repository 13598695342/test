#!/usr/bin/python
#-*- coding:utf-8 -*-
a=[1,3,2,4,6,5]
a.sort()
a[-1],a[0]=a[0],a[-1]
print(a)
