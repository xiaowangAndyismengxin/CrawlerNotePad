from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:

    browser.get("https://jqueryui.com/droppable/")

    # 切换到iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, '//*[@id="content"]/iframe'))

    # 定位拖拽元素和目标元素
    draggable = browser.find_element(By.ID, "draggable")
    droppable = browser.find_element(By.ID, "droppable")

    # 拖拽不能拖拽的元素，没用
    # draggable = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/ul/li[2]')
    # droppable = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/ul/li[4]')

    # 执行拖拽操作
    actions = ActionChains(browser)
    actions.drag_and_drop(draggable, droppable)
    actions.perform()

    sleep(5)
