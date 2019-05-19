#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
class douban(object):
    def send(self):
        url='https://movie.douban.com/cinema/nowplaying/kaifeng/'
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def filtration(self,html):
        lie=[]
        f=re.compile(r'data-title="(.*?)"',re.S)
        title=f.findall(html)
        ff=re.compile(r'<li class="poster">(.*?)</a>',re.S)
        title1=ff.findall(html)
        for i in title1:
            fff=re.compile(r'<img src="(.*?)"')
            title2=fff.findall(i)
            lie.extend(title2)
        return title,lie
    def save(self,title,lie):
        for h,j in enumerate(lie):
            res=requests.get(j)
#    接收响应的结果只能用content
            qq=res.content
            z=title[h]
            with open('{}.jpg'.format(z),'ab') as f:
                f.write(qq)
dou=douban()
b=dou.send()
bb,aa=dou.filtration(b)
dou.save(bb,aa)
