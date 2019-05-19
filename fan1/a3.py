#!/usr/bin/python
#-*- coding:utf-8 -*-
#if True:
 #   print('nihao')
#else:
  #  print('een')
#print(type(1234),end="")
#print('nihao',end="")
#a='qrtwqte'
#print(a*2)
#print(a + 'test')
#isinstance(1,int)
#print('nihao')
#a=input('qing')
#print('a=',end="")
#print(a,end="")
#print('ru\noob')
#print(r'ru\noob')
#list=['qeqe',1323,345,'fgh']
#tinylist=['fdsafsa',123]

#print(list)
#print(list[0])
#print(list[1:3])
#print(list[2:])
#print(tinylist*2)
#print(list + tinylist)
#tuple=('eqreqr',13123,6545,342.3454)
#tinytuple=('qeqr',13,'e231')

#print(tuple)
#print(tuple[0])
#print(tuple[2:])
#print(tuple[1:3])
#print(tinytuple*2)
#print(tuple + tinytuple)
# a='qwTqr{}q123{}'
#b=a.replace('q','547')
#b=a.split('qr')
#print(a)
#c='-'.join(b)
#print(c)
# b= ['133','qe','qweq','eeee']
#c='123%s,%d' %(90,90)
# print(b)
# print(b[1:])
# print(b[:1])
# print(b[1:3])
# print(b[::2])
# c=b.index('133')
# print(c)
#c=b.strip()
#print(c)
# b.append(100)
# print(b)
# a='  qwe%srT%d  '
# b=a.upper()
# print(b)
# b=a.swapcase()
# print(b)
# b=a.replace('q','123')
# b=a.split('e')
# c='-'.join(b)
# print(c)
# b=int(input('请输入'))
# c=a.format(age='weq',name=b)
# c=a %('dadsa',1321)
# print(c)

# b=a.rstrip()
# print(a)
# # print(b)
# a=['dada',1321,'afdsa',1314,1321,[100,[300,400],200]]
# import  copy
# b=copy.deepcopy(a)
# a.append(133)
# a[-1].append(120)
# print(a)
# print(b)
# a={23,43,56,78}
# a.pop()
# print(a)
# a={'name':'xiaoming','age':[20,45,56]}
# b={'desf':123}
# a.update(b)
# a=
# a=str(a)
# if 't'  in a :
#   print(a)
# elif 'y' in a :
#     print('byebye')
# elif 'p' in a :
#     print('ene')
# else :
#     print('nihao')
# a=(input('>>>'))
# a=int(a)
# if  90<=a<=100 :
#     print('优秀')
# elif 70<=a<90 :
#     print('一般')
# elif 60<=a<70 :
#     print('及格')
# elif 0<=a<60 :
#     print('不及格')
# else :
#     print('请重新输入')

# a=input('>>>')
# a=int(a)
# if a%2==0 :
#     if a%3==0 :
#         print('helloword')
# elif a%2==0:
#     print('hello')
# elif a%3==0:
#     print('word')
# else :
#     print(123)



# a=input('>>>')
# if (a.startswith('a') or a.startswith('A')) and a.endswith('c') :
#     print(110)
# elif a.startswith('a'):
#     print(120)
# # elif a.endswith('c'):
# print(130)
# else:
#    print(250)
# a=input('>>>')
# b=a[0]
# c=a[-1]
# if b == 'a' or b == 'A' :
#     if c == 'c':
#         print(110)
# elif b == 'a':
#     print(120)
# elif c == 'c':
#     print(130)
# else:
#     print(250)

# a=input('>>>')
# if (a.startswith('a') or a.startswith('A')) and a.endswith('c') :
#     print(110)
# elif a.startswith('a'):
#     print(120)
# elif a.endswith('c'):
#     print(130)
# else:
#     print(250)
# a=(12,23,34)
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)
# print(sum(range(101)))
# a=0
# for i in range(1,10,2):
#     if i==7 :
#         continue
#     else:
#         print(i)
# else :
#     print('hello')

# a=0
# for i in range(1,100):
#     if i%2==0:
#         a=a-i
#     else:
#         a=a+i
# print(a)
# import  random
# a = random.randrange(1,10)
# print(a)
# for i in range(3):
#     j=random.randrange(1,10)
#     if j > a :
#         print('大','还剩{}次'.format(2-i))
#     elif j < a :
#         print('小','还剩{}次'.format(2-i))
#     elif j == a :
#         print('正确')
#         break
# else:
#     print('废物')
# a=['dinanao','shouji','jisuanji']
# for i,j in enumerate(a):
#     print(i+1,j)
# a=3
# while a>=2:
#     if a==2:
#         break
#     print('hello')
#     a-=1
# else:
#     print(123)
# a=[12,212,23,12]
# b=int(input('>>>>'))
# # while :
# #     print(a[b])
# #     b+=1
# if b>20:
#     a=b-20
#     for i in range(a):
#         print('nihao')
# # sum=0
# # b=1
# # while b<=100 :
# #      sum=sum+b
# #      b += 1
# # print(sum)
# #所有的函数没有调用就不会执行
#
# def nihao(b):
#     a=0
#     c=[]
#     for i in range(1,b+1):
#         a=a+i
#         c.append(a)
#     print(c)
#     return 12
# #d=[]
# # for i in range(11):
# nihao(10)
# print(nihao(10))
# #     d.append(c)
# # print(d)
# #     c=[]
# #     for i in b:
# #         if i not in c:
# #             c.append(i)
# #     print(c)
# # b=[12,12,12,23,2,0]
#
# for i in range(4):
# a=[]
# for i in range(10):
#     if i > 6:
#         a.append(i)
# print(a)
# a=[ '{}*{}={}'.format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]
# print(a)
# a=lambda x,y :x/y
# print(a(3,4))
# print(a(3,4))
# d=open(r'C:\Users\fansl\Desktop\新建文本文档.txt','r',encoding='ansi')
# with open('a.txt','w',encoding='utf-8') as f:#执行with语句时自动执行__enter__函数
#     f.write('qwe')
#     f.write(123)#执行报错就会自动执行__exit__函数一般不用写f.close
#     f.close()
# # i=1
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print(d.write('{}*{}={}\t'.format(i,j,i*j)))
# #     print(d.write('\n'))
# #
# # d.close()
# print(d.readline())
# print(d.readline())
# print(d.readlines())
#
# d.close()
# import pprint
#
# productList = [('Iphone 8', 10000),
#                ('GTX2080', 8000),
#                ('Z7KP7-GT', 6000),
#                ('Mac pro', 15000),
#                ('Honor 10', 2800),
#                ('Iphone XR', 12000),
#                ('Mi 8', 2999)
#                ]
#
# shoppingList = []
#
# print('输入你的工资:')
# salary = input()
# if not salary.isdigit():
#     print('请输入整数')
# else:
#     salary = int(salary)
#     while True:
#         for index, item in enumerate(productList):
#             print(index + 1, item)
#         print('输入你要买的商品的序号：')
#         userWant = input()
#         if userWant.isdigit():
#             userWant = int(userWant)
#             if userWant <= len(productList) and userWant > 0:
#                 print('你要购买的是：', productList[userWant - 1][0])
#                 if salary >= productList[userWant - 1][1]:
#                     shoppingList.append(productList[userWant - 1][0])
#                     salary -= productList[userWant - 1][1]
#                     print('你已经购买了' + productList[userWant - 1][0] + ', 你的余额为 ' + str(salary))
#                 else:
#                     print('对不起，你的余额不足！请努力工作吧！')
#                     print('你当前所购买的商品为：')
#                     for brought in shoppingList:
#                         pprint.pprint(brought)
#                     print('你当前余额为：', salary)
#                     exit()
#             else:
#                 print('你输入的商品序号有错，请重新输入')
#         elif userWant == 'q':
#             print('-----------Shopping List----------')
#             for brought in shoppingList:
#                 pprint.pprint(brought)
#             print('你的余额为 ', salary)
#             exit()
#         else:
#             print('Invalid input！！！')
# for i in range(1,10):
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             sum=sum+j
#     if sum==i:
#         print(i)
# import ccc
# print(ccc.ccc(5))
# import random
# from ccc import *
# print(ccc1(10))
# print(a(10))
# a='123244'
# a=a[::-1]
# c=0
# for i in range(0,len(a)):
#     for j in range(1,10):
#         if str(j)==a[i]:
#             c+=j*10**i
# print(c)
# a=16
# b=float(a**0.5)
# print('%0.2f的平方根为%0.2f' %(a,b))
# try:
#     a=20
#     print(a+b)
# except TypeError as e:
#     print(e)
# finally:
#     print('nihao')
# a=int(input('>>>'))
# if a>3:
#    raise TypeError('hello')
# else:
#    raise NameError('123')
while True:
    try:
        x=int(input('请输入要转换什么进制的数：'))
        if x==2 or x==8 or x==16:
            while True:
                num_d=input('请输入一个%s进制数：'% x)
                if num_d=='exit':
                    break
                n=len(num_d)
                num=0
                try:
                    for i in num_d:
                        if i=='A':
                            i=10
                        if i=='B':
                            i=11
                        if i=='C':
                            i=12
                        if i=='D':
                            i=13
                        if i=='E':
                            i=14
                        if i=='F':
                            i=15
                        if 0<=int(i)<x:
                            num+=int(i)*x**(n-1)
                            n-=1
                        else:
                            print('输入有误')
                            break
                except:
                    print('输入有误')
                    break
                print('转换的十进制数为：',num)
            else:
                print('输入有误')
                break
    except:
        print('输入有误')
