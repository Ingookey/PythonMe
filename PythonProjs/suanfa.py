import os
import sys
import random
import pdb
import numpy as np


def test():
    if False:
        a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
        a.sort()

        last = a[-1]
        for i in range(len(a) - 2, -1, -1):
            print(a[i])
            pdb.set_trace()
            if last == a[i]:
                del a[i]
            else:
                last = a[i]
            print(a)
        pass

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

'''
1. 
'''
def binary_search(li, data):
    mid = len(li) // 2
    if data < li[mid]:
        return binary_search(li[0:mid], data)
    elif data > li[mid]:
        return binary_search(li[mid + 1 :], data)
    else:
        return mid


def hui_wen(li):
    if len(li) < 2:
        return True
    if li[0] != li[-1]:
        return False
    return hui_wen(li[1:-1])


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
            j = 2 * i +1
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


def topk(li, k):
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


if __name__ == '__main__':
    li = np.random.permutation(10)
    print("list.pre {}".format(li))
    #quick_sort(li, 0, len(li)-1)
    bubble_sort(li)
    print("list.post {}".format(li))

    #print(binary_search(li, 5), 5/2, 5//2)
