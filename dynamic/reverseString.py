# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : reverseString
@author  : illusion
@desc    : 
@create  : 2021/7/30 1:47 下午:20
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]):
        if not len(s):
            return
        last = len(s) - 1
        left = 0
        while left < last / 2:
            right = last - left
            s[left], tp = s[right], s[left]
            s[right] = tp
            left += 1


if __name__ == '__main__':
    s = Solution()
    li = ["h", "e", "l", "l", "o"]
    s.reverseString(li)
    print(li)
