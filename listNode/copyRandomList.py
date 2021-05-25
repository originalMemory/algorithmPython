# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : copyRandomList
@author  : illusion
@desc    : 138. 复制带随机指针的链表 https://leetcode-cn.com/problems/copy-list-with-random-pointer/
@create  : 2021/5/25 1:34 下午:17
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None
        cur = head
        while cur:
            copy_node = Node(cur.val)
            tmp, cur.next = cur.next, copy_node
            copy_node.next = tmp
            cur = tmp
        new_head = head.next
        cur = head
        while cur:
            next_node = cur.next
            if cur.random:
                next_node.random = cur.random.next
            cur = next_node.next
            if next_node.next:
                next_node.next = next_node.next.next
        return new_head


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
n2.random = n1

s = Solution()
print(s.copyRandomList(n1))
