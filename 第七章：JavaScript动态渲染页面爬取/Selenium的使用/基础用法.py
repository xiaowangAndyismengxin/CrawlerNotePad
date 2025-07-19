from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 明确指定本地驱动路径（已跳过自动检测逻辑）
chrome_driver_path = "D:/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

with webdriver.Chrome(service=service) as browser:

    # -------------------打开网页-------------------
    browser.get("https://www.baidu.com")
    print(browser.page_source[:100] + "......")

    # -------------------选择元素-------------------
    input_frame = browser.find_element(By.ID, "head_wrapper").find_element(By.ID, "kw")
    top_left_a = browser.find_element(By.ID, "s-top-left").find_elements(
        By.TAG_NAME, "a"
    )
    print(input_frame)
    print(top_left_a)  # list

    # -------------------节点交互-------------------
    search_button = browser.find_element(By.XPATH, '//input[@value="百度一下"]')

    input_frame.send_keys("C++全套学习教程")
    sleep(2)
    input_frame.clear()
    input_frame.send_keys("Python全套教程")

    # input_frame.send_keys(Keys.ENTER)
    search_button.click()

    # -------------------END-------------------

    sleep(5)
