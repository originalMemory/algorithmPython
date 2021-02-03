#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : reverseBetween
@author  : illusion
@desc    : 92. 反转链表 II https://leetcode-cn.com/problems/reverse-linked-list-ii/
@create  : 2020-10-25 17:28:10
"""
from listNode.model import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        newHead = ListNode(-1)
        newHead.next = head
        begin = newHead  # m-1 处
        # 遍历到逆转的起来
        i = 1
        while i < m:
            begin, i = begin.next, i + 1
        cur = begin.next
        start = begin.next # m 处
        pre = None
        while i <= n:
            tp, cur.next = cur.next, pre
            pre, cur, i = cur, tp, i + 1
        begin.next = pre
        if start:
            start.next = cur
        return newHead.next


s = Solution()
n5 = ListNode(5)
n4 = ListNode(4)
n4.next = n5
n3 = ListNode(3)
n3.next = n4
n2 = ListNode(2)
n2.next = n3
n1 = ListNode(1)
n1.next = n2
s = Solution()
r: list = s.reverseBetween(n1, 2, 4)
string = "["
if r:
    string += str(r.val)
    r = r.next
    while r:
        string += f", {r.val}"
        r = r.next
string += ']'
print(string)
