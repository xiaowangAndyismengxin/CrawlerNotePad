from urllib.request import (
    HTTPPasswordMgrWithDefaultRealm,
    HTTPBasicAuthHandler,
    build_opener,
)
from urllib.error import URLError


url = "https://ssr3.scrape.center"
username = "admin"
password = "admin"
p = (
    HTTPPasswordMgrWithDefaultRealm()
)  # 继承自HTTPPasswordMgr类，增加了对默认认证域的支持。当没有指定认证域时，可以使用默认认证域。
p.add_password(None, url, username, password)  # 自动域，超智能的
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)


try:
    result = opener.open(url)  # <class 'http.client.HTTPResponse'>
    html = result.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
