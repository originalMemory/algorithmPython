# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : tribonacci
@author  : illusion
@desc    : 1137. 第 N 个泰波那契数 https://leetcode-cn.com/problems/n-th-tribonacci-number/
@create  : 2021/8/20 1:19 下午:56
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        动态规划法
        :param n:
        :return:
        """
        if n == 0:
            return 0
        t0 = 0
        t1 = 1
        t2 = 1
        for i in range(0, n - 2):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2

    def tribonacci2(self, n: int) -> int:
        """
        矩阵快速幂算法，参考 https://leetcode-cn.com/circle/article/8uRHgu/
        :param n:
        :return:
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        m = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        k = n - 2
        while k:
            if k & 1:
                ans = self.matrix_mltiply(ans, m)
            m = self.matrix_mltiply(m, m)
            k >>= 1
        return ans[0][0] + ans[0][1]

    def matrix_mltiply(self, m, n):
        """
        矩阵乘法
        :param m:
        :param n:
        :return:
        """
        n_row = len(m)
        n_col = len(n[0])
        n_tmp = len(m[0])
        res = [[0 for _ in range(n_col)] for _ in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                for x in range(n_tmp):
                    res[i][j] += m[i][x] * n[x][j]
        return res


if __name__ == '__main__':
    print(Solution().tribonacci2(4))
