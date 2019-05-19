#!/usr/bin/python
#-*- coding:utf-8 -*-
import re
# a='wqe\nfwq123qfwqw'
a='wqe\nQfwq123qfQwqw'
# 只匹配指定的内容给正则条件加括号
# p=re.compile('q(.*?)q')
# .是可以匹配字符，除换行符（\n）之外的任意字符，输出结果为：['123']
# 但是 re.S给.加功能，可以匹配换行符在内的任意字符，输出结果为:['e\nfw', 'fw']
# p=re.compile('q(.*?)q',re.S)
# 正则区分大小写，但是re.I 给条件加功能，不区分大小写，输出结果为：['fw', 'f']
p=re.compile('q(.*?)q',re.I)
# complie 编译
# p=re.compile('[0-9]{2,4}')
#贪婪模式：尽可能匹配更多的内容，输出结果为['efwq123fw']
# p=re.compile('q(.*)q')
#非贪婪模式:尽可能匹配少的内容，输出结果为['efw']
# p=re.compile('q(.*?)q')
# findall 从某一个地方查找符合正则的字符串
# findall 用法1：正则 如果有两个参数：1.正则条件  2.查找范围
# c=re.findall(p,a)
# c=re.findall('[0-9]{2,4}',a)
# findall 用法2：条件 如果有一个参数的时候，是查找范围
c=p.findall(a)
print(c)

# 匹配前边和后边的
import re
a='qwer123122'
p=re.compile('(.*)e.*?2(.*)')
c=p.findall(a)
print(c)
