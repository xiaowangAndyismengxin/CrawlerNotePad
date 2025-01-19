from urllib.parse import urlsplit, urlunsplit


url = "https://www.baidu.com;user?id=5#comment"
result = urlsplit(url, scheme="http", allow_fragments=True)
print(result)  # <class 'urllib.parse.ParseResult'>
print(result[1])
print(result.netloc)
print(result.fragment)
print(result[-1])

# 复现
# parse_list = [*result]
parse_list = [result.scheme, result.netloc, result.path, result.query, result.fragment]
result2 = urlunsplit(parse_list)
print(result2)
