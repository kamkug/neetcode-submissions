"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        o_to_n = {}
        q = deque([node])
        o_to_n[node] = Node(node.val)

        while q:
            curr = q.popleft()

            for neigh in curr.neighbors:
                if neigh not in o_to_n:
                    o_to_n[neigh] = Node(neigh.val)
                    q.append(neigh)
                o_to_n[curr].neighbors.append(o_to_n[neigh])
        
        return o_to_n[node]
