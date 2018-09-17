# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# -*- coding:utf-8 -*-
# project:douban_group
# file:item.py
# author:Paul_wang

import scrapy

class DoubanGroupItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	groupName=scrapy.Field()
	groupUrl=scrapy.Field()
	totalNumber=scrapy.Field()