#!/usr/bin/python
#-*- coding:utf-8 -*-
# 质数之和：
def zhi(a,b):
    sum=0
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum=sum+i
    return sum
#因数之和
def yin(b):
    for i in range(1,b+1):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum=sum+j
        if sum==i:
            print(i)
    return i
#九九乘法表
def jiu(b):
    for i in range(1,b+1):
        for j in range(1,i+1):
            print('{}*{}={}'.format(i,j,i*j),end='\t')
        print()
#不用int将字符串变成整数
# a='1234454120'
# a=a[::-1]
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             c+=j*10**i
# print(c)
#任意四个数字，组成不想同的三位数
def san(a,b,c,d):
    f=[]
    n=[a,b,c,d]
    for i in n:
        for j in n:
            for e in n:
                v=i*100+j*10+e*1
                f.append(v)
    b=list(set(f))
    b.sort()
    return  b
#判断字符串是否回文
def hui(b):
    c=len(b)
    for i in range(len(b)//2):
        if b[i]!=b[len(b)-i-1]:
            print('不是回文')
            break
    else:
        print('是回文')
#冒泡排序
# b=[123,43,654,765,87,12,3,6,8967,65]
# for i in range(1,len(b)):
#     for j in range(1,len(b)):
#         if b[j-1]>b[j]:
#             b[j-1],b[j]=b[j],b[j-1]
#             print(b)
#水仙花数
def shui(n,m):
    for i in range(n,m):
        a=i//100
        b=i//10%10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)
#t统计文件有多少行,统计时将文件中的空行注释去除
# with open(r'c:\Users\fansl\Desktop\新建文本文档.txt','r',encoding='ansi') as f:
#     b=f.readlines()
#     sum=0
#     for i in b:
#         if i.startswith('#') or not i.split():
#             sum=sum+1
#     print(len(b)-sum)
#     print(sum)
#将十进制转十六进制
# def shiliu(b):
#     a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#     f=''
#     while True:
#         c=b%16
#         b=b//16
#         f=f+a[c]
#         if b==0:
#             break
#     return f[::-1]
#阶乘之和
# def jie(a,b):
#     sum=0
#     for i in range(a,b+1):
#         b=1
#         for j in range(1,i+1):
#             b=b*j
#         sum+=b
#     return sum
# a='noob'
# for i in range(len(a)//2):
#     if a[i]!=a[len(a)-i-1]:
#         print('不是回文')
#         break
# else:
#     print('是回文')
import a
Lei=a.Xiaona()
Lei.hanshu()
x=a.Leiming()
x.han()



