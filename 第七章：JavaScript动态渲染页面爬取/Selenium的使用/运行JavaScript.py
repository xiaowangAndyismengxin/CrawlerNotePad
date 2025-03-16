from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoAlertPresentException


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:
    url = 'https://www.bilibili.com'
    browser.get(url)

    # 执行JavaScript代码
    browser.execute_script('alert("Hello, World!")')
    # 等待弹窗出现并关闭
    sleep(2)

    # 如果弹窗未关闭, 关闭弹窗
    try:
        browser.switch_to.alert.accept()
    except NoAlertPresentException:
        pass

    # 滚动页面到页面底部
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 修改页面标题
    browser.execute_script('document.title = "New Title"')

    # 获取页面标题
    title = browser.execute_script('return document.title')
    print(title)

    sleep(5)
