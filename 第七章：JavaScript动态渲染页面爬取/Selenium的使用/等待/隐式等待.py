from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import time, sleep


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:
    browser.implicitly_wait(5)
    target_url = 'https://spa5.scrape.center/'

    browser.get(target_url)

    try:

        start_time = time()
        element = browser.find_element(By.CSS_SELECTOR, '.logo-image')
        print(element)
        end_time = time()
        print(f'元素查询耗时：{end_time - start_time}')
    except TimeoutException:
        print('未找到元素')

    sleep(5)
