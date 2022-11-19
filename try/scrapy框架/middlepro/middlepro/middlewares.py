# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random

class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    user_agent_list = [
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        # "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        # "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        # "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        # "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        # "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        # "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        # "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        # "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        # "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        # "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        # "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        # "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        # "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        # "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    ]
    PROXY_http = [
        '1.197.34.81:37824',
        '218.23.199.121:17881',
        '117.57.62.191:17351',
        '60.163.223.242:10329',
        '111.224.219.16:31848',
    ]
    PROXY_https = [
        '1.197.34.81:37824',
        '218.23.199.121:17881',
        '117.57.62.191:17351',
        '60.163.223.242:10329',
        '111.224.219.16:31848',
    ]
    #用于拦截请求
    def process_request(self, request, spider):
        #UA伪装,建立一个UA池
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        #验证代理操作
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://'+random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://'+random.choice(self.PROXY_https)
        return None

    #拦截所有相应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    #拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        #选择代理
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://'+random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://'+random.choice(self.PROXY_https)
        return request #将修正之后的请求对象进行重新发送请求