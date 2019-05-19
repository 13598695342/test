#!/usr/bin/python
#-*- coding:utf-8 -*-
c,b=list(),list()
for i in range(1,100,2):
    if i>=55:
        b.append(i)
    elif i<55:
        c.append(i)
print(b)
print(c)
