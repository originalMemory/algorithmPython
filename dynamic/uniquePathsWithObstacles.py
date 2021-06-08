# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : uniquePathsWithObstacles
@author  : illusion
@desc    : 63. 不同路径 II https://leetcode-cn.com/problems/unique-paths-ii/
@create  : 2021/6/8 1:36 下午:40
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if not len(obstacleGrid) or not len(obstacleGrid[0]):
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0
        col_length = len(obstacleGrid[0])
        dp = []
        has_obs = False
        for col in range(col_length):
            if obstacleGrid[0][col] == 1:
                has_obs = True
            if has_obs:
                dp.append(0)
            else:
                dp.append(1)
        for row in range(1, len(obstacleGrid)):
            for col in range(col_length):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
