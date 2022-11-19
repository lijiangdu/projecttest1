from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
import time

path = 'D://Driver/edgedriver/msedgedriver.exe'
driver = webdriver.Edge(path)

driver.get('https://bing.com')

# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()
# time.sleep(5)
driver.get('http://scxk.nmpa.gov.cn:81/xk/')
page_text = driver.page_source
#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
time.sleep(5)
driver.quit()