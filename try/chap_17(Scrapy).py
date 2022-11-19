#encoding: utf-8
import scrapy
class Example1(scrapy.Spider):
    name = 'example1'
    start_urls = ['https://blog.scrapinghub.com']
    def parse(self, response, **kwargs):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}
        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page,self.parse)