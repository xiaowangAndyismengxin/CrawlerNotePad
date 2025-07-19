import requests


s = requests.Session()
s.get("https://www.httpbin.org/cookies/set/number/123456789")
print(s.cookies.get_dict())
r = s.get("https://www.httpbin.org/cookies")
print(r.text)
