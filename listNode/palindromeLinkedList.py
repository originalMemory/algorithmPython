# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : palindromeLinkedList
@author  : illusion
@desc    : 234. 回文链表 https://leetcode-cn.com/problems/palindrome-linked-list/
@create  : 2021/2/7 1:35 下午:35
"""
from listNode.model import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse(slow.next)
        second_half_start = second_half
        first_half = head
        result = True
        while first_half and second_half:
            if first_half.val != second_half.val:
                result = False
                break
            first_half, second_half = first_half.next, second_half.next
        slow.next = self.reverse(second_half_start)
        return result

    def reverse(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            tmp, head.next = head.next, pre
            pre, head = head, tmp
        return pre
