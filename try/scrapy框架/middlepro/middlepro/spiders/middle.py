import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    #allowed_domains = ['www.xxxx.']
    start_urls = ['http://mip.chinaz.com/']

    def parse(self, response, **kwargs):
        page_text = response.text
        with open('./ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
