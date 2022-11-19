import scrapy


class GetnovelSpider(scrapy.Spider):
    name = 'getnovel'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qidian.com/all/']
    url = 'https://www.qidian.com/all/page%d/'
    page_num = 2
    fp = open('./novelname.txt','w',encoding='utf-8')

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="book-img-text"]/ul/li')
        for li in li_list:
            novelName = li.xpath('./div[2]/h2/a/text()').extract()[0]
            # print(novelName)
            self.fp.write(novelName+'\n')
        if self.page_num <= 10:
            new_url = format(self.url %self.page_num)
            self.page_num+=1
            #手动发起请求：callback回调函数专门用于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)