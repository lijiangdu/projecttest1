import requests
from lxml import etree
import os
if __name__ == "__main__":
    url = 'http://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
    }
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    # print(page_text)
    fp = open('./city.txt','w',encoding='utf-8')
    tree = etree.HTML(page_text)
    # li_list1 = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li')
    # for li in li_list1:
    #     src = li.xpath('./a/text()')[0]
    #     fp.write(src+'\n')
    # ul_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul')
    # for ul in ul_list:
    #     li_list2 = ul.xpath('./div[2]/li')
    #     for li2 in li_list2:
    #         src = li2.xpath('./a/text()')[0]
    #         fp.write(src+'\n')
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        fp.write(city_name+'\n')