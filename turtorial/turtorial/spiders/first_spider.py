import scrapy
from ..items import TestItem
from bs4 import BeautifulSoup

class FirstSpider(scrapy.Spider):
    name = 'bspider'
    start_urls = ['http://codingpy.com/']
    def parse(self, response):
        bs = BeautifulSoup(response.body,'lxml')
        alinks = bs.find_all('a')
        for i in alinks:
            testItem = TestItem()
            testItem['title'] = i.get('title')
            testItem['link'] = i.get('href')
            testItem['desc'] = i.get_text()
            yield  testItem

