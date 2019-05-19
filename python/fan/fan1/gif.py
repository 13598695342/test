#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
import json
# 爬取的任何资源，html文件，爬取文字，图片都是静态网页
# 动态网页，资源不在html文件中，实时刷新，例如京东网站
# 加载网页资源：javascript，ajax
# json：轻量级的数据传输格式 传言json可能取代html因为他比较快
url='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=13&city=410200&geoobj=114.289449|34.775662|114.441578|34.820781&keywords=洗浴中心'
res=requests.get(url)
qwe=res.text
asd=json.loads(qwe)
# 将json格式转换成字典
# qwe=json.dumps(asd)
# 将字典转换成json格式
print(asd['data']['poi_list'][1]['cityname'])
