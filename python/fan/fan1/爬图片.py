#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
class Tupian(object):
    def 发送请求(self,page):
        url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def 过滤(self,abc):
        lie=[]
        patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
        items=patt.findall(abc)
        for i in items:
            new_a=re.compile(r'img src="(.*?)"',re.S)
            item=new_a.findall(i)
            lie.extend(item)
        print(lie)
        return lie
    def save(self,shu):
        global bc
#   图片是个链接，请求图片的链接，将相应保存
        for h,j in enumerate(shu):
            res=requests.get('https:'+j)
#    接收响应的结果只能用content
            qq=res.content
            with open('{}.jpg'.format(bc),'ab') as f:
                f.write(qq)
            bc+=1
tu=Tupian()
bc=0
for i in range(1,4):
    b=tu.发送请求(i)
    bb=tu.过滤(b)
    cc=tu.save(bb)
print(bc)
