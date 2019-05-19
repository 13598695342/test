#!/usr/bin/python
#-*- coding:utf-8 -*-
# sum=0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         print(i)
#         sum=sum+i
# print(sum)
def ccc1(b):
    sum=0
    for i in range(2,b+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
            sum=sum+i
    return sum,i
# a=lambda x:x+2
# print(__name__)
# if __name__=='__main__':
#     print('hello')
ccc1(5)
