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
        o_to_n[node] = Node(node.val)
        stack = [node]

        while stack:
            curr_node = stack.pop()

            for neigh in curr_node.neighbors:
                if neigh not in o_to_n:
                    o_to_n[neigh] = Node(neigh.val)
                    stack.append(neigh)
                
                print(f'{o_to_n[curr_node].val} get {o_to_n[neigh].val} as a neighbor')
                o_to_n[curr_node].neighbors.append(o_to_n[neigh])
            
            print()
            print(20*"=")

        return o_to_n[node]



        