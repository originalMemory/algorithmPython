# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : list_node
@author  : illusion
@desc    : 
@create  : 2021/2/3 1:37 下午:59
"""
from listNode.model import ListNode
from listNode import linkedListCycle, palindromeLinkedList
import unittest


class ListNodeTest(unittest.TestCase):
    def test_linked_list_cycle(self):
        s = linkedListCycle.Solution()

        node = ListNode(3)
        node.next = ListNode(2)
        node.next.next = ListNode(0)
        end_node = ListNode(-4)
        end_node.next = node.next
        node.next.next.next = end_node
        self.assertEqual(s.hasCycle(node), True)

        node2 = ListNode(1)
        self.assertEqual(s.hasCycle(node2), False)

    def test_is_palindrome(self):
        s = palindromeLinkedList.Solution()

        node1 = ListNode(1)
        node1.next = ListNode(2)
        self.assertEqual(s.isPalindrome(node1), False)

        node2 = ListNode(1)
        node2.next = ListNode(2)
        node2.next.next = ListNode(2)
        node2.next.next.next = ListNode(1)
        self.assertEqual(s.isPalindrome(node2), True)


if __name__ == '__main__':
    unittest.main()
