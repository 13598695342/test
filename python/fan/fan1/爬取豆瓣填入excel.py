#!/usr/bin/python
#-*- coding:utf-8 -*-
from xlutils.copy import copy
import re
import requests
import xlrd
import xlwt
class Excel(object):
    def send(self,page):
        url='https://movie.douban.com/top250?start={}&filter='.format(page)
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

    def sav(self,lis):
        try:
            rea=xlrd.open_workbook('movie.xls')
            read=rea.sheets()[0]
            hang=read.nrows
            new_rea=copy(rea)
            new_sheet=new_rea.get_sheet(0)
            z2=hang+1
            for q,w,e,r in lis:
                new_sheet.write(z2,1,q)
                new_sheet.write(z2,2,w)
                new_sheet.write(z2,3,e)
                new_sheet.write(z2,4,r)
                z2+=1
            new_rea.save('movie.xls')
        except:
            wri=xlwt.Workbook()
            sheet=wri.add_sheet('movie')
            sheet.write(1,1,'电影名称')
            sheet.write(1,2,'导演')
            sheet.write(1,3,'评分')
            sheet.write(1,4,'评价')
            z1=2
            for q,w,e,r in lis:
                sheet.write(z1,1,q)
                sheet.write(z1,2,w)
                sheet.write(z1,3,e)
                sheet.write(z1,4,r)
                z1+=1
            wri.save('movie.xls')
exc=Excel()
for i in range(0,125,25):
    b=exc.send(i)
    bb=exc.filtration(b)
    exc.sav(bb)





