# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : heap_sort
@author  : illusion
@desc    :  堆排序
@create  : 2021/6/7 1:25 下午:37
"""


class Solution:
    def heapSort(self, nodes: [int]) -> [int]:
        length = len(nodes)
        for i in range(length // 2 - 1, -1, -1):
            self.sink(nodes, i, length)
        for i in range(length - 1, -1, -1):
            nodes[0], nodes[i] = nodes[i], nodes[0]
            self.sink(nodes, 0, i)
        return nodes

    def sink(self, nodes: [int], i: int, length: int):
        while True:
            l = i * 2 + 1
            r = i * 2 + 2
            big_index = i
            if l < length and nodes[l] > nodes[big_index]:
                big_index = l
            if r < length and nodes[r] > nodes[big_index]:
                big_index = r
            if big_index == i:
                break
            nodes[i], nodes[big_index] = nodes[big_index], nodes[i]
            i = big_index

    def quickSort(self, nodes: [int]):
        self.quick(nodes, 0, len(nodes) - 1)
        return nodes

    def quick(self, nodes: [int], start, end):
        if start < end:
            pivot = self.partition(nodes, start, end)
            self.quick(nodes, start, pivot - 1)
            self.quick(nodes, pivot + 1, end)

    def partition(self, nodes: [int], start, end):
        p = nodes[end]
        i = start
        for j in range(start, end):
            if nodes[j] < p:
                nodes[i], nodes[j] = nodes[j], nodes[i]
                i += 1
        nodes[i], nodes[end] = nodes[end], nodes[i]
        return i

    def mergeSort(self, nodes: [int]):
        if len(nodes) <= 1:
            return nodes
        mid = len(nodes) // 2
        left = self.mergeSort(nodes[0: mid])
        right = self.mergeSort(nodes[mid:])
        print(left, right)
        res = self.merge(left, right)
        return res

    def merge(self, left, right):
        res, l, r = [], 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        while l < len(left):
            res.append(left[l])
            l += 1
        while r < len(right):
            res.append(right[r])
            r += 1
        return res


if __name__ == '__main__':
    print(Solution().heapSort([4, 10, 3, 5, 1]))
    print(Solution().quickSort([4, 10, 3, 5, 1]))
    print(Solution().mergeSort([4, 10, 3, 5, 1]))
