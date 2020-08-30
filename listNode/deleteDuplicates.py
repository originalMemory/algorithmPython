#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : deleteDuplicates
@author  : illusion
@desc    : 82. 删除排序链表中的重复元素 II https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
@create  : 2020-08-30 16:11:21
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        new_head = ListNode(-1)
        new_head.next = head
        now = new_head
        while now.next and now.next.next:
            if now.next.val == now.next.next.val:
                repeat_val = now.next.val
                while now.next and now.next.val == repeat_val:
                    now.next = now.next.next
            else:
                now = now.next
        return new_head.next
