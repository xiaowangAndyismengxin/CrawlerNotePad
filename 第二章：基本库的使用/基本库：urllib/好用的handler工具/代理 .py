from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


url = "https://www.example.com"
proxy_handle = ProxyHandler({"协议": "链接"})
opener = build_opener(proxy_handle)
try:
    response = opener.open(url)
    html = response.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
