import scrapy
from selenium import webdriver
from news.items import NewsItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_list = [] #用来存储五大板块对应详情页的Url

    #实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Edge(executable_path='D://Driver/edgedriver/msedgedriver.exe')


    #通过主页解析出五大板块对应的url
    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        a_list = [2,3,5,6,8]
        # print(len(li_list))
        for a in a_list:
            model_url = li_list[a].xpath('./a/@href').extract_first()
            self.models_list.append(model_url)
            # print(model_url)

        #依次对每一个板块对应的页面进行请求
        for url in self.models_list:
            yield scrapy.Request(url,callback=self.parse_model)

    #每一个板块对应的新闻都是动态加载出来的
    def parse_model(self,response):  #解析每一个板块所对应详情页的url
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            #进行请求传参传递title
            item = NewsItem()
            item['title'] = title
            #对新闻详情页url发请求
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):  #解析新闻内容
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self,spider):
        self.bro.quit()