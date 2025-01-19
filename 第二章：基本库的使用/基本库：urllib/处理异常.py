from urllib.error import URLError, HTTPError  # 继承自OSError:)
from urllib.request import urlopen


try:
    response = urlopen("https://ssr1.scrape.center/666", timeout=60)
except TimeoutError as e:
    print(e.args)
except HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)
except URLError as e:
    print(e.reason)
