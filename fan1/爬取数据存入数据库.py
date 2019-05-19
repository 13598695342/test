#!/usr/bin/python
#-*- coding:utf-8 -*-
from xlutils.copy import copy
import re
import requests
import xlrd
import xlwt
import pymysql
conn=pymysql.connect(host='192.168.1.117',user='root',passwd='123456')
my=conn.cursor()
class Excel(object):
    def send(self):
        url='https://movie.douban.com/top250?start={}&filter='.format(25)
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html

    def filtration(self,html):
        dire=[]
        value=[]
        movie_name=re.compile(r'<img width="100" alt="(.*?)" src=',re.S)
        mov=movie_name.findall(html)
        print(mov)
        dircetor=re.compile(r'<p class="">(.*?)</p>',re.S)
        f1=dircetor.findall(html)
        for i in f1:
            new_dircetor=re.compile(r'导演: (.*?)&nbsp',re.S)
            f2=new_dircetor.findall(i)
            dire.extend(f2)
        score=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>',re.S)
        sco=score.findall(html)
        star=re.compile(r'<div class="star">(.*?)</div>',re.S)
        f4=star.findall(html)
        for j in f4:
            val=re.compile(r' <span>(.*?)</span>',re.S)
            f5=val.findall(j)
            value.extend(f5)
        return list(zip(mov,dire,sco,value))


exc=Excel()
b=exc.send()
bb=exc.filtration(b)
# try:
#     my.execute('create database pa;')
# except:
my.execute('use pa;')

my.execute('create table papa(movie char(35),autor text,score float(2,1),people char(35));')
for q,w,e,r in bb:
    my.execute('insert into papa values("{}","{}","{}","{}");'.format(q,w,e,r))
my.execute('select * from papa')
b=my.fetchall()
print(b)
conn.close()


