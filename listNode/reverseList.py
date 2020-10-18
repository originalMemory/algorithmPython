#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : reverseList
@author  : illusion
@desc    : 206. 反转链表 https://leetcode-cn.com/problems/reverse-linked-list/
@create  : 2020-10-18 15:20:14
"""
from listNode.model import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = None
        while head:
            tp, head.next = head.next, pre
            pre, head = head, tp
        return pre

n3 = ListNode(3)
n2 = ListNode(2)
n2.next = n3
n1 = ListNode(1)
n1.next = n2
s = Solution()
s.reverseList(n1)
