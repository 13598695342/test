#!/usr/bin/python
#-*- coding:utf-8 -*-

a='0123456318312391253210'
a=a[::-1]
b=0
for i in range(len(a)):
   for j in range(10):
      if str(j)==a[i]:
         b+=j*10**i   #b+=j*10**(len(a)-1-i)
print(b)


