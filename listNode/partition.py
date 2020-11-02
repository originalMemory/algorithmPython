# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : partition
@author  : illusion
@desc    : 86. 分隔链表 https://leetcode-cn.com/problems/partition-list/
@create  : 2020/11/2 1:49 下午:26
"""
from listNode.model import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head_dummy = ListNode(0)
        tail_dummy = ListNode(0)
        head_dummy.next = head
        head = head_dummy
        tail = tail_dummy
        while head.next:
            if head.next.val < x:
                head = head.next
            else:
                tp, head.next = head.next, head.next.next
                tail.next, tail = tp, tp
        tail.next = None
        head.next = tail_dummy.next
        return head_dummy.next


l = ListNode(1)
l.next = ListNode(4)
l.next.next = ListNode(3)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(2)

s = Solution()
s.partition(l, 3)
