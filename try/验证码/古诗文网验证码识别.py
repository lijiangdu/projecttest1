import requests
from lxml import etree
import chaojiying
#将验证码图片下载到本地
chaojiying = chaojiying.Chaojiying_Client('lijiangdu01', '123456789aaa', '928700')	#用户中心>>软件ID 生成一个替换 96001
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
code_list = chaojiying.PostPic(im, 1902)
code = code_list['pic_str']
print(code)