#!/usr/bin/python
#-*- coding:utf-8 -*-
a=input('请输入4个数：')
b=a.split(',')
v,c=[],[]
for n in b:
    c.append(int(n))
print(c)
for i in  c:
    for j in c:
        for d in c:
            if i!=j and j!=d and d!=i:
                s=int(i)*100+(j)*10+int(d)*1
                v.append(s)

v.sort()
print(len(v))
