import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 "
                  "Safari/537.36",
}

url = "https://ts4.cn.mm.bing.net/th?id=ODLS.1e67f861-d980-4c01-ba66-9450f90172f4&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid="
response = requests.get(url, headers=headers)

headers = response.headers  # <class 'requests.structures.CaseInsensitiveDict'>
assert headers['Content-Type'].split('/')[0] == 'image'
file_type = headers['Content-Type'].split('/')[1]

with open(f'bilibili_image.{file_type}', 'wb') as e:
    e.write(response.content)
