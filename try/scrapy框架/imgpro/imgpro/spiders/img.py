import scrapy
from imgpro.items import ImgproItem

#爬取图片流程：
#1.解析出图片地址
#2.将图片地址item提交到指定的管道类
#get_media_request  file_path  item_completed
#3.在配置文件中：
#指定图片储存的目录：IMAGES_STORE = ''  指定开启的管道：自定制的管道类



class ImgSpider(scrapy.Spider):
    name = 'img'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response, **kwargs):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            #使用伪属性src2
            src = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            # print(src)

            item = ImgproItem()
            item['src'] = src

            yield item