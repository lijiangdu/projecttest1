import requests
import json
if __name__ == '__main__':
    #指定Url
    post_url = 'https://fanyi.baidu.com/sug'
    #进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    #post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #请求发送
    response = requests.post(url=post_url,data=data)
    #获取响应数据:json()方法返回的是一个字典对象(确认响应数据是json类型的才可以使用这个方法)
    dic_obj = response.json()
    print(dic_obj)
    #进行持久化存储
    fileName = word +'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!')