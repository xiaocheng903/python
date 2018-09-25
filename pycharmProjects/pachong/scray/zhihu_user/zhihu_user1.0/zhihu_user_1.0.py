#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import http.cookiejar
import requests
import mysql.connector

class Login(object):
    def __init__(self):
        pass

    #获取_xsrf的值
    def collect(self):
        reponse=urllib.request.urlopen('https://www.zhihu.com/#signin')
        data=reponse.read().decode()
        soup=BeautifulSoup(data,'html.parser')

        link=soup.find_all('input')

        link=str(link[0])
        link=link[41:73]
        return link
 
    #post相关的数据
    def post(self):
        cj = http.cookiejar.CookieJar()
        pro = urllib.request.HTTPCookieProcessor(cj)
        opener = urllib.request.build_opener(pro)
        urllib.request.install_opener(opener)
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        header = {'User-Agent': user_agent}


        postdata = urllib.parse.urlencode({
            '_xsrf':self.collect(),
            'password':'a12345',
            'phone_num':'15598438801'
            
        })

        postdata = postdata.encode('utf-8')
        url = 'https://www.zhihu.com/login/phone_num'
        req = urllib.request.Request(url,postdata,headers=header)
        result=opener.open(req)
        
        #获取json中的数据,并插入数据库，URL除第一个为均为自动获取
        conn=mysql.connector.connect(user='root',password='',database='spider')
        cursor=conn.cursor()
        m=1
        rr=requests.get('https://www.zhihu.com/api/v4/members/evilcos/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20',cookies=cj,headers=header).json()
##        print(rr)
        try:
            while not rr['paging']['is_end']:
                for user in rr['data']:
                    name=user['name']
                    headline=user['headline']
                    user_url=urllib.parse.urljoin('https://www.zhihu.com/people/',user['id'])
                    answer_count=user['answer_count']
                    articles_count=user['articles_count']
                    follower_count=user['follower_count']
                    user_id=user['id']
                    user_avatar_url=user['avatar_url']
                    cursor.execute('insert ignore into zhihu_user(id, user_name,user_headline,user_url,user_answer_count,user_articles_count,user_follower_count,user_id) values(%s,%s,%s,%s,%s,%s,%s,%s)',[m,name,headline,user_url,answer_count,articles_count,follower_count,user_id])
                    conn.commit()
                    #将用户的头像图片放在相应的文件夹中
##                    t=str(m)+'.jpg'
##                    pic=urllib.request.urlopen(user_avatar_url)
##                    content=pic.read()
##                    ff=open(t,'wb')
##                    ff.write(content)
##                    ff.close()
                    print('已经插入'+str(m)+'条')
                    m=m+1
                url=rr['paging']['next']
                rr=requests.get(url,cookies=cj,headers=header).json()
            cursor.close()
            conn.close()
        except Exception as e:
            print('error:',e)

if __name__=='__main__':
    ff=Login()
    ff.post()

