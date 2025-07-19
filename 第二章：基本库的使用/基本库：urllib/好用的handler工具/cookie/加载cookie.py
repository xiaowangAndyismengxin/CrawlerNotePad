from http.cookiejar import (
    LoadError,
    MozillaCookieJar,
)  # LoadError: 内置错误: OSError子类，处理加载问题
from urllib.request import HTTPCookieProcessor, build_opener, Request


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
    "Safari/537.36",
    "host": "www.bilibili.com",
}
request = Request("https://www.bilibili.com", headers=headers, method="GET")


file_name = "example_Mozilla_cookie.txt"
cookie = MozillaCookieJar(file_name)
try:
    cookie.load(ignore_discard=False, ignore_expires=False)
except FileNotFoundError as e:
    print(e.args)
except LoadError as e:
    print(e.args)
else:
    handler = HTTPCookieProcessor(cookie)
    opener = build_opener(handler)
    response = opener.open(request)
