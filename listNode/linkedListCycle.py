# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : linkedListCycle
@author  : illusion
@desc    : 141. 环形链表 https://leetcode-cn.com/problems/linked-list-cycle/
@create  : 2021/2/3 1:35 下午:45
"""
from listNode.model import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
