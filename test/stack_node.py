# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : stack_node
@author  : illusion
@desc    : 
@create  : 2021/6/1 1:27 下午:03
"""
import unittest

from stack import inorderTraversal
from stack.inorderTraversal import TreeNode


class StackNodeTest(unittest.TestCase):
    def test_inorder_traversal(self):
        s = inorderTraversal.Solution()

        node = TreeNode(1)
        node.right = TreeNode(2)
        node.right.left = TreeNode(3)
        self.assertEqual(s.dfs(node), [1, 3, 2])
        self.assertEqual(s.iteration(node), [1, 3, 2])
        self.assertEqual(s.morries(node), [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
