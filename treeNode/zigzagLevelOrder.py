#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : zigzagLevelOrder
@author  : wuhoubo
@desc    : 
@create  : 2020-07-30 13:26:24
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        queue = [root]
        need_reverse = False
        while len(queue):
            next_list = []
            for i in range(len(queue)):
                node = queue.pop(0)
                next_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if need_reverse:
                next_list = next_list[::-1]
                need_reverse = False
            else:
                need_reverse = True
            result.append(next_list)
        return result


root = TreeNode(3)
root.left = TreeNode(9)
node2 = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)
root.right = node2

s = Solution()
print(s.zigzagLevelOrder(root))
