import requests


url = "https://www.httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 "
                  "Safari/537.36",
}
data = {
    "profile": "I am a robot."
}
response = requests.post(url, data=data, headers=headers)
print(response.text)
