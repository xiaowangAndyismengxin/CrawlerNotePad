import json


data = {
    'name': '王伟',
    'sex': '男',
    'age': 114
}
# Help on built-in function seek:
#
# seek(cookie, whence=0, /) method of _io.TextIOWrapper instance
#     Set the stream position, and return the new stream position.
#
#       cookie
#         Zero or an opaque number returned by tell().
#       whence
#         The relative position to seek from.
#
#     Four operations are supported, given by the following argument
#     combinations:
#
#     - seek(0, SEEK_SET): Rewind to the start of the stream.
#     - seek(cookie, SEEK_SET): Restore a previous position;
#       'cookie' must be a number returned by tell().
#     - seek(0, SEEK_END): Fast-forward to the end of the stream.
#     - seek(0, SEEK_CUR): Leave the current stream position unchanged.
#
#     Any other argument combinations are invalid,
#     and may raise exceptions.
with open('data.json', 'w+', encoding='UTF-8') as f:
    json.dump(data, f, indent=2)
    print(f.tell())
    f.seek(0, 0)
    print(len(f.read()))
    f.seek(0, 0)
    print(f.read())
    # load无法正确读取
