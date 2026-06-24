"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        o_to_n = {}

        def dfs(node):
            if node in o_to_n:
                return o_to_n[node]
    
            o_to_n[node] = Node(node.val)

            for neigh in node.neighbors:
                o_to_n[node].neighbors.append(dfs(neigh))

            return o_to_n[node]

        dfs(node)
        
        return o_to_n[node]
            
