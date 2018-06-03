# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:46:00 2018

@author: fydf
"""

import urllib.request as r

url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'

while 1:
    
    city_p=input("请输入你所查询城市的拼音：")
    info=r.urlopen(url.format(city_p)).read().decode('utf-8','ignore')

    print(info)

    import json
    sdata=json.loads(info)
    print(sdata)

    number=input("请输入你要查询的菜单号:1、查看最近几天全部天气|2、查询其他城市天气情况|3、查看指定日期天气的情况")
    if number=="1":
        for i in range(1,40):
            print("当前日期："+str(sdata["list"][i-1]["dt_txt"])+"当前天气："+str(sdata["list"][i-1]["weather"][0]["description"])+"当前温度："+str(sdata["list"][i-1]["main"]["temp"])+"当前最高温度："+str(sdata["list"][i-1]["main"]["temp_max"]))
        break        
    if number=="2":
        print("查看其他天气情况")
    if number=="3":
        j=int(input("请输入你查询第几天:"))-1
        for n in range(0,7):
            print("当前日期："+str(sdata["list"][j*7+n]["dt_txt"])+"当前天气："+str(sdata["list"][j*7+n]["weather"][0]["description"])+"当前温度："+str(sdata["list"][j*7+n]["main"]["temp"])+"当前最高温度："+str(sdata["list"][j*7+n]["main"]["temp_max"]))
        
        break
        
        
    



