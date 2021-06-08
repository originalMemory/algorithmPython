# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : canJump
@author  : illusion
@desc    : 55. 跳跃游戏 https://leetcode-cn.com/problems/jump-game/
@create  : 2021/6/7 1:56 下午:08
"""


class Solution:
    def canJump(self, nums: [int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break
        return dp[-1]

    def canJump2(self, nums: [int]) -> bool:
        right_max = 0
        for i in range(len(nums)):
            if i > right_max:
                break
            if i + nums[i] >= len(nums) - 1:
                return True
            right_max = max(right_max, i + nums[i])
        return False


if __name__ == '__main__':
    print(Solution().canJump2([2, 3, 1, 1, 4]))
