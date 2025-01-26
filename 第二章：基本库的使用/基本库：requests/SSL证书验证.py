import requests
import logging


logging.captureWarnings(True)
requests.urllib3.disable_warnings()
url = "https://ssr2.scrape.center"
resp = requests.get(url, verify=False)
print(resp.status_code)
print(resp.text[:50], '...')
