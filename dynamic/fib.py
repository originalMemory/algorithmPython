# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : fib
@author  : illusion
@desc    : 509. 斐波那契数 https://leetcode-cn.com/problems/fibonacci-number/
@create  : 2021/8/20 1:16 下午:20
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp1 = 0
        dp2 = 1
        for i in range(2, n + 1):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2


if __name__ == '__main__':
    print(Solution().fib(4))
