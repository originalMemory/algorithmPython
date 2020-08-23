#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : insertIntoBST
@author  : illusion
@desc    : 701. 二叉搜索树中的插入操作 https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
@create  : 2020-08-23 15:20:36
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
            return root
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
