#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Author: HuangJie
Date: 2019/8/25 10:45 AM
"""
from douban_spider import url_manager
from douban_spider import html_downloader
from douban_spider import html_parser
from douban_spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, url):
        self.urls.add_new_url(url)
        try:
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
        except:
            print("crawl failed !")
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://movie.douban.com/subject/26425063/"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)