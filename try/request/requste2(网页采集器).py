#UA:User-Agent(请求载体的身份标识)
#UA检测：门户网站服务器检测相应请求载体的身份标示，如果检测到的身份
#标示是基于某一款浏览器，说明这是一个正常的访问，如果检测到的载体身份
#不是正常的请求（爬虫）,则会有可能拒绝该请求
#UA伪装：让爬虫的对应身份标识伪装成某一款浏览器

import requests
if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    url = 'https://mp.weixin.qq.com/s/ozRWXrdOaAM-ZGvRkVL1Pw'
    #处理url携带的参数：封装到字典中
    # kw = input('enter a word:')
    # param = {
    #     'q':kw
    # }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    # response = requests.get(url=url, params=param, headers=headers)
    # page_text = response.text
    for i in range(1,10000):
        response = requests.get(url=url,headers=headers)
        # page_text = response.text
        print(1)
    # fileName = kw + '.html'
    # fileName = '111.html'
    # with open(fileName,'w',encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print(fileName,"保存成功")