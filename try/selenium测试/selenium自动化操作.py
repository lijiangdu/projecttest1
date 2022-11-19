from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

bro = webdriver.Edge('D://Driver/edgedriver/msedgedriver.exe')
bro.get('https://www.taobao.com/')

#标签定位
search_input = bro.find_element(By.ID,'q')
#标签交互
search_input.send_keys('Iphone')
#执行一组js程序
sleep(2)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(1)
#点击搜索按钮
btn = bro.find_element(By.CLASS_NAME,'btn-search')
btn.click()
#换一个页面
bro.get('https://www.baidu.com/')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()

sleep(5)
bro.quit()