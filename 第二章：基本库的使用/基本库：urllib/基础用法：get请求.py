import urllib.request


response = urllib.request.urlopen("https://www.httpbin.org/get")
print(type(response))
print(response.msg)  # str
print(response.code)  # int
print(response.status)  # int
print(response.getheaders())  # list
print(response.getheader("server"))  # Press Environment
print(response.read().decode("utf-8"))
