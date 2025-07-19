import requests


proxies = {"协议": "链接"}
r = requests.get("https://www.httpbin.org/get", proxies=proxies)
print(r.text)
