#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    def parser(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url, soup)
        new_datas=self._get_new_datas(new_url, soup)
        return new_urls, new_datas

    def _get_new_urls(self, new_url, soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            a_new_url=link['href']
            new_full_url=urllib.parse.urljoin(new_url,a_new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_datas(self, new_url, soup):
        res_data={}

        #存放url
        res_data['url']=new_url
        #存放标题  <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()
        #存放简介<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find('div',class_='lemma-summary')
        res_data['summary']=summary_node.get_text()

        return res_data