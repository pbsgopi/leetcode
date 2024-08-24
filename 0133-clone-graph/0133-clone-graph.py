"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap={}
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            copy=Node(node.val)
            hashmap[node]=copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        if node:
            return dfs(node)
        None