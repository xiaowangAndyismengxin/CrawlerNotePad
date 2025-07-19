from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:
    url = "https://spa2.scrape.center/"
    browser.get(url)

    # 定位元素
    logo_image = browser.find_element(By.CLASS_NAME, "logo-image")
    logo_title = browser.find_element(By.CLASS_NAME, "logo-title")

    # 获取属性
    href = logo_image.get_attribute("href")
    src = logo_image.get_attribute("src")
    alt = logo_image.get_attribute("alt")

    # 输出属性值
    print("href:", href)
    print("src:", src)
    print("alt:", alt)

    # 输出文本
    print("logo_title:", logo_title.text)

    # 输出元素的其他属性
    print("logo_image:", logo_image.id)
    print("logo_image:", logo_image.tag_name)
    print("logo_image:", logo_image.size)
    print("logo_image:", logo_image.location)
    print("logo_image:", logo_image.rect)

    sleep(5)
