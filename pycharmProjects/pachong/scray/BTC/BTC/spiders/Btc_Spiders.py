# -*- coding: utf-8 -*-


from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
import re,time
from time import strftime
import BTC.items
from scrapy import Request
from datetime import datetime
import json

class BtcSpiders(Spider):
	name='BTC'
	allowed_domains=['btcchina.com']
	start_urls=[
			'https://data.btcchina.com/data/ticker?market=all',
	]

	def _get_sys_time(self):
		#now_time=strftime("%Y-%m-%d %H:%M:%S",gmtime())
		now_time=datetime.now()
		now_time=now_time.strftime("%Y-%m-%d %H:%M:%S")
		return now_time

	def parse(self,response):
		url=response.url
		#url='https://data.btcchina.com/data/ticker?market=all'

		#hxs=HtmlXPathSelector(response)sss
		hxs=json.loads(response.body_as_unicode())

		item=BTC.items.BtcItem()

		item['time']=self._get_sys_time()
		item['now']=hxs['ticker_btccny']['buy']
		item['height']=hxs['ticker_btccny']['high']
		item['low']=hxs['ticker_btccny']['low']
		yield item
		yield Request(url)
