from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:

    url = "https://www.w3school.com.cn/tiy/t.asp?f=tag_iframe_name"

    browser.get(url)

    # 切换到frame
    browser.switch_to.frame("iframeResult")
    browser.switch_to.frame("iframe_a")

    in_frame_a_xpath_string = "/html/body"
    in_fame_a_parent_xpath_string = "/html/body/h1"

    # 定位元素
    in_frame_a = browser.find_element(By.XPATH, in_frame_a_xpath_string)

    # 输出文本
    print(in_frame_a.text)

    # 切换到父frame
    browser.switch_to.parent_frame()

    # 定位元素
    in_fame_a_parent = browser.find_element(By.XPATH, in_fame_a_parent_xpath_string)

    # 输出文本
    print(in_fame_a_parent.text)

    # 切换到默认frame
    browser.switch_to.default_content()

    try:
        # 定位元素
        in_frame_a = browser.find_element(By.XPATH, in_frame_a_xpath_string)
        # 输出文本
        print(in_frame_a.text)
        print("Get wrong element in wrong frame.")

    except NoSuchElementException:
        print("Can not find element in wrong frame.")

    sleep(5)
