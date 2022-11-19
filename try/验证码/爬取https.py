import requests
import json
from lxml import etree

def check(ip):
    try:
        url = 'https://www.baidu.com'
        proxies = {
            # 'http':ip,
            'https': ip
        }
        page = requests.get(url=url, proxies=proxies, timeout=(3, 3))
        if page.status_code == 200:
            return True
        else:
            return False
    except:
        return False
# print(check('103.103.3.6:8080'))
if __name__ == '__main__':
    https_list = []
    for i in range(1,15):
        # 指定Url
        url = 'http://nimadaili.com/https/%d/' %i
        # 进行UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
        }
        # 请求发送
        response = requests.get(url=url, headers=headers)
        # 获取响应数据:json()方法返回的是一个字典对象(确认响应数据是json类型的才可以使用这个方法)
        page_text = response.text
        tree = etree.HTML(page_text)
        tr_list = tree.xpath('/html/body/div[1]/div[1]/div/table/tbody/tr')
        tr1_list = []
        for tr in tr_list:
            if check(tr.xpath('./td[1]/text()')) == True:
                tr1_list.append('有效ip')
            else:
                tr1_list.append('无效ip')
        for tr in tr_list:
            data = tr.xpath('./td/text()')
            tr1_list.append(data)
        https_list.append(tr1_list)
    fp = open('./https.txt','w',encoding='utf-8')
    for x in https_list:
        for y in x:
            for z in y:
                fp.write(z)
                fp.write(' ')
            fp.write('\n')
    print('over!')