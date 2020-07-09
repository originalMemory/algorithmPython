import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSinglePath(root)
        return self.maxLength

    maxLength = -sys.maxsize - 1

    def maxSinglePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftPath = self.maxSinglePath(root.left)
        rightPath = self.maxSinglePath(root.right)
        cur_sum = max(max(leftPath, rightPath) + root.val, root.val)
        self.maxLength = max(self.maxLength, max(cur_sum, leftPath + rightPath + root.val))
        return cur_sum

s = Solution()
n1 = TreeNode(9)
n2 = TreeNode(6)
n1.left = n2
n3 = TreeNode(-3)
n1.right = n3
n4 = TreeNode(-6)
n3.left = n4
n5 = TreeNode(2)
n3.right = n5
n6 = TreeNode(2)
n5.left = n6
n7 = TreeNode(-6)
n6.left = n7
n8 = TreeNode(-6)
n6.right = n8
n9 = TreeNode(-6)
n7.left = n9
print(s.maxPathSum(n1))