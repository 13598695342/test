#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
import json
import pymysql
conn=pymysql.connect(host='192.168.2.119',user='root',passwd='123456')
mys=conn.cursor()
# mys.execute('create database zhilian;')
mys.execute('use zhilian;')
# mys.execute('create table zhilian(shijian char(25),chengshi char(25),gongzi char(25),jingyan char(25),gongsi char(25),gongzuo char(25));')

class Zhilian():
    def send(self):
        head='求封'
        url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=695&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.65946716&x-zp-page-request-id=70b8cb49b7654ad98d7c813f753b4be5-1553945815480-560621'
        res=requests.get(url,header=head)
        qwe=res.text
        asd=json.loads(qwe)
        return asd
    def filtration(self,asd):
        shijian=[]
        chengshi=[]
        gongzi=[]
        jingyan=[]
        gongsi=[]
        gongzuo=[]
        for i in range(89):
            time=asd['data']['results'][i]['updateDate']
            shijian.append(time)
            city=asd['data']['results'][i]['city']['display']
            chengshi.append(city)
            # salary=asd['data']['results'][i]['welfare']['salary']
            # gongzi.append(salary)
            exp=asd['data']['results'][i]['workingExp']['name']
            jingyan.append(exp)
            company=asd['data']['results'][i]['company']['name']
            gongsi.append(company)
            jobname=asd['data']['results'][i]['jobName']
            gongzuo.append(jobname)
        return list(zip(shijian,chengshi,jingyan,gongsi,gongzuo))


zhi=Zhilian()
c=zhi.send()
d=zhi.filtration(c)
e=0
for q,w,r,t,y in d:
    e=e+1
    mys.execute('insert into zhilian values("{}","{}","{}","{}","{}","{}");'.format(q,w,e,r,t,y))
    conn.commit()
mys.execute('select * from zhilian')
b=mys.fetchall()
print(b)
conn.close()
