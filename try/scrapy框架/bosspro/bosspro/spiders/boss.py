import scrapy
from bosspro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://yhdm04.com/']
    print(1)

    page_num = 2
    url = ''

    def detail_parse(self,response):
        #回调接收item
        item = response.meta['item']
        film_desc = response.xpath('/html/body/div[2]/div[2]/div[2]/dl/dt[2]/div/div[2]/text()').extract()
        film_detail = ''.join(film_desc)
        film_detail = film_detail.replace(' ','')
        item['film_detail'] = film_detail
        yield item
        # print(film_detail)

    def parse(self, response, **kwargs):
        # print(2)
        li_list = response.xpath('/html/body/div[2]/div[5]/div[1]/ul/li')
        # print(li_list)
        for li in li_list:
            item = BossproItem()
            message = li.xpath('./a[@class="li-hv"]/@href').extract()
            if message == []:
                continue
            url = 'http://yhdm04.com/' + message[0]
            detail = li.xpath('./a[@class="li-hv"]/@title').extract()
            if detail == []:
                continue
            film_name = detail[0]
            item['film_name'] = film_name
            # print(message)
            # print(name)
            # print(url)
            # print(detail)
            # 手动发起请求传参，通过meta字典传递给请求对应的回调函数
            yield scrapy.Request(url,callback=self.detail_parse,meta={'item':item})
        #分页操作
        if self.page_num <= 10:
            new_url = format(self.url %self.page_num)
            self.page_num+=1
            #手动发起请求：callback回调函数专门用于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)