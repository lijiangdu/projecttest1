import time

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

bro = webdriver.Edge('D://Driver/edgedriver/msedgedriver.exe')
bro.get('https://news.4399.com/hxjy/')
bro.switch_to.frame('flash22')
bro.switch_to.frame('popup_login_frame')
username = bro.find_element(By.ID,'username')
password = bro.find_element(By.ID,'j-password')
btn = bro.find_element(By.CLASS_NAME,'ptlogin_btn')
time.sleep(1)
username.send_keys('153901436')
time.sleep(1)
password.send_keys('shanghai1')
time.sleep(1)
btn.click()
time.sleep(3)
bro.quit()