#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : isValidBST
@author  : illusion
@desc    : 98. 验证二叉搜索树 https://leetcode-cn.com/problems/validate-binary-search-tree/
@create  : 2020-08-09 23:50:01
"""

import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.inOrder(root, -sys.maxsize - 1, sys.maxsize)

    def inOrder(self, root: TreeNode, left_max, right_min):
        if not root:
            return True
        if root.val <= left_max or root.val >= right_min:
            return False
        return self.inOrder(root.left, left_max, root.val) and self.inOrder(root.right, root.val, right_min)
