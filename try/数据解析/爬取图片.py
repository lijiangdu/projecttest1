import requests
if __name__ == '__main__':
    url = 'https://i0.hdslb.com/bfs/archive/aaa1dfba090a875fbab4bb0ac1af48a9d438c996.png'
    #content返回的是二进制形式的图片数据
    #text(字符串) content(二进制) json(对象)
    img_data = requests.get(url=url).content
    with open('./img.jpg','wb') as fp :
        fp.write(img_data)