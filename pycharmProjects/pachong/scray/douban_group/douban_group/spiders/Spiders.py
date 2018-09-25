# -*- coding : utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
import re,time
import douban_group.items
from scrapy import Request


class Spiders(Spider):
	name='douban_group'
	allowed_domains=['douban.com']
	start_urls=[
		'https://www.douban.com/group/ProductManager/',
	]


	def  __get_id_from_group_url(self,url):
		m=re.search("^https://www.douban.com/group/([^/]+)/$",url)

		if (m):
			return m.group(1)
		else:
			return 0

	def parse(self,response):
		self.log("fetch group home page: %s" % response.url)

		hxs=HtmlXPathSelector(response)


		item=douban_group.items.DoubanGroupItem()

		item['groupName']=hxs.select('//*[@id="group-info"]/h1/text()').re('^\s+(.*)\s+$')[0]
		item['groupUrl']=response.url

		group_id=self.__get_id_from_group_url(response.url)

		member_url='https://www.douban.com/group/%s/members' % group_id
		member_text=hxs.select('//a[contains(@href,"%s")]/text()' % member_url).re('(\d+)')

		item['totalNumber']=member_text[0]

		groups=hxs.select('//div[contains(@class,"group-list-item")]')

		for group in groups:
			url=group.select('div[contains(@class,"title")]/a/@href').extract()[0]
			yield Request(url)
		
		time.sleep(1)
		yield item