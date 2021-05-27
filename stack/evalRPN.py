# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : evalRPN
@author  : illusion
@desc    : 150. 逆波兰表达式求值 https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
@create  : 2021/5/27 1:22 下午:54
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(int(token))
                continue
            if len(stack) < 2:
                continue
            n2 = stack.pop()
            n1 = stack.pop()
            if token == '+':
                stack.append(n1 + n2)
            elif token == '-':
                stack.append(n1 - n2)
            elif token == '*':
                stack.append(n1 * n2)
            elif token == '/':
                stack.append(int(n1 / n2))
        return stack.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
