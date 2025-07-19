from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")

with webdriver.Chrome(service=service) as browser:

    target_url = "https://www.taobao.com"

    browser.get(target_url)

    wait = WebDriverWait(browser, 10)

    input_ele = wait.until(ec.presence_of_element_located((By.ID, "q")))
    search_button_ele = wait.until(
        ec.element_to_be_clickable((By.CLASS_NAME, "btn-search"))
    )

    print("input_ele:", input_ele)
    print("search_button_ele:", search_button_ele)

    # ---------------常见等待条件---------------

    # 等待条件                                 含义
    # title_is                                标题是某内容
    # title_contains                          标题包含某内容
    # presence_of_element_located             元素加载出，参数为元素的定位元组，如(By.ID, 'p')
    # visibility_of_element_located           元素可见，参数为元素的定位元组
    # visibility_of                           可见，传入元素对象
    # presence_of_all_elements_located        所有元素加载出
    # text_to_be_present_in_element           某个元素文本值包含某文字
    # text_to_be_in_present_in_element_value  某个节点值中包含某文字
    # frame_to_be_available_and_switch_to_it  frame加载并切换
    # invisibility_of_element_located         元素不可见
    # element_to_be_clickable                 元素可点击
    # staleness_of                            判断一个元素是否仍在DOM树中，可判断页面是否已经刷新
    # element_to_be_selected                  元素可选择，参数为元素对象
    # element_located_to_be_selected          元素可选择，传入定位元组
    # element_selection_state_to_be           传入元素对象以及状态，相等返回True，否则返回False
    # element_located_selection_state_to_be   传入定位元组以及状态，相等返回True，否则返回False
    # alert_is_present                        预期alert出现
