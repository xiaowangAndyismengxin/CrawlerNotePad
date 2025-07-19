import json


data = {"name": "王伟", "sex": "男", "age": 114}
with open("data.json", "w+", encoding="UTF-8") as f:
    json.dump(data, f, indent=2)
    print(f.tell())
    f.seek(0, 0)
    print(len(f.read()))
    f.seek(0, 0)
    print(f.read())
    # load无法正确读取
with open("data.json") as f:
    print(json.load(f, strict=False))
