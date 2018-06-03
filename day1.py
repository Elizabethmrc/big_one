# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:35:35 2018

@author: fydf
"""
import urllib.request as  r


while 1:
    city_p=input("请输入查询城市拼音：")
    print(city_p)
    address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    info=r.urlopen(address.format(city_p)).read().decode('utf-8','ignore')
    print(info)
    import json
    wdata=json.loads(info)
    print(wdata)
    print(address.format(city_p))
    print("1、查看当前城市天气，2、查看其他城市天气，3、保存当前城市")
    mennu=input("请输入菜单号：")
    if mennu=="1":
        print("查看当前城市天气")
        print("当前气候："+str(wdata["weather"][0]["description"]))
        print("当前温度："+str(wdata["main"]["temp"]))
        print("当天最大温度"+str(wdata["main"]["temp_max"]))
        print("当天气压："+str(wdata["main"]["pressure"]))
        break
    if mennu=="2":
        print("查看其他城市天气")
    if mennu=="3":
        print("保存当前城市")
        break
    


        