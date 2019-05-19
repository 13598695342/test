#!/usr/bin/python
#-*- coding:utf-8 -*-
#
# while True:
#     c=[]
#     a=input('请输入一组数据，以逗号隔开：')
#     if '-' in a:
#         break
#     else:
#         b=a.split(',')
#         for i in b:
#             c.append(int(i))
#         d=(sum(c)/len(c))
#         print('平均数为{}'.format(d))
#         for j in c:
#             if j<d:
#                 print('低于平均分得学生成绩{}'.format(j))

a=[]
while True:
    j=int(input('qing'))
    a.append(j)
    if j<0:
        break
    print(a)
b=(sum(a)/len(a))
c=0
while c<len(a):
    if a[c]<b:
        print(a[c])
    c=c+1

