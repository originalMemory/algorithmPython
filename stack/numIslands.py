#!/user/bin/env python3
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : numIslands
@author  : illusion
@desc    : 200. 岛屿数量 https://leetcode-cn.com/problems/number-of-islands/
@create  : 2021/6/5
"""


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        num = 0
        visited = [[False for n in range(len(grid[m]))] for m in range(len(grid))]
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                value = grid[m][n]
                if visited[m][n] or value == '0':
                    continue
                num += 1
                self.dfs_mark_visit(grid, m, n, visited)
        return num

    def dfs_mark_visit(self, grid: [[str]], m: int, n: int, visited: [[int]]):
        if m < 0 or m >= len(grid) or n < 0 or n >= len(grid[m]) or visited[m][n] or grid[m][n] == '0':
            return
        visited[m][n] = True
        self.dfs_mark_visit(grid, m - 1, n, visited)
        self.dfs_mark_visit(grid, m + 1, n, visited)
        self.dfs_mark_visit(grid, m, n - 1, visited)
        self.dfs_mark_visit(grid, m, n + 1, visited)

    def numIslands_length(self, grid: [[str]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        num = 0
        visited = [[False for n in range(len(grid[m]))] for m in range(len(grid))]
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                value = grid[m][n]
                if visited[m][n] or value == '0':
                    continue
                num += 1
                stack = [(m, n)]
                while len(stack):
                    m1, n1 = stack.pop()
                    if visited[m1][n1] or grid[m1][n1] == '0':
                        continue
                    visited[m1][n1] = True
                    if m1 > 0:
                        stack.append((m1 - 1, n1))
                    if m1 < len(grid) - 1:
                        stack.append((m1 + 1, n1))
                    if n1 > 0:
                        stack.append((m1, n1 - 1))
                    if n1 < len(grid[m1]) - 1:
                        stack.append((m1, n1 + 1))

        return num
