import requests
import re
import os
#需求：从例如云上下载图片
if __name__ == '__main__':
    #创建一个文件夹，用于保存所有图片
    if not os.path.exists('./liruyun'):
        os.mkdir('./liruyun')
    url = 'https://moodle.scnu.edu.cn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    #使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url,headers=headers).text
    #使用聚焦爬虫将页面中所有图片进行解析/提取
    ex = '<div class="img-inner">.*?<img src="(.*?)" class.*?</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    print(img_src_list)
    for src in img_src_list:
        #首先拼接出一个图片完整的url
        #请求一个图片的二进制数据
        img_data = requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name = src.split('/')[-1]
        #图片储存路径
        img_Path = './liruyun/'+img_name
        with open(img_Path, 'wb') as fp:
            fp.write(img_data)
            print(img_name+'下载成功')