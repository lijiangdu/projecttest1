#实例化BeautifulSoup对象:from bs4 import BeautifulSoup
#对象的实例化：
# 1.从本地html文档中数据加载到该对象中
#fp = open('./test.html','r',encoding = 'utf-8')
#soup = BeautifulSoup('fp','lxml')
#2.将互联网上获取的网页源码加载到该对象中
# page_text = response.text
# soup = BeautifulSoup(page_text,'lxml')
#提供的用于数据解析的方法和属性：
#soup.tagName:返回的是文件中第一次出现tagName对应的标签
#soup.find():soup.find('tarName')等于soup.tagName
#属性定位：soup.find('div',class_/id_/attr_='str')属性名后面要加上_
#soup.find_all('tarName'):返回符合要求的所有标签（列表）
#select('某冲选择器（id,class等）')返回的是一个列表
#层级选择器：soup.select('.tang>ul>li>a'):>标示一个层级
#soup.select('.tang>ul a'):空格标示多个层级
#获取标签之间的文本数据：soup.a.text/string/get_text()
#text/get_text()可以获取某一个标签中所有的文本内容
#string只可以获取该标签直系的文本内容
#获取标签中的属性值：soup.a['href']

import requests
from bs4 import BeautifulSoup
#需求：爬取三国演义章节标题和章节内容https://www.shicimingju.com/book/sanguoyanyi.html
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    page_text = requests.get(url=url,headers=headers)
    #在首页中解析章节标题和详情页的url
    #1.实例化BeautifulSoup对象
    soup = BeautifulSoup(page_text.content,'lxml')
    a_text = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in a_text:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com/'+li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).content
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到了章节内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title+'爬取成功')