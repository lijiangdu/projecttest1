#/表示一个层级，//表示多个层级，可以表示从任意位子开始定位，//div[@class='song']属性定位，//div[@class='song']/p[3]索引定位
#取文本/text()获取的是标签中直系的文本内容列表//text()获取的是标签中所有文本内容列表
#取属性/@attrName
import requests
from lxml import etree
#取58二手房中房源信息
if __name__ == '__main__':
    url = 'https://gz.58.com/ershoufang'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    page_text = requests.get(url=url, headers=headers).text
    fp = open('./58tongcheng.html','w',encoding='utf-8')
    # fp.write(page_text)
    #数据解析
    tree = etree.HTML(page_text)
    # a_list = tree.xpath('//div[@class="property"]/a')
    # for a in a_list:
    #     title = a.xpath('.//div[@class="property-content-title"]/h3/@title')[0]
    #     print(title)
    a_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
    house_list = []
    print(a_list)
    for a in a_list:
        house_list.append(a.xpath('./a/div[2]/div[1]/div[1]/h3/@title')[0])
    fp.write(str(house_list))