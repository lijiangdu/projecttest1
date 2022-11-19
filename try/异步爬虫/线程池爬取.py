import requests
from lxml import etree
from multiprocessing import Pool

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }

def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载')
    data = requests.get(url=url, headers=headers).content
    fp = open(dic['name'], 'wb')
    fp.write(data)
    print(dic['name'], '下载成功')

url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
page_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []
for li in page_list:
    detail_url = li.xpath('./div/a/@href')[0]
    detail_name = (li.xpath('./div/a/div[2]/text()')[0] + '.mp4').replace(' ', '')
    videoId = detail_url.split('_')[1]
    vedioHref = 'https://www.pearvideo.com/videoStatus.jsp?contId=' + videoId
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43',
        'Referer': 'https://www.pearvideo.com/video_' + videoId
    }
    vedio_url = requests.get(url=vedioHref, headers=headers).json()
    vedio = vedio_url['videoInfo']['videos']['srcUrl']
    video = vedio.replace(vedio.split('/')[-1].split('-')[0], 'cont-%s' % videoId)
    dic = {
        'name': './' + videoId + '.mp4',
        # 'name': './'+detail_name,
        'url': video
    }
    urls.append(dic)
    # vedio_media = requests.get(url=video,headers=headers).content
    # file_name = './'+videoId + '.mp4'
    # with open(file_name,'wb') as fp:
    #     fp.write(vedio_media)
    #     print(detail_name+'下载成功')
    # print(video)
    # print(vedioHref)
    # # print(detail_url,detail_name)
    # print(dic)
if __name__ == '__main__':
    pool = Pool(4)
    pool.map(get_video_data, urls)
    pool.close()
    pool.join()
    # get_video_data(urls[0])