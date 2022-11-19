import time

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunpro.items import SunproItem
from sunpro.items import DetailItem

#使用链接提取器提取所有页码链接
#再使用链接提取器提取出所有详情页链接
class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qidian.com/all/page1/']

    #链接提取器（根据制定规则对指定链接进行提取）（allow为正则）
    link = LinkExtractor(allow=r'page\d+')

    link_detail = LinkExtractor(allow='https://book.qidian.com/info/\d+/')

    rules = (
        #规则解析器
        #follow后面如果是True那么可以作用在提取出来的页面中继续提取
        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail, callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        #在xpath表达式中不能出现tbody，不会被检测到
        # print(response)
        li_list = response.xpath('//*[@id="book-img-text"]/ul/li')
        for li in li_list:
            author = li.xpath('./div[2]/p[1]/a[1]/text()').extract_first()
            name = li.xpath('./div[2]/h2/a/text()').extract_first()
            item = SunproItem()
            item['name']=name
            item['author']=author
            yield item
            # print(name,author)

    #进入详情页解析作品信息
    #两个Parse方法不能互相传递参数，不能放在同一个item中，可以依次储存在两个item中
    def parse_detail(self,response):
        new_name = response.xpath('/html/body/div[1]/div[6]/div[1]/div[2]/h1/em/text()').extract_first()
        introduce = response.xpath('/html/body/div[1]/div[6]/div[4]/div[1]/div[1]/div[1]/p//text()').extract()
        introduce = ''.join(introduce)
        item = DetailItem()
        item['new_name']=new_name
        item['introduce']=introduce
        yield item
        # print(new_name,introduce)