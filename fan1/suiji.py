#!/usr/bin/python
#-*- coding:utf-8 -*-
import random
a=100
c=0
d=[]
while True:
    b=random.randrange(1,11)
    a-=b
    c+=1
    d.append(a)
    if a<=0:
        break
    print('第{}个人，收到{}元，剩余{}元'.format(c,b,a))
print('第{}个人，收到{}元，剩余0元'.format(c,d[-2]))

