from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


service = Service(executable_path="D:/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--headless')

with webdriver.Chrome(service=service, options=options) as browser:

    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })

    browser.get('https://antispider1.scrape.center/')

    browser.set_window_size(1366, 768)
    print('Current window size:', browser.get_window_size())
    sleep(3)
    browser.get_screenshot_as_file('handless_screenshot.png')

    # sleep(3)
