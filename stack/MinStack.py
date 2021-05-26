# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : MinStack
@author  : illusion
@desc    : 155. 最小栈 https://leetcode-cn.com/problems/min-stack/
@create  : 2021/5/26 1:38 下午:22
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not len(self.min):
            self.min.append(val)
            return
        last_min = self.min[-1]
        if val < last_min:
            self.min.append(val)
        else:
            self.min.append(last_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
