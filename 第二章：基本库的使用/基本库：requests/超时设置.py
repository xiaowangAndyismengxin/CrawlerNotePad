import requests


#                                                  链接 读取
r = requests.get("https://www.httpbin.org", timeout=(5, 30))  # 只传一个数就是总和
