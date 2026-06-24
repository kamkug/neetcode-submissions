# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def inner(node: TreeNode) -> bool:
            nonlocal k, res

            if not node:
                return False
            
            if inner(node.left):
                return True
            
            k -= 1
            if k == 0:
                res = node.val
                return True 
            
            return inner(node.right)
        
        inner(root)
        return res
