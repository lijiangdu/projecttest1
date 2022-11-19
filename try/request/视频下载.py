import requests
from lxml import etree
from multiprocessing import Pool

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
proxies = {
    # 'http': '222.110.147.50:3128'
    'http':'175.100.72.95:57938'
}
def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载')
    data = requests.get(url=url, headers=headers,proxies=proxies).content
    fp = open(dic['name'], 'wb')
    fp.write(data)
    print(dic['name'], '下载成功')
# dic1 = {
#     'name': '111.mp4',
#     'url':'https://9uu33.com/20211029/uu/uu/f9c603c93ebce18aa3c0d4877f129b6e/f9c603c93ebce18aa3c0d4877f129b6e.mp4'
# }
dic1 = {
    'name': '111.html',
    'url':'https://www.baidu.com/s?wd=ip'
}
urls = []
urls.append(dic1)
get_video_data(dic1)
# if __name__ == '__main__':
#     pool = Pool(4)
#     pool.map(get_video_data, urls)
#     pool.close()
#     pool.join()
#     # get_video_data(urls[0])