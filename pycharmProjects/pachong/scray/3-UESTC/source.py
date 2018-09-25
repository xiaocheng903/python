#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


class Source(object):
    def __init__(self):
        self.data={}

    def clsource(self):
        req=urllib.request.urlopen(self.choice())
        return req.read().decode()

    def output(self):
        data=self.clsource()
        soup = BeautifulSoup(data, 'html.parser')
        links=soup.find_all('td')
        datas = []
        a = 3
        while a < len(links):
            datas.append(links[a].get_text().strip())
            a = a + 5
        i = 0
        while i < len(datas):
            print('科目：', datas[i])
            i = i + 1
            print('成绩', datas[i])
            i = i + 1



    def choice(self):
        url=''
        datetime=input('请输入你要查询的学期（例如：2014-2015 1）：')
        if datetime=='2014-2015 1':
            url='http://eams.uestc.edu.cn/eams/teach/grade/course/person!search.action?semesterId=43&projectType='
        elif datetime=='2014-2015 2':
            url='http://eams.uestc.edu.cn/eams/teach/grade/course/person!search.action?semesterId=63&projectType='
        elif datetime=='2015-2016 1':
            url='http://eams.uestc.edu.cn/eams/teach/grade/course/person!search.action?semesterId=84&projectType='
        elif datetime=='2015-2016 2':
            url='http://eams.uestc.edu.cn/eams/teach/grade/course/person!search.action?semesterId=103&projectType='
        elif datetime=='2016-2017 1':
            url='http://eams.uestc.edu.cn/eams/teach/grade/course/person!search.action?semesterId=123&projectType='
        else :
            print('对不起，没有当前学期的成绩！')
        return url

