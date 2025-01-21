import requests
import logging


logging.captureWarnings(True)
# 编辑器可能会报错，但的确可以，因为存在于__init__.py中
requests.urllib3.disable_warnings()
url = "https://ssr2.scrape.center"
# ???
