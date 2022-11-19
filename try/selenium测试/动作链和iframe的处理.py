from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

bro = webdriver.Edge('D://Driver/edgedriver/msedgedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果标签是存在于iframe中的则必须通过以下操作进行标签定位
bro.switch_to.frame('iframeResult')#切换浏览器标签定位作用域
div = bro.find_element(By.ID, 'draggable')
#动作链
action = ActionChains(bro)
#点击长按指定标签
action.click_and_hold(div)

for i in range(5):
    #perform()立即执行动作链操作
    #move by offset(x,y):x为水平方向，y为竖直方向
    action.move_by_offset(30,0).perform()
    sleep(0.3)
#释放动作链
action.release()
bro.quit()