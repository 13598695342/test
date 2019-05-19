#!/usr/bin/python
#-*- coding:utf-8 -*-
l=[]
a=0
for i in range(1,1000):
    for j in range(1,i):
        if i%j==0:
            l.append(j)
    if sum(l)==i:
        print(l)
        print(i)
        a=a+i
        print(a)
    l=[]


for i in range(1,1000):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)

