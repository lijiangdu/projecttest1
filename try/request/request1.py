#需求：爬取搜狗首页的页面数据
import requests
if __name__ == '__main__':
    #step1:指定url
    url = 'https://www.zhipin.com/c101280100-p100512/?ka=search_100512'
    #step2:发起请求
    #step方法回返回一个相应对象
    response = requests.get(url)
    #step3:获取相应数据(.text返回的是字符串形式的相应数据)
    page_text = response.text
    print(page_text)
    #step4:持久化储存
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)