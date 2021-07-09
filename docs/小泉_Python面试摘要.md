# Python基础

> 合并2个列表，外加排序呢？
```python
li1 = [1, 5, 7, 9]
li2 = [2, 2, 6, 8]
for item in li2:
    li1.append(item)
li1.extend(li2) # [1, 5, 7, 9, 2, 2, 6, 8]
li1 += li2      # [1, 5, 7, 9, 2, 2, 6, 8]
li1.sort(reverse=False)          # [1, 2, 2, 5, 6, 7, 8, 9]
li1 = sorted(li1, reverse=False) # [1, 2, 2, 5, 6, 7, 8, 9]
```

> python中什么元素为False
0，""，[]、{}、()、None, False; 这些元素为False,可通过bool(var)测试
any(var_iter): 迭代器中有一个元素为真就为真
all(var_iter): 迭代器中所有的判断项返回都是真，结果才为真
```python
bool(()) # False
li = ['showme', '']
any(li)  # True
all(li)  # False
```

> zip()的使用？
```python
la = ('a', 'b')
lb = (1, 2)
ret = zip(la, lb)  # <zip object at 0x0000023E8A11FE00>
list(ret)    # [('a', 1), ('b', 2)]
dict(ret)    # {'a': 1, 'b': 2}

# 其它创建列表的方法
ret = dict([('a', 'b'), (1, 2)])    # {'a': 'b', 1: 2}
ret = dict([['a', 'b'], [1, 2]])    # {'a': 'b', 1: 2}
```

> 装饰器
```python
from functools import wraps

def wrapper(func):
    @wraps(func)
    def in_logic(*args, **kwargs):
        print("wraps info {}".format(func.__name__))
        func(*args, **kwargs)
    return in_logic

# @wrapper相当于real_logic=wrapper(real_logic)
@wrapper
def real_logic(msg):
    print("info is {}".format(msg))

real_logic("mesage") # real_logic函数名可以像变量一样赋值，赋值时不执行；加()就是执行函数
```
```python
class Rect:
    def __init__(self, area):
        self.__area = area
    
    @property   # @property修饰的方法操作类中的area私有属性
    def area(self):
        return self.__area
    
    @area.setter    # @方法名.setter
    def area(self, newvar):
        self.__area = newvar

    @area.deleter    # @方法名.setter
    def area(self):
        self.__area = 0

rect = Rect(30)
print("area：", rect.area)  # area： 30
rect.area = 90
print("area：", rect.area)  # area： 90
del rect.area
print("area：", rect.area)  # area： 0
```

> 迭代器与生成器



> re正则表达式

r表示需要原始字符串，不转义特殊字符
re.compile 将正则表达式编译成一个对象，以加快匹配速度并重复使用
re.match() 总是从字符串的开头匹配，返回对象需要用group()来显示
re.search() 对整个字符串进行搜索匹配，返回第一个匹配的字符串的匹配对象，返回对象需要用group()来显示
re.findall() 查找并返回所有匹配的对象，返回对象不需要用group()来显示
re.sub() 相当于字符串操作中的replace，比如 li = 'showme    showme\r\n'; ret = re.sub("(?isu)\r\n", "", li)

![img](%E5%B0%8F%E6%B3%89_Python%E9%9D%A2%E8%AF%95%E6%91%98%E8%A6%81.assets/20150807191845558.jpg)

```python
li = "<a>showme</a><a>showme</a>"
# 注意*或+后面跟着？表示非贪婪匹配，匹配到第一个符合条件的结尾即可
# (.*）贪婪匹配，会尽可能多的匹配
ret1 = re.findall(r"<a>(.*)</a>", li)  # ['showme</a><a>showme']
# （.*?）非贪婪匹配，会尽可能少匹配
ret1 = re.findall(r"<a>(.*?)</a>", li)  # ['showme', 'showme']

# 匹配电话号码，并排除尾号是4或1
tel = '18872548980'
ret = re.match('1\d{9}[^41]', tel)  # <re.Match object; span=(0, 11), match='18872548980'>

# (.*?)提取匹配的字符串
strs = '<div class="nam">showme</div>>中国<'
ret = re.findall(r'<div class=".*">.*?</div>>(.*?)<', strs)  # ['中国']

li = "showme, 中国，汉字"
ret = re.findall(r"[\u4e00-\u9fa5]+", li) # ['中国', '汉字']

# 匹配163.com的邮箱
ret = re.match(r"\w{4,20}@163\.com$", li)

# 匹配出<html><h1>showme</h1></html>
li = ["<html><h1>http://www.showme.cn</h1></html>", \
        "<html><h2>http://www.showme.cn</h1></html>"]
for item in li:
    ret = re.match(r"<(\w*)><(\w*)>(.*?)</\2></\1>", item)
    print(ret, ret.group()) #<re.Match object; span=(0, 43), match='<html><h1>http://www.showme.cn</h1></html>'> <html><h1>http://www.showme.cn</h1></html>

```

> 单例模式
```python
class Kfc(object):
    __instance = None

    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
```

> 列表推导式，字典推导式，生成器
```python
li = [i for i in range(10)]
print(li, type(li))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>

di = {k: random.randint(4, 8) for k in ['a', 'b', 'c', 'd']}
print(di, type(di))
# {'a': 8, 'b': 5, 'c': 5, 'd': 7} <class 'dict'>

ti = (i for i in range(10))
print(ti, type(ti))
# <generator object <genexpr> at 0x0000028F45B39C10> <class 'generator'>

# 按字符长度排序
li = ['abc', 'a', 'ac']
ret = sorted(li, key=lambda k:len(k)) # 或li.sort(key=len)
# ['a', 'ac', 'abc']
```
```python
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = [i for i in li if i % 2 == 1] # [1, 3, 5, 7, 9]

def is_odd(var):
    return var % 2 == 1
# filter将li中每一个元素使用函数处理返回True或False，并返回一个迭代器
ret = filter(is_odd, li)  # <filter object at 0x0000016B5E3B9820>
rut = list(ret)           # [1, 3, 5, 7, 9]
```

# Python数据结构与算法
部分算法可参考 https://cloud.tencent.com/developer/article/1466212
> 快速排序
```python
'''
1. 取一个元素target（第一个元素），让target归位
2. 列表左边的元素都比target小，右边的元素都比target大
3. 递归地完成排序
'''
def quick_sort(li, low, high):
    if low >= high:
        return li
    i = low
    j = high
    target = li[i]
    while i < j:
        while i < j and li[j] >= target:
            j -= 1
        li[i] = li[j]
        while i < j and li[i] <= target:
            i += 1
        li[j] = li[i]
    li[i] = target

    quick_sort(li, low, i - 1)
    quick_sort(li, i + 1, high)
    return li
```

> 归并排序
```python
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j +=1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    for i in range(low, high + 1):
        li[i] = li_tmp[i-low]

'''
1. 原始数组分段有序
2. T:nlog(n) S:n
'''
def merge_sort(li, low, high):
    mid = (low + high) // 2
    if low < high:
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)
    pass
```

> 堆排序 & topk
```python
def heap_adjust(li, low, high):
    temp = li[low]
    i = low
    j = 2 * i + 1

    while j <= high:
        if (j < high) and (li[j] < li[j + 1]):
            j += 1
        if temp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = temp

def heap_sort(li):
    n = len(li)

    # 1. 建堆
    for i in range((n - 1) >> 1, -1, -1):
        heap_adjust(li, i, n-1)

    # 2. 出数
    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        heap_adjust(li, 0, i - 1)


def topk(li, k): # 目前有点问题
    heap = li[0:k]    

    # 1. 建堆
    for i in range((k - 1) >> 1, -1, -1):
        heap_adjust(heap, i, k - 1)
        
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            heap_adjust(heap, 0, k-1)

    # 2. 出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap_adjust(heap, 0, i - 1)
    return heap
```

> 冒泡排序
```python
""" alt shift a
1. 相邻元素的对比交接，共进行len-1次趟
2. T:n*n
"""
def bubble_sort(li):
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        pass
```

> 选择排序
```python
"""
1. 选择排序仅记录最大值的位置，最后一次性交换
T:n*n
"""
def select_sort(li):
    for i in range(len(li) - 1, 0, -1):
        posm = 0
        for j in range(1, i + 1):
            if li[j] > li[posm]:
                posm = j
        if posm != i:
            li[i], li[posm] = li[posm], li[i]
```

> 二分查找
```python
"""
1. 前提:li是有序的列表
"""
def binary_search(li, data):
    mid = len(li) // 2
    if data < li[mid]:
        return binary_search(li[0:mid], data)
    elif data > li[mid]:
        return binary_search(li[mid + 1 :], data)
    else:
        return mid
```

> 回文
```python
"""
1. 回文数字或字符串的递归方式
"""
def hui_wen(li):
    if len(li) < 2:
        return True
    if li[0] != li[-1]:
        return False
    return hui_wen(li[1:-1])
```
> 去重
```python
def remove_repeat():
    a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
    a.sort() # [0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 7, 7, 8, 9, 10]
    print(a)

    last = a[-1]
    for i in range(len(a) - 2, -1, -1):
        if last == a[i]:
            del a[i]
        else:
            last = a[i]
    # [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
    pass

# 去除空格
li = "showme showme"
ret = li.replace(" ", "")  # showmeshowme

ret = list(li.split(" "))
rut = "".join(ret) # showmeshowme
```

> 其它杂集
```python
sum(range(1, 101)

import numpy as np
li = np.random.permutation(10) # 生成10个随机元素
```

# Python易错点

