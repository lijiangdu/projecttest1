from selenium import webdriver
from time import sleep
from selenium.webdriver.edge.options import Options

#实现无可视化操作,让selenium规避被检测识别
edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')
edge_options.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Edge(executable_path='D://Driver/edgedriver/msedgedriver.exe',options=edge_options)

#无可视化界面（无头浏览器）phantomJs
bro.get('https://www.baidu.com')
print(bro.page_source)
sleep(2)
bro.quit()