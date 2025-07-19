from urllib.parse import quote, unquote  # 编码与解码
from urllib.parse import urlparse, parse_qs


question = "壁纸"
url = "https://www.baidu.com/s?wd=" + quote(question)
print(url)

# 复现
query = urlparse(url).query
q = unquote(parse_qs(query)["wd"][0])
print(q)
