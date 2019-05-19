#!/usr/bin/python
#-*- coding:utf-8 -*-
a=input('请输入字符串：')
# b=0
# while b<(len(a)//2):
#     if a[b]==a[len(a)-b-1]:
#         count=1
#         b=b+1
#     else:
#         count=0
#         break
# if count==1:
#     print('huiwen')
# elif count==0:
#     print('no')
b=len(a)
for i in range(b//2):
    if a[i] != a[-i-1]:
        print('不是回文')
        break
else:
    print('是回文')
