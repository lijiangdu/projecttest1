import scrapy
from qiubaipro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['https://tieba.baidu.com/f?kw=%E6%9F%AF%E5%8D%97&ie=utf-8&tp=0']
    start_urls = ['https://v.qq.com/']

    # def parse(self, response, **kwargs):
    #     # page_text = response.text
    #     # fp = open('./text.html','w',encoding='utf-8')
    #     # fp.write(page_text)
    #     # print('over')
    #     li_list = response.xpath('//*[@id="new_vs_focus"]/div[2]/a')
    #     print(1)
    #     data_list =[]
    #     # print(li_list)
    #     for li in li_list:
    #         name = li.xpath('./span/span/text()').extract()
    #         message = li.xpath('./span/text()').extract()
    #         print(name,message)
    #         dic = {
    #             'name':name,
    #             'message':message
    #         }
    #         data_list.append(dic)
    #     return data_list
    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="new_vs_focus"]/div[2]/a')
        print(1)
        for li in li_list:
            name = li.xpath('./span/span/text()').extract()
            message = li.xpath('./span/text()').extract()
            if name ==[]:
                name = ['空']
            if message == []:
                message = ['空']
            # print(name,message)
            item = QiubaiproItem()
            item['name'] = name[0]
            item['message'] = message[0]
            # print(name[0],message[0])
            yield item# 将item提交给管道