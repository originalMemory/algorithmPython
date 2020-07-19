#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : levelOrder
@author  : illusion
@desc    : 
@create  : 2020-07-19 20:01:03
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
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
