#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
import mysql.connector
import xlrd

class CET(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.header = {'User-Agent': self.user_agent,
                       'Host':'www.chsi.com.cn',
                       'Referer':'http://www.chsi.com.cn/cet/'}
        
    def collect(self,i):
        excel=xlrd.open_workbook('F:\CET\CET.xlsx')
        sheet=excel.sheets()[0]
        row_data=sheet.row_values(i)
        return row_data[5],row_data[6]

    def post(self,user_id,user_name):
        url='http://www.chsi.com.cn/cet/query?zkzh='+user_id+'&xm='+user_name
        r=requests.get(url,headers=self.header)
##        r=requests.get('http://www.chsi.com.cn/cet/query',params={'zkzh':user_id,'xm':user_name},headers=self.header)
        print(r.url)
        return r.text

    def scrapy(self,data):
        soup=bs(data,'html.parser')
        links=soup.find_all('td')
        # 4 6 8 10 12
        n_data=[]
        i=4
        while i<13:
            n_data.append(links[i].get_text().strip())
            i=i+2
        return n_data

    def stored(self,data,i,user_id,user_name):
        #在这里采用直接将数据插入到数据库内  也可以直接插入到Excel表格中
        conn=mysql.connector.connect(user='root',password='',database='spider')
        cursor=conn.cursor()
        cursor.execute('insert ignore into cet(id,user_name,user_id,zongfen,tingli,yuedu,xiezuo,cet) values(%s,%s,%s,%s,%s,%s,%s,%s)',[i,user_name,user_id,int(data[1]),int(data[2]),int(data[3]),int(data[4]),data[0]])
        conn.commit()
        cursor.close()
        conn.close()
        
    def spider_main(self):
        i=1
        try:
            while i<100:
                user_id,user_name=self.collect(i)
                f=self.post(user_id,user_name)
                a=self.scrapy(f)
                self.stored(a,i,user_id,user_name)
                i=i+1
        except Exception as e:
            print(e)


if __name__=='__main__':
    obj_cet=CET()
    obj_cet.spider_main()
