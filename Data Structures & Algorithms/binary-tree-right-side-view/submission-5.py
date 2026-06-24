# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [(root, 0)]
        res = []

        while stack:
            for i in range(0, len(stack)):
                node, depth = stack.pop()
                
                if depth == len(res):
                    res.append(node.val)
                
                if node.left:
                    stack.append((node.left, depth+1))
                
                if node.right:
                    stack.append((node.right, depth+1))
        
        return res
