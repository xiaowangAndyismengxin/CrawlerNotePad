from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:

    urls = [
        "https://www.htmlandcssbook.com/code-samples/chapter-01",
        "https://www.htmlandcssbook.com/code-samples/chapter-02",
        "https://www.htmlandcssbook.com/code-samples/chapter-03",
        "https://www.htmlandcssbook.com/code-samples/chapter-04",
        "https://www.htmlandcssbook.com/code-samples/chapter-05",
    ]

    for url in urls:
        browser.get(url)

    sleep(1)

    browser.back()
    sleep(1)
    browser.back()
    sleep(1)
    browser.forward()

    sleep(5)
