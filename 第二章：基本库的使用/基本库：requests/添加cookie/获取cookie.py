import requests


url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 "
    "Safari/537.36",
}
r = requests.get(url, headers=headers)
print(type(r.cookies), r.cookies)
print(r.cookies.get("BAIDUID"))
print(r.cookies.set("a", "b"))
print(r.cookies.get_dict())
print(r.cookies.keys())
print(r.cookies.values())
for k, v in r.cookies.items():
    print(k, "=", v)
r.cookies.clear()
print(r.cookies.get_dict())
