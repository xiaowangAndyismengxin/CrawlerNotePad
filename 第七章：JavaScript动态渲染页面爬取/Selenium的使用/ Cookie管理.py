from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:

    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())

    sleep(2)
