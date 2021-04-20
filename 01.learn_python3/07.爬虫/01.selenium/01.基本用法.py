import time
from selenium import webdriver  # 驱动浏览器
from selenium.webdriver import ActionChains  # 滑动
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as ec  # 等待所有标签加载完毕
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载完毕 寻找某些元素

browser = webdriver.Chrome()  # 调用Chrome 驱动，生成浏览器对象
wait = WebDriverWait(browser, 10)  # 设置selenium等待浏览器加载完毕的最大等待时间

try:
    browser.get('https://www.baidu.com/')
    baidu_input_tag = browser.find_element_by_id("kw")  # 寻找到百度页面的id='kw'的标签
    key = baidu_input_tag.send_keys('张根')  # 在标签中输入'张根'

    baidu_button_tag = browser.find_element_by_id('su')  # 寻找到百度页面id='su'的标签
    baidu_button_tag.click()  # 点击
    wait.until(ec.presence_of_element_located((By.ID, '4')))  # 等待百度页面 ID='4'的标签完毕，最大等待10秒
    '''
    请求相关：
    browser.get('url')
    响应相关：
    print(browser.page_source) #显示网页源码
    print(browser.current_url)   #获取当前url
    print(browser.get_cookies()) #获取当前网页cokies
    '''

finally:
    time.sleep(5)
    browser.close()  # 关闭浏览器