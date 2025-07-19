from requests import Request, Session

url = "https://www.httpbin.org/post"
data = {
    "profile": "I am a robot",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 "
    "Safari/537.36",
}
s = Session()
req = Request("POST", url, headers, data=data)
prepared = s.prepare_request(req)
r = s.send(prepared)
print(r.text)
