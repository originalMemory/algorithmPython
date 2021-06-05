#!/user/bin/env python3
# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : cloneGraph
@author  : illusion
@desc    : 133. 克隆图 https://leetcode-cn.com/problems/clone-graph/
@create  : 2021/6/5
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = {}
        return self.dfs(node, visited)

    def dfs(self, node: 'Node', visited):
        if node in visited:
            return visited[node]
        new_node = Node(val=node.val)
        visited[node] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.dfs(neighbor, visited))
        return new_node
