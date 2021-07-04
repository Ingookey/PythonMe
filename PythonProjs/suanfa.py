import os
import sys
import re
import random
import pdb
import numpy as np


def test():
    a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
    a.sort()

    last = a[-1]
    for i in range(len(a) - 2, -1, -1):
        if last == a[i]:
            del a[i]
        else:
            last = a[i]


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if False:
        li = np.random.permutation(10)
        print("list.pre {}".format(li))
        print(sum(range(1, 101)))

        strs = '<div class="nam">old</div>>new<'
        result = re.findall(r'<div class=".*">.*?</div>>(.*?)<', strs)
        print(result)
    
        li = "uis ui io uis ui s"
        print(li.count('ui'))

        tel = '13488951877'
        ret = re.match('1\d{9}[0-3,5-6,8-9]', tel)
        print(ret)


        li = ["<html><h1>http://www.itcast.cn</h1></html>", "<html><h1>http://www.itcast2.cn</h1></html>"]
        for item in li:
            ret = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>", item)
            print(ret)
    
