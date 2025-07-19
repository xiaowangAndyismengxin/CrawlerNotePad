from urllib.parse import urlencode, parse_qs, parse_qsl


params = {"name": "Kimi", "comment": ["Very reliable", "Good_Helper"]}
url = "https://www.example.com"
new_url = url + "?" + urlencode(params, doseq=True)
print(new_url)

# 反序列化
query = new_url.split("?")[1]
print(query)
print(parse_qs(query))
print(parse_qsl(query))
