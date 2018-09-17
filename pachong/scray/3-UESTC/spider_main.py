#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Login,source

class Spider(object):
    def __init__(self):
        self.login=Login.Login()
        self.source=source.Source()

    def start(self):
        self.login.post()
        self.source.output()
        aaa=input('')

if __name__=='__main__':
    ff=Spider()
    ff.start()
