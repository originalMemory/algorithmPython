#!/user/bin/env python
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : reorderList
@author  : illusion
@desc    : 143. 重排链表 https://leetcode-cn.com/problems/reorder-list/
@create  : 2020-12-06 23:12:41
"""
from listNode.model import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        # 找到中点
        slow = head
        fast = head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        cur = slow.next
        slow.next = None

        # 反转后半部分
        pre = None
        while cur:
            tp, cur.next = cur.next, pre
            pre, cur = cur, tp

        # 重新合并两段
        left = head
        right = pre
        while left and right:
            tp_right = right.next
            right.next, left.next = left.next, right
            left, right = right.next, tp_right
        return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
s = Solution()
r = s.reorderList(l)
r.print()
