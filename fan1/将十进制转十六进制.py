#!/usr/bin/python
#-*- coding:utf-8 -*-
# a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# # a=[str(i) for i in range(0,10)]
# # b=[chr(i) for i in range(65,71) ]
# # a=a + b
# while True:
#     b=int(input('请输入一个十进制数'))
#     if b<0:
#         break
#     f=''
#     while True:
#         c=b%16
#         b=b//16
#         f+=a[c]
#         if b==0:
#             break
#     print(f[::-1])

a=[str(i) for i in range(10)]+[chr(i) for i in  range(97,103)]
b=int(input('>>>'))
f=[]
while True:
    c=b%16
    b=b//16
    f.append(a[c])
    if b==0:
        break
f.reverse()
f=''.join(f)
print('0x{}'.format(f))
