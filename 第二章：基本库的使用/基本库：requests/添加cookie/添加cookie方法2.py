import requests.cookies


url = 'https://www.httpbin.org/get'

cookies = ("_gh_sess=K8uqU%2BNh5MtW2Vs5S5ASZ5qwUJPu7ThF5tJHTIoE9doYLvcJ5ug%2FOkPHeu5kKs0JQ%2BDip05"
           "57D1RC3tew3l8gWxJO4NM8yppecFopLZF%2BDHyXTvpsKgUs6yW1x5b%2FZwQ0soiJBHa7YTdDiDgU9RGe1GQ4JSfDRXJqA71RHks50DG"
           "2EWkwV0ilmd%2Fv2zqfwvz%2Fcxlm21%2B1M3cxzB4vfDjUE7VarYdEo%2FXF9Zi3JeWqYo%2FPNnJ7rzPLXOpt8%2BHjUQpuMEpu60N%2"
           "B6iW3kbgBurMjuE%2BVMkp7bGkbQfwBdQUYo4LXsJK716WqlDusqcbQqo8pXwyLoRkDyvinlmDRl7rpKkPcBJ8Ll1Uy%2BITySkZMHoKt"
           "iJO%2BLET1a4We3FARo5daZgVUn%2F%2BZQjauuqZdLexMez5LW2HOb9utxXE7LBQVPW3eDeRcwxGDiq2PrSBWmFRIvSXDN1poZ5OXBX00"
           "OqZRHqsPHXpa7jrJR0Bgpeojk3hZRJCEhBCfucYMcAn6lbj7MQ7F7N88YBIHbDy2NamHC4j1t3LhQWFTOlQac8l4o0FV2V2U9StSA%3D"
           "%3D--oVba8aDh7O4HTO0s--63CAfPj1wd%2BFLxuWlybjSA%3D%3D; path=/; SameSite=Lax")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 "
                  "Safari/537.36",
}
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    k, v = cookie.split('=', 1)
    jar.set(k, v)
response = requests.get(url, headers=headers, cookies=jar)
print(response.request.headers)
