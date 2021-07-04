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

> 迭代器与生成器



> re正则表达式

re.compile是将正则表达式编译成一个对象，以加快匹配速度并重复使用
r表示需要原始字符串，不转义特殊字符

![img](%E5%B0%8F%E6%B3%89_Python%E9%9D%A2%E8%AF%95%E6%91%98%E8%A6%81.assets/20150807191845558)

```python
li = "<a>showme</a><a>showme</a>"
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

> 列表推导式

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

