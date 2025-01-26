import httpx


url = 'https://www.httpbin.org/get'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 "
                  "Safari/537.36",
}
with httpx.Client(http2=True, verify=False, headers=headers) as client:  # 约等于requests中的Session
    r = client.get(url)
    print(type(r.status_code), r.status_code)
    print(type(r.headers), r.headers.get('date'))
    print(type(r.text), r.text)
    print(type(r.request.headers), r.request.headers)
