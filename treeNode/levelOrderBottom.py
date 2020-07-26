#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : levelOrderBottom
@author  : illusion
@desc    : 107. 二叉树的层次遍历 II https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
@create  : 2020-07-26 15:55:32
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        result = self.levelOrder(root)
        result.reverse()
        return result

    def levelOrder(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        queue = [root]
        while len(queue):
            list = []
            for i in range(len(queue)):
                level = queue[0]
                queue = queue[1:]
                list.append(level.val)
                if level.left:
                    queue.append(level.left)
                if level.right:
                    queue.append(level.right)
            result.append(list)
        return result
