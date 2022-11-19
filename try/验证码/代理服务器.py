import time

import requests
import socket
from requests.adapters import HTTPAdapter
from lxml import etree
import chaojiying


# url = 'https://ip.hao86.com/'
url = 'http://mip.chinaz.com/'
# url = 'http://httpbin.org/ip'
headers = {
    'Connection':'close',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
proxies = {
    # 'http': '222.110.147.50:3128'
    'http':'27.192.200.7:9000',
    # 'https':'110.18.154.231:9999'
}
# time.sleep(3)
i = 0
while True:
    try:
        # s = requests.Session()
        # s.mount('http://', HTTPAdapter(max_retries=3))  # 访问http协议时，设置重传请求最多三次
        # s.mount('https://', HTTPAdapter(max_retries=3))  # 访问https协议时，设置重传请求最多三次
        # requests.adapters.DEFAULT_RETRIES = 5
        i+=1
        if i>10:
            print('fail')
            break
        page_text = requests.get(url=url, headers=headers, proxies=proxies, timeout=(3, 7)).text
        with open('./ip.html', 'w', encoding='utf-8') as fp:
            fp.write(str(page_text))
    except:
        time.sleep(2)
        continue
# except Exceptio as e:##正常运行
# except urllib.error.URLError as e:## 报错socket.timeout: timed out
#     print("Fail")