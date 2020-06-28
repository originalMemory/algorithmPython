# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        depth = (leftDepth if leftDepth > rightDepth else rightDepth) + 1
        return depth
