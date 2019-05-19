#!/usr/bin/python
#-*- coding:utf-8 -*-
while True:
    b=int(input('请输入范围起始数'))
    c=int(input('请输入范围结束数'))
    if b<0:
        break
    sum=0
    for i in range(b,c+1):
        b=1
        for j in range(1,i+1):
           b=b*j
        sum=sum+b
    print(sum)
