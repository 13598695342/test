#!/usr/bin/python
#-*- coding:utf-8 -*-
class Object1():
    def jiu(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('{}*{}={}'.format(i,j,i*j),end='\t')
            print()
    def xu(self,a):
        for i in range(1,len(a)):
            for j in range(1,len(a)):
                if a[j-1]>a[j]:
                    a[j-1],a[j]=a[j],a[j-1]
        print(a)
    def hua(self,b,a=100):
        for i in range(a,b+1):
            a=i//100
            b=i%10//10
            c=i%10
            if a**3+b**3+c**3==i:
                print(i)
    def zhishu(self):
        sum=0
        for i in range(2,100):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                sum=sum+i
        print(sum)
    # def jiecheng(self):
lei=Object1()
lei.zhishu()
