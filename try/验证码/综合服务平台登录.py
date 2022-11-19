#验证码的识别，获取验证码的文字数据
#对post发送请求
#对响应数据进行持久化存储

import requests
from lxml import etree
import chaojiying

#对验证码图片进行获取和识别
chaojiying = chaojiying.Chaojiying_Client('lijiangdu01', '123456789aaa', '928700')	#用户中心>>软件ID 生成一个替换 96001
url = 'https://sso.scnu.edu.cn/AccountService/user/login.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
session = requests.session()
page_text = session.get(url=url, headers=headers).text
code_img_src = 'https://sso.scnu.edu.cn/AccountService/user/rancode.jpg'
img_data = session.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
code_list = chaojiying.PostPic(im, 1902)
code = code_list['pic_str']
print(code)
log_url = 'https://sso.scnu.edu.cn/AccountService/user/login.html'
data = {
    'account': '20202005442',
    'password': '123456789aaa!ABC',
    'rancode': code,
}
response = session.post(url=log_url,data=data)
print(response.status_code)
login_page = response.text
with open('./zonghe.html','w',encoding='utf-8') as fp2:
    fp2.write(login_page)

index_url = 'https://sso.scnu.edu.cn/AccountService/user/index.html'
response = session.get(url=index_url)
print(response.status_code)
login_page = response.text
with open('./index.html','w',encoding='utf-8') as fp3:
    fp3.write(login_page)