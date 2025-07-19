from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor, build_opener, Request


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
    "Safari/537.36",
    "host": "www.bilibili.com",
}
request = Request("https://www.bilibili.com", headers=headers, method="GET")

cookie = CookieJar()
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
response = opener.open(request)
for (
    item
) in (
    cookie
):  # item: <class 'http.cookiejar.Cookie'> cookie: <class 'http.cookiejar.CookieJar'>
    print(item.name + " = " + item.value)
