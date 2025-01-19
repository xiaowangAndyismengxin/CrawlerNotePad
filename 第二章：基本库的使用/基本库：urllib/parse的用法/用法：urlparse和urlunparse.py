from urllib.parse import urlparse, urlunparse


url = "https://www.baidu.com/index.html;user?id=5#comment"
result = urlparse(url, scheme="http", allow_fragments=True)
print(result)  # <class 'urllib.parse.ParseResult'>
print(result[1])
print(result.netloc)
print(result.fragment)
print(result[-1])

# 复现
# parse_list = [*result]
parse_list = [result.scheme, result.netloc, result.path, result.params, result.query, result.fragment]
result2 = urlunparse(parse_list)
print(result2)
