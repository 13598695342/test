#!/usr/bin/python
#-*- coding:utf-8 -*-

def hanshu():
    c=[]
    e=[]
    a=input('请输入一组数据')
    b=a.split(',')
    for i in b:
        c.append(int(i))
    for g in c:
        if g not in e:
            e.append(g)
    k=len(e)
    for j in range(1,k):
        for d in range(1,k):
            if e[d-1]>e[d]:
               e[d-1],e[d]=e[d],e[d-1]
    print(e)
#调用函数，函数名加括号
hanshu()
