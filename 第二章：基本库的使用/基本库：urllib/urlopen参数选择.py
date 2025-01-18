import urllib.request
import urllib.parse
import urllib.error
import socket  # 一个库，可以实现TCP/UDP/IP等协议的底层操作


# data, timeout, contest, cafile, capath
# def urlopen(
#     url: str | Request,
#     data: _DataType | None = None,
#     timeout: float | None = ...,
#     *,
#     cafile: str | None = None,
#     capath: str | None = None,
#     cadefault: bool = False,
#     context: ssl.SSLContext | None = None,
# ) -> _UrlopenRet: ..
data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding="utf-8")
try:
    response = urllib.request.urlopen(url="https://www.httpbin.org/post", data=data, timeout=60)
except urllib.error.URLError as e:
    print(e.reason)
    print(isinstance(e.reason, socket.timeout))
else:
    print(response.read().decode("utf-8"))
