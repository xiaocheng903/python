#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html_parser,url_manager,html_downloder,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.url_manager=url_manager.UrlManager()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
        self.downloder=html_downloder.HtmlDownloder()

    def craw(self, root_url):
        summ=1
        self.url_manager.add_new_url(root_url)
        while self.url_manager.has_new_url():
            try:
                new_url=self.url_manager.get_new_url()
                print('craw %d:%s'%(summ,new_url))
                html_cont=self.downloder.downlod(new_url)
                new_urls,new_data=self.parser.parser(new_url,html_cont)
                self.url_manager.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if summ==100:
                    break
                summ=summ+1
            except:
                print('craw faild')
        self.outputer.output_html()


if __name__=='__main__':
    root_url='http://baike.baidu.com/view/21087.htm'
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)