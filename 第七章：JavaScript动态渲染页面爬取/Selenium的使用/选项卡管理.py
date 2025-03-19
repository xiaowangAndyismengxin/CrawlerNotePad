from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:

    browser.get('https://www.baidu.com')

    # tab 是标签页， window 是窗口， 默认tab
    # browser.switch_to.new_window('window')

    browser.execute_script('window.open()')

    print(browser.window_handles, type(browser.window_handles[0]))

    sleep(1)

    browser.switch_to.window(browser.window_handles[0])

    sleep(3)
