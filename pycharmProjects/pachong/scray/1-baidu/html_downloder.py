#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request

class HtmlDownloder(object):
    def downlod(self, new_url):
        if new_url is None:
            return None
        response = urllib.request.urlopen(new_url)
        if response.getcode()!=200:
            return None
        return response.read()
