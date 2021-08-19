# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : jump
@author  : illusion
@desc    : 45. 跳跃游戏 II https://leetcode-cn.com/problems/jump-game-ii/
@create  : 2021/6/8 1:47 下午:11
"""


class Solution:
    def jump(self, nums: [int]) -> int:
        if not len(nums):
            return 0
        dp = [9999999] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums):
                    break
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
