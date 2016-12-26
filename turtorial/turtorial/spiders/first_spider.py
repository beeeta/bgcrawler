import scrapy

class FirstSpider(scrapy.Spider):
    name = 'bspider'
    start_urls = ['http://www.csdn.net/']
    def parse(self, response):
        filename = response.url.split('/')[-2]+'.html'
        with open('E:\\abc.html','wb') as f:
            f.write(response.body)