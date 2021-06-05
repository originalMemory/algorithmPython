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

from stack import inorderTraversal, cloneGraph
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

    def test_clone_graph(self):
        s = cloneGraph.Solution()
        n1 = cloneGraph.Node(val=1)
        n2 = cloneGraph.Node(val=2)
        n3 = cloneGraph.Node(val=3)
        n4 = cloneGraph.Node(val=4)
        n1.neighbors.append(n2)
        n1.neighbors.append(n4)
        n2.neighbors.append(n1)
        n2.neighbors.append(n3)
        n3.neighbors.append(n2)
        n3.neighbors.append(n4)
        n4.neighbors.append(n1)
        n4.neighbors.append(n3)
        res = s.cloneGraph(n1)


if __name__ == '__main__':
    unittest.main()
