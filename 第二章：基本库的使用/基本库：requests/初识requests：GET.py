import requests
from json.decoder import JSONDecodeError


url = "https://www.httpbin.org/get"
data = {
    "name": "Python_Crawler",
}
response = requests.get(url, params=data)
print(response.text)
try:
    print(response.json())
except JSONDecodeError as e:
    print(e.args)
    print(e.msg)
