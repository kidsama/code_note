# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。

# json string -> json.loads() -> python object
# python object -> json.dumps() -> json string

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)