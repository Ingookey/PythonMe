# coding: utf-8
# demoJson.py: used for json.

import json


def testJson():
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    json_str = json.dumps(data)
    print("Python 原始数据：", repr(data))
    print("JSON 对象：", json_str)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: {}, data2['url']: {}".format(
        data2['name'], data2['url']))

    # 对文件写入Json数据
    with open('../config/testJson.json', 'w') as f:
        json.dump(data, f)

    # 通过文件读取Json数据
    with open('../config/testJson.json', 'r') as f:
        data = json.load(f)
        print(data)
    pass


if __name__ == '__main__':
    testJson()
    pass
