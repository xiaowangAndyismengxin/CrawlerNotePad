import re


s = """2025-1-25
2025-1-26
2025-1-28
2025-1-1
2025-1-17
2025-1-10y"""
pattern = re.compile(r'(\d{4})-(\d{1,2})-(\d{1,2})')
content = re.sub(pattern, r'\2-\3-\1', s)
print(content)
