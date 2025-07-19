import requests


url = "https://www.httpbin.org/post"
with open("bilibili_image.png", "rb") as f:
    files = {"bilibili_image": f.read()}
response = requests.post(url, files=files)
print(response.text)
