#!/usr/bin/python
#-*- coding:utf-8 -*-
from xlutils.copy import copy
import requests
import json
import re
import pymysql
import xlwt
import xlrd
import smtplib
import email.mime.multipart
import email.mime.text
class Zhilian(object):
    def response(self):
        url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=695&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.65946716&x-zp-page-request-id=70b8cb49b7654ad98d7c813f753b4be5-1553945815480-560621'
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/66.0'}
        res=requests.get(url)
        qwe=res.text
        asd=json.loads(qwe)
        return asd

    def feltration(self,asd):
        shijian=[]
        chengshi=[]
        gongzi=[]
        jingyan=[]
        gongsi=[]
        gongzuo=[]
        num=asd['data']['results']
        n=len(num)
        for i in range(n):
            time=asd['data']['results'][i]['updateDate']
            shijian.append(time)
            city=asd['data']['results'][i]['city']['display']
            chengshi.append(city)
            salary=asd['data']['results'][i]['salary']
            gongzi.append(salary)
            exp=asd['data']['results'][i]['workingExp']['name']
            jingyan.append(exp)
            company=asd['data']['results'][i]['company']['name']
            gongsi.append(company)
            jobname=asd['data']['results'][i]['jobName']
            gongzuo.append(jobname)
        return list(zip(shijian,chengshi,gongzi,jingyan,gongsi,gongzuo))

    def wexcel(self,neirong):
        try:
            xr=xlrd.open_workbook('zuoye.xls')
            new_xr=copy(xr)
            sheet1=new_xr.get_sheet(0)
            rows=sheet1.nrows()
            i=rows+1
            for q,w,e,r,t,y in neirong:
                sheet1.write(i,0,'q')
                sheet1.write(i,1,'w')
                sheet1.write(i,2,'e')
                sheet1.write(i,3,'r')
                sheet1.write(i,4,'t')
                sheet1.write(i,5,'y')
                i+=1
            new_xr.save('zuoye.xls')
        except:
            xl=xlwt.Workbook()
            sheet=xl.add_sheet('sheet1')
            sheet.write(0,0,'更新时间')
            sheet.write(0,1,'城市')
            sheet.write(0,2,'薪资')
            sheet.write(0,3,'经验')
            sheet.write(0,4,'公司')
            sheet.write(0,5,'职位')
            i=1
            for q,w,e,r,t,y in neirong:
                sheet.write(i,0,'q')
                sheet.write(i,1,'w')
                sheet.write(i,2,'e')
                sheet.write(i,3,'r')
                sheet.write(i,4,'t')
                sheet.write(i,5,'y')
                i+=1
            xl.save('zuoye.xls')
zl=Zhilian()
resp=zl.response()
felt=zl.feltration(resp)
print(felt)
xls=zl.wexcel(felt)
