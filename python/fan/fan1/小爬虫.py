# #!/usr/bin/python
# #-*- coding:utf-8 -*-
# #对服务器造成压力：短时间内频繁发送请求
# #      # 一 分析网址
# # #https://www.qiushibaike.com/text/page/1/
# import requests
# import re
# for ii in range(1,13):
#     a='http://www.qiushibaike.com/text/page/{}/'.format(ii)
#     # 简单反防爬程序伪装
#     oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
#     # 发送请求
#     b=requests.get(a,headers=oo)
#     # 接收响应1.text （print(b.text)）2.content 以字节得方式接收（在网页源代码里看编码方式）
#     # 得到网页源代码
#     c=b.content.decode('utf-8')
#     # 二 过滤想要的内容
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     dd=re.compile('<h2>(.*?)</h2>')
#     fff=dd.findall(c)
#     ff1=[]
#     for j in fff:
#         ff1.append(j)
#     f=d.findall(c)
#     print(f)
#     ff=[]
#     for i in f:
#         i=i.replace('<span>','').replace('<br/>','')
#         i=i.strip()
#         ff.append(i)
#     # pp=[]
#     # for j in fff:
#     #     pp.append(j)
#     # print(len(pp))
#     #三 保存过滤的内容
#     with open('a.txt','w',encoding='utf-8') as g:
#         ss=0
#         for i in ff:
#             ss+=1
#             if ss>(len(ff1)-1):
#                 break
#             g.write(ff1[ss])
#             print(ff1[ss])
#             g.write(i+'\n\n')

import requests
import re
import xlwt
for z in range(1,2):
    a='https://www.qiushibaike.com/text/page/{}/'.format(z)
    oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    b=requests.get(a,headers=oo)
    c=b.content.decode('utf-8')
    d=re.compile('<h2>(.*?)</h2>',re.S)
    f=d.findall(c)
    print(type(f))
    dd=re.compile('<div class="content">(.*?)</span>',re.S)
    ff=dd.findall(c)
    print(type(ff))
    gg=[]
    for i in ff:
        i=i.replace('<span>','').replace('<br/>','')
        i=i.strip()
        gg.append(i)
    x=xlwt.Workbook()
    sheet=x.add_sheet('test')
    x.save('a.xls')
    # with open('a.txt','a',encoding='utf-8') as g:
    #     su=0
    #     for j in gg:
    #         if su>(len(f)-1):
    #             su=0
    #         else:
    #             g.write(f[su])
    #             g.write(j+'\n\n')
    #             su+=1
