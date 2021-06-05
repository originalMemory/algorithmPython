#!/user/bin/env python3
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : largestRectangleArea
@author  : illusion
@desc    : 84. 柱状图中最大的矩形 https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
@create  : 2021/6/5
"""


class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        st = [0]  # 增量栈
        heights = [0] + heights + [0]
        max_area = 0
        for i in range(len(heights)):
            # 下降时计算前面的面积
            while heights[i] < heights[st[-1]]:
                # 计算 st 最后1个的面积
                cur_width = heights[st.pop()]
                area = cur_width * (i - st[-1] - 1)
                max_area = max(max_area, area)
            st.append(i)
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 0, 2]))
