# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : inorderTraversal
@author  : illusion
@desc    : 94. 二叉树的中序遍历 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
@create  : 2021/6/1 1:26 下午:22
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        return [0]

    def dfs(self, root: TreeNode) -> [int]:
        if root is None:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left + [root.val] + right

    def iteration(self, root: TreeNode) -> [int]:
        stack = []
        if not root:
            return stack
        res = []
        node = root
        while node or len(stack):
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def morries(self, root: TreeNode) -> [int]:
        node = root
        res = []
        while node:
            if node.left:
                # pre 是当前 node 往左走一步，然后一直向右走到尽头
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                # 令 pre 的右结点指向 node ，继续遍历左子树
                if not pre.right:
                    pre.right = node
                    node = node.left
                # 说明左子树访问完了，需要断开连接
                else:
                    pre.right = None
                    res.append(node.val)
                    node = node.right
            # 没有左结点时直接访问右结点
            else:
                res.append(node.val)
                node = node.right
        return res



