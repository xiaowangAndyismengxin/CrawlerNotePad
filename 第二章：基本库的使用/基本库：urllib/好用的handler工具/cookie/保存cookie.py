from http.cookiejar import MozillaCookieJar
from urllib.request import HTTPCookieProcessor, build_opener, Request


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
                  "Safari/537.36",
    "host": "www.bilibili.com"
}
request = Request("https://www.bilibili.com", headers=headers, method="GET")


file_name = "example_Mozilla_cookie.txt"
cookie = MozillaCookieJar(file_name)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
response = opener.open(request)
cookie.save(ignore_discard=False, ignore_expires=False)
