#!/usr/bin/python
#-*- coding:utf-8 -*-
# a=int(input('请输入'))
# b=int(input('请输入'))
# c=int(input('请输入'))
# if (a+b>c) and (a+c>b) and (b+c>a):
#     if (c*c>b*b+a*a) or (a*a>b*b+c*c) or (b*b>a*a+c*c):
#         print('钝角三角形')
#     elif (a*a+b*b==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a) :
#         print('直角三角形')
#     elif (c*c<b*b+a*a) or (a*a<b*b+c*c) or (b*b<a*a+c*c):
#         print('锐角三角形')
#     else:
#         print('不规则三角形')
# else:
#     print('不是三角形')



a=int(input('请输入边长'))
b=int(input('请输入边长'))
c=int(input('请输入边长'))
l=[]
l.append(a)
l.append(b)
l.append(c)
l.sort()
if (l[0]+l[1]>l[2]):
    if l[0]**2+l[1]**2>l[2]**2:
        print('锐角三角形')
    if l[0]**2+l[1]**2==l[2]**2:
        print('直角三角形')
    if l[0]**2+l[1]**2<l[2]**2:
        print('钝角三角形')
else:
    print('不是三角形')
