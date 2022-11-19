import time

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PIL import Image

bro = webdriver.Edge('D://Driver/edgedriver/msedgedriver.exe')
bro.get('https://news.4399.com/hxjy/')
time.sleep(1)
bro.save_screenshot('aa.png')
fr1_ele = bro.find_element(By.XPATH,'//*[@id="flash22"]')
fr1_loc = fr1_ele.location
bro.switch_to.frame('flash22')
fr2_ele = bro.find_element(By.XPATH,'//*[@id="popup_login_frame"]')
fr2_loc = fr2_ele.location
bro.switch_to.frame('popup_login_frame')
#确定登录界面坐标,由于在两个iframe里面，因此需要吧两个iframe先确定位置再加上两个iframe的坐标才是最终坐标
img_ele = bro.find_element(By.XPATH,'//*[@id="popup_login_div"]')
location = img_ele.location#确定左上角坐标
print('location:',location)
size = img_ele.size #确定对应标签宽度
print('size:',size)
#左上角和右下角坐标
rangle = ((location['x']+fr1_loc['x']+fr2_loc['x'])*1.25,(location['y']+fr1_loc['y']+fr2_loc['y'])*1.25,(location['x']+size['width']+fr1_loc['x']+fr2_loc['x'])*1.25,(location['y']+size['height']+fr1_loc['y']+fr2_loc['y'])*1.25)
i = Image.open('./aa.png')
#crop根据指定区域对图片进行裁剪
frame = i.crop(rangle)
frame.save('./login.png')
bro.quit()