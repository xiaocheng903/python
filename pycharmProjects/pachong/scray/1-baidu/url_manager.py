#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class UrlManager(object):

    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()

    def add_new_url(self, url):
        if url is None:
            return None
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return None
        for url in urls:
            self.add_new_url(url)
    def has_new_url(self):
        return not len(self.new_urls) == 0

    def get_new_url(self):
        newurl=self.new_urls.pop()
        self.old_urls.add(newurl)
        return newurl

