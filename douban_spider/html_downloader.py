#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Author: HuangJie
Date: 2019/8/25 10:46 AM
"""
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
