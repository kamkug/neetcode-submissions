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
        
        q = deque([root])
        result = []

        while q:
            q_len = len(q)
            rightmost = None

            for i in range(q_len):
                rightmost = q.popleft()

                if rightmost.left:
                    q.append(rightmost.left)
                
                if rightmost.right:
                    q.append(rightmost.right)
            
            result.append(rightmost.val)
        
        return result