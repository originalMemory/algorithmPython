# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # https://leetcode-cn.com/problems/balanced-binary-tree/
    def isBalanced(self, root: TreeNode) -> bool:
        return self.maxDepth(root) >= 0

    def maxDepth(self, root: TreeNode) -> bool:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if leftDepth == -1 or rightDepth ==  -1 or abs(leftDepth - rightDepth) > 1:
            return -1
        else:
            return max(leftDepth, rightDepth) + 1
