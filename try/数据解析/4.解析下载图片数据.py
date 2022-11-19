import requests
from lxml import etree
import os
if __name__ == "__main__":
    url = 'https://pic.netbian.com/e/search/result/?searchid=4318'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'
    }
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    print(page_text)
#反爬了已经
    # tree = etree.HTML(page_text)
    # li_list = tree.xpath('//div[@class="slist"]/ul/li')
    # if not os.path.exists('./picLibs'):
    #     os.mkdir('./picLibs')
    #
    # for li in li_list:
    #     img_src = 'https://pic.netbian.com' + li.xpath('./a/@href')[0]
    #     new_response = requests.get(url=img_src, headers=headers).text
    #     new_tree = etree.HTML(new_response)
    #     # 数据解析：src的属性值  alt属性
    #     download = 'https://pic.netbian.com' + new_tree.xpath('//div【@class="photo-pic"】/a/img/@src')[0]
    #     img_name = new_tree.xpath('//div[@class="photo-pic"]/a/img/@alt')[0] + '.png'
    #     img_name = img_name.encode('iso-8859-1').decode('gbk')
    #
    #     # 请求图片进行持久化存储
    #     img_data = requests.get(url=download, headers=headers).content
    #     img_path = 'picLibs/' + img_name
    #     with open(img_path, 'wb') as fp:
    #         fp.write(img_data)
    #         print(img_name, '下载成功！！！')


    # tree = etree.HTML(page_text)
    # li_list = tree.xpath('// *[ @ id = "main"] / div[3] / ul/li')
    # print(li_list)
    # for a in li_list:
    #     # src = a.xpath('./a/img/@src')[0]
    #     src = a.xpath('//*[@id="main"]/div[3]/ul/li[1]/a/img')[0]
    #     print(src)