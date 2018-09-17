# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import json

class BtcPipeline(object):

	def __init__(self):
		self.host='127.0.0.1',
		self.dbname='spider',
		self.user='root',
		self.password='',
		self.conn=mysql.connector.connect(user=self.user,password=self.password,database=self.dbname)
		self.cursor=self.conn.cursor()

	def process_item(self, item, spider):
		self._push_data_to_mysql(item)
		return item

	def _push_data_to_mysql(self,item):
		time=item['time']
		now=item['now']
		height=item['height']
		low=item['low']

		self.conn.commit()

	def spider_closed(self,spider):
		self.cursor.close()
		self.conn.close()

class BtcJsonPipeline(object):
	def __init__(self):
		self.file=open('info.json','a')

	def process_item(self,item,spider):
		line=json.dumps(dict(item))
		self.file.write(line+'\n')
		return item 
		
	def spider_closed(self,spider):
		self.file.close()