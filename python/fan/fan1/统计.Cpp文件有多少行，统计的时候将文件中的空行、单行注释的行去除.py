#!/usr/bin/python
#-*- coding:utf-8 -*-
# with open(r'c:\Users\fansl\Desktop\新建文本文档.txt','r',encoding='ansi') as f:
#  with open('a.txt','w',encoding='ansi') as _f:
#     for i in f:
#         if i.startswith('#'):
#             continue
#         d=i.split()
#         if len(d)==0:
#             continue
#         else:
#             _f.write(i)
# with open('a.txt','r',encoding='ansi') as n:
#     j=[]
#     while True:
#         a=n.readline()
#         if a=='':
#             break
#         j.append(a)
#     print(len(j))
with open(r'c:\Users\fansl\Desktop\新建文本文档.txt','r',encoding='utf-8') as  a:
    b=a.readlines()
    d=0
    for i in b:
        if i.startswith('#') or not i.split():
            d=d+1
    print(len(b)-d)
    print(d)
