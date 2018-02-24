# coding: utf-8
import json


def executeJson():
    data = {
        'num': 1,
        'name': 'json test',
        'url': 'http://www.runoob.com'
    }

    json_str = json.dumps(data)
    print("[executeJson] normal data：", repr(data))
    print("[executeJson] json object：", json_str)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: {0}, data2['url']: {1}".format(
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
    executeJson()
    pass
