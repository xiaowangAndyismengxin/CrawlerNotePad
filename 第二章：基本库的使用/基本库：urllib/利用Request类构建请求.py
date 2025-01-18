import urllib.request
import urllib.parse


data = bytes(urllib.parse.urlencode({'profile': 'i am a robot'}), encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
                  "Safari/537.36",
    "Host": "www.httpbin.org"  # 必须含有Host
}
request = urllib.request.Request('https://www.httpbin.org/post', data=data, headers=headers, method="POST")
request.add_header('Name', 'Python_crawler')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
