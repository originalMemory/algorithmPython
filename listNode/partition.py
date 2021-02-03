#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : partition
@author  : illusion
@desc    : 148. 排序链表 https://leetcode-cn.com/problems/sort-list/
@create  : 2020-11-29 15:19:29
"""
from listNode.model import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head)

    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow

    def merge_list(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(-1)
        cur = new_head
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
        return new_head.next

    def merge_sort(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.find_middle(head)
        tail = mid.next
        mid.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(tail)
        return self.merge_list(left, right)


l = ListNode(4)
l.next = ListNode(2)
l.next.next = ListNode(1)
l.next.next.next = ListNode(3)
s = Solution()
result = s.sortList(l)
print(result)