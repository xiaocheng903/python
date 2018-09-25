#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import http.cookiejar

class Login(object):
    def clt(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        ##print(data.decode())
        link = soup.find_all('input')
        aa = link[2]
        aa=str(aa)
        return aa[38:-3]

    def post(self):
        cj = http.cookiejar.CookieJar()
        pro = urllib.request.HTTPCookieProcessor(cj)
        opener = urllib.request.build_opener(pro)
        urllib.request.install_opener(opener)
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        header = {'User-Agent': user_agent}

        username=input('请输入你信息门户的账号：')
        password=input('请输入你信息门户的密码：')

        postdata = urllib.parse.urlencode({
            'username': username,
            'password': password,
            'lt': self.clt('http://idas.uestc.edu.cn/authserver/login'),
            'dllt': 'userNamePasswordLogin',
            'execution': 'e1s1',
            '_eventId': 'submit',
            'rmShown': '1'
        })

        postdata = postdata.encode('utf-8')
        url = 'http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F'
        req = urllib.request.Request(url, postdata, headers=header)
        result=opener.open(req)


