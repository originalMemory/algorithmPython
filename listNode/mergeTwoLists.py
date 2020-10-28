# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : mergeTwoLists
@author  : illusion
@desc    : 21. 合并两个有序链表 https://leetcode-cn.com/problems/merge-two-sorted-lists/
@create  : 2020/10/28 1:06 下午:11
"""
from listNode.model import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode(-1)
        cur = newHead
        while l1 or l2:
            while l1:
                if l2 and l1.val > l2.val:
                    break
                cur.next = l1
                cur, l1 = cur.next, l1.next
            while l2:
                if l1 and l2.val > l1.val:
                    break
                cur.next = l2
                cur, l2 = cur.next, l2.next
        return newHead.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode(-1)
        cur = newHead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        while l1:
            cur.next, l1 = l1, l1.next
            cur = cur.next
        while l2:
            cur.next, l2 = l2, l2.next
            cur = cur.next
        return newHead.next


l1 = ListNode(-9)
l1.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(7)
s = Solution()
s.mergeTwoLists2(l1, l2)
