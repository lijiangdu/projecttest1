# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse

class NewsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    #该方法拦截五大板块对应的响应对象，进行篡改
    def process_response(self, request, response, spider):  #spider是爬虫对象
        bro = spider.bro  #获取了在爬虫类中定义的浏览器对象

        # 挑选出指定的响应对象进行篡改
        #通过url定位request
        #通过request指定response
        if request.url in spider.models_list:
            bro.get(request.url)#对五个板块对应的url发送请求
            time.sleep(2)
            page_text = bro.page_source #包含了动态加载的新闻数据
            #response对应五大板块的响应对象
            #针对定位到的这些url进行篡改
            #实例化一个新的响应对象（符合要求的包含动态加载的新闻数据），替代原来的响应对象导入一个包
            #可以基于selenuim获取动态加载数据
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            #response其他要求的响应对象
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

