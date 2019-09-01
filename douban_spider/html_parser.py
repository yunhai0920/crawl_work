#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
Author: HuangJie
Date: 2019/8/25 10:47 AM
"""
from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):

    # <a class="item" target="_blank" href="https://movie.douban.com/subject/27010768/?tag=热门&amp;from=gaia">
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find('div', class_="").find_all('a', href=re.compile(r"/subject/\d"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('div', class_="related-info").find('h2').find('i')
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_="indent").find('span', property='v:summary')
        res_data["summary"] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data



