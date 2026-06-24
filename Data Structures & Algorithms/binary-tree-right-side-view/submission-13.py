# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [(root, 0)]
        result = []

        while stack:
            stack_len = len(stack)

            for i in range(stack_len):
                node, depth = stack.pop()

                if depth == len(result):
                    result.append(node.val)
                
                if node.left:
                    stack.append((node.left, depth+1))
                
                if node.right:
                    stack.append((node.right, depth+1))
        
        return result
