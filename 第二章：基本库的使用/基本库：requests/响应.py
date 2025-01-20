import requests


url = "https://ssr1.scrape.center"
r = requests.get(url)
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
print(r.status_code == requests.codes.ok)
