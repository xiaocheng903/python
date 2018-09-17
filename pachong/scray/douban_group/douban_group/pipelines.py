# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
##import json
class DoubanGroupPipeline(object):

	def __init__(self):
		self.host='127.0.0.1'
		self.dbname='spider'
		self.user='root'
		self.password=''
		self.conn=mysql.connector.connect(user=self.user,password=self.password,database=self.dbname)
		self.cursor=self.conn.cursor()

	def process_item(self, item, spider):
		self._push_data_to_mysql(item)
		return item

	def _push_data_to_mysql(self,item):
		
		name=item['groupName']
		url=item['groupUrl']
		number=item['totalNumber']
		self.cursor.execute('insert ignore into douban_group (name,url,number) values (%s,%s,%s)',[name,url,number])
		self.conn.commit()

	def spider_closed(self,spider):
		self.cursor.close()
		self.conn.close()


class JsonWithPipeline(object):
	def __init__(self):
		self.file = open('info.json', 'w', encoding='utf-8')#保存为json文件
	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"#转为json的
		self.file.write(line)#写入文件中
		return item
	def spider_closed(self, spider):#爬虫结束时关闭文件
		self.file.close()
